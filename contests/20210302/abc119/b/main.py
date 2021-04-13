n = int(input())

c = 0
for a, b in [[ii for ii in input().split()] for _ in range(n)]:
    a = float(a)
    if b != "JPY":
        a = a * 380000.0
    c += a
print(c)
