from pyrebase import pyrebase

config = {
  "apiKey": "AIzaSyADNrd2ixpxkPjceRVOfVDIE_83ZRFqMes",
  "authDomain": "adminsis-50e2e.firebaseapp.com",
  "databaseURL": "https://adminsis-50e2e.firebaseio.com/",
  "projectId": "adminsis-50e2e",
  "storageBucket": "adminsis-50e2e.appspot.com"
}


firebase = pyrebase.initialize_app(config)

#REGISTRO
auth = firebase.auth()
#email = input('Please enter email')
#passw = input('Please enter your passwprd')
#user = auth.create_user_with_email_and_password(email, passw)

#INICIO SESION
user = auth.sign_in_with_email_and_password("marios.sanzs@gmail.com", "123456")
#auth.send_email_verification(user['idToken'])

print(auth.get_account_info(user['idToken']))

print("aaaaaaa")
print(user['localId'])

# Get a reference to the database service
db = firebase.database()


data = {"name22": "set mario o"}
db.child("Users").child(user['localId']).set(data, user['idToken'])

# data to save
data = {
    "name": "push mario"
}
results = db.child("Users").child(user['localId']).push(data, user['idToken'])



db.child("Users").child(user['localId']).child("name22").remove(user['idToken'])

users = db.child("Users").get(user['idToken'])
print(users.val())





