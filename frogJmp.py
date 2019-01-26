# Problem Description:
# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
# Count minimal number of jumps from position X to Y.
# ------------------------------------------------------------------

import random
from timeit import Timer


def solution(X, Y, D):
    if (Y - X) % D:
        return (Y - X) // D + 1
    else:
        return (Y - X) // D


test_solution1 = solution(10, 20, 9)
print(test_solution1)
obj1 = Timer("test_solution1", 'from __main__ import test_solution1')
print(obj1.repeat(repeat=60, number=10))
