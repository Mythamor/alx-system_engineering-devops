#!/usr/bin/python3
"""
Script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress
export data in the CSV format
"""

from csv import DictWriter, QUOTE_ALL
import json
import requests
from sys import argv

def write_to_csv(data, uid):
    """
    exports json data to csv
    """
    with open(f"{uid}.csv", "w") as file:
        headers = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",\
                "TASK_TITLE"]
        csv_writer = DictWriter(file, fieldnames=headers, quoting=QUOTE_ALL)
        for d in data:
            csv_writer.writerow(d)
    return


if __name__ == "__main__":

    uid = argv[1]

    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"https://jsonplaceholder.typicode.com/users/{uid}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={uid}"

    user_res = requests.get(user_url)
    user_info = user_res.json()
    user_name = user_info.get("username")

    todo_res = requests.get(todo_url)
    todo_data = todo_res.json()

    data = []

    for task in todo_data:
        users_info = {"USER_ID": uid,
                      "USERNAME": user_name,
                      "TASK_COMPLETED_STATUS": task.get("completed"),
                      "TASK_TITLE": task.get("title")}
        data.append(users_info)

    write_to_csv(data, uid)
