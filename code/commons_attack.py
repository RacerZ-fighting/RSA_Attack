# coding=gbk
import binascii
from Crypto.Util.number import *

N = []
e = []
c = []

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd(b%a, a)
        return (gcd, y - (b//a) * x, x) # 辗转相除法反向推导每层a、b的因子使得gcd(a,b)=ax+by成立 

# 0, 4
def attack(i, j):
    e1 = int(e[i], 16)
    e2 = int(e[j], 16)
    c1 = int(c[i], 16)
    c2 = int(c[j], 16)
    n = int(N[i], 16)

    gcd, r, s = egcd(e1, e2)
    # 考虑r, s为负数的情况
    if r < 0:
        r = -r
        c1 = inverse(c1, n)
    elif s < 0:
        s = -s
        c2 = inverse(c2, n)
    m = pow(c1, r, n)*pow(c2, s, n) % n
    plain = binascii.a2b_hex(hex(m)[2:])
    print(plain[-8:])

for i in range(21):
    with open(f"/Users/racerz/Desktop/密码学/待解决的问题/密码挑战赛赛题三/data/Frame{i}", 'r') as f:
        data = f.read()
        N.append(data[:256])
        e.append(data[256:512])
        c.append(data[512:768])
attack(0, 4)

