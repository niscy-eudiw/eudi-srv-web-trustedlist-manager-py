#!/usr/bin/env python

#
# Generated Wed Feb 18 16:01:37 2026 by generateDS.py version 2.44.3.
# Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)]
#
# Command line options:
#   ('-o', 'lote_api.py')
#   ('-s', 'lote_sub.py')
#   ('--super', 'lote_api')
#
# Command line arguments:
#   1960201_xsd_schema.xsd
#
# Command line:
#   generateDS.py -o "lote_api.py" -s "lote_sub.py" --super="lote_api" 1960201_xsd_schema.xsd
#
# Current working directory (os.getcwd()):
#   xml_gen_lote
#

import os
import sys
from lxml import etree as etree_

import lote_api as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Globals
#

ExternalEncoding = ''
SaveElementTreeNode = True

#
# Data representation classes
#


class InternationalNamesTypeSub(supermod.InternationalNamesType):
    def __init__(self, Name=None, **kwargs_):
        super(InternationalNamesTypeSub, self).__init__(Name,  **kwargs_)
supermod.InternationalNamesType.subclass = InternationalNamesTypeSub
# end class InternationalNamesTypeSub


class MultiLangNormStringTypeSub(supermod.MultiLangNormStringType):
    def __init__(self, lang=None, valueOf_=None, **kwargs_):
        super(MultiLangNormStringTypeSub, self).__init__(lang, valueOf_,  **kwargs_)
supermod.MultiLangNormStringType.subclass = MultiLangNormStringTypeSub
# end class MultiLangNormStringTypeSub


class MultiLangStringTypeSub(supermod.MultiLangStringType):
    def __init__(self, lang=None, valueOf_=None, **kwargs_):
        super(MultiLangStringTypeSub, self).__init__(lang, valueOf_,  **kwargs_)
supermod.MultiLangStringType.subclass = MultiLangStringTypeSub
# end class MultiLangStringTypeSub


class AddressTypeSub(supermod.AddressType):
    def __init__(self, PostalAddresses=None, ElectronicAddress=None, **kwargs_):
        super(AddressTypeSub, self).__init__(PostalAddresses, ElectronicAddress,  **kwargs_)
supermod.AddressType.subclass = AddressTypeSub
# end class AddressTypeSub


class PostalAddressListTypeSub(supermod.PostalAddressListType):
    def __init__(self, PostalAddress=None, **kwargs_):
        super(PostalAddressListTypeSub, self).__init__(PostalAddress,  **kwargs_)
supermod.PostalAddressListType.subclass = PostalAddressListTypeSub
# end class PostalAddressListTypeSub


class PostalAddressTypeSub(supermod.PostalAddressType):
    def __init__(self, lang=None, StreetAddress=None, Locality=None, StateOrProvince=None, PostalCode=None, CountryName=None, **kwargs_):
        super(PostalAddressTypeSub, self).__init__(lang, StreetAddress, Locality, StateOrProvince, PostalCode, CountryName,  **kwargs_)
supermod.PostalAddressType.subclass = PostalAddressTypeSub
# end class PostalAddressTypeSub


class ElectronicAddressTypeSub(supermod.ElectronicAddressType):
    def __init__(self, URI=None, **kwargs_):
        super(ElectronicAddressTypeSub, self).__init__(URI,  **kwargs_)
supermod.ElectronicAddressType.subclass = ElectronicAddressTypeSub
# end class ElectronicAddressTypeSub


class AnyTypeSub(supermod.AnyType):
    def __init__(self, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, extensiontype_=None, **kwargs_):
        super(AnyTypeSub, self).__init__(anytypeobjs_, valueOf_, mixedclass_, content_, extensiontype_,  **kwargs_)
supermod.AnyType.subclass = AnyTypeSub
# end class AnyTypeSub


class ExtensionTypeSub(supermod.ExtensionType):
    def __init__(self, anytypeobjs_=None, Critical=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(ExtensionTypeSub, self).__init__(anytypeobjs_, Critical, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.ExtensionType.subclass = ExtensionTypeSub
# end class ExtensionTypeSub


class ExtensionsListTypeSub(supermod.ExtensionsListType):
    def __init__(self, Extension=None, **kwargs_):
        super(ExtensionsListTypeSub, self).__init__(Extension,  **kwargs_)
supermod.ExtensionsListType.subclass = ExtensionsListTypeSub
# end class ExtensionsListTypeSub


class NonEmptyMultiLangURIListTypeSub(supermod.NonEmptyMultiLangURIListType):
    def __init__(self, URI=None, **kwargs_):
        super(NonEmptyMultiLangURIListTypeSub, self).__init__(URI,  **kwargs_)
supermod.NonEmptyMultiLangURIListType.subclass = NonEmptyMultiLangURIListTypeSub
# end class NonEmptyMultiLangURIListTypeSub


class NonEmptyURIListTypeSub(supermod.NonEmptyURIListType):
    def __init__(self, URI=None, **kwargs_):
        super(NonEmptyURIListTypeSub, self).__init__(URI,  **kwargs_)
supermod.NonEmptyURIListType.subclass = NonEmptyURIListTypeSub
# end class NonEmptyURIListTypeSub


class ListOfTrustedEntitiesTypeSub(supermod.ListOfTrustedEntitiesType):
    def __init__(self, LOTETag=None, Id=None, ListAndSchemeInformation=None, TrustedEntitiesList=None, Signature=None, **kwargs_):
        super(ListOfTrustedEntitiesTypeSub, self).__init__(LOTETag, Id, ListAndSchemeInformation, TrustedEntitiesList, Signature,  **kwargs_)
supermod.ListOfTrustedEntitiesType.subclass = ListOfTrustedEntitiesTypeSub
# end class ListOfTrustedEntitiesTypeSub


class TrustedEntitiesListTypeSub(supermod.TrustedEntitiesListType):
    def __init__(self, TrustedEntity=None, **kwargs_):
        super(TrustedEntitiesListTypeSub, self).__init__(TrustedEntity,  **kwargs_)
supermod.TrustedEntitiesListType.subclass = TrustedEntitiesListTypeSub
# end class TrustedEntitiesListTypeSub


class LoTEListAndSchemeInformationTypeSub(supermod.LoTEListAndSchemeInformationType):
    def __init__(self, LoTEVersionIdentifier=None, LoTESequenceNumber=None, LoTEType=None, SchemeOperatorName=None, SchemeOperatorAddress=None, SchemeName=None, SchemeInformationURI=None, StatusDeterminationApproach=None, SchemeTypeCommunityRules=None, SchemeTerritory=None, PolicyOrLegalNotice=None, HistoricalInformationPeriod=None, PointersToOtherLoTE=None, ListIssueDateTime=None, NextUpdate=None, DistributionPoints=None, SchemeExtensions=None, **kwargs_):
        super(LoTEListAndSchemeInformationTypeSub, self).__init__(LoTEVersionIdentifier, LoTESequenceNumber, LoTEType, SchemeOperatorName, SchemeOperatorAddress, SchemeName, SchemeInformationURI, StatusDeterminationApproach, SchemeTypeCommunityRules, SchemeTerritory, PolicyOrLegalNotice, HistoricalInformationPeriod, PointersToOtherLoTE, ListIssueDateTime, NextUpdate, DistributionPoints, SchemeExtensions,  **kwargs_)
supermod.LoTEListAndSchemeInformationType.subclass = LoTEListAndSchemeInformationTypeSub
# end class LoTEListAndSchemeInformationTypeSub


class PolicyOrLegalnoticeTypeSub(supermod.PolicyOrLegalnoticeType):
    def __init__(self, LoTEPolicy=None, LoTELegalNotice=None, **kwargs_):
        super(PolicyOrLegalnoticeTypeSub, self).__init__(LoTEPolicy, LoTELegalNotice,  **kwargs_)
supermod.PolicyOrLegalnoticeType.subclass = PolicyOrLegalnoticeTypeSub
# end class PolicyOrLegalnoticeTypeSub


class NextUpdateTypeSub(supermod.NextUpdateType):
    def __init__(self, dateTime=None, **kwargs_):
        super(NextUpdateTypeSub, self).__init__(dateTime,  **kwargs_)
supermod.NextUpdateType.subclass = NextUpdateTypeSub
# end class NextUpdateTypeSub


class OtherLoTEPointersTypeSub(supermod.OtherLoTEPointersType):
    def __init__(self, OtherLoTEPointer=None, **kwargs_):
        super(OtherLoTEPointersTypeSub, self).__init__(OtherLoTEPointer,  **kwargs_)
supermod.OtherLoTEPointersType.subclass = OtherLoTEPointersTypeSub
# end class OtherLoTEPointersTypeSub


class OtherLoTEPointerTypeSub(supermod.OtherLoTEPointerType):
    def __init__(self, ServiceDigitalIdentities=None, LoTELocation=None, AdditionalInformation=None, **kwargs_):
        super(OtherLoTEPointerTypeSub, self).__init__(ServiceDigitalIdentities, LoTELocation, AdditionalInformation,  **kwargs_)
supermod.OtherLoTEPointerType.subclass = OtherLoTEPointerTypeSub
# end class OtherLoTEPointerTypeSub


class ServiceDigitalIdentityListTypeSub(supermod.ServiceDigitalIdentityListType):
    def __init__(self, ServiceDigitalIdentity=None, **kwargs_):
        super(ServiceDigitalIdentityListTypeSub, self).__init__(ServiceDigitalIdentity,  **kwargs_)
supermod.ServiceDigitalIdentityListType.subclass = ServiceDigitalIdentityListTypeSub
# end class ServiceDigitalIdentityListTypeSub


class AdditionalInformationTypeSub(supermod.AdditionalInformationType):
    def __init__(self, TextualInformation=None, OtherInformation=None, **kwargs_):
        super(AdditionalInformationTypeSub, self).__init__(TextualInformation, OtherInformation,  **kwargs_)
supermod.AdditionalInformationType.subclass = AdditionalInformationTypeSub
# end class AdditionalInformationTypeSub


class TETypeSub(supermod.TEType):
    def __init__(self, TrustedEntityInformation=None, TrustedEntityServices=None, **kwargs_):
        super(TETypeSub, self).__init__(TrustedEntityInformation, TrustedEntityServices,  **kwargs_)
supermod.TEType.subclass = TETypeSub
# end class TETypeSub


class TrustedEntityInformationTypeSub(supermod.TrustedEntityInformationType):
    def __init__(self, TEName=None, TETradeName=None, TEAddress=None, TEInformationURI=None, TEInformationExtensions=None, **kwargs_):
        super(TrustedEntityInformationTypeSub, self).__init__(TEName, TETradeName, TEAddress, TEInformationURI, TEInformationExtensions,  **kwargs_)
supermod.TrustedEntityInformationType.subclass = TrustedEntityInformationTypeSub
# end class TrustedEntityInformationTypeSub


class TrustedEntityServicesListTypeSub(supermod.TrustedEntityServicesListType):
    def __init__(self, TrustedEntityService=None, **kwargs_):
        super(TrustedEntityServicesListTypeSub, self).__init__(TrustedEntityService,  **kwargs_)
supermod.TrustedEntityServicesListType.subclass = TrustedEntityServicesListTypeSub
# end class TrustedEntityServicesListTypeSub


class TrustedEntityServiceTypeSub(supermod.TrustedEntityServiceType):
    def __init__(self, ServiceInformation=None, ServiceHistory=None, **kwargs_):
        super(TrustedEntityServiceTypeSub, self).__init__(ServiceInformation, ServiceHistory,  **kwargs_)
supermod.TrustedEntityServiceType.subclass = TrustedEntityServiceTypeSub
# end class TrustedEntityServiceTypeSub


class TEServiceInformationTypeSub(supermod.TEServiceInformationType):
    def __init__(self, ServiceTypeIdentifier=None, ServiceName=None, ServiceDigitalIdentity=None, ServiceStatus=None, StatusStartingTime=None, SchemeServiceDefinitionURI=None, ServiceSupplyPoints=None, TEServiceDefinitionURI=None, ServiceInformationExtensions=None, **kwargs_):
        super(TEServiceInformationTypeSub, self).__init__(ServiceTypeIdentifier, ServiceName, ServiceDigitalIdentity, ServiceStatus, StatusStartingTime, SchemeServiceDefinitionURI, ServiceSupplyPoints, TEServiceDefinitionURI, ServiceInformationExtensions,  **kwargs_)
supermod.TEServiceInformationType.subclass = TEServiceInformationTypeSub
# end class TEServiceInformationTypeSub


class ServiceSupplyPointsTypeSub(supermod.ServiceSupplyPointsType):
    def __init__(self, ServiceSupplyPoint=None, **kwargs_):
        super(ServiceSupplyPointsTypeSub, self).__init__(ServiceSupplyPoint,  **kwargs_)
supermod.ServiceSupplyPointsType.subclass = ServiceSupplyPointsTypeSub
# end class ServiceSupplyPointsTypeSub


class DigitalIdentityListTypeSub(supermod.DigitalIdentityListType):
    def __init__(self, DigitalId=None, **kwargs_):
        super(DigitalIdentityListTypeSub, self).__init__(DigitalId,  **kwargs_)
supermod.DigitalIdentityListType.subclass = DigitalIdentityListTypeSub
# end class DigitalIdentityListTypeSub


class DigitalIdentityTypeSub(supermod.DigitalIdentityType):
    def __init__(self, X509Certificate=None, X509SubjectName=None, KeyValue=None, X509SKI=None, OtherId=None, **kwargs_):
        super(DigitalIdentityTypeSub, self).__init__(X509Certificate, X509SubjectName, KeyValue, X509SKI, OtherId,  **kwargs_)
supermod.DigitalIdentityType.subclass = DigitalIdentityTypeSub
# end class DigitalIdentityTypeSub


class ServiceHistoryTypeSub(supermod.ServiceHistoryType):
    def __init__(self, ServiceHistoryInstance=None, **kwargs_):
        super(ServiceHistoryTypeSub, self).__init__(ServiceHistoryInstance,  **kwargs_)
supermod.ServiceHistoryType.subclass = ServiceHistoryTypeSub
# end class ServiceHistoryTypeSub


class ServiceHistoryInstanceTypeSub(supermod.ServiceHistoryInstanceType):
    def __init__(self, ServiceTypeIdentifier=None, ServiceName=None, ServiceDigitalIdentity=None, ServiceStatus=None, StatusStartingTime=None, ServiceInformationExtensions=None, **kwargs_):
        super(ServiceHistoryInstanceTypeSub, self).__init__(ServiceTypeIdentifier, ServiceName, ServiceDigitalIdentity, ServiceStatus, StatusStartingTime, ServiceInformationExtensions,  **kwargs_)
supermod.ServiceHistoryInstanceType.subclass = ServiceHistoryInstanceTypeSub
# end class ServiceHistoryInstanceTypeSub


class SignatureTypeSub(supermod.SignatureType):
    def __init__(self, Id=None, SignedInfo=None, SignatureValue=None, KeyInfo=None, Object=None, **kwargs_):
        super(SignatureTypeSub, self).__init__(Id, SignedInfo, SignatureValue, KeyInfo, Object,  **kwargs_)
supermod.SignatureType.subclass = SignatureTypeSub
# end class SignatureTypeSub


class SignatureValueTypeSub(supermod.SignatureValueType):
    def __init__(self, Id=None, valueOf_=None, **kwargs_):
        super(SignatureValueTypeSub, self).__init__(Id, valueOf_,  **kwargs_)
supermod.SignatureValueType.subclass = SignatureValueTypeSub
# end class SignatureValueTypeSub


class SignedInfoTypeSub(supermod.SignedInfoType):
    def __init__(self, Id=None, CanonicalizationMethod=None, SignatureMethod=None, Reference=None, **kwargs_):
        super(SignedInfoTypeSub, self).__init__(Id, CanonicalizationMethod, SignatureMethod, Reference,  **kwargs_)
supermod.SignedInfoType.subclass = SignedInfoTypeSub
# end class SignedInfoTypeSub


class CanonicalizationMethodTypeSub(supermod.CanonicalizationMethodType):
    def __init__(self, Algorithm=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(CanonicalizationMethodTypeSub, self).__init__(Algorithm, anytypeobjs_, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.CanonicalizationMethodType.subclass = CanonicalizationMethodTypeSub
# end class CanonicalizationMethodTypeSub


class SignatureMethodTypeSub(supermod.SignatureMethodType):
    def __init__(self, Algorithm=None, HMACOutputLength=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(SignatureMethodTypeSub, self).__init__(Algorithm, HMACOutputLength, anytypeobjs_, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.SignatureMethodType.subclass = SignatureMethodTypeSub
# end class SignatureMethodTypeSub


class ReferenceTypeSub(supermod.ReferenceType):
    def __init__(self, Id=None, URI=None, Type=None, Transforms=None, DigestMethod=None, DigestValue=None, **kwargs_):
        super(ReferenceTypeSub, self).__init__(Id, URI, Type, Transforms, DigestMethod, DigestValue,  **kwargs_)
supermod.ReferenceType.subclass = ReferenceTypeSub
# end class ReferenceTypeSub


class TransformsTypeSub(supermod.TransformsType):
    def __init__(self, Transform=None, **kwargs_):
        super(TransformsTypeSub, self).__init__(Transform,  **kwargs_)
supermod.TransformsType.subclass = TransformsTypeSub
# end class TransformsTypeSub


class TransformTypeSub(supermod.TransformType):
    def __init__(self, Algorithm=None, anytypeobjs_=None, XPath=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(TransformTypeSub, self).__init__(Algorithm, anytypeobjs_, XPath, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.TransformType.subclass = TransformTypeSub
# end class TransformTypeSub


class DigestMethodTypeSub(supermod.DigestMethodType):
    def __init__(self, Algorithm=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(DigestMethodTypeSub, self).__init__(Algorithm, anytypeobjs_, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.DigestMethodType.subclass = DigestMethodTypeSub
# end class DigestMethodTypeSub


class KeyInfoTypeSub(supermod.KeyInfoType):
    def __init__(self, Id=None, KeyName=None, KeyValue=None, RetrievalMethod=None, X509Data=None, PGPData=None, SPKIData=None, MgmtData=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(KeyInfoTypeSub, self).__init__(Id, KeyName, KeyValue, RetrievalMethod, X509Data, PGPData, SPKIData, MgmtData, anytypeobjs_, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.KeyInfoType.subclass = KeyInfoTypeSub
# end class KeyInfoTypeSub


class KeyValueTypeSub(supermod.KeyValueType):
    def __init__(self, DSAKeyValue=None, RSAKeyValue=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(KeyValueTypeSub, self).__init__(DSAKeyValue, RSAKeyValue, anytypeobjs_, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.KeyValueType.subclass = KeyValueTypeSub
# end class KeyValueTypeSub


class RetrievalMethodTypeSub(supermod.RetrievalMethodType):
    def __init__(self, URI=None, Type=None, Transforms=None, **kwargs_):
        super(RetrievalMethodTypeSub, self).__init__(URI, Type, Transforms,  **kwargs_)
supermod.RetrievalMethodType.subclass = RetrievalMethodTypeSub
# end class RetrievalMethodTypeSub


class X509DataTypeSub(supermod.X509DataType):
    def __init__(self, X509IssuerSerial=None, X509SKI=None, X509SubjectName=None, X509Certificate=None, X509CRL=None, anytypeobjs_=None, **kwargs_):
        super(X509DataTypeSub, self).__init__(X509IssuerSerial, X509SKI, X509SubjectName, X509Certificate, X509CRL, anytypeobjs_,  **kwargs_)
supermod.X509DataType.subclass = X509DataTypeSub
# end class X509DataTypeSub


class X509IssuerSerialTypeSub(supermod.X509IssuerSerialType):
    def __init__(self, X509IssuerName=None, X509SerialNumber=None, **kwargs_):
        super(X509IssuerSerialTypeSub, self).__init__(X509IssuerName, X509SerialNumber,  **kwargs_)
supermod.X509IssuerSerialType.subclass = X509IssuerSerialTypeSub
# end class X509IssuerSerialTypeSub


class PGPDataTypeSub(supermod.PGPDataType):
    def __init__(self, PGPKeyID=None, PGPKeyPacket=None, anytypeobjs_=None, **kwargs_):
        super(PGPDataTypeSub, self).__init__(PGPKeyID, PGPKeyPacket, anytypeobjs_,  **kwargs_)
supermod.PGPDataType.subclass = PGPDataTypeSub
# end class PGPDataTypeSub


class SPKIDataTypeSub(supermod.SPKIDataType):
    def __init__(self, SPKISexp=None, anytypeobjs_=None, **kwargs_):
        super(SPKIDataTypeSub, self).__init__(SPKISexp, anytypeobjs_,  **kwargs_)
supermod.SPKIDataType.subclass = SPKIDataTypeSub
# end class SPKIDataTypeSub


class ObjectTypeSub(supermod.ObjectType):
    def __init__(self, Id=None, MimeType=None, Encoding=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(ObjectTypeSub, self).__init__(Id, MimeType, Encoding, anytypeobjs_, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.ObjectType.subclass = ObjectTypeSub
# end class ObjectTypeSub


class ManifestTypeSub(supermod.ManifestType):
    def __init__(self, Id=None, Reference=None, **kwargs_):
        super(ManifestTypeSub, self).__init__(Id, Reference,  **kwargs_)
supermod.ManifestType.subclass = ManifestTypeSub
# end class ManifestTypeSub


class SignaturePropertiesTypeSub(supermod.SignaturePropertiesType):
    def __init__(self, Id=None, SignatureProperty=None, **kwargs_):
        super(SignaturePropertiesTypeSub, self).__init__(Id, SignatureProperty,  **kwargs_)
supermod.SignaturePropertiesType.subclass = SignaturePropertiesTypeSub
# end class SignaturePropertiesTypeSub


class SignaturePropertyTypeSub(supermod.SignaturePropertyType):
    def __init__(self, Target=None, Id=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(SignaturePropertyTypeSub, self).__init__(Target, Id, anytypeobjs_, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.SignaturePropertyType.subclass = SignaturePropertyTypeSub
# end class SignaturePropertyTypeSub


class DSAKeyValueTypeSub(supermod.DSAKeyValueType):
    def __init__(self, P=None, Q=None, G=None, Y=None, J=None, Seed=None, PgenCounter=None, **kwargs_):
        super(DSAKeyValueTypeSub, self).__init__(P, Q, G, Y, J, Seed, PgenCounter,  **kwargs_)
supermod.DSAKeyValueType.subclass = DSAKeyValueTypeSub
# end class DSAKeyValueTypeSub


class RSAKeyValueTypeSub(supermod.RSAKeyValueType):
    def __init__(self, Modulus=None, Exponent=None, **kwargs_):
        super(RSAKeyValueTypeSub, self).__init__(Modulus, Exponent,  **kwargs_)
supermod.RSAKeyValueType.subclass = RSAKeyValueTypeSub
# end class RSAKeyValueTypeSub


class NonEmptyURITypeSub(supermod.NonEmptyURIType):
    def __init__(self, valueOf_=None, extensiontype_=None, **kwargs_):
        super(NonEmptyURITypeSub, self).__init__(valueOf_, extensiontype_,  **kwargs_)
supermod.NonEmptyURIType.subclass = NonEmptyURITypeSub
# end class NonEmptyURITypeSub


class DigestValueTypeSub(supermod.DigestValueType):
    def __init__(self, valueOf_=None, **kwargs_):
        super(DigestValueTypeSub, self).__init__(valueOf_,  **kwargs_)
supermod.DigestValueType.subclass = DigestValueTypeSub
# end class DigestValueTypeSub


class NonEmptyMultiLangURITypeSub(supermod.NonEmptyMultiLangURIType):
    def __init__(self, lang=None, valueOf_=None, **kwargs_):
        super(NonEmptyMultiLangURITypeSub, self).__init__(lang, valueOf_,  **kwargs_)
supermod.NonEmptyMultiLangURIType.subclass = NonEmptyMultiLangURITypeSub
# end class NonEmptyMultiLangURITypeSub


class AttributedNonEmptyURITypeSub(supermod.AttributedNonEmptyURIType):
    def __init__(self, type_=None, valueOf_=None, **kwargs_):
        super(AttributedNonEmptyURITypeSub, self).__init__(type_, valueOf_,  **kwargs_)
supermod.AttributedNonEmptyURIType.subclass = AttributedNonEmptyURITypeSub
# end class AttributedNonEmptyURITypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'InternationalNamesType'
        rootClass = supermod.InternationalNamesType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:lote="http://uri.etsi.org/019602/v1#"',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'InternationalNamesType'
        rootClass = supermod.InternationalNamesType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'InternationalNamesType'
        rootClass = supermod.InternationalNamesType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:lote="http://uri.etsi.org/019602/v1#"')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'InternationalNamesType'
        rootClass = supermod.InternationalNamesType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from lote_api import *\n\n')
        sys.stdout.write('import lote_api as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
