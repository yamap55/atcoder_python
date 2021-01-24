#!/usr/bin/env python3
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from fractions import gcd
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, merge
from itertools import accumulate, combinations, permutations, product

S = input()
N = int(input())


print(sorted([a + b for a, b in product(S, S)])[N - 1])
