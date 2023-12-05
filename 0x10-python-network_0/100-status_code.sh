#!/bin/bash
# Script that sends a request to a URL passed as an argument, and display
# ... only the status code of the response.
# Not allowed to use any pipe, redirection, ; and &&

curl -s -o /dev/null -w "%{http_code}" $1
