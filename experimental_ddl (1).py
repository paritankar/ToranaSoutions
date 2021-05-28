'''
Created on Dec 12, 2020

@author: Ashwin Bhimate
'''
from _io import StringIO
import json
import re
import os
import requests
from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('D:/Electrik.ai/1DMP/MDW Scripts/eai-datastore-scripts/BACKUP/eai-prod-298215-7fa8670fdb27.json')
project_id = 'eai-prod-298215'
client = bigquery.Client(credentials= credentials,project=project_id)

# FILE_PATH = 'D:\\Ashwin\\Projects\\Electrik.aI Microservices\\documents\\DMP Scripts\\linkedin_ad_master.sql'
BASE_PATH = "D:\\Electrik.ai\\1DMP\\Upoload Script"
MEANT_FOR = 'MDW'
ACCESS_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJUdXQ3V0tnRjhUSmNhUi1fUDRTamoyeWNDM09jRE1iRHUxOFJRYncxeDhrIn0.eyJleHAiOjE2MjM0NzAwMDMsImlhdCI6MTYyMDg3ODAwMywianRpIjoiODE5MGFhNzQtYTI0MS00ZTMxLWEzNGQtNDdlNDVjNDk4MTA3IiwiaXNzIjoiaHR0cHM6Ly9pYW0uZWxlY3RyaWsuYWkvYXV0aC9yZWFsbXMvZWxlY3RyaWsuYWkiLCJhdWQiOlsicmVhbG0tbWFuYWdlbWVudCIsImFjY291bnQiXSwic3ViIjoiYjE3YzA1N2QtZjgzYS00MDIzLWE2ZjEtNTExMWJiZDNiZjNmIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiZWxlY3RyaWsuYWktYWRtaW4tc2VydmljZSIsInNlc3Npb25fc3RhdGUiOiIzYzc1MGM5MC1jOTBkLTQ2YTktYTMzZi1kMGQ1YzdlY2Y2YzYiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHBzOi8vaW8tc2VydmljZS11aS12Mi00b2NocWt6NHdxLXVjLmEucnVuLmFwcCIsImh0dHBzOi8vY2RwLmVsZWN0cmlrLmFpIiwiaHR0cDovL2xvY2FsaG9zdDo5NDAwIiwiaHR0cDovL2xvY2FsaG9zdDo0MjAwIiwiaHR0cDovL2xvY2FsaG9zdDo5MjAwIiwiaHR0cDovL2VhaS5jZHAubm9kZTo0MjAwIiwiaHR0cHM6Ly9pYW0uZWxlY3RyaWsuYWkiLCJodHRwOi8vZWFpLmNkcC5ub2RlOjQzMDAiLCJodHRwOi8vbG9jYWxob3N0OjkxMDAiLCJodHRwczovL2FkbWluLmVsZWN0cmlrLmFpIiwiaHR0cHM6Ly9hcGkuZWxlY3RyaWsuYWkiLCJodHRwczovL2lvLmVsZWN0cmlrLmFpIiwiaHR0cHM6Ly9zdGFnaW5nLmVsZWN0cmlrLmFpIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJBZ2VuY3kgQWRtaW4iLCJQcm9qZWN0IFVzZXIiLCJPcmdhbml6YXRpb24gTWFuYWdlciIsIm9mZmxpbmVfYWNjZXNzIiwiQ29uZmlndXJhdGlvbiBNYW5hZ2VyIiwiQ0RQIFVzZXIiLCJDRFAgTWFuYWdlciIsInVtYV9hdXRob3JpemF0aW9uIiwiQWdlbmN5IE1hbmFnZXIiLCJPcmdhbml6YXRpb24gQWRtaW4iLCJTdXBlcnVzZXIiLCJJTyBEZXZlbG9wZXIiXX0sInJlc291cmNlX2FjY2VzcyI6eyJyZWFsbS1tYW5hZ2VtZW50Ijp7InJvbGVzIjpbInZpZXctaWRlbnRpdHktcHJvdmlkZXJzIiwidmlldy1yZWFsbSIsIm1hbmFnZS1pZGVudGl0eS1wcm92aWRlcnMiLCJpbXBlcnNvbmF0aW9uIiwicmVhbG0tYWRtaW4iLCJjcmVhdGUtY2xpZW50IiwibWFuYWdlLXVzZXJzIiwicXVlcnktcmVhbG1zIiwidmlldy1hdXRob3JpemF0aW9uIiwicXVlcnktY2xpZW50cyIsInF1ZXJ5LXVzZXJzIiwibWFuYWdlLWV2ZW50cyIsIm1hbmFnZS1yZWFsbSIsInZpZXctZXZlbnRzIiwidmlldy11c2VycyIsInZpZXctY2xpZW50cyIsIm1hbmFnZS1hdXRob3JpemF0aW9uIiwibWFuYWdlLWNsaWVudHMiLCJxdWVyeS1ncm91cHMiXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJ2aWV3LWNvbnNlbnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsIm1hbmFnZS1jb25zZW50Iiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiRWxlY3RyaWsuQUkgU3VwZXJ1c2VyIiwicHJlZmVycmVkX3VzZXJuYW1lIjoic3VwZXJ1c2VyIiwiZ2l2ZW5fbmFtZSI6IkVsZWN0cmlrLkFJIiwiZmFtaWx5X25hbWUiOiJTdXBlcnVzZXIiLCJlbWFpbCI6InJlZ2lzdGVyQGVsZWN0cmlrLmFpIn0.QBPX_n1eGQjy89n2hbIMhZyjm9hJQ3Bzrea_ZWQTvrT5A5Ke_OFeI2QUtxUvYq6YTdyloj08FMtBs1N2LLr8z56VjRtjFnwS4lksleO5EKQ_MBhBGg2qZ3vROHFH5bDt6apmTptOw4NJAlUacqcctsZs5Opr9LxLlhZMUIT_-7MKiVB3JPHQmI7f0rjwii1ir-4JBZ_WN3pl8SZdUfZx00e7pPYmsA6YzXtjEfDvTZLaOHv4wxCbeD5kTf4eqLdhodh1RENIQtJsNMQU1-ljQNtD5Tggxo1A1fr2RDBwAA2BCWvZFKEg9KaQDVqTOxkt8-cuTiWtYoV3NNyp2Z-tqw'

ddls = []

def read_queries(file_path):
    query = StringIO()
    is_procedure = False
    
    with open(file_path, 'r') as file:
        for line in file:
            
            if re.search('procedure', line.strip(), re.IGNORECASE):
                is_procedure = True
                query.write(line.strip())
                query.write(' ')
            elif is_procedure == True and line.strip().endswith('END;') or line.strip().endswith('end;'):
                query.write(line.strip())
                query.write(' ')
                create_ddl_reference(query.getvalue().strip())
                query = StringIO()
                is_procedure = False
            elif line.strip().startswith('--') or line.strip().startswith('/*'):
#                 print(line.strip())
                continue
            elif is_procedure == False and line.strip().endswith(';'):
                query.write(line.strip())
                query.write(' ')
                create_ddl_reference(query.getvalue().strip())
                query = StringIO()
            else:
                query.write(line.strip().strip())
                query.write(' ')


def create_ddl_reference(query):
    query = query.replace('icedq', '${dataset-id}').replace('electrik-ai-dev', '${project-id}').replace('\t', ' ')
    ddl_reference_payload = {}
    ddl_reference_payload['entityType'] = get_entity_type(query)
    ddl_reference_payload['id'] = get_table_name(query)
    ddl_reference_payload['sql'] = query
    ddl_reference_payload['properties'] = {}
    ddl_reference_payload['properties']['meantFor'] = MEANT_FOR
    ddls.append(ddl_reference_payload)


def get_table_name(query):
    start_index = query.find('.')
    start_index += 1
    end_index = query.find('(')
    entity_name = query[start_index:end_index].strip().replace('`', '')
    entity_name = entity_name.replace('${dataset-id}', '')
    entity_name = entity_name.replace('${project-id}', '')
    entity_name = entity_name.replace('.', '')
    
    if len(entity_name) > 200 or  (' ' in entity_name) == True:
        entity_name = entity_name[0: entity_name.find('AS')]
        entity_name = entity_name.strip()
        
    return entity_name


def get_entity_type(query):
    if re.search('table', query, re.IGNORECASE):
        return 'table'
    elif re.search('procedure', query, re.IGNORECASE):
        return 'procedure'
    elif re.search('view', query, re.IGNORECASE):
        return 'view'
    elif query.startswith('call') or query.startswith('CALL'):
        return 'procedure call'


def batch_upload_ddl():
    
    url = 'https://api.electrik.ai/datastore/v1/ddl/references/batch-upload'
    request_headers = {
        'Authorization': 'Bearer ' + ACCESS_TOKEN,
        'Content-Type': 'application/json'
    }
    file_path = "D:\\Electrik.ai\\1DMP\\MDW Scripts\\new 4.txt"
    f = open(file_path, "w")
    f.write(json.dumps(ddls))
    print(json.dumps(ddls))
    f.close()  
    response = requests.post(url, headers=request_headers, data=json.dumps(ddls))
    print('Response code: ' + response.status_code.__str__())
    print('Response code: ' + response.text)


for dirpath, dirnames, files in os.walk(BASE_PATH):
    print(f'Found directory: {dirpath}')
    if dirpath.find('git') == -1: 
        for file_name in files:
            if file_name.find('git') != -1:
                print (f'ignore: {file_name}')
            else:
                print(file_name)
                read_queries(dirpath + '\\' + file_name)



batch_upload_ddl()

query_update =client.query("""
   UPDATE `datastore_operations.eai_entities_ddl_staging` SET Entity_type='procedure',priority=60 where Entity_key like 'sp_%' and Entity_type='table'
 """)
result3 = query_update.result()

query_dedup = client.query("""
   DELETE from datastore_operations.eai_entities_ddl_staging WHERE (concat(Entity_key , Entity_type ), Update_dttm) IN (
SELECT(EntityKey,Update_dttm)FROM (    SELECT    concat(Entity_key , Entity_type ) as EntityKey, Update_dttm, ROW_NUMBER() OVER (PARTITION BY concat(Entity_key , Entity_type )    ORDER BY Update_dttm DESC) AS rn FROM datastore_operations.eai_entities_ddl_staging  )a
WHERE    a.rn <> 1) """)

query_setpriority = client.query("""
   CALL datastore_operations.sp_entities_set_priorities() """)

result3 = query_update.result()
results1 = query_dedup.result() # Wait for the job to complete.
results2 = query_setpriority.result()
