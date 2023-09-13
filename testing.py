import requests
import json

url = 'https://gachenge.pythonanywhere.com'

def addPerson(data):
    add = f'{url}/api'
    response = requests.post(add, json=data)

    if response.status_code == 201:
        return response.json()
    else:
        return f"Error {response.status_code}"

def getPerson(user_id):
    getp = f'{url}/api/{user_id}'
    response = requests.get(getp)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error {response.status_code}"

def updPerson(user_id, data):
    upd = f'{url}/api/{user_id}'
    response = requests.put(upd, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error {response.status_code}"

def delPerson(user_id):
    dele = f'{url}/api/{user_id}'
    response = requests.delete(dele)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error {response.status_code}"

newPerson = {'name': 'Thomas Eddisson'}
print(addPerson(newPerson))

print(getPerson(2))

newName = {'name': 'James Essien'}
print(updPerson(3, newName))

print(delPerson(4))
