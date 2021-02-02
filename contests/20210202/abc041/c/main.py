#!/usr/bin/env python3
N = int(input())

l = {str(i + 1): int(v) for i, v in enumerate(input().split())}

a = sorted(l.items(), key=lambda x: x[1], reverse=True)

for aa in a:
    print(aa[0])
