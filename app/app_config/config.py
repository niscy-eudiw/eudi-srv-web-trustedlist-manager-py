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
This config.py contains configuration data for the age-over-poc Web service. 

NOTE: You should only change it if you understand what you're doing.
"""

import logging
from logging.handlers import TimedRotatingFileHandler
import os
from flask import  session
import logging
from logging.handlers import TimedRotatingFileHandler


class ConfService:
    
    two_operators = False

    secret_key = os.urandom(32).hex()

    #service_url = "http://127.0.0.1:5000/"
    service_url = os.getenv("SERVICE_URL", "https://trustedlist.serviceproviders.eudiw.dev/")

    #trusted_CAs_path = "app\certs"
    trusted_CAs_path = os.getenv("TRUSTED_CAS_PATH")

    deffered_expiry = 100

    url_verifier= os.getenv("VERIFIER")
    
    sca_signer_url=os.getenv("SCA_SIGNER_URL")


    lote_and_tsl_ids={
    }

    test_lotl=[
        "https://trustedlist.serviceproviders.eudiw.dev/TL/EU/01.xml", "https://trustedlist.serviceproviders.eudiw.dev/TL/AT/01.xml", 
        "https://trustedlist.serviceproviders.eudiw.dev/TL/CZ/01.xml", "https://trustedlist.serviceproviders.eudiw.dev/TL/DE/01.xml", 
        "https://trustedlist.serviceproviders.eudiw.dev/TL/EE/01.xml", "https://trustedlist.serviceproviders.eudiw.dev/TL/FI/01.xml", 
        "https://trustedlist.serviceproviders.eudiw.dev/TL/FR/01.xml", "https://trustedlist.serviceproviders.eudiw.dev/TL/GR/01.xml", 
        "https://trustedlist.serviceproviders.eudiw.dev/TL/HU/01.xml", "https://trustedlist.serviceproviders.eudiw.dev/TL/IT/01.xml", 
        "https://trustedlist.serviceproviders.eudiw.dev/TL/LU/01.xml", "https://trustedlist.serviceproviders.eudiw.dev/TL/NL/01.xml", 
        "https://trustedlist.serviceproviders.eudiw.dev/TL/NO/01.xml", "https://trustedlist.serviceproviders.eudiw.dev/TL/PL/01.xml", 
        "https://trustedlist.serviceproviders.eudiw.dev/TL/PT/01.xml", "https://trustedlist.serviceproviders.eudiw.dev/TL/UT/01.xml", 
        "https://trustedlist.serviceproviders.eudiw.dev/LOTL/01.xml", 
    ]

    test_lote=[
      "https://trustedlist.serviceproviders.eudiw.dev/LOTE/json/PIDProviders.jwt","https://trustedlist.serviceproviders.eudiw.dev/LOTE/json/PubEAAProviders.jwt",
      "https://trustedlist.serviceproviders.eudiw.dev/LOTE/json/RegistrarsAndRegisters.jwt ","https://trustedlist.serviceproviders.eudiw.dev/LOTE/json/WalletProviders.jwt",
      "https://trustedlist.serviceproviders.eudiw.dev/LOTE/json/WRPACProviders.jwt","https://trustedlist.serviceproviders.eudiw.dev/LOTE/json/WRPRCProviders.jwt"    ]


    roles = {
      "tsp_op":"TSP Operator",
      "tsl_op":"TSL Operator",
      "lotl_op": "LoTL Operator"
    }

    #Form data- TSL

    qualifiers = {
      "QCForESig": "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCForESig",
      "QCStatement": "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCStatement",
      "QCQSCDStatusAsInCert": "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCQSCDStatusAsInCert"
    }

    lang = {
      "Portugues": "pt", 
      "English": "en"
    }

    SchemeTypeCommunityRules ={
      "Eu Common": "https://uri.etsi.org/TrstSvc/TrustedList/schemerules/EUcommon", 
      "Scheme Territory": "http://uri.etsi.org/TrstSvc/TrustedList/schemerules/",
    }

    TSLType = ["http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric","http://uri.etsi.org/TrstSvc/TrustedList/TSLType/CClist"]
    
    LoTEType = ["http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList",
               "http://uri.etsi.org/19602/LoTEType/EUWalletProvidersList",
               "http://uri.etsi.org/19602/LoTEType/EUWRPACProvidersList",
               "http://uri.etsi.org/19602/LoTEType/EUWRPRCProvidersList",
               "http://uri.etsi.org/19602/LoTEType/EUPubEAAProvidersList",
               "http://uri.etsi.org/19602/LoTEType/EURegistrarsAndRegistersList"
    ]
    statusDetermination=["http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/EUappropriate",
                          "http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/CCdetermination"]
    
    lotestatusDetermination = ["http://uri.etsi.org/19602/PIDProvidersList/StatusDetn/EU",
                              "http://uri.etsi.org/19602/WalletProvidersList/StatusDetn/EU",
                              "http://uri.etsi.org/19602/WRPACProvidersList/StatusDetn/EU",
                              "http://uri.etsi.org/19602/WRPRCrovidersList/StatusDetn/EU",
                              "http://uri.etsi.org/19602/PubEAAProvidersList/StatusDetn/EU",
                              "http://uri.etsi.org/19602/RegistrarsAndRegistersList/StatusDetn/EU"]

    ServiceStatus= { "Qualified":["http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted", "http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/withdrawn"],
                     "Others":["http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/recognisedatnationallevel","http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/deprecatedatnationallevel"],
                     }

    LoTE_ServiceStatus={
                        "Pub-EAA_Providers": ["http://uri.etsi.org/19602/PubEAAProvidersList/SvcStatus/notified", "http://uri.etsi.org/19602/PubEAAProvidersList/SvcStatus/withdrawn"]}

    qualified=["http://uri.etsi.org/TrstSvc/Svctype/EAA/Q"]

    non_qualified=["http://uri.etsi.org/TrstSvc/Svctype/EAA","http://uri.etsi.org/TrstSvc/Svctype/EAA/Pub-EAA",
                    "http://uri.etsi.org/Svc/Svctype/Provider/Wallet","http://uri.etsi.org/Svc/Svctype/Provider/PID",
                    "http://uri.etsi.org/Svc/Svctype/CA/RPaccess"]
    
    providers=[ "http://uri.etsi.org/19602/SvcType/PID/Issuance", "http://uri.etsi.org/19602/SvcType/PID/Revocation",
                "http://uri.etsi.org/19602/SvcType/WalletSolution/Issuance", "http://uri.etsi.org/19602/SvcType/WalletSolution/Revocation",
                "http://uri.etsi.org/19602/SvcType/WRPAC/Issuance", "http://uri.etsi.org/19602/SvcType/WRPAC/Revocation",
                "http://uri.etsi.org/19602/SvcType/WRPRC/Issuance", "http://uri.etsi.org/19602/SvcType/WRPRC/Revocation",
                "http://uri.etsi.org/19602/SvcType/PubEAA/Issuance", "http://uri.etsi.org/19602/SvcType/PubEAA/Revocation",
                "http://uri.etsi.org/19602/SvcType/Register"]

    national=[]

    #test
    service_dict={
                "http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList": "http://uri.etsi.org/19602/SvcType/PID/Issuance",
                "http://uri.etsi.org/19602/LoTEType/EUWalletProvidersList":"http://uri.etsi.org/19602/SvcType/WalletSolution/Issuance",
                "http://uri.etsi.org/19602/LoTEType/EUWRPACProvidersList":"http://uri.etsi.org/19602/SvcType/WRPAC/Issuance",
                "http://uri.etsi.org/19602/LoTEType/EUWRPRCProvidersList":"http://uri.etsi.org/19602/SvcType/WRPRC/Issuance",
                "http://uri.etsi.org/19602/LoTEType/EUPubEAAProvidersList":"http://uri.etsi.org/19602/SvcType/PubEAA/Issuance",
                "http://uri.etsi.org/19602/LoTEType/EURegistrarsAndRegistersList": "http://uri.etsi.org/19602/SvcType/Register"
               
    }

    # qualified=["http://uri.etsi.org/TrstSvc/Svctype/CA/QC","http://uri.etsi.org/TrstSvc/Svctype/Certstatus/OCSP/QC",
    #            "http://uri.etsi.org/TrstSvc/Svctype/Certstatus/CRL/QC","http://uri.etsi.org/TrstSvc/Svctype/TSA/QTST",
    #            "http://uri.etsi.org/TrstSvc/Svctype/EDS/Q","http://uri.etsi.org/TrstSvc/Svctype/EDS/REM/Q",
    #            "http://uri.etsi.org/TrstSvc/Svctype/PSES/Q", "http://uri.etsi.org/TrstSvc/Svctype/QESValidation/Q",
    #            "http://uri.etsi.org/TrstSvc/Svctype/RemoteQSigCDManagement/Q", "http://uri.etsi.org/TrstSvc/Svctype/RemoteQSealCDManagement/Q",
    #            "http://uri.etsi.org/TrstSvc/Svctype/EAA/Q","http://uri.etsi.org/TrstSvc/Svctype/ElectronicArchiving/Q",
    #            "http://uri.etsi.org/TrstSvc/Svctype/Ledgers/Q"]

    # non_qualified=["http://uri.etsi.org/TrstSvc/Svctype/CA/PKC","http://uri.etsi.org/TrstSvc/Svctype/Certstatus/OCSP",
    #                "http://uri.etsi.org/TrstSvc/Svctype/Certstatus/CRL","http://uri.etsi.org/TrstSvc/Svctype/TSA",
    #                "http://uri.etsi.org/TrstSvc/Svctype/TSA/TSS-QC","http://uri.etsi.org/TrstSvc/Svctype/TSA/TSS-AdESQCandQES",
    #                "http://uri.etsi.org/TrstSvc/Svctype/EDS", "http://uri.etsi.org/TrstSvc/Svctype/EDS/REM",
    #                "http://uri.etsi.org/TrstSvc/Svctype/PSES", "http://uri.etsi.org/TrstSvc/Svctype/AdESValidation",
    #                "http://uri.etsi.org/TrstSvc/Svctype/AdESGeneration", "http://uri.etsi.org/TrstSvc/Svctype/RemoteSigCDManagement",
    #                "http://uri.etsi.org/TrstSvc/Svctype/RemoteSealCDManagement", "http://uri.etsi.org/TrstSvc/Svctype/EAA",
    #                "http://uri.etsi.org/TrstSvc/Svctype/ElectronicArchiving", "http://uri.etsi.org/TrstSvc/Svctype/Ledgers",
    #                "http://uri.etsi.org/TrstSvc/Svctype/PKCValidation", "http://uri.etsi.org/TrstSvc/Svctype/PKCPreservation",
    #                "http://uri.etsi.org/TrstSvc/Svctype/EAAValidation ", "http://uri.etsi.org/TrstSvc/Svctype/TSTValidation ",
    #                "http://uri.etsi.org/TrstSvc/Svctype/EDSValidation" , "http://uri.etsi.org/TrstSvc/Svctype/EAA/Pub-EAA",
    #                "http://uri.etsi.org/TrstSvc/Svctype/Ledgers", "http://uri.etsi.org/TrstSvc/Svctype/PKCValidation",
    #                "http://uri.etsi.org/TrstSvc/Svctype/PKCPreservation", "http://uri.etsi.org/TrstSvc/Svctype/EAAValidation" ,
    #                "http://uri.etsi.org/TrstSvc/Svctype/TSTValidation" , "http://uri.etsi.org/TrstSvc/Svctype/EDSValidation ",
    #                "http://uri.etsi.org/TrstSvc/Svctype/EAA/Pub-EAA","http://uri.etsi.org/TrstSvc/Svctype/CA/PKC/CertsforOtherTypesOfTS",
    #                "http://uri.etsi.org/TrstSvc/Svctype/PKCValidation/CertsforOtherTypesOfTS"]

    # national=["http://uri.etsi.org/TrstSvc/Svctype/RA","http://uri.etsi.org/TrstSvc/Svctype/RA/nothavingPKIid","http://uri.etsi.org/TrstSvc/Svctype/ACA",
    #           "http://uri.etsi.org/TrstSvc/Svctype/SignaturePolicyAuthority", "http://uri.etsi.org/TrstSvc/Svctype/Archiv",
    #           "http://uri.etsi.org/TrstSvc/Svctype/Archiv/nothavingPKIid","http://uri.etsi.org/TrstSvc/Svctype/IdV",
    #           "http://uri.etsi.org/TrstSvc/Svctype/IdV/nothavingPKIid","http://uri.etsi.org/TrstSvc/Svctype/KEscrow",
    #           "http://uri.etsi.org/TrstSvc/Svctype/KEscrow/nothavingPKIid","http://uri.etsi.org/TrstSvc/Svctype/PPwd",
    #           "http://uri.etsi.org/TrstSvc/Svctype/PPwd/nothavingPKIid","http://uri.etsi.org/TrstSvc/Svctype/TLIssuer",
    #           "http://uri.etsi.org/TrstSvc/Svctype/NationalRootCA-QC","http://uri.etsi.org/TrstSvc/Svctype/unspecified"]


    log_dir = os.getenv("LOG_PATH", "app/log")
    #log_dir = "/tmp/log"
    log_file_info = "_t.log"

    eu_languages = [
    "bg", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr",
    "ga", "hr", "hu", "it", "lt", "lv", "mt", "nl", "pl", "pt",
    "ro", "sk", "sl", "sv", "no"]
    eu_countries = [
    "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR",
    "DE", "GR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL",
    "PL", "PT", "RO", "SK", "SI", "ES", "SE","UT","NO","EU"]
