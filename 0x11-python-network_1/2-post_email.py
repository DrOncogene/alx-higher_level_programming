#!/usr/bin/python3
"""posts an email to a server"""
import sys
import urllib.request
import urllib.parse


def post_email(url: str, email: str):
    """posts an email"""
    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as f:
        print(f.read().decode('utf-8'))


if __name__ == "__main__":
    post_email(sys.argv[1], sys.argv[2])
