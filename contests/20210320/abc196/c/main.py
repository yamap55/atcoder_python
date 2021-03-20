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

# count = 0
# for i in range(1, I() + 1):
#     ii = str(i)
#     _len = len(ii)
#     if len(ii) % 2 != 0:
#         continue
#     a = int(_len / 2)

#     if ii[:a] == ii[a:]:
#         count += 1
# print(count)

s = S()
_len = len(s)

if _len == 1:
    print(0)
elif _len % 2 == 0:
    # 桁数が偶数の場合
    # 奇数の時も多分同じロジックになる？
    a = int(_len / 2)
    b = int(s[:a])
    c = int(s[a:])
    if b > c:
        b -= 1
    print(b)
else:
    # 奇数の時
    a = int(_len / 2)
    s = "9" * a * 2
    b = int(s[:a])
    c = int(s[a:])
    if b > c:
        b -= 1
    print(b)
