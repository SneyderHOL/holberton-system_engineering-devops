#!/usr/bin/python3
"""Module for make a request to an API"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    employee_id = int(sys.argv[1])
    user_id_url = url + str(employee_id)
    request_user = requests.get(user_id_url)
    request_user_todo_list = requests.get(user_id_url + "/todos")
    user_json = json.loads(request_user.text)
    todos_json = json.loads(request_user_todo_list.text)
    employee_name = user_json.get('name', 'Not found')
    total_number_of_tasks = len(todos_json)
    tasks_completed = []
    for task in todos_json:
        if task['completed'] is True:
            tasks_completed.append(task.get('title', ''))
    number_of_done_tasks = len(tasks_completed)
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, number_of_done_tasks, total_number_of_tasks))
    for task in tasks_completed:
        print("\t " + task)
