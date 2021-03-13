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
i = I()

# i = 1_000
# i = 999_999_999
_len = len(str(i))

if _len <= 3:
    print(0)
    sys.exit(0)
a = int((_len - 1) / 3)
# print(a)


def f(i: int) -> int:
    a = 0
    for j in range(1, i + 1):
        a += (int(f"{'999'*(j+1)}") - int(f"{'999'*(j)}")) * j
        # aa = int(f"999{'000'*j}")
        # # print(aa)
        # a += aa
    return a


def ff(i: int) -> int:
    return int(f"{'999'*(i+1)}")


z = f(a - 1)  # フルで数えられる分のカンマ数

y = ff(a - 1)  # フルで数えられた分の値
# print(f"z + (i - y) * a: {z} + ({i} - {y}) * {a}")
print(z + (i - y) * a)
