#!/usr/bin/python3
"""
This script exports data in the CSV format
"""
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
    with open("{}.csv".format(emp_id), "w") as f:
        for todo in todos:
            f.write('"{}","{}","{}","{}"\n'.format(
                emp_id, user_name, todo.get("completed"), todo.get("title")
            ))
