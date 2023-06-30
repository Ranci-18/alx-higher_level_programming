#!/usr/bin/python3
"""Python script to list 10 commits from recent to oldest
of user rails and repo rails takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    response = requests.get(url)
    commits = response.json()
    for i in range(10):
        print("{}: {}".format(commits[i].get("sha"),
                              commits[i].get("commit").get("author").get("name")))
