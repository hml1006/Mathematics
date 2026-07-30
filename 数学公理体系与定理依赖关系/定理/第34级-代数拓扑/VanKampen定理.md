# Van Kampen定理

## 介绍

Van Kampen定理（也称为 Seifert-van Kampen 定理）是代数拓扑中计算基本群的最重要工具。它断言：如果一个拓扑空间可以表示为两个开子集的并，且交非空道路连通，则空间的基本群可以由这两个子集的基本群通过某种自由积与融合积（amalgamated free product）得到。这个定理提供了从局部基本群构造全局基本群的方法，是计算各种空间（如楔积、环面、射影平面等）基本群的核心工具。

## 分析

**定理的精确表述**：设 $X$ 是拓扑空间，$U, V \subset X$ 是开集，满足 $X = U \cup V$，$U \cap V$ 非空且道路连通。取基点 $x_0 \in U \cap V$。则包含映射 $i: U \cap V \hookrightarrow U$，$j: U \cap V \hookrightarrow V$，$k: U \hookrightarrow X$，$l: V \hookrightarrow X$ 诱导的基本群同态满足：

$$
\pi_1(X, x_0) \cong \pi_1(U, x_0) *_{\pi_1(U \cap V, x_0)} \pi_1(V, x_0),
$$

即 $\pi_1(X)$ 是 $\pi_1(U)$ 和 $\pi_1(V)$ 关于 $\pi_1(U \cap V)$ 的融合自由积，其中融合关系由 $i_*$ 和 $j_*$ 给出。具体地，设

$$
\pi_1(U) = \langle \alpha_1, \ldots, \alpha_m \mid r_1, \ldots, r_p \rangle,
$$
$$
\pi_1(V) = \langle \beta_1, \ldots, \beta_n \mid s_1, \ldots, s_q \rangle,
$$
$$
\pi_1(U \cap V) = \langle \gamma_1, \ldots, \gamma_k \mid t_1, \ldots, t_r \rangle.
$$

则

$$
\pi_1(X) = \langle \alpha_1, \ldots, \alpha_m, \beta_1, \ldots, \beta_n \mid r_1, \ldots, r_p, s_1, \ldots, s_q, i_*(\gamma_l) = j_*(\gamma_l) \text{ 对所有 } l \rangle.
$$

**推论**：若 $U \cap V$ 是单连通的，则 $\pi_1(X) \cong \pi_1(U) * \pi_1(V)$（自由积）。

**关键要点**：

- Van Kampen 定理本质上是一个"分解"定理——将空间的拓扑分解转化为基本群的代数分解。
- 定理要求 $U$ 和 $V$ 是开集，且 $U \cap V$ 道路连通。这些条件都是必要的。
- 当 $U \cap V$ 不连通时，需要更一般的版本（使用 groupoid）。
- 对楔积 $X \vee Y$，$\pi_1(X \vee Y) \cong \pi_1(X) * \pi_1(Y)$。

## 思考过程

Van Kampen 定理的证明基于对 $X$ 中道路的同伦进行分解：

1. 将 $X$ 中的闭道路分解为有限段，每段完全落在 $U$ 或完全落在 $V$ 中。

2. 利用 $U \cap V$ 的道路连通性，在交点处插入"过渡"路径，将道路重写为 $U$ 和 $V$ 中道路的交替拼接。

3. 同伦关系可以分解为 $U$ 内部和 $V$ 内部的同伦，由此得到基本群的表示。

4. 代数上，这对应于自由积上的融合关系。

## 证明过程

**证明**：我们给出 Van Kampen 定理的证明概要。

**步骤 1**：构造同态 $\Phi: \pi_1(U) * \pi_1(V) \to \pi_1(X)$。由包含映射 $k: U \hookrightarrow X$ 和 $l: V \hookrightarrow X$ 诱导的同态 $k_*: \pi_1(U) \to \pi_1(X)$ 和 $l_*: \pi_1(V) \to \pi_1(X)$，由自由积的泛性质，存在唯一的同态 $\Phi: \pi_1(U) * \pi_1(V) \to \pi_1(X)$ 使得 $\Phi|_{\pi_1(U)} = k_*$，$\Phi|_{\pi_1(V)} = l_*$。

**步骤 2**：满射性。任意 $[\gamma] \in \pi_1(X)$，将 $\gamma$ 表示为有限段 $\gamma = \gamma_1 * \gamma_2 * \cdots * \gamma_m$，每段完全落在 $U$ 或 $V$ 中。通过 Lebesgue 数引理，这样的分解存在。在交点处将路径连接起来，得到 $[\gamma] = \Phi([\alpha_1][\beta_1]\cdots)$，其中 $\alpha_i$ 在 $U$ 中，$\beta_i$ 在 $V$ 中。故 $\Phi$ 满射。

**步骤 3**：核的刻画。$\ker \Phi$ 由关系 $i_*(\gamma) = j_*(\gamma)$（对 $[\gamma] \in \pi_1(U \cap V)$）生成。即若 $[\gamma]$ 在 $U \cap V$ 中，则在 $U$ 中看和 $V$ 中看代表同一个元素，这就是融合关系。

**步骤 4**：由同态基本定理，

$$
\pi_1(X) \cong \frac{\pi_1(U) * \pi_1(V)}{\langle i_*(\gamma)j_*(\gamma)^{-1} \rangle} = \pi_1(U) *_{\pi_1(U \cap V)} \pi_1(V).
$$

$\square$

**例子**：
1. **圆周 $S^1$**：将 $S^1$ 分解为两个开弧 $U, V$ 的并，$U \cap V$ 是两个不交开区间（不连通）。Van Kampen 定理不适用。但将 $S^1$ 视为两个开半圆的并，交点有两个连通分支，可以使用 groupoid 版本。

2. **环面 $T^2$**：$T^2 = S^1 \times S^1$，可以分解为 $U = S^1 \times (S^1 \setminus \{p\})$ 和 $V = (S^1 \setminus \{q\}) \times S^1$。$U$ 和 $V$ 都同伦于 $S^1$，$U \cap V$ 同伦于 $S^1 \vee S^1$。计算得 $\pi_1(T^2) \cong \mathbb{Z} \times \mathbb{Z}$。

3. **楔积 $X \vee Y$**：取 $U = X$ 加 $Y$ 的一个小邻域，$V = Y$ 加 $X$ 的一个小邻域，$U \cap V$ 可缩。由 Van Kampen 定理，$\pi_1(X \vee Y) \cong \pi_1(X) * \pi_1(Y)$。