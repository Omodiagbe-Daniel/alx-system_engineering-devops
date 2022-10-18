#!/usr/bin/python3
"""returns to-do list of a person"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    employe_name = requests.get(user_url)
    employee_name = employe_name.json().get("name")
    url = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    task = requests.get(url)
    tasks = task.json()
    task_done = 0
    lists = []
    for i in tasks:
        file = [argv[1], employee_name, i["completed"], i["title"]]
        lists.append(file)

    with open('{}.csv'.format(argv[1]), "w", newline="") as csvfile:
        for row in lists:
            print(row)
            my_writer = csv.writer(csvfile, delimiter=',')
            my_writer.writerow(row)
