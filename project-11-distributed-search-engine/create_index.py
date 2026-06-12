from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

index_name = "products"

if not es.indices.exists(index=index_name):

    es.indices.create(index=index_name)

    print("Index created successfully")
