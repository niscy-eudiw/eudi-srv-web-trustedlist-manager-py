# coding: latin-1
###############################################################################
# Copyright (c) 2023 European Commission
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
"""
This xml_config.py contains configuration data for the xml generator. 

NOTE: You should only change it if you understand what you're doing.
"""

class ConfXML:

    TLSVersionIdentifier=6

    TSLType={
        "EU":"http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric",
        "LoTL":"http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUlistofthelists"
    }

    StatusDeterminationApproach={
        "EU":"http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/EUappropriate",
        "LoTL":"http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/EUlistofthelists"
    }

    SchemeTypeCommunityRules={
        "EU":"http://uri.etsi.org/TrstSvc/TrustedList/schemerules/EUcommon",
        "LoTL":"http://uri.etsi.org/TrstSvc/TrustedList/schemerules/EUlistofthelists",
        "Country":"http://uri.etsi.org/TrstSvc/TrustedList/schemerules/"
    }

    DistributionPoints={
        "LoTL":"https://trustedlist.serviceproviders.eudiw.dev/LOTL/01.xml"
    }

    lotl_location="https://trustedlist.serviceproviders.eudiw.dev/LOTL/01.xml"

    HistoricalInformationPeriod=65535

    #schema = r"app\xml_gen\ts_119612v020101_xsd_modified.xsd"
    schema = "/app/xml_gen/ts_119612v020101_xsd_modified.xsd"

    #months
    validity=6

    #LoTE

    
    LoTEVersionIdentifier=1
    
    LoTEType={
        "EU":"http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList",
        "LoTL":"http://uri.etsi.org/19602/LoTEType/EURegistrarsAndRegistersList"
    }

    
    LoTEStatusDeterminationApproach={
        "EU":"http://uri.etsi.org/19602/PIDProvidersList/StatusDetn/EU",
        "LoTL":"http://uri.etsi.org/19602/RegistrarsAndRegistersList/StatusDetn/EU",
        "http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList":"http://uri.etsi.org/19602/PIDProvidersList/StatusDetn/EU",
        "http://uri.etsi.org/19602/LoTEType/EUWalletProvidersList":"http://uri.etsi.org/19602/WalletProvidersList/StatusDetn/EU",
        "http://uri.etsi.org/19602/LoTEType/EUWRPACProvidersList":"http://uri.etsi.org/19602/WRPACProvidersList/StatusDetn/EU",
        "http://uri.etsi.org/19602/LoTEType/EUWRPRCProvidersList":"http://uri.etsi.org/19602/WRPRCrovidersList/StatusDetn/EU",
        "http://uri.etsi.org/19602/LoTEType/EUPubEAAProvidersList":"http://uri.etsi.org/19602/PubEAAProvidersList/StatusDetn/EU",
        "http://uri.etsi.org/19602/LoTEType/EURegistrarsAndRegistersList":"http://uri.etsi.org/19602/RegistrarsAndRegistersList/StatusDetn/EU"
    }

    LoTESchemeTypeCommunityRules={
        "EU":"http://uri.etsi.org/19602/PIDProviders/schemerules/EU",
        "LoTL":"http://uri.etsi.org/19602/RegistrarsAndRegistersList/schemerules/EU",
        "http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList":"http://uri.etsi.org/19602/PIDProviders/schemerules/EU",
        "http://uri.etsi.org/19602/LoTEType/EUWalletProvidersList":"http://uri.etsi.org/19602/WalletProvidersList/schemerules/EU",
        "http://uri.etsi.org/19602/LoTEType/EUWRPACProvidersList":"http://uri.etsi.org/19602/WRPACProvidersList/schemerules/EU",
        "http://uri.etsi.org/19602/LoTEType/EUWRPRCProvidersList":"http://uri.etsi.org/19602/WRPRCProvidersList/schemerules/EU",
        "http://uri.etsi.org/19602/LoTEType/EUPubEAAProvidersList":"http://uri.etsi.org/19602/PubEAAProvidersList/schemerules/EU",
        "http://uri.etsi.org/19602/LoTEType/EURegistrarsAndRegistersList":"http://uri.etsi.org/19602/RegistrarsAndRegistersList/schemerules/EU"
    }

    LoTElotl_location="https://trustedlist.serviceproviders.eudiw.dev/LOTE/01.xml"

    LoTEHistoricalInformationPeriod=65535

    #LoTEschema = r"app\xml_gen_lote\1960201_xsd_schema.xsd"
    LoTEschema = "/app/xml_gen_lote/1960201_xsd_schema.xsd"

    #months
    LoTEvalidity=6
