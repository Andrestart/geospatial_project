from functools import reduce
import operator
""""
"""
def type_point(lista):
    return {"type":"Point", "coordinates": lista}

def getFromDict(diccionario,mapa):
    return reduce(operator.getitem,mapa,diccionario)

def extraetodo(json):
    todo = {"nombre": ["name"], "latitud": ["location", "lat"], "longitud": ["location", "lng"]} 
    total = []
    for elemento in json:
        star = {key: getFromDict(elemento, value) for key,value in todo.items()}
        star["location"] = type_point([star["latitud"], star["longitud"]])
        total.append(star)
    return total

