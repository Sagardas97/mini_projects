import json
from urllib import response
from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/pentation',methods = ['GET'])
def sagar():
    p = "Welcome to Pentation Analytics"
    a = "Pentation Analytics"
    w = "https://www.pentationanalytics.com/"

    return jsonify({"Welcome Message":p,"Company":a,"Website":w})

@app.route('/',methods = ['GET'])
def home():
    r = "Welcome to our Home Page"
    return jsonify({"Welcome Message":r})

@app.route('/signin',methods = ['POST']) 
def signin():
    req = request.json
    id = req['ID']
    pasw = req['password']
    if id == "sagar" and pasw == "sagar":
        resp = jsonify({"message":"Authentication Successful"})
    else:
        resp = jsonify({"message":"Login failed"}) 

    return resp       

if __name__ == "__main__":
    app.run(debug=True)