# Dirichlet 算术级数定理

> **一句话大白话**：只要 $a$ 与 $q$ 互素，数列 $a, a+q, a+2q, a+3q,\dots$ 里就有无穷多个素数。例如 $4k+1$、$4k+3$、$6k+1$ 这些"等差"序列全都藏着无穷多个素数。
>
> **小例子**：$q=4$，$a=3$：$3,7,11,19,23,31,43,47,59,\dots$ 全是素数且无穷多；$a=1$：$5,13,17,29,37,41,\dots$ 同样无穷多。每个与 $4$ 互素的余类里都有无穷多素数。

## 一、定理介绍

Dirichlet 定理（1837）是解析数论的里程碑：它保证素数在每个"与模互素的算术级数"中分布无穷，并给出了它们的渐近密度 $\frac1{\varphi(q)}$。它首次系统引入 Dirichlet 特征与 L-函数，是数论从"初等"走向"解析"的分水岭，也是后续 Langlands 纲领的算术起点。

## 二、原理思路

把"素数按模 $q$ 的余类计数"转化为"一组 L-函数的对数导数的加权和"。对 $n\equiv a\pmod q$ 的素数幂求和可写为
$$\sum_{\substack{n\equiv a\bmod q}}\frac{\Lambda(n)}{n^s}=\frac1{\varphi(q)}\sum_{\chi\bmod q}\overline\chi(a)\left(-\frac{L'(s,\chi)}{L(s,\chi)}\right),$$
这是基于特征的正交性。关键在于证明对每个非主特征有 $L(1,\chi)\neq0$（否则会导出一个非零实根，与算术矛盾）。一旦 $L(1,\chi)\neq0$，主特征贡献主导项 $\frac1{\varphi(q)}\frac1{s-1}$，再由 Tauber 定理推出结果。

## 三、定理的严格表述

设 $q\ge1$ 为正整数，$\gcd(a,q)=1$。则算术级数 $\{a+kq:k\ge0\}$ 中含无穷多个素数，且
$$\#\{p\le x:p\equiv a\pmod q\}\sim\frac1{\varphi(q)}\frac{x}{\log x}\quad(x\to\infty).$$

## 四、证明过程

**证明（利用 $L(1,\chi)\neq0$）：**

**步骤 1：特征正交关系。** 对 $\operatorname{Re}(s)>1$，$-\frac{L'(s,\chi)}{L(s,\chi)}=\sum_n \chi(n)\Lambda(n)n^{-s}$。由
$$\sum_{\chi\bmod q}\overline\chi(a)\chi(n)=\begin{cases}\varphi(q),&n\equiv a\pmod q,\\0,&\text{否则},\end{cases}$$
得
$$\sum_{n\equiv a\bmod q}\frac{\Lambda(n)}{n^s}=\frac1{\varphi(q)}\sum_{\chi}\overline\chi(a)\left(-\frac{L'(s,\chi)}{L(s,\chi)}\right).$$

**步骤 2：主特征行为。** $L(s,\chi_0)=\zeta(s)\prod_{p\mid q}(1-p^{-s})$，在 $s=1$ 处有一阶极点。

**步骤 3：证明 $L(1,\chi)\neq0$。** 考虑 $F(s)=\prod_{\chi}L(s,\chi)$。若某非主特征 $L(1,\chi)=0$，则其零点抵消主特征的极点，$F$ 在 $s=1$ 解析。但
$$\log F(s)=\sum_{\chi}\sum_{p}\sum_{k\ge1}\frac{\chi(p^k)}{kp^{ks}}=\sum_{p^k\equiv1\bmod q}\frac{\varphi(q)}{kp^{ks}}\ge0,\quad s>1,$$
故 $F(s)\to+\infty$ 当 $s\to1^+$，与"解析且取有限正值的 $F(1)$"矛盾。故对所有非主特征 $L(1,\chi)\neq0$。

**步骤 4：应用 Tauber 定理。** 因 $L(1,\chi)\neq0$，仅主特征在 $s=1$ 有极点，故 $\sum_{n\equiv a\bmod q}\Lambda(n)\sim\frac{x}{\varphi(q)}$，推出 $\#\{p\le x:p\equiv a\pmod q\}\sim\frac1{\varphi(q)}\frac{x}{\log x}$。$\square$

## 五、应用与意义

Dirichlet 定理是素数分布理论的基本构件。它的"L-函数与特征分解"思想被推广为 Chebotarev 稠密定理（代数数域）、Langlands 对偶与自守形式理论——每个更深的"素数在算术群中的分布"问题都以之为原型。在密码学与算法数论中，它保证了构造大素数（特殊余类）的可行性，是现代素性检测与密钥生成的理论基础。