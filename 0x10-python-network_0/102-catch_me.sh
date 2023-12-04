#!/bin/bash
# Sending a POST request with a 0.0.0.0:5000/catch_me  that
# ...tirigger the server respnse
curl -sL -X PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
