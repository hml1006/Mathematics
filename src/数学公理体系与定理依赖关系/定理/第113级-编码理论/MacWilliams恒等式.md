# MacWilliams恒等式

> **一句话大白话**：一个线性码和它的对偶码，重量分布不是"各算各的"，而是由一个漂亮的多项式公式互相锁定：知道了原码每个重量有多少个码字，就能直接推出对偶码的重量分布，不用再去逐个数。
>
> **小例子**：$[7,4,3]$ Hamming 码及其增广对偶——通过 MacWilliams 恒等式，用原码 $(A_0,A_1,\dots)$ 代入 $W_{\mathcal C^\perp}(x,y)=\frac1{|\mathcal C|}W_{\mathcal C}(y-x,y+(q-1)x)$，展开比较 $x^jy^{n-j}$ 系数即得对偶码各重量计数，全程无需手工枚举。

## 一、定理介绍

**MacWilliams 恒等式**：设 $\mathcal C$ 为 $\mathbb F_q$ 上 $[n,k]$ 线性码，$\mathcal C^\perp$ 为其对偶码，重量分布分别为 $(A_i)$ 与 $(B_j)$，重量枚举多项式 $W_{\mathcal C}(x,y)=\sum_iA_ix^iy^{n-i}$。则
$$
W_{\mathcal C^\perp}(x,y)=\frac{1}{|\mathcal C|}W_{\mathcal C}\big(y-x,\ y+(q-1)x\big).
$$
等价地逐系数用 **Krawtchouk 多项式** $P_j(i;n,q)$ 表示。

## 二、原理思路

用**有限 Fourier 分析**。引入非平凡加法特征 $\chi$，把指示函数 $\mathbf 1_{\mathcal C}$ 做 Fourier 变换：因 $\mathcal C$ 是子空间，$\widehat{\mathbf1}_{\mathcal C}(u)=|\mathcal C|\,\mathbf1_{\mathcal C^\perp}(u)$（在 $\mathcal C^\perp$ 上为 $|\mathcal C|$、否则为 0）。对 $g(v)=x^{w(v)}y^{n-w(v)}$ 用 **Poisson 求和公式**：$\sum_{v\in\mathcal C}g(v)=\frac1{|\mathcal C^\perp|}\sum_{u\in\mathcal C^\perp}\hat g(u)$。计算 $\hat g(u)=(y-x)^{w(u)}(y+(q-1)x)^{n-w(u)}$，代回并整理即得恒等式。

## 三、定理的严格表述

$W_{\mathcal C^\perp}(x,y)=\frac1{|\mathcal C|}W_{\mathcal C}(y-x,\,y+(q-1)x)$。系数形式：
$$
B_j=\frac1{|\mathcal C|}\sum_{i=0}^nA_i\,P_j(i;n,q),\qquad
P_j(i;n,q)=\sum_{r=0}^j(-1)^r(q-1)^{j-r}\binom{i}{r}\binom{n-i}{j-r}.
$$

## 四、证明要点

1. **Fourier 变换**.$\hat f(u)=\sum_{v\in\mathbb F_q^n}f(v)\chi(u\cdot v)$；$\mathbf1_{\mathcal C}$ 的变换在子空间上为 $|\mathcal C|$、其余为 0。
2. **Poisson 求和**.$\sum_{v\in\mathcal C}g(v)=\frac1{|\mathcal C^\perp|}\sum_{u\in\mathcal C^\perp}\hat g(u)$。
3. **计算 $\hat g$**.因 $g$ 是乘积型且 $\chi(u\cdot v)=\prod_i\chi(u_iv_i)$，$u_i\ne0$ 的那个坐标贡献 $y-x$、$u_i=0$ 的贡献 $y+(q-1)x$，故 $\hat g(u)=(y-x)^{w(u)}(y+(q-1)x)^{n-w(u)}$。
4. **代回比较系数**.用 $|\mathcal C^\perp|=q^n/|\mathcal C|$ 整理，比较 $x^jy^{n-j}$ 系数即得系数型恒等式与 Krawtchouk 多项式。$\square$

## 五、应用与意义

- **对偶重量分布**.免去对偶码的冗长枚举，直接代数得出。
- **性能分析**.用于纠错译码的误码/(码)重量谱推导，评估随机差错。
- **与码率优化结合**.配合"对偶码更短"的特性优化存储。
- **理论地位**.线性码代数结构（Fourier/对偶）跟组合重量分布的桥梁式定理。