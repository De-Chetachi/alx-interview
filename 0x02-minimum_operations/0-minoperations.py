#!/usr/bin/python3
'''this module contains a function that finds
the minimum number of operations required to achieve a purpose'''
from math import sqrt


def is_prime(n):
    '''checks if a number n is prime
    param: n
    return: boolean, true if n is prime ese false'''
    if n <= 1:
        return False
    limit = int(sqrt(n)) + 1
    for i in range(2, limit):
        if not n % i:
            return False
    return True


def minOperations(n):
    '''
    returns the minimum number of operations required to achiev
    exactly n number of a in a file
    the only possible operations are copy all and paste
    paras: n
    return: minimum number of operations an integer'''
    if n <= 1:
        return 0

    primes = []
    if is_prime(n):
        primes.append(n)
        primes.append(1)
        return int(sum(primes))

    while 1:
        limit = int(sqrt(n)) + 1
        for i in range(2, limit):
            if is_prime(i) and n % i == 0:
                primes.append(i)
                break
        n = n / i
        if is_prime(n):
            primes.append(n)
            break
    return int(sum(primes))
