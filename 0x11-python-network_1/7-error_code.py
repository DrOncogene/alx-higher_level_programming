#!/usr/bin/python3
"""
sends a request and prints the status code if >= 400
"""
import sys
import requests


def print_error_code(url: str):
    """prints the error code following a request"""
    resp = requests.get(url)
    if resp.status_code >= 400:
        print(f"Error code: {resp.status_code}")
    else:
        print(resp.text)


if __name__ == "__main__":
    print_error_code(sys.argv[1])
