#!/usr/bin/python3
"""
Script that sends a request to the URL and displays the
body of the response (decoded in utf-8).
Manage urllib.error.HTTPError exceptions and print: Error code:
    followed by the HTTP status code
"""


from urllib.request import urlopen
from sys import argv
from urllib import error

if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as response:
            readurl = response.read().decode('utf-8')
            print(readurl)
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
