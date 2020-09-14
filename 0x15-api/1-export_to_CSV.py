#!/usr/bin/python3
"""Module for make a request to an API"""
import json
import requests
import sys


if __name__ == "__main__":
    filename = sys.argv[1] + ".csv"
    url = "https://jsonplaceholder.typicode.com/users/"
    employee_id = int(sys.argv[1])
    user_id_url = url + str(employee_id)
    request_user = requests.get(user_id_url)
    request_user_todo_list = requests.get(user_id_url + "/todos")
    user_json = json.loads(request_user.text)
    todos_json = json.loads(request_user_todo_list.text)
    employee_username = user_json.get('username', 'Not found')
    with open(filename, mode='w', encoding='utf-8') as csv_file:
        for task in todos_json:
            csv_file.write('"{}","{}","{}","{}"\n'
                           .format(employee_id, employee_username,
                                   task.get('completed', ''),
                                   task.get('title', '')))
