#from urllib3.request import localhost

from flask import Flask
import scraper as sc

app = Flask(__name__)

@app.route('/hotels/<action>')
def searchhotel(action):
    response = sc.performAction(action)
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000)
