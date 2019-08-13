"""
A file for executing math functions
"""

def euler(n=10):

    factorial = 1
    result = 1
    for x in range(1, n + 1):
        factorial *= x
        result += 1. / factorial

    return result
