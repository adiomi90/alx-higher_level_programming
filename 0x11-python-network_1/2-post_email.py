#!/usr/bin/python3
"""
    The script takes a url and an email, sends a
    Post request with email as paramter and
    displays body response
"""

import sys
from urllib import parse
from urllib.request import Request, urlopen


def post_request_url(url, email):
    try:
        values = {"email": email}
        data = parse.urlencode(values).encode("ascii")
        request = Request(url, data, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(request) as response:
            content = response.read().decode("utf-8")
        return content

    except Exception as e:
        print(f"Error {e}")
        return None


def main():
    url = sys.argv[1]
    email = sys.argv[2]

    request = post_request_url(url, email)
    print(request)


if __name__ == "__main__":
    main()
