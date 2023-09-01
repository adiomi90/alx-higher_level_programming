#!/usr/bin/python3
"""
Python script that fetches an URL with requests package
"""
import requests


def make_request():
    the_request = requests.get('https://alx-intranet.hbtn.io/status')
    text = the_request.text

    print("Body response:")
    print(f"\t- type: {type(the_request)}")
    print(f"\t- content: {text}")


if __name__ == "__main__":
    make_request()
