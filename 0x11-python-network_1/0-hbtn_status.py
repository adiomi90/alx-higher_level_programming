#!/usr/bin/bash
"""script that fetches from the url https://alx-intranet.hbtn.io/status"""
from urllib.request import urlopen, Request
# headers={'User-Agent': 'Mozilla/5.0'}


def make_request(url):
    try:
        request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(request) as response:
            content = response.read()
        return content
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    content = make_request("https://alx-intranet.hbtn.io/status")

    if content:
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")


if __name__ == '__main__':
    main()

