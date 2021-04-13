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

n, k = LI()


a = LI()
index_list = []
aa = []

_next = a[0]
l = [1]
ll = [_next]
while True:
    i = _next - 1
    _next = a[i]
    if _next in ll:
        break
    l.append(i)
    ll.append(_next)

for i in a:
    if i in aa:
        break
    aa.append(i)

l = len(aa)

h = k % l
# hh = h - 1
# if hh == -1:
#     hh = l
hh = h
print(f"hoge: {aa}, {h}")
print(aa[hh])
