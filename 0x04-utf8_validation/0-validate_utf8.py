#!/usr/bin/python3
'''utf=8validatin'''


def sigbits(number: int):
    '''set how many significant bits are in a byte'''
    sigs = 0
    for i in range(7, 0, -1):
        if (number >> i) & 1:
            sigs = sigs + 1
        else:
            break
    return sigs


def validUTF8(data):
    '''valid utf8 or not'''
    index = 0
    while 1:
        if index >= len(data):
            break
        number = data[index]
        sig = sigbits(number)
        if sig > 4:
            return False
        if sig == 1:
            return False
        for j in range(index + 1, index + sig):
            try:
                if data[j] >> 6 != 2:
                    return False
            except IndexError:
                return False
        if sig:
            index += sig
        else:
            index += 1
    return True
