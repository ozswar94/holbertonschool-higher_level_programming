#!/usr/bin/python3
""" script GET a webpag with requests lib """
import requests


if __name__ == '__main__':
    rep = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(rep.text))
    print('\t- content:', rep.text)
