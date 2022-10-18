#!/usr/bin/python3
"""returns to-do list of a person"""

import requests
from sys import argv


if __name__ == "__main__":
    if argv[1]:
        user_url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
        employe_name = requests.get(user_url)
        employee_name = employe_name.json().get("name")
        task_url = "https://jsonplaceholder.\
                typicode.com/todos?userId=" + argv[1]
        task = requests.get(task_url)
        tasks = task.json()
        task_done = 0
        lists = []
        for i in range(len(tasks)):
            if tasks[i]["completed"] is True:
                lists.append(tasks[i]["title"])
                task_done += 1

        print("Employee {} is done with tasks({}/{})".format((employee_name),
              str(task_done), str(20)))

        for z in range(len(lists)):
            print("\t{}".format(lists[z]))
