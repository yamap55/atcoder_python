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
ca = LIR(n)

# print(ca)
for l, r in ca:
    # print(l, r)
    # print(l, r)
    # for i in combinations(range(l, r + 1), 3):
    #     print(i)
    if l == r:
        if l == 0:
            print(1)
        else:
            print(0)
        continue
    n1 = l * 2

    a = r - n1 + 1
    # if n1 < r:
    #     print(0)
    #     continue

    # a = r - l - 1
    aa = int(a / 2 * (a + 1))
    # if l == 0:
    #     aa += r - l + 1
    print(aa)
