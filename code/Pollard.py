# coding=gbk
import gmpy2
import binascii

N = []
e = []
c = []

def pollard(n):
    B = 2 ** 20
    a = 2
    for i in range(2, B+1):
        a = pow(a, i, n)    # 优化
        d = gmpy2.gcd(a-1, n)
        if 1<d<n:
            return d

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

index = [2, 6, 19]

for each in index:
    p = pollard(int(N[each], 16))
    q = int(N[each], 16) // p
    print(f'[+]frame{each}\'s p = {p} and q = {q}')

    plain = decrypt(p, q, int(e[each], 16), int(c[each], 16))
    plain = binascii.a2b_hex(hex(plain)[2:])
    print(f'[+]frame{each}\'s plain is {plain[-8:].decode()}')
