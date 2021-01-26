#!/usr/bin/env python3
N = [int(_) for _ in input().split()]
x = N[0]
y = N[1]

if x % y == 0:
    print(-1)
else:
    for i in range(2, 1000000000):
        # for i in range(2, 1000):
        a = x * i
        # print(a, x, i)
        if a % y == 0:
            continue
        print(a)
        break
