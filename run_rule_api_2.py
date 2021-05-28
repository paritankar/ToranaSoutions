
import requests
import json

#setup url and token
headers = {
  'accessToken': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOjcsInJlcG9zaXRvcnkiOiJERU1PLVJFVEFJTC1NUyIsInVzZXJOYW1lIjoiYWRtaW4iLCJjYWxsZWRGcm9tIjoiUkVTVF9BUEkiLCJyYW5kb20iOiJncTNjc3UwbHFma3Zrajk5YTlrYXI5Nms5byJ9.5K8Y1aIAUjOAgaEhOyjHkubVm6IBiJAZhtYTeFOSA2Y',
  'Content-Type': 'application/json',
  'client': 'Web service'
}

#execute the rule
executerule_api = 'http://192.168.1.30:8400/ice/api/2.0/rulerun'
#create a request body 
requestBody = {}
requestBody['ruleId']=717292
requestBody['parameter']=[{}]
requestBody['parameter'][0]={}
requestBody['parameter'][0]['key']=''
requestBody['parameter'][0]['value']=''#
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

#trigger post method 
response = requests.request("POST", executerule_api, headers=headers, data=exe_requestbody)


if '200' in str(response):
    ruleresponse = response.json()
else:
    print ("error encountered in executing rule")

#Convert response in json format and print
executerule = json.dumps(response.json(), indent=4,separators=(',', ': '), ensure_ascii=False)
executerule_json = json.loads(executerule)
print(ruleresponse)


#get the status of the rule
#get the instanceid from the response of the execution of the rule
rule_instanceid= executerule_json['instanceId']

#call get status api by using the instanceid
get_status_api='http://192.168.1.30:8400/ice/api/2.0/rulerun/status/%s'%rule_instanceid
response = requests.request("GET", get_status_api, headers=headers, data={})

if '200' in str(response):
    ruleresponse = response.json()
else:
    print ("error encountered in getting status")

#print the response
rulestatus = json.dumps(response.json(), indent=4,separators=(',', ': '), ensure_ascii=False)
print (rulestatus)

#get the result of the rule(value can be detail or summary) by using instanceid
get_result_api='http://192.168.1.30:8400/ice/api/2.0/rulerun/instance/%s?result=detail'%rule_instanceid
response = requests.request("GET", get_result_api, headers=headers, data={})

if '200' in str(response):
    ruleresponse = response.json()
else:
    print ("error encountered in getting result")

#print the response
result = json.dumps(response.json(), indent=4,separators=(',', ': '), ensure_ascii=False)
print (result)
