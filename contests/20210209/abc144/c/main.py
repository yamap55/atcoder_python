#!/usr/bin/env python3

import math

N = int(input())

for i in reversed(range(1, int(math.sqrt(N)) + 1)):
    if N % i == 0:

        print(int(i - 1 + (N / i - 1)))
        break
