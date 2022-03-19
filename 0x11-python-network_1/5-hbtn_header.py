#!/usr/bin/python3
"""fetches a url and prints and header value"""
import sys
import requests


def get_header(url: str):
    """prints the X-Request-Id header from the response"""
    resp = requests.get(url)
    print(resp.headers['X-Request-Id'])


if __name__ == '__main__':
    get_header(sys.argv[1])
