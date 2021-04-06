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

s = S()
c = Counter(s)

# a = True
# b = True
ns = True
we = True
if c["N"]:
    if not c["S"]:
        ns = False
        # print("No")
        # exit(0)
elif c["S"]:
    if not c["N"]:
        ns = False
        # print("No")
        # exit(0)
elif c["W"]:
    if not c["E"]:
        we = False
        # print("No")
        # exit(0)
elif c["E"]:
    if not c["W"]:
        we = False
        # print("No")
        # exit(0)
# print("Yes")

if ns and we:
    print("Yes")
else:
    print("No")

# a = 0
# b = 0
# for i in s:
#     if i == "N":
#         a += 1
#     elif i == "S":
#         a -= 1
#     elif i == "W":
#         b += 1
#     else:
#         b -= 1

# a = 0
# b = 0
# for i in s:
#     if i == "N":
#         if a < 0:
#             a = 0
#         else:
#             a += 1
#     elif i == "S":
#         if a > 0:
#             a = 0
#         else:
#             a -= 1
#     elif i == "W":
#         if b < 0:
#             b = 0
#         else:
#             b += 1
#     else:
#         if b > 0:
#             b = 0
#         else:
#             b -= 1

# a = 0
# b = 0
# for i in s:
#     if i == "N":
#         if a == 0:
#             a += 1
#         else:
#     elif i == "S":
#         a -= 1
#     elif i == "W":
#         b += 1
#     else:
#         b -= 1


# if a == 0 and b == 0:
#     print("Yes")
#     exit(0)

# print("No")
