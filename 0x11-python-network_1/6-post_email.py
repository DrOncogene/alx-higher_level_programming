#!/usr/bin/python3
"""posts an email to a server"""
import sys
import requests


def post_email(url: str, email: str):
    """posts an email"""
    data = {'email': email}
    resp = requests.post(url, data={'email': email})
    print(resp.text)


if __name__ == "__main__":
    post_email(sys.argv[1], sys.argv[2])
