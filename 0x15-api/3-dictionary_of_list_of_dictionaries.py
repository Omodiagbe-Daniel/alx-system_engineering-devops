#!/usr/bin/python3
"""returns to-do list of a person"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users/"
    employe_name = requests.get(user_url)
    employee_name = employe_name.json()
    url = "https://jsonplaceholder.typicode.com/todos"
    task = requests.get(url)
    tasks = task.json()
    lists = []
    list1 = []
    for user_id in tasks:
        lists.append(user_id["userId"])
    list_set = set(lists)
    list1 = list(list_set)
    list1.sort()
    user_name = []
    for name in range(len(employee_name)):
        user_name.append(employee_name[name].get("username"))
    task_dict = {}
    count = 1
    for i in user_name:
        task_file = []
        for j in tasks:
            if j["userId"] == count:
                file_dict = ({"username": i, "task": j["title"],
                             "completed": j["completed"]})
                task_file.append(file_dict)
        task_dict[count] = task_file
        count += 1

    with open("todo_all_employees.json", "w", newline="") as jsonfile:
        json.dump(task_dict, jsonfile)
