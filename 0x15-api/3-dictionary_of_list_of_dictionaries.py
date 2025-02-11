#!/usr/bin/python3
"""
This script exports data in the in json format
"""
import json
import requests


data = {}
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()
    for user in users:
        userid = user.get("id")
        data[userid] = {}
        username = user.get("username")
        todos = f"https://jsonplaceholder.typicode.com/users/{userid}/todos"
        response = requests.get(todos)
        todos = response.json()
        task = []
        for todo in todos:
            task.append({
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            })
        data[userid] = ({
            "username": username,
            "tasks": task
        })
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
