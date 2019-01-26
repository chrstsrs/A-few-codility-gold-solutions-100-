# Problem Description:
# https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
# Calculate the values of counters after applying all alternating operations:
# increase counter by 1; set value of all counters to current maximum.
# -------------------------------------------------------------
# O(N+M)


import random
from timeit import Timer
from collections import deque


def solution(N, A):
    dA = deque(A)
    maximum = 0
    Nmap = [0] * N
    state_maximum = 0
    while dA:
        operation = dA.popleft() - 1
        try:
            Nmap[operation] = Nmap[operation] + \
                1 if Nmap[operation] > state_maximum else state_maximum + 1
            maximum = Nmap[operation] if Nmap[operation] > maximum else maximum
        except IndexError:
            state_maximum = maximum
    Nmap = list(map(lambda x: x if x > state_maximum else state_maximum, Nmap))
    return Nmap


N = 100000
L = [3, 4, 4, 6, 1, 4, 4]
test_solution1 = solution(N, [2, 2, 2]+[100001] * N)
obj1 = Timer("test_solution1", 'from __main__ import test_solution1')
print(obj1.repeat(repeat=6, number=10))
