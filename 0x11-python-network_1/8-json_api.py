#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


import requests
from sys import argv

if __name__ == "__main__":
    letter = argv[1] if len(argv) > 1 else ""
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, {'q': letter})
    try:
        j_res = response.json()
        if j_res:
            print(f"[{j_res.get('id')}] {j_res.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
