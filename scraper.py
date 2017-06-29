from flask import make_response
import requests
import json
from multiprocessing.dummy import Pool as ThreadPool
import heapq


def performAction(action):
    #if action=="search":
       result = searchSite()
       result ={"results":result}
       response = jsonResponse(result)
       return response

def searchSite():
    sites=['Expedia','Orbitz','Priceline','Travelocity','Hilton']
    store=[]
    pm = ThreadPool(5)
    results = pm.map(scrapSite,sites)
    pm.close()
    pm.join()
    merged=heapq.merge(results)
    '''for x in results:
        for y in x:
            store.append(y)
    store.sort(key=sortByEcstasy,reverse=True) ' '''
    return list(merged)

def scrapSite(site):
    baseurl="http://localhost:9000/scrapers/"
    url = baseurl+site
    result = requests.get(url)
    result = result.json()
    result = result.get("results")
    return result

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