# coding=gbk
import gmpy2
import binascii


N = []
e = []
c = []

def find_same_actor():
    global N
    ps = []
    same_actor = []
    for i in range(21):
        for j in range(i+1, 21):
            if int(N[i] == N[j]):
                continue
            p = gmpy2.gcd(int(N[i], 16), int(N[j], 16))
            if p != 1:
                print(f'[+] ({i}, {j})')
                ps.append(p)
                same_actor.append((i,j))
    return ps, same_actor

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

ps, same_actor = find_same_actor()
for p, index in zip(ps, same_actor):
    q1 = int(N[index[0]], 16) // p
    q2 = int(N[index[1]], 16) // p

    print(f'[+]frame{index[0]}\'s p = {p}, q = {q1}')
    plain1 = decrypt(p, q1, int(e[index[0]], 16), int(c[index[0]], 16))
    print(f'[+]plain from frame{index[0]}\'s {binascii.a2b_hex(hex(plain1)[2:])[-8:]}')
    
    print(f'[+]frame{index[1]}\'s p = {p}, q = {q2}')
    plain2 = decrypt(p, q2, int(e[index[1]], 16), int(c[index[1]], 16))
    print(f'[+]plain from frame{index[1]}\'s {binascii.a2b_hex(hex(plain2)[2:])[-8:]}')

    