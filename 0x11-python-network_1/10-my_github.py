#!/usr/bin/python3
""" My GitGub """
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    _auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    rep = requests.get('https://api.github.com/user', auth=_auth)
    print(rep.json().get("id"))
