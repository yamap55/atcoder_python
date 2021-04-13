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

s = input()


def ff(ss):
    pass


def f(ss):
    end_flag = False
    b = ss
    a = None
    try:
        a = ss.index("LR")
        b = ss[0 : a + 1]
    except ValueError:
        # 最後まで来ている
        end_flag = True
    if len(ss) == a + 2:
        end_flag = True
    ff(b)
    if end_flag:
        return

    s = ss[a + 1 :]
    print(s)


a = s.index("LR")
b = s[0 : a + 1]
print(b)
s = s[a + 1 :]
print(s)
