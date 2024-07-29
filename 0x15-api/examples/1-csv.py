#!/usr/bin/python3
'print as expected in task 0'

if __name__=="__main__":
    import requests
    import sys
    import csv
    user_id = sys.argv[1]
    url_todos = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    url_user = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    name = requests.get(url_user).json().get('username')
    r = requests.get(url_todos)
    completed = 0
    total = 0
    completed_titles = []
    rows = []
    for item in r.json():
        row = ["2", name, item.get('completed'), item.get('title')]
        rows.append(row)
    with open('USER_ID.csv', 'w', newline='') as file:
        writer  = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(rows)
