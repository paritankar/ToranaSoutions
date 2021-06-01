import requests
import json
import time

#setup url and token
requestHeader = {}
requestHeader['accessToken'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOjcsInJlcG9zaXRvcnkiOiJERU1PLVJFVEFJTC1NUyIsInVzZXJOYW1lIjoiYWRtaW4iLCJjYWxsZWRGcm9tIjoiUkVTVF9BUEkiLCJyYW5kb20iOiJncTNjc3UwbHFma3Zrajk5YTlrYXI5Nms5byJ9.5K8Y1aIAUjOAgaEhOyjHkubVm6IBiJAZhtYTeFOSA2Y'
requestHeader['Content-Type'] = 'application/json'
requestHeader['client'] = 'Web service'
requestHeader['repository'] = 'DEMO-RETAIL-MS'

api_base_url='http://192.168.1.30:8400/ice/api/2.0'
#execute the rule
execute_rule_api = '{base_url}/rulerun'.format(base_url=api_base_url)
#create a request body 
requestBody = {}
requestBody['ruleId']=744768
requestBody['parameter']=[{}]
requestBody['parameter'][0]={}
requestBody['parameter'][0]['key']=''
requestBody['parameter'][0]['value']=''
requestBody['connection']={}
requestBody['connection']['source']=[{}]
requestBody['connection']['source'][0]={}
requestBody['connection']['source'][0]['find']=''
requestBody['connection']['source'][0]['replace']=''
requestBody['connection']['target']=[{}]
requestBody['connection']['target'][0]={}
requestBody['connection']['target'][0]['find']=''
requestBody['connection']['target'][0]['replace']=''


exe_requestbody=json.dumps(requestBody)

#Trigger Rule Run API. 
rule_run_response = requests.request("POST", execute_rule_api, headers=requestHeader, data=exe_requestbody)


if '200' in str(rule_run_response):
    rule_run_json = rule_run_response.json()
    print("The run rule api is triggered")
    #time.sleep(2)
    print("The rule is running over the following instanceId")
    #time.sleep(2)
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
    run_status_api='{base_url}/rulerun/status/{instanceid}'.format(instanceid=rule_instance_id,base_url=api_base_url)
    run_status_response = requests.request("GET", run_status_api, headers=requestHeader, data={})

    if '200' in str(run_status_response):
        run_status_json = run_status_response.json()
        while run_status_json['status'] == 'Running':
            run_status_response = requests.request("GET", run_status_api, headers=requestHeader, data={})
            if '200' in str(run_status_response):
                run_status_json = run_status_response.json()
            else:
                print ("error encountered in getting status")
                #set get summary error flag
                run_get_summary='failed'
        print("The rule status:")
        print(run_status_json)
        #set get summary success flag
        run_get_summary='success'
        print(run_get_summary)
    else:
        print ("error encountered in getting status")
        #set get summary error flag
        run_get_summary='failed'