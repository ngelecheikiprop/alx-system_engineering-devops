#!/usr/bin/python3
'print as expected in task 0'

if __name__ == "__main__":
    import requests
    import sys
    user_id = sys.argv[1]
    url_todos = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    url_user = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    name = requests.get(url_user).json().get('name')
    r = requests.get(url_todos)
    completed = 0
    total = 0
    completed_titles = []
    for item in r.json():
        if item.get('completed') is True:
            completed += 1
            completed_titles.append(item.get('title'))
        total += 1
    print(f"Employee {name} is done with tasks({completed}/{total}):")
    for title in completed_titles:
        print(f"\t {title}")
