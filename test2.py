
import requests
import json

#setup url and token 


ruleAPI = 'http://96.56.44.182:8400/ice/rest/iaudit/rule/run-rule-by-code'
requestHeader = {}
requestHeader['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOjcsInJlcG9zaXRvcnkiOiJERU1PLVJFVEFJTC1NUyIsInVzZXJOYW1lIjoiYWRtaW4iLCJjYWxsZWRGcm9tIjoiUkVTVF9BUEkiLCJyYW5kb20iOiJncTNjc3UwbHFma3Zrajk5YTlrYXI5Nms5byJ9.5K8Y1aIAUjOAgaEhOyjHkubVm6IBiJAZhtYTeFOSA2Y'

#create a request body 
requestBody = {}
requestBody['userObj'] = {}
requestBody['userObj']['userName'] = 'admin'
requestBody['userObj']['repository'] = 'DEMO-RETAIL-MS'
requestBody['projectName'] = 'Data Mart - Customers'
requestBody['folderName'] = 'Customer'
requestBody['ruleCode'] = 'R007'
requestBody['paramKeyValues'] = 'runid=1^gender=M' #override parameters
requestBody['srcConName'] = ''
requestBody['trgConName'] = ''
requestBody['execMedium'] = 'Web Service'
requestBody['calledProgramName'] = 'ICEServices'

#trigger post method 
response = requests.post(ruleAPI, json=requestBody, headers=requestHeader)

if '200' in str(response):
    ruleResponse = response.json()
else:
    print ("error encountered")

#print the response
jsonOutput = json.dumps(ruleResponse, indent=4,separators=(',', ': '), ensure_ascii=False)
print(jsonOutput)
