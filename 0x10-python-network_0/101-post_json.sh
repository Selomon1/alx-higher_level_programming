#!/bin/bash
# Script that sends a JSON POST request to a URL passed as first argument,
# ... and displays the body of the response
# must send a post request with the contents of a file, passed with the filename as second argument of the script

curl -s -X POST -d @"$2" -H "Content-Type: application/json" "$1"
