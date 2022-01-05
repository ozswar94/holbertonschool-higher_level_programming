#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return None
    result = 0
    quotient = 0
    for i in my_list:
        result += i[0] * i[1]
        quotient += i[1]
    return result / quotient
