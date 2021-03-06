#!/usr/bin/python3
"""
A Python script that fetches https://intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    try:
        response = requests.get('https://intranet.hbtn.io/status')
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
    except Exception as e:
        print(e)
