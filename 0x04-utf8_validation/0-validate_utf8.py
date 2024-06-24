#!/usr/bin/python3
"""
A module that validate characters of UTF-8 encoding.
"""


def validUTF8(data):
    """
    A function that returns true if date is valid
    utf-8 encoding , else false.
    """
    count_byte_value = 0

    for i in data:
        if count_byte_value == 0:
            if i >> 5 == 0b1110 or i >> 5 == 0b110:
                count_byte_value = 1
            elif i >> 4 == 0b1110:
                count_byte_value = 2
            elif i >> 3 == 0b11110:
                count_byte_value = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            count_byte_value -= 1
    return count_byte_value == 0
