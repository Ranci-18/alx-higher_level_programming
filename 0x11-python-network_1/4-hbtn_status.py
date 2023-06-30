#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
using requests module"""
import requests


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)
    body = response.text
    print('Body response:')
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
