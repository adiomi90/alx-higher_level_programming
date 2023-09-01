#!/usr/bin/python3
""" Fetch content from https://alx-intranet.hbtn.io/status """

from urllib.request import urlopen, Request


def make_request():
    req = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(req) as response:
        content = response.read()

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode('utf-8')}")


if __name__ == '__main__':
    make_request()
