import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)
db = firestore.client()

from flask import Flask
app = Flask(__name__)

@app.route('/firestore/users/<username>')
def getFirebaseUser(username):
	docs = db.collection('mariausers').where('name', '==', username).stream()
	for doc in docs:
		d = doc.to_dict()
		print(d)
		return f'Hello {username}<br>Age: {d["age"]}<br>Employee ID: {d["employee_id"]}'
	return "sorry this user doesn't exists"
