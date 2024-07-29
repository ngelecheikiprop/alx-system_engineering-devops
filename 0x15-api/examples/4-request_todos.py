#!/usr/bin/python3
'get the employee name when given user id'
import requests


if __name__=="__main__":
    import requests
    import sys
    user_id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    r = requests.get(url)
    print(r.json().get('name'))
