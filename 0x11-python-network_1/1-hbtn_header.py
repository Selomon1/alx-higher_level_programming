#!/usr/bin/python3
"""
Script that sends a request to the URL and displays the value
of the "X-Request-Id" found in the header of the response
"""

from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with urlopen(url) as response:
        req_id = response.headers['X-Request-Id']
        print(f"{req_id}")
