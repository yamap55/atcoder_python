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
h, w, a, b = LI()

if a == 0:
    print(1)
elif a == 1:
    aa = (h - 1) * (w - 1) * 2 + h - 1 + w - 1
    print(aa)

else:

    class point:
        def __init__(self, x1, y1, x2, y2):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2

        def get_t(self):
            return [(self.x1, self.y1), (self.x2, self.y2)]

    points = []
    for hh in range(h - 1):
        for ww in range(w - 1):
            points.append(point(hh, ww, hh + 1, ww))
            points.append(point(hh, ww, hh, ww + 1))
    for ww in range(w - 1):
        points.append(point(h, ww, h, ww + 1))
    for hh in range(h - 1):
        points.append(point(hh, w, h + 1, w))

    count = 0
    # print(len(points), a, len(list(combinations(points, a))))
    for z in combinations(points, a):
        l = []
        f = True
        for zz in z:
            t1, t2 = zz.get_t()
            if t1 in l or t2 in l:
                f = False
                break
            else:
                l.append(t1)
                l.append(t2)
        if f:
            ccc = []
            for zz in z:
                t1, t2 = zz.get_t()
                ccc.append([t1, t2])
            print(ccc)

            count += 1
    print(count)
