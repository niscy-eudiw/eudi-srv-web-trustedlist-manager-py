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
This manages necessary data and it's removal 

"""

import base64
import json
import threading
from datetime import datetime, timedelta, timezone
from venv import logger

from flask import flash, redirect, session

from app.json_gen.jsonGen import json_gen_json
from app.xml_gen.xmlGen import xml_gen_xml
import app.EJBCA_and_DB_func as func
from app_config.config import ConfService as cfgserv
from app.app_config.xml_config import ConfXML as confxml

from .app_config.config import ConfService as cfgservice
import requests


oid4vp_requests = {}
p12_temp={}
certificate_data_List={}


################################################
## To be moved to a file with scheduled jobs

scheduler_call = 300  # scheduled periodic job will be called every scheduler_call seconds (should be 300; 30 for debug)
scheduler_call_lote_tsl=86400


def clear_par():
    """Function to clear parRequests"""
    now = int(datetime.timestamp(datetime.now()))
    #print("Job scheduled: clear_par() at " + str(now))

    
    for id in oid4vp_requests.copy():
        if datetime.now() > oid4vp_requests[id]["expires"]:
            #cfgservice.logger_info.info("Current oid4vp_requests:\n" + str(oid4vp_requests))
            oid4vp_requests.pop(id)
    for id in p12_temp.copy():
        if datetime.now() > p12_temp[id]["expires"]:
            #cfgservice.logger_info.info("Current oid4vp_requests:\n" + str(oid4vp_requests))
            p12_temp.pop(id)
    for id in certificate_data_List.copy():
        if datetime.now() > certificate_data_List[id]["expires"]:
            #cfgservice.logger_info.info("Current oid4vp_requests:\n" + str(oid4vp_requests))
            certificate_data_List.pop(id)

def auto_update_tsl_and_lote():
    #update automatically
    now = datetime.now()

    lote_and_tsl_ids= cfgserv.lote_and_tsls_ids

    for lote_or_tsl_id in lote_and_tsl_ids.keys():

        check = func.check_tsl(lote_or_tsl_id, "auto")

        if check == "tsp":
            print("This TSL doesn't have at least one TSP associated.")
            continue
        elif check == "service":
            print("This TSL doesn't have at least one Service associated to an TSP.")
            continue
        
        tsl_info = func.tsl_info(lote_or_tsl_id, "auto")
        
        user_info = func.get_user_info(tsl_info["operator_id"], "auto")

        if tsl_info["next_update"] < now:

            lang_based_fields = [
                "SchemeName_lang",
                "Uri_lang",
                "SchemeTypeCommunityRules_lang",
                "PolicyOrLegalNotice_lang"
            ]

            for key in lang_based_fields:
                try:
                    tsl_info[key] = json.loads(tsl_info[key]) if tsl_info[key] else []
                except json.JSONDecodeError:
                    extra = {'code': session["session_id"]} 
                    logger.error(f"Error decoding : {key}: {tsl_info[key]}", extra=extra)
                    print(f"Error decoding {key}: {tsl_info[key]}")
                    tsl_info[key] = []

            try:
                tsl_info["DistributionPoints"] = json.loads(tsl_info["DistributionPoints"]) if tsl_info["DistributionPoints"] else []
                if not isinstance(tsl_info["DistributionPoints"], list):
                    raise ValueError("DistributionPoints não é uma lista válida!")
            except (json.JSONDecodeError, ValueError):
                extra = {'code': session["session_id"]} 
                logger.error(f"Error decoding DistributionPoints: {tsl_info['DistributionPoints']}", extra=extra)
                print(f"Error decoding DistributionPoints: {tsl_info['DistributionPoints']}")
                tsl_info["DistributionPoints"] = []


            Issue_date = datetime.now(timezone.utc).replace(microsecond=0)
            NextUpdate = Issue_date + timedelta(days=6*30)

            dictFromDB_trusted_lists={
                "SequenceNumber":   tsl_info["SequenceNumber"] + 1,
                "TSLType":  tsl_info["TSLType"],
                "SchemeName":   tsl_info["SchemeName_lang"],
                "SchemeInformationURI": tsl_info["Uri_lang"],
                #"StatusDeterminationApproach":  confxml.StatusDeterminationApproach.get("EU"),
                #"SchemeTypeCommunityRules": tsl_info["SchemeTypeCommunityRules_lang"],
                "PolicyOrLegalNotice":  tsl_info["PolicyOrLegalNotice_lang"],
                #"pointers_to_other_tsl" :   tsl_info["pointers_to_other_tsl"].encode('utf-8'),
                "HistoricalInformationPeriod":  confxml.HistoricalInformationPeriod,
                "schemeTerritory": tsl_info["schemeTerritory"],
                #AdditionalInformation,ver

                #"DistributionPoints" :  tsl_info["DistributionPoints"],
                "issue_date" :  Issue_date,
                "next_update":   NextUpdate,
                "status":   tsl_info["status"]
            }
            
            tsp_data = func.get_tsp_info_xml(lote_or_tsl_id, "auto")

            if  tsl_info["schemeTerritory"] in confxml.countries:

                cert_location = confxml.countries[tsl_info["schemeTerritory"]][0]
                privkey_location = confxml.countries[tsl_info["schemeTerritory"]][1]
            else :
                cert_location = confxml.countries["EU"][0]
                privkey_location = confxml.countries["EU"][1]

            service_data = []

            for item in tsp_data:
                tsp_id = item["tsp_id"]
                
                service_info = func.get_service_info_xml(tsp_id, "auto")
            
                service_data.append(service_info)

                service_history_ids=[]

                service_data=[service for sublist in service_data for service in sublist]

                for service in service_data:

                    service_id=service["service_id"]

                    service_history_ids.append(service_id)

                    service_history=func.get_service_history_xml(service_history_ids, "auto")

                # for service_list in service_data:
                #     for service in service_list:
                #         service['qualifier'] = cfgserv.qualifiers.get(service["qualifier"])

                if tsl_info["TSLType"] in cfgserv.TSLType:
                    dictFromDB_trusted_lists["Version"]= confxml.TLSVersionIdentifier

                    file, thumbprint, xml_hash_before_sign = xml_gen_xml(user_info, cert_location, privkey_location, dictFromDB_trusted_lists, tsp_data, service_data,service_history, tsl_info["tsl_id"], "auto")
                    file_bytes= base64.b64decode(json_file.encode()) 
                    
                elif tsl_info["TSLType"] in cfgserv.LoTEType:
                    dictFromDB_trusted_lists["Version"]= confxml.LoTEVersionIdentifier

                    json_file, json_thumbprint, json_hash_before_sign = json_gen_json(user_info, cert_location, privkey_location, dictFromDB_trusted_lists, tsp_data, service_data,service_history, tsl_info["tsl_id"], "auto")
                    file_bytes= base64.b64decode(json_file.encode()) 

                try:
                    with open(lote_and_tsl_ids[lote_or_tsl_id], "wb") as f:
                        f.write(file_bytes)

                except Exception as e:       
                    print("Error:", e)
                    continue

                check = func.edit_tsl_dates_and_sequence_number(
                    Issue_date, NextUpdate,
                    tsl_info["SequenceNumber"] + 1 , 
                    lote_or_tsl_id, 
                    "auto"
                )

                if check is None:
                    print("error")
        
        else:
            continue
                

def run_scheduler():
    #print("Run scheduler.")
    threading.Timer(scheduler_call, run_scheduler).start()
    clear_par()

def run_scheduler_lote_and_tsl():
    #print("Run scheduler.")
    threading.Timer(scheduler_call_lote_tsl, run_scheduler).start()
    auto_update_tsl_and_lote()

run_scheduler()
run_scheduler_lote_and_tsl()