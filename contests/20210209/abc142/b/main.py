#!/usr/bin/env python3
n = [int(_) for _ in input().split()]
N = n[0]
K = n[1]

print(len([True for _ in input().split() if int(_) >= K]))
