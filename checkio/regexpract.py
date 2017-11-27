#!/usr/bin/env python

from re import findall

out = """
interface ethernet {0}
\tswitchport access vlan {1}
"""

a = ['Et1', 'Et2', 'Et3', 'Et4', 'Et5', 'Et6']

for interface in a:
    int_num = findall(r'\D*(\d+)', interface).pop()
    print out.format(int_num, '500')