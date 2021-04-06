#!/usr/bin/env python3
import sys
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right  # type: ignore
from collections import Counter, defaultdict, deque  # type: ignore
from fractions import gcd  # type: ignore
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, merge  # type: ignore
from itertools import accumulate, combinations, permutations, product  # type: ignore
import math

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
p = permutations(l, len(l))
p = list(p)
_len = len(p)
all_total = 0
for pp in p:
    total = 0
    point = None
    for x, y in pp:
        if point is None:
            pass
        else:
            total += math.sqrt((point[0] - x) ** 2 + (point[1] - y) ** 2)
        point = x, y
    # print(f"pp: {pp}, {total}")

    all_total += total

print(all_total / _len)
#
#
# 1.41421356237
