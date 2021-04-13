#!/usr/bin/env python3
from collections import deque

N = int(input())
NN = [[int(_) for _ in input().split()] for _ in range(2)]

x_list = deque(NN[0])
y_list = deque(NN[1])


def f(x, y, max_1, new_x, new_y):
    _max = x * y
    max_1 = new_x if new_x > max_1 else max_1
    new = max_1 * new_y
    output = _max
    if _max < new:
        output = new
        x = max_1
        y = new_y
    return x, y, max_1, output


x = y = max_1 = 0
for _ in range(N):
    x, y, max_1, output = f(x, y, max_1, x_list.popleft(), y_list.popleft())
    print(output)
