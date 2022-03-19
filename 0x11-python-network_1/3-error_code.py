#!/usr/bin/python3
"""sends a request and handles the error"""
import sys
from urllib.request import Request, urlopen
from urllib.error import URLError


def error_code(url: str):
    """prints the error code following a request"""
    req = Request(url)
    try:
        resp = urlopen(req)
    except URLError as e:
        if hasattr(e, 'code'):
            print(f"Error code: {e.code}")
        else:
            pass


if __name__ == "__main__":
    error_code(sys.argv[1])
