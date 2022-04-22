#!/usr/bin/python3
""" get a request of websever with lib """
import sys
import requests


if __name__ == "__main__":
    rep = requests.get('https://intranet.hbtn.io/status')
    print(rep.headers.get('X-Request-Id'))
