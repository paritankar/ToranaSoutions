import requests
from urllib3.exceptions import InsecureRequestWarning
import json

#setup url and token
requestHeader = {}
requestHeader['accessToken'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOjkwNjE1MjQsInJlcG9zaXRvcnkiOiJpY2VkcV9zcGFya19zcWxzZXJ2ZXJfSU5EIiwidXNlck5hbWUiOiJwYXJpbWFsLmkiLCJjYWxsZWRGcm9tIjoiUkVTVF9BUEkiLCJyYW5kb20iOiJqNnZqMzRubmhwbXB0dnEyYTQ3ZjlxMXBkbiJ9.qkz0RQavXcfUMyEa2hXKaiwNFxcr39EFeSpC5S-Kvi8'
requestHeader['Content-Type'] = 'application/json'
requestHeader['client'] = 'Web service'
#requestHeader['repository'] = 'DEMO-RETAIL-MS'

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
api_base_url='https://192.168.100.99:8443/ice/api/2.0'
#execute the regressionpack
execute_regressionpack_api = '{base_url}/regressionrun'.format(base_url=api_base_url)
#create a request body 
requestBody = {}
requestBody['regressionId']=9103258
requestBody['parameter']=[{}]
requestBody['parameter'][0]={}
requestBody['parameter'][0]['key']=''
requestBody['parameter'][0]['value']=''
requestBody['connection']={}
requestBody['connection']['source']=[{},{}]
requestBody['connection']['source'][0]={}
requestBody['connection']['source'][0]['find']='MSSQL_FULLURL'
requestBody['connection']['source'][0]['replace']='MSSQL_FULLURL2'
requestBody['connection']['source'][0]['seq']=[1]
requestBody['connection']['source'][1]['find']='1640_Hive_UserPass_130'
requestBody['connection']['source'][1]['replace']='1640_Hive_UserPass_130_replace'
requestBody['connection']['source'][1]['seq']=[2]
requestBody['connection']['target']=[{}]
requestBody['connection']['target'][0]={}
requestBody['connection']['target'][0]['find']=''
requestBody['connection']['target'][0]['replace']=''
requestBody['connection']['target'][0]['seq']=[]

exe_requestbody=json.dumps(requestBody)
print(exe_requestbody)
#Trigger regressionpack Run API. 
regressionpack_run_response = requests.request("POST", execute_regressionpack_api, headers=requestHeader, data=exe_requestbody, verify=False)
print(regressionpack_run_response)
if '200' in str(regressionpack_run_response):
    regressionpack_run_json = regressionpack_run_response.json()
    print(regressionpack_run_json)
    #set get status success  flag
    regressionpack_get_status='success'
else:
    print ("error encountered in executing rule")
    #set error flag
    regressionpack_get_status='failed'
    regressionpack_get_summary='failed'


if regressionpack_get_status== 'success':
    #Get the regressionpack InstanceID to poll the status of regressionpack execution
    regressionpack_instance_id= regressionpack_run_json['instanceId']
    #Get the regressionpack Execution Status for above regressionpack InstanceID
    run_status_api='{base_url}/regressionrun/status/{instanceid}'.format(instanceid=regressionpack_instance_id,base_url=api_base_url)
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
    #Get the regressionpack Execution Summary
    get_result_api='{base_url}/regressionrun/instance/{instanceid}?start=1&limit=4&result=detail'.format(base_url=api_base_url,instanceid=regressionpack_instance_id)
    regressionpack_exe_summ_response = requests.request("GET", get_result_api, headers=requestHeader, data={}, verify=False)

    if '200' in str(regressionpack_exe_summ_response):
        regressionpack_exe_summ_json=regressionpack_exe_summ_response.json()
        #regressionpack_exe_summ_json=json.dumps(rule_exe_summ_response.json(), indent=4,separators=(',', ': '), ensure_ascii=False)
        print(regressionpack_exe_summ_json)
    else:
        print("error encountered in getting rule execution summary")