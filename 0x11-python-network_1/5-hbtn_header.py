#!/usr/bin/python3

"""
- takes in a URL
- sends a request to the URL
- displays the value of the variable
- X-Request-Id in the response header
"""

import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
