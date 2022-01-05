#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_list = 0
    uniq_list = []
    for i in my_list:
        if i not in uniq_list:
            sum_list += i
            uniq_list.append(i)
    return sum_list
