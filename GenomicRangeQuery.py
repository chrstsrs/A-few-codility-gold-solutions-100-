# Problem Description:
# https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/
# Find the minimal nucleotide from a range of sequence DNA.
# ---------------------------------------------------------------
# A,C,G,T -> 1,2,3,4
# A memory list is implemented for A, C and G gens
# we don't need memory list for the T gen
# The memory lists contain the info of the next appearence of this gen
# ie the value of 4 in the memoryC means that the next appearence of the
# gen C is in 4th position. This value is repeated in any previous position.
# At the end of each memory list there are the values of -1 meaning that the
# specified gen does not appear anywhere after in the list.
# Complexity O(N+M)

import random
from timeit import Timer


def solution(S, P, Q):
    memoryA = []
    memoryC = []
    memoryG = []
    a_idx = -1
    c_idx = -1
    g_idx = -1
    for i, gen in enumerate(S):
        if gen == 'A':
            memoryA.extend([i]*(i - a_idx))
            a_idx = i
        elif gen == 'C':
            memoryC.extend([i]*(i - c_idx))
            c_idx = i
        elif gen == 'G':
            memoryG.extend([i]*(i - g_idx))
            g_idx = i

    l = len(S)
    memoryA.extend([-1]*(l-a_idx - 1))
    memoryC.extend([-1]*(l-c_idx - 1))
    memoryG.extend([-1]*(l-g_idx - 1))

    result = list()
    for idx, p in enumerate(P):
        if 0 <= memoryA[P[idx]] <= Q[idx]:
            result.append(1)
        elif 0 <= memoryC[P[idx]] <= Q[idx]:
            result.append(2)
        elif 0 <= memoryG[P[idx]] <= Q[idx]:
            result.append(3)
        else:
            result.append(4)
    return result


S = ''.join([['A', 'C', 'G', 'T'][random.randint(0, 3)] for _ in range(100000)])
P = [random.randint(0, 99999) for _ in range(10000)]
Q = [random.randint(P[i], min(99999, P[i]+5)) for i in range(10000)]

test_solution1 = solution(S, P, Q)
print(test_solution1)
obj1 = Timer("test_solution1", 'from __main__ import test_solution1')
print(obj1.repeat(repeat=6, number=10))
