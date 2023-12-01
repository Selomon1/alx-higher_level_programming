#!/usr/bin/python3
"""
Script that sends a request to the URL and displays the value of
the variable X-Request-Id in the response
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
