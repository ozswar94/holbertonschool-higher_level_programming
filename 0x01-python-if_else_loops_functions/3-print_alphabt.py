#!/usr/bin/python3

for i in range(26):
    if ord('a') + i == ord('e'):
        i += 1
    elif ord('a') + i == ord('q'):
        i += 1
    else:
        print(chr(ord('a') + i), end='')
