#!/usr/bin/python3
""" Handel error with lib requests"""
import sys
import requests


if __name__ == "__main__":
    rep = requests.get(sys.argv[1])
    if rep.status_code >= 400:
        print('Error code:', rep.status_code)
    else:
        print(rep.text)
