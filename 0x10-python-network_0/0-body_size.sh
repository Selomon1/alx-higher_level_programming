#!/bin/bash
# Script that takes in a URL, sends a request to that URL, and display
curl -s $1 | wc -c
