#!/bin/bash
# Script that takes in a URL, sends a request to that URL, and display
# ... the size of the body of the response
curl -s $1 | wc -c
