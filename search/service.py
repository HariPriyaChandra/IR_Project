from elasticsearch import Elasticsearch

class RetrieveResults:
    def __init__(self):
        self.es = Elasticsearch(["https://5le474lcfl:emqtdufgbg@shri-ir-project-3685951519.us-east-1.bonsaisearch.net:443"])

    def get_results_by_bm25(self, query):
        results = self.es.search(index="science_fiction_films_index1",
                body={"query": {
                                "match": {"description": query}
                                }
                     }
                        )

        processed_results = []

        for result in results['hits']['hits']:
            #print(type(result))
            processed_results.append(result['_source'])
        return processed_results

    def get_results_by_jelinekMercer(self, query):
        results = self.es.search(index="science_fiction_films_index_2",
                body={"query": {
                      "bool": {
                            "must": {
                                "match_phrase": {
                                    "description": query,
                                                 }
                                    },
                                #"filter": {"bool": {"must_not": {"match_phrase": {"director": "George Albert Smith"}}}},
                                     },
                               },            
                     }
                )
        processed_results = []

        for result in results['hits']['hits']:
            #print(type(result))
            processed_results.append(result['_source'])
        return processed_results

