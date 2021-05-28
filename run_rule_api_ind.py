import requests
from urllib3.exceptions import InsecureRequestWarning
import json

#setup url and token
requestHeader = {}
requestHeader['accessToken'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOjkwNjE1MjQsInJlcG9zaXRvcnkiOiJpY2VkcV9zcGFya19zcWxzZXJ2ZXJfSU5EIiwidXNlck5hbWUiOiJwYXJpbWFsLmkiLCJjYWxsZWRGcm9tIjoiUkVTVF9BUEkiLCJyYW5kb20iOiJqNnZqMzRubmhwbXB0dnEyYTQ3ZjlxMXBkbiJ9.qkz0RQavXcfUMyEa2hXKaiwNFxcr39EFeSpC5S-Kvi8'
requestHeader['Content-Type'] = 'application/json'
requestHeader['client'] = 'Web service'
#requestHeader['repository'] = 'icedq_spark_sqlserver_IND'

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
api_base_url='https://192.168.100.99:8443/ice/api/2.0'
#execute the rule
execute_rule_api = '{base_url}/rulerun'.format(base_url=api_base_url)
#create a request body 
requestBody = {}
requestBody['ruleId']=9102034
requestBody['parameter']=[{}]
requestBody['parameter'][0]={}
requestBody['parameter'][0]['key']=''
requestBody['parameter'][0]['value']=''
requestBody['connection']={}
requestBody['connection']['source']=[{}]
requestBody['connection']['source'][0]={}
requestBody['connection']['source'][0]['find']='1640_Hive_UserPass_130'
requestBody['connection']['source'][0]['replace']='1640_Hive_UserPass_130_replace'
requestBody['connection']['target']=[{}]
requestBody['connection']['target'][0]={}
requestBody['connection']['target'][0]['find']='1640_Hive_UserPass_130'
requestBody['connection']['target'][0]['replace']='1640_Hive_UserPass_130_replace'


exe_requestbody=json.dumps(requestBody)

#Trigger Rule Run API. 
rule_run_response = requests.request("POST", execute_rule_api, headers=requestHeader, data=exe_requestbody, verify=False)
print(exe_requestbody)
if '200' in str(rule_run_response):
    rule_run_json = rule_run_response.json()
    print(rule_run_json)
    #set get status success  flag
    run_get_status='success'
else:
    print ("error encountered in executing rule")
    #set error flag
    run_get_status='failed'
    run_get_summary='failed'

if run_get_status== 'success':
    #Get the Rule InstanceID to poll the status of Rule execution
    rule_instance_id= rule_run_json['instanceId']
    #Get the Rule Execution Status for above Rule InstanceID
    run_status_api='{base_url}/rulerun/status/{instanceid}'.format(instanceid=rule_instance_id,base_url=api_base_url)
    run_status_response = requests.request("GET", run_status_api, headers=requestHeader, data={}, verify=False)

    if '200' in str(run_status_response):
        run_status_json = run_status_response.json()
        print(run_status_json)
        #set get summary success flag
        run_get_summary='success'
    else:
        print ("error encountered in getting status")
        #set get summary error flag
        run_get_summary='failed'

if run_get_summary== 'success':
    #Get the Rule Execution Summary
    get_result_api='{base_url}/rulerun/instance/{instanceid}?result=detail'.format(base_url=api_base_url,instanceid=rule_instance_id)
    rule_exe_summ_response = requests.request("GET", get_result_api, headers=requestHeader, data={}, verify=False)

    if '200' in str(rule_exe_summ_response):
        rule_exe_summ_json=rule_exe_summ_response.json()
        #rule_exe_summ_json=json.dumps(rule_exe_summ_response.json(), indent=4,separators=(',', ': '), ensure_ascii=False)
        print(rule_exe_summ_json)
    else:
        print("error encountered in getting rule execution summary")