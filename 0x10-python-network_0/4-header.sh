#!/bin/bash
# add a custom header to the url request
curl -s "$1" -H "X-School-User-Id: 98"
