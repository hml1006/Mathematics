# 完备化与Hensel引理

> **一句话大白话**：在"某素点附近"把环补全成连续世界（如同把有理数补全成实数），Hensel 引理说：在这个补全世界里，只要一个小解粗略成立即可"精确到可迭代"，小根能一路精确提升成大真根——数值分析的模版。
>
> **小例子**：解 $x^2\equiv2\,(\bmod\,7^k)$，模 $7$ 的近似解 $x\equiv3$ 经 Hensel 提升逐步可推出模任意 $7^k$ 的解，其在 $7$-进制数 $\mathbb{Z}_7$ 中有唯一真解 $\sqrt{2}$。

## 介绍

完备化（Completion）是交换代数中通过赋予环一个拓扑结构（通常是 $\mathfrak{m}$-adic 拓扑）来构造新环的方法，类似于从有理数域 $\mathbb{Q}$ 构造 $p$-adic 数域 $\mathbb{Q}_p$。Hensel 引理（Hensel's Lemma）是完备化理论中的核心结果，它断言在完备局部环中，如果多项式在剩余域中有根，则可以提升到环中有根。Hensel 引理是 $p$-adic 分析、代数数论和代数几何中研究局部环的基本工具。

## 分析

**前置依赖**：交换代数、局部环、逆极限、拓扑环、多项式环。

**数学内涵**：

**定义**：
- 设 $(R, \mathfrak{m})$ 是局部环，$R$ 的 $\mathfrak{m}$-adic 完备化定义为 $\hat{R} = \varprojlim_{n} R/\mathfrak{m}^n$。
- 完备化的元素是序列 $(a_n)_{n \ge 1}$，其中 $a_n \in R/\mathfrak{m}^n$ 且 $a_{n+1} \equiv a_n \pmod{\mathfrak{m}^n}$。
- $R$ 称为**完备**的，如果自然映射 $R \to \hat{R}$ 是同构。

**Hensel 引理**：设 $(R, \mathfrak{m})$ 是完备局部环，$k = R/\mathfrak{m}$ 是剩余域。设 $f(x) \in R[x]$ 是多项式，$\bar{f}(x) \in k[x]$ 是 $f$ 在 $k$ 上的约化。若存在分解 $\bar{f}(x) = \bar{g}_0(x) \bar{h}_0(x)$，其中 $\bar{g}_0(x)$ 和 $\bar{h}_0(x)$ 在 $k[x]$ 中互素，则存在 $f(x) = g(x) h(x)$ 在 $R[x]$ 中的分解，使得 $\bar{g}(x) = \bar{g}_0(x)$，$\bar{h}(x) = \bar{h}_0(x)$，且 $\deg g = \deg \bar{g}_0$。

**数学内涵**：Hensel 引理断言，在完备局部环中，多项式在剩余域中的因子分解可以提升到环中。

**证明策略**：利用 Newton 迭代法或归纳法构造提升序列，通过完备性取极限。

## 思考过程

Hensel 引理的核心思想是"从模 $\mathfrak{m}$ 到模 $\mathfrak{m}^n$ 的逐步提升"。给定模 $\mathfrak{m}$ 下的根 $a_0$（即 $f(a_0) \equiv 0 \pmod{\mathfrak{m}}$），我们可以逐步构造 $a_1, a_2, \ldots$ 使得 $f(a_n) \equiv 0 \pmod{\mathfrak{m}^{n+1}}$。这个过程类似于牛顿法求根，其中导数 $f'(a_0)$ 的可逆性保证了迭代的收敛性。

完备性保证了极限 $\lim a_n$ 存在，且在 $R$ 中，从而得到精确的根。

在 $p$-adic 数论中，Hensel 引理是研究 $\mathbb{Z}_p$ 上多项式方程解的基本工具。例如，它可用于判断 $\mathbb{Q}_p$ 中的平方数。

## 证明过程

### 完备化的构造

**定义**：设 $(R, \mathfrak{m})$ 是局部环。$R$ 的 $\mathfrak{m}$-adic 完备化定义为：
$$
\hat{R} = \varprojlim_{n} R/\mathfrak{m}^n = \left\{(a_n) \in \prod_{n=1}^\infty R/\mathfrak{m}^n \mid a_{n+1} \equiv a_n \pmod{\mathfrak{m}^n}\right\}
$$

**定理 1**：$\hat{R}$ 是局部环，极大理想为 $\hat{\mathfrak{m}} = \varprojlim \mathfrak{m}/\mathfrak{m}^n$，且 $\hat{R}/\hat{\mathfrak{m}} \cong R/\mathfrak{m}$。

**证明**：$\hat{R}$ 是逆极限，环结构由分量运算给出。$\hat{R}$ 中的元素 $(a_n)$ 可逆当且仅当 $a_1 \ne 0$ 在 $R/\mathfrak{m}$ 中，故 $\hat{\mathfrak{m}}$ 是唯一的极大理想。$\square$

### Hensel 引理（简单形式）

**引理**（Hensel 引理 - 简单形式）：设 $(R, \mathfrak{m})$ 是完备局部环，$f(x) \in R[x]$，$a_0 \in R$ 满足：
1. $f(a_0) \equiv 0 \pmod{\mathfrak{m}}$；
2. $f'(a_0) \not\equiv 0 \pmod{\mathfrak{m}}$（即 $f'(a_0)$ 是单位）。
则存在唯一的 $a \in R$ 使得 $f(a) = 0$ 且 $a \equiv a_0 \pmod{\mathfrak{m}}$。

**证明**：构造序列 $\{a_n\}$ 如下：
- 假设已构造 $a_n$ 满足 $f(a_n) \equiv 0 \pmod{\mathfrak{m}^{n+1}}$。
- 令 $a_{n+1} = a_n - f(a_n) f'(a_n)^{-1}$（Newton 迭代）。
- 则 $f(a_{n+1}) \equiv 0 \pmod{\mathfrak{m}^{n+2}}$。

由完备性，$\{a_n\}$ 收敛到 $a \in R$，且 $f(a) = 0$。$\square$

### Hensel 引理（一般形式）

**定理 2**（Hensel 引理 - 一般形式）：设 $(R, \mathfrak{m})$ 是完备局部环，$k = R/\mathfrak{m}$，$f(x) \in R[x]$。若在 $k[x]$ 中有分解 $\bar{f}(x) = \bar{g}_0(x) \bar{h}_0(x)$，其中 $\bar{g}_0, \bar{h}_0$ 互素，则存在 $R[x]$ 中的分解 $f(x) = g(x) h(x)$ 使得 $\bar{g} = \bar{g}_0$，$\bar{h} = \bar{h}_0$，且 $\deg g = \deg \bar{g}_0$。

**证明**：

**步骤 1**：构造 $g_0, h_0 \in R[x]$ 使得 $\bar{g}_0 = \bar{g}_0$，$\bar{h}_0 = \bar{h}_0$，且 $\deg g_0 = \deg \bar{g}_0$，$\deg h_0 \le \deg \bar{h}_0$。

**步骤 2**：设 $f - g_0 h_0 \in \mathfrak{m} R[x]$。假设已构造 $g_n, h_n$ 使得 $f - g_n h_n \in \mathfrak{m}^{n+1} R[x]$。寻找 $u_n, v_n \in \mathfrak{m}^{n+1} R[x]$ 使得：
$$
f - (g_n + u_n)(h_n + v_n) \in \mathfrak{m}^{n+2} R[x]
$$
这等价于 $f - g_n h_n - g_n v_n - h_n u_n \in \mathfrak{m}^{n+2} R[x]$。

**步骤 3**：由于 $\bar{g}_0$ 和 $\bar{h}_0$ 互素，存在 $a, b \in R[x]$ 使得 $a g_0 + b h_0 \equiv 1 \pmod{\mathfrak{m}}$。令：
$$
u_n = b (f - g_n h_n), \quad v_n = a (f - g_n h_n)
$$
则 $g_n v_n + h_n u_n = (g_n a + h_n b)(f - g_n h_n) \equiv f - g_n h_n \pmod{\mathfrak{m}^{n+2}}$，从而 $f - (g_n + u_n)(h_n + v_n) \in \mathfrak{m}^{n+2} R[x]$。

**步骤 4**：由完备性，序列 $\{g_n\}$ 和 $\{h_n\}$ 收敛到 $g, h \in R[x]$，且 $f = gh$，$\bar{g} = \bar{g}_0$，$\bar{h} = \bar{h}_0$。$\square$

### 推论

**推论 1**（根的提升）：若 $f(x) \in R[x]$，$\bar{f}(x)$ 在 $k$ 中有单根 $\bar{a}$，则存在 $a \in R$ 使得 $f(a) = 0$ 且 $a \equiv \bar{a} \pmod{\mathfrak{m}}$。

**证明**：取 $\bar{g}_0(x) = x - \bar{a}$，$\bar{h}_0(x) = \bar{f}(x)/(x - \bar{a})$，应用 Hensel 引理。$\square$

**推论 2**（多项式的因子分解）：完备局部环上的一元多项式环是唯一因子分解整环。

**推论 3**（$\mathbb{Z}_p$ 上的 Hensel 引理）：设 $f(x) \in \mathbb{Z}_p[x]$，$\bar{f}(x) \in \mathbb{F}_p[x]$。若 $\bar{f}(x)$ 在 $\mathbb{F}_p$ 中有分解为互素因子的乘积，则 $f(x)$ 在 $\mathbb{Z}_p$ 中有对应的分解。

**例**：在 $\mathbb{Z}_5$ 中，方程 $x^2 + 1 = 0$ 有解，因为模 $5$ 时 $x^2 + 1 \equiv (x-2)(x-3) \pmod{5}$，且两个因子互素。由 Hensel 引理，存在 $a \in \mathbb{Z}_5$ 使得 $a^2 + 1 = 0$，即 $\sqrt{-1} \in \mathbb{Q}_5$。

**应用**：完备化与 Hensel 引理是代数数论（$p$-adic 数）、代数几何（形式概形）和局部环理论的基本工具。$\square$