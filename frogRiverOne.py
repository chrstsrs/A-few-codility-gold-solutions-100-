# Problem Description:
# https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
# Find the earliest time when a frog can jump to the other side of a river.
# -----------------------------------------------------------
# Using deque from collections and sets

import random
from timeit import Timer
from collections import deque


def solution(X, A):
    path = {i for i in range(1, X+1)} - set(A[:X])
    DA = deque(A[X:])
    i = X-1
    while path and DA:
        path.discard(DA.popleft())
        i += 1
    return -1 if path else i


test_solution1 = solution(2, [i for i in range(1, 10)])
print(test_solution1)
obj1 = Timer("test_solution1", 'from __main__ import test_solution1')
print(obj1.repeat(repeat=6, number=10))
