#!/usr/bin/python3
"""Module for make a request to an API"""
import json
import requests
import sys


if __name__ == "__main__":
    filename = sys.argv[1] + ".json"
    url = "https://jsonplaceholder.typicode.com/users/"
    employee_id = int(sys.argv[1])
    user_id_url = url + str(employee_id)
    request_user = requests.get(user_id_url)
    request_user_todo_list = requests.get(user_id_url + "/todos")
    user_json = json.loads(request_user.text)
    todos_json = json.loads(request_user_todo_list.text)
    employee_username = user_json.get('username', 'Not found')
    separator = ""
    with open(filename, mode='w', encoding='utf-8') as json_file:
        json_file.write("{")
        json_file.write('"{id}": ['.format(id=employee_id))
        for task in todos_json:
            if task.get('completed', '') is True:
                task_status = "true"
            else:
                task_status = "false"
            result = (separator + '{"task": "' + task.get('title', '') +
                      '", "completed": ' + task_status + ', "username": "' +
                      employee_username + '"}')
            json_file.write(result)
            separator = ", "
        else:
            json_file.write(']}')
