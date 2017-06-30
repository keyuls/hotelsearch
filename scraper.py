from flask import make_response
import requests
import json
from multiprocessing.dummy import Pool as ThreadPool

collect=[]

def performAction(action):
       result ={"results":searchSite()}
       response = jsonResponse(result)
       return response

def searchSite():
    sites =['Expedia','Orbitz','Travelocity','Priceline','Hilton']
    store=[]
    pm = ThreadPool(processes=5)
    results = pm.map_async(scrapSite,sites)
    pm.close()
    pm.join()       
    return collect

def scrapSite(site):
    baseurl="http://localhost:9000/scrapers/"
    url = baseurl+site 
    result = requests.get(url)
    result = result.json()
    collect.extend(result.get("results"))
    collect.sort(key=sortByEcstasy,reverse=True)
    return

def jsonResponse(result):
    res = json.dumps(result, indent=4)
    res = make_response(res)
    res.headers['content-type'] = 'application/json'
    return res

def sortByEcstasy(data):
    try:
        return int(data['ecstasy'])
    except KeyError:
        return 0
