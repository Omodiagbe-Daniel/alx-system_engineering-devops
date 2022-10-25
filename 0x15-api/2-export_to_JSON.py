#!/usr/bin/python3
"""returns to-do list of a person"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    employe_name = requests.get(user_url)
    employee_name = employe_name.json().get("username")
    url = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    task = requests.get(url)
    tasks = task.json()
    id = tasks[0].get("userId")
    task_done = 0
    lists = []
    for i in tasks:
        file_dict = ({"tasks": i["title"], "completed":
                     i["completed"], "username": employee_name})
        lists.append(file_dict)
    json_dict = {id: lists}

    with open('{}.json'.format(id), "w", newline="") as jsonfile:
        json.dump(json_dict, jsonfile)
