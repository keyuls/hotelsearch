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
    #merged=heapq.merge(results)
    #yo= min(data[0]['ecstasy'] for data in results)
    #print(yo)
    while len(results)>0:
           minObj = [data[-1]['ecstasy'] for data in results]
           print(minObj)
           minIndex = minObj.index(min(minObj))
           store.append(results[minIndex][-1])
           results[minIndex].pop()
           if len(results[minIndex])==0:
                  results.pop(minIndex)
    store.reverse()       
    '''for x in results:
        for y in x:
            store.append(y)
    store.sort(key=sortByEcstasy,reverse=True)'''
    return store

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
