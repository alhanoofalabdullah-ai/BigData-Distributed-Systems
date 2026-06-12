from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

query = {

    "query": {

        "fuzzy": {

            "product_name": {

                "value": "laptpo"
            }
        }
    }
}

results = es.search(index="products", body=query)

print(results)
