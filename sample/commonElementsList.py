#!/usr/bin/env python
# returning the most common elements in a two lists


def comm_elements(a, b):
    return set(a) & set(b)


a = ['1', '2', '3', '4', '5']
b = ['2', '3', '5', '6']

print(comm_elements(a, b))