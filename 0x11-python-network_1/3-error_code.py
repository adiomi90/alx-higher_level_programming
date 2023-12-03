#!/usr/bin/python3
"""
    The script take a URL, send request and displays
    response handling the errors
"""

import sys
from urllib.request import urlopen, Request
from urllib.error import HTTPError


def get_url_request(url):
    try:
        request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(request) as response:
            content = response.read().decode("utf-8")
        return content

    except HTTPError as e:
        return (f"Error code: {e.code}")


def main():
    url = sys.argv[1]
    print(get_url_request(url))


if __name__ == "__main__":
    main()
