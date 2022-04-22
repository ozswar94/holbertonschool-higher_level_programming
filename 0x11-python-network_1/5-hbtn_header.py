#!/usr/bin/python3
""" get a request of websever with lib """
import sys
import requests


if __name__ == "__main__":
    rep = requests.get(sys.argv[1])
    print(rep.headers.get('X-Request-Id'))
