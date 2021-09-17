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

x = I()

s = str(x)

if x < 100:
    print(0)
    sys.exit()

aa = x / 105
bb = x % 105

total_105 = aa * 105

# if aa == 0:
#     # 100 以上 104円以下
#     if x:

if bb == 0:
    if x >= total_105:
        print(1)
    else:
        print(0)
    sys.exit()
    # print(1)
    # sys.exit()

# 104 以下
if x >= 100:
    print(1)
    sys.exit()

a = bb / 5
b = bb % 5

total_5 = a * 105

if b == 0:
    if x >= total_105 + total_5:
        print(1)
    else:
        print(0)
    sys.exit()

if x >= total_105 + total_5 + 100 + b:
    print(1)
else:
    print(0)
sys.exit()
