"""
A file for executing math functions
"""
from typing import Union
import numpy as np

def euler(n=10):

    if n < 0:
        raise ValueError("Only positive integers are allowed")
    factorial = 1
    result = 1
    for x in range(1, n + 1):
        factorial *= x
        result += 1. / factorial

    return result


def pi(n=10000):

    r_pts = np.random.rand(n, 2)
    norms = np.linalg.norm(r_pts, axis=1)
    in_circ = norms < 1
    return 4. * np.mean(in_circ)

