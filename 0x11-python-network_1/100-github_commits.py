#!/usr/bin/python3
"""
Script take repository and owner name to list 10 commits
"""

import requests
from sys import argv

if __name__ == "__main__":
    repository = argv[1]
    owner = argv[2]
    url = f'https://api.github.com/repos/{owner}/{repository}/commits'
    response = requests.get(url, params={'page': 10})
    commits = response.json()
    try:
        for comm in commits:
            commit = comm['commit']
            sha = comm['sha']
            aut_name = commit['author']['name']
            print(f"{sha}: {aut_name}")
    except IndexError:
        pass
