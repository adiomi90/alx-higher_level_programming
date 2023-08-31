#!/bin/bash
#this script takes in a rul, and displace the body size

curl -sI "$1 | greo Content-Length | cut -d ' ' -f 2
