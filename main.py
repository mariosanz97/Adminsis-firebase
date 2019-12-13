from pyrebase import pyrebase

config = {
  "apiKey": "AIzaSyADNrd2ixpxkPjceRVOfVDIE_83ZRFqMes",
  "authDomain": "adminsis-50e2e.firebaseapp.com",
  "databaseURL": "https://adminsis-50e2e.firebaseio.com/",
  "projectId": "adminsis-50e2e",
  "storageBucket": "adminsis-50e2e.appspot.com"
}


firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
db = firebase.database()

user = ""

def add(user):
  c = input('clave:')
  v = input('valor:')
  data = {c: v}
  #db.child("Users").child(user['email']).set(data, user['idToken'])
  print(user['email'])
  path = str(user['email']).split("@")
  import re
  line = re.sub(r'[^\w]', '', path[0])
  print(line)
  db.child("Users").child(line).set(data, user['idToken'])
  print("añadido correctamente")


def getinfo(user):
  users = db.child("Users").get(user['idToken'])
  print(users.val())


def acciones(user):
  x=True
  while(x==True):
    print("0 Mostrar datos")
    print("1 Añadir dato")
    print("2 Modificar Datos")
    print("3 Eliminar Datos")
    option = input('Elige opcion: ')
    if (option == '0'):
      getinfo(user)
    if (option == '1'):
      add(user)
    if (option == '2'):
      #update()
      print("update")
    if (option == '3'):
      print("delete")
      #delete()
    if (option == '3'):
      x = False

def registro():
  print("Registrate con email y usuario")
  email = input('Please enter email: ')
  passw = input('Please enter your passwprd: ')
  user = auth.create_user_with_email_and_password(email, passw)
  auth.send_email_verification(user['idToken'])
  print("Por favor, verifica tu correo electronico")

def login():
  print("Login con email y usuario")
  email = input('Please enter email: ')
  passw = input('Please enter your passwprd: ')
  user = auth.sign_in_with_email_and_password(email, passw)
  #user = auth.sign_in_with_email_and_password("marios.sanzs@gmail.com", "123456")
  print(user)
  acciones(user)


x=True
while(x==True):
  if(auth.current_user==None):
    print("1 Registrarse")
    print("2 Logearse")
    print("3 Falir")
    option = input('Elige opcion: ')
    if(option=='1'):
      registro()
    if(option=='2'):
      login()
    if(option=='3'):
      x=False



#REGISTRO
#print("Registrate con email y usuario")
#email = input('Please enter email')
#passw = input('Please enter your passwprd')
#user = auth.create_user_with_email_and_password(email, passw)

#INICIO SESION
#print("Logeate y verifica el email")
#user = auth.sign_in_with_email_and_password("marios.sanzs@gmail.com", "123456")
#auth.send_email_verification(user['idToken'])


"""
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
"""




