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
from dataclasses import asdict
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
from jadessigner import jadesigner

def parse_json_field(field):
    try:
        return json.loads(field) if isinstance(field, str) else field
    except json.JSONDecodeError:
        return field
    
def json_gen_json(user_info, dictFromDB_trusted_lists, tsp_data, service_data, tsl_id, log_id):
    service_data = [service for sublist in service_data for service in sublist]

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
    
    
    root=JSON.LoTE

    root.set_TSLTag("http://uri.etsi.org/19612/TSLTag")
    root.set_Id("TrustServiceStatusList")

    schemeInfo = root.ListAndSchemeInformation

    schemeInfo.LoTEVersionIdentifier=confxml.TLSVersionIdentifier
    schemeInfo.LoTESequenceNumber=dictFromDB_trusted_lists["SequenceNumber"] + 1
    schemeInfo.LoTEType=confxml.TSLType["EU"]

    #schemeOperatorName

    schemeOName = list

    #for cycle
    op_name = parse_json_field(user_info["operator_name"])
    for item in op_name:
        schemeOName.append(JSON.MultiLangString(item['lang'], item["text"]))

    schemeInfo.SchemeOperatorName=schemeOName

    #Scheme Operator Address
    schemeOAddress= JSON.SchemeOperatorAddress

    eletronic=JSON.ElectronicAddress

    #for cycle
    EletronicAddress = parse_json_field(user_info["EletronicAddress"])
    for item in EletronicAddress:
        eletronic.append(JSON.NonEmptyMultiLangURI(item['lang'],item["URI"]))
    #----------------------------------------------------#
    schemeOAddress.SchemeOperatorElectronicAddress(eletronic)

    PostalAdresses=JSON.PostalAddresses

    #for cycle for postal address
    postal = parse_json_field(user_info["postal_address"])
    for item in postal:
        postal=JSON.PostalAddress
        postal.lang=item['lang']
        postal.Country=item["CountryName"]
        postal.StreetAddress=item["StreetAddress"]
        postal.Locality=item["Locality"]
        postal.StateOrProvince=item["StateOrProvince"]
        postal.PostalCode=item["PostalCode"]
        PostalAdresses.append(postal)

    schemeOAddress.SchemeOperatorPostalAddress(PostalAdresses)
    schemeInfo.SchemeOperatorAddress=schemeOAddress

    #schemeName
    schemeName=list

    #for cycle
    for scheme in dictFromDB_trusted_lists["SchemeName"]:
        schemeName.append(JSON.MultiLangString(scheme["lang"], scheme["text"]))
    
    schemeInfo.SchemeName=schemeName

    #SchemeInformationURI
    schemeInformationURI=list

    #for cycle
    for scheme in dictFromDB_trusted_lists["SchemeInformationURI"]:
        schemeInformationURI.append(JSON.NonEmptyMultiLangURI(scheme["lang"], scheme["URI"]))
    
    schemeInfo.SchemeInformationURI=schemeInformationURI

    #StatusDeterminationApproach
    schemeInfo.StatusDeterminationApproach=confxml.StatusDeterminationApproach["EU"]
    
    #schemeTypeCommunityRules
    schemeCRules= list

    #for cycle
    schemeCRules.append(JSON.MultiLangString("en", confxml.SchemeTypeCommunityRules["EU"]))
    schemeCRules.append(JSON.MultiLangString("en", confxml.SchemeTypeCommunityRules["Country"] + dictFromDB_trusted_lists["schemeTerritory"] ))
    schemeInfo.SchemeTypeCommunityRules= schemeCRules

    #SchemeTerritory
    schemeInfo.SchemeTerritory=dictFromDB_trusted_lists["schemeTerritory"]

    #PolicyOrLegalNotice
    PolicyOrLegalNotice= list

    #for cycle
    for scheme in dictFromDB_trusted_lists["PolicyOrLegalNotice"]:
        PolicyOrLegalNotice.append(JSON.MultiLangString(scheme["lang"], scheme["text"]))

    schemeInfo.PolicyOrLegalNotice=PolicyOrLegalNotice

    #HistoricalInformationPeriod
    schemeInfo.HistoricalInformationPeriod=dictFromDB_trusted_lists["HistoricalInformationPeriod"]

    #PointerToOtherTSL
    Pointers= JSON.PointersToOtherLoTE

    #OtherTSLPointerType-LoTL

    ServiceDigitalIdentities= list
    serviceDigitalIdentity=JSON.ServiceDigitalIdentity

    serviceDigitalIdentity.X509Certificates.append(base64.b64decode(cert_cleaned))

    ServiceDigitalIdentities.append(serviceDigitalIdentity)

    Pointer= JSON.OtherLoTEPointer
    Pointer.ServiceDigitalIdentities=ServiceDigitalIdentities

    #additional Info
    
    #TSLTypeAdditionalInformation

    AdditionalInfo = JSON.LoTEQualifier

    AdditionalInfo.LoTEType=confxml.TSLType["LoTL"]


    #SchemeNameOperatorAdditionalInformation
    #for cycle

    AdditionalInfo_SchemeOperatorName=list
    AdditionalInfo_SchemeOperatorName.append(JSON.MultiLangString("en", "EU-LOTL"))

    AdditionalInfo.SchemeOperatorName= AdditionalInfo_SchemeOperatorName

    #SchemeTerritoryAdditionalInformation

    AdditionalInfo.SchemeTerritory="EU"

    #SchemeTypeCommunityRules
    schemetypeCommunityRules_add=list

    #for cycle
    schemetypeCommunityRules_add.append(JSON.NonEmptyMultiLangURI("en", confxml.SchemeTypeCommunityRules["LoTL"]))

    AdditionalInfo.SchemeTypeCommunityRules= schemetypeCommunityRules_add

    #MimeType

    AdditionalInfo.MimeType= "application/vnd.etsi.tsl+xml"

    Pointer.LoTELocation=confxml.lotl_location

    Pointer.LoTEQualifiers.append(AdditionalInfo)
    Pointers.append(Pointer)

    schemeInfo.PointersToOtherLoTE=Pointers
    
    schemeInfo.ListIssueDateTime=dictFromDB_trusted_lists["issue_date"]
    
    #Next Update
    
    schemeInfo.NextUpdate= dictFromDB_trusted_lists["next_update"]

    #DistribuitionPoints
    URIDP=list

    #for cycle
    
    # for dp in dictFromDB_trusted_lists["DistributionPoints"]:
    #     URIDP.add_URI(test.NonEmptyURIType(dp))
    last= dictFromDB_trusted_lists["SchemeInformationURI"][-1].get("URI")

    URIDP.append(last)

    schemeInfo.DistributionPoints=URIDP

    #--------------------------------------------#

    #TrustServiceProviderList

    TrustServiceProviderList=JSON.TrustedEntitiesList


    for tsp in tsp_data:
        TrustServiceProvider= JSON.TrustedEntity
        TSPInformation=JSON.TrustedEntityInformation
        TSPName=list
        TSPTradeName= list
        TSPAddress=JSON.TEAddress
        TSPPostalAddress=JSON.PostalAddresses
        TSPEletronicAddress=JSON.ElectronicAddress
        TSPInformationURI= list

        name = parse_json_field(tsp["name"])
        for item in name:
            TSPName.append(JSON.MultiLangString(item['lang'], item["text"]))

        trade_name = parse_json_field(tsp["trade_name"])
        for item in trade_name:
            TSPTradeName.append(JSON.MultiLangString(item['lang'], item["text"]))

        address = parse_json_field(tsp["postal_address"])
        for item in address:
            postal1=JSON.PostalAddress
            postal1.lang=item['lang']
            postal1.Country=item["CountryName"]
            postal1.StreetAddress=item["StreetAddress"]
            postal1.Locality=item["Locality"]
            postal1.StateOrProvince=item["StateOrProvince"]
            postal1.PostalCode=item["PostalCode"]
            TSPPostalAddress.append(postal1)
        
        
    
        ele_address = parse_json_field(tsp["EletronicAddress"])
        for item in ele_address:
            TSPEletronicAddress.append(JSON.NonEmptyMultiLangURI(item['lang'],item["URI"]))


        uri = parse_json_field(tsp["TSPInformationURI"])
        for item in uri:
            TSPInformationURI.append(JSON.NonEmptyMultiLangURI(item['lang'],item["URI"]))

        TSPAddress.TEPostalAddress=TSPPostalAddress
        TSPAddress.TEElectronicAddress=TSPEletronicAddress
        TSPInformation.TEName=TSPName
        TSPInformation.TETradeName=TSPTradeName
        TSPInformation.TEAddress=TSPAddress
        TSPInformation.TEInformationURI=TSPInformationURI
        TrustServiceProvider.TrustedEntityInformation=TSPInformation

        #Services
        TSPServices=list

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
                
                TSPService=JSON.TrustedEntityService
                ServiceInformation=JSON.ServiceInformation
                ServiceName=list
                SchemeServiceDefinitionURI=list

                ServiceInformation.ServiceTypeIdentifier=each["service_type"]

                serv_name = parse_json_field(each["ServiceName"])
                for item in serv_name:
                    ServiceName.append(JSON.MultiLangString(item["lang"], item["text"]))

                ServiceInformation.ServiceName=ServiceName

                ServiceDigitalIdentity=JSON.ServiceDigitalIdentity
                X509Certificates= list
                X509Certificates.append(base64.b64decode(each["digital_identity"]))
                ServiceDigitalIdentity.X509Certificates= X509Certificates
                ServiceInformation.ServiceDigitalIdentity=ServiceDigitalIdentity

                ServiceInformation.ServiceStatus=each["status"]
                ServiceInformation.StatusStartingTime=each["status_start_date"]

                uri = parse_json_field(each["SchemeServiceDefinitionURI"])
                for item in uri:
                    SchemeServiceDefinitionURI.append(JSON.NonEmptyMultiLangURI(item["lang"],item["URI"]))
                
                ServiceInformation.ServiceDefinitionURI=SchemeServiceDefinitionURI

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

                TSPService.ServiceInformation=ServiceInformation
                TSPServices.append(TSPService)

        #AdditionalServiceInformation		
        TrustServiceProvider.TrustedEntityServices=TSPServices
        TrustServiceProviderList.append(TrustServiceProvider)

    root.TrustedEntitiesList=TrustServiceProviderList

    json_str = json.dumps(asdict(root))
    json_bytes= json_str.decode('utf-8')

    cert_for_hash=x509.load_pem_x509_certificate(cert, default_backend())
    thumbprint= hashlib.sha256(cert_for_hash.tbs_certificate_bytes).hexdigest()
 
    key=open(cfgserv.priv_key_UT, "rb").read()

    encoded_file, json_hash_before_sign= jadesigner(base64.b64encode(json_bytes).decode("utf-8"),base64.b64encode(cert).decode("utf-8"), cfgserv.priv_key_UT )

    # with open ("teste.xml", "w") as file: 
    #     signed_root.write(file, level=0) 

    return encoded_file, thumbprint, json_hash_before_sign


def json_gen_lote_json(user_info, tsl_list, dict_tsl_mom, log_id):

    der_data=open(cfgserv.cert_UT, "rb").read()
    cert_der= x509.load_der_x509_certificate(der_data, backend=default_backend())
    cert = cert_der.public_bytes(encoding=serialization.Encoding.PEM)

    pem_str = cert.decode('utf-8')
    cert_cleaned = ''.join(line for line in pem_str.splitlines() if "CERTIFICATE" not in line)

    root=JSON.LoTE

    root.set_TSLTag("http://uri.etsi.org/19612/TSLTag")
    root.set_Id("TrustServiceStatusList")

    schemeInfo = JSON.ListAndSchemeInformation

    schemeInfo.LoTEVersionIdentifier=confxml.TLSVersionIdentifier
    schemeInfo.LoTESequenceNumber=dict_tsl_mom["SequenceNumber"] + 1
    
    schemeInfo.LoTEType=confxml.TSLType["LoTL"]

    #schemeOperatorName

    schemeOName = JSON.SchemeOperatorName

    #for cycle
    op_name = parse_json_field(user_info["operator_name"])
    for item in op_name:
        schemeOName.append(JSON.MultiLangString(item['lang'], item["text"]))

    schemeInfo.SchemeOperatorName=schemeOName

    #Scheme Operator Address
    schemeOAddress= JSON.SchemeOperatorAddress

    eletronic=JSON.ElectronicAddress

    #for cycle
    EletronicAddress = parse_json_field(user_info["EletronicAddress"])
    for item in EletronicAddress:
        eletronic.append(JSON.NonEmptyMultiLangURI(item['lang'],item["URI"]))
    #----------------------------------------------------#
    schemeOAddress.SchemeOperatorElectronicAddress=eletronic

    PostalAdresses=JSON.PostalAddresses

    #for cycle for postal address
    postal = parse_json_field(user_info["postal_address"])
    for item in postal:
        postal=JSON.PostalAddress
        postal.lang=item['lang']
        postal.Country=item["CountryName"]
        postal.StreetAddress=item["StreetAddress"]
        postal.Locality=item["Locality"]
        postal.StateOrProvince=item["StateOrProvince"]
        postal.PostalCode=item["PostalCode"]
        PostalAdresses.append(postal)

    schemeOAddress.SchemeOperatorPostalAddress=PostalAdresses
    schemeInfo.SchemeOperatorAddress=schemeOAddress
    
    schemeName=JSON.SchemeName
    PolicyOrLegalNotice= JSON.PolicyOrLegalNotice
    schemeInformationURI=JSON.SchemeInformationURI
    schemeCRules= JSON.SchemeTypeCommunityRules
    Pointers=JSON.PointersToOtherLoTE
    

    #schemeName
    #for cycle
    for scheme in dict_tsl_mom["SchemeName"]:
        schemeName.append(JSON.MultiLangString(scheme["lang"], scheme["text"]))
    
    schemeInfo.SchemeName = schemeName

    #SchemeInformationURI
    
    #for cycle
    for scheme in dict_tsl_mom["SchemeInformationURI"]:
        schemeInformationURI.append(JSON.NonEmptyMultiLangURI(scheme["lang"], scheme["URI"]))
    
    schemeInfo.SchemeInformationURI= schemeInformationURI

    #StatusDeterminationApproach
    schemeInfo.StatusDeterminationApproach=confxml.StatusDeterminationApproach["LoTL"]
    
    #schemeTypeCommunityRules

    #for cycle
    schemeCRules.append(JSON.NonEmptyMultiLangURI("en", confxml.SchemeTypeCommunityRules["LoTL"]))
    schemeInfo.SchemeTypeCommunityRules=schemeCRules

    #SchemeTerritory
    schemeInfo.SchemeTerritory= "EU"

    #PolicyOrLegalNotice

    #for cycle
    for scheme in dict_tsl_mom["PolicyOrLegalNotice"]:
        PolicyOrLegalNotice.append(JSON.MultiLangString(scheme["lang"], scheme["text"]))
    
    schemeInfo.PolicyOrLegalNotice(PolicyOrLegalNotice)

    #HistoricalInformationPeriod
    schemeInfo.HistoricalInformationPeriod= dict_tsl_mom["HistoricalInformationPeriod"]

    #PointerToOtherTSL

    #OtherTSLPointerType-LoTL

    ServiceDigitalIdentities=list
    serviceDigitalIdentity=JSON.ServiceDigitalIdentity

    serviceDigitalIdentity.X509Certificates.append(base64.b64decode(cert_cleaned))

    ServiceDigitalIdentities.append(serviceDigitalIdentity)
    Pointer= JSON.OtherLoTEPointer
    Pointer.ServiceDigitalIdentities = ServiceDigitalIdentities

    #additional Info
    AdditionalInfo=JSON.LoTEQualifier
    #TSLTypeAdditionalInformation

    AdditionalInfo.LoTEType= confxml.TSLType["LoTL"]

    #SchemeNameOperatorAdditionalInformation
    #for cycle
    schemeNametest=JSON.SchemeOperatorName
    for item in op_name:
        schemeNametest.append(JSON.MultiLangString(item['lang'], item["text"]))
    
    AdditionalInfo.SchemeOperatorName = schemeNametest

    #SchemeTerritoryAdditionalInformation

    AdditionalInfo.SchemeTerritory="EU"


    #SchemeTypeCommunityRules
    
    schemetypeCommunityRules_add=JSON.SchemeTypeCommunityRules

    #for cycle
    schemetypeCommunityRules_add.append(JSON.NonEmptyMultiLangURI("en", confxml.SchemeTypeCommunityRules["LoTL"]))

    AdditionalInfo.SchemeTypeCommunityRules = schemetypeCommunityRules_add

    #MimeType

    AdditionalInfo.MimeType = "application/vnd.etsi.tsl+xml"

    last = dict_tsl_mom["SchemeInformationURI"][-1].get("URI")
    Pointer.LoTELocation = last

    Pointer.LoTEQualifiers.append(AdditionalInfo)
    Pointers.append(Pointer)

    #for cycle
    for tsl_data in tsl_list:
        Pointer = JSON.OtherLoTEPointer

        ServiceDigitalIdentities= list
        serviceDigitalIdentity=JSON.ServiceDigitalIdentity

        #for cycle novo
        aux = func.get_old_cert(tsl_data["id"], log_id)

        for each in aux:
            serviceDigitalIdentity.X509Certificates.append(base64.b64decode(each["cert"]))
        
        #end

        ServiceDigitalIdentities.append(serviceDigitalIdentity)
        Pointer.ServiceDigitalIdentities = ServiceDigitalIdentities

        #additional Info
        AdditionalInfo= JSON.LoTEQualifier
        #TSLTypeAdditionalInformation
        
        AdditionalInfo.LoTEType= confxml.TSLType["EU"]

        #SchemeNameOperatorAdditionalInformation
        #for cycle
        schemeNametest=JSON.SchemeOperatorName
        for item in tsl_data["SchemeName"]:
            schemeNametest.append(JSON.MultiLangString(item['lang'], item["text"]))

        AdditionalInfo.SchemeOperatorName=schemeNametest

        #SchemeTerritoryAdditionalInformatio

        AdditionalInfo.SchemeTerritory= tsl_data["schemeTerritory"]


        #SchemeTypeCommunityRules
        
        schemetypeCommunityRules_add=JSON.SchemeTypeCommunityRules

        #for cycle
        schemetypeCommunityRules_add.append(JSON.NonEmptyMultiLangURI("en", confxml.SchemeTypeCommunityRules["EU"]))
        schemetypeCommunityRules_add.append(JSON.NonEmptyMultiLangURI("en", confxml.SchemeTypeCommunityRules["Country"] + tsl_data["schemeTerritory"]))

        AdditionalInfo.SchemeTypeCommunityRules = schemetypeCommunityRules_add

        #MimeType

        AdditionalInfo.MimeType="application/vnd.etsi.tsl+xml"

        last= tsl_data["SchemeInformationURI"][-1].get("URI")
        Pointer.LoTELocation=last

        Pointer.LoTEQualifiers.append(AdditionalInfo)
        Pointers.append(Pointer)
    
    schemeInfo.PointersToOtherLoTE=Pointers
    
    schemeInfo.ListIssueDateTime=dict_tsl_mom["issue_date"]
    #Next Update
    
    schemeInfo.NextUpdate= dict_tsl_mom["next_update"]

    #DistribuitionPoints

    #for cycle
    URIDP=list
    last= dict_tsl_mom["SchemeInformationURI"][-1].get("URI")
    URIDP.append(last)

    schemeInfo.DistributionPoints=URIDP

    root.ListAndSchemeInformation=schemeInfo

    # with open ("cert_UT.pem", "rb") as file: 
    #     cert = file.read()
    #     cert=x509.load_pem_x509_certificate(cert)

    cert_for_hash=x509.load_pem_x509_certificate(cert, default_backend())
    thumbprint= hashlib.sha256(cert_for_hash.tbs_certificate_bytes).hexdigest()

    # with open ("privkey_UT.pem", "rb") as key_file: 
    #     key = serialization.load_pem_private_key(key_file.read(),password=None,backend=default_backend())
        
    key_location=open(cfgserv.priv_key_UT, "rb").read()
    
    json_str = json.dumps(asdict(root))
    json_bytes= json_str.decode('utf-8')

    cert_for_hash=x509.load_pem_x509_certificate(cert, default_backend())
    thumbprint= hashlib.sha256(cert_for_hash.tbs_certificate_bytes).hexdigest()
 
    key=open(cfgserv.priv_key_UT, "rb").read()

    encoded_file, json_hash_before_sign= jadesigner(base64.b64encode(json_bytes).decode("utf-8"),base64.b64encode(cert).decode("utf-8"), cfgserv.priv_key_UT )

    # with open ("teste.xml", "w") as file: 
    #     signed_root.write(file, level=0) 

    return encoded_file, thumbprint, json_hash_before_sign



    