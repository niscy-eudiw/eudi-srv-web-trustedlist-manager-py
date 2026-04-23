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
import datetime
from io import StringIO
import io
import re
from dateutil.relativedelta import relativedelta
from flask import send_file
from signxml import DigestAlgorithm
from signxml.xades import (XAdESSigner,XAdESVerifier, XAdESSignaturePolicy,XAdESVerifyResult, XAdESDataObjectFormat)
import xml_gen_lote.lote_api as LOTE
from signxml.xades import (XAdESSigner, XAdESSignaturePolicy, XAdESDataObjectFormat)
from app.app_config.xml_config import ConfXML as confxml
from signxml import XMLSigner, algorithms, methods, namespaces
import json

from app_config.config import ConfService as cfgserv
from cryptography.hazmat.primitives import serialization
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import hashlib
from lxml import etree
import xml.etree.ElementTree as ET
from cryptography.hazmat.primitives.serialization import Encoding
import app.EJBCA_and_DB_func as func

def parse_json_field(field):
    try:
        return json.loads(field) if isinstance(field, str) else field
    except json.JSONDecodeError:
        return field
    
def xml_gen_xml_LoTE(user_info, dictFromDB_trusted_lists, tsp_data, service_data, tsl_id, log_id):
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
    
    root=LOTE.ListOfTrustedEntitiesType()

    root.set_LOTETag("http://uri.etsi.org/1960201/LoTETag")
    root.set_Id("ListofTrustedEntities")

    schemeInfo = LOTE.LoTEListAndSchemeInformationType()

    schemeInfo.set_LoTEVersionIdentifier(confxml.LoTEVersionIdentifier)
    schemeInfo.set_LoTESequenceNumber(dictFromDB_trusted_lists["SequenceNumber"] + 1)
    TSLType=LOTE.NonEmptyURIType()
    LoTEType=dictFromDB_trusted_lists["TSLType"]
    TSLType.valueOf_=LoTEType
    schemeInfo.LoTEType=TSLType

    #schemeOperatorName

    schemeOName = LOTE.InternationalNamesType()

    #for cycle
    op_name = parse_json_field(user_info["operator_name"])
    for item in op_name:
        schemeOName.add_Name(LOTE.MultiLangNormStringType(item['lang'], item["text"]))

    schemeInfo.SchemeOperatorName=schemeOName

    #Scheme Operator Address
    schemeOAddress= LOTE.AddressType()

    eletronic=LOTE.ElectronicAddressType()

    #for cycle
    EletronicAddress = parse_json_field(user_info["EletronicAddress"])
    for item in EletronicAddress:
        eletronic.add_URI(LOTE.NonEmptyMultiLangURIType(item['lang'],item["URI"]))
    #----------------------------------------------------#
    schemeOAddress.set_ElectronicAddress(eletronic)

    PostalAdresses=LOTE.PostalAddressListType()

    #for cycle for postal address
    postal = parse_json_field(user_info["postal_address"])
    for item in postal:
        postal=LOTE.PostalAddressType()
        postal.set_lang(item['lang'])
        postal.set_CountryName(item["CountryName"])
        postal.set_StreetAddress(item["StreetAddress"])
        postal.set_Locality(item["Locality"])
        postal.set_StateOrProvince(item["StateOrProvince"])
        postal.set_PostalCode(item["PostalCode"])
        PostalAdresses.add_PostalAddress(postal)

    schemeOAddress.set_PostalAddresses(PostalAdresses)
    schemeInfo.SchemeOperatorAddress=schemeOAddress

    #schemeName
    schemeName=LOTE.InternationalNamesType()

    #for cycle
    for scheme in dictFromDB_trusted_lists["SchemeName"]:
        schemeName.add_Name(LOTE.MultiLangNormStringType(scheme["lang"], scheme["text"]))
    
    schemeInfo.set_SchemeName(schemeName)

    #SchemeInformationURI
    schemeInformationURI=LOTE.NonEmptyMultiLangURIListType()

    #for cycle
    for scheme in dictFromDB_trusted_lists["SchemeInformationURI"]:
        schemeInformationURI.add_URI(LOTE.NonEmptyMultiLangURIType(scheme["lang"], scheme["URI"]))
    
    schemeInfo.set_SchemeInformationURI(schemeInformationURI)

    #StatusDeterminationApproach
    schemeInfo.StatusDeterminationApproach=LOTE.NonEmptyURIType(confxml.LoTEStatusDeterminationApproach[LoTEType])
    
    #schemeTypeCommunityRules
    schemeCRules= LOTE.NonEmptyMultiLangURIListType()

    #for cycle
    schemeCRules.add_URI(LOTE.NonEmptyMultiLangURIType("en", confxml.LoTESchemeTypeCommunityRules[dictFromDB_trusted_lists["TSLType"]]))
    schemeInfo.set_SchemeTypeCommunityRules(schemeCRules)

    #SchemeTerritory
    schemeInfo.set_SchemeTerritory(dictFromDB_trusted_lists["schemeTerritory"])

    #PolicyOrLegalNotice
    PolicyOrLegalNotice= LOTE.PolicyOrLegalnoticeType()

    #for cycle
    for scheme in dictFromDB_trusted_lists["PolicyOrLegalNotice"]:
        PolicyOrLegalNotice.add_LoTELegalNotice(LOTE.MultiLangStringType(scheme["lang"], scheme["text"]))

    schemeInfo.set_PolicyOrLegalNotice(PolicyOrLegalNotice)

    #HistoricalInformationPeriod
    if LoTEType == "http://uri.etsi.org/19602/LoTEType/EUPubEAAProvidersList":
        schemeInfo.set_HistoricalInformationPeriod(dictFromDB_trusted_lists["HistoricalInformationPeriod"])

    #PointerToOtherTSL
    Pointers= LOTE.OtherLoTEPointersType()

    #OtherTSLPointerType-LoTL

    ServiceDigitalIdentities= LOTE.ServiceDigitalIdentityListType()
    serviceDigitalIdentity=LOTE.DigitalIdentityListType()

    digitalID=LOTE.DigitalIdentityType()
    digitalID.set_X509Certificate(base64.b64decode(cert_cleaned))

    serviceDigitalIdentity.add_DigitalId(digitalID)
    ServiceDigitalIdentities.add_ServiceDigitalIdentity(serviceDigitalIdentity)

    Pointer= LOTE.OtherLoTEPointerType()
    Pointer.set_ServiceDigitalIdentities(ServiceDigitalIdentities)

    #additional Info
    
    #TSLTypeAdditionalInformation

    TSLTypeAdditionalInformation=LOTE.NonEmptyURIType()
    TSLTypeAdditionalInformation.original_tagname_="LoTEType"
    TSLTypeAdditionalInformation.valueOf_=dictFromDB_trusted_lists["TSLType"]

    objectLOTE=LOTE.AnyType()
    objectLOTE.valueOf_=TSLTypeAdditionalInformation
    
    AdditionalInfo=LOTE.AdditionalInformationType()
    AdditionalInfo.add_OtherInformation(objectLOTE)

    #SchemeNameOperatorAdditionalInformation
    #for cycle
    schemeNameLOTE=LOTE.InternationalNamesType()
    schemeNameLOTE.add_Name(LOTE.MultiLangStringType("en", "EU-LOTE"))
    schemeNameLOTE.original_tagname_="SchemeOperatorName"

    AdditionalInfo.add_OtherInformation(schemeNameLOTE)

    # LOTEes=LOTE.TakenOverByType()
    # LOTEes.SchemeOperatorName=schemeNameLOTE

    # AdditionalInfo.add_OtherInformation(LOTEes)

    #SchemeTerritoryAdditionalInformation

    scheme=LOTE.AnyType()
    
    scheme.original_tagname_="SchemeTerritory"
    scheme.valueOf_="EU"

    AdditionalInfo.add_OtherInformation(scheme)


    #SchemeTypeCommunityRules
    
    schemetypeCommunityRules_add=LOTE.NonEmptyMultiLangURIListType()
    schemetypeCommunityRules_add.original_tagname_="SchemeTypeCommunityRules"
    
    objectLOTE_stcr=LOTE.AnyType()
    objectLOTE_stcr.original_tagname_="SchemeTypeCommunityRules"

    #for cycle
    schemetypeCommunityRules_add.add_URI(LOTE.NonEmptyMultiLangURIType("en", confxml.LoTESchemeTypeCommunityRules[dictFromDB_trusted_lists["TSLType"]]))

    objectLOTE_stcr.valueOf_=schemetypeCommunityRules_add

    AdditionalInfo.add_OtherInformation(objectLOTE_stcr)

    #MimeType
    ObjectType=LOTE.ObjectType()
    ObjectType.original_tagname_="MimeType"
    ObjectType.set_valueOf_("application/vnd.etsi.tsl+xml")

    objectMimeType=LOTE.AnyType()
    objectMimeType.set_valueOf_(ObjectType)

    AdditionalInfo.add_OtherInformation(objectMimeType)

    Pointer.LoTELocation=LOTE.NonEmptyURIType(confxml.lotl_location)

    Pointer.AdditionalInformation=AdditionalInfo
    Pointers.add_OtherLoTEPointer(Pointer)

    #PointersToOtherLoTE
    #schemeInfo.PointersToOtherLoTE=Pointers
    
    schemeInfo.ListIssueDateTime=dictFromDB_trusted_lists["issue_date"]
    
    #Next Update
    NUpdate=LOTE.NextUpdateType()
    NUpdate.set_dateTime(dictFromDB_trusted_lists["next_update"])
    
    schemeInfo.NextUpdate= NUpdate

    #DistribuitionPoints
    URIDP=LOTE.NonEmptyURIListType()

    #for cycle
    
    # for dp in dictFromDB_trusted_lists["DistributionPoints"]:
    #     URIDP.add_URI(LOTE.NonEmptyURIType(dp))
    last= dictFromDB_trusted_lists["SchemeInformationURI"][-1].get("URI")

    URIDP.add_URI(LOTE.NonEmptyURIType(last))

    schemeInfo.DistributionPoints=URIDP

    root.ListAndSchemeInformation=schemeInfo

    #--------------------------------------------#

    #TrustedEntitiesList

    TrustedEntitiesList=LOTE.TrustedEntitiesListType()


    for tsp in tsp_data:
        TrustServiceProvider= LOTE.TEType()
        TSPInformation=LOTE.TrustedEntityInformationType()
        TSPName=LOTE.InternationalNamesType()
        TSPTradeName= LOTE.InternationalNamesType()
        TSPAddress=LOTE.AddressType()
        TSPPostalAddress=LOTE.PostalAddressListType()
        TSPEletronicAddress=LOTE.ElectronicAddressType()
        TSPInformationURI= LOTE.NonEmptyMultiLangURIListType()

        name = parse_json_field(tsp["name"])
        for item in name:
            TSPName.add_Name(LOTE.MultiLangNormStringType(item['lang'], item["text"]))

        trade_name = parse_json_field(tsp["trade_name"])
        for item in trade_name:
            TSPTradeName.add_Name(LOTE.MultiLangNormStringType(item['lang'], item["text"]))

        address = parse_json_field(tsp["postal_address"])
        for item in address:
            postal1=LOTE.PostalAddressType()
            postal1.set_lang(item['lang'])
            postal1.set_CountryName(item["CountryName"])
            postal1.set_StreetAddress(item["StreetAddress"])
            postal1.set_Locality(item["Locality"])
            postal1.set_StateOrProvince(item["StateOrProvince"])
            postal1.set_PostalCode(item["PostalCode"])
            TSPPostalAddress.add_PostalAddress(postal1)
        
        
    
        ele_address = parse_json_field(tsp["EletronicAddress"])
        for item in ele_address:
            TSPEletronicAddress.add_URI(LOTE.NonEmptyMultiLangURIType(item['lang'],item["URI"]))


        uri = parse_json_field(tsp["TSPInformationURI"])
        for item in uri:
            TSPInformationURI.add_URI(LOTE.NonEmptyMultiLangURIType(item['lang'],item["URI"]))

        TSPAddress.set_PostalAddresses(TSPPostalAddress)
        TSPAddress.set_ElectronicAddress(TSPEletronicAddress)
        TSPInformation.set_TEName(TSPName)
        TSPInformation.set_TETradeName(TSPTradeName)
        TSPInformation.set_TEAddress(TSPAddress)
        TSPInformation.set_TEInformationURI(TSPInformationURI)
        TrustServiceProvider.set_TrustedEntityInformation(TSPInformation)

        #Services
        TSPServices=LOTE.TrustedEntityServicesListType()

        #ServiceInformationExtensions=LOTE.ExtensionsListType()
        # Extension =LOTE.ExtensionType()
        # Qualifications=LOTE.QualificationsType()
        # qualificationElement=LOTE.QualificationElementType()
        # qualifiers=LOTE.QualifiersType()
        # qualifier=LOTE.QualifierType()
        # CriteriaList=LOTE.CriteriaListType()
        # PolicySet=LOTE.PoliciesListType()
        # PolicyIdentifier=LOTE.ObjectIdentifierType()
        # Identifier=LOTE.IdentifierType()
        # AdditionalServiceInformation=LOTE.AdditionalServiceInformationType()
        # ExtensionAdditionalServiceInformation=LOTE.ExtensionType()
        # ExtensionAdditionalServiceInformation.set_anytypeobjs_(LOTE.AdditionalServiceInformationType())
        # Extension.set_anytypeobjs_(LOTE.QualificationsType())

        for each in service_data:

            if each["tsp_id"] == tsp["tsp_id"]:
                
                TSPService=LOTE.TrustedEntityServiceType()
                ServiceInformation=LOTE.TEServiceInformationType()
                ServiceName=LOTE.InternationalNamesType()
                SchemeServiceDefinitionURI=LOTE.NonEmptyMultiLangURIListType()

                ServiceInformation.set_ServiceTypeIdentifier(LOTE.NonEmptyURIType(each["service_type"]))

                serv_name = parse_json_field(each["ServiceName"])
                for item in serv_name:
                    ServiceName.add_Name(LOTE.MultiLangNormStringType(item["lang"], item["text"]))

                ServiceInformation.set_ServiceName(ServiceName)

                ServiceDigitalIdentity=LOTE.DigitalIdentityListType()
                digitalID = LOTE.DigitalIdentityType()
                digitalID.set_X509Certificate(base64.b64decode(each["digital_identity"]))
                ServiceDigitalIdentity.add_DigitalId(digitalID)
                ServiceInformation.set_ServiceDigitalIdentity(ServiceDigitalIdentity)

                if each["service_type"] == "http://uri.etsi.org/19602/SvcType/PubEAA/Issuance" or each["service_type"] == "http://uri.etsi.org/19602/SvcType/PubEAA/Revocation" :
                    ServiceInformation.set_ServiceStatus(LOTE.NonEmptyURIType(each["status"]))
                    ServiceInformation.set_StatusStartingTime(each["status_start_date"])



                uri = parse_json_field(each["SchemeServiceDefinitionURI"])
                for item in uri:
                    SchemeServiceDefinitionURI.add_URI(LOTE.NonEmptyMultiLangURIType(item["lang"],item["URI"]))
                
                ServiceInformation.set_SchemeServiceDefinitionURI(SchemeServiceDefinitionURI)

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

                
                # AdditionalServiceInformation.set_URI(LOTE.NonEmptyMultiLangURIType("en","	https://www.LOTEe.com"))
                # Extension.set_valueOf_(Qualifications)
                # Extension.set_Critical(True)

                # ExtensionAdditionalServiceInformation.set_valueOf_(AdditionalServiceInformation)
                # ExtensionAdditionalServiceInformation.set_Critical(True)

                # ServiceInformationExtensions.add_Extension(Extension)
                # ServiceInformationExtensions.add_Extension(ExtensionAdditionalServiceInformation)
                # ServiceInformation.set_ServiceInformationExtensions(ServiceInformationExtensions)

                TSPService.set_ServiceInformation(ServiceInformation)
                TSPServices.add_TrustedEntityService(TSPService)

        #AdditionalServiceInformation		
        TrustServiceProvider.set_TrustedEntityServices(TSPServices)
        TrustedEntitiesList.add_TrustedEntity(TrustServiceProvider)

    root.set_TrustedEntitiesList(TrustedEntitiesList)

    xml_buffer=StringIO()
    root.export(xml_buffer,0,"")
    xml_string=xml_buffer.getvalue()
    
    content=xml_string
    content = re.sub(r'xmlns:ns0="([^"]+)"', r'xmlns="\1"', content)

    content = re.sub(r'<ns0:', r'<', content)
    content = re.sub(r'</ns0:', r'</', content)

    # with open ("cert_UT.pem", "rb") as file: 
    #     cert = file.read()
    #     cert=x509.load_pem_x509_certificate(cert)

    cert_for_hash=x509.load_pem_x509_certificate(cert, default_backend())
    thumbprint= hashlib.sha256(cert_for_hash.tbs_certificate_bytes).hexdigest()

    # with open ("privkey_UT.pem", "rb") as key_file: 
    #     key = serialization.load_pem_private_key(key_file.read(),password=None,backend=default_backend())
        
    key=open(cfgserv.priv_key_UT, "rb").read()
    
    ET.register_namespace("", "http://uri.etsi.org/019602/v1#")

    rootTemp=ET.fromstring(content)

    new_root = ET.Element(rootTemp.tag, attrib=rootTemp.attrib)
    new_root.text = rootTemp.text

    new_root.attrib["xmlns:ns2"] = "http://www.w3.org/2000/09/xmldsig#"
    new_root.attrib["xmlns:ns3"] = "http://uri.etsi.org/01903/v1.3.2#"

    for child in rootTemp:
        new_root.append(child )

    root_temp_str = ET.tostring(rootTemp, encoding="utf-8")
    root_lxml = etree.fromstring(root_temp_str)
    root_bytes = etree.tostring(root_lxml, method="c14n")
    xml_hash_before_sign = hashlib.sha256(root_bytes).hexdigest()

    data_object_format = XAdESDataObjectFormat(
        Description="TSL signature",
        MimeType="text/xml",
    )

    signer = XAdESSigner(
        claimed_roles=["signer"],
        data_object_format=data_object_format,
        c14n_algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315",
        signature_algorithm=algorithms.SignatureMethod.ECDSA_SHA256,
        method=methods.enveloped
    )

    signed_root = signer.sign(data=new_root, key=key, cert=cert)
    
    tree = etree.ElementTree(signed_root)

    signed_root_bytes=etree.tostring(tree, encoding="utf-8", xml_declaration=True) 

    # with open ("teste.xml", "w") as file: 
    #     signed_root.write(file, level=0) 

    encoded_file = base64.b64encode(signed_root_bytes).decode('utf-8')

    return encoded_file, thumbprint, xml_hash_before_sign


def xml_gen_lote_xml(user_info, tsl_list, dict_tsl_mom, log_id):

    der_data=open(cfgserv.cert_UT, "rb").read()
    cert_der= x509.load_der_x509_certificate(der_data, backend=default_backend())
    cert = cert_der.public_bytes(encoding=serialization.Encoding.PEM)

    pem_str = cert.decode('utf-8')
    cert_cleaned = ''.join(line for line in pem_str.splitlines() if "CERTIFICATE" not in line)

    root=LOTE.ListOfTrustedEntitiesType()

    root.set_LOTETag("http://uri.etsi.org/19612/TSLTag")
    root.set_Id("TrustServiceStatusList")

    schemeInfo = LOTE.LoTEListAndSchemeInformationType()

    schemeInfo.set_LoTEVersionIdentifier(confxml.LoTEVersionIdentifier)
    schemeInfo.set_LoTESequenceNumber(dict_tsl_mom["SequenceNumber"] + 1)
    TSLType=LOTE.NonEmptyURIType()
    TSLType.valueOf_=confxml.LoTEType["LoTL"]
    schemeInfo.LoTEType=TSLType

    #schemeOperatorName

    schemeOName = LOTE.InternationalNamesType()

    #for cycle
    op_name = parse_json_field(user_info["operator_name"])
    for item in op_name:
        schemeOName.add_Name(LOTE.MultiLangNormStringType(item['lang'], item["text"]))

    schemeInfo.SchemeOperatorName=schemeOName

    #Scheme Operator Address
    schemeOAddress= LOTE.AddressType()

    eletronic=LOTE.ElectronicAddressType()

    #for cycle
    EletronicAddress = parse_json_field(user_info["EletronicAddress"])
    for item in EletronicAddress:
        eletronic.add_URI(LOTE.NonEmptyMultiLangURIType(item['lang'],item["URI"]))
    #----------------------------------------------------#
    schemeOAddress.set_ElectronicAddress(eletronic)

    PostalAdresses=LOTE.PostalAddressListType()

    #for cycle for postal address
    postal = parse_json_field(user_info["postal_address"])
    for item in postal:
        postal=LOTE.PostalAddressType()
        postal.set_lang(item['lang'])
        postal.set_CountryName(item["CountryName"])
        postal.set_StreetAddress(item["StreetAddress"])
        postal.set_Locality(item["Locality"])
        postal.set_StateOrProvince(item["StateOrProvince"])
        postal.set_PostalCode(item["PostalCode"])
        PostalAdresses.add_PostalAddress(postal)

    schemeOAddress.set_PostalAddresses(PostalAdresses)
    schemeInfo.SchemeOperatorAddress=schemeOAddress
    
    schemeName=LOTE.InternationalNamesType()
    PolicyOrLegalNotice= LOTE.PolicyOrLegalnoticeType()
    schemeInformationURI=LOTE.NonEmptyMultiLangURIListType()
    schemeCRules= LOTE.NonEmptyMultiLangURIListType()
    Pointers=LOTE.OtherLoTEPointersType()
    

    #schemeName
    #for cycle
    for scheme in dict_tsl_mom["SchemeName"]:
        schemeName.add_Name(LOTE.MultiLangNormStringType(scheme["lang"], scheme["text"]))
    
    schemeInfo.set_SchemeName(schemeName)

    #SchemeInformationURI
    
    #for cycle
    for scheme in dict_tsl_mom["SchemeInformationURI"]:
        schemeInformationURI.add_URI(LOTE.NonEmptyMultiLangURIType(scheme["lang"], scheme["URI"]))
    
    schemeInfo.set_SchemeInformationURI(schemeInformationURI)

    #StatusDeterminationApproach
    schemeInfo.StatusDeterminationApproach=LOTE.NonEmptyURIType(confxml.LoTEStatusDeterminationApproach["LoTL"])
    
    #schemeTypeCommunityRules

#for cycle
    schemeCRules.add_URI(LOTE.NonEmptyMultiLangURIType("en", confxml.LoTESchemeTypeCommunityRules["LoTL"]))
    schemeInfo.set_SchemeTypeCommunityRules(schemeCRules)

    #SchemeTerritory
    schemeInfo.set_SchemeTerritory("EU")

    #PolicyOrLegalNotice

    #for cycle
    for scheme in dict_tsl_mom["PolicyOrLegalNotice"]:
        PolicyOrLegalNotice.add_LoTELegalNotice(LOTE.MultiLangStringType(scheme["lang"], scheme["text"]))
    
    schemeInfo.set_PolicyOrLegalNotice(PolicyOrLegalNotice)

    #HistoricalInformationPeriod
    schemeInfo.set_HistoricalInformationPeriod(dict_tsl_mom["HistoricalInformationPeriod"])

    #PointerToOtherTSL

    #OtherTSLPointerType-LoTL

    ServiceDigitalIdentities= LOTE.ServiceDigitalIdentityListType()
    serviceDigitalIdentity=LOTE.DigitalIdentityListType()

    digitalID=LOTE.DigitalIdentityType()
    digitalID.set_X509Certificate(base64.b64decode(cert_cleaned))

    serviceDigitalIdentity.add_DigitalId(digitalID)
    ServiceDigitalIdentities.add_ServiceDigitalIdentity(serviceDigitalIdentity)
    Pointer= LOTE.OtherLoTEPointerType()
    Pointer.set_ServiceDigitalIdentities(ServiceDigitalIdentities)

    #additional Info
    
    #TSLTypeAdditionalInformation

    TSLTypeAdditionalInformation=LOTE.NonEmptyURIType()
    TSLTypeAdditionalInformation.original_tagname_="LoTEType"
    TSLTypeAdditionalInformation.valueOf_=confxml.LoTEType["LoTL"]

    objectLOTE=LOTE.AnyType()
    objectLOTE.valueOf_=TSLTypeAdditionalInformation
    
    AdditionalInfo=LOTE.AdditionalInformationType()
    AdditionalInfo.add_OtherInformation(objectLOTE)

    #SchemeNameOperatorAdditionalInformation
    #for cycle
    schemeNameLOTE=LOTE.InternationalNamesType()
    schemeNameLOTE.original_tagname_="SchemeOperatorName"
    for item in op_name:
        schemeNameLOTE.add_Name(LOTE.MultiLangNormStringType(item['lang'], item["text"]))
    
    AdditionalInfo.add_OtherInformation(schemeNameLOTE)

    #SchemeTerritoryAdditionalInformation

    scheme=LOTE.AnyType()
    scheme.original_tagname_="SchemeTerritory"
    scheme.valueOf_="EU"

    AdditionalInfo.add_OtherInformation(scheme)


    #SchemeTypeCommunityRules
    
    schemetypeCommunityRules_add=LOTE.NonEmptyMultiLangURIListType()
    schemetypeCommunityRules_add.original_tagname_="SchemeTypeCommunityRules"
    
    objectLOTE_stcr=LOTE.AnyType()
    objectLOTE_stcr.original_tagname_="SchemeTypeCommunityRules"

    #for cycle
    schemetypeCommunityRules_add.add_URI(LOTE.NonEmptyMultiLangURIType("en", confxml.LoTESchemeTypeCommunityRules["LoTL"]))

    objectLOTE_stcr.valueOf_=schemetypeCommunityRules_add

    AdditionalInfo.add_OtherInformation(objectLOTE_stcr)

    #MimeType
    ObjectType=LOTE.ObjectType()
    ObjectType.original_tagname_="MimeType"
    ObjectType.set_valueOf_("application/vnd.etsi.tsl+xml")

    objectMimeType=LOTE.AnyType()
    objectMimeType.set_valueOf_(ObjectType)

    AdditionalInfo.add_OtherInformation(objectMimeType)

    last = dict_tsl_mom["SchemeInformationURI"][-1].get("URI")
    Pointer.LoTELocation=LOTE.NonEmptyURIType(last)

    Pointer.AdditionalInformation=AdditionalInfo
    Pointers.add_OtherLoTEPointer(Pointer)

    #for cycle
    for tsl_data in tsl_list:
        ServiceDigitalIdentities= LOTE.ServiceDigitalIdentityListType()
        serviceDigitalIdentity=LOTE.DigitalIdentityListType()

        #for cycle novo
        aux = func.get_old_cert(tsl_data["id"], log_id)

        for each in aux:
            digitalID=LOTE.DigitalIdentityType()
            digitalID.set_X509Certificate(base64.b64decode(each["cert"]))
            serviceDigitalIdentity.add_DigitalId(digitalID)
        #end

        ServiceDigitalIdentities.add_ServiceDigitalIdentity(serviceDigitalIdentity)
        Pointer= LOTE.OtherLoTEPointerType()
        Pointer.set_ServiceDigitalIdentities(ServiceDigitalIdentities)

        #additional Info
        
        #TSLTypeAdditionalInformation
        TSLTypeAdditionalInformation=LOTE.NonEmptyURIType()
        TSLTypeAdditionalInformation.original_tagname_="LoTEType"
        TSLTypeAdditionalInformation.valueOf_=(confxml.LoTEType["EU"])

        objectLOTE=LOTE.AnyType()
        objectLOTE.valueOf_=TSLTypeAdditionalInformation
        
        AdditionalInfo=LOTE.AdditionalInformationType()
        AdditionalInfo.add_OtherInformation(objectLOTE)

        #SchemeNameOperatorAdditionalInformation
        #for cycle
        schemeNameLOTE=LOTE.InternationalNamesType()
        schemeNameLOTE.original_tagname_="SchemeOperatorName"
        for item in tsl_data["SchemeName"]:
            schemeNameLOTE.add_Name(LOTE.MultiLangNormStringType(item['lang'], item["text"]))
        
        AdditionalInfo.add_OtherInformation(schemeNameLOTE)

        #SchemeTerritoryAdditionalInformatio

        scheme=LOTE.AnyType()
        scheme.original_tagname_="SchemeTerritory"
        scheme.valueOf_=tsl_data["schemeTerritory"]

        AdditionalInfo.add_OtherInformation(scheme)


        #SchemeTypeCommunityRules
        
        schemetypeCommunityRules_add=LOTE.NonEmptyMultiLangURIListType()
        schemetypeCommunityRules_add.original_tagname_="SchemeTypeCommunityRules"
        
        objectLOTE_stcr=LOTE.AnyType()
        objectLOTE_stcr.original_tagname_="SchemeTypeCommunityRules"

        #for cycle
        schemetypeCommunityRules_add.add_URI(LOTE.NonEmptyMultiLangURIType("en", confxml.LoTESchemeTypeCommunityRules["EU"]))
        objectLOTE_stcr.valueOf_=schemetypeCommunityRules_add

        AdditionalInfo.add_OtherInformation(objectLOTE_stcr)

        #MimeType
        ObjectType=LOTE.ObjectType()
        ObjectType.original_tagname_="MimeType"
        ObjectType.set_valueOf_("application/vnd.etsi.tsl+xml")

        objectMimeType=LOTE.AnyType()
        objectMimeType.set_valueOf_(ObjectType)

        AdditionalInfo.add_OtherInformation(objectMimeType)

        last= tsl_data["SchemeInformationURI"][-1].get("URI")
        Pointer.LoTELocation=LOTE.NonEmptyURIType(last)

        Pointer.AdditionalInformation=AdditionalInfo
        Pointers.add_OtherLoTEPointer(Pointer)
    
    schemeInfo.PointersToOtherLoTE=Pointers
    
    schemeInfo.ListIssueDateTime=dict_tsl_mom["issue_date"]
    #Next Update
    NUpdate=LOTE.NextUpdateType()
    NUpdate.set_dateTime(dict_tsl_mom["next_update"])
    schemeInfo.NextUpdate= NUpdate

    #DistribuitionPoints

    #for cycle
    URIDP=LOTE.NonEmptyURIListType()
    last= dict_tsl_mom["SchemeInformationURI"][-1].get("URI")
    URIDP.add_URI(LOTE.NonEmptyURIType(last))

    schemeInfo.DistributionPoints=URIDP

    root.ListAndSchemeInformation=schemeInfo

    xml_buffer=StringIO()
    root.export(xml_buffer,0,"")
    xml_string=xml_buffer.getvalue()

    content=xml_string
    content = re.sub(r'xmlns:ns0="([^"]+)"', r'xmlns="\1"', content)

    content = re.sub(r'<ns0:', r'<', content)
    content = re.sub(r'</ns0:', r'</', content)

    # with open ("cert_UT.pem", "rb") as file: 
    #     cert = file.read()
    #     cert=x509.load_pem_x509_certificate(cert)

    cert_for_hash=x509.load_pem_x509_certificate(cert, default_backend())
    thumbprint= hashlib.sha256(cert_for_hash.tbs_certificate_bytes).hexdigest()

    # with open ("privkey_UT.pem", "rb") as key_file: 
    #     key = serialization.load_pem_private_key(key_file.read(),password=None,backend=default_backend())
        
    key=open(cfgserv.priv_key_UT, "rb").read()
    
    rootTemp=ET.fromstring(content)

    new_root = ET.Element(rootTemp.tag, attrib=rootTemp.attrib)
    new_root.text = rootTemp.text

    new_root.attrib["xmlns:ns2"] = "http://www.w3.org/2000/09/xmldsig#"
    new_root.attrib["xmlns:ns3"] = "http://uri.etsi.org/01903/v1.3.2#"

    for child in rootTemp:
        new_root.append(child )
    
    ET.register_namespace("", "http://uri.etsi.org/019602/v1#")

    root_temp_str = ET.tostring(rootTemp, encoding="utf-8")
    root_lxml = etree.fromstring(root_temp_str)
    root_bytes = etree.tostring(root_lxml, method="c14n")
    xml_hash_before_sign = hashlib.sha256(root_bytes).hexdigest()

    data_object_format = XAdESDataObjectFormat(
        Description="TSL signature",
        MimeType="text/xml",
    )

    signer = XAdESSigner(
        claimed_roles=["signer"],
        data_object_format=data_object_format,
        c14n_algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315",
        signature_algorithm=algorithms.SignatureMethod.ECDSA_SHA256,
        method=methods.enveloped
    )

    signed_root = signer.sign(data=new_root, key=key, cert=cert)
    
    tree = etree.ElementTree(signed_root)

    signed_root_bytes=etree.tostring(tree, encoding="utf-8", xml_declaration=True) 

    encoded_file = base64.b64encode(signed_root_bytes).decode('utf-8')


    return encoded_file, thumbprint, xml_hash_before_sign


def xml_lote_validator(file):

    # Load Schema
    with open(confxml.LoTEschema, 'rb') as f:
        schema_root = etree.parse(f)
        schema = etree.XMLSchema(schema_root)

    # Load XML
    # with open("LOTEe2.xml", 'rb') as f:
    #     xml_tree = etree.parse(f)

    xml_tree= etree.fromstring(file)

    # Validate XML
    if schema.validate(xml_tree):
        return 200,"Valid XML"
    else:
        msg= "Invalid XML"
        for error in schema.error_log:
            msg = msg + f"\nLine {error.line}: {error.message}"
        
        return 500, msg

    