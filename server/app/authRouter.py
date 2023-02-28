from app import app
from flask import request
from app import userDatabase

auth = userDatabase.UserDatabase()

'''listens for login routes and calls the appropriate method to deal with the required functionaliy'''
@app.route("/auth/login", methods=['POST'])
def Login():
   username = request.json['username']
   password = request.json['password']
   return auth.Login(username, password)

'''listens for register routes and calls the appropriate method to deal with the required functionaliy'''
@app.route("/auth/register", methods=['POST'])
def Register():
   username = request.json['username']
   password = request.json['password']
   return auth.Register(username, password)