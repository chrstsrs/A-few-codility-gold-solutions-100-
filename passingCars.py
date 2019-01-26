# Problem Description:
# https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/
# Count the number of passing cars on the road.
# -----------------------------------------------------------------
# It is more efficient to start counting from the end. Each time we find a car
# moving to west we just increase them. Every car that is moving to east, is
# going to meet pass all the moving to west up to now.
# Complexity is O(N) (worst case)

import random
from timeit import Timer


def solution(A):
    total_west = 0
    passing_cars = 0
    for i in reversed(A):
        if i:
            total_west += 1
        else:
            passing_cars += total_west
            if passing_cars > 1000000000:
                return -1
    return passing_cars


test_solution1 = solution([random.randint(0, 1) for i in range(100000)])
print(test_solution1)
obj1 = Timer("test_solution1", 'from __main__ import test_solution1')
print(obj1.repeat(repeat=6, number=10))
