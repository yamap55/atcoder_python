#!/usr/bin/env python3
NN = [int(_) for _ in input().split()]
N = NN[0]
L = NN[1]

_lines = [[_ for _ in input().split("|")] for _ in range(L)]

lines = []
for l in _lines:
    l.pop(-1)
    l.pop(0)
    lines.append(l)

# for _ in lines:
#     print(_)
# print(lines)
y = input()

ans_n = int(y.index("o") / 2)
# print(ans_n)
lines = reversed(lines)
a = ans_n

if N == 1:
    print(a + 1)
    exit(0)

for line in lines:
    # print(f"line: {a}, {line}")

    if a == 0:
        if line[a] == "-":
            a = a + 1
    elif a == len(line):
        if line[a - 1] == "-":
            a = a - 1
    else:
        if line[a] == "-":
            a = a + 1
        elif line[a - 1] == "-":
            a = a - 1
# print(y)
# if N == 1:

print(a + 1)
