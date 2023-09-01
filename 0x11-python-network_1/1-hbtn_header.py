#!/usr/bin/python3
""" This script take in url and displays the value
    of X-Request_Id variable found in header
"""
import urllib.request
import sys

def make_request():
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))


if __name__ == '__main__':
    make_request()
