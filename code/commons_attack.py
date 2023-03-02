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
        return (gcd, y - (b//a) * x, x) # շת����������Ƶ�ÿ��a��b������ʹ��gcd(a,b)=ax+by���� 

# 0, 4
def attack(i, j):
    e1 = int(e[i], 16)
    e2 = int(e[j], 16)
    c1 = int(c[i], 16)
    c2 = int(c[j], 16)
    n = int(N[i], 16)

    gcd, r, s = egcd(e1, e2)
    # ����r, sΪ���������
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
    with open(f"/Users/racerz/Desktop/����ѧ/�����������/������ս��������/data/Frame{i}", 'r') as f:
        data = f.read()
        N.append(data[:256])
        e.append(data[256:512])
        c.append(data[512:768])
attack(0, 4)

