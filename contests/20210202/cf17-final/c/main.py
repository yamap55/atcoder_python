#!/usr/bin/env python3
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right  # type: ignore
from collections import Counter, defaultdict, deque  # type: ignore
from fractions import gcd  # type: ignore
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, merge  # type: ignore
from itertools import accumulate, combinations, permutations, product  # type: ignore

n = int(input())

N = [int(_) for _ in input().split()]

if n == 1:
    print(N[0])
else:

    result = 999
    for x, y in combinations(N, 2):
        a = abs(x - y)
        b = abs(x - abs(24 - y))
        c = max(a, b)
        result = c if result > c else result
    print(result)
