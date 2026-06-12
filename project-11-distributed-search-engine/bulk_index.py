from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json

es = Elasticsearch("http://localhost:9200")

with open("sample-data/products.json") as file:

    products = json.load(file)

actions = []

for product in products:

    actions.append({

        "_index": "products",

        "_source": product

    })

bulk(es, actions)

print("Documents indexed successfully")
