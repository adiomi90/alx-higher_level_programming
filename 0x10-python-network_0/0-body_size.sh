#!/bin/bash
#this script takes url andshows the body size

curl -sI "$1" | grep Content-Length | cut -d ' ' -f 2
