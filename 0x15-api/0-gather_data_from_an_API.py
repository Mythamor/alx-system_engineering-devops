#!/usr/bin/python3
"""
Script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    uid = argv[1]

    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"https://jsonplaceholder.typicode.com/users/{uid}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={uid}"

    user_res = requests.get(user_url)
    user_info = user_res.json()
    user_name = user_info["name"]

    todo_res = requests.get(todo_url)
    todo_data = todo_res.json()

    done_tasks = 0
    total_tasks = 0
    completed_tasks = []

    for task in todo_data:
        if task["completed"]:
            done_tasks += 1
            completed_tasks.append(task["title"])
        total_tasks += 1

    print(f"Employee {user_name} is done with tasks {done_tasks}\
/{total_tasks}")
    for title in completed_tasks:
        print(f"\t{title}")
