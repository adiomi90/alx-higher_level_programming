#!/bin/bash
# This script take in a URL and display ll methods accpeted
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
