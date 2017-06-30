from flask import make_response
import requests
import json
from multiprocessing.dummy import Pool as ThreadPool

# handle GET request and send response
def searchAction():
       result ={"results":searchSite()}
       response = jsonResponse(result)
       return response

# create processes for sites scraping and collecting results
def searchSite():
    store=[]   
    sites =['Expedia','Orbitz','Travelocity','Priceline','Hilton']
    pm = ThreadPool(processes=5)
    results = pm.map(scrapSite,sites)
    pm.close()
    pm.join()   
    store = sortData(results)       
    return store

# call API for each site and retrieve results
def scrapSite(site):
    baseurl="http://127.0.0.1:9000/scrapers/"
    url = baseurl+site 
    result = requests.get(url)
    result = result.json()
    result = result.get("results")
    return result

#Prepare json response to send back
def jsonResponse(result):
    res = json.dumps(result, indent=4)
    res = make_response(res)
    res.headers['content-type'] = 'application/json'
    return res


#sorting results
def sortData(results):
    store=[] 
    while len(results)>0:                                     
           minObj = [data[-1]['ecstasy'] for data in results] #getting object with minimum ecstasy value from each result
           minIndex = minObj.index(min(minObj))               #find smallest of all minimum in previous result & get index of smallest element
           store.append(results[minIndex][-1])                #store smallest elemnt in new list
           results[minIndex].pop()                            #removing element from results
           if len(results[minIndex])==0:                      #when list is empty remove it from results 
                  results.pop(minIndex)
    store.reverse()
    return store
