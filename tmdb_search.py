import requests 
import json

def search(query):
    url = "http://localhost:9200/tmdb/movie/_search?explain"
    res = requests.get(url, data=json.dumps(query))

   # print(res.text)

    responseBody = json.loads(res.text)
    hits = responseBody["hits"]
    firstHit = hits["hits"][0]

    print("Explain for {0}".format(firstHit["_source"]["title"]))
    print(json.dumps(firstHit["_explanation"], indent=True))

    print("\n\nNum\tRelevance Score\t\tMovie Title")

    for i,hit in enumerate(hits["hits"]):
        print ("{0}\t{1}\t\t{2}".format(i+1, hit["_score"], hit["_source"]["title"]))

if __name__ == "__main__":
    searchText = "basketball with cartoon aliens"
    query = {
        "query": {
            "multi_match": {
                "query": searchText,
                "fields": ["title^10", "overview"]
            }
        }
    }

    search(query)


