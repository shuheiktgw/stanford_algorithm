import math
import random

def karatsuba(top, bottom):
    len_top = len(str(abs(top)))
    len_bottom = len(str(abs(bottom)))

    if len_top == 1 or len_bottom == 1:
        return top * bottom
    else:

        n = max(len_top, len_bottom)
        nby2 = int(math.trunc(n / 2))

        a = int(math.trunc(top / 10 ** nby2))
        b = int(math.trunc(top % 10 ** nby2))
        c = int(math.trunc(bottom / 10 ** nby2))
        d = int(math.trunc(bottom % 10 ** nby2))

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = ac + bd - karatsuba(a - b, c - d)

        return ac * 10 ** (2*nby2) + ad_plus_bc * 10 ** nby2 + bd

karatsuba(-11, -11)
# cont = True
# while cont:
#     first = random.randint(1 ,10000)
#     second = random.randint(1 ,10000)
#     ans = first * second
#     print(first)
#     print(second)
#
#     if karatsuba(first, second) != ans:
#         cont = False
#         print("Miss!!!!!!")
#     else:
#         print("Good")










