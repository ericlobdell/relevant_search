import requests 
import json

def extract ():
    f = open('..\ipython\\tmdb.json')
    if f:
        return json.loads(f.read())

def reindex(analysisSettings = {}, mappingSettings = {}, movieData = {}):
    settings = {
        "settings": {
            "number_of_shards": 1,
            "index": {
                "analysis": analysisSettings
            }
        }
    }

    if mappingSettings:
        settings["mappings"] = mappingSettings
    
    url = "http://localhost:9200/tmdb"
    resp = requests.delete(url)
    resp = requests.put(url, data=json.dumps(settings))

    bulkMovies = ""
    for id, movie in movieData.items():
        addCmd = {
            "index": {
                "_index": "tmdb",
                "_type": "movie",
                "_id": movie["id"]
            }
        }

        bulkMovies += json.dumps(addCmd) + "\n" + json.dumps(movie) + "\n"

    resp = requests.post("http://localhost:9200/_bulk", data=bulkMovies)

if __name__ == "__main__":
    movieData = extract()
    reindex(movieData = movieData)

