import requests

def api_movies():    

    movies = []

    api_url = "http://swapi.dev/api/films/"
    response = requests.get(api_url, verify=False)
    films = response.json()

    for i in range(0,6): 
        title = films["results"][i]["title"] 
        movies.append([title])

    return movies