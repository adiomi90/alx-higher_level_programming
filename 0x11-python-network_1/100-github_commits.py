#!/usr/bin/python3
"""
Python script that shows the last 10 commits of a repository
in GitHub
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    headers = {
              'Accept': 'application/vnd.github.v3+json',
              }
    params = {
        'per_page': 10,
    }

    res = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
                      owner, repo_name),
                      headers=headers, params=params)
    json_res = res.json()
    for commit in json_res:
        print(commit['sha'] + ':', commit['commit']['author']['name'])
