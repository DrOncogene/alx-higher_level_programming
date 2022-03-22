#!/usr/bin/python3
"""
Script that:
  - takes Github username and repo
  - list 10 commits by commit time
"""
import sys
import requests


if __name__ == "__main__":
    owner, repo = sys.argv[2], sys.argv[1]
    res = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")
    commits = res.json()

    for i in range(len(commits)):
        if i < 10:
            sha = commits[i].get('sha')
            author_name = commits[i].get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
