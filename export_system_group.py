import requests
import json
import time
import re

#setup url and token
requestHeader = {}
requestHeader['accessToken'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOjIwNSwicmVwb3NpdG9yeSI6ImljZWRxXzE2NTBfb3JhX3FhX3Y4IiwidXNlck5hbWUiOiJhZG1pbiIsImNhbGxlZEZyb20iOiJSRVNUX0FQSSIsInJhbmRvbSI6Im41bnJubHI1Z21saW1vMzB2ZGVnbXZia2o3In0.4BLv0PhQRaZm_FE2QcRpuQOJfns1783DMMMfTMUjMfU'
requestHeader['Content-Type'] = 'application/json'
#requestHeader['client'] = 'Web service'
#requestHeader['repository'] = 'DEMO-RETAIL-MS'

api_base_url='http://192.168.100.175:8300/ice/api/2.0/export'
#execute the rule
execute_rule_api = '{base_url}/systemgroup'.format(base_url=api_base_url)

requestBody = {}
requestBody['systemGroupId']=2951

exe_requestbody=json.dumps(requestBody)

rule_run_response = requests.request("POST", execute_rule_api, headers=requestHeader, data=exe_requestbody, allow_redirects=True)
print(rule_run_response.headers)
d=rule_run_response.headers['content-disposition']
print(d)
fname = re.findall("filename=(.+)", d)
print(fname[0])
filename= fname[0]
filename2= filename.replace('"','')
print(filename2)
open(filename2, 'wb').write(rule_run_response.content)
    