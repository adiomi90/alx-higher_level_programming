#!/usr/bin/python3
"""
    A python script that sends a request
    to the url and sidplay the value of the variable
    X-Request-Id
"""
from requests import get, exceptions
from sys import argv


def get_x_request_id(url):
    try:
        response = get(url)
        response.raise_for_status()
        return response.headers.get("X-Request-Id")
    except exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def main():
    url = argv[1]
    x_request_id = get_x_request_id(url)
    if x_request_id is not None:
        print(x_request_id)


if __name__ == "__main__":
    main()
