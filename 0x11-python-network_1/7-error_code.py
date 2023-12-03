#!/usr/bin/python3
"""
    A python scipt that uses the requests packaage
    sends a requewst to the URL and display body
    response
"""
from sys import argv
from requests import get, exceptions


def get_request(url):
    try:
        response = get(url)
        response.raise_for_status()
        return response
    except exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def main():
    url = argv[1]
    request = get_request(url)
    
    if request is None:
        print("Request failed")
        return

    if request.status_code >= 400:
        print(f"Error code: {request.status_code}")
    else:
        print(request.text)


if __name__ == "__main__":
    main()
