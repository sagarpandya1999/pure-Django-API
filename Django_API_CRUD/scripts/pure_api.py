import requests
import json


BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "rest/api/"


# for retrieve
def get_data(id=None):
    data = json.dumps({})
    if id is not None:
        data = json.dumps({'pk':id})
    r = requests.get(BASE_URL + ENDPOINT, data=data)
    data = r.json()
    print(r.headers)
    print(data)

get_data()

# for create
def create_update():
    new_data = {
        'user':1,
        'content':"another cool pot that you would like!!",
    }
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.status_code)
    print(r.headers)
    if r.status_code == requests.codes.ok:
        print(r.json())
    print(r.text)

# create_update()

# for update
def do_obj_update():
    new_data = {
        'pk':1,
        'content':"another cool new update",
    }
    r = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    # new_data = {
    #     'id': 1,
    #     'content': "another cool pot that you would like!!",
    # }
    # r2 = requests.put(BASE_URL + ENDPOINT, data=new_data)

    print(r.status_code)
    # print(r.headers)
    if r.status_code == requests.codes.ok:
        print(r.json())
    print(r.text)

# do_obj_update()

#for delete
def do_obj_delete():
    new_data = {
        'pk':8
    }
    r = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(new_data))

    # new_data = {
    #     'id': 1,
    #     'content': "another cool pot that you would like!!",
    # }
    # r2 = requests.put(BASE_URL + ENDPOINT, data=new_data)

    print(r.status_code)
    # print(r.headers)
    if r.status_code == requests.codes.ok:
        print(r.json())
    print(r.text)

# do_obj_delete()