import requests
import json
import time
import re

#setup url and token
requestHeader = {}
requestHeader['accessToken'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOjIwNSwicmVwb3NpdG9yeSI6ImljZWRxXzE2NTBfb3JhX3FhX3Y4IiwidXNlck5hbWUiOiJhZG1pbiIsImNhbGxlZEZyb20iOiJSRVNUX0FQSSIsInJhbmRvbSI6ImE4NDNwYmpybGFzMzJ1bDA1aWg3YTE0YzYyIn0.A6xm4Jt9jcs0_8r1hswcNJgJV5bLKf3HMZ8SgZJfW38'
requestHeader['Content-Type'] = 'application/json'
requestHeader['Content-Disposition'] = 'form-data'

api_base_url='http://192.168.100.175:8300/ice/api/2.0/import'

#Export Rule

#Create the request body
requestBody = {}
requestBody['connection']=[{}]
requestBody['connection'][0]={}
requestBody['connection'][0]['find']=''
requestBody['connection'][0]['replace']=''
requestBody['parameter']=[{}]
requestBody['parameter'][0]={}
requestBody['parameter'][0]['find']=''
requestBody['parameter'][0]['replace']=''

exe_requestbody=json.dumps(requestBody)

#Trigger Import API 

inputfile={'file':open('C:/Users/ParimalItankar/Downloads/DEMO-RETAIL-MS_1622222322588.tar','rb')}

export_rule_response = requests.request("POST", api_base_url, data=exe_requestbody, headers=requestHeader,  files=inputfile ,allow_redirects=True)

if '200' or '202' in str(export_rule_response):
    respose=export_rule_response.json()
    print(respose)

else:
    print ("error encountered in Exporting Rule") 
