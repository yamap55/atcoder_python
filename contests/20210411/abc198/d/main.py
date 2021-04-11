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

DEFINE = "UNSOLVABLE"
s1, s2, s3 = SR(3)


def f():
    m = max(len(s1), len(s2))
    l = len(s3)

    return m == l or (m == l - 1)


if not f():
    print(DEFINE)
    exit(0)

unique_str = set(s1 + s2 + s3)
_len = len(unique_str)

if _len > 10:
    print(DEFINE)
    exit(0)

for p in permutations(range(10), _len):
    ss1 = s1
    ss2 = s2
    ss3 = s3
    for a, b in zip(unique_str, p):
        ss1 = ss1.replace(a, str(b))
        ss2 = ss2.replace(a, str(b))
        ss3 = ss3.replace(a, str(b))
    if ss1[0] == "0":
        continue
    if ss2[0] == "0":
        continue
    if ss3[0] == "0":
        continue
    i1 = int(ss1)
    i2 = int(ss2)
    i3 = int(ss3)

    if len(str(i1)) != len(s1):
        continue
    if len(str(i2)) != len(s2):
        continue
    if len(str(i3)) != len(s3):
        continue
    if i1 + i2 == i3:
        print(i1)
        print(i2)
        print(i3)
        exit(0)

print(DEFINE)


# z = list(a)[0]
# s = set('a' + 'b')

# list(zip(s, z))
