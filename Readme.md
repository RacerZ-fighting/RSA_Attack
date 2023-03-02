**1.** **Commons_attack 共模攻击**

先看一下帧数据结构

![img](file:////private/var/folders/j8/6sgvpp850l38kj2v82cgnmwm0000gn/T/com.kingsoft.wpsoffice.mac/wps-racerz/ksohtml//wps1.jpg) 

明文结构如下:

>  分片明文填充为 512 比特消息后再进行加密，填充规则为高位添加 64 比特标志位，随后加上 32 比特通信序号，再添加若干个 0，最后 64 比特为明文分片字符对应的 ASCII 码

将所有帧中的对应模数、加密指数以及密文分组提取出来，方便后续计算

```python
for i in range(21):
    with open(f"/Users/racerz/Desktop/密码学/待解决的问题/密码挑战赛赛题三/data/Frame{i}", 'r') as f:
        data = f.read()
        N.append(data[:256])
        e.append(data[256:512])
        c.append(data[512:768])
print(N)
```

共模攻击的利用条件是**两个密文加密时使用相同的模数，且加密相同明文**

我们先寻找有无公共模数

```python
def find():
    index1 = 0
    index2 = 0
    for i in range(21):
        for j in range(i+1, 21):
            if N[i] == N[j]:
                print(str((i, j)))
```

然后利用公共模数攻击

PS：对于扩展欧几里得算法递归式思路，[如图所示](https://www.cnblogs.com/fusiwei/p/11775503.html)

![img](file:////private/var/folders/j8/6sgvpp850l38kj2v82cgnmwm0000gn/T/com.kingsoft.wpsoffice.mac/wps-racerz/ksohtml//wps2.jpg) 

代码见 `code/commons_attack.py`	 

输出结果为 `My secre`

**2.** **Low Private Exponent 低加密指数攻击**

原理：假设所有的加密指数 $e_i$ 都等于3. 一个简单的论证表明，如果 $k \geq 3$，Marvin 便可以恢复M。实际上，Marvin 得到 $C_1,C_2,C_3$，其中
$$
C_1=M^3 \ mod\ N_1, \ \ C_2=M^3 \ mod\ N_2, \ \ C_3=M^3 \ mod\ N_3
$$
我们假设 $N_i$ 之间两两互素，否则的话 Marvin 便可以直接因式分解其中的一些 $N_i$。利用 CRT，我们就可以得到一个 $C’ \in \Z_{N_1N_2N_3}$ 满足 $C’ = M^3 \ mod \ N_1N_2N_3$ . 因为M是小于所有 $N_i$ 的，因此 $M^3 < N_1N_2N_3$. 所以 $C’=M^3$ 遍历整数，Marvin 可以通过计算 $C’$ 的立方根来恢复M。更一般地说，如果所有公共指数都等于e，只需 $k \geq e$ ， Marvin 便可以恢复 M。只有当使用小 e 时，攻击才是可行的。

我们结合上述思路去做题。符合低加密指数的帧有Frame3 8 12 16 20

代码见 `code/low_e.py`	

**3.** 因数碰撞攻击 Frame1 18

这种含有共因子的可以通过欧几里得求 gcd 得到模数的因子，进而通过简单的乘除运算即可分解 N，比较简单

代码见 `code/gcd.py`

结果如下：

![img](file:////private/var/folders/j8/6sgvpp850l38kj2v82cgnmwm0000gn/T/com.kingsoft.wpsoffice.mac/wps-racerz/ksohtml//wps15.jpg) 

**4.** **费马分解法 Frame 10**

![img](file:////private/var/folders/j8/6sgvpp850l38kj2v82cgnmwm0000gn/T/com.kingsoft.wpsoffice.mac/wps-racerz/ksohtml//wps16.jpg)

代码见 `code/fermat_factor.py`

结果如下:

![img](file:////private/var/folders/j8/6sgvpp850l38kj2v82cgnmwm0000gn/T/com.kingsoft.wpsoffice.mac/wps-racerz/ksohtml//wps17.jpg) 

**5.** Pollard p-1 分解法 Frame 2 6 19

**适用于p-1或q-1能够被小素数整除的情况**

![img](file:////private/var/folders/j8/6sgvpp850l38kj2v82cgnmwm0000gn/T/com.kingsoft.wpsoffice.mac/wps-racerz/ksohtml//wps18.jpg)

算法步骤：

![img](file:////private/var/folders/j8/6sgvpp850l38kj2v82cgnmwm0000gn/T/com.kingsoft.wpsoffice.mac/wps-racerz/ksohtml//wps19.jpg) 

代码见 `code/Pollard.py`

结果如下：

![img](file:////private/var/folders/j8/6sgvpp850l38kj2v82cgnmwm0000gn/T/com.kingsoft.wpsoffice.mac/wps-racerz/ksohtml//wps20.jpg) 

最终仍有5个Frame无法恢复，分别是5,9,13,14,17

通过猜测获得最终明文：

> "My secret is a famous saying of Albert Einstein. That is \\"Logic will get you from A to B. Imagination will take you everywhere.\\""