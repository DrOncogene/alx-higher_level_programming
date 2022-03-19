#!/usr/bin/python3
"""A script tha:
- takes in a letter
- sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests


def json_api(letter: str):
    """processes a json response"""
    res = requests.post("http://0.0.0.0:5000/search_user", data={'q': letter})
    try:
        res_dict = res.json()
        if len(res_dict) == 0:
            print("No result")
            return
        print(f"[{res_dict.get('id')}] {res_dict.get('name')}")
    except Exception:
        print("Not a valid JSON")


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    json_api(letter)
