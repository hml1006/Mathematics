# Sobolev 嵌入定理

## 介绍

Sobolev 嵌入定理（Sobolev embedding theorem）是 Sobolev 空间理论中最核心的定理之一，它描述了 Sobolev 空间 $W^{k,p}(\Omega)$ 与更光滑的函数空间（如 $L^q$ 空间、Hölder 空间）之间的包含关系。该定理断言，当函数的弱导数阶数足够高时，函数实际上具有更好的可积性或连续性。该定理是 PDE 解的正则性分析中不可或缺的工具。

## 分析

**前置依赖**：Sobolev 空间定义、$L^p$ 空间、Hölder 空间、嵌入、紧嵌入。

**定理内容**：设 $\Omega \subset \mathbb{R}^n$ 是有界光滑区域，$1 \le p < \infty$，$k$ 为非负整数。

**(1) Gagliardo–Nirenberg–Sobolev 不等式**（$1 \le p < n$）：存在常数 $C = C(n,p)$ 使得对所有 $u \in W_0^{1,p}(\Omega)$，
$$\|u\|_{L^{p^*}(\Omega)} \le C \|\nabla u\|_{L^p(\Omega)}$$
其中 $p^* = \frac{np}{n-p}$ 是 Sobolev 共轭指数。

**(2) 嵌入定理**：
- 若 $kp < n$，则 $W^{k,p}(\Omega) \hookrightarrow L^q(\Omega)$ 对任意 $q \in [p, p^*]$ 连续嵌入，其中 $p^* = \frac{np}{n-kp}$。
- 若 $kp = n$，则 $W^{k,p}(\Omega) \hookrightarrow L^q(\Omega)$ 对任意 $q \in [p, \infty)$ 连续嵌入。
- 若 $kp > n$，则 $W^{k,p}(\Omega) \hookrightarrow C^{k-\lfloor n/p\rfloor-1,\gamma}(\overline{\Omega})$ 连续嵌入到 Hölder 空间。

**(3) Rellich–Kondrachov 紧嵌入定理**：若 $kp \le n$ 且 $q < p^*$，则嵌入 $W^{k,p}(\Omega) \hookrightarrow\hookrightarrow L^q(\Omega)$ 是紧的（即 $W^{k,p}$ 中的有界列在 $L^q$ 中有收敛子列）。

**数学内涵**：Sobolev 嵌入定理揭示了弱导数阶数 $k$、空间维数 $n$ 和可积性指数 $p$ 之间的精妙关系。当 $k > n/p$ 时，函数实际上连续（Morrey 不等式），这解释了为何 PDE 在空间维数较低时具有更好的正则性。

**证明策略**：
- GNS 不等式：通过 $L^p$ 版本的微积分基本定理和 Hölder 不等式证明。
- 一般嵌入：通过迭代应用 GNS 不等式和插值不等式。
- 紧嵌入：通过 Arzelà–Ascoli 定理和 $L^p$ 空间的紧性准则。

## 思考过程

Sobolev 嵌入定理的直观理解：如果 $u$ 有足够多的弱导数，那么 $u$ 比一般的 $L^p$ 函数更"光滑"。$k$ 越大、$p$ 越大，$u$ 的正则性越好。

关键的数量关系是 $k - n/p$，它可以看作 Sobolev 函数的"正则性指数"：
- 若 $k - n/p < 0$，则 $u$ 在 $L^q$ 中，$q$ 可以比 $p$ 大（$p^*$ 是最大值）。
- 若 $k - n/p > 0$，则 $u$ 是 Hölder 连续的（指数为 $k - n/p$ 的小数部分）。
- 若 $k - n/p = 0$，则 $u$ 属于所有 $L^q$（$q < \infty$）但不一定连续。

物理上，$n=1$ 时 $H^1$ 中的函数连续（$1/2 > 0$），$n=2$ 时 $H^1$ 中的函数属于所有 $L^q$（$q<\infty$）但不一定连续，$n=3$ 时 $H^1$ 嵌入到 $L^6$。

## 证明过程

**定理**（Gagliardo–Nirenberg–Sobolev 不等式）：设 $1 \le p < n$，则存在 $C = C(n,p)$ 使得对所有 $u \in C_c^1(\mathbb{R}^n)$，
$$\|u\|_{L^{p^*}(\mathbb{R}^n)} \le C \|\nabla u\|_{L^p(\mathbb{R}^n)}$$
其中 $p^* = np/(n-p)$。

**证明**（对 $p=1$ 的情形）：

**步骤 1**：对 $x = (x_1,\dots,x_n) \in \mathbb{R}^n$，由微积分基本定理，
$$|u(x)| \le \int_{-\infty}^{x_1} |\partial_{x_1} u(t_1, x_2,\dots,x_n)| \, dt_1 \le \int_{-\infty}^{\infty} |\partial_{x_1} u(t_1, x_2,\dots,x_n)| \, dt_1$$
类似地，在 $n$ 个坐标方向都有这样的估计。

**步骤 2**：将这 $n$ 个不等式相乘，得到
$$|u(x)|^n \le \prod_{i=1}^n \left(\int_{-\infty}^{\infty} |\partial_{x_i} u(\dots, t_i,\dots)| \, dt_i\right)$$

**步骤 3**：对 $x_1$ 积分，利用 Hölder 不等式和 Fubini 定理，可得
$$\int_{-\infty}^{\infty} |u(x)|^{n/(n-1)} \, dx_1 \le \left(\int_{-\infty}^{\infty} |\nabla u| \, dx_1\right)^{1/(n-1)} \prod_{i=2}^n \left(\cdots\right)^{1/(n-1)}$$
重复此过程，最终得到
$$\|u\|_{L^{n/(n-1)}(\mathbb{R}^n)} \le \prod_{i=1}^n \left(\int_{\mathbb{R}^n} |\partial_{x_i} u| \, dx\right)^{1/n} \le \frac{1}{n} \sum_{i=1}^n \int_{\mathbb{R}^n} |\partial_{x_i} u| \, dx \le \int_{\mathbb{R}^n} |\nabla u| \, dx$$

**步骤 4**：对一般 $1 < p < n$，对 $v = |u|^\gamma$ 应用 $p=1$ 的结果，结合 Hölder 不等式可得一般情形。$\square$

**定理**（Sobolev 嵌入定理）：设 $\Omega \subset \mathbb{R}^n$ 是有界光滑区域，则：
1. 若 $kp < n$，则 $W^{k,p}(\Omega) \hookrightarrow L^q(\Omega)$ 对 $p \le q \le p^* = np/(n-kp)$。
2. 若 $kp > n$，则 $W^{k,p}(\Omega) \hookrightarrow C^{0,\gamma}(\overline{\Omega})$，其中 $\gamma = k - \lfloor n/p\rfloor - 1$（若 $n/p$ 不是整数）或任意 $\gamma < 1$（若 $n/p$ 是整数）。

**证明思路**：对 $k=1$ 的情形，GNS 不等式给出 $W^{1,p} \hookrightarrow L^{p^*}$。对 $k>1$，迭代应用 $k$ 次，每次提升可积性指数。对于 $kp > n$ 的情形，利用 Morrey 不等式
$$\|u\|_{C^{0,\gamma}(\overline{\Omega})} \le C \|u\|_{W^{1,p}(\Omega)}$$
其中 $\gamma = 1 - n/p$，然后迭代。$\square$

**推论**（紧嵌入）：若 $1 \le q < p^*$，则 $W^{1,p}(\Omega) \hookrightarrow\hookrightarrow L^q(\Omega)$ 是紧嵌入，即 $W^{1,p}$ 中的有界列在 $L^q$ 中有收敛子列。