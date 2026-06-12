from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

query = {

    "query": {

        "bool": {

            "must": [

                {

                    "match": {

                        "category": "electronics"
                    }
                }

            ],

            "filter": [

                {

                    "range": {

                        "price": {

                            "lte": 5000
                        }
                    }
                }

            ]
        }
    }
}

results = es.search(index="products", body=query)

print(results)
