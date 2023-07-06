#!/usr/bin/python3
"""A Python script to export data in the CSV format"""

import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_info = requests.get(url).json()
    todo_info = requests.get(todo_url).json()

    employee_name = user_info.get("name")
    employee_username = user_info.get("username")
    total_tasks = [task for task in todo_info if task["completed"]]
    task_com = len(total_tasks)
    total_task_done = len(todo_info)

    with open(f"{employee_id}.csv", "w") as f:
        for task in todo_info:
            f.write(
                f'"{employee_id}",'
                f'"{employee_username}",'
                f'"{str(task["completed"])}",'
                f'"{task["title"]}",'
                "\n"
            )

