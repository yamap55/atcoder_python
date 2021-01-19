#!/usr/bin/env python3

N = int(input())
P = [int(_) for _ in input().split()]

count = 0
flag = False

for i, v in enumerate(P):
    ii = i + 1

    if v == ii:
        if flag:
            flag = False
        else:
            count += 1
            flag = True
    elif flag:
        flag = False
print(count)
