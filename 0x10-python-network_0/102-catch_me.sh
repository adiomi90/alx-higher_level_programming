#!/bin/bash
#Script that makes a request to 0.0.0.5000/catch me
curl -sL -X PUT -d "user_id=98" -H "origin: HolbertonSchool" 0.0.0.0:5000/catch_me
