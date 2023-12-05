#!/usr/bin/python3
"""
Script take repository and owner name to list 10 commits
"""

import requests
from sys import argv

if __name__ == "__main__":
    repository = argv[1]
    owner = argv[2]
    url = f'https://api.github.com/repos{owner}/{repository}/commits'
    response = requests.get(url, params={'per_page': 10})
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        pass
