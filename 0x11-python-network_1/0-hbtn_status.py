#!/usr/bin/bash
"""script that fetches from the url https://alx-intranet.hbtn.io/status"""
from urllib.request import urlopen, Request


def main():

    request = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(request) as response:
        content = response.read()

        if content:
            print("Body response:")
            print(f"\t- type: {type(content)}")
            print(f"\t- content: {content}")
            print(f"\t- utf8 content: {content.decode('utf-8')}")


if __name__ == '__main__':
    main()

