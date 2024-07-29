#!/usr/bin/python3
'python script to get todo list progress'


import requests

"""
user - 1
todo - userid - 1 , id 1, id 2 - false/True

for the employee id  - all todos - true/total
display 

urls =https://jsonplaceholder.typicode.com/users/1/todos - all todos for a user 1

"""
if __name__=="__main__":
    import requests
    url = 'https://jsonplaceholder.typicode.com/users/1/todos'
    r = requests.get(url)
    completed = 0
    total = 0
    for item in r.json():
        if item.get('completed') == True:
            completed += 1
        total += 1
    print(completed, '/', total)
