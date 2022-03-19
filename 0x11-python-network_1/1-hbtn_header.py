#!/usr/bin/python3
"""fetches a url and prints and header value"""
import urllib.request
import sys


def get_header(url: str):
    """prints the X-Request-Id header from the response"""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as f:
        print(f.headers['X-Request-Id'])


if __name__ == '__main__':
    get_header(sys.argv[1])
