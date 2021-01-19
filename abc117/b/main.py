#!/usr/bin/env python3
N = int(input())
L = [int(_) for _ in input().split()]

m = max(L)
print("Yes" if m < (sum(L) - m) else "No")
