#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID, returns"""

import json
import requests
import sys

BASE_URL = 'https://jsonplaceholder.typicode.com'

def get_user_info(user_id):
    user_url = f'{BASE_URL}/users/{user_id}'
    response = requests.get(user_url)
    response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
    return response.json()

def get_user_tasks(user_id):
    tasks_url = f'{BASE_URL}/todos?userId={user_id}'
    response = requests.get(tasks_url)
    response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
    return response.json()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    try:
        user_data = get_user_info(user_id)
        name = user_data['name']

        tasks_data = get_user_tasks(user_id)
        total_tasks = len(tasks_data)
        completed_tasks = [task for task in tasks_data if task['completed']]

        print(f"Employee {name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task['title']}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching data: {e}")
    except (KeyError, IndexError):
        print(f"User with ID {user_id} not found.")

