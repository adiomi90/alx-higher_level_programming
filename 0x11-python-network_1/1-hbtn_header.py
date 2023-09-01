#!/usr/bin/python3
"""
This  script take a URL, sends a request and displays
the value of the X-Request-Id variable
"""
import urllib.request
import sys



if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
