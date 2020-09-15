#!/usr/bin/python3
"""Module for make a request to an API"""
import json
import requests
import sys


if __name__ == "__main__":
    filename = "todo_all_employees.json"
    url = "https://jsonplaceholder.typicode.com/users"
    request_users = requests.get(url)
    user_json = json.loads(request_users.text)
    separator = ""
    with open(filename, mode='w', encoding='utf-8') as json_file:
        json_file.write("{")
        for user in user_json:
            user_id = str(user.get('id'))
            user_id_str = '"{}": '.format(user_id)
            user_name = user.get('username', 'Not found')
            user_name_str = '"username": "{}"'.format(user_name)
            user_id_url = url + "/" + user_id
            request_user_todo_list = requests.get(user_id_url + "/todos")
            todos_json = json.loads(request_user_todo_list.text)
            json_file.write(separator + user_id_str + '[')
            content = ""
            sec_separator = ""
            for task in todos_json:
                task_value = task.get('title', '')
                if task.get('completed', '') is True:
                    task_status = "true"
                else:
                    task_status = "false"
                task_str = '"task": "{}", "completed": {}'.format(task_value,
                                                                  task_status)
                content += (sec_separator + '{' + user_name_str + ', ' +
                            task_str + '}')
                sec_separator = ", "
            json_file.write(content + ']')
            separator = ", "
        json_file.write('}')
