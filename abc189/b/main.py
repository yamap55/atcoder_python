#!/usr/bin/env python3
a = [int(_) for _ in input().split()]
N = a[0]
X = a[1]

l = [input().split() for _ in range(N)]

al = 0
result = -1
for i, r in enumerate(l):
    v = int(r[0])
    p = int(r[1])
    # al = al + (v * p / 100)
    # if X < al:
    # 小数点以下は誤差が出るので100倍して比較
    al = al + (v * p)
    if (X * 100) < al:
        result = i + 1
        break

print(result)
