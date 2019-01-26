# Problem Description:
# https://app.codility.com/programmers/lessons/6-sorting/triangle/
# Determine whether a triangle can be built from a given set of edges.
# --------------------------------------------------------
# There must be a sequence of three numbers that solve the problem.
# It's a kind of sorting problem, but we do not need values ​​that are <= 0. Also,
# we will not sort the entire list, but we will stop the sorting process when
# the problem is resolved. The most appropriate algorithm is a selection sort.
# For this problem, the first step is to find the 2 maximum elements in the list
# and to alternate them with the last two elements in the table, while deleting
# all elements <= 0. Then we find the next maximum element and test it if it
# resolves problem. We repeat this step as long as there are elements in the
# array or the problem is resolved.
# There has to be found a sequence of three numbers that meet the problem.
#
# Complexity: O(N*log(N))

import random
from timeit import Timer


def solution(A):
    l = len(A)
    count_deleted_nodes = 0
    first_iteration = True
    for idx in range(l-1, -1, -1):
        if count_deleted_nodes != 0:
            count_deleted_nodes -= 1
            continue
        if A[idx] <= 0:
            del A[idx]
            l -= 1
            continue
        maximum1 = idx
        for imax in range(idx-1, -1, -1):
            if A[imax] < 0:
                del A[imax]
                l -= 1
                count_deleted_nodes += 1
                continue
            if A[imax] > A[maximum1-count_deleted_nodes]:
                maximum1 = imax+count_deleted_nodes
        A[idx-count_deleted_nodes], A[maximum1-count_deleted_nodes] = A[maximum1 -
                                                                        count_deleted_nodes], A[idx-count_deleted_nodes]
        if first_iteration:
            first_iteration = False
        else:
            break

    for idx in range(l-1, 1, -1):
        maximum1 = idx
        maximum2 = idx-1
        maximum3 = idx-2
        for imax in range(idx-3, -1, -1):
            if A[imax] > A[maximum3]:
                maximum3 = imax
        A[idx-2], A[maximum3] = A[maximum3], A[idx-2]
        if A[idx-2]+A[idx-1] > A[idx]:
            return 1
    return 0


'''
    l = len(A)
    count_deleted_nodes = 0
    for idx in range(l-1,-1,-1):
        if count_deleted_nodes != 0:
            count_deleted_nodes -= 1
            continue
        if A[idx] <= 0:
            del A[idx]
            continue
        maximum1 = A[idx]
        count_deleted_nodes = 0
        for imin in range(idx-1, -1, -1):
            if A[imin] <= 0:
                del A[imin]
                count_deleted_nodes += 1
                continue


    Apos = [x for x in A if x>0]
    sort(Apos)
    l = len(Apos)
    if Apos[0]*l < Apos[-1]:
        return 1
    else:
        first = Apos[0]
        second = Apos[1]
        for idx in Apos:
             if Apos[idx-2]+Apos[idx-1] < Apos[idx]:
                 return 1
    10, 10, 20, 20, 40, 40, 80, 80
    5,  5,  10, 10, 20, 20, 40, 40

'''
L = [-4, 2, 1, 77, 2, -3, -11, 55, 1, 21, -3, -2]  # [10, 50, 5, 1]  #
test_solution1 = solution(L)
print(test_solution1)
obj1 = Timer("test_solution1", 'from __main__ import test_solution1')
print(obj1.repeat(repeat=6, number=10))
