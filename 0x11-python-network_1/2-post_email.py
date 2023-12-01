#!/usr/bin/python3
"""
Script that sends a "POST" request to the passed URL with the email
as a parameter, and displays the body of the response (decoded in utf-8).
"""

from urllib.request import urlopen
from sys import argv
from urllib import parse

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = parse.urlencode({'email': email}).encode('utf-8')
    with urlopen(url, data) as response:
        readurl = response.read().decode('utf-8')
        print(readurl)
