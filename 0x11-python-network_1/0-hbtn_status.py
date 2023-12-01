#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
using urllib package with the specif format
"""

from urllib.request import Request, urlopen

if __name__ == "__main__":
    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        readurl = response.read()
        print("Body response:")
        print("\t- type:", type(readurl))
        print("\t- content:", readurl)
        print("\t- utf8 content:", readurl.decode('utf8'))
