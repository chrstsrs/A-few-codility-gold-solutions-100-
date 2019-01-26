# Problem Description:
# https://app.codility.com/programmers/lessons/6-sorting/distinct/
# Compute number of distinct values in an array.
# -------------------------------------------------------------------
# Time complexity O(N*log(N)) or O(N)

from collections import Counter
import random
from timeit import Timer


def solution(A):
    return len(Counter(A))


N = 100000
test_solution = solution([random.randint(-1000000, 1000000) for i in range(N)])
print(test_solution)
obj1 = Timer("test_solution", 'from __main__ import test_solution')
print(obj1.repeat(repeat=6, number=10))
