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

h, w, x, y = LI()

x -= 1
y -= 1

l = [S() for _ in range(h)]


# yy =

# kakutei_count = 0
# count = 0
# for i, yy in enumerate(l[y]):
#     print(yy)
#     if i < x:
#         if yy == ".":
#             count += 1
#         else:
#             count = 0
#     elif i == x:
#         count += 1
#         kakutei_count += count
#         count = 0
#     elif i == (w - 1):
#         if yy == ".":
#             count += 1
#             kakutei_count += count
#         else:
#             kakutei_count += count
#             count = 0
#     else:
#         if yy == ".":
#             count += 1
#         else:
#             count = 0

# ll = [yy[x] for yy in l]

# count = 0
# kakutei_count_x = 0
# for i, xx in enumerate(ll):
#     print(xx)
#     if i < y:
#         if xx == ".":
#             count += 1
#         else:
#             count = 0
#     elif i == y:
#         count += 1
#         kakutei_count_x += count
#         count = 0

#     elif i == (h - 1):
#         if xx == ".":
#             count += 1
#             kakutei_count_x += count
#         else:
#             kakutei_count_x += count
#             count = 0
#     else:
#         if xx == ".":
#             count += 1
#         else:
#             count = 0
# print(kakutei_count, kakutei_count_x, 1)
# print(kakutei_count + kakutei_count_x - 1)

kakutei_count = 0
count = 0
for i, yy in enumerate(l[x]):
    # print(yy)
    if i < y:
        if yy == ".":
            count += 1
        else:
            count = 0
    elif i == y:
        count += 1
        kakutei_count += count
        count = 0
    elif i == (w - 1):
        if yy == ".":
            count += 1
            kakutei_count += count
        else:
            kakutei_count += count
            count = 0
    else:
        if yy == ".":
            count += 1
        else:
            kakutei_count += count
            count = 0
            break
ll = [yy[y] for yy in l]

count = 0
kakutei_count_x = 0
for i, xx in enumerate(ll):
    # print(xx)
    if i < x:
        if xx == ".":
            count += 1
            # print("aa")
        else:
            count = 0
            # print("bb")
    elif i == x:
        count += 1
        kakutei_count_x += count
        count = 0
        # print("cc")

    elif i == (h - 1):
        if xx == ".":
            count += 1
            kakutei_count_x += count
            # print("dd")
        else:
            kakutei_count_x += count
            count = 0
            # print("ee")
    else:
        if xx == ".":
            count += 1
            # print("ff")
        else:
            kakutei_count_x += count
            count = 0
            # print("gg")
            break
# print(kakutei_count, kakutei_count_x, 1)
print(kakutei_count + kakutei_count_x - 1)
