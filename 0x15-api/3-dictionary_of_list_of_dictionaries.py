#!/usr/bin/python3
'get the tasks of all employees'

if __name__=="__main__":
    import requests
    import json
    employees_tasks = {}
    url_users = 'https://jsonplaceholder.typicode.com/users'
    r = requests.get(url_users)
    users = r.json()
    for user in users:
        user_id = user.get('id')
        url_user = f'https://jsonplaceholder.typicode.com/users/{user_id}'
        user_name = requests.get(url_user).json().get('username')
        url_todos = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
        r = requests.get(url_todos)
        user_tasks = []
        for item in r.json():
            task_dict = {
                "username": user_name,
                "task": item.get('title'),
                "completed": item.get('completed')
            }
            user_tasks.append(task_dict)
        employees_tasks.update({user_id: user_tasks})
    with open('todo_all_employees.json', 'w', encoding='utf-8') as file:
        json.dump(employees_tasks, file)
