#!/bin/bash
# Script that displays all HTTP methods the server will accept
curl -Is $1 | grep "Allow" | cut -d " " -f 2-
