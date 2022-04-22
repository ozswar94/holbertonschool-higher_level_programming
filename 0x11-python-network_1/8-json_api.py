#!/usr/bin/python3
""" Search API """
import sys
import requests


if __name__ == '__main__':
    rep = requests.post('http://0.0.0.0:5000/search_user',
                        data={'q': sys.argv[1]})
    rep = rep.json()
    for key, value in rep.items():
        print('[{}] {}'.format(key, value))
