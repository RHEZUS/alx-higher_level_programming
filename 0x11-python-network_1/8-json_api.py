#!/usr/bin/python3

"""
- takes in a letter
- sends a POST request to http://0.0.0.0:5000/search_user
 with the letter as a parameter.
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
