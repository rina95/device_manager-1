import pyrebase
import os

def firebase():
  config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "databaseURL": os.getenv("FIREBASE_DB_URL"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_IP"),
  }
  return pyrebase.initialize_app(config)

def all_employees_code():
  db = firebase().database()
  all_employees = db.child("EMPLOYEE").get()
  codes = []
  for user in all_employees.each():
    codes.append(user.val()["employeeCode"])
  return codes

