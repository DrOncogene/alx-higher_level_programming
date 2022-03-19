#!/usr/bin/python3
"""fetches data from a url using urllib"""
import urllib.request


def get_status():
    """fetches a resource"""
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as f:
        resp = f.read()
        print('Body response:')
        print('\t- type: {}'.format(type(resp)))
        print('\t- content: {}'.format(resp))
        print('\t- utf8 content: {}'.format(resp.decode('utf-8')))


if __name__ == "__main__":
    get_status()
