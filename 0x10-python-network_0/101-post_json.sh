#!/bin/bash
#Sends a request to a URL passed as an argument, displays only the status code
curl -sL -H "content-type:application/json"  -d @"$2" -X POST "$1"
