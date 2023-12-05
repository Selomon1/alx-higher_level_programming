#!/bin/bash
# Script that sends a JSON POST request to a URL passed as first argument,
# ... and displays the body of the response
# must send a post request with the contents of a file, passed with the filename as second argument of the script
url=$1
file=$2
curl -s POST -H "Content-Type: application/json" -d "@$file" "$url"
