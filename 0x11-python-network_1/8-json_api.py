#!/usr/bin/python3
""" Search API """
import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) == 1:
        let = ""
    else:
        let = sys.argv[1]
    rep = requests.post('http://0.0.0.0:5000/search_user',
                        data={'q': let})
    rep = rep.json()
    if rep == {}:
        print("No result")
    else:
        print('[{}] {}'.format(rep.get('id'), rep.get('name')))
