#!/usr/bin/python3
""" POST email """
import sys
from urllib import request, parse


url = sys.argv[1]
email = sys.argv[2]

if __name__ == '__main__':
    value = {'email': email}
    value = parse.urlencode(value).encode('utf-8')
    req = request.Request(url, value)
    with request.urlopen(req) as reponse:
        print(reponse.read().decode('utf-8'))
