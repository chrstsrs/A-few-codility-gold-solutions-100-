# Problem Description:
# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
# Find the smallest positive integer that does not occur in a given sequence.
# ---------------------------------------------------------


import random
from timeit import Timer


def solution(A):
    Aset = set(A)
    N = len(Aset)
    for i in range(1, N+2):
        if i not in Aset:
            return i


N = 100000
test_solution1 = solution([i for i in range(1, N)])
print(test_solution1)
obj1 = Timer("test_solution1", 'from __main__ import test_solution1')
print(obj1.repeat(repeat=6, number=10))
