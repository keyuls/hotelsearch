### Background
This is a hotel search API for Hipmunk that queries each of different partners sites and merges their results together. 
The list of hotels is sorted by ecstasy. 

It's run on localhost 127.0.0.1 with port 8000.
 The HTTP endpoint:
```GET /hotels/search``` - returns hotel results from all providers as JSON

### Prerequisites
- Setup [Hipproblem](https://github.com/Hipmunk/hipproblems) project
- Run [Hotel_Search](https://github.com/Hipmunk/hipproblems/tree/master/hotel_search) 

### Instructions

To run this project, follow below steps.
```
git clone https://github.com/keyuls/hotelsearch.git
cd hotelsearch
pip install -r requirements.txt
pyhton hotelsearch.py
```
