#!/usr/bin/python3
"""
Script that takes your Github credentials (username and password) and
uses the GitHub API to display your id.
(only read: user permission is needed)
"""


import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = argv[1]
    password = argv[2]
    response = requests.get(url, (username, password))
    if response.status_code == 200:
        user_id = response.json().get('id')
        print(user_id)
    else:
        print(None)

    
