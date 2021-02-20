#!/usr/bin/env python3
import sys
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right  # type: ignore
from collections import Counter, defaultdict, deque  # type: ignore
from fractions import gcd  # type: ignore
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, merge  # type: ignore
from itertools import accumulate, combinations, permutations, product  # type: ignore


LI = lambda: list(map(int, sys.stdin.buffer.readline().split()))
I = lambda: int(sys.stdin.buffer.readline())
LS = lambda: sys.stdin.buffer.readline().rstrip().decode("utf-8").split()
S = lambda: sys.stdin.buffer.readline().rstrip().decode("utf-8")
IR = lambda n: [I() for _ in range(n)]
LIR = lambda n: [LI() for _ in range(n)]
SR = lambda n: [S() for _ in range(n)]
LSR = lambda n: [LS() for _ in range(n)]
SRL = lambda n: [list(S()) for _ in range(n)]
MSRL = lambda n: [[int(i) for i in list(S())] for _ in range(n)]

n, k = LS()
k = int(k)
# print(n, k)


def g2(x: str):
    return int("".join(sorted(x)))


def g1(x: str):
    return int("".join(sorted(x, reverse=True)))


d = {}


def f(x: str):
    if x in d:
        return d[x]
    # print(g1(x), g2(x))
    result = g1(x) - g2(x)
    d[x] = result
    return result


a = n
for _ in range(k):
    a = f(str(a))

print(a)
