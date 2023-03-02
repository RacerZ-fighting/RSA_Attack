# coding=gbk
import binascii
from Crypto.Util.number import *
import gmpy2


N = []
e = []
c = []

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd(b%a, a)
        return (gcd, y - (b//a) * x, x) # 辗转相除法反向推导每层a、b的因子使得gcd(a,b)=ax+by成立 


def chinese_remainder_therom(items):
    N = 1
    result = 0
    for a,n in items:
        N *= n
    for a, n in items:
        m = N//n
        gcd, r, s = egcd(n, m)
        if gcd != 1:
            N = N // n
            continue
        result += a*s*m
    return result % N, N

# 低加密指数
# Frame3/8/12/16/20
def low_e_5():
    sessions = [
        {"c":int(c[3], 16), "n": int(N[3], 16)},
        {"c":int(c[8], 16), "n": int(N[8], 16)},
        {"c":int(c[12], 16), "n": int(N[12], 16)},
        {"c":int(c[16], 16), "n": int(N[16], 16)},
        {"c":int(c[20], 16), "n": int(N[20], 16)},
    ]
    data = []
    for session in sessions:
        data += [(session['c'], session['n'])]
    x, y = chinese_remainder_therom(data)
    return x, y

def recover_the_plain():
    x,y = low_e_5()
    tmp = gmpy2.iroot(gmpy2.mpz(x), 5)
    return binascii.a2b_hex(hex(tmp[0])[2:])


for i in range(21):
    with open(f"/Users/racerz/Desktop/密码学/待解决的问题/密码挑战赛赛题三/data/Frame{i}", 'r') as f:
        data = f.read()
        N.append(data[:256])
        e.append(data[256:512])
        c.append(data[512:768])

plain = recover_the_plain()
print(plain[-8:])
