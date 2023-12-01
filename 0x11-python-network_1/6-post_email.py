#!/usr/bin/python3
"""
Script that sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response using requests
and sys packages.
"""


import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
