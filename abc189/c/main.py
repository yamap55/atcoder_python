#!/usr/bin/env python3
N = int(input())
L = [int(_) for _ in input().split()]

max_count = -1
temp = None
for i, num in enumerate(L):

    kosuu = N - i
    for ii, numnum in enumerate(L):
        if ii < i:
            continue
        # 愚直にやりすぎ。多分もう一回ループを回すのは悪手

        if num > numnum:
            kosuu = ii - i
            break
    count = num * kosuu
    # print("その数のカウント: ", count, num, kosuu, i, ii)
    if max_count < count:
        temp = num, kosuu
        max_count = count

# print("temp: ", temp)
print(max_count)


# ある範囲内のmin * lenが値になるので、それの最大を求めれば良いっというのが答えだと思うのだけど。。。
#


# max_count = -1
# temp = None
# for i, num in enumerate(L):

#     kosuu = N - i
#     for ii, numnum in enumerate(L[i:]):
#         # 愚直にやりすぎ。多分もう一回ループを回すのは悪手

#         if num > numnum:
#             kosuu = ii
#             break
#     count = num * kosuu
#     # print("その数のカウント: ", count, num, kosuu, i, ii)
#     if max_count < count:
#         temp = num, kosuu
#         max_count = count

# # print("temp: ", temp)
# print(max_count)
