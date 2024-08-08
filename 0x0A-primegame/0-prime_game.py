#!/usr/bin/python3
""" Prime Game game!!!"""


def generatePrimeNumbers(limit):
    """get array of primes"""
    primeNumbers = []
    sieveList = [True] * (limit + 1)
    for potentialPrime in range(2, limit + 1):
        if sieveList[potentialPrime]:
            primeNumbers.append(potentialPrime)
            for multiple in range(potentialPrime, limit + 1, potentialPrime):
                sieveList[multiple] = False
    return primeNumbers


def isWinner(numRounds, roundValues):
    """check winner"""
    if not numRounds or not roundValues:
        return None
    mariaScore = benScore = 0
    for i in range(numRounds):
        primes = generatePrimeNumbers(roundValues[i])
        if len(primes) % 2 == 0:
            benScore += 1
        else:
            mariaScore += 1
    if mariaScore > benScore:
        return "Maria"
    elif benScore > mariaScore:
        return "Ben"
    return None
