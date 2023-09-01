#!/usr/bin/python3
"""
Python script that fetches an URL with requests package
"""
import requests


def make_request():
    request = requests.get('https://alx-intranet.hbtn.io/status')
    text = request.text
    print("Body response:")
    print("\t- type: {request}")
    print("\t- content: {text}")


if __name__ == "__main__":
    make_request()
