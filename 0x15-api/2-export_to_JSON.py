#!/usr/bin/python3
"""
This script exports data in the CSV format
"""
import json
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    response = requests.get(url)
    user_name = response.json().get("username")
    todo_url = url + "/todos"
    response = requests.get(todo_url)
    todos = response.json()
    todo_list = {emp_id: []}
    for todo in todos:
        todo_list[emp_id].append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user_name
        })
    with open("{}.json".format(emp_id), "w") as f:
        json.dump(todo_list, f)
