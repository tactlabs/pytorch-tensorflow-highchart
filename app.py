'''
Source:

Author: Raja CSP


'''
from flask import Flask,render_template, jsonify, request
import random
import json


app  = Flask(__name__)
PORT = 3000

@app.route("/", methods=["GET","POST"])
def startpy():

    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    # return jsonify(result)
    return render_template("index.html") 

'''
http://0.0.0.0:3091/api/data
'''

@app.route("/api/data", methods=["GET"])
def api_get_data():

    year       =  ['2016', '2017', '2018', '2019', '2020']
    pytorch    = [0,0,20,60,160]
    tensorFlow = [0,10,70,90,80]

    result_dict = {

        'year'       : year,
        'pytorch'    : pytorch,
        'tensorFlow' : tensorFlow

    }

    return jsonify(result_dict)


if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port = PORT)