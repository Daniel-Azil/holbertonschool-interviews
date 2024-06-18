#!/usr/bin/python3
"""A module that reads stdin line by line and computes metrics"""


import sys

dict_store = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
sz_len = 0
var = 0

try:
    for element in sys.stdin:
        var2 = element.split(" ")
        if len(var2) > 4:
            var3 = var2[-2]
            len = int(var2[-1])
            if var3 in dict_store.keys():
                dict_store[var3] += 1
            sz_len += len
            var += 1

        if var == 10:
            var = 0
            print('File len: {}'.format(sz_len))
            for dict_key, dict_value in sorted(dict_store.items()):
                if dict_value != 0:
                    print('{}: {}'.format(dict_key, dict_value))

except Exception as err:
    pass

finally:
    print('File len: {}'.format(sz_len))
    for dict_key, dict_value in sorted(dict_store.items()):
        if dict_value != 0:
            print('{}: {}'.format(dict_key, dict_value))
