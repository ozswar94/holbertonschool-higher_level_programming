#!/usr/bin/python3
""" POST with requests lib """
import sys
import requests


if __name__ == "__main__":
    rep = requests.post(sys.argv[1], data={email: sys.argv[2]})
    print(rep.text)
