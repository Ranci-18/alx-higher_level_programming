#!/usr/bin/python3
"""Python script that takes your Github credentials (username and password)
and uses the Github API to display your id"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    data = response.json()
    github_id = data.get("id")
    print(github_id)
