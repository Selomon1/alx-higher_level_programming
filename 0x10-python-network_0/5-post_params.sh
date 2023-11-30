#!/bin/bash
# Script that sends a POST request to the passed URL
curl -X POST -H email=test@gmail.com -d subject="I will always be here for PLD" $1
