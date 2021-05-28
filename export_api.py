import requests
import json
import time
import re

#setup url and token
requestHeader = {}
requestHeader['accessToken'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOjIwNSwicmVwb3NpdG9yeSI6ImljZWRxXzE2NTBfb3JhX3FhX3Y4IiwidXNlck5hbWUiOiJhZG1pbiIsImNhbGxlZEZyb20iOiJSRVNUX0FQSSIsInJhbmRvbSI6Im41bnJubHI1Z21saW1vMzB2ZGVnbXZia2o3In0.4BLv0PhQRaZm_FE2QcRpuQOJfns1783DMMMfTMUjMfU'
requestHeader['Content-Type'] = 'application/json'

api_base_url='http://192.168.100.175:8300/ice/api/2.0/export'


#Export System Group
execute_api = '{base_url}/systemgroup'.format(base_url=api_base_url)
#Create the request body
requestBody = {}
requestBody['systemGroupId']=2951
#Trigger Export System Group API 
exe_requestbody=json.dumps(requestBody)
export_sg_response = requests.request("POST", execute_api, headers=requestHeader, data=exe_requestbody, allow_redirects=True)

if '200' in str(export_sg_response):
    print('Dispalying Header Information: ',export_sg_response.headers)
    attachment_details=export_sg_response.headers['content-disposition']
    fname = re.findall("filename=(.+)", attachment_details)
    filename= fname[0].replace('"','')
    open(filename, 'wb').write(export_sg_response.content)

else:
    print ("error encountered in Exporting System Group")




#Export Connection
execute_api = '{base_url}/connection'.format(base_url=api_base_url)
#Create the request body
requestBody = {}
requestBody['connectionId']=504
#Trigger Export System Group API 
exe_requestbody=json.dumps(requestBody)
export_con_response = requests.request("POST", execute_api, headers=requestHeader, data=exe_requestbody, allow_redirects=True)

if '200' in str(export_con_response):
    print('Dispalying Header Information: ',export_con_response.headers)
    attachment_details=export_con_response.headers['content-disposition']
    fname = re.findall("filename=(.+)", attachment_details)
    filename= fname[0].replace('"','')
    open(filename, 'wb').write(export_con_response.content)

else:
    print ("error encountered in Exporting Connection")



#Export Folder group
execute_api = '{base_url}/foldergroup'.format(base_url=api_base_url)
#Create the request body
requestBody = {}
requestBody['foldergroupId']=219
#Trigger Export System Group API 
exe_requestbody=json.dumps(requestBody)
export_fg_response = requests.request("POST", execute_api, headers=requestHeader, data=exe_requestbody, allow_redirects=True)

if '200' in str(export_fg_response):
    print('Dispalying Header Information: ',export_fg_response.headers)
    attachment_details=export_fg_response.headers['content-disposition']
    fname = re.findall("filename=(.+)", attachment_details)
    filename= fname[0].replace('"','')
    open(filename, 'wb').write(export_fg_response.content)

else:
    print ("error encountered in Exporting FolderGroup")




#Export Folder group
execute_api = '{base_url}/folder'.format(base_url=api_base_url)
#Create the request body
requestBody = {}
requestBody['folderId']=2961
#Trigger Export System Group API 
exe_requestbody=json.dumps(requestBody)
export_folder_response = requests.request("POST", execute_api, headers=requestHeader, data=exe_requestbody, allow_redirects=True)

if '200' in str(export_folder_response):
    print('Dispalying Header Information: ',export_folder_response.headers)
    attachment_details=export_folder_response.headers['content-disposition']
    fname = re.findall("filename=(.+)", attachment_details)
    filename= fname[0].replace('"','')
    open(filename, 'wb').write(export_folder_response.content)

else:
    print ("error encountered in Exporting Folder")




#Export Rule
execute_api = '{base_url}/rule'.format(base_url=api_base_url)
#Create the request body
requestBody = {}
requestBody['ruleIds']=192263
#Trigger Export System Group API 
exe_requestbody=json.dumps(requestBody)
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


#Export RegressionPack
execute_api = '{base_url}/rule'.format(base_url=api_base_url)
#Create the request body
requestBody = {}
requestBody['regressionIds']=192263
#Trigger Export System Group API 
exe_requestbody=json.dumps(requestBody)
export_regressionpack_response = requests.request("POST", execute_api, headers=requestHeader, data=exe_requestbody, allow_redirects=True)
print(export_regressionpack_response)
if '200' in str(export_regressionpack_response):
    print('Dispalying Header Information: ',export_regressionpack_response.headers)
    attachment_details=export_regressionpack_response.headers['content-disposition']
    fname = re.findall("filename=(.+)", attachment_details)
    filename= fname[0].replace('"','')
    open(filename, 'wb').write(export_regressionpack_response.content)

else:
    print ("error encountered in Exporting Rule")