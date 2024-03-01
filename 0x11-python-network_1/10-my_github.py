#!/usr/bin/python3
"""
    a Python script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""
import requests
import sys

user = sys.argv[1]
passwd = sys.argv[2]
url = "https://api.github.com/user"

response = requests.get(url, auth=(user, passwd))

user_data = response.json()
user_id = user_data["id"]
print(f"{user_id}")
