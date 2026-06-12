from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

query = {

    "query": {

        "match": {

            "product_name": "laptop"
        }
    }
}

results = es.search(index="products", body=query)

print(results)
