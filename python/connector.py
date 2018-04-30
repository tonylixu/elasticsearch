# make sure ES is up and running
import requests
from elasticsearch import Elasticsearch
import json
res = requests.get('http://localhost:9200')
print(res.content)

# Now connect to cluster
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Iterate over swapi people documents and index them
r = requests.get('http://localhost:9200') 
i = 1
while r.status_code == 200:
    r = requests.get('http://swapi.co/api/people/'+ str(i))
    es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
    i=i+1
 
print(i)