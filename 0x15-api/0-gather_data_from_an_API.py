#!/usr/bin/python3
"""
access to do list using REST API
"""
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    response = requests.get(url)
    name = response.json().get("name")
    todo_url = url + "/todos"
    response = requests.get(todo_url)
    todos = response.json()
    completed = 0
    done = []
    for todo in todos:
        if todo.get("completed") is True:
            done.append(todo)
            completed += 1
    print("Employee {} is done with tasks({}/{}):".format(
        name, completed, len(todos)))
    for todo in done:
        print("\t", todo.get("title"))
