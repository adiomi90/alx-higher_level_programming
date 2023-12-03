#!/usr/bin/python3
"""
python script that takes in a URL, sends a request and
displays the vlaue of the X-Request-id variable found in the header
"""
from urllib.request import urlopen, Request
import sys


def get_x_request_id(url):
    try:
        request = Request(url)
        with urlopen(request) as response:
            html = response.info()
            return html.get("X-Request-Id")
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    x_request_id = get_x_request_id(sys.argv[1])

    if x_request_id is not None:
        print(x_request_id)


if __name__ == "__main__":
    main()
