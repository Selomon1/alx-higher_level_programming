#!/bin/bash
# Script that sends a request to a URL passed as an argument, and display
# ... only the status code of the response.
# Not allowed to use any pipe, redirection, ; and &&

curl -s -I "$1" | grep -oP '(?<=HTTP\/1\.1 )\d{3}'
