import firebase_admin
import pymongo
import os
from firebase_admin import credentials
from firebase_admin import firestore
from pymongo import MongoClient

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)
firestoreDB = firestore.client()

mongoConnString = f"mongodb+srv://{os.environ['MONGO_USER']}:{os.environ['MONGO_PASSWORD']}@{os.environ['MONGO_HOST']}"
mongoClient = MongoClient(mongoConnString)[os.environ['MONGO_DB']]

from flask import Flask
app = Flask(__name__)

@app.route('/firestore/users/<username>')
def getFirebaseUser(username):
	docs = firestoreDB.collection('users').where('name', '==', username).stream()
	for doc in docs:
		d = doc.to_dict()
		return f'Hello {username}<br>Age: {d["age"]}<br>Employee ID: {d["employee_id"]}'
	return "sorry this user doesn't exists in firestore"

@app.route('/mongodb/users/<username>')
def getMongoUser(username):
	items = mongoClient['users'].find({"name": username})
	for item in items:
		return f'Hello {username}<br>Pay Grade: {item["pay_grade"]}<br>Leaves left: {item["leaves_left"]}'
	return "sorry this user doesn't exists in mongodb"