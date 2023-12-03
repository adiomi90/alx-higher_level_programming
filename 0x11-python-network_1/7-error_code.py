#!/usr/bin/python3
"""
    A Python script that uses the requests package
    sends a request to the URL and displays the body response
"""
import sys
import requests

def main():
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()

        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
