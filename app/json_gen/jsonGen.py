# coding: latin-1
###############################################################################
# Copyright (c) 2026 European Commission
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
###############################################################################
import base64
from dataclasses import asdict, is_dataclass
import datetime
from io import StringIO
import io
import re
from dateutil.relativedelta import relativedelta
from flask import send_file
import json_gen.models as JSON
from app.app_config.xml_config import ConfXML as confxml
from signxml import XMLSigner, algorithms, methods, namespaces
import json

from app_config.config import ConfService as cfgserv
from cryptography.hazmat.primitives import serialization
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import hashlib
import xml.etree.ElementTree as ET
from cryptography.hazmat.primitives.serialization import Encoding
import app.EJBCA_and_DB_func as func
from app.json_gen.jadessigner import jadesigner

def parse_json_field(field):
    try:
        return json.loads(field) if isinstance(field, str) else field
    except json.JSONDecodeError:
        return field
    
def json_gen_json(user_info, dictFromDB_trusted_lists, tsp_data, service_data,service_history, tsl_id, log_id):

    der_data=open(cfgserv.cert_UT, "rb").read()
    cert_der = x509.load_der_x509_certificate(der_data, backend=default_backend())
    cert = cert_der.public_bytes(encoding=serialization.Encoding.PEM)

    pem_str = cert.decode('utf-8')
    cert_cleaned = ''.join(line for line in pem_str.splitlines() if "CERTIFICATE" not in line)

    check = func.get_old_cert(tsl_id, log_id)
    aux = 0
    if(check is not None):
        for each in check:
            if(each["cert"] != cert_cleaned):
                aux = 1
    else:
        if(aux != 1):
            func.insert_old_cert(cert_cleaned, tsl_id, log_id)
    
    LoTEType=dictFromDB_trusted_lists["TSLType"]
    
    #root=JSON.LoTE()

    # root.set_TSLTag("http://uri.etsi.org/19612/TSLTag")
    # root.set_Id("TrustServiceStatusList")

    #schemeInfo = JSON.ListAndSchemeInformation()

    # schemeInfo.LoTEVersionIdentifier=confxml.TLSVersionIdentifier
    # schemeInfo.LoTESequenceNumber=dictFromDB_trusted_lists["SequenceNumber"] + 1
    # schemeInfo.LoTEType=confxml.TSLType["EU"]

    #schemeOperatorName

    schemeOName = list()

    #for cycle
    op_name = parse_json_field(user_info["operator_name"])
    for item in op_name:
        schemeOName.append(JSON.MultiLangString(item['lang'], item["text"]))

    #schemeInfo.SchemeOperatorName=schemeOName

    #Scheme Operator Address
    

    eletronic=JSON.ElectronicAddress()

    #for cycle
    EletronicAddress = parse_json_field(user_info["EletronicAddress"])
    for item in EletronicAddress:
        eletronic.append(JSON.NonEmptyMultiLangURI(item['lang'],item["URI"]))
    #----------------------------------------------------#

    PostalAdresses_list=list()

    #for cycle for postal address
    postal = parse_json_field(user_info["postal_address"])
    for item in postal:
        postal=JSON.PostalAddress(
            lang=item['lang'],
            Country=item["CountryName"],
            StreetAddress=item["StreetAddress"],
            Locality=item["Locality"],
            StateOrProvince=item["StateOrProvince"],
            PostalCode=item["PostalCode"]
        )
        PostalAdresses_list.append(postal)

    PostalAdresses=JSON.PostalAddresses(PostalAdresses_list)
    schemeOAddress= JSON.SchemeOperatorAddress(
        SchemeOperatorElectronicAddress=eletronic,
        SchemeOperatorPostalAddress=PostalAdresses
    )

    #schemeName
    schemeName=list()

    #for cycle
    for scheme in dictFromDB_trusted_lists["SchemeName"]:
        schemeName.append(JSON.MultiLangString(scheme["lang"], scheme["text"]))

    #SchemeInformationURI
    schemeInformationURI=list()

    #for cycle
    for scheme in dictFromDB_trusted_lists["SchemeInformationURI"]:
        schemeInformationURI.append(JSON.NonEmptyMultiLangURI(scheme["lang"], scheme["URI"]))
    
    #schemeTypeCommunityRules
    schemeCRules= list()

    #for cycle
    schemeCRules.append(JSON.NonEmptyMultiLangURI("en", confxml.LoTESchemeTypeCommunityRules[LoTEType]))

    #PolicyOrLegalNotice
    PolicyOrLegalNotice= list()

    #for cycle
    for scheme in dictFromDB_trusted_lists["PolicyOrLegalNotice"]:
        policy={
            "LoTEPolicy":{
                "lang":scheme["lang"],
                "uriValue":scheme["text"]
            }
        }
        PolicyOrLegalNotice.append(policy)

    #PointerToOtherTSL
    Pointers= JSON.PointersToOtherLoTE()

    #OtherTSLPointerType-LoTL

    ServiceDigitalIdentities= list()
    X509Certificates=list()
    X509Certificates.append(cert_cleaned)
    serviceDigitalIdentity=JSON.ServiceDigitalIdentity(X509Certificates=X509Certificates, X509SubjectNames=None, PublicKeyValues=None, X509SKIs=None, OtherIds=None, additionalProperties=None)

    ServiceDigitalIdentities.append(serviceDigitalIdentity)


    #additional Info

    #SchemeNameOperatorAdditionalInformation
    #for cycle

    AdditionalInfo_SchemeOperatorName=schemeOName
    #AdditionalInfo_SchemeOperatorName.append(JSON.MultiLangString("en", "E))


    #SchemeTypeCommunityRules
    schemetypeCommunityRules_add=list()

    #for cycle
    schemetypeCommunityRules_add.append(JSON.NonEmptyMultiLangURI("en", confxml.LoTESchemeTypeCommunityRules["LoTL"]))

    AdditionalInfo=JSON.LoTEQualifier(
        LoTEType=LoTEType,
        SchemeOperatorName=AdditionalInfo_SchemeOperatorName,
        SchemeTerritory="EU",
        SchemeTypeCommunityRules=schemetypeCommunityRules_add,
        MimeType= "application/json",

    )

    Lote_qualifiers=list()
    Lote_qualifiers.append(AdditionalInfo)

    Pointer= JSON.OtherLoTEPointer(
        LoTELocation=confxml.LoTElotl_location,
        ServiceDigitalIdentities=ServiceDigitalIdentities,
        LoTEQualifiers=Lote_qualifiers
    )

    Pointers.append(Pointer)

    #DistribuitionPoints
    URIDP=list()

    #for cycle
    
    # for dp in dictFromDB_trusted_lists["DistributionPoints"]:
    #     URIDP.add_URI(test.NonEmptyURIType(dp))
    last= dictFromDB_trusted_lists["SchemeInformationURI"][-1].get("URI")

    URIDP.append(last)

    schemeInfo=JSON.ListAndSchemeInformation(
        LoTEVersionIdentifier=confxml.LoTEVersionIdentifier,
        LoTESequenceNumber=dictFromDB_trusted_lists["SequenceNumber"] ,
        SchemeOperatorName=schemeOName,
        ListIssueDateTime=dictFromDB_trusted_lists["issue_date"].strftime("%Y-%m-%dT%H:%M:%SZ"),
        NextUpdate=dictFromDB_trusted_lists["next_update"].strftime("%Y-%m-%dT%H:%M:%SZ"),
        LoTEType=LoTEType,
        SchemeOperatorAddress=schemeOAddress,
        SchemeName=schemeName,
        SchemeInformationURI=schemeInformationURI,
        StatusDeterminationApproach=confxml.LoTEStatusDeterminationApproach[LoTEType],
        SchemeTypeCommunityRules=schemeCRules,
        SchemeTerritory=dictFromDB_trusted_lists["schemeTerritory"],
        PolicyOrLegalNotice=PolicyOrLegalNotice,
        #PointersToOtherLoTE=Pointers,
        DistributionPoints=URIDP,


    )

    if LoTEType == "http://uri.etsi.org/19602/LoTEType/EUPubEAAProvidersList":
        schemeInfo.HistoricalInformationPeriod=dictFromDB_trusted_lists["HistoricalInformationPeriod"]

    #--------------------------------------------#

    #TrustServiceProviderList

    TrustServiceProviderList=JSON.TrustedEntitiesList()


    for tsp in tsp_data:
        TSPName=list()
        TSPTradeName= list()
        TSPPostalAddress=JSON.PostalAddresses()
        TSPEletronicAddress=JSON.ElectronicAddress()
        TSPInformationURI= list()

        name = parse_json_field(tsp["name"])
        for item in name:
            TSPName.append(JSON.MultiLangString(item['lang'], item["text"]))

        trade_name = parse_json_field(tsp["trade_name"])
        for item in trade_name:
            TSPTradeName.append(JSON.MultiLangString(item['lang'], item["text"]))

        address = parse_json_field(tsp["postal_address"])
        for item in address:
            postal1=JSON.PostalAddress(
                lang=item['lang'],
                Country=item["CountryName"],
                StreetAddress=item["StreetAddress"],
                Locality=item["Locality"],
                StateOrProvince=item["StateOrProvince"],
                PostalCode=item["PostalCode"]
                    
            )
            
            TSPPostalAddress.append(postal1)
    
        ele_address = parse_json_field(tsp["EletronicAddress"])
        for item in ele_address:
            TSPEletronicAddress.append(JSON.NonEmptyMultiLangURI(lang=item['lang'],uriValue=item["URI"]))
        
        
        TSPAddress=JSON.TEAddress(
            TEPostalAddress=TSPPostalAddress,
            TEElectronicAddress=TSPEletronicAddress
        )


        uri = parse_json_field(tsp["TSPInformationURI"])
        for item in uri:
            TSPInformationURI.append(JSON.NonEmptyMultiLangURI(item['lang'],item["URI"]))

        TSPInformation=JSON.TrustedEntityInformation(
            TEName=TSPName,
            TETradeName=TSPTradeName,
            TEAddress=TSPAddress,
            TEInformationURI=TSPInformationURI
        )

        #Services
        TSPServices=list()

        #ServiceInformationExtensions=test.ExtensionsListType()
        # Extension =test.ExtensionType()
        # Qualifications=test.QualificationsType()
        # qualificationElement=test.QualificationElementType()
        # qualifiers=test.QualifiersType()
        # qualifier=test.QualifierType()
        # CriteriaList=test.CriteriaListType()
        # PolicySet=test.PoliciesListType()
        # PolicyIdentifier=test.ObjectIdentifierType()
        # Identifier=test.IdentifierType()
        # AdditionalServiceInformation=test.AdditionalServiceInformationType()
        # ExtensionAdditionalServiceInformation=test.ExtensionType()
        # ExtensionAdditionalServiceInformation.set_anytypeobjs_(test.AdditionalServiceInformationType())
        # Extension.set_anytypeobjs_(test.QualificationsType())

        for each in service_data:

            if each["tsp_id"] == tsp["tsp_id"]:
                
                ServiceName=list()
                SchemeServiceDefinitionURI=list()

                serv_name = parse_json_field(each["ServiceName"])
                for item in serv_name:
                    ServiceName.append(JSON.MultiLangString(item["lang"], item["text"]))

                X509Certificates= list()
                X509Certificates.append(JSON.PkiOb(val=each["digital_identity"]))
                ServiceDigitalIdentity=JSON.ServiceDigitalIdentity(
                    X509Certificates=X509Certificates
                )

                uri = parse_json_field(each["SchemeServiceDefinitionURI"])
                for item in uri:
                    SchemeServiceDefinitionURI.append(JSON.NonEmptyMultiLangURI(item["lang"],item["URI"]))
                

                #Extensions

                #Qualification
                # Qualifications.__setattr__("_Critical",True)

                # qualifier.set_uri(each["qualifier"])
                # qualifiers.add_Qualifier(qualifier)

                # Identifier.set_Qualifier("OIDAsURI")
                # Identifier.set_valueOf_("0.4.0.194112.1.2")
                # PolicyIdentifier.add_Identifier(Identifier)
            

                # PolicySet.add_PolicyIdentifier(PolicyIdentifier)

                # CriteriaList.add_PolicySet(PolicySet)
                # CriteriaList.set_assert("all")

                # qualificationElement.set_CriteriaList(CriteriaList)
                # qualificationElement.set_Qualifiers(qualifiers)

                # Qualifications.add_QualificationElement(qualificationElement)

                
                # AdditionalServiceInformation.set_URI(JSON.NonEmptyMultiLangURI("en","	https://www.teste.com"))
                # Extension.set_valueOf_(Qualifications)
                # Extension.set_Critical(True)

                # ExtensionAdditionalServiceInformation.set_valueOf_(AdditionalServiceInformation)
                # ExtensionAdditionalServiceInformation.set_Critical(True)

                # ServiceInformationExtensions.add_Extension(Extension)
                # ServiceInformationExtensions.add_Extension(ExtensionAdditionalServiceInformation)
                # ServiceInformation.set_ServiceInformationExtensions(ServiceInformationExtensions)

                ServiceInformation=JSON.ServiceInformation(
                    ServiceName=ServiceName,
                    ServiceDigitalIdentity=ServiceDigitalIdentity,
                    ServiceTypeIdentifier=each["service_type"],
                    SchemeServiceDefinitionURI=SchemeServiceDefinitionURI,

                )
                if each["service_type"] == "http://uri.etsi.org/19602/SvcType/PubEAA/Issuance" or each["service_type"] == "http://uri.etsi.org/19602/SvcType/PubEAA/Revocation" :
                    ServiceInformation.ServiceStatus= each["status"]
                    ServiceInformation.StatusStartingTime= each["status_start_date"].strftime("%Y-%m-%dT%H:%M:%SZ")
                
                #ServiceHistoryInstance
                #equal to Service Information
                ServiceHistory= list()

                TSPService= JSON.TrustedEntityService(
                    ServiceInformation=ServiceInformation,
                )


                if service_history:

                    for history in service_history:
                        if each["service_id"] == history["service_id"]:

                            ServiceName=list()

                            serv_name = parse_json_field(history["ServiceName"])
                            for item in serv_name:
                                ServiceName.append(JSON.MultiLangString(item["lang"], item["text"]))

                            
                            ServiceHistoryInstance=JSON.ServiceHistoryInstance(
                                ServiceName=ServiceName,
                                ServiceDigitalIdentity=JSON.ServiceDigitalIdentity(),
                                ServiceTypeIdentifier=history["service_type"],
                                ServiceStatus=history["status"],
                                StatusStartingTime=history["status_start_date"].strftime("%Y-%m-%dT%H:%M:%SZ")                                                         
                            )

                            X509SKIs= list()
                            cert_service_bytes = base64.b64decode(history["digital_identity"])
                            try:

                                cert_service = x509.load_der_x509_certificate(cert_service_bytes, default_backend())

                            except (ValueError, TypeError):
                                
                                cert_service = x509.load_pem_x509_certificate(cert_service_bytes, default_backend())
                                
                            try:
                                ski = cert_service.extensions.get_extension_for_oid(x509.oid.ExtensionOID.SUBJECT_KEY_IDENTIFIER)

                                ski_value=ski.value.digest.hex()

                                X509SKIs.append(ski_value)

                                ServiceDigitalIdentity=JSON.ServiceDigitalIdentity(
                                    X509SKIs=X509SKIs
                                )

                                ServiceHistoryInstance.ServiceDigitalIdentity= ServiceDigitalIdentity

                            except x509.extensions.ExtensionNotFound:
                                
                                print("No SKI")
                            
                            ServiceHistory.append(ServiceHistoryInstance)

                if ServiceHistory.has__content() == True:
                    TSPService.ServiceHistory(ServiceHistory)

                TSPServices.append(TSPService)

        #AdditionalServiceInformation		

        TrustServiceProvider= JSON.TrustedEntity(
            TrustedEntityInformation=TSPInformation,
            TrustedEntityServices=TSPServices
        )

        TrustServiceProviderList.append(TrustServiceProvider)

    root= JSON.LoTE(
        TrustedEntitiesList=TrustServiceProviderList,
        ListAndSchemeInformation=schemeInfo
    )

    
    clean_dict = remove_none(root)

    dict={
        "LoTE":clean_dict
    }
    json_str = json.dumps(dict)
    json_bytes= json_str.encode('utf-8')

    cert_for_hash=x509.load_pem_x509_certificate(cert, default_backend())
    thumbprint= hashlib.sha256(cert_for_hash.tbs_certificate_bytes).hexdigest()
 
    #key=open(cfgserv.priv_key_UT, "rb").read()

    encoded_file, json_hash_before_sign= jadesigner(base64.b64encode(json_bytes).decode("utf-8"),base64.b64encode(cert).decode("utf-8"), cfgserv.priv_key_UT )

    # with open ("teste.xml", "w") as file: 
    #     signed_root.write(file, level=0)


    file=base64.b64decode(encoded_file).decode()

    file=json.loads(file)

    #print(file)

    jwt= f'{file["signatures"][0]["protected"]}.{file["payload"]}.{file["signatures"][0]["signature"]}'

    return base64.b64encode(jwt.encode()).decode(), thumbprint, json_hash_before_sign


def json_gen_lote_json(user_info, tsl_list, dict_tsl_mom, log_id):

    der_data=open(cfgserv.cert_UT, "rb").read()
    cert_der= x509.load_der_x509_certificate(der_data, backend=default_backend())
    cert = cert_der.public_bytes(encoding=serialization.Encoding.PEM)

    pem_str = cert.decode('utf-8')
    cert_cleaned = ''.join(line for line in pem_str.splitlines() if "CERTIFICATE" not in line)


    schemeOName = list()

    #for cycle
    op_name = parse_json_field(user_info["operator_name"])
    for item in op_name:
        schemeOName.append(JSON.MultiLangString(item['lang'], item["text"]))

    #schemeInfo.SchemeOperatorName=schemeOName

    #Scheme Operator Address
    

    eletronic=JSON.ElectronicAddress()

    #for cycle
    EletronicAddress = parse_json_field(user_info["EletronicAddress"])
    for item in EletronicAddress:
        eletronic.append(JSON.NonEmptyMultiLangURI(item['lang'],item["URI"]))
    #----------------------------------------------------#

    PostalAdresses_list=list()

    #for cycle for postal address
    postal = parse_json_field(user_info["postal_address"])
    for item in postal:
        postal=JSON.PostalAddress(
            lang=item['lang'],
            Country=item["CountryName"],
            StreetAddress=item["StreetAddress"],
            Locality=item["Locality"],
            StateOrProvince=item["StateOrProvince"],
            PostalCode=item["PostalCode"]
        )
        PostalAdresses_list.append(postal)

    PostalAdresses=JSON.PostalAddresses(PostalAdresses_list)
    schemeOAddress= JSON.SchemeOperatorAddress(
        SchemeOperatorElectronicAddress=eletronic,
        SchemeOperatorPostalAddress=PostalAdresses
    )

    #schemeName
    schemeName=list()

    #for cycle
    for scheme in dict_tsl_mom["SchemeName"]:
        schemeName.append(JSON.MultiLangString(scheme["lang"], scheme["text"]))

    #SchemeInformationURI
    schemeInformationURI=list()

    #for cycle
    for scheme in dict_tsl_mom["SchemeInformationURI"]:
        schemeInformationURI.append(JSON.NonEmptyMultiLangURI(scheme["lang"], scheme["URI"]))
    
    #schemeTypeCommunityRules
    schemeCRules= list()

    #for cycle
    schemeCRules.append(JSON.MultiLangString("en", confxml.SchemeTypeCommunityRules["LoTL"]))
    

    #PolicyOrLegalNotice
    PolicyOrLegalNotice= list()

    #for cycle
    for scheme in dict_tsl_mom["PolicyOrLegalNotice"]:
        PolicyOrLegalNotice.append(JSON.MultiLangString(scheme["lang"], scheme["text"]))

    #PointerToOtherTSL
    Pointers= JSON.PointersToOtherLoTE()

    #OtherTSLPointerType-LoTL

    ServiceDigitalIdentities= list()
    X509Certificates=list()
    X509Certificates.append(cert_cleaned)
    serviceDigitalIdentity=JSON.ServiceDigitalIdentity(X509Certificates=X509Certificates, X509SubjectNames=None, PublicKeyValues=None, X509SKIs=None, OtherIds=None, additionalProperties=None)

    ServiceDigitalIdentities.append(serviceDigitalIdentity)


    #additional Info

    #SchemeNameOperatorAdditionalInformation
    #for cycle

    AdditionalInfo_SchemeOperatorName=list()
    AdditionalInfo_SchemeOperatorName.append(JSON.MultiLangString("en", "EU-LOTE"))


    #SchemeTypeCommunityRules
    schemetypeCommunityRules_add=list()

    #for cycle
    schemetypeCommunityRules_add.append(JSON.NonEmptyMultiLangURI("en", confxml.SchemeTypeCommunityRules["EU"]))

    AdditionalInfo=JSON.LoTEQualifier(
        LoTEType=confxml.TSLType["LoTL"],
        SchemeOperatorName=AdditionalInfo_SchemeOperatorName,
        SchemeTerritory="EU",
        SchemeTypeCommunityRules=schemetypeCommunityRules_add,
        MimeType= "application/json",

    )

    Lote_qualifiers=list()
    Lote_qualifiers.append(AdditionalInfo)

    Pointer= JSON.OtherLoTEPointer(
        LoTELocation=dict_tsl_mom["SchemeInformationURI"][-1].get("URI"),
        ServiceDigitalIdentities=ServiceDigitalIdentities,
        LoTEQualifiers=Lote_qualifiers
    )

    Pointers.append(Pointer)

    for tsl_data in tsl_list:
        
        ServiceDigitalIdentities= list()

        #for cycle novo
        aux = func.get_old_cert(tsl_data["id"], log_id)

        X509certificates=list()
        for each in aux:
            X509certificates.append(each["cert"])
    
        #end
        
        serviceDigitalIdentity=JSON.ServiceDigitalIdentity(X509Certificates=X509certificates)

        ServiceDigitalIdentities.append(serviceDigitalIdentity)

        #SchemeNameOperatorAdditionalInformation
        #for cycle
        schemeNametest=JSON.SchemeOperatorName()
        for item in tsl_data["SchemeName"]:
            schemeNametest.append(JSON.MultiLangString(item['lang'], item["text"]))

        #SchemeTypeCommunityRules
        
        schemetypeCommunityRules_add=JSON.SchemeTypeCommunityRules()

        #for cycle
        schemetypeCommunityRules_add.append(JSON.NonEmptyMultiLangURI("en", confxml.SchemeTypeCommunityRules["EU"]))
        schemetypeCommunityRules_add.append(JSON.NonEmptyMultiLangURI("en", confxml.SchemeTypeCommunityRules["Country"] + tsl_data["schemeTerritory"]))


        AdditionalInfo=JSON.LoTEQualifier(
            LoTEType=confxml.TSLType["EU"],
            SchemeOperatorName=schemeNametest,
            SchemeTerritory=tsl_data["schemeTerritory"],
            SchemeTypeCommunityRules=schemetypeCommunityRules_add,
            MimeType= "application/json",
        )
            
        Lote_qualifiers=list()
        Lote_qualifiers.append(AdditionalInfo)


        last= tsl_data["SchemeInformationURI"][-1].get("URI")

        Pointer= JSON.OtherLoTEPointer(
            LoTELocation=last,
            ServiceDigitalIdentities=ServiceDigitalIdentities,
            LoTEQualifiers=Lote_qualifiers
        )   
        Pointers.append(Pointer)
    

    #DistribuitionPoints
    URIDP=list()

    #for cycle
    
    # for dp in dict_tsl_mom["DistributionPoints"]:
    #     URIDP.add_URI(test.NonEmptyURIType(dp))
    last= dict_tsl_mom["SchemeInformationURI"][-1].get("URI")

    URIDP.append(last)

    schemeInfo=JSON.ListAndSchemeInformation(
        LoTEVersionIdentifier=confxml.TLSVersionIdentifier,
        LoTESequenceNumber=dict_tsl_mom["SequenceNumber"],
        SchemeOperatorName=schemeOName,
        ListIssueDateTime=dict_tsl_mom["issue_date"].strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        NextUpdate=dict_tsl_mom["next_update"].strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        LoTEType=confxml.TSLType["EU"],
        SchemeOperatorAddress=schemeOAddress,
        SchemeName=schemeName,
        SchemeInformationURI=schemeInformationURI,
        StatusDeterminationApproach=confxml.StatusDeterminationApproach["LoTL"],
        SchemeTypeCommunityRules=schemeCRules,
        SchemeTerritory="EU",
        PolicyOrLegalNotice=PolicyOrLegalNotice,
        HistoricalInformationPeriod=dict_tsl_mom["HistoricalInformationPeriod"],
        PointersToOtherLoTE=Pointers,
        DistributionPoints=URIDP,


    )

    root= JSON.LoTE(
        ListAndSchemeInformation=schemeInfo
    )

    # with open ("cert_UT.pem", "rb") as file: 
    #     cert = file.read()
    #     cert=x509.load_pem_x509_certificate(cert)
    clean_dict = remove_none(root)

    json_str = json.dumps(clean_dict)
    json_bytes= json_str.encode('utf-8')

    cert_for_hash=x509.load_pem_x509_certificate(cert, default_backend())
    thumbprint= hashlib.sha256(cert_for_hash.tbs_certificate_bytes).hexdigest()

    encoded_file, json_hash_before_sign= jadesigner(base64.b64encode(json_bytes).decode("utf-8"),base64.b64encode(cert).decode("utf-8"), cfgserv.priv_key_UT )
    
    # with open ("teste.xml", "w") as file: 
    #     signed_root.write(file, level=0) 

    return encoded_file, thumbprint, json_hash_before_sign


def remove_none(obj):
    if is_dataclass(obj):
        obj = asdict(obj)

    if isinstance(obj, dict):
        return {k: remove_none(v) for k, v in obj.items() if v is not None}
    elif isinstance(obj, list):
        return [remove_none(v) for v in obj if v is not None]
    else:
        return obj

    