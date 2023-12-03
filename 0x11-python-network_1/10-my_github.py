#!/usr/bin/python3
"""
Script that takes your Github credentials (username and password) and
uses the GitHub API to display your id.
(only read: user permission is needed)
"""


import requests
from sys import argv

if __name__ == "__main__":
    url = f"https://api.github.com/user"
    username = argv[1]
    password = argv[2]
    auth = (argv[1], argv[2])

    response = requests.get(url, auth=auth)
    print(response.json().get('id'))  
