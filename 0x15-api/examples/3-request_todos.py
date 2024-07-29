#!/usr/bin/python3
'get the employee name'


import requests


if __name__=="__main__":
    import requests
    url = 'https://jsonplaceholder.typicode.com/users/1'
    r = requests.get(url)
    print(r.json().get('name'))
