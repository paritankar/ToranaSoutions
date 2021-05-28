import requests
import json
import time
import re

#setup url and token
requestHeader = {}
requestHeader['accessToken'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOjIwNSwicmVwb3NpdG9yeSI6ImljZWRxXzE2NTBfb3JhX3FhX3Y4IiwidXNlck5hbWUiOiJhZG1pbiIsImNhbGxlZEZyb20iOiJSRVNUX0FQSSIsInJhbmRvbSI6ImE4NDNwYmpybGFzMzJ1bDA1aWg3YTE0YzYyIn0.A6xm4Jt9jcs0_8r1hswcNJgJV5bLKf3HMZ8SgZJfW38'
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
print(export_rule_response.headers)


if '200' in str(export_rule_response):
    print('Dispalying Header Information: ',export_rule_response.headers)
    attachment_details=export_rule_response.headers['content-disposition']
    fname = re.findall("filename=(.+)", attachment_details)
    filename= fname[0].replace('"','')
    open(filename, 'wb').write(export_rule_response.content)

else:
    print ("error encountered in Exporting Rule")