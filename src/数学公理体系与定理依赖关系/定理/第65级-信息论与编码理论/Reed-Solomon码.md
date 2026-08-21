# Reed–Solomon 码

> **一句话大白话**：把一段数据看成多项式的取值，靠"采样点多于坏点数"来揪出错位——即便一小撮字节被篡改，凭剩余完好的点也能把整条多项式原样复原。
>
> **小例子**：对有限域 $\mathbb F_q$ 上度数 $<k$ 的多项式，取它在 $n$ 个不同点上的取值作为码字，当 $n-k$ 为偶数时可纠正 $\frac{n-k}{2}$ 个错误——CD、二维码就是这么活下来的。

## 一、定理介绍

> **前置依赖**：有限域 $\mathbb{F}_q$ 的结构理论、多项式根数不超过其次数的基本定理、线性码的维数与最小距离、Singleton 界、Hamming 重量与纠错能力的关系。

Reed–Solomon（RS）码是一类基于有限域上多项式取值构造的线性码。它同时达到 Singleton 界，因此是**最大距离可分（MDS）码**。RS 码具有较强的纠错能力，且拥有高效的译码算法（如 Berlekamp–Massey 算法），是实际通信和存储系统中最广泛使用的纠错码之一。

## 二、原理思路

Reed–Solomon 码把 $k$ 个信息符号看作一个次数小于 $k$ 的多项式

$$
f(X)=a_0+a_1X+\cdots+a_{k-1}X^{k-1}
$$

的系数。编码过程是在 $n$ 个不同的有限域点上求值，得到码字

$$
\bigl(f(\alpha_1),f(\alpha_2),\dots,f(\alpha_n)\bigr).
$$

由于非零次数小于 $k$ 的多项式至多有 $k-1$ 个根，因此任意非零码字至少有 $n-k+1$ 个非零分量，即最小距离至少为 $n-k+1$。而 Singleton 界断言 $d\le n-k+1$，故等号成立。

## 三、定理的严格表述

设 $q$ 为素数幂，$\mathbb{F}_q$ 为 $q$ 元有限域。取 $1\le k\le n\le q$，并选取 $n$ 个互不相同的点

$$
\alpha_1,\alpha_2,\dots,\alpha_n\in\mathbb{F}_q.
$$

定义 Reed–Solomon 码为

$$
C=\left\{\bigl(f(\alpha_1),f(\alpha_2),\dots,f(\alpha_n)\bigr)\in\mathbb{F}_q^n:\;f\in\mathbb{F}_q[X],\;\deg f<k\right\}.
$$

则 $C$ 是 $\mathbb{F}_q$ 上的线性 $[n,k,n-k+1]$ 码，因而是 MDS 码。

## 四、证明过程

### 1. 线性性

设 $f,g\in\mathbb{F}_q[X]$ 的次数均小于 $k$，$\lambda\in\mathbb{F}_q$。则 $\deg(f+\lambda g)<k$，且

$$
(f+\lambda g)(\alpha_i)=f(\alpha_i)+\lambda g(\alpha_i).
$$

因此码字集合对加法和数乘封闭，$C$ 是线性子空间。

### 2. 维数

映射

$$
\varphi:\{f\in\mathbb{F}_q[X]:\deg f<k\}\longrightarrow \mathbb{F}_q^n,
\quad f\mapsto \bigl(f(\alpha_1),\dots,f(\alpha_n)\bigr)
$$

是线性映射。若 $\varphi(f)=0$，则 $f$ 在 $n$ 个不同点 $\alpha_1,\dots,\alpha_n$ 上取零值。但 $\deg f<k\le n$，故 $f$ 必为零多项式。因此 $\varphi$ 是单射，定义域维数为 $k$，所以 $\dim C=k$。

### 3. 最小距离

任取非零码字 $c=\varphi(f)$。因为 $f\neq 0$ 且 $\deg f\le k-1$，$f$ 在 $\mathbb{F}_q$ 中至多有 $k-1$ 个根。因此 $c$ 的零分量数至多为 $k-1$，非零分量数至少为 $n-k+1$，即 Hamming 重量

$$
w_H(c)\ge n-k+1.
$$

于是最小距离 $d\ge n-k+1$。

### 4. 达到 Singleton 界

对任意 $[n,k,d]$ 线性码，Singleton 界给出

$$
d\le n-k+1.
$$

结合第 3 步，得到 $d=n-k+1$，故 RS 码是 MDS 码。

## 五、应用与意义

1. **光盘与二维码**：CD、DVD、蓝光光盘以及 QR 码都使用 Reed–Solomon 码纠正突发错误和擦除。
2. **卫星与深空通信**：NASA 的深空探测任务广泛采用 RS 码与卷积码级联，以对抗高噪声信道。
3. **存储系统**：RAID 6、SSD 控制器和分布式存储中的擦除码常基于 Reed–Solomon 构造。
4. **代数编码理论**：RS 码是 BCH 码的特殊情形，也是构造更复杂码（如代数几何码、级联码、局部可修复码）的基本构件。
5. **译码效率**：基于 syndrome 的 Berlekamp–Massey 算法和基于插值的 Guruswami–Sudan 列表译码算法，使 RS 码在理论和实践中都极具价值。
