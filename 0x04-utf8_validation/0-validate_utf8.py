#!/usr/bin/python3
"""
A function that checks if a given data set
utf-8 valid
"""


def validUTF8(data):
    """
    function to validate utf-8 encoding
    """
    validutf8 = 0
    for val in data:
        byte = val & 255
        if validutf8:
            if byte >> 6 != 2:
                return False
            validutf8 -= 1
            continue
        while (1 << abs(7 - validutf8)) & byte:
            validutf8 += 1
        if validutf8 == 1 or validutf8 > 4:
            return False
        validutf8 = max(validutf8 - 1, 0)
    return validutf8 == 0
