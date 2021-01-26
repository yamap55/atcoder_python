#!/usr/bin/env python3
N = [int(_) for _ in input().split()]
H = N[0]
W = N[1]

M = [int(_) for _ in input().split()]

h = M[0]
w = M[1]


print((H - h) * (W - w))
