# Roth 定理

> **一句话大白话**：对于"好脾气的"代数无理数，Dirichlet 的平方界 $\frac1{q^2}$ 已经是最优——任何想要把指数加到 $2+\varepsilon$ 的逼近，都只有有限多个解能做到。代数数十分"顽固"，很难被过分精确地逼近。
>
> **小例子**：$\sqrt2$ 满足 $|\sqrt2-\frac pq|\ge\frac c{q^2}$ 型下界（这是时域型 Liouv假设），丰富的 $|\sqrt2-\frac pq|<\frac1{q^2}$ 解（由连分数给出，如 $\frac{577}{408}$）其误差总在 $1/q^2$ 量级、不会再小一个数量级到 $1/q^{2.001}$ 的无穷族。

## 一、定理介绍

Roth 定理（1955）是丢番图逼近的最高峰之一（Roth 因之获 1958 Fields 奖）。它断言：对代数无理数 $\alpha$ 和任意 $\varepsilon>0$，不等式 $|\alpha-\frac pq|<\frac1{q^{2+\varepsilon}}$ 只有有限多个有理数解。这使指数 $2$ 成为代数无理数的精确临界指数。

## 二、原理思路

依靠 Roth 引理（近年由 Faltings、Vojta 等推广）。在反证假设下构造无穷多的"过好"逼近，用抽屉原理构造一个 $m$ 元整系数多项式 $P$（在 $(\alpha,\dots,\alpha)$ 有高阶零点大、系数有界）。把逼近点代入，Taylor 展开：逼近假设使主项小，代数数结构性（分数分母下界）使非零有理数不得太小；选取 $m$ 与次数使之矛盾。

## 三、定理的严格表述

设 $\alpha$ 是代数无理数。则对任意 $\varepsilon>0$，不等式
$$\left|\alpha-\frac pq\right|<\frac{1}{q^{2+\varepsilon}}$$
只有有限多个有理数解 $\frac pq$（$q>0$）。

## 四、证明过程

**证明思路（Roth 方法）：**

**步骤 1：反证假设。** 设有无穷多个 $\frac{p_i}{q_i}$ 满足 $|\alpha-\frac{p_i}{q_i}|<q_i^{-(2+\varepsilon)}$，取 $q_i$ 严格递增子列。$\blacksquare$

**步骤 2：构造辅助多项式。** 对给定 $m$，用 Siegel/Dirichlet 引理构造非零整系数多项式 $P(x_1,\dots,x_m)$，关于 $x_i$ 次数 $\le r_i$，且其在 $(\alpha,\dots,\alpha)$ 处的所有 $0\le k_i\le r_i-1$ 阶偏导数为零，系数绝对值有界。这是 Roth 引理的核心。$\blacksquare$

**步骤 3：代入逼近点。** 因 $P(\alpha,\dots,\alpha)=0$，Taylor 展开得
$$P\left(\frac{p_1}{q_1},\dots,\frac{p_m}{q_m}\right)=\sum_{k}\frac1{k_1!\cdots k_m!}\partial^k P(\xi)\prod_i\left(\frac{p_i}{q_i}-\alpha\right)^{k_i}.$$
由逼近假设与系数控制，当 $m$ 充分大时 $\left|P(\frac{p_1}{q_1},\dots,\frac{p_m}{q_m})\right|<1$。$\blacksquare$

**步骤 4：下界与矛盾。** $P(\frac{p_1}{q_1},\dots,\frac{p_m}{q_m})$ 是具有分母 $q_1^{r_1}\cdots q_m^{r_m}$ 的有理数；若非零，则 $\ge\frac1{q_1^{r_1}\cdots q_m^{r_m}}$。选 $m,r_i$（使 $r_i\propto\log q_i$）使此下界大于步骤 3 的上界，矛盾。故非零 $P$ 不可能；即假设不成立，仅有限多个解。$\square$

**注：** Roth 定理是非有效的：证明用反证法且参数选择无法算法化，故不再给出解的个数上界。这是 Roth 定理的主要局限之一。

## 五、应用与意义

Roth 定理是丢番图逼近的基准定理：确定代数无理数精确逼近指数为 2，具普遍性却非有效。它用于：(1) 证明许多 Diophantine 方程只有有限解（结合有效化）；(2) Thue 方程、超椭圆方程的有限性；(3) 亏格数论、线性形式在代数点上的估计。它推广了 Liouville/Thue/Siegel 的结果，并孕育 Vojta 高度理论、与算术几何（子品种定理）深度交融。