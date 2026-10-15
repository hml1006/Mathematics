# Kronecker 定理

> **一句话大白话**：一个代数整数，如果它的所有共轭的模长都不超过 $1$，那它一定是个单位根——没有"模都不大却永远转不回原地"的代数整数。

> **小例子**：$\alpha=\frac{1+i\sqrt3}{2}$ 的共轭是 $\frac{1-i\sqrt3}{2}$，两者的模都是 $1$，而 $\alpha^3=-1$、$\alpha^6=1$，确是单位根。反之 $2$ 的共轭模为 $2>1$，不受此定理约束。

## 一、定理介绍

> **前置依赖**：代数整数、极小多项式与共轭、范数与多项式系数、单位根（概念）、代数整数环（概念）。

Kronecker 定理（Leopold Kronecker，1857）是代数数论与丢番图逼近中的一条基本判别准则：若代数整数 $\alpha$ 的每个 Galois 共轭的绝对值都不超过 $1$，则 $\alpha=0$ 或 $\alpha$ 是单位根（特别地当其所有共轭模都等于 $1$ 时必为单位根）。提出它源于 Kronecker 对代数整数与单位群的研究：他想刻画那些"在全部嵌入下都不增长"的代数整数。这条定理给出了一个极简的判别条件——只需检查模长，无需解方程——因此成为数域单位群理论中的关键引理。它在 Dirichlet 单位定理中用于证明对数嵌入的核恰为单位根群，在代数数论、代数动力系统（用于判定整数矩阵的特征值是否为根）、以及多项式的根分布研究中反复出现。

## 二、原理思路

1. 设 $\alpha$ 为 $d$ 次代数整数，共轭为 $\alpha_1=\alpha,\alpha_2,\dots,\alpha_d$，且 $|\alpha_i|\le1$。
2. 对每个 $k\ge1$，$\alpha^k$ 仍是次数 $\le d$ 的代数整数，其共轭为 $\alpha_i^k$，模长仍 $\le1$；于是 $\alpha^k$ 的极小多项式首一、整系数，且每个系数作为共轭的初等对称函数被 $\binom{d}{j}$ 界住。
3. 首一整系数、次数 $\le d$、系数有界的多项式只有有限多个，故全体 $P_k$ 只有有限多个；而 $\alpha^k$ 恒为 $P_k$ 的根，于是 $\{\alpha^k\}$ 是有限集，必有 $\alpha^m=\alpha^n$，当 $\alpha\neq0$ 时即得 $\alpha^{m-n}=1$。

## 三、定理的严格表述

设 $\alpha$ 是代数整数，$\alpha_1=\alpha,\alpha_2,\dots,\alpha_d$ 为其全部 Galois 共轭（$d=[\mathbb{Q}(\alpha):\mathbb{Q}]$，计重数）。若
$$
|\alpha_i|\le 1\qquad(i=1,\dots,d),
$$
则 $\alpha=0$ 或 $\alpha$ 是单位根（即存在正整数 $m$ 使 $\alpha^m=1$）。特别地，若对所有 $i$ 都有 $|\alpha_i|=1$，则 $\alpha$ 必为单位根。

## 四、证明过程

**证明：**

**步骤 1：$\alpha^k$ 的共轭与其极小多项式。** 固定 $k\ge1$。$\alpha^k\in\mathbb{Z}[\alpha]$ 是代数整数，且 $\mathbb{Q}(\alpha^k)\subseteq\mathbb{Q}(\alpha)$，故 $[\mathbb{Q}(\alpha^k):\mathbb{Q}]\le d$。设 $P_k$ 为 $\alpha^k$ 的极小多项式，则 $P_k$ 首一、次数 $\le d$、系数为整数（代数整数的极小多项式整系数）。$P_k$ 的每个根都可写成某个 $\alpha_i^k$：因为对任何嵌入 $\sigma:\mathbb{Q}(\alpha)\hookrightarrow\mathbb{C}$ 有 $\sigma(\alpha^k)=\sigma(\alpha)^k=\alpha_i^k$。

**步骤 2：系数的一致有界性。** 由 $|\alpha_i|\le1$ 得 $|\alpha_i^k|\le1$。设 $P_k(x)=x^{D}+\sum_{j=0}^{D-1}c_{k,j}x^{j}$（$D=\deg P_k\le d$），则 $-c_{k,j}$ 是 $\alpha^k$ 的 $D-j$ 个共轭之积的和，故
$$
|c_{k,j}|\le \binom{D}{D-j}\le \binom{d}{\lfloor d/2\rfloor}=:B .
$$
因 $c_{k,j}\in\mathbb{Z}$，故 $c_{k,j}\in\mathbb{Z}\cap[-B,B]$。

**步骤 3：只有有限多个候选多项式。** 首一、次数 $\le d$、每个系数取自有限集 $\mathbb{Z}\cap[-B,B]$ 的整系数多项式只有有限多个。设这样的多项式共有 $M$ 个，则 $\{P_k:k\ge1\}\subseteq\{Q_1,\dots,Q_M\}$，其中 $Q_1,\dots,Q_M$ 为全部候选。

**步骤 4：$\{\alpha^k\}$ 是有限集。** 对每个 $k$，$\alpha^k$ 是 $P_k$ 的根，而 $P_k$ 必等于某个 $Q_\ell$，$Q_\ell$ 只有 $\deg Q_\ell\le d$ 个根。于是
$$
\{\alpha^k:k\ge1\}\subseteq\bigcup_{\ell=1}^{M}\{\text{$Q_\ell$ 的全部根}\},
$$
右端是有限集（至多 $Md$ 个元素）。

**步骤 5：得单位根。** 由步骤 4，$\{\alpha^k:k\ge1\}$ 有限，故存在 $m>n\ge1$ 使 $\alpha^m=\alpha^n$。若 $\alpha\neq0$，两边同除 $\alpha^n$ 得 $\alpha^{m-n}=1$，故 $\alpha$ 是单位根；若 $\alpha=0$，则为定理所述的平凡情形。$\square$

## 五、应用与意义

- 它是 Dirichlet 单位定理的关键引理：对数嵌入的核（所有嵌入模长为 $1$ 的单位）恰为数域的单位根群。
- 它给出"单位是否为单位根"的最简判别，避免了解方程，是数域单位群计算的实用工具。
- 在代数动力系统中，用它判定整数矩阵的特征值是否为根（若特征值及其共轭模都 $\le1$ 则是根）。
- 在丢番图逼近中，它与 Kronecker 逼近定理（同名的另一个结果）共同构成"代数数与逼近"的基本工具集。
- 它体现了"有界根的有限性"思想，是 Chebyshev、Mahler 测度与多项式高度理论中同类论证的原型。

## 课堂问答

**老师**：Kronecker 定理的判据是什么？为什么它如此简洁？

**学生**：若代数整数 $\alpha$ 的全部 Galois 共轭满足 $|\alpha_i|\le1$，则 $\alpha=0$ 或 $\alpha$ 是单位根。简洁之处在于只看模长、不解方程——因为一旦所有共轭模长有界，"$\alpha^k$ 的可能取值"就被迫落在有限集里。

**老师（追问）**：这个有限性是怎么逼出来的？

**学生**：对每个 $k$，$\alpha^k$ 是次数 $\le d$ 的代数整数，其极小多项式首一整系数，系数是共轭的初等对称函数，满足
$$
|c_{k,j}|\le\binom{d}{\lfloor d/2\rfloor}=B.
$$
首一、次数 $\le d$、系数取自 $\mathbb{Z}\cap[-B,B]$ 的多项式只有有限多个，故 $\{\alpha^k\}$ 是有限集，必有 $\alpha^m=\alpha^n$（$m>n$），非零时即 $\alpha^{m-n}=1$。

**老师（拓展）**：它在单位群理论里扮演什么角色？

**学生**：它正是 Dirichlet 单位定理中"对数嵌入的核为单位根群"这一步：若对一切嵌入 $|\sigma(\alpha)|=1$，则 $\alpha$ 是单位根；它也可用于判定整数矩阵特征值是否为根。误区是把它与同名的 Kronecker 逼近定理混为一谈，后者讲的是丢番图逼近，与本定理无关。

## 相关条目

- [Dirichlet 单位定理](./Dirichlet单位定理.md)：本定理用于识别对数嵌入的核为单位根群。
- [Kronecker-Weber 定理](./Kronecker-Weber定理.md)：同属 Kronecker 的定理但内容不同（刻画 $\mathbb{Q}$ 的 Abel 扩张），可对照理解。
- [数域整数环是 Dedekind 整环](./数域整数环是Dedekind整环.md)：提供代数整数与极小多项式的环论背景。
- [理想唯一分解定理](./理想唯一分解定理.md)：数域中代数整数因子分解的结构定理，与单位群理论配合。
- [Dirichlet 单位定理（第53级-代数数论）](../第53级-代数数论/Dirichlet单位定理.md)：其中同样引用 Kronecker 定理判定单位根，可交叉参考。
