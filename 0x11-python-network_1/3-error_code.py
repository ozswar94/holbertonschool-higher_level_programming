#!/usr/bin/python3
# manage error
import sys
from urllib import request, error


if __name__ == '__main__':
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code:", err.code)
