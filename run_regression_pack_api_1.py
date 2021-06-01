import requests
import json

#setup url and token
requestHeader = {}
requestHeader['accessToken'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOjcsInJlcG9zaXRvcnkiOiJERU1PLVJFVEFJTC1NUyIsInVzZXJOYW1lIjoiYWRtaW4iLCJjYWxsZWRGcm9tIjoiUkVTVF9BUEkiLCJyYW5kb20iOiJncTNjc3UwbHFma3Zrajk5YTlrYXI5Nms5byJ9.5K8Y1aIAUjOAgaEhOyjHkubVm6IBiJAZhtYTeFOSA2Y'
requestHeader['Content-Type'] = 'application/json'
requestHeader['client'] = 'Jenkins'
requestHeader['repository'] = 'DEMO-RETAIL-MS'

api_base_url='http://192.168.1.30:8400/ice/api/2.0'
#execute the regressionpack
execute_regressionpack_api = '{base_url}/regressionrun'.format(base_url=api_base_url)
#create a request body 
requestBody = {}
requestBody['regressionId']=717433
requestBody['parameter']=[{}]
requestBody['parameter'][0]={}
requestBody['parameter'][0]['key']=''
requestBody['parameter'][0]['value']=''
requestBody['connection']={}
requestBody['connection']['source']=[{},{},{}]
requestBody['connection']['source'][0]={}
requestBody['connection']['source'][0]['find']='ZenCycleOLTP'
requestBody['connection']['source'][0]['replace']='ZenCycleDW'
requestBody['connection']['source'][0]['seq']=[1]
requestBody['connection']['source'][1]['find']='ZenCycleOLTP'
requestBody['connection']['source'][1]['replace']='ZenCycleDW'
requestBody['connection']['source'][1]['seq']=[2]
requestBody['connection']['source'][2]['find']='ZenCycleDemo'
requestBody['connection']['source'][2]['replace']='ZenCycleDW'
requestBody['connection']['source'][2]['seq']=[3]
requestBody['connection']['target']=[{}]
requestBody['connection']['target'][0]={}
requestBody['connection']['target'][0]['find']=''
requestBody['connection']['target'][0]['replace']=''
requestBody['connection']['target'][0]['seq']=[]

exe_requestbody=json.dumps(requestBody)

#Trigger regressionpack Run API. 
regressionpack_run_response = requests.request("POST", execute_regressionpack_api, headers=requestHeader, data=exe_requestbody)
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
    run_status_response = requests.request("GET", run_status_api, headers=requestHeader, data={})

    if '200' in str(run_status_response):
        run_status_json = run_status_response.json()
        while run_status_json['status'] == 'Running':
            run_status_response = requests.request("GET", run_status_api, headers=requestHeader, data={})
            if '200' in str(run_status_response):
                run_status_json=run_status_response.json()
            else:
                print ("error encountered in getting status")
                #set get summary error flag
                run_get_summary='failed'
        print("The Regression Pack status:")
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
    regressionpack_exe_summ_response = requests.request("GET", get_result_api, headers=requestHeader, data={})

    if '200' in str(regressionpack_exe_summ_response):
        regressionpack_exe_summ_json=regressionpack_exe_summ_response.json()
        print("The result summary of the Regression Pack")
        print(regressionpack_exe_summ_json)
    else:
        print("error encountered in getting rule execution summary")