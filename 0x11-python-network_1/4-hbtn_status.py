#!/usr/bin/python3
"""
    A python script that send requests
    and print the body response
"""

import requests


def main():
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")


if __name__ == "__main__":
    main()
