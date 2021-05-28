import requests
import json
import time
import re

#setup url and token
requestHeader = {}
requestHeader['accessToken'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOjIwNSwicmVwb3NpdG9yeSI6ImljZWRxXzE2NTBfb3JhX3FhX3Y4IiwidXNlck5hbWUiOiJhZG1pbiIsImNhbGxlZEZyb20iOiJSRVNUX0FQSSIsInJhbmRvbSI6Im41bnJubHI1Z21saW1vMzB2ZGVnbXZia2o3In0.4BLv0PhQRaZm_FE2QcRpuQOJfns1783DMMMfTMUjMfU'
requestHeader['Content-Type'] = 'application/json'

api_base_url='http://192.168.100.175:8300/ice/api/2.0/export'

#Export Rule
execute_api = '{base_url}/rule'.format(base_url=api_base_url)
#Create the request body
requestBody = {}
requestBody['ruleIds']=190501
#Trigger Export System Group API 
exe_requestbody=json.dumps(requestBody)
print(exe_requestbody)
export_rule_response = requests.request("POST", execute_api, headers=requestHeader, data=exe_requestbody, allow_redirects=True)
print(export_rule_response)

if '200' in str(export_rule_response):
    print('Dispalying Header Information: ',export_rule_response.headers)
    attachment_details=export_rule_response.headers['content-disposition']
    fname = re.findall("filename=(.+)", attachment_details)
    filename= fname[0].replace('"','')
    open(filename, 'wb').write(export_rule_response.content)

else:
    print ("error encountered in Exporting Rule")