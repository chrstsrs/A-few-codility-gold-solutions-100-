# Proplem Description: https://app.codility.com/programmers/lessons/1-iterations/
# ----------------------------------------------------------------
# This solution has O(N) complexity

import random
from timeit import Timer


def binary_gap(N):
    counter = 0
    max_counter = -1
    while(N):
        counter = 0 if N % 2 else counter + 1
        if N % 2:
            if max_counter == -1:
                max_counter = 0
            elif counter > max_counter:
                max_counter = counter
        N //= 2
    return max_counter


N = 1000000

test_solution = [binary_gap(i) for i in range(N)]
obj = Timer("test_solution", 'from __main__ import test_solution')
print(obj.repeat(repeat=6, number=10))
