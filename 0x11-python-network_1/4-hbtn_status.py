#!/usr/bin/python3
"""
Script that fetch a given URL using the package "requests"
"""


import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
