# Kolmogorov–Chentsov 连续性定理

> **一句话大白话**：如果间隔很小的两个时刻，过程差值的"高阶矩"以足够快的速度收缩（像 $|X_s-X_t|\le C|t-s|^\beta$ 的矩条件），就能证明整个路径可以搭一条连续版本，连 Hölder 光滑度都能给出来。
>
> **小例子**：Brown 运动满足 $\mathbb{E}|B_t-B_s|^{2m}\le C_m|t-s|^m$，取 $m>1$ 使条件成立，得到 $B$ 有连续路径的版本，且几乎处处 $\alpha<\tfrac12$ 次 Hölder 连续。

## 介绍

Kolmogorov–Chentsov 连续性定理（Kolmogorov continuity criterion）是随机过程理论中关于样本路径连续性的基本定理。它给出了一个随机过程存在连续修正的充分条件：若过程的矩满足某种 Hölder 条件，则存在一个连续版本的样本路径。该定理是构造 Brown 运动等连续随机过程的关键工具，也是随机分析中许多估计的基础。

## 分析

**前置依赖**：Kolmogorov 扩张定理、随机过程、样本路径、修正、Hölder 连续性、矩条件。

**定理内容**：设 $\{X_t, t \in [0,T]\}$ 是随机过程，若存在常数 $a,b,C > 0$ 使得对所有 $s,t \in [0,T]$，
$$E[|X_t - X_s|^a] \le C|t-s|^{1+b}$$
则存在 $X$ 的修正 $\tilde{X}$（即 $\tilde{X}_t = X_t$ a.s. 对所有 $t$），使得 $\tilde{X}$ 的样本路径几乎必然连续。更精确地，$\tilde{X}$ 的样本路径对任意 $\gamma \in (0, b/a)$ 是 $\gamma$-Hölder 连续的：
$$|\tilde{X}_t(\omega) - \tilde{X}_s(\omega)| \le K(\omega) |t-s|^\gamma$$
其中 $K(\omega)$ 是有限随机变量。

**数学内涵**：该定理表明，过程的矩条件可以控制样本路径的正则性。矩条件 $E[|X_t - X_s|^a] \le C|t-s|^{1+b}$ 意味着过程在 $L^a$ 意义下是 $(1+b)/a$-Hölder 连续的，而这个条件足以保证存在连续版本。

**证明策略**：利用 dyadic 分划（二进制有理点）上的估计，通过 Borel–Cantelli 引理证明在这些点上的一致收敛，然后将 $\tilde{X}$ 定义为极限过程，再延拓到所有实数。

## 思考过程

Kolmogorov–Chentsov 连续性定理的证明思路是通过离散点上的控制来得到连续版本的构造。其核心是估计在 dyadic 分划（即形如 $k/2^n$ 的点）上的增量：

对 $t = k/2^n$，$s = (k-1)/2^n$，由 Chebyshev 不等式，
$$P(|X_t - X_s| \ge 2^{-\gamma n}) \le 2^{\gamma a n} E[|X_t - X_s|^a] \le C 2^{\gamma a n} 2^{-n(1+b)} = C 2^{-n(1+b-\gamma a)}$$
当 $\gamma < b/a$ 时，$1+b-\gamma a > 1$，故 $\sum_{n} \sum_{k} P(|X_{k/2^n} - X_{(k-1)/2^n}| \ge 2^{-\gamma n}) < \infty$。由 Borel–Cantelli 引理，以概率 1，对充分大的 $n$，所有 dyadic 区间上的增量都小于 $2^{-\gamma n}$，从而样本路径在 dyadic 点上一致连续，可以唯一延拓到所有实数。

## 证明过程

**定理**（Kolmogorov–Chentsov 连续性准则）：设 $\{X_t, t \in [0,T]\}$ 满足
$$E[|X_t - X_s|^a] \le C|t-s|^{1+b}$$
对某些 $a,b,C > 0$。则存在修正 $\tilde{X}$ 具有 $\gamma$-Hölder 连续样本路径，对任意 $\gamma \in (0, b/a)$。

**证明**：

**步骤 1**：Dyadic 分划上的估计。对 $n \ge 1$，定义 $D_n = \{k/2^n \mid 0 \le k \le 2^n\}$，$D = \bigcup_{n\ge 1} D_n$（二进制有理点集）。

对 $t^{(n)}_k = k/2^n$，考虑增量 $\Delta^{(n)}_k = X_{t^{(n)}_k} - X_{t^{(n)}_{k-1}}$。由矩条件，
$$P(|\Delta^{(n)}_k| \ge 2^{-\gamma n}) \le 2^{\gamma a n} E[|\Delta^{(n)}_k|^a] \le C 2^{\gamma a n} \cdot 2^{-n(1+b)} = C 2^{-n(1+b-\gamma a)}$$

**步骤 2**：Borel–Cantelli 论证。由于 $\gamma < b/a$，$1+b-\gamma a > 1$，故
$$\sum_{n=1}^\infty \sum_{k=1}^{2^n} P(|\Delta^{(n)}_k| \ge 2^{-\gamma n}) \le C \sum_{n=1}^\infty 2^n \cdot 2^{-n(1+b-\gamma a)} = C \sum_{n=1}^\infty 2^{-n(b-\gamma a)} < \infty$$
由 Borel–Cantelli 引理，以概率 1，存在 $N(\omega)$ 使得对所有 $n \ge N(\omega)$ 和所有 $k$，$|\Delta^{(n)}_k| < 2^{-\gamma n}$。

**步骤 3**：Dyadic 点上的 Hölder 连续性。对任意 $s,t \in D$，$s < t$，将区间 $[s,t]$ 表示为二进制区间的并，可得
$$|X_t - X_s| \le \frac{2}{1-2^{-\gamma}} |t-s|^\gamma$$
以概率 1 成立。

**步骤 4**：一致连续性和延拓。由上述估计，$\{X_t, t \in D\}$ 以概率 1 一致连续。定义 $\tilde{X}_t(\omega) = \lim_{D \ni s \to t} X_s(\omega)$（当极限存在且有限时），否则定义 $\tilde{X}_t(\omega) = 0$。则 $\tilde{X}$ 是 $X$ 的修正，且样本路径连续。

**步骤 5**：Hölder 连续性。对任意 $\gamma < b/a$，$\tilde{X}$ 的样本路径是 $\gamma$-Hölder 连续的。$\square$

**推论**（Brown 运动的存在性）：标准 Brown 运动 $B_t$ 满足 $E[|B_t - B_s|^4] = 3|t-s|^2$，即 $a=4$，$b=1$。由 Kolmogorov–Chentsov 定理，Brown 运动存在连续修正，且对任意 $\gamma < 1/2$，其样本路径是 $\gamma$-Hölder 连续的。