#!/usr/bin/env python3
N = [int(_) for _ in input().split()]
A = N[0]
B = N[1]
C = N[2]


if C == 0:
    A = A - 1
else:
    B = B - 1

if A == B:
    if C == 0:
        print("Takahashi")
    else:
        print("Aoki")
elif A > B:
    print("Takahashi")
else:
    print("Aoki")
