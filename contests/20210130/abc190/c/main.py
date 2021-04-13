#!/usr/bin/env python3
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right  # type: ignore
from collections import Counter, defaultdict, deque  # type: ignore
from fractions import gcd  # type: ignore
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, merge  # type: ignore
from itertools import accumulate, combinations, permutations, product  # type: ignore

n = [int(_) for _ in input().split()]


M = n[1]

joken_list = [[int(_) for _ in input().split()] for _ in range(M)]

K = int(input())

humans = [[int(_) for _ in input().split()] for _ in range(K)]

l = product(*humans)


def f(p):
    sara_list = [False for _ in range(n[0])]

    for a in p:
        sara_list[a - 1] = True

    count = 0

    for joken in joken_list:
        joken_a = joken[0] - 1
        joken_b = joken[1] - 1

        if sara_list[joken_a] and sara_list[joken_b]:
            count += 1

    return count


max_num = -1
for pp in l:
    nn = f(pp)
    # print("a", pp, nn)
    max_num = nn if max_num < nn else max_num

print(max_num)
