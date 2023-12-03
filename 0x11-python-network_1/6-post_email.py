#!/usr/bin/python3
"""
    A python script that takes in a URL,
    and email address sends a post request
    and displays the body using requests package
"""

from requests import post
from sys import argv


def post_request(url, data):
    try:
        response = post(url, data)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    url, email = argv[1], argv[2]
    data = {"email": email}
    post_result = post_request(url, data)
    if post_result is not None:
        print(post_result)


if __name__ == "__main__":
    main()
