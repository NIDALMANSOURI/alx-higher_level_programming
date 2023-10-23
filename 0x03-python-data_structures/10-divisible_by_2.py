#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_div = []
    for x in my_list:
        if x % 2 == 0:
            list_div.append(True)
        else:
            list_div.append(False)
    return list_div
