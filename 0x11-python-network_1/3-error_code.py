#!/usr/bin/python3
"""sends a request and handles the error"""
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError


def error_code(url: str):
    """prints the error code following a request"""
    req = Request(url)
    try:
        with urlopen(req) as f:
            pass
    except HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    error_code(sys.argv[1])
