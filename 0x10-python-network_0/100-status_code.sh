#!/bin/bash
# Script that sends request and extract only the status code
curl -s -o /dev/null -w "%{http_code}" $1
