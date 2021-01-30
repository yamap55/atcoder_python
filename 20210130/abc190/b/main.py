#!/usr/bin/env python3
n = [int(_) for _ in input().split()]
N = n[0]
S = n[1]
D = n[2]

l = [[int(_) for _ in input().split()] for i in range(N)]

flag = False
for a in l:
    x = a[0]
    y = a[1]

    if x < S and y > D:
        # print(x, y)
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")
