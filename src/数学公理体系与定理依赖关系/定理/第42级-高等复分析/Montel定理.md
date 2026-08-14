# Montel 定理

## 一、定理介绍

Montel 定理是复分析中关于正规族（normal family）的核心定理，由 Paul Montel 于 1912 年提出。该定理给出了全纯函数族为正规族的充分条件：局部一致有界的全纯函数族是正规族（即每个序列都有子列一致收敛于紧集上）。

Montel 定理是复分析中紧性论证的基本工具，在 Riemann 映射定理的证明、Picard 定理的证明以及复动力系统的研究中起着关键作用。

## 二、原理思路

**核心思想**：全纯函数的局部一致有界性蕴含等度连续性，从而通过 Arzelà-Ascoli 定理得到正规族。

**关键观察**：
1. 全纯函数满足 Cauchy 估计：$|f'(z)| \leq \frac{M}{r}$（$|f| \leq M$ 在 $D(z, r)$ 上）
2. 局部一致有界性通过 Cauchy 估计给出导数的一致有界性
3. 导数一致有界蕴含 Lipschitz 连续，从而等度连续
4. Arzelà-Ascoli 定理将等度连续性和一致有界性转化为相对紧性

**证明策略**：
- 利用 Cauchy 积分公式建立导数估计
- 通过等度连续性应用 Arzelà-Ascoli 定理
- 对角线方法处理可数稠密子集

## 三、定理的严格表述

**定义（正规族）**：设 $\mathcal{F}$ 是区域 $\Omega \subset \mathbb{C}$ 上的全纯函数族。称 $\mathcal{F}$ 为**正规族**，如果 $\mathcal{F}$ 中每个函数序列都有子列在 $\Omega$ 的任意紧子集上一致收敛（收敛到全纯函数或恒为 $\infty$）。

**定理（Montel）**：设 $\Omega \subset \mathbb{C}$ 是区域，$\mathcal{F}$ 是 $\Omega$ 上的全纯函数族。若 $\mathcal{F}$ 在 $\Omega$ 上**局部一致有界**（即对任意紧集 $K \subset \Omega$，存在 $M_K > 0$ 使得 $|f(z)| \leq M_K$ 对所有 $z \in K$ 和 $f \in \mathcal{F}$ 成立），则 $\mathcal{F}$ 是正规族。

**Montel 定理的加强形式**：

1. **大 Montel 定理**：若 $\mathcal{F}$ 是 $\Omega$ 上的全纯函数族，且存在两个不同的复数值 $a, b$ 使得 $f(z) \neq a$ 且 $f(z) \neq b$ 对所有 $z \in \Omega$ 和 $f \in \mathcal{F}$ 成立，则 $\mathcal{F}$ 是正规族。

2. **等价刻画**：$\mathcal{F}$ 是正规族当且仅当 $\mathcal{F}$ 在 $\Omega$ 的每个紧子集上相对紧（在一致收敛拓扑下）。

## 四、证明过程

**定理（Montel）**：局部一致有界的全纯函数族是正规族。

**证明**：

**步骤 1**：等度连续性。设 $K \subset \Omega$ 是紧集。对任意 $z_0 \in K$，存在 $r > 0$ 使得 $D(z_0, 2r) \subset \Omega$。由局部一致有界性，存在 $M > 0$ 使得 $|f(z)| \leq M$ 对所有 $z \in D(z_0, 2r)$ 和 $f \in \mathcal{F}$ 成立。

由 Cauchy 估计，对任意 $z \in D(z_0, r)$，
$$|f'(z)| \leq \frac{M}{r}$$
对所有 $f \in \mathcal{F}$ 成立。

因此对任意 $z, w \in D(z_0, r)$，
$$|f(z) - f(w)| \leq \frac{M}{r} |z - w|$$

这表明 $\mathcal{F}$ 在 $D(z_0, r)$ 上等度连续。由于 $K$ 可以被有限个这样的圆盘覆盖，$\mathcal{F}$ 在 $K$ 上等度连续。

**步骤 2**：Arzelà-Ascoli 定理。由于 $\mathcal{F}$ 在 $K$ 上一致有界且等度连续，由 Arzelà-Ascoli 定理，$\mathcal{F}$ 在 $K$ 上相对紧（在一致收敛拓扑下）。

**步骤 3**：对角线方法。设 $\{K_n\}$ 是 $\Omega$ 的穷竭紧集序列（$K_n \subset K_{n+1}^\circ$，$\bigcup K_n = \Omega$）。设 $\{f_m\}$ 是 $\mathcal{F}$ 中的序列。

- 在 $K_1$ 上，$\{f_m\}$ 有子列 $\{f_{m,1}\}$ 一致收敛
- 在 $K_2$ 上，$\{f_{m,1}\}$ 有子列 $\{f_{m,2}\}$ 一致收敛
- 依次类推

取对角线子列 $\{f_{n,n}\}$，它在每个 $K_n$ 上一致收敛，因此在 $\Omega$ 的任意紧子集上一致收敛。

**步骤 4**：极限的全纯性。由 Weierstrass 定理，全纯函数序列在紧集上一致收敛的极限是全纯函数。$\square$

**大 Montel 定理的证明思路**：

**步骤 1**：通过 Möbius 变换，可以假设 $a = 0$，$b = 1$。即 $\mathcal{F}$ 中的函数不取 0 和 1。

**步骤 2**：构造 Schottky 定理。对不取 0 和 1 的全纯函数 $f$，Schottky 定理给出 $|f(z)|$ 在 $|z| \leq r$ 上的上界，由 $|f(0)|$ 控制。

**步骤 3**：若 $\mathcal{F}$ 不是正规族，由 Marty 定理，存在序列 $\{f_n\} \subset \mathcal{F}$ 和点 $z_0$ 使得 $f_n^\#(z_0) \to \infty$（$f^\#$ 是球面导数）。

**步骤 4**：通过缩放和 Zalcman 引理，可以构造非恒常数的全纯函数 $g: \mathbb{C} \to \mathbb{C} \setminus \{0, 1\}$，与 Picard 小定理矛盾。$\square$

## 五、应用与意义

Montel 定理在复分析中有广泛应用：

1. **Riemann 映射定理**：Montel 定理用于证明 Riemann 映射定理中存在极值函数的存在性。

2. **Picard 定理**：大 Montel 定理是证明 Picard 大定理的关键工具。

3. **复动力系统**：Julia 集和 Fatou 集的分类依赖正规族理论。

4. **值分布理论**：Nevanlinna 理论中正规族是核心概念。

5. **全纯映射空间**：全纯映射空间的紧性研究使用 Montel 定理。

6. **微分方程**：复常微分方程解的解析延拓和存在性证明中使用 Montel 定理。

Montel 定理的推广包括：Marty 定理（球面导数刻画正规族）、Zalcman 引理（正规族的精细分析）、以及高维复分析中的正规族理论。
