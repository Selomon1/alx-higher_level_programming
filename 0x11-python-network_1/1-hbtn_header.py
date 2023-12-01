#!/usr/bin/python3
"""
Script that sends a request to the URL and displays the value
of the "X-Request-Id" found in the header of the response
"""

from urllib.request import urlopen, Request
from sys import argv

if __name__ == "__main__":
    with urlopen(Request(url)) as response:
