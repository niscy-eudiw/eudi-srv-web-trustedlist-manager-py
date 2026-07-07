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
This lote_routes.py file is the blueprint of the Web Trusted List Manager service.
"""

from app import logger, login_required
import base64
import binascii
from collections import defaultdict
from datetime import datetime, timedelta, timezone
import io
import json
import os
import re
from uuid import uuid4
import uuid
import cbor2
from flask import (
    Blueprint,
    Flask,
    flash,
    g,
    redirect,
    render_template,
    request,
    send_file,
    session,
    url_for,
    jsonify
)
import requests

import base64
from cryptography import x509
import urllib.parse
from app.xml_gen_lote.xmlGen import xml_gen_lote_xml, xml_gen_xml_LoTE, xml_lote_validator
from app.json_gen.jsonGen import json_gen_json, json_gen_lote_json
from app_config.config import ConfService as cfgserv
from app_config.xml_config import ConfXML as cfgxml
import segno

from app.data_management import oid4vp_requests
from app.validate_vp_token import validate_vp_token, cbor2elems

import user as get_hash_user_pid
import app.EJBCA_and_DB_func as func
from app_config.Crypto_Info import Crypto_Info as crypto
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from app.app_config.xml_config import ConfXML as confxml
from xml_gen.xmlGen import xml_gen_xml, xml_gen_lotl_xml, xml_validator
from xml_gen.xmlGen_List import xml_gen_xml_lotl
from dateutil.relativedelta import relativedelta
from db import get_db_connection as conn
import ast

lote = Blueprint("LoTE", __name__, url_prefix="/")

lote.template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template/')

@lote.route('/lote/xml_TE', methods=["GET", "POST"])
@login_required
def xml_TE():
    
    temp_user_id = session['temp_user_id']
    user = session[temp_user_id]

    tsl_id = request.args.get("id")

    check = func.check_tsl(tsl_id, session["session_id"])

    if check == "tsp":
        flash("This LoTE doesn't have at least one TE associated.", "danger")
        return redirect('/lote/list')
    elif check == "service":
        flash("This LoTE doesn't have at least one Service associated to an TE.", "warning")
        return redirect('/lote/list')
    
    user_info = func.get_user_info(user["id"], session["session_id"])

    tsl_info = func.tsl_info(tsl_id, session["session_id"])

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
    if  tsl_info["schemeTerritory"] in cfgxml.countries:
        cert_location = cfgxml.countries[tsl_info["schemeTerritory"]][0]
        privkey_location = cfgxml.countries[tsl_info["schemeTerritory"]][1]
    
    dictFromDB_trusted_lists={
        "Version":  confxml.LoTEVersionIdentifier,
        "SequenceNumber":   tsl_info["SequenceNumber"] + 1 ,
        "TSLType": tsl_info["TSLType"],
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
        "next_update":  NextUpdate,
        "status":   tsl_info["status"]
    }
    
    tsp_data = func.get_tsp_info_xml(tsl_id, session["session_id"])

    service_data = []

    for item in tsp_data:
        tsp_id = item["tsp_id"]
        
        service_info = func.get_service_info_xml(tsp_id, session["session_id"])
    
        service_data.append(service_info)

        service_history_ids=[]

        service_data=[service for sublist in service_data for service in sublist]

        for service in service_data:

            service_id=service["service_id"]

            service_history_ids.append(service_id)

        service_history=func.get_service_history_xml(service_history_ids, session["session_id"])

    # for service_list in service_data:
    #     for service in service_list:
    #         service['qualifier'] = cfgserv.qualifiers.get(service["qualifier"])

    file, thumbprint, xml_hash_before_sign = xml_gen_xml_LoTE(user_info,cert_location, privkey_location, dictFromDB_trusted_lists, tsp_data, service_data, service_history, tsl_info["tsl_id"], session["session_id"])
    
    check = func.edit_tsl_dates_and_sequence_number(
        Issue_date, NextUpdate,
        tsl_info["SequenceNumber"] + 1 , 
        tsl_id, 
        session["session_id"]
        )


    if check is None:
        return ("error")
    
    else:
        if(cfgserv.two_operators):
            role = func.check_role_user(session[temp_user_id]['id'], session["session_id"])
            if(role == "tsl_op"):
                menu= cfgserv.service_url + "menu_tsl"
                return render_template("download_tsl.html", menu = menu, lote="True", xml_hash_before_sign = xml_hash_before_sign, thumbprint = thumbprint, dictFromDB_trusted_lists = dictFromDB_trusted_lists, file_data = file, temp_user_id = temp_user_id)
            elif(role == "tsp_op"):
                menu= cfgserv.service_url + "menu_tsp"
                return render_template("download_tsl.html", menu = menu, lote="True",  xml_hash_before_sign = xml_hash_before_sign, thumbprint = thumbprint, dictFromDB_trusted_lists = dictFromDB_trusted_lists, file_data = file, temp_user_id = temp_user_id)
            else:
                return ("error")
        else:
            menu= cfgserv.service_url + "menu"

        return render_template("download_tsl.html", menu = menu, lote="True" , xml_hash_before_sign = xml_hash_before_sign, thumbprint = thumbprint, dictFromDB_trusted_lists = dictFromDB_trusted_lists, file_data = file, temp_user_id = temp_user_id, url= cfgserv.service_url)

@lote.route('/lote/json', methods=["GET", "POST"])
@login_required
def json_file():
    
    temp_user_id = session['temp_user_id']
    user = session[temp_user_id]

    tsl_id = request.args.get("id")

    check = func.check_tsl(tsl_id, session["session_id"])

    if check == "tsp":
        flash("This LoTE doesn't have at least one TE associated.", "danger")
        return redirect('/lote/list')
    elif check == "service":
        flash("This LoTE doesn't have at least one Service associated to an TE.", "warning")
        return redirect('/lote/list')
    
    user_info = func.get_user_info(user["id"], session["session_id"])

    tsl_info = func.tsl_info(tsl_id, session["session_id"])

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

    if  tsl_info["schemeTerritory"] in cfgxml.countries:
        cert_location = cfgxml.countries[tsl_info["schemeTerritory"]][0]
        privkey_location = cfgxml.countries[tsl_info["schemeTerritory"]][1]
    
    dictFromDB_trusted_lists={
        "Version":  confxml.LoTEVersionIdentifier,
        "SequenceNumber":   tsl_info["SequenceNumber"] + 1,
        "TSLType": tsl_info["TSLType"],
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
        "next_update":  NextUpdate,
        "status":   tsl_info["status"]
    }
    
    tsp_data = func.get_tsp_info_xml(tsl_id, session["session_id"])

    service_data = []

    for item in tsp_data:
        tsp_id = item["tsp_id"]
        
        service_info = func.get_service_info_xml(tsp_id, session["session_id"])
    
        service_data.append(service_info)

        service_history_ids=[]

        service_data=[service for sublist in service_data for service in sublist]

        for service in service_data:

            service_id=service["service_id"]

            service_history_ids.append(service_id)

        service_history=func.get_service_history_xml(service_history_ids, session["session_id"])

    # for service_list in service_data:
    #     for service in service_list:
    #         service['qualifier'] = cfgserv.qualifiers.get(service["qualifier"])

    json_file, json_thumbprint, json_hash_before_sign = json_gen_json(user_info, cert_location, privkey_location, dictFromDB_trusted_lists, tsp_data, service_data,service_history, tsl_info["tsl_id"], session["session_id"])
    
    check = func.edit_tsl_dates_and_sequence_number(
        Issue_date, NextUpdate,
        tsl_info["SequenceNumber"] + 1 , 
        tsl_id, 
        session["session_id"]
    )


    if check is None:
        return ("error")
    
    else:
        if(cfgserv.two_operators):
            role = func.check_role_user(session[temp_user_id]['id'], session["session_id"])
            if(role == "tsl_op"):
                menu= cfgserv.service_url + "menu_tsl"
                return render_template("download_tsl.html", menu = menu, json=True, xml_hash_before_sign = json_hash_before_sign, thumbprint = json_thumbprint, dictFromDB_trusted_lists = dictFromDB_trusted_lists, file_data = json_file, temp_user_id = temp_user_id)
            elif(role == "tsp_op"):
                menu= cfgserv.service_url + "menu_tsp"
                return render_template("download_tsl.html", menu = menu,json=True, xml_hash_before_sign = json_hash_before_sign, thumbprint = json_thumbprint, dictFromDB_trusted_lists = dictFromDB_trusted_lists, file_data = json_file, temp_user_id = temp_user_id)
            else:
                return ("error")
        else:
            menu= cfgserv.service_url + "menu"

        return render_template("download_tsl.html", menu = menu,json=True, xml_hash_before_sign = json_hash_before_sign, thumbprint = json_thumbprint, dictFromDB_trusted_lists = dictFromDB_trusted_lists, file_data = json_file, temp_user_id = temp_user_id, url= cfgserv.service_url)

@lote.route('/lote/list')
@login_required
def list_lote():
        
    temp_user_id = session['temp_user_id']
    user = session[temp_user_id]
    
    tsl_dict = func.get_tsl_info(user["id"], session["session_id"])
    
    header_table=[ "Version","Sequence Number","Type","Scheme Name","Scheme Territory","Issue Date","Next Update"]
    if(tsl_dict == "err"):
        data={}
    else:

        data={}

        for tsl in tsl_dict:
            if tsl["TSLType"] in cfgserv.LoTEType:
                data_temp={
                    tsl["tsl_id"]:{
                        "Version":tsl["Version"],
                        "Sequence Number":tsl["SequenceNumber"],
                        "Type":tsl["TSLType"],
                        "Scheme Name":tsl["SchemeName_lang"],
                        "Scheme Territory":tsl["schemeTerritory"],
                        "Issue Date":tsl["issue_date"],
                        "Next Update":tsl["next_update"]
                    }
                }
                data.update(data_temp)
    
    tsp_dict = func.get_tsp_update(user["id"], session["session_id"])
    
    list = []
    if(data != {}):
        if(tsp_dict != "err"):

            for item in tsp_dict:
                if item["type"] == "TE":
                    name = json.loads(item["name"])
                    
                    name_txt = name[0]["text"] if name else "No Name"
                    if(item["tsl_id"] != None):
                        tsl_name = func.get_tsl_name(item["tsl_id"], session["session_id"])
                        aux_name = json.loads(tsl_name["SchemeName_lang"])
                        tsl_name = aux_name[0]["text"] if aux_name else "No Name"
                        
                        new_item = {
                            "id": item["tsp_id"],
                            "name": name_txt,
                            "associated_id": item["tsl_id"],
                            "ass_name": tsl_name
                        }
                    else:
                        new_item = {
                            "id": item["tsp_id"],
                            "name": name_txt,
                            "associated_id": item["tsl_id"],
                            "ass_name": ""
                        }
                    
                    list.append(new_item)
    
    if(cfgserv.two_operators):
        role = func.check_role_user(session[temp_user_id]['id'], session["session_id"])
        if(role == "tsl_op"):
            menu= cfgserv.service_url + "menu_tsl"
            return render_template("CertificateList.html", h1 = "Lists of Trusted Entities", menu = menu, data=data, title="LoTEs", list= list, header_table=header_table, url=cfgserv.service_url +"lote", temp_user_id = temp_user_id)
        elif(role == "tsp_op"):
            menu= cfgserv.service_url + "menu_tsp"
            return render_template("CertificateList.html", h1 = "Lists of Trusted Entities", menu = menu, data=data, title="LoTEs", list= list, header_table=header_table, url=cfgserv.service_url +"lote", temp_user_id = temp_user_id)
        else:
            return ("error")
    else:
        menu= cfgserv.service_url + "menu"
        return render_template("CertificateList.html", h1 = "Lists of Trusted Entities", menu = menu, data=data, title="LoTEs", list= list, header_table=header_table, url=cfgserv.service_url +"lote", temp_user_id = temp_user_id)

    
@lote.route('/lote/create')
@login_required
def create_lote():
    
    temp_user_id = session['temp_user_id']
    user = session[temp_user_id]
    
    attributesForm={}

    form_items={
        "Lang": "lang",
        "Type" : "TSLType",
        "Scheme Name": "string", 
        "Scheme Information URI": "string",
        "Scheme Territory": "country",
        #"Scheme Type Community Rules": "rules",
        "Policy Or Legal Notice": "string",
        #"Pointers to other TSL": "string",
        #"Distribution Points": "string",
        #"Status determination approach": "StatusDetermination",
        "Additional Information": "string"
    }
    descriptions = {
        "Lang": "lang",
        #"TSL Type" : "string",
        "Scheme Name": "string", 
        "Scheme Information URI": "string",
        "Scheme Territory": "country",
        #"Scheme Type Community Rules": "string",
        "Policy Or Legal Notice": "string",
        #"Pointers to other TSL": "string",
        #"Distribution Points": "string",
        #"Status": "string",
        "Additional Information": "string"
    }

    attributesForm.update(form_items)
    #rules = cfgserv.SchemeTypeCommunityRules
    # for items in rules:
    #     if 'Scheme Territory' in items:
    #         rules[items] = rules[items] + user['issuing_country']
            
    return render_template("form_create.html", h3 = "LoTE information form", countries=cfgserv.eu_countries, title="LoTEs", TSLType= cfgserv.LoTEType, lang = cfgserv.eu_languages, desc = descriptions, attributes = attributesForm, temp_user_id = temp_user_id, redirect_url= cfgserv.service_url + "lote/create/db")

@lote.route('/lote/create/db', methods=["GET", "POST"])
@login_required
def create_lote_db():
    
    temp_user_id = session['temp_user_id']
    user = session[temp_user_id]

    lang = request.form.get('Lang') 
    Version = confxml.LoTEVersionIdentifier
    Sequence_number = 0
    Type = request.form.get('Type')
    SchemeName_lang = request.form.get('Scheme Name')
    Uri_lang = request.form.get('Scheme Information URI')
    
    #options = request.form.getlist('rules')
 
    schemeTerritory = request.form.get('Scheme Territory')
    PolicyOrLegalNotice_lang = request.form.get('Policy Or Legal Notice')
    #PointerstootherTSL = request.form.get('Pointers to other TSL')
    #DistributionPoints = request.form.get('Distribution Points')
    Issue_date = datetime.now(timezone.utc)
    NextUpdate = Issue_date + timedelta(days=6*30)
    #Status = request.form.get('Status determination approach')
    AdditionalInformation = request.form.get('Additional Information')

    # if TSLType == "http://uri.etsi.org/TrstSvc/TrustedList/TSLType/CClist":
    #     TSLType="http://uri.etsi.org/TrstSvc/TrustedList/TSLType/"+ schemeTerritory + "list"
    
    # if  "http://uri.etsi.org/TrstSvc/TrustedList/schemerules/" in options:
    #    i= options.index("http://uri.etsi.org/TrstSvc/TrustedList/schemerules/")
    #    options[i]= "http://uri.etsi.org/TrstSvc/TrustedList/schemerules/" + schemeTerritory

    # SchemeTypeCommunityRules_lang = ", ".join(options)

    SchemeName_lang = '[{"lang":"' + lang + '", "text":"'+ SchemeName_lang + '"}]'
    Uri_lang = '[{"lang":"' + lang + '", "URI":"'+ Uri_lang + '"}]'
    #SchemeTypeCommunityRules_lang = '[{"lang":"' + lang + '", "URI":"'+ SchemeTypeCommunityRules_lang + '"}]'
    PolicyOrLegalNotice_lang = '[{"lang":"' + lang + '", "text":"'+ PolicyOrLegalNotice_lang + '"}]'
    #DistributionPoints = '["'+ DistributionPoints + '"]'

    lotl = 0

    check = func.check_country(session["session_id"])
    
    if user['issuing_country'] not in check:

        return ("err")

    check = func.tsl_db_info(user['id'], Version, Sequence_number,Type, SchemeName_lang, Uri_lang,
                             PolicyOrLegalNotice_lang, Issue_date, NextUpdate, 
                             AdditionalInformation, schemeTerritory, lotl, check, session["session_id"])
    
    if check is None:
        return ("err")
    else:   
        return redirect('/lote/list')

@lote.route('/lote/edit', methods=["GET", "POST"])
@login_required
def lote_edit():
    
    if not request.args.get("id"):
        return ""
    
    tsl_id = request.args.get("id")

    temp_user_id = session['temp_user_id']
    user = session[temp_user_id]

    db_data = func.get_data_tsl_edit(tsl_id, session["session_id"])

    for key in db_data:
        if db_data[key]: 
            try:
                db_data[key] = json.loads(db_data[key])
            except json.JSONDecodeError as e:
                extra = {'code': session["session_id"]} 
                logger.error(f"error: {e}", extra=extra)

    return render_template("dynamic-form_edit_TLS.html", h3 = "LoTEs Information", id = tsl_id, lang = cfgserv.lang, role = cfgserv.roles, data_edit = db_data, Langs=cfgserv.eu_languages,Countries=cfgserv.eu_countries, temp_user_id=temp_user_id, redirect_url= cfgserv.service_url + "lote/edit_db")

@lote.route('/lote/edit_db', methods=["GET", "POST"])
@login_required
def lote_edit_db():

    temp_user_id = session['temp_user_id']
    user = session[temp_user_id]

    tsl_id = request.form.get("id")

    form = dict(request.form)
    form.pop("proceed")
    grouped = defaultdict(list)

    for key, value in form.items():
        match = re.match(r"(lang|text|URI)_(.*?).(\d+)", key)
        match2=re.match(r"(postal_address)_(.*?).(\d+)",key)
        if match:
            attr, prefix, index = match.groups()
            index = int(index)
            while len(grouped[prefix]) <= index:
                grouped[prefix].append({})
            grouped[prefix][index][attr] = value
        elif match2:
            attr, prefix, index = match2.groups()
            index = int(index)
            while len(grouped[attr]) <= index:
                grouped[attr].append({})
            grouped[attr][index][prefix] = value

        elif "DistributionPoints" in key:
                key_dict=key.split(".")
                grouped[key_dict[0]].append(value)
                
        else:
            grouped[key] = value

    check = func.edit_tsl_db_info(
        grouped, 
        tsl_id, 
        session["session_id"]
    )

    if check is None:
        return ("erro")
    else:
        return redirect('/lote/list')
#depois
@lote.route('/lote/update_tes', methods=["GET", "POST"])
@login_required
def update_TEs():

    tsl_id = request.args.get("id")
    tsps = ast.literal_eval(request.args.get("checks"))
    user_id =request.args.get("user_id")
    log_id = request.args.get("log_id")

    for elem in tsps:
        tsp_id = int(elem)

        check = func.update_tsp(tsp_id, tsl_id, session["session_id"])
        
        if check is None:
            return ("erro")

    return redirect('/lote/list')

@lote.route('/lote/data_lang')
@login_required
def lote_lang():
    temp_user_id = session['temp_user_id']
    
    attributesForm={}
    tsp_id = request.args.get("id")
    form_items={
        "Lang": "lang",
        "Scheme Name": "string", 
        "Uri": "string",
        "Scheme Type Community Rules": "string",
        "Policy Or Legal Notice": "string",
        "Distribution Points": "string"
    }
    descriptions = {
        "Lang": "lang",
        "Scheme Name": "string", 
        "Uri": "string",
        "Scheme Type Community Rules": "string",
        "Policy Or Legal Notice": "string",
        "Distribution Points": "string"
    }

    attributesForm.update(form_items)
    
    return render_template("form.html", id = tsp_id, countries=cfgserv.eu_countries, title="LoTEs", lang = cfgserv.eu_languages, desc = descriptions, attributes = attributesForm, temp_user_id = temp_user_id, redirect_url= cfgserv.service_url + "lote/lote_db_data_lang")


@lote.route('/lote/lote_db_data_lang', methods=["GET", "POST"])
@login_required
def lote_db_lang():
    temp_user_id = session['temp_user_id']
    user = session[temp_user_id]

    tsl_id = request.form.get("id")

    schemeName = request.form.get('Scheme Name')
    uri = request.form.get('Uri')
    schemeTypeCommunityRules= request.form.get('Scheme Type Community Rules')
    policyLegalNotice= request.form.get('Policy Or Legal Notice')
    distributionPoints= request.form.get('Distribution Points')
    lang = request.form.get('Lang')

    db_data = func.get_data_tsl(tsl_id, session["session_id"])

    current_data_schemeName = None
    current_data_uri= None
    current_data_schemeTypeCommunityRules = None
    current_data_policyLegalNotice = None
    current_data_distributionPoints = None

    if schemeName:
        schemeName_data = {"lang": lang, "text": schemeName}
        current_data_schemeName = json.loads(db_data.get('SchemeName_lang', '[]'))
        current_data_schemeName.append(schemeName_data)
        current_data_schemeName = json.dumps(current_data_schemeName)

    if uri:
        uri_data = {"lang": lang, "URI": uri}
        current_data_uri = json.loads(db_data.get('Uri_lang', '[]'))
        current_data_uri.append(uri_data)
        current_data_uri = json.dumps(current_data_uri)
        
    if schemeTypeCommunityRules:
        schemeTypeCommunityRules_data = {"lang": lang, "URI": schemeTypeCommunityRules}
        current_data_schemeTypeCommunityRules = json.loads(db_data.get('SchemeTypeCommunityRules_lang', '[]'))
        current_data_schemeTypeCommunityRules.append(schemeTypeCommunityRules_data)
        current_data_schemeTypeCommunityRules = json.dumps(current_data_schemeTypeCommunityRules)

    if policyLegalNotice:
        policyLegalNotice_data = {"lang": lang, "text": policyLegalNotice}
        current_data_policyLegalNotice = json.loads(db_data.get('PolicyOrLegalNotice_lang', '[]'))
        current_data_policyLegalNotice.append(policyLegalNotice_data)
        current_data_policyLegalNotice = json.dumps(current_data_policyLegalNotice)

    if distributionPoints:
        distributionPoints_data = distributionPoints
        current_data_distributionPoints = json.loads(db_data.get('DistributionPoints', '[]'))
        current_data_distributionPoints.append(distributionPoints_data)
        current_data_distributionPoints = json.dumps(current_data_distributionPoints)

    check = func.tsl_db_lang(user['id'], 
                             tsl_id, 
                             current_data_schemeName, 
                             current_data_uri, 
                             current_data_schemeTypeCommunityRules,
                             current_data_policyLegalNotice, 
                             current_data_distributionPoints, 
                             session["session_id"])

    if check is None:
        return "err"
    else:   
        return redirect('/lote/list')

# TSP
@lote.route('/te/list')
@login_required
def list_te():

    temp_user_id = session['temp_user_id']
    user = session[temp_user_id]

    tsp_dict = func.get_tsp_info(user["id"], session["session_id"])
    header_table=[ "TE Name", "Trade Name", "Postal Address", "EletronicAddress","InformationURI"]

    if(tsp_dict == "err"):
        data = {}
    else:
        
        data = {}
        
        for tsp in tsp_dict:
            if tsp["type"] == "TE":
                data_temp={
                
                    tsp["tsp_id"]:{
                        "TSP/TE Name": tsp["name"],
                        "Trade Name": tsp["trade_name"],
                        "Postal Address": tsp["postal_address"],
                        "EletronicAddress": tsp["EletronicAddress"],
                        "InformationURI": tsp["TSPInformationURI"]
                    }
                }
                data.update(data_temp)

    service_dict = func.get_service_update(user["id"], session["session_id"])
    
    list = []

    if(service_dict != "err"):
        for item in service_dict:
            if item["service_type"] in cfgserv.providers:
                name = json.loads(item["ServiceName"])
                name_txt = name[0]["text"] if name else "No Name"

                if(item["tsp_id"] != None):
                    tsp_name = func.get_tsp_name(item["tsp_id"], session["session_id"])
                    aux_name = json.loads(tsp_name["name"])
                    tsp_name = aux_name[0]["text"] if aux_name else "No Name"

                    new_item = {
                        "id": item["service_id"],
                        "name": name_txt,
                        "associated_id": item["tsp_id"],
                        "ass_name": tsp_name
                    }
                else:
                    new_item = {
                        "id": item["service_id"],
                        "name": name_txt,
                        "associated_id": item["tsp_id"],
                        "ass_name": ""
                    }
                
                list.append(new_item)

    if(cfgserv.two_operators):
        role = func.check_role_user(session[temp_user_id]['id'], session["session_id"])
        if(role == "tsl_op"):
            menu= cfgserv.service_url + "menu_tsl"
            return render_template("CertificateList.html", h1 = "Trusted Entities", menu = menu, data=data, title="Trusted Entities", list= list, header_table=header_table, url=cfgserv.service_url +"te", temp_user_id = temp_user_id)
        elif(role == "tsp_op"):
            menu= cfgserv.service_url + "menu_tsp"
            return render_template("CertificateList.html", h1 = "Trusted Entities", menu = menu, data=data, title="Trusted Entities", list= list, header_table=header_table, url=cfgserv.service_url +"te", temp_user_id = temp_user_id)
        else:
            return ("error")
    else:
        menu= cfgserv.service_url + "menu"
        return render_template("CertificateList.html", h1 = "Trusted Entities", menu = menu, data=data, title="Trusted Entities", list= list, header_table=header_table, url=cfgserv.service_url +"te", temp_user_id = temp_user_id)

@lote.route('/te/create')
@login_required
def create_te():
    
    temp_user_id = session['temp_user_id']
    
    attributesForm={}

    form_items={
        "Lang": "lang",
        "Name": "string",
        "Trade Name": "string",
        "Eletronic Address": "string",
        "Information URI": "string",
        "Street Address" : "string",
        "Locality": "string",
        "State Or Province": "string",
        "Postal Code": "string",
        "Country Name": "country",
    }
    
    descriptions = {
        "Lang": "lang",
        "Name": "string",
        "Trade Name": "string",
        "Eletronic Address": "string",
        "Information URI": "string",
        "Street Address": "string",
        "Locality": "string",
        "State Or Province": "string",
        "Postal Code": "string",
        "Country Name": "country",
    }

    attributesForm.update(form_items)
    
    return render_template("form_create.html", h3 = "Trusted Entity information form", countries=cfgserv.eu_countries, title="Trusted Entity", lang = cfgserv.eu_languages, desc = descriptions, attributes = attributesForm, temp_user_id = temp_user_id, redirect_url= cfgserv.service_url + "te/create/db")


@lote.route('/te/create/db', methods=["GET", "POST"])
@login_required
def create_te_db():
    
    temp_user_id = session['temp_user_id']
    user = session[temp_user_id]

    name = request.form.get('Name')
    trade_name = request.form.get('Trade Name')
    StreetAddress = request.form.get('Street Address')
    Locality= request.form.get('Locality')
    StateOrProvince= request.form.get('State Or Province')
    PostalCode= request.form.get('Postal Code')
    EletronicAddress= request.form.get('Eletronic Address')
    TSPInformationURI= request.form.get('Information URI')
    country= request.form.get('Country Name')
    lang = request.form.get('Lang')

    name = '[{"lang":"' + lang + '", "text":"'+ name + '"}]'
    trade_name = '[{"lang":"' + lang + '", "text":"'+ trade_name + '"}]'
    EletronicAddress = '[{"lang":"' + lang + '", "URI":"'+ EletronicAddress + '"}]'
    TSPInformationURI = '[{"lang":"' + lang + '", "URI":"'+ TSPInformationURI + '"}]'
    PostalAddress = '[{"lang":"' + lang + '", "StreetAddress":"'+ StreetAddress + '", "Locality":"'+ Locality + '", "StateOrProvince":"'+ StateOrProvince + '", "PostalCode":"'+ PostalCode + '", "CountryName":"'+ country + '"}]'
    
    check = func.tsp_db_info(user['id'], name, trade_name, PostalAddress, EletronicAddress, TSPInformationURI, "TE", session["session_id"])

    if check is None:
        return "err"
    else:
        return redirect('/te/list')
        

@lote.route('/te/data_lang')
@login_required
def te_lang():
    temp_user_id = session['temp_user_id']
    
    attributesForm={}
    tsp_id = request.args.get("id")
    form_items={
        "Lang": "lang",
        "Name": "string",
        "Trade Name": "string",
        "Eletronic Address": "string",
        "Information URI": "string",
        "Street Address" : "string",
        "Locality": "string",
        "State Or Province": "string",
        "Postal Code": "string",
        "Country Name": "country"
    }
    descriptions = {
        "Lang": "lang",
        "Name": "string",
        "Trade Name": "string",
        "Eletronic Address": "string",
        "Information URI": "string",
        "Street Address" : "string",
        "Locality": "string",
        "State Or Province": "string",
        "Postal Code": "string",
        "Country Name": "country"
    }

    attributesForm.update(form_items)
    
    return render_template("form.html", id = tsp_id, countries=cfgserv.eu_countries, title="Trusted Entity", lang = cfgserv.eu_languages, desc = descriptions, attributes = attributesForm, temp_user_id = temp_user_id, redirect_url= cfgserv.service_url + "te/te_db_data_lang")


@lote.route('/te/te_db_data_lang', methods=["GET", "POST"])
@login_required
def te_db_lang():
    temp_user_id = session['temp_user_id']
    user = session[temp_user_id]

    tsp_id = request.form.get("id")

    name = request.form.get('Name')
    trade_name = request.form.get('Trade Name')
    StreetAddress = request.form.get('Street Address')
    Locality= request.form.get('Locality')
    StateOrProvince= request.form.get('State Or Province')
    PostalCode= request.form.get('Postal Code')
    CountryName= request.form.get('Country Name')
    EletronicAddress= request.form.get('Eletronic Address')
    TSPInformationURI= request.form.get('Information URI')
    lang = request.form.get('Lang')

    db_data = func.get_data_tsp(tsp_id, session["session_id"])

    current_data_name = None
    current_data_trade_name = None
    current_data_postal_address = None
    current_data_EletronicAddress = None
    current_data_TSPInformationURI = None

    if name:
        name_data = {"lang": lang, "text": name}
        current_data_name = json.loads(db_data.get('name', '[]'))
        current_data_name.append(name_data)
        current_data_name = json.dumps(current_data_name)

    if trade_name:
        trade_name_data = {"lang": lang, "text": trade_name}
        current_data_trade_name = json.loads(db_data.get('trade_name', '[]'))
        current_data_trade_name.append(trade_name_data)
        current_data_trade_name = json.dumps(current_data_trade_name)

    if all([StreetAddress, Locality, StateOrProvince, PostalCode, CountryName]):
        postal_address_data = {
            "lang": lang,
            "StreetAddress": StreetAddress,
            "Locality": Locality,
            "StateOrProvince": StateOrProvince,
            "PostalCode": PostalCode,
            "CountryName": CountryName
        }
        current_data_postal_address = json.loads(db_data.get('postal_address', '[]'))
        current_data_postal_address.append(postal_address_data)
        current_data_postal_address = json.dumps(current_data_postal_address)

    if EletronicAddress:
        electronic_address_data = {"lang": lang, "URI": EletronicAddress}
        current_data_EletronicAddress = json.loads(db_data.get('EletronicAddress', '[]'))
        current_data_EletronicAddress.append(electronic_address_data)
        current_data_EletronicAddress = json.dumps(current_data_EletronicAddress)

    if TSPInformationURI:
        tsp_info_data = {"lang": lang, "URI": TSPInformationURI}
        current_data_TSPInformationURI = json.loads(db_data.get('TSPInformationURI', '[]'))
        current_data_TSPInformationURI.append(tsp_info_data)
        current_data_TSPInformationURI = json.dumps(current_data_TSPInformationURI)

    check = func.tsp_db_lang(user['id'], 
                             tsp_id, 
                             current_data_name, 
                             current_data_trade_name, 
                             current_data_postal_address,
                             current_data_EletronicAddress, 
                             current_data_TSPInformationURI, 
                             session["session_id"])

    if check is None:
        return "err"
    else:   
        return redirect('/te/list')


@lote.route('/te/edit')
@login_required
def te_edit():
        
    temp_user_id = session['temp_user_id']
    user = session[temp_user_id]
    tsp_id = request.args.get("id")

    db_data = func.get_data_tsp_edit(tsp_id, session["session_id"])

    for key in db_data: 
        db_data[key] = json.loads(db_data[key])

    
    return render_template("dynamic-form_edit_TLS.html", h3 = "Trusted Entity Information", title = "Trusted Entity", id = tsp_id, lang = cfgserv.lang, role = cfgserv.roles, data_edit = db_data, Langs=cfgserv.eu_languages,Countries=cfgserv.eu_countries, temp_user_id=temp_user_id, redirect_url= cfgserv.service_url + "/te/te_edit_db")

@lote.route('/te/te_edit_db', methods=["GET", "POST"])
@login_required
def te_edit_db():

    temp_user_id = session['temp_user_id']
    user = session[temp_user_id]
    
    tsp_id = request.form.get("id")

    form = dict(request.form)
    form.pop("proceed")
    grouped = defaultdict(list)

    for key, value in form.items():
        match = re.match(r"(lang|text|URI)_(.*?).(\d+)", key)
        match2=re.match(r"(postal_address)_(.*?).(\d+)",key)
        if match:
            attr, prefix, index = match.groups()
            index = int(index)
            while len(grouped[prefix]) <= index:
                grouped[prefix].append({})
            grouped[prefix][index][attr] = value
        elif match2:
            attr, prefix, index = match2.groups()
            index = int(index)
            while len(grouped[attr]) <= index:
                grouped[attr].append({})
            grouped[attr][index][prefix] = value

        elif "DistributionPoints" in key:
                key_dict=key.split(".")
                grouped[key_dict[0]].append(value)
                
        else:
            grouped[key] = value
    
    check = func.edit_tsp_db_info(
        grouped, 
        tsp_id, 
        session["session_id"]
    )

    if check is None:
        return ("erro")
    else:
        return redirect('/te/list')
    
#depois        
@lote.route('/te/update_services', methods=["GET", "POST"])
def update_services():

    tsp_id = request.args.get("id")
    services = ast.literal_eval(request.args.get("checks"))
    user_id =request.args.get("user_id")
    log_id = request.args.get("log_id")

    for elem in services:
        service_id = int(elem)

        check = func.update_service(service_id, tsp_id, session["session_id"])
        
        if check is None:
            return ("erro")

    return redirect('/te/list')
    
# Service
@lote.route('/te_service/list')
@login_required
def list_te_service():
    temp_user_id = session['temp_user_id']
    user = session[temp_user_id]
    
    service_dict = func.get_service_info(user["id"], session["session_id"])
    header_table=[ "Service Type","Service Name","Status","Status Starting Date", "Qualifier", "SchemeService Definition URI"]

    if(service_dict == "err"):
        data = {}
    else:
        data = {}
    
        for service in service_dict:
            if service["service_type"] in cfgserv.providers:
                data_temp={
                    service["service_id"]:{
                        "Service Type": service["service_type"],
                        "Service Name": service["ServiceName"],
                        "Status": service["status"],
                        "Status start date": service["status_start_date"],
                        "Qualifier": service["qualifier"],
                        "SchemeService Definition URI": service["SchemeServiceDefinitionURI"]
                    }
                }
                data.update(data_temp)

    service_history_ids=[]

    for service in data:
        service_history_ids.append(service)
    list = []

    service_history=func.get_service_history_xml(service_history_ids, session["session_id"])
    if service_history:
        for history in service_history:
            name = json.loads(history["ServiceName"])       
            name_txt = name[0]["text"]
            new_item = {
                "id": history["history_id"],
                "name": name_txt,
                "status": history["status"],
                "status_start_date":history["status_start_date"],
                "service_id":history["service_id"]
            }
                    
            list.append(new_item)
    
    if(cfgserv.two_operators):
        role = func.check_role_user(session[temp_user_id]['id'], session["session_id"])
        if(role == "tsl_op"):
            menu= cfgserv.service_url + "menu_tsl"
            return render_template("CertificateList.html", h1 = "Services", menu = menu, data=data, title="Services", list= list, header_table=header_table, url=cfgserv.service_url +"te_service", temp_user_id = temp_user_id)
        elif(role == "tsp_op"):
            menu= cfgserv.service_url + "menu_tsp"
            return render_template("CertificateList.html", h1 = "Services", menu = menu, data=data, title="Services", list= list, header_table=header_table, url=cfgserv.service_url +"te_service", temp_user_id = temp_user_id)
        else:
            return ("error")
    else:
        menu= cfgserv.service_url + "menu"
        return render_template("CertificateList.html", h1 = "Services",  menu = menu, data=data, title="Services", list= list, header_table=header_table, url=cfgserv.service_url +"te_service", temp_user_id = temp_user_id)

@lote.route('/te_service/create')
@login_required
def create_service():
    
    temp_user_id = session['temp_user_id']
    
    attributesForm={}

    form_items={
        "Lang": "lang",
        "Service Type": "select_type",
        "Service Name": "string",
        #"Qualifier": "select",
        "Digital Identity" : "textarea",
        "Service Status": "status",
        "Status Start Date": "full-date",
        "Scheme Service Definition URI": "string"
    }
    descriptions = {
        "Lang": "string",
        "Service Type": "Type of service provided",
        "Service Name": "Provide the service name",
        #"Qualifier": "Select applicable qualifiers",
        "Digital Identity": "Specify the digital Certificate (It's not necessary to include BEGIN or END certificate.)",
        "Status": "Service status",
        "Status Start Date": "Start date of the current status",
        "Uri": "Service URI"
    }

    attributesForm.update(form_items)
    
    return render_template("form_service.html", title="Service",status = cfgserv.LoTE_ServiceStatus, lang = cfgserv.eu_languages, desc = descriptions, attributes = attributesForm, temp_user_id = temp_user_id, 
                           data = cfgserv.qualifiers, redirect_url= cfgserv.service_url + "te_service/create/db",qualified = [],
                           non_qualified = [], national = [], LoTE=cfgserv.providers, url_certificate=cfgserv.service_url + "checkcertificate")

@lote.route('/te_service/create/db', methods=["GET", "POST"])
@login_required
def service_te_db():
    
    temp_user_id = session['temp_user_id']
    user = session[temp_user_id]
    
    service_type = request.form.get('category')
    service_name = request.form.get('Service Name')
    #qualifier = request.form.get('Qualifier')
    digital_identity = request.form.get('Digital Identity')
    
    status = request.form.get('Service Status')
    status_start_date = request.form.get('Status Start Date')
    uri = request.form.get('Scheme Service Definition URI')
    lang = request.form.get('Lang')

    ServiceName = '[{"lang":"' + lang + '", "text":"'+ service_name + '"}]'
    SchemeServiceDefinitionURI = '[{"lang":"' + lang + '", "URI":"'+ uri + '"}]'

    check = func.service_db_info(user['id'], ServiceName, SchemeServiceDefinitionURI, digital_identity, service_type, status, status_start_date, session["session_id"])

    if check is None:
        return (check)
    else:
        
        return redirect('/te_service/list')
       
@lote.route('/te_service/data_lang')
@login_required
def service_lang():
    
    temp_user_id = session['temp_user_id']
    
    service_id = request.args.get("id")

    attributesForm={}

    form_items={
        "Lang": "lang",
        "Service Name": "string",
        "Uri": "string"
    }
    descriptions = {
        "Lang": "string",
        "Service Name": "Provide the service name",
        "Uri": "Service URI"
    }

    attributesForm.update(form_items)
    
    return render_template("form.html", id = service_id, countries=cfgserv.eu_countries, title="Service", lang = cfgserv.eu_languages, desc = descriptions, attributes = attributesForm, temp_user_id = temp_user_id, 
                           data = cfgserv.qualifiers, redirect_url= cfgserv.service_url + "te_service/service_lang_db")


@lote.route('/te_service/service_lang_db', methods=["GET", "POST"])
@login_required
def service_db():
    
    temp_user_id = session['temp_user_id']
    user = session[temp_user_id]

    service_id = request.form.get("id")

    service_name = request.form.get('Service Name')
    uri = request.form.get('Uri')
    lang = request.form.get('Lang')

    db_data = func.get_data_service(service_id, session["session_id"])
    
    current_data_ServiceName = None
    current_data_SchemeServiceDefinitionURI = None

    if service_name:
        service_name_data = {"lang": lang, "text": service_name}
        current_data_ServiceName = json.loads(db_data.get('ServiceName', '[]'))
        current_data_ServiceName.append(service_name_data)
        current_data_ServiceName = json.dumps(current_data_ServiceName)

    if uri:
        scheme_service_data = {"lang": lang, "URI": uri}
        current_data_SchemeServiceDefinitionURI = json.loads(db_data.get('SchemeServiceDefinitionURI', '[]'))
        current_data_SchemeServiceDefinitionURI.append(scheme_service_data)
        current_data_SchemeServiceDefinitionURI = json.dumps(current_data_SchemeServiceDefinitionURI)

    check = func.service_db_lang(
        service_id,
        current_data_ServiceName,
        current_data_SchemeServiceDefinitionURI,
        session["session_id"]
    )

    if check is None:
        return ("err")
    else:
        return redirect('/te_service/list')
       

@lote.route('/te_service/edit')
@login_required
def service_edit():
        
    temp_user_id = session['temp_user_id']
    user = session[temp_user_id]

    service_id = request.args.get("id")

    db_data = func.get_data_service_edit(service_id, session["session_id"])

    for key in db_data:
        if key != "status" : 
            db_data[key] = json.loads(db_data[key])
    
    return render_template("dynamic-form_edit_TLS.html", h3 = "Service Information", title = "Service", id = service_id, lang = cfgserv.lang, role = cfgserv.roles, data_edit = db_data, Langs=cfgserv.eu_languages,Countries=cfgserv.eu_countries, temp_user_id=temp_user_id, status = cfgserv.LoTE_ServiceStatus, redirect_url= cfgserv.service_url + "/te_service/service_edit_db")

@lote.route('/te_service/service_edit_db', methods=["GET", "POST"])
@login_required
def service_edit_db():

    temp_user_id = session['temp_user_id']
    user = session[temp_user_id]

    service_id = request.form.get("id")

    form = dict(request.form)
    form.pop("proceed")
    grouped = defaultdict(list)

    for key, value in form.items():
        match = re.match(r"(lang|text|URI)_(.*?).(\d+)", key)
        match2=re.match(r"(postal_address)_(.*?).(\d+)",key)
        if match:
            attr, prefix, index = match.groups()
            index = int(index)
            while len(grouped[prefix]) <= index:
                grouped[prefix].append({})
            grouped[prefix][index][attr] = value
        elif match2:
            attr, prefix, index = match2.groups()
            index = int(index)
            while len(grouped[attr]) <= index:
                grouped[attr].append({})
            grouped[attr][index][prefix] = value

        elif "DistributionPoints" in key:
                key_dict=key.split(".")
                grouped[key_dict[0]].append(value)
                
        else:
            grouped[key] = value
            
    db_data_old = func.get_status_service(service_id, session["session_id"])

    grouped["status_start_date"]=db_data_old.get("status_start_date")

    if(db_data_old != "err"):

        if grouped["status"] != db_data_old.get('status'):

            grouped["status_start_date"]=datetime.now(timezone.utc)

            history= func.insert_service_history(db_data_old.get("service_type"), db_data_old.get("digital_identity"),db_data_old.get("status"),db_data_old.get("status_start_date"), db_data_old.get("ServiceName"),service_id, session["session_id"])

            if history is None:
                return ("erro")
            
    check = func.edit_service_db_info(
        grouped, 
        service_id, 
        session["session_id"]
    )

    if check is None:
        return ("erro")
    else:
        return redirect('/te_service/list')


# logout
@lote.route('/logout')
def logout():
    session.clear()
    
    return redirect(url_for('RPR.initial_page'))
