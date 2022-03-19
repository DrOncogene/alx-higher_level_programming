#!/usr/bin/python3
"""
sends a post request and prints the response if it's a valid JSON
prints 'No result' or 'Not valid JSON' in some cases

args:
    letter(str): single letter
return:
    None
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
    try:
        json_api(sys.argv[1])
    except IndexError:
        json_api("")
