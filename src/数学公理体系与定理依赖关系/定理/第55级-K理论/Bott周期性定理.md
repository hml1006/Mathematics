# Bott 周期性定理

> **一句话大白话**：向量丛分到一定程度后又"转回原点"——复 K 理论每 2 步轮一周、实 K 理论每 8 步轮一周，分类表其实是按周期排版的。
>
> **小例子**：复情形 $\widetilde K(S^n)\cong\mathbb{Z}$（$n$ 为偶数）而 $\cong0$（$n$ 为奇数），由此 K$^*$ 以 2 为周期；实 KO 理论则以 8 为周期。

## 一、定理介绍

> **前置依赖**：拓扑 K 理论与约化 K 群、稳定酉群的同伦群、clutching 构造与 Hopf 线丛、Morse 理论、环路空间与分类空间

Bott 周期性定理是拓扑 K 理论中最深刻的结果之一，由 Raoul Bott 于 1957 年在研究 Lie 群的同伦群时发现。该定理揭示了 K 理论具有惊人的周期性结构：复 K 理论的周期为 2，实 K 理论（KO 理论）的周期为 8。

这一发现不仅简化了 K 理论的计算，而且在指标定理、稳定同伦论和数学物理中都有深远影响。Bott 因此项工作及其他贡献获得了 1993 年 Wolf 数学奖。

## 二、原理思路

### 核心思想

Bott 周期性的本质在于酉群（或正交群）的稳定同伦性质。关键观察是：

1. **稳定酉群**：考虑包含映射 $U(n) \hookrightarrow U(n+1)$，当 $n \to \infty$ 时，同伦群 $\pi_k(U(n))$ 在 $n$ 足够大时稳定。

2. **分类空间**：酉群 $U$ 的分类空间 $BU$ 满足 $\Omega^2 BU \simeq BU \times \mathbb{Z}$，其中 $\Omega$ 表示环路空间。

3. **Clutching 构造**：通过球面上的向量丛的 clutching 构造，将 $\tilde{K}(S^2)$ 与 $\tilde{K}(X)$ 联系起来。

### 证明策略

有多种证明方法：
- **Bott 的原始证明**：使用 Morse 理论研究酉群上的测地流
- **Atiyah-Bott 证明**：使用代数拓扑和 K 理论本身的方法
- **Atiyah-Singer 证明**：使用指标定理
- **初等证明**：使用显式的 clutching 函数构造

## 三、定理的严格表述

**定理 1（复 Bott 周期性）** 对于任意紧 Hausdorff 空间 $X$，存在自然同构：
$$\beta: K(X) \xrightarrow{\cong} K^{-2}(X) = \tilde{K}(\Sigma^2 X)$$
等价地，对于约化 K 理论：
$$\tilde{K}(X) \cong \tilde{K}(S^2 \wedge X)$$
其中 $S^2 \wedge X$ 表示 $S^2$ 与 $X$ 的_smash_积。

**定理 2（Bott 同构的显式构造）** Bott 同构 $\beta$ 可以通过与生成元 $b \in \tilde{K}(S^2) \cong \mathbb{Z}$ 的外部积来定义：
$$\beta(x) = b \otimes x$$
其中 $b = [H] - 1$，$H$ 为 $S^2 \cong \mathbb{CP}^1$ 上的 Hopf 线丛。

**定理 3（稳定同伦版本）** 稳定酉群 $U = \varinjlim U(n)$ 满足：
$$\pi_k(U) \cong \begin{cases} \mathbb{Z} & k \text{ 为奇数} \\ 0 & k \text{ 为偶数} \end{cases}$$
且环路空间满足同伦等价：
$$\Omega U \simeq \mathbb{Z} \times BU$$
$$\Omega^2(\mathbb{Z} \times BU) \simeq \mathbb{Z} \times BU$$

**定理 4（实 Bott 周期性）** 对于实 K 理论 $KO$，存在自然同构：
$$KO(X) \cong KO^{-8}(X)$$
即实 K 理论的周期为 8。具体地，对于 $k = 0, 1, \ldots, 7$：
$$\tilde{KO}(S^k \wedge X) \cong \tilde{KO}^{-k}(X)$$
且稳定正交群 $O = \varinjlim O(n)$ 的同伦群满足 8-周期性：
$$\pi_k(O) \cong \begin{cases} \mathbb{Z}_2 & k \equiv 0, 1 \pmod{8} \\ \mathbb{Z} & k \equiv 3, 7 \pmod{8} \\ 0 & k \equiv 2, 4, 5, 6 \pmod{8} \end{cases}$$

## 四、证明过程

### 复 Bott 周期性的证明（Atiyah-Bott 方法）

**步骤 1：约化到球面**

首先证明对于任意紧空间 $X$，Bott 映射
$$\beta: \tilde{K}(X) \to \tilde{K}(S^2 \wedge X)$$
$$\beta([E] - [F]) = ([H] - 1) \otimes ([E] - [F])$$
是良定义的同态。

**步骤 2：计算 $\tilde{K}(S^2)$**

利用 clutching 构造计算 $\tilde{K}(S^2)$：
- 将 $S^2$ 分解为两个半球 $D_+$ 和 $D_-$，交集为赤道 $S^1$
- $S^2$ 上的向量丛由赤道上的转移函数 $f: S^1 \to GL(n, \mathbb{C})$ 决定
- 由于 $D_\pm$ 可缩，丛在半球上平凡
- 因此 $\text{Vect}_n(S^2) \cong \pi_1(GL(n, \mathbb{C})) \cong \pi_1(U(n)) \cong \mathbb{Z}$

对于 $n = 1$，生成元为 Hopf 丛 $H$，其转移函数为 $z \mapsto z$（恒等映射 $S^1 \to S^1 \subset \mathbb{C}^*$）。

因此 $\tilde{K}(S^2) \cong \mathbb{Z}$，由 $[H] - 1$ 生成。

**步骤 3：Bott 映射是单射**

**关键引理**：若 $E \to S^2 \wedge X$ 是向量丛，则存在 $N$ 使得 $E \oplus N\mathbb{C} \cong \beta(F)$ 对某个 $F \in K(X)$。

**证明思路**：
- 利用 $S^2 \wedge X$ 的细胞分解
- 通过归纳法构造原像
- 使用向量丛的扩展性质

**步骤 4：Bott 映射是满射**

构造逆映射 $\beta^{-1}: \tilde{K}(S^2 \wedge X) \to \tilde{K}(X)$。

**方法**：使用 Thom 同构定理的 K 理论版本。

考虑 $S^2$ 作为 $\mathbb{C} \cup \{\infty\}$，$S^2 \wedge X$ 可以看作 $X$ 的单点紧化与 $S^2$ 的_smash_积。

定义 $\beta^{-1}$ 为：
$$\beta^{-1}([E]) = \text{index of family of Dirac operators on } S^2$$

更初等地，可以使用"积分"映射：
$$\beta^{-1}: \tilde{K}(S^2 \wedge X) \to \tilde{K}(X)$$
通过将 $S^2$ 上的 K 类"推前"到点来定义。

**步骤 5：验证互逆**

需要证明 $\beta \circ \beta^{-1} = \text{id}$ 且 $\beta^{-1} \circ \beta = \text{id}$。

这可以通过计算生成元的像来完成：
- $\beta^{-1}(\beta(x)) = \beta^{-1}(b \otimes x) = x \cdot \beta^{-1}(b) = x \cdot 1 = x$
- 其中使用了 $\beta^{-1}(b) = 1$，这来自 Hopf 丛的指标计算

### Morse 理论证明（Bott 原始方法）

**步骤 1：定义能量泛函**

在酉群 $U(n)$ 上定义能量泛函（或长度泛函）：
$$E(\gamma) = \int_0^1 \|\dot{\gamma}(t)\|^2 dt$$
其中 $\gamma: [0, 1] \to U(n)$ 是路径。

**步骤 2：研究临界点**

临界点对应于测地线。在 $U(n)$ 上，测地线具有形式：
$$\gamma(t) = \exp(tA) \cdot \gamma(0)$$
其中 $A$ 是反 Hermite 矩阵。

**步骤 3：计算 Morse 指数**

对于每个临界点，计算 Morse 指数（负特征方向的数量）。

**关键计算**：对于从 $I$ 到 $-I$ 的测地线，Morse 指数为 $2k+1$（奇数）。

**步骤 4：应用 Morse 理论**

由 Morse 理论，环路空间 $\Omega U(n)$ 的同伦类型由临界点决定。由于所有 Morse 指数都是奇数，细胞分解只有奇数维细胞。

取极限 $n \to \infty$，得到：
$$\Omega U \simeq \mathbb{Z} \times BU$$
其中 $\mathbb{Z}$ 对应于不同连通分支（由 $\pi_0(\Omega U) = \pi_1(U) = \mathbb{Z}$）。

再次取环路空间：
$$\Omega^2(\mathbb{Z} \times BU) \simeq \Omega U \simeq \mathbb{Z} \times BU$$

这证明了 Bott 周期性。

## 五、应用与意义

### 1. K 理论的计算

Bott 周期性极大地简化了 K 群的计算。例如：
$$K^{-n}(pt) = \tilde{K}(S^n) \cong \begin{cases} \mathbb{Z} & n \text{ 为偶数} \\ 0 & n \text{ 为奇数} \end{cases}$$

### 2. 稳定同伦论

Bott 周期性是稳定同伦论的基础之一。它提供了计算球面稳定同伦群的重要工具：
$$\pi_k^s(S^0) \otimes \mathbb{Q} \cong \begin{cases} \mathbb{Q} & k = 0 \\ 0 & k > 0 \end{cases}$$

### 3. 指标定理

在 Atiyah-Singer 指标定理的 K 理论证明中，Bott 周期性用于构造 Thom 同构和推前映射。

### 4. 算子 K 理论

在算子代数中，Bott 周期性对应于 C*-代数的周期性：
$$K_0(A) \cong K_0(A \otimes C_0(\mathbb{R}^2))$$
$$K_i(A) \cong K_{i+2}(A)$$
其中 $C_0(\mathbb{R}^2)$ 是 $\mathbb{R}^2$ 上消失于无穷远的连续函数代数。

### 5. 物理学应用

在弦理论中，Bott 周期性解释了为什么 Type II 弦理论有 10 维：
- 超对称要求时空维数与 Bott 周期相关
- D-膜电荷的 K 理论分类依赖于 Bott 周期性

在凝聚态物理中，实 K 理论的 8-周期性解释了拓扑绝缘体的分类：
- 二维拓扑绝缘体由 $\mathbb{Z}$ 分类
- 三维拓扑绝缘体由 $\mathbb{Z}_2$ 分类
- 这与 $KO^{-n}(pt)$ 的值完全一致

### 6. 广义上同调理论

Bott 周期性使得 K 理论成为一个周期广义上同调理论，这启发了其他广义上同调理论的构造，如：
- 椭圆上同调（周期为 576）
- 模形式上同调
- 代数 K 理论

### 7. 代数几何

在代数几何中，Bott 周期性对应于 Perfectoid 空间和 prismatic 上同调中的周期性现象，这是当代算术几何研究的前沿。
