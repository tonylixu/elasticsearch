# make sure ES is up and running
import requests
from elasticsearch import Elasticsearch
res = requests.get('http://localhost:9200')
print(res.content)

# Now connect to cluster

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])