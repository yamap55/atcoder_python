#!/usr/bin/env python3
N = int(input())


def f(target):
    # 総和を求める。
    # 多分使用しない
    _len = len(target)
    result = (target[0] + target[-1]) * int(_len / 2)

    if _len % 2 == 1:
        result += target[int(_len / 2)]
    return result


def ff(i, a, b):
    # 割ってる数と、割った数と、その余りで出せるはず
    return True


count = 0
for i in range(1, N + 1):
    a = int(N / i)  #
    b = N % i  #

    # i = 51
    # x = 6

    n = int(N / i)  # 8

    _max = n + int(i / 2)  # 11
    _min = _max - i + 1  # 5 + 1
    if _min < 0:
        break
    ll = range(_min, _max + 1)

    if sum(ll) == N:
        print(_min, _max)
        print(sum(ll), list(ll))
        count += 2

print(count)
