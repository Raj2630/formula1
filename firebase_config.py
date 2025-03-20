import firebase_admin
from firebase_admin import credentials, firestore, auth

cred = credentials.Certificate("formula1-50fc0-firebase-adminsdk-fbsvc-baef6e9396.json") 
firebase_admin.initialize_app(cred)

db = firestore.client()
