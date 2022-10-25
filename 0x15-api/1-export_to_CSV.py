#!/usr/bin/python3
"""returns to-do list of a person"""

import csv
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
        file = [argv[1], employee_name, i["completed"], i["title"]]
        lists.append(file)

    with open('{}.csv'.format(id), "w", newline="") as csvfile:
        for row in lists:
            my_writer = csv.writer(csvfile,
                                   quoting=csv.QUOTE_ALL, delimiter=',')
            my_writer.writerow(row)
