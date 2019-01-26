# Problem Description:
# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
# Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.
# -------------------------------------------------------------
# There is no reason to start with an empty set. This increases even more the
# efficiency.

import random
from timeit import Timer


def solution(A):
    N = len(A)
    s1 = A[0]
    s2 = sum(A[1:])
    P = 1
    diff = abs(s1 - s2)
    for i in range(2, N):
        s1 += A[i-1]
        s2 -= A[i-1]
        diff_new = abs(s1 - s2)
        if diff_new < diff:
            diff = diff_new
            P = i
    return diff


N = 100000
L = [random.randint(-1000, 1000) for _ in range(2, N)]
print(L)

test_solution = solution(L)
print(test_solution)
obj = Timer("test_solution", 'from __main__ import test_solution')
print(obj.repeat(repeat=6, number=10))
