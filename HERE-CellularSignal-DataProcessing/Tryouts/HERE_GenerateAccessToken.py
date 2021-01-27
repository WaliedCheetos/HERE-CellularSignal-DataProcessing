# Python3.7
import requests
import os
import random
import json
import time
import hashlib
import base64
import random
import hmac
import urllib
from os.path import expanduser
from requests_oauthlib import OAuth1Session
import codecs
import sys
# print(sys.version)
url = "https://account.api.here.com/oauth2/token"
def _prepare_signature():
    nonce = base64.b64encode(b"%0x" % random.getrandbits(256)).decode('utf-8')[:11]
    timestamp = int(time.time())
    home = expanduser("~")
    creds_path = os.path.join(os.path.join(home, ".here"), "credentials.properties")
    credentials = os.getenv("OLP_CREDENTIALS") if os.getenv("OLP_CREDENTIALS") is not None else creds_path
    # print(creds_path)
    with open(credentials) as f:
        l = [line.split("=") for line in f.readlines()]
        properties = {key.strip(): value.strip() for key, value in l}
    # key = properties["here.access.key.id"].strip()
    key = "***"
    # print(key)
    secret = "***"
    # secret = properties["here.access.key.secret"].strip()
    # print(secret)
    normalized_url = urllib.parse.quote_plus(url)
    # print(normalized_url)
    signing_method = "HMAC-SHA256"
    sig_string = '{}&{}&{}&{}&{}'.format(
        "oauth_consumer_key={}".format(key),
        "oauth_nonce={}".format(nonce),
        "oauth_signature_method={}".format(signing_method),
        "oauth_timestamp={}".format(timestamp),
        "oauth_version=1.0").strip()
    # print(sig_string)
    normalised_string = "POST&" + normalized_url.strip() + "&" + urllib.parse.quote_plus(sig_string.strip())
    signingKey = bytes(urllib.parse.quote_plus(secret).encode('utf-8') + "&".encode('utf-8')).decode('utf-8')
    # print(signingKey)
    # print(normalised_string)
    digest = hmac.new(signingKey.encode('utf-8'), normalised_string.encode(), hashlib.sha256).digest()
    # print(codecs.encode(digest, 'hex').decode('utf-8'))
    signature = codecs.encode(digest, 'base64').decode('utf-8')
    # print(signature)
    signature = signature[:-1]
    return key, signing_method, urllib.parse.quote_plus(signature), timestamp, nonce
def get_token():
    key, method, signature, time, nonce = _prepare_signature()
    payload = "{\n  \"grantType\": \"client_credentials\"\n}"
    Header = "OAuth oauth_consumer_key=\"{}\"," \
    "oauth_signature_method=\"{}\"," \
    "oauth_signature=\"{}\"," \
    "oauth_timestamp=\"{}\"," \
    "oauth_nonce=\"{}\"," \
    "oauth_version=\"1.0\"".format(key, method, signature, time, nonce)
    # print(Header)
    headers = {
        'Content-Type': "application/json",
        'Authorization': Header,
        'Cache-Control': "no-cache",
    }
    
    response = requests.request("POST", url, data=payload, headers=headers)
    return json.loads(response.text)['accessToken']
if __name__ == "__main__":
    accessToken = get_token()
    if accessToken == '':
        print("Access token not granted.Please contact the admin")
        sys.exit(-1)
    print("Access token granted: " + accessToken)
