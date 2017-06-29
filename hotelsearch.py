from urllib.request import localhost

from flask import Flask
import scraper as sc

app = Flask(__name__)

@app.route('/hotels/<action>')
def searchhotel(action):
    response = sc.performAction(action)
    return response

if __name__ == '__main__':
    app.run(host='localhost',port=8000)
