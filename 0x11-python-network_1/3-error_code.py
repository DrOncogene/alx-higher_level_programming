#!/usr/bin/python3
"""sends a request and handles the HTTPError"""
import sys
import urllib.request
import urllib.error


def error_code(url: str):
    """prints the error code following a request"""
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as f:
            print(f.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    error_code(sys.argv[1])
