#!/usr/bin/env python3
from collections import defaultdict

aa = [int(_) for _ in input().split()]
N = aa[0]
K = aa[1]
l = [int(_) for _ in input().split()]

l.sort()


d = defaultdict(int)
for i in l:
    d[str(i)] += 1
# print(d)
_max = l[-1]
a = K  # 残りの箱
total = 0
for i in range(_max + 1):
    # print("now: ", a, total)
    _count = d[str(i)]
    if not _count:
        # 数値がなかった時（穴あきの時
        total += a * i
        a = 0
        break
    # 数値があった時
    diff = _count - a
    if diff < 0:
        # totalに加算して、残りの箱を減らす
        a += diff
        # print("diff: ", diff, (diff * -1 * i))
        total = total + (diff * -1 * i)
        if a < 0:
            break
# print("last: ", f"{total}, {a} * {_max} +1")
total = total + (a * (_max + 1))
print(total)
