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
x = S()
m = I()


def f(X, n):
    out = 0
    for i in range(1, len(str(X)) + 1):
        out += int(X[-i]) * (n ** (i - 1))
    return out


c = 0
b = int(max(x)) + 1

if m < f(x, b):
    print(0)
    exit()

# while True:

#     ii = f(x, b)
#     if m < ii:
#         break
#     c += 1
#     b += 1

# print(c)

ok = b
ng = int(x)


def ff(ok, ng):
    # print(ok, ng)
    if (ng - ok) == 1:
        # print(f"end: {ok}")
        return ok
    a = int((ok + ng) / 2)
    ii = f(x, a)
    # print(f"計算結果: {ii}")
    if m >= ii:
        return ff(a, ng)
    else:
        return ff(ok, a)


z = ff(ok, ng)
print(z - b + 1)
