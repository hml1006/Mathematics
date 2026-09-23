# Khintchine 不等式

> **一句话大白话**：用随机正负号把一组数随机加权相加，其结果大小的各阶矩彼此只差一个只依赖阶数的常数——$L^p$ 大小与 $L^2$ 大小是等价的。
>
> **小例子**：取 $a_1=\cdots=a_n=1$，则 $\big(\mathbb E|\sum_{i\le n}r_i|^p\big)^{1/p}$ 与 $\sqrt n$ 只差一个只依赖 $p$ 的常数。

## 介绍

Khintchine 不等式由 Aleksandr Khintchine 于 1923 年证明，是概率论与 Banach 空间理论中关于 Rademacher 随机和的基本不等式。它断言：对任意实（或复）系数 $a_1,\dots,a_n$，随机和 $S=\sum_{i=1}^n a_i r_i$（$r_i$ 为独立 Rademacher 变量，即取值 $\pm1$ 各以概率 $1/2$）的各 $L^p$ 范数彼此等价，等价常数只依赖于 $p$ 而与 $n$ 及 $a_i$ 无关。

Khintchine 不等式是刻画 Banach 空间"型（type）与余型（cotype）"的关键工具：Hilbert 空间具有型 $2$ 与余型 $2$，据此可以给出 Rademacher 级数的收敛判据。

它在上调和分析、随机级数、算子理论与数值线性代数（矩阵的随机符号化、JL 引理）中也有广泛用途。

## 分析

**前置依赖**：Rademacher 随机变量与独立性、Hoeffding 引理（次高斯尾界）、Lyapunov 不等式（$L^p$ 范数关于 $p$ 单调）、Paley–Zygmund 不等式、Hölder 不等式

**定理内容**：对每个 $0<p<\infty$，存在常数 $A_p,B_p>0$（只依赖 $p$）使得对任意有限实系数 $a_1,\dots,a_n$ 与独立 Rademacher 变量 $r_1,\dots,r_n$，

$$A_p\Big(\sum_{i=1}^n a_i^2\Big)^{1/2}\le\Big(\mathbb E\Big|\sum_{i=1}^n a_i r_i\Big|^p\Big)^{1/p}\le B_p\Big(\sum_{i=1}^n a_i^2\Big)^{1/2}.$$

**关键要点**：

- 记 $\sigma^2=\sum_i a_i^2=\mathbb E[S^2]$，则左右两端都以 $\sigma$ 为标尺；
- 常数 $A_p,B_p$ 与维度 $n$ 及系数无关，这正是Khintchine 不等式的价值；
- 上界对 $p\ge2$ 由次高斯尾界给出，对 $p<2$ 由 $L^p$ 范数单调性给出；下界对 $p\ge2$ 用 Lyapunov 不等式，对 $p<2$ 用 Paley–Zygmund 不等式。

## 思考过程

上界的来源是"随机和是次高斯的"。由于每个 $r_i$ 有界且零均值，Hoeffding 引理给出 $\mathbb E[e^{tS}]\le e^{t^2\sigma^2/2}$，等价于尾概率 $\mathbb P(|S|\ge t)\le2e^{-t^2/(2\sigma^2)}$。用 $\mathbb E|S|^p=p\int_0^\infty t^{p-1}\mathbb P(|S|\ge t)\,dt$ 把尾界积成矩界，即得 $\|S\|_p\le B_p\sigma$。当 $p<2$ 时更简单：概率测度下 $(x\mapsto x^{p/2}$ 凹$)$ 由 Jensen 得 $\|S\|_p\le\|S\|_2=\sigma$。

下界的来源分为两段。$p\ge2$ 时，$L^p$ 范数关于 $p$ 单调（Lyapunov 不等式）直接给出 $\|S\|_2\le\|S\|_p$，取 $A_p=1$。$0<p<2$ 时不能用单调性，改用 Paley–Zygmund 不等式：只需知道 $S$ 以一致正概率取到"与 $\sigma$ 同量级"的值。这由四阶矩控制——因为 $S$ 是 Rademacher 线性组合，$\mathbb E[S^4]\le3\sigma^4$，故 $S^2$ 落在 $\sigma^2/2$ 以上的概率至少 $1/12$，于是 $\mathbb E|S|^p\ge12^{-1}2^{-p/2}\sigma^p$。

## 证明过程

记 $S=\sum_{i=1}^n a_i r_i$，$\sigma^2=\mathbb E[S^2]=\sum_{i=1}^n a_i^2$。

**步骤 1：次高斯尾界。** 由 Hoeffding 引理，对任意 $t\in\mathbb R$，

$$\mathbb E\big[e^{tS}\big]=\prod_{i=1}^n\mathbb E\big[e^{ta_i r_i}\big]\le\prod_{i=1}^n e^{t^2 a_i^2/2}=e^{t^2\sigma^2/2},$$

因为 $\cosh(x)\le e^{x^2/2}$。由 Markov 不等式，对 $u>0$，

$$\mathbb P(S\ge u)\le e^{-tu}\mathbb E[e^{tS}]\le e^{-tu+t^2\sigma^2/2},$$

取 $t=u/\sigma^2$ 得 $\mathbb P(S\ge u)\le e^{-u^2/(2\sigma^2)}$；对 $-S$ 同理，故

$$\mathbb P(|S|\ge u)\le 2e^{-u^2/(2\sigma^2)}.$$

**步骤 2：$p\ge1$ 的上界。** 利用 $\mathbb E|S|^p=p\int_0^\infty u^{p-1}\mathbb P(|S|\ge u)\,du$ 与步骤 1，

$$\mathbb E|S|^p\le 2p\int_0^\infty u^{p-1}e^{-u^2/(2\sigma^2)}du=2p\cdot\frac12(2\sigma^2)^{p/2}\Gamma\!\Big(\frac p2\Big)=p\,2^{p/2}\sigma^p\,\Gamma\!\Big(\frac p2\Big).$$

由 $\Gamma(p/2)\le(p/2)^{p/2}$，得

$$\|S\|_p\le 2^{1/2}\Big(p\,\Gamma\!\Big(\frac p2\Big)\Big)^{1/p}\sigma\le 2^{1/2}p^{1/p}\Big(\frac p2\Big)^{1/2}\sigma\le C\sqrt p\,\sigma,$$

其中 $C>0$ 为绝对常数。这给出 $p\ge1$ 时 $B_p=C\sqrt p$。

**步骤 3：$0<p<2$ 的上界。** 概率测度下 $L^p$ 范数关于 $p$ 单调（Lyapunov/Cauchy–Schwarz 或 Jensen 凹性），故 $\|S\|_p\le\|S\|_2=\sigma$，即取 $B_p=1$ 即可。

**步骤 4：$p\ge2$ 的下界。** 由 Lyapunov 不等式，$L^p$ 范数关于 $p$ 递增，故

$$\|S\|_p\ge\|S\|_2=\sigma,$$

即取 $A_p=1$。

**步骤 5：$0<p<2$ 的下界（四阶矩 + Paley–Zygmund）。** 先计算四阶矩。因各 $r_i$ 独立、$\mathbb E[r_i^2]=1$、$\mathbb E[r_i^4]=1$、奇次矩为 $0$，

$$\mathbb E[S^4]=\sum_{i=1}^n a_i^4\,\mathbb E[r_i^4]+6\sum_{i<j}a_i^2a_j^2\,\mathbb E[r_i^2r_j^2]=3\sigma^4-2\sum_{i=1}^n a_i^4\le 3\sigma^4.$$

由 Paley–Zygmund 不等式，对 $0<\theta<1$，

$$\mathbb P\big(S^2>\theta\,\mathbb E[S^2]\big)\ge(1-\theta)^2\frac{(\mathbb E[S^2])^2}{\mathbb E[S^4]}\ge\frac{(1-\theta)^2}{3}.$$

取 $\theta=1/2$，得 $\mathbb P(|S|>\sigma/\sqrt2)\ge1/12$。于是

$$\mathbb E|S|^p\ge\mathbb P\Big(|S|>\frac{\sigma}{\sqrt2}\Big)\Big(\frac{\sigma}{\sqrt2}\Big)^p\ge\frac{1}{12}\,2^{-p/2}\sigma^p,$$

即 $\|S\|_p\ge A_p\sigma$，其中 $A_p=12^{-1/p}2^{-1/2}$（此式对一切 $0<p<2$ 成立）。

**步骤 6：合并。** 取 $A_p=\min(1,12^{-1/p}2^{-1/2})$、$B_p=\max(1,C\sqrt p)$，两步结论合并即得定理的双边估计。$\square$

## 相关条目

- [Banach空间型与余型](./Banach空间型与余型.md)：型与余型的定义直接以 Khintchine 型估计为范本。
- [Riesz表示定理](./Riesz表示定理.md)：$L^p$ 范数等价性常与对偶空间的表示配合使用。
