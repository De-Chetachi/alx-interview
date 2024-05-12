#!/usr/bin/python3
'''this module contains a function that checks the
utf-8 validity of a given encoding'''


def validUTF8(data):
    '''checks if a given encoding is valid utf-8
    params:
        data: a list of integers each integer represents one byte of data
    return
        true: if valid utf-8
        false: if not valid utf-8'''

    for byte in data:
        if byte >> 8:
            return False
    return True
