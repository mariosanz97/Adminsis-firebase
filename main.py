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
  c = db.generate_key()
  v = input('valor:')
  data = {c: v}
  print(user['email'])
  path = str(user['email']).split("@")
  import re
  line = re.sub(r'[^\w]', '', path[0])
  print(line)

  db.child("Users").child(line).update(data, user['idToken'])

  print("añadido correctamente")


def add_key(user):
  c = input('clave: ')
  v = input('valor: ')
  data = {c: v}
  print(user['email'])
  path = str(user['email']).split("@")
  import re
  line = re.sub(r'[^\w]', '', path[0])
  print(line)

  db.child("Users").child(line).update(data, user['idToken'])

  print("añadido correctamente")

def getinfo(user):
  all_users = db.child("Users").get(user['idToken'])
  for user in all_users.each():
    print(user.key())  # Morty
    print(user.val())  # {name": "Mortimer 'Morty' Smith"}


def update(user):
  c = input('Id para modificar: ')
  d = input('valor: ')

  path = str(user['email']).split("@")
  import re
  line = re.sub(r'[^\w]', '', path[0])

  db.child("Users").child(line).update({c: d}, user['idToken'])

def delete(user):
  path = str(user['email']).split("@")
  import re
  line = re.sub(r'[^\w]', '', path[0])
  c = input('Id para borrar: ')
  db.child("Users").child(line).child(c).remove(user['idToken'])


"""
·······································API··········································
"""


import requests
def getinfoAPI(user):
  response = requests.get('https://adminsis-50e2e.firebaseio.com/Users.json?auth='+user['idToken'])
  import json
  json_string = json.dumps(response.json(), indent=4)
  print(json_string)

def crearRamaApi(user):
  path = str(user['email']).split("@")
  import re
  line = re.sub(r'[^\w]', '', path[0])

  c = input('clave: ')
  d = input('valor: ')
  response = requests.post('https://adminsis-50e2e.firebaseio.com/Users/'+line+'.json?auth='+user['idToken'], data='{"'+c+'":"'+d+'"}')
  print(response.text)

def AddRamaApi(user):
  path = str(user['email']).split("@")
  import re
  line = re.sub(r'[^\w]', '', path[0])

  d = input('valor: ')
  response = requests.patch('https://adminsis-50e2e.firebaseio.com/Users/'+line+'.json?auth='+user['idToken'], data='{"'+db.generate_key()+'":"'+d+'"}')
  print(response.text)

def AddRamaApiCon_clave(user):
  path = str(user['email']).split("@")
  import re
  line = re.sub(r'[^\w]', '', path[0])

  c = input('clave: ')
  d = input('valor: ')
  response = requests.patch('https://adminsis-50e2e.firebaseio.com/Users/'+line+'.json?auth='+user['idToken'], data='{"'+c+'":"'+d+'"}')
  print(response.text)

def UpdateRamaApi(user):
  path = str(user['email']).split("@")
  import re
  line = re.sub(r'[^\w]', '', path[0])

  d = input('Clave del valor que quieres modificar: ')
  v = input('valor: ')
  response = requests.patch('https://adminsis-50e2e.firebaseio.com/Users/'+line+'.json?auth='+user['idToken'], data='{"'+d+'":"'+v+'"}')
  print(response.text)


def deleteApi(user):
  path = str(user['email']).split("@")
  import re
  line = re.sub(r'[^\w]', '', path[0])

  d = input('Clave del valor que quieres modificar: ')
  response = requests.delete('https://adminsis-50e2e.firebaseio.com/Users/'+line+'/'+d+'.json?auth='+user['idToken'])
  print(response.text)

def acciones(user):
  x=True
  while(x==True):
    print("1 Mostrar datos")
    print("2 Crear rama con tu propia clave")
    print("3 Añadir dato con clave automatica")
    print("4 Añadir dato con una clave propia")
    print("5 Modificar Datos")
    print("6 Eliminar Datos")
    print("7 Salir")
    option = input('Elige opcion: ')
    if (option == '1'):
      #getinfo(user)
      getinfoAPI(user)
    if (option == '2'):
      crearRamaApi(user)
      #add_key(user)
    if (option == '3'):
      AddRamaApi(user)
      #add(user)
    if (option == '4'):
      AddRamaApiCon_clave(user)
      #update(user)
    if (option == '5'):
      UpdateRamaApi(user)
    if (option == '6'):
      #delete(user)
      deleteApi(user)
    if (option == '7'):
      SystemExit(0)
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
  #user = auth.sign_in_with_email_and_password("mario.s_97@hotmail.com", "123456")
  #print(user)
  acciones(user)


x=True
while(x==True):
  if(auth.current_user==None):
    print("1 Registrarse")
    print("2 Logearse")
    print("3 Salir")
    option = input('Elige opcion: ')
    if(option=='1'):
      registro()
    if(option=='2'):
      login()
    if(option=='3'):
      x=False
      SystemExit(0)



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




