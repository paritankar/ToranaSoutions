
import requests
import json


#define the header
headers = {
  'accessToken': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOjcsInJlcG9zaXRvcnkiOiJERU1PLVJFVEFJTC1NUyIsInVzZXJOYW1lIjoiYWRtaW4iLCJjYWxsZWRGcm9tIjoiUkVTVF9BUEkiLCJyYW5kb20iOiJncTNjc3UwbHFma3Zrajk5YTlrYXI5Nms5byJ9.5K8Y1aIAUjOAgaEhOyjHkubVm6IBiJAZhtYTeFOSA2Y',
  'Content-Type': 'application/json',
  'client': 'Web service'
}


#execute the rule
executerule_api = 'http://96.56.44.182:8400/ice/api/2.0/rulerun'
exe_rule_payload='{ "ruleId": 255, "parameter": [ { "key": "", "value": "" } ], "connection": { "source": [], "target": [] } }'
response = requests.request("POST", executerule_api, headers=headers, data=exe_rule_payload)
print(exe_rule_payload)
if '200' in str(response):
    ruleresponse = response.json()
else:
    print ("error encountered in executing rule")

#print the response
executerule = json.dumps(response.json(), indent=4,separators=(',', ': '), ensure_ascii=False)
executerule_json = json.loads(executerule)

#get the status of the rule
rule_instanceid= executerule_json['instanceId']
get_status_api='http://96.56.44.182:8400/ice/api/2.0/rulerun/status/%s'%rule_instanceid
response = requests.request("GET", get_status_api, headers=headers, data={})

if '200' in str(response):
    ruleresponse = response.json()
else:
    print ("error encountered in getting status")

rulestatus = json.dumps(response.json(), indent=4,separators=(',', ': '), ensure_ascii=False)
print (rulestatus)

#get the result of the rule(value can be detail or summary)
get_result_api='http://96.56.44.182:8400/ice/api/2.0/rulerun/instance/%s?result=detail'%rule_instanceid
response = requests.request("GET", get_result_api, headers=headers, data={})

if '200' in str(response):
    ruleresponse = response.json()
else:
    print ("error encountered in getting result")

result = json.dumps(response.json(), indent=4,separators=(',', ': '), ensure_ascii=False)
print (result)

