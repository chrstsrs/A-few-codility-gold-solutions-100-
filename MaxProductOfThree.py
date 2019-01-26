# Problem Description:
# https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/
# Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).
# ----------------------------------------------------
# The maximum value can be generated from 3 positive numbers or from 2 negative
# and the highest positive number. We can find these 5 total prices in a single
# pass, but this is a more styled solution.
# Determined time complexity O(N * log(N))

import random
from timeit import Timer


def solution(A):
    max_list = []
    for _ in range(3):
        maximum = max(A)
        max_list.append(maximum)
        A.remove(maximum)

    A.extend(max_list)
    min_list = []
    for _ in range(2):
        minimum = min(A)
        min_list.append(minimum)
        A.remove(minimum)
    return max(max_list[0] * max_list[1] * max_list[2], max_list[0] * min_list[0] * min_list[1])


N = 100000
test_solution = solution([random.randint(-1000, 1000) for i in range(N)])
print(test_solution)
obj1 = Timer("test_solution", 'from __main__ import test_solution')
print(obj1.repeat(repeat=6, number=10))
