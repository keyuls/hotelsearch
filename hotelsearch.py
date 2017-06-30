from flask import Flask
import scraper as sc

app = Flask(__name__)

# GET hotels/search/
@app.route('/hotels/search/',methods=['GET'])
def searchhotel():
    response = sc.searchAction()
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000)
