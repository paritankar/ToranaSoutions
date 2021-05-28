import requests
import json

#define the header
headers = {
  'accessToken': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOjcsInJlcG9zaXRvcnkiOiJERU1PLVJFVEFJTC1NUyIsInVzZXJOYW1lIjoiYWRtaW4iLCJjYWxsZWRGcm9tIjoiUkVTVF9BUEkiLCJyYW5kb20iOiJncTNjc3UwbHFma3Zrajk5YTlrYXI5Nms5byJ9.5K8Y1aIAUjOAgaEhOyjHkubVm6IBiJAZhtYTeFOSA2Y',
  'Content-Type': 'application/json',
  'client': 'Web service'
}

#execute the rule
executereg_api = 'http://96.56.44.182:8400/ice/api/2.0/regressionrun'
exe_reg_payload='{ "regressionId": 257, "connection": { "source": [], "target": [] } }'
response = requests.request("POST", executereg_api, headers=headers, data=exe_reg_payload)

if '200' in str(response):
    ruleresponse = response.json()
else:
    print ("error encountered in executing the rule")

executeregpack = json.dumps(response.json(), indent=4,separators=(',', ': '), ensure_ascii=False)
print(executeregpack)

#get the status
executeregpack_json = json.loads(executeregpack)
print(executeregpack_json)
rule_instanceid= executeregpack_json['instanceId']
getstatus_api = 'http://96.56.44.182:8400/ice/api/2.0/regressionrun/status/%s'%rule_instanceid
response = requests.request("GET", getstatus_api, headers=headers, data={})

if '200' in str(response):
    ruleresponse = response.json()
else:
    print ("error encountered in getting status")

getstaus_regpack = json.dumps(response.json(), indent=4,separators=(',', ': '), ensure_ascii=False)
print(getstaus_regpack)

#get result of execution
get_result_api='http://96.56.44.182:8400/ice/api/2.0/regressionrun/instance/%s?start=1&limit=100&result=regressionsummary'%rule_instanceid
response = requests.request("GET", get_result_api, headers=headers, data={})

if '200' in str(response):
    ruleresponse = response.json()
else:
    print ("error encountered in getting the result")

result = json.dumps(response.json(), indent=4,separators=(',', ': '), ensure_ascii=False)
print (result)