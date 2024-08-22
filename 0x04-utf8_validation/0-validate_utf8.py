#!/usr/bin/python3
""" UTF-8 Validation.
"""


def validUTF8(data):
    """ Determines if a given data set represents
     a valid UTF-8 encoding or not.
    """
    count = 0
    for dt in data:
        if count == 0:
            if dt & 128 == 0:
                count = 0
            elif dt & 224 == 192:
                count = 1
            elif dt & 240 == 224:
                count = 2
            elif dt & 248 == 240:
                count = 3
            else:
                return False
        else:
            if dt & 192 != 128:
                return False
            count -= 1
    if count == 0:
        return True
    return False
