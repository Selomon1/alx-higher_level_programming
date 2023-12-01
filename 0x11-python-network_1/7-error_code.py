#!/usr/bin/python3
"""
Script that sends requests and display response
if HTTP greater and eaqual t0 400 to print Error Code:
"""


import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    if response.HTTP_status >= 400:
        print(f"Error code: {response.HTTP_status}")
