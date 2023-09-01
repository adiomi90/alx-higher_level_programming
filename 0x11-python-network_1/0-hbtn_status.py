#!/usr/bin/python3
""" This script fetches https://alx-intranet.hbtn.io/status """

from urllib.request import urlopen, Request

request = Request('https://alx-intranet.hbtn.io/status')
with urlopn(request) as response:
    content = response.read()
print("Body response:")
print(f"\t- type: {type(content)}")
print(f"\t- content: {content}")
print(f"\t- utfs content: {content.decode('utf-8')}")
