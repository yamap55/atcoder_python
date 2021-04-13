#!/usr/bin/env python3
n = [int(_) for _ in input().split()]
N = n[0]
K = n[1]

N = [int(input()) for _ in range(N)]

total = 0
for i, v in enumerate(N):
    total += v
    if K <= total:
        print(i + 1)
        break
