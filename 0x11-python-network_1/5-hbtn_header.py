#!/usr/bin/python3
"""
Python script that sends a request to the URL and
displays the value of a variable in the response header
"""
import requests
import sys


def make_request():
    try:
        req = requests.get(sys.argv[1])
        print(req.headers['X-Request-Id'])
    except:
        pass


if __name__ == "__main__":
    make_request()
