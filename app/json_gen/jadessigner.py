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
from http.client import HTTPException
import json
import logging
from logging.handlers import TimedRotatingFileHandler
import os
import sys

import pymysql
from requests import Session
import requests
import urllib

from app.app_config.config import ConfService

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import ec, utils


sys.path.append(os.path.dirname(__file__))


from flask import Flask, render_template
from flask_session import Session
from flask_cors import CORS
from pycose.keys import EC2Key

import os
from flask import Flask
import os
from app_config.config import ConfService as cfgserv


def jadesigner(base64_payload, base64_cert, privkey_location):

    payload=json.dumps({

            "documents":[{

                "document": base64_payload,
                "signature_format": "J",
                "conformance_level":"Ades-B-B",
                "signed_envelope_property": "ENVELOPING",
                "container": "No"

            } ],
        "endEntityCertificate": base64_cert,
        "certificateChain": [
        ],
        "hashAlgorithmOID": "2.16.840.1.101.3.4.2.1"

    })

    headers={
        'Content-Type': 'application/json'
    }    
    
    headers={
        'Content-Type': 'application/json'
    }

    calculate_hash=requests.post(url=cfgserv.sca_signer_url+"/signatures/calculate_hash",headers=headers, data=payload)


    hashes1 = calculate_hash.json()["hashes"]

    base64_string = urllib.parse.unquote(hashes1[0])

    data_to_be_signed = base64.b64decode(base64_string)

    signature_date = calculate_hash.json()["signature_date"]

    with open(privkey_location, "rb") as f:
        private_key = serialization.load_pem_private_key(
        f.read(),
        password=None,
        backend=default_backend()
    )

    signature = private_key.sign(
        data_to_be_signed,
        ec.ECDSA(utils.Prehashed(hashes.SHA256()))
    )

    base64_signature= base64.b64encode(signature).decode()

    payload = json.dumps({
        "documents": [
            {
                "document": base64_payload,
                "signature_format": "J",
                "conformance_level":"Ades-B-B",
                "signed_envelope_property": "ENVELOPING",
                "container": "No"
            }
        ],
        "hashAlgorithmOID": "2.16.840.1.101.3.4.2.1",
        "returnValidationInfo": False,
        "endEntityCertificate": base64_cert,
        "certificateChain": [
        ],
        "signatures":[base64_signature],
        "date": signature_date
    }).encode()

    obtain_signed_document=requests.post(url=cfgserv.sca_signer_url+"/signatures/obtain_signed_doc",headers=headers, data=payload)
    
    document_with_signature=obtain_signed_document.json()["documentWithSignature"][0]

    return document_with_signature, base64_string

    # data=json.loads(base64.b64decode(document_with_signature).decode("utf-8"))

    # jwt_payload=data["payload"]
    # jwt_header=data["signatures"][0]["protected"]
    # jwt_signature=data["signatures"][0]["signature"]

    # jwt = jwt_header + "." + jwt_payload + "." + jwt_signature

    # output_file ="teste.json"

    # with open(output_file, "w", encoding="utf-8") as f:
    #     json.dump(
    #         json.loads(base64.b64decode(document_with_signature).decode()),
    #         f,
    #     )
