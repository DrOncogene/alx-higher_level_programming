#!/usr/bin/python3
"""Script that
  - takes Github username and PAT
  - authenticates with github
  - prints user id
"""
import sys
import requests


if __name__ == "__main__":
    user, pat = sys.argv[1], sys.argv[2]
    res = requests.get(f"https://api.github.com/user", auth=(user, pat))
    print(res.json().get('id'))
