import requests #Needed for making HTTP requests
import time #Needed to generate the OAuth timestamp
import urllib.parse #Needed to URLencode the parameter string
from base64 import b64encode  #Needed for create_signature function
import hmac  #Needed for create_signature function
import hashlib #Needed for create_signature functionx
import binascii#Needed for create_signature function

grant_type = 'client_credentials'
oauth_consumer_key = 'T7htmXCALsbOTfyRPwZbLQ' #'HERE.ACCESS.KEY.ID' From credentials.properties file
access_key_secret = 'IheOYj_YsApBkCTjaxVz2DBe47FZ6PQu6T_OlitB43QRddHQpJPMEkBrsvoS2DmrXZffEBX1bp9TRvmpESt0Kg' #'HERE.ACCESS.KEY.SECRET' From credentials.properties file
oauth_nonce = str(int(time.time()*1000))
oauth_timestamp = str(int(time.time()))
oauth_signature_method = 'HMAC-SHA256'
oauth_version = '1.0'
url = 'https://account.api.here.com/oauth2/token'

# HMAC-SHA256 hashing algorithm to generate the OAuth signature
def create_signature(secret_key, signature_base_string):
    encoded_string = signature_base_string.encode()
    encoded_key = secret_key.encode()
    temp = hmac.new(encoded_key, encoded_string, hashlib.sha256).hexdigest()
    byte_array = b64encode(binascii.unhexlify(temp))
    return byte_array.decode()
    
# concatenate the six oauth parameters, plus the request parameters from above, sorted alphabetically by the key and separated by "&"
def create_parameter_string(grant_type, oauth_consumer_key,oauth_nonce,oauth_signature_method,oauth_timestamp,oauth_version):
    parameter_string = ''
    parameter_string = parameter_string + 'grant_type=' + grant_type
    parameter_string = parameter_string + '&oauth_consumer_key=' + oauth_consumer_key
    parameter_string = parameter_string + '&oauth_nonce=' + oauth_nonce
    parameter_string = parameter_string + '&oauth_signature_method=' + oauth_signature_method
    parameter_string = parameter_string + '&oauth_timestamp=' + oauth_timestamp
    parameter_string = parameter_string + '&oauth_version=' + oauth_version
    return parameter_string
   
parameter_string = create_parameter_string(grant_type, oauth_consumer_key,oauth_nonce,oauth_signature_method,oauth_timestamp,oauth_version)
encoded_parameter_string = urllib.parse.quote(parameter_string, safe='')
encoded_base_string = 'POST' + '&' + urllib.parse.quote(url, safe='')
encoded_base_string = encoded_base_string + '&' + encoded_parameter_string

# create the signing key
signing_key = access_key_secret + '&'

oauth_signature = create_signature(signing_key, encoded_base_string)
encoded_oauth_signature = urllib.parse.quote(oauth_signature, safe='')

#---------------------Requesting Token---------------------
body = {'grant_type' : '{}'.format(grant_type)}

headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Authorization' : 'OAuth oauth_consumer_key="{0}",oauth_nonce="{1}",oauth_signature="{2}",oauth_signature_method="HMAC-SHA256",oauth_timestamp="{3}",oauth_version="1.0"'.format(oauth_consumer_key,oauth_nonce,encoded_oauth_signature,oauth_timestamp)
          }
    
response = requests.post(url, data=body, headers=headers)

print(response.text)
