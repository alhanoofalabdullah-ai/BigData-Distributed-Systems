from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

query = {

    "query": {

        "prefix": {

            "product_name": "lap"
        }
    }
}

results = es.search(index="products", body=query)

print(results)
