import json
import requests
BASE_URL = 'http://127.0.0.1:8000/'

def get_all_resource():
    END_POINT = 'api/'
    resp = requests.get(BASE_URL+END_POINT)
    print(resp.json())

def get_resource_id():
    id = input('Enter the id :')
    END_POINT = 'id/'
    resp = requests.get(BASE_URL+END_POINT+str(id))
    print(resp.json())

def create_resource():
    END_POINT = 'update/'
    emp = {
        'eno' : 600,
        'ename' : 'Sonu',
        'esal' : 24000,
        'eaddr' : 'Hyderabad'
        }
    resp = requests.post(BASE_URL+END_POINT, data=json.dumps(emp))
    print(resp.json())

def update_resource():
    END_POINT = 'id/'
    id = int(input('Enter the id to update :'))
    emp = {
    'ename' : 'Sourav'
    }
    resp = requests.put(BASE_URL+END_POINT+str(id)+'/', data=json.dumps(emp))
    print(resp.json())

def delete_resource():
    END_POINT = 'id/'
    id = int(input('Enter the id to delete :'))
    resp = requests.delete(BASE_URL+END_POINT+str(id)+'/')
    print(resp.json())




print('*******************Client Application******************')
print('Menu____________________________')
print('1.Get All the Resource')
print('2.Get Resource by Id')
print('3.Create a Resource')
print('4.Update a Resource')
print('5.Delete a Resource')

choice = int(input('Enter the Choice :'))
if choice == 1 :
    get_all_resource()
elif choice == 2:
    get_resource_id()
elif choice == 3:
    create_resource()
elif choice == 4:
    update_resource()
else:
    delete_resource()
