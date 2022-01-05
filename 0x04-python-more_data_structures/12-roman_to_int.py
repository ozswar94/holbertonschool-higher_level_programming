#!/usr/bin/python3
def roman_to_int(roman_string):
    r_number = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    number = 0
    for c in roman_string:
         number += r_number[c]
    return number
