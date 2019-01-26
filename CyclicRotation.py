# Problem Description:
# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
# Rotate an array to the right by a given number of steps.
# -----------------------------------------------------------------


import random
from timeit import Timer


def solution(A, K):
    try:
        K = K % len(A)
        return A[-K:].extend(A[:-K])
    except ZeroDivisionError:
        return []


N = 10000

L = [i for i in range(N)]
test_solution1 = solution(L, 13)
obj1 = Timer("test_solution1", 'from __main__ import test_solution1')
print(obj1.repeat(repeat=60, number=10))
