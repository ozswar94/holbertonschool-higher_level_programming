#!/usr/bin/python3

import urllib.request


if __name__ == '__main__':
    print('Body response:')
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        r = response.read()
        print('    - type: ', type(r))
        print('    - content', r)
        print('    - utf8 content:', r.decode('utf8'))