# Problem Description:
# https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/
# Find the minimal average of any slice containing at least two elements.
# -------------------------------------------------------------------------
# It has been proved that the maximum slice can be 3. So, the test is only for 2
# or three arguments of the list
# ComplextiyO(N)

import random
from timeit import Timer


def solution(A):
    minimum = (A[0] + A[1])/2
    start_at = 0
    for idx, value in enumerate(A[:-1]):
        if (value+A[idx+1])/2 < minimum:
            minimum = (value+A[idx+1])/2
            start_at = idx
        try:
            if (value+A[idx+1]+A[idx+2])/3 < minimum:
                minimum = (value+A[idx+1]+A[idx+2])/3
                start_at = idx
        except IndexError:
            pass
    return start_at


test_solution1 = solution([random.randint(-10000, 10000) for _ in range(1000)])
print(test_solution1)
obj1 = Timer("test_solution1", 'from __main__ import test_solution1')
print(obj1.repeat(repeat=6, number=10))
