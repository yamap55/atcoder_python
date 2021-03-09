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

n, m = LI()

l = IR(m)

s = 1

d = {"1": 1, "2": 2, "3": 3}


def f(i: int) -> int:
    si = str(i)

    if si in d:
        return d[si]
    else:
        j = f(i - 1) + f(i - 2)
        d[si] = j
        return j


before = -1

for i, x in enumerate(l):
    if before + 1 == x:
        print(0)
        sys.exit(0)
    y = 2
    if i == 0:
        y = 1
    z = f(x - s - y)
    s *= z
    before = x

z = f(n - l[-1])
s *= z

print(s % 1000000007)
