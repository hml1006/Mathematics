# DirichletL函数

> **一句话大白话**：给 $\zeta$ 函数装上"特征滤波器"$\chi(n)$ 得到 $L(s,\chi)=\sum\chi(n)/n^s$，于是素数在不同剩余类里的分布是否均匀，就看它在 $s=1$ 处的行为——关键是 $L(1,\chi)\neq 0$。
>
> **小例子**：对模 $q$ 的 Dirichlet 主特征以外的任意特征 $\chi$，都有 $L(1,\chi)\neq 0$；正是这个结论保证了算数级数里素数对每个剩余类"雨露均沾"。

## 介绍

Dirichlet L 函数是 Dirichlet 特征与 Riemann Zeta 函数的结合，定义为 $L(s, \chi) = \sum_{n=1}^\infty \chi(n) n^{-s}$，其中 $\chi$ 是模 $q$ 的 Dirichlet 特征。L 函数是解析数论中研究素数在算术级数中分布的核心工具，也是类数公式、素数定理在算术级数中的推广等许多重要结果的基础。L 函数的理论深刻揭示了数论与复分析之间的内在联系。

## 分析

**前置依赖**：Riemann Zeta 函数、Dirichlet 特征、群特征标、Euler 乘积。

**定理内容**：
- 对 $\operatorname{Re}(s) > 1$，$L(s, \chi) = \sum_{n=1}^\infty \chi(n) n^{-s}$ 绝对收敛。
- Euler 乘积：$L(s, \chi) = \prod_p (1 - \chi(p) p^{-s})^{-1}$。
- 对非主特征 $\chi$，$L(s, \chi)$ 可解析延拓为整函数。
- 对主特征 $\chi_0$，$L(s, \chi_0)$ 在 $s=1$ 处有单极点，留数为 $\prod_{p \mid q} (1 - p^{-1})$。

**数学内涵**：
- $L(1, \chi) \neq 0$ 对非主特征成立，这是 Dirichlet 定理的核心。
- 类数公式将二次域的类数与 $L(1, \chi)$ 的值联系起来。
- 广义 Riemann 假设（GRH）：$L(s, \chi)$ 的所有非平凡零点位于 $\operatorname{Re}(s) = 1/2$ 上。

**证明策略**：
1. 证明 Euler 乘积公式。
2. 利用 Poisson 求和公式和 theta 函数证明解析延拓和函数方程。
3. 利用 $L(1, \chi) \neq 0$ 的证明和 Dirichlet 定理。

## 思考过程

Dirichlet L 函数是 Zeta 函数的自然推广，其核心思想是将特征标 $\chi(n)$ 的周期性引入级数求和，从而筛选出特定剩余类中的素数。与 $\zeta(s)$ 类似，$L(s, \chi)$ 也具有 Euler 乘积和函数方程，但其性质因 $\chi$ 是否为实特征而有显著差异。

实特征 $\chi$（即 $\chi(n) \in \{\pm 1, 0\}$）对应的 L 函数在 $s=1$ 附近的零点行为需要特别处理——这正是 Dirichlet 定理证明中最困难的部分。对于复特征，利用 $L(1, \chi) = 0$ 与 $L(1, \overline{\chi}) = 0$ 成对出现的事实可以简洁地导出矛盾。

## 证明过程

**定理 1**（Euler 乘积）：对 $\operatorname{Re}(s) > 1$，
$$L(s, \chi) = \prod_p \frac{1}{1 - \chi(p) p^{-s}}$$

**证明**：与 $\zeta(s)$ 的 Euler 乘积类似，利用 $\chi$ 的完全积性：
$$\prod_p \frac{1}{1 - \chi(p)p^{-s}} = \prod_p \sum_{k=0}^\infty \chi(p)^k p^{-ks} = \sum_{n=1}^\infty \chi(n) n^{-s} = L(s, \chi)$$
其中利用了 $\chi$ 的完全积性 $\chi(n) = \prod_p \chi(p)^{e_p}$。$\square$

**定理 2**（解析延拓）：对非主特征 $\chi$，$L(s, \chi)$ 可解析延拓为整个复平面上的整函数。

**证明**：利用部分求和（Abel 求和）：
$$L(s, \chi) = \sum_{n=1}^\infty \chi(n) n^{-s} = s \int_1^\infty S(x) x^{-s-1} dx$$
其中 $S(x) = \sum_{n \leq x} \chi(n)$。由于 $\chi$ 是非主特征，$\sum_{n=1}^q \chi(n) = 0$，故 $S(x)$ 有界（$|S(x)| \leq \varphi(q)$）。因此积分对 $\operatorname{Re}(s) > 0$ 收敛，给出解析延拓。再通过函数方程延拓到整个复平面。$\square$

**定理 3**（函数方程）：设 $\chi$ 是本原特征模 $q$，定义
$$\Lambda(s, \chi) = \left(\frac{q}{\pi}\right)^{s/2} \Gamma\left(\frac{s + \delta}{2}\right) L(s, \chi)$$
其中 $\delta = 0$ 若 $\chi(-1) = 1$，$\delta = 1$ 若 $\chi(-1) = -1$。则
$$\Lambda(s, \chi) = \varepsilon(\chi) q^{1/2-s} \Lambda(1-s, \overline{\chi})$$
其中 $|\varepsilon(\chi)| = 1$ 是 Gauss 和相关的常数。$\square$

**定理 4**（$L(1, \chi) \neq 0$）：对非主特征 $\chi$，$L(1, \chi) \neq 0$。

**证明**：考虑乘积
$$\prod_{\chi} L(s, \chi) = \prod_p \prod_{\chi} \frac{1}{1 - \chi(p)p^{-s}}$$

若 $\chi$ 是实特征且 $L(1, \chi) = 0$，则 $L(s, \chi)$ 在 $s=1$ 处有零点，导致乘积在 $s=1$ 处为零，但 $\prod_{\chi} L(s, \chi)$ 在 $s=1$ 处的极点阶数可计算，导出矛盾。对复特征，若 $L(1, \chi) = 0$，则 $L(1, \overline{\chi}) = 0$，零点阶数至少为 2，同样矛盾。$\square$