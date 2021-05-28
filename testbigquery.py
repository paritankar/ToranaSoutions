from google.cloud import bigquery
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file('C:/Users/ParimalItankar/Downloads/electrik-ai-dev-e46fa8ed4be1.json')

project_id = 'electrik-ai-dev'
client = bigquery.Client(credentials= credentials,project=project_id)

query_job = client.query("""
   INSERT INTO mdw_test.test (NAME) VALUES ('Success') """)

results = query_job.result() # Wait for the job to complete.
print(results)