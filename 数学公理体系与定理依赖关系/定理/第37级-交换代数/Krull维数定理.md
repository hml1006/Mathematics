# Krull维数定理

## 介绍

Krull维数定理（Krull's Dimension Theorem）是交换代数中关于环的维数理论的核心结果，由沃尔夫冈·克鲁尔于 20 世纪早期建立。该定理给出了诺特环的 Krull 维数与其素理想链长度之间的关系，特别是关于多项式环的维数、素理想的高度与生成元个数之间的关系。Krull维数定理是交换代数中维数理论的基础，为代数几何中代数簇的维数概念提供了代数的严格定义。

## 分析

**前置依赖**：交换代数、诺特环、素理想、局部环、整扩张。

**数学内涵**：

**定理内容**：

1. **主理想定理**（Krull's Principal Ideal Theorem）：设 $R$ 是诺特环，$a \in R$ 不是零因子也不是可逆元。则包含 $a$ 的每个极小素理想 $\mathfrak{p}$ 的高度为 1（即 $\operatorname{ht} \mathfrak{p} = 1$）。

2. **一般 Krull 维数定理**：设 $R$ 是诺特环，$I = \langle a_1, \ldots, a_r \rangle$ 是由 $r$ 个元素生成的理想。则 $I$ 的每个极小素理想 $\mathfrak{p}$ 满足 $\operatorname{ht} \mathfrak{p} \le r$。

3. **多项式环的维数**：$\dim R[x] = \dim R + 1$。

**数学内涵**：Krull维数定理揭示了环的维数（素理想链的最大长度）与生成元个数之间的深刻关系，是交换代数中维数理论的基础。

**证明策略**：利用局部化将问题化为局部环的情形，通过整扩张和 Going-up 定理分析维数，利用诺特环的准素分解性质。

## 思考过程

Krull维数定理的直观意义是：一个由 $r$ 个元素生成的理想，其"最小"的素理想（即极小素理想）的高度不超过 $r$。特别地，由一个非零非单位元素生成的理想，其极小素理想的高度为 1——也就是说，在素理想链中，这个素理想最多只能覆盖一个"层次"。

在代数几何中，Krull 维数对应代数簇的几何维数。主理想定理对应于：一个超曲面（由一个方程定义）的每个不可约分支的余维数为 1。

多项式环的维数公式 $\dim R[x] = \dim R + 1$ 是直观的：添加一个变量增加一个维数。

## 证明过程

### 主理想定理

**引理 1**：设 $R$ 是诺特环，$a \in R$ 不是零因子。则 $\operatorname{ht}(\mathfrak{p}) = 1$ 对包含 $a$ 的每个极小素理想 $\mathfrak{p}$ 成立。

**证明**：

**步骤 1**：设 $\mathfrak{p}$ 是包含 $a$ 的极小素理想。考虑局部化 $R_{\mathfrak{p}}$，其极大理想为 $\mathfrak{p} R_{\mathfrak{p}}$。需要证明 $\dim R_{\mathfrak{p}} = 1$。

**步骤 2**：$\mathfrak{p} R_{\mathfrak{p}}$ 是 $R_{\mathfrak{p}}$ 的唯一的素理想（因为 $\mathfrak{p}$ 是 $R$ 中包含 $a$ 的极小素理想）。由诺特性，$R_{\mathfrak{p}}$ 中每个元素 $b$ 满足 $\mathfrak{p} R_{\mathfrak{p}} = \sqrt{\langle b \rangle}$ 或更小。

**步骤 3**：由于 $a$ 不是零因子，$a$ 在 $R_{\mathfrak{p}}$ 中也不是零因子。考虑 $R_{\mathfrak{p}}/\langle a \rangle$，其每个素理想对应 $R_{\mathfrak{p}}$ 中包含 $a$ 的素理想。由 $\mathfrak{p}$ 的极小性，$R_{\mathfrak{p}}/\langle a \rangle$ 中只有零维的素理想。因此 $\dim R_{\mathfrak{p}} = 1$。$\square$

### 一般 Krull 维数定理

**定理 1**（Krull 维数定理）：设 $R$ 是诺特环，$I = \langle a_1, \ldots, a_r \rangle$ 是由 $r$ 个元素生成的理想。则对 $I$ 的每个极小素理想 $\mathfrak{p}$，$\operatorname{ht} \mathfrak{p} \le r$。

**证明**：对 $r$ 归纳。

$r = 1$ 时即主理想定理。

假设对 $r-1$ 成立。设 $\mathfrak{p}$ 是 $I = \langle a_1, \ldots, a_r \rangle$ 的极小素理想，$\mathfrak{p}_0 \subsetneq \mathfrak{p}_1 \subsetneq \cdots \subsetneq \mathfrak{p}_n = \mathfrak{p}$ 是长度为 $n$ 的素理想链，$n = \operatorname{ht} \mathfrak{p}$。

**步骤 1**：不妨设 $\mathfrak{p}$ 是极大理想（否则考虑局部化）。由 $\mathfrak{p}$ 的极小性，$\mathfrak{p}$ 是包含 $I$ 的极小素理想，故 $\mathfrak{p} = \sqrt{I}$（在 $R_{\mathfrak{p}}$ 中）。

**步骤 2**：存在 $a_1 \notin \mathfrak{p}_1$（否则 $a_1$ 属于所有 $\mathfrak{p}_i$，从而 $\mathfrak{p}$ 也包含 $\langle a_2, \ldots, a_r \rangle$ 的极小素理想，由归纳假设，$n \le r-1$）。

**步骤 3**：考虑 $R' = R/\mathfrak{p}_0$，$\bar{\mathfrak{p}}_i = \mathfrak{p}_i/\mathfrak{p}_0$。在 $R'$ 中，$\bar{\mathfrak{p}}_1$ 是包含 $\bar{a}_1$ 的极小素理想，故 $\operatorname{ht} \bar{\mathfrak{p}}_1 = 1$。

**步骤 4**：在 $R'/\langle \bar{a}_1 \rangle$ 中，$\bar{\mathfrak{p}}_n = \mathfrak{p}/\mathfrak{p}_0$ 是包含 $\bar{a}_2, \ldots, \bar{a}_r$ 的像的极小素理想。由归纳假设，$\bar{\mathfrak{p}}_n$ 在 $R'/\langle \bar{a}_1 \rangle$ 中的高度 $\le r-1$。

**步骤 5**：因此 $n = \operatorname{ht} \mathfrak{p} = \operatorname{ht} \mathfrak{p}_0 + \operatorname{ht}(\mathfrak{p}/\mathfrak{p}_0) \le 0 + 1 + (r-1) = r$。$\square$

### 多项式环的维数

**定理 2**：设 $R$ 是诺特环，则 $\dim R[x] = \dim R + 1$。

**证明**：

**步骤 1**：$\dim R[x] \ge \dim R + 1$。取 $R$ 中的素理想链 $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_n$，则 $\mathfrak{p}_0[x] \subsetneq \cdots \subsetneq \mathfrak{p}_n[x] \subsetneq \mathfrak{p}_n[x] + \langle x \rangle$ 是 $R[x]$ 中的长度为 $n+1$ 的素理想链。

**步骤 2**：$\dim R[x] \le \dim R + 1$。设 $\mathfrak{q}_0 \subsetneq \cdots \subsetneq \mathfrak{q}_m$ 是 $R[x]$ 中的素理想链。令 $\mathfrak{p}_i = \mathfrak{q}_i \cap R$。则 $\mathfrak{p}_i$ 是 $R$ 中的素理想，且 $\mathfrak{p}_i \subseteq \mathfrak{p}_{i+1}$。

**步骤 3**：若所有 $\mathfrak{p}_i$ 都相同，则 $\mathfrak{q}_i$ 是 $R[x]$ 中收缩到同一个 $\mathfrak{p}$ 的素理想。此时 $\mathfrak{q}_i/\mathfrak{p}[x]$ 是 $k(\mathfrak{p})[x]$ 中的素理想，其中 $k(\mathfrak{p})$ 是域。由于 $k(\mathfrak{p})[x]$ 的维数为 1，链长最多为 1。

**步骤 4**：若 $\mathfrak{p}_i$ 不全相同，则链长最多为 $\dim R + 1$（因为 $\mathfrak{p}_i$ 的链长最多为 $\dim R$，且每个 $\mathfrak{p}_i$ 至多对应一个额外的 $R[x]$ 中的素理想）。$\square$

### 推论

**推论 1**：$\dim k[x_1, \ldots, x_n] = n$，其中 $k$ 是域。

**证明**：反复应用定理 2，$\dim k[x_1, \ldots, x_n] = \dim k + n = 0 + n = n$。$\square$

**推论 2**（局部环的维数）：设 $(R, \mathfrak{m})$ 是诺特局部环，则 $\dim R$ 等于 $\mathfrak{m}$ 的极小生成元个数的最小值（即 $R$ 的嵌入维数）。

**定义**：$R$ 称为**正则局部环**，如果 $\dim R = \dim_{R/\mathfrak{m}} \mathfrak{m}/\mathfrak{m}^2$（即嵌入维数等于 Krull 维数）。

**应用**：Krull维数定理是交换代数中维数理论的基石，广泛应用于代数几何（代数簇的维数）、局部环理论（正则性判定）和交换环的分类。$\square$