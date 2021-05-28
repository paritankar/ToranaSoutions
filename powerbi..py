import adodbapi

# Connection string
conn = adodbapi.connect("Provider=MSOLAP; \
    Data Source='powerbi://api.powerbi.com/v1.0/myorg/iCEDQPowerBI';  ")

# Example query
print('The tables in your database are:')
for name in conn.get_table_names():
    print(name)