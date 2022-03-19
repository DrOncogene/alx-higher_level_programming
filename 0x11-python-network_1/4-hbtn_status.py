#!/usr/bin/python3
"""fetches data from a url using the request package"""
import requests


def get_status():
    """fetches a resource"""
    resp = requests.get("https://alx-intranet.hbtn.io/status")
    print('Body response:')
    print('\t- type: {}'.format(type(resp.text)))
    print('\t- content: {}'.format(resp.text))


if __name__ == "__main__":
    get_status()
