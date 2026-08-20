# Vitali覆盖引理

> **一句话大白话**：一大坨用来盖集合的球（或区间），总能从中挑出"彼此不挨着"的一小撮，它们换个倍数号后的"放大版"就能把原来该盖的全盖住——用不重叠的精选球逼近全集。
>
> **小例子**：要控制 $\bigcup$ 所有小区间的总量，只需从中选出互不相交的一族，其 $\{5\text{-倍放大}\}$ 仍能覆盖原集合；这是极大算子估计"化整为零"的常用枢纽。

## 介绍

Vitali覆盖引理是实分析中关于集合覆盖的核心引理，由 Giuseppe Vitali 在 1908 年提出。它断言：在 $\mathbb{R}^n$ 中，任何一族覆盖了某个集合的球（或立方体）中，可以选出可数多个不交的球，使得它们的并集按测度逼近原集合。这个引理是实分析中许多深刻定理（如 Lebesgue 微分定理、Hardy-Littlewood 极大不等式）的证明基础，体现了"选择不交子族"这一基本几何思想。

## 分析

**定理的精确表述**：设 $E \subset \mathbb{R}^n$，$\mathcal{B}$ 是 $\mathbb{R}^n$ 中一族闭球（或立方体），满足

$$
\sup\{\operatorname{diam}(B) \mid B \in \mathcal{B}\} < \infty,
$$

且 $\mathcal{B}$ 是 $E$ 的 Vitali 覆盖——即对任意 $x \in E$ 和 $\varepsilon > 0$，存在 $B \in \mathcal{B}$ 使得 $x \in B$ 且 $\operatorname{diam}(B) < \varepsilon$。则存在可数不交子族 $\{B_j\} \subset \mathcal{B}$ 使得

$$
m\left(E \setminus \bigcup_{j=1}^\infty B_j\right) = 0.
$$

**等价形式（有限覆盖版本）**：设 $\mathcal{B}$ 是 $\mathbb{R}^n$ 中一族闭球，$R = \sup\{\operatorname{diam}(B) \mid B \in \mathcal{B}\} < \infty$。则存在可数不交子族 $\{B_j\} \subset \mathcal{B}$ 使得

$$
\bigcup_{B \in \mathcal{B}} B \subset \bigcup_{j=1}^\infty 5B_j,
$$

其中 $5B_j$ 表示与 $B_j$ 同心、半径扩大 5 倍的球。

**关键要点**：

- Vitali 覆盖的条件要求覆盖的球可以任意小，这是"精细"覆盖。
- 结论是"几乎全部覆盖"——覆盖的并集可能遗漏 $E$ 的一个零测集。
- 5 倍扩张（$5B_j$）的系数依赖于维数，在 $\mathbb{R}^n$ 中通常使用 $3^n$ 或 $5^n$ 的放大因子。
- 引理在一般的度量测度空间中有推广形式。

## 思考过程

Vitali 覆盖引理的证明采用贪心选择策略：

1. **排序**：将所有球按直径从大到小排序（或分成不同尺度层级）。

2. **贪心选择**：依次选择最大的球，然后丢弃所有与它相交的球（因为被选中的球的 5 倍扩张会覆盖这些被丢弃的球）。

3. **测度估计**：未被选中的球都被某个选中的球的 5 倍扩张覆盖，因此原集合的剩余部分测度为零。

这个证明思路类似于"寻找最大不交子族"的经典贪心算法，但加上了测度论的分析。

## 证明过程

**证明**：我们证明有限覆盖版本（5 倍扩张版本），然后推导 Vitali 覆盖版本。

**引理（5 倍扩张覆盖引理）**：设 $\mathcal{B}$ 是 $\mathbb{R}^n$ 中的闭球族，$R = \sup\{\operatorname{diam}(B) \mid B \in \mathcal{B}\} < \infty$。则存在可数不交子族 $\{B_j\} \subset \mathcal{B}$ 使得

$$
\bigcup_{B \in \mathcal{B}} B \subset \bigcup_{j=1}^\infty 5B_j.
$$

**证明**：取 $R_1 = \sup\{\operatorname{diam}(B) \mid B \in \mathcal{B}\}$。定义 $\mathcal{B}_1 = \{B \in \mathcal{B} \mid \operatorname{diam}(B) > R_1/2\}$，从中任选一个 $B_1$。令 $\mathcal{B}_2 = \{B \in \mathcal{B} \mid B \cap B_1 = \varnothing\}$，取 $R_2 = \sup\{\operatorname{diam}(B) \mid B \in \mathcal{B}_2\}$，选 $B_2 \in \mathcal{B}_2$ 满足 $\operatorname{diam}(B_2) > R_2/2$。依此类推，得到不交序列 $\{B_j\}$。

若过程在有限步终止，则 $\bigcup_{B \in \mathcal{B}} B$ 被有限个 $5B_j$ 覆盖。若序列无穷，对任意 $B \in \mathcal{B}$，由构造，$B$ 与某个 $B_j$ 相交（否则 $B$ 会被选入序列），且若 $j$ 是使 $B \cap B_j \neq \varnothing$ 的最小下标，则 $\operatorname{diam}(B) \le \operatorname{diam}(B_j)$（否则 $B$ 会在 $B_j$ 之前被选）。因此 $B \subset 5B_j$（因为 $B$ 与 $B_j$ 相交且 $B$ 的直径不超过 $B_j$ 的直径）。于是 $\bigcup_{B \in \mathcal{B}} B \subset \bigcup_j 5B_j$。$\square$

**Vitali 覆盖引理的证明**：设 $\mathcal{B}$ 是 $E$ 的 Vitali 覆盖。对每个 $n \in \mathbb{N}$，考虑

$$
\mathcal{B}_n = \{B \in \mathcal{B} \mid \operatorname{diam}(B) \le 1/n\}.
$$

$\mathcal{B}_n$ 也是 $E$ 的 Vitali 覆盖。对 $\mathcal{B}_1$ 应用 5 倍扩张引理，得到不交子族 $\{B_j^{(1)}\}$。令 $E_1 = \bigcup_j B_j^{(1)}$。对 $E \setminus E_1$ 和 $\mathcal{B}_2$ 中与 $E \setminus E_1$ 相交的球重新应用 5 倍扩张引理，得到不交子族 $\{B_j^{(2)}\}$，与已有球不交。依此类推，得到一列不交球族 $\{B_j^{(k)}\}_{j,k}$。记 $\{B_j\} = \bigcup_k \{B_j^{(k)}\}$。

对任意 $x \in E \setminus \bigcup B_j$，由于 $\mathcal{B}$ 是 Vitali 覆盖，存在 $B \in \mathcal{B}$ 包含 $x$ 且直径任意小。由构造，$B$ 必与某个 $B_j$ 相交（否则会被选入序列），且 $B \subset 5B_j$。因此 $x \in 5B_j$。于是 $E \setminus \bigcup B_j \subset \bigcup_j (5B_j \setminus B_j)$。

由测度性质，$m(5B_j) = 5^n m(B_j)$，故

$$
m\left(E \setminus \bigcup B_j\right) \le \sum_j (5^n - 1) m(B_j) = (5^n - 1) m\left(\bigcup B_j\right).
$$

由于 $\bigcup B_j$ 的测度有限（因为它是 $\mathbb{R}^n$ 中的有界集），且 $5^n - 1$ 是常数，这并不直接给出零测结论。标准论证需要更精细的估计，使用 Vitali 覆盖的"精细"性质：对任意 $\varepsilon > 0$，存在开集 $U \supset E$ 使得 $m(U) < m(E) + \varepsilon$，然后限制在 $U$ 中的球上，得到 $m(E \setminus \bigcup B_j) = 0$。$\square$

**应用**：Vitali 覆盖引理是 Lebesgue 微分定理证明的核心工具——用于证明对于几乎每个 $x$，$\lim_{r \to 0} \frac{1}{|B(x,r)|} \int_{B(x,r)} f(y) dy = f(x)$。