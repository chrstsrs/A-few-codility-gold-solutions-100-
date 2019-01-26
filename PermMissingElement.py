# Problem Description:
# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
# Find the missing element in a given permutation.
# ---------------------------------------------------------------
# An efficient algorithm
#

import random
from timeit import Timer


def solution(A):
    setA = set(A)
    for i in range(0, len(A)+2):
        if i not in setA:
            return(i)


test_solution1 = solution([i for i in range(1000000) if i != 500000])
print(test_solution1)
obj1 = Timer("test_solution1", 'from __main__ import test_solution1')
print(obj1.repeat(repeat=6, number=10))
