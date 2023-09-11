import requests
import json

url = 'https://gachenge.pythonanywhere.com'


def allPeople():
    people = f'{url}'
    response = requests.get(people)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"


def addPerson(data):
    add = f'{url}/api'
    headers = {'Content-type': 'application/json'}
    response = requests.post(add, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error {response.status_code}"


def getPerson(user_id):
    getp = f'{url}/api/{user_id}'
    headers = {'Content-type': 'application/json'}
    response = requests.get(getp, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error {response.status_code}"


def updPerson(user_id, data):
    upd = f'{url}/api/{user_id}'
    headers = {'Content-type': 'application/json'}
    response = requests.put(upd, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error {response.status_code}"


def delPerson(user_id):
    dele = f'{url}/api/{user_id}'
    headers = {'Content-type': 'application/json'}
    response = requests.delete(dele, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error {response.status_code}"


print(allPeople())

newPerson = {'name': 'James May'}
print(addPerson(newPerson))

print(getPerson(2))

newName = {'name': 'James Essien'}
print(updPerson(3, newName))

print(delPerson(4))
