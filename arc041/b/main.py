#!/usr/bin/env python3
N = [int(_) for _ in input().split()]
Y = N[0]
X = N[1]

L = [[int(_) for _ in input()] for _ in range(Y)]

print(Y, X)
print(L)

print(L[0])
print(L[len(L) - 1])

result = [["0" for _ in range(X)] for _ in range(Y)]


def f(x, y):
    xx = x - 1
    yy = y - 1

    # 差分
    diff_y = len(L) - y
    diff_x = len(L[0]) - x


# output
for a in result:
    print("".join(a))
