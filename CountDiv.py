# Problem Description:
# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/
# Compute number of integers divisible by k in range [a..b].
# ---------------------------------------
# In (A, B] there are B//K - A // K solutions.
# If we want to consider A as well, we have to examine if A is divided by K.
# In this case we have to consider one more solution.
# Complexity O(1)

import random
from timeit import Timer


def solution(A, B, K):
    if A % K:
        return B//K - A//K
    else:
        return B//K - A//K + 1


test_solution1 = solution(6, 14, 2)
print(test_solution1)
obj1 = Timer("test_solution1", 'from __main__ import test_solution1')
print(obj1.repeat(repeat=6, number=10))
