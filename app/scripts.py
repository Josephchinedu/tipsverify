import json

def freetips(send_date):
    import requests
    

    url = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"

    querystring = {"market":"classic","iso_date":send_date}

    headers = {
        'x-rapidapi-key': "9d7.......................................",
        'x-rapidapi-host': "football-prediction-api.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    
    return json.loads(response.text)


def futurepredictions():
    import requests

    url = "https://football-betting-odds1.p.rapidapi.com/provider1/live/upcoming"

    headers = {
        'x-rapidapi-key': "9d..................................................",
        'x-rapidapi-host': "football-betting-odds1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    return json.loads(response.text)



def sportshight():
    import requests

    url = "https://free-football-soccer-videos.p.rapidapi.com/"

    headers = {
        'x-rapidapi-key': "9...................................",
        'x-rapidapi-host': "free-football-soccer-videos.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    return json.loads(response.text)

