# Ikehara-Wiener Tauber 定理

> **一句话大白话**：如果一个非负系数的 Dirichlet 级数在 $s=1$ 处的主要奇性只是一个留数为 $A$ 的单极点，其余部分在该直线上"规矩"（连续），那么系数的累加和就精确地按 $Ax$ 增长。

> **小例子**：$\zeta(s)=\sum n^{-s}$ 满足 $\zeta(s)-\frac1{s-1}$ 在 $\operatorname{Re}s\ge1$ 连续，取 $a_n=1$、$A=1$，定理直接给出 $\sum_{n\le x}1\sim x$——这正是"整数个数约等于 $x$"。

## 一、定理介绍

> **前置依赖**：Dirichlet 级数、Mellin 变换、Perron 公式（概念）、解析延拓、非负系数的 Karamata 论证（概念）。

Ikehara–Wiener Tauber 定理由江原正博（Shikao Ikehara）于 1931 年在 Wiener 的 Tauber 理论与陶伯型定理框架下证明，是把"解析函数的奇性"翻译为"系数累加和的渐近"的关键工具。它断言：若非负系数 Dirichlet 级数 $\sum a_n n^{-s}$ 在 $\operatorname{Re}s>1$ 收敛，且 $f(s)-\frac{A}{s-1}$ 能连续延拓到闭半平面 $\operatorname{Re}s\ge1$，则 $\sum_{n\le x}a_n\sim Ax$。提出它的动机是给素数定理（PNT）提供一个无需显式公式、无需知道零点分布的干净证明路径：只要验证 $\zeta$ 在 $\operatorname{Re}s\ge1$ 无零点，定理立刻给出 $\psi(x)\sim x$。它是 Wiener 一般 Tauber 定理在 Dirichlet 级数上最常用的特例，也是 Chebotarev 密度定理、Dirichlet 定理与许多数论渐近结果的共同引擎。

## 二、原理思路

1. 用 Mellin–Stieltjes 表示把累加和 $A(x)=\sum_{n\le x}a_n$ 与 $f(s)$ 联系起来：$f(s)=s\int_1^\infty A(x)x^{-s-1}dx$。问题化为由 $f$ 的奇性反推 $A$。
2. 用 Perron 公式把 $A(x)$ 写成沿竖线 $\operatorname{Re}s=c>1$ 的积分，再把积分路径左移到 $\operatorname{Re}s=1$；极点 $\frac{A}{s-1}$ 贡献主角 $Ax$，其余部分因 $h(s)=f(s)-\frac{A}{s-1}$ 在直线上连续而有"频率衰减"，贡献 $o(x)$。
3. 非负性 $a_n\ge0$ 的作用是：$A(x)$ 单调不减，于是"用光滑核卷积得到的平均收敛"可以升级为"逐点收敛"，这是 Wiener–Ikehara 论证的核心一步。

## 三、定理的严格表述

设 $a_n\ge0$（$n\ge1$），且 Dirichlet 级数 $f(s)=\sum_{n\ge1}a_nn^{-s}$ 在 $\operatorname{Re}s>1$ 收敛。若存在常数 $A>0$，使
$$
h(s)=f(s)-\frac{A}{s-1}
$$
可以连续延拓到闭半平面 $\{s:\operatorname{Re}s\ge1\}$（即在 $\operatorname{Re}s\ge1$ 上连续，在 $\operatorname{Re}s>1$ 上解析），则
$$
A(x)=\sum_{n\le x}a_n\sim A\,x\qquad(x\to\infty).
$$

## 四、证明过程

**证明：**

**步骤 1：Mellin–Stieltjes 表示。** 对 $\operatorname{Re}s>1$，由分部求和（Abel 求和）
$$
f(s)=\sum_{n\ge1}a_nn^{-s}=s\int_1^\infty A(x)\,x^{-s-1}\,dx,
$$
因为 $A(x)$ 是阶梯函数、$A(x)=O_\epsilon(x^{1+\epsilon})$。

**步骤 2：Perron 公式。** 对 $c>1$，Perron 公式给出
$$
A(x)=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}f(s)\,\frac{x^{s}}{s}\,ds ,
$$
其中积分沿竖线 $\operatorname{Re}s=c$ 取主值；对非整数 $x$ 此式精确成立（取 $c>1$ 固定，积分绝对收敛性由 $A(x)=O(x^{1+\epsilon})$ 保证）。

**步骤 3：左移积分路径。** 把路径向左移到 $\operatorname{Re}s=1$。被积函数 $\frac{f(s)x^s}{s}$ 在 $s=1$ 有单极点，留数为 $\frac{A\cdot x}{1}=Ax$。于是
$$
A(x)=Ax+\frac{1}{2\pi i}\int_{1-i\infty}^{1+i\infty}h(s)\,\frac{x^{s}}{s}\,ds ,
$$
其中 $h(s)=f(s)-\frac{A}{s-1}$ 在 $\operatorname{Re}s\ge1$ 连续（由假设）且 $h(1)$ 按连续延拓取值。

**步骤 4：残余积分为 $o(x)$。** 记残余积分 $R(x)=\frac{x}{2\pi i}\int_{-\infty}^{\infty}h(1+it)\,\frac{x^{it}}{1+it}\,dt$。令 $g(t)=\frac{h(1+it)}{1+it}$，则 $R(x)/x=\frac{1}{2\pi i}\int_{-\infty}^{\infty}g(t)e^{it\log x}\,dt$ 是 $g$ 的傅里叶逆变换在 $\log x$ 处的值。由 $h$ 在 $\operatorname{Re}s=1$ 连续且 $f$ 有界（非负系数的 Dirichlet 级数在 $\operatorname{Re}s\ge1$ 处 $|f|\le\sum a_nn^{-1}<\infty$），知 $g\in L^2(\mathbb{R})$。由 Riemann–Lebesgue 引理，当 $x\to\infty$（即 $\log x\to\infty$，以平滑化的观点看）
$$
\frac{R(x)}{x}=\frac{1}{2\pi i}\int_{\mathbb{R}}g(t)e^{it\log x}dt\longrightarrow 0 .
$$
更严格地，对 $g$ 先用截断核 $\hat\phi\ge0$（$\phi$ 为光滑紧支函数）做卷积：$\int g(t)\hat\phi(\epsilon t)e^{it\log x}dt$ 一致趋于 $0$（因 $g$ 的平滑化后仍在 $L^1$，其傅里叶变换趋于零），而卷积误差可由 $L^2$ 范数控制。

**步骤 5：由非负性升级为逐点收敛。** 余下的问题只是把"平滑平均收敛"变成"$A(x)/x\to A$"。由于 $a_n\ge0$，$A$ 单调不减，对任意 $0<\lambda<1<\mu$ 有 $\frac{A(\lambda x)}{x}\le\frac{A(x)}{x}\le\frac{A(\mu x)}{x}$。用步骤 4 的结果对 $\lambda x,\mu x$ 取极限，再用 $\lambda\to1^-,\mu\to1^+$ 夹逼，得
$$
A\le\liminf_{x\to\infty}\frac{A(x)}{x}\le\limsup_{x\to\infty}\frac{A(x)}{x}\le A ,
$$
故 $\frac{A(x)}{x}\to A$，即 $A(x)\sim Ax$。$\square$

## 五、应用与意义

- 它是素数定理的干净证明引擎：由 $\zeta(s)-\frac1{s-1}$ 在 $\operatorname{Re}s\ge1$ 连续（等价于 $\zeta$ 在该处无零点）直接得 $\psi(x)\sim x$。
- 用于 Dirichlet 算术级数定理：非主特征 $L(1,\chi)\neq0$ 保证 $L(s,\chi)$ 无极点，定理给出各同余类的素数等分布。
- 在 Chebotarev 密度定理与代数数论中，它是把 Dedekind $\zeta$、Artin $L$-函数的极点信息转为计数渐近的标准工具。
- 在加性数论与筛选理论中，它是圆法、Selberg 筛之外另一条"由解析奇性得渐近"的主干线。
- Wiener 型版本把结论推广到任意 Tauber 核，是调和分析与数论的公共桥梁。

## 相关条目

- [素数定理](./素数定理.md)：以本定理作为最后一步，由 $\psi(x)\sim x$ 推出 $\pi(x)\sim\frac{x}{\log x}$。
- [Dirichlet 算术级数定理](./Dirichlet算术级数定理.md)：对 $L(s,\chi)$ 应用本定理得到算术级数中的素数分布。
- [Mellin 变换](./Mellin变换.md)：本定理中 $f(s)=s\int A(x)x^{-s-1}dx$ 的积分就是 Mellin 变换。
- [Tauber 定理](./Tauber定理.md)：本定理是 Tauber 型结论在 Dirichlet 级数与非负系数下的具体形式。
- [Selberg 筛法](./Selberg筛法.md)：与本文同为计数素数分布的工具，方法互补（筛法 vs 解析奇性）。
- [Chebotarev 密度定理](../第53级-代数数论/Chebotarev密度定理.md)：其证明在最后一步调用 Ikehara 型 Tauber 定理。
