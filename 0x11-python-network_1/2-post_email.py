#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response
"""
from urllib import request, parse
import sys

def make_request():
    email = {'email': sys.argv[2]}
    post = parse.urlencode(email)
    with_ascii = post.encode('ascii')
    request = request.Request(sys.argv[1], with_ascii)
    with request.urlopen(request) as response:
        body = response.read()
        print(body.decode('utf-8'))


if __name__ == "__main__":
    make_request()
