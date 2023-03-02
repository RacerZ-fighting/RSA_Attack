# coding=gbk
import gmpy2
import binascii
import math

N = []
e = []
c = []


def factor(n):
    base = math.factorial(2 ** 14)
    x = 0
    i = 0
    y = 0
    x0 = gmpy2.iroot(n, 2)[0] + 1
    while(i <= (base - 1)):
        x = (x0+i)*(x0+i) - n
        if gmpy2.is_square(x):
            y = gmpy2.isqrt(x)
            break
        i += 1
    p = x0 + i + y     # 平方差
    return p

def decrypt(p, q, e, c):
    phi = (p-1)*(q-1)
    
    d = gmpy2.invert(e, phi)
    plain = gmpy2.powmod(c, d, p*q)
    return plain

for i in range(21):
    with open(f"/Users/racerz/Desktop/密码学/待解决的问题/密码挑战赛赛题三/data/Frame{i}", 'r') as f:
        data = f.read()
        N.append(data[:256])
        e.append(data[256:512])
        c.append(data[512:768])

p = factor(int(N[10], 16))
q = int(N[10], 16) // p
print(f'[+]frame10\'s p = {p} and q = {q}')
plain = decrypt(p, q, int(e[10], 16), int(c[10], 16))
plain = binascii.a2b_hex(hex(plain)[2:])
print(f'[+]frame10\'s plain is {plain[-8:].decode()}')


