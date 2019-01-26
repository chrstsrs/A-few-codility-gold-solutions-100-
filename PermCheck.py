# Problem Description:
# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
# Check whether array A is a permutation.
# ----------------------------------------------------
# The simple is always the better and mor efficient.

import random
from timeit import Timer


# better performance
def solution(A):
    s = set(A)
    N = len(s)
    return 1 if len(A) == N == max(s) and min(s) == 1 else 0


test_solution1 = solution([i for i in range(1, 1000000)])
print(test_solution1)
obj1 = Timer("test_solution1", 'from __main__ import test_solution1')
print(obj1.repeat(repeat=6, number=10))
