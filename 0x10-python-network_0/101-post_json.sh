#!/bin/bash
# Script that sends a JSON POST request from the specified file and display
curl -s -X POST -d "@$2" -H "Content-Type: application/json" "$1"
