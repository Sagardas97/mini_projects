import json
from urllib import response
from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/hello',methods = ['GET'])
def sagar():
    p = "Welcome"
    a = "Hello World"
    w = "https://www.github.com/"

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
