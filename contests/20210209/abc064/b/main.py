#!/usr/bin/env python3
N = int(input())

l = [int(_) for _ in input().split()]

print(max(l) - min(l))
