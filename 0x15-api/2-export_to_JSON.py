#!/usr/bin/python3
'print as expected in task 0'

if __name__ == "__main__":
    import requests
    import sys
    import json
    user_id = sys.argv[1]
    url_todos = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    url_user = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    name = requests.get(url_user).json().get('username')
    r = requests.get(url_todos)
    user_tasks = []
    for item in r.json():
        mydict = {
            "task": item.get('title'),
            "completed": item.get('completed'),
            "username": name}
        user_tasks.append(mydict)
    user_data = {user_id: user_tasks}
    with open(f'{user_id}.json', 'w', encoding='utf-8') as file:
        json.dump(user_data, file)
