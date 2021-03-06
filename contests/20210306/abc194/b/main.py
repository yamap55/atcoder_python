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

n = I()
l = LIR(n)

a1 = (10 ** 6, None)
a2 = (10 ** 6, None)
b1 = (10 ** 6, None)
b2 = (10 ** 6, None)

# bl = []
for i, (a, b) in enumerate(l):
    if a < a1[0]:
        a2 = a1
        a1 = (a, i)
    elif a < a2[0]:
        a2 = (a, i)

    if b < b1[0]:
        b2 = b1
        b1 = (b, i)
    elif b < b2[0]:
        b2 = (b, i)
    # print(f"a1={a1}, a2={a2},b1={b1}, b2={b2}")

# print(f"a1={a1}, a2={a2},b1={b1}, b2={b2}")

# print(f"aa {a1[1]} == {b1[1]}")
if a1[1] == b1[1]:
    # print(a1[0], b1[0], a2[0], b2[0])
    print(min(max(a1[0], b2[0]), max(a2[0], b1[0]), a1[0] + b1[0]))
else:
    # print(a1[0], b1[0])
    print(max(a1[0], b1[0]))
