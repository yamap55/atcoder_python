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

a, b, w = LI()

w = w * 1000

if a == b:
    if w % a == 0:
        aa = w / a
        print(aa, aa)
    else:
        print("UNSATISFIABLE")
x = min(a, b)
y = max(a, b)

maxx = int(w / x)
minx = int(w / y)

result = []
print(minx, maxx + 1)
for i in range(minx, maxx + 1):

    for j in range(i + 1):
        aa = x * (i - j) + y * j
        print(f"aa :{aa}, x*(i-j): {x}*{i-j}, y*j: {y}*{j}")
        if w == aa:
            result.append(i)
            break
        elif w < aa:
            break

        # aa = x * (i-j) + x *

# print(f"{result}")
if result:
    print(min(result), max(result))
else:
    print("UNSATISFIABLE")

# 解説見た↓
# import math
# u = math.floor(1000*w/a)
# u = math.floor(1000*w/a)
