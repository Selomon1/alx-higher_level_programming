#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
using urllib package with the specif format
"""

from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(Request(url)) as response:
        print("Body response:")
        print("\t- type:", type(response.read()))
        print("\t- content:", response.read())
        print("\t- utf8 content:", response.read().decode('utf8'))
