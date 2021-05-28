import requests
import json

#setup url and token
headers = {
  'accessToken': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOjcsInJlcG9zaXRvcnkiOiJERU1PLVJFVEFJTC1NUyIsInVzZXJOYW1lIjoiYWRtaW4iLCJjYWxsZWRGcm9tIjoiUkVTVF9BUEkiLCJyYW5kb20iOiJncTNjc3UwbHFma3Zrajk5YTlrYXI5Nms5byJ9.5K8Y1aIAUjOAgaEhOyjHkubVm6IBiJAZhtYTeFOSA2Y',
  'Content-Type': 'application/json',
  'client': 'Web service'
}

#execute the rule
execute_rule_api = 'http://96.56.44.182:8400/ice/api/2.0/rulerun'
#create a request body 
requestBody = {}
requestBody['ruleId']=255
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
rule_run_response = requests.request("POST", execute_rule_api, headers=headers, data=exe_requestbody)


if '200' in str(rule_run_response):
    rule_run_json = rule_run_response.json()
    print(rule_run_json)	
else:
    print ("error encountered in executing rule")

#Get the Rule InstanceID to poll the status of Rule execution
rule_instance_id= rule_run_json['instanceId']

#Get the Rule Execution Status for above Rule InstanceID
run_status_api='http://96.56.44.182:8400/ice/api/2.0/rulerun/status/{0}'.format(rule_instance_id)
run_status_response = requests.request("GET", run_status_api, headers=headers, data={})

if '200' in str(run_status_response):
    run_status_json = run_status_response.json()
    print(run_status_json)	
else:
    print ("error encountered in getting status")