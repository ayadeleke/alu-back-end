#!/usr/bin/python3
"""
    Python script that returns TODO list progress for a given employee ID
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    # Functions for gathering data from an API
    employee_id = argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'
    request_employee = requests.get(f'{base_url}/users/{employee_id}')
    employee = json.loads(request_employee.text)
    employee_name = employee.get("name")

    request_todos = requests.get(f'{base_url}/todos?userId={employee_id}')
    employee_todos = json.loads(request_todos.text)

    tasks = {}
    for dictionary in employee_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    TOTAL_NUMBER_OF_TASKS = len(tasks)
    NUMBER_OF_DONE_TASKS = len([k for k, v in tasks.items() if v is True])

    print(f"Employee {employee_name} is done with tasks ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for k, v in tasks.items():
        if v is True:
            print("\t{}".format(k))
