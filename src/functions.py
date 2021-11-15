import os
from dotenv import load_dotenv
import requests
import json
import time
from functools import reduce
import operator
import pandas as pd

def getFromDict(diccionario,mapa):
    return reduce(operator.getitem,mapa,diccionario)

def extraetodo(json):
    todo = {"name": ["name"], "lat": ["location", "lat"], "lon": ["location", "lng"], "distance":['location', 'distance']} 
    total = []
    for elemento in json:
        dic = {key: getFromDict(elemento, value) for key,value in todo.items()}
        dic["location"] = {'type': 'Point', 'coordinates': [dic["lat"], dic["lon"]]}
        total.append(dic)
    return total

client_id = os.getenv("tok1")
client_secret = os.getenv("tok2")

def get_data (latitude, longitude, query):
    time.sleep(2)
    parametres = {"client_id" : os.getenv("tok1"),
              "client_secret" : os.getenv("tok2"),
              "v": "20180323",
              "ll": f"{latitude},{longitude}", 
              "query":query,
              "limit": 100}
    time.sleep(1)

    resp = requests.get(url= 'https://api.foursquare.com/v2/venues/search', params=parametres).json()
    return resp

def respven(dic):
    return dic['response']['venues']

def fin(city, q):
    return extraetodo(respven(get_data(city['coordinates'][0], city['coordinates'][1],q)))

def todf(fincity):
    fordf = []
    for dic in fincity:
            for i in dic:
                todf = {}
                todf["name"] = getFromDict(i,["name"])
                todf["lat"] = getFromDict(i,["lat"])
                todf["lon"] = getFromDict(i,["lon"])
                todf["location"] = getFromDict(i,["location"])
                todf["category"] = getFromDict(i,["category"])
                todf["distance"] = getFromDict (i,["distance"])
                fordf.append(todf)
    df = pd.DataFrame(fordf)
    return df

def dropbydist(df, dis, cat):
    return df.drop(df[(df.distance > dis) & (df.category == cat)].index, inplace=True)

