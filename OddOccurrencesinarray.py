# Problem Description:
# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
# Find value that occurs in odd number of elements.
# ---------------------------------------------------------
# Using the collections module for better performance.
# Improved performance by far...


import random
from timeit import Timer
from collections import Counter


def solution(A):
    A_dict = Counter(A).most_common()
    unpair = [v for (v, rep) in A_dict if rep % 2][0]
    return unpair


N = 1000000

L = [i for i in range(N)]
L.append(-5)
L.extend([i for i in range(N)])
test_solution1 = solution(L)
obj1 = Timer("test_solution1", 'from __main__ import test_solution1')
print(obj1.repeat(repeat=6, number=10))
