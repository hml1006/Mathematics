# Kolmogorov 0-1 律

## 介绍

Kolmogorov 0-1 律（Kolmogorov's Zero-One Law）是概率论中关于尾事件（tail events）的深刻结论，由苏联数学家安德雷·柯尔莫哥洛夫（Andrey Kolmogorov）提出。该定律指出：对于独立随机变量序列，任何尾事件的概率要么为 $0$，要么为 $1$。尾事件是指那些不依赖于序列中任意有限个随机变量取值的事件，例如"级数 $\sum X_n$ 收敛"、"$\limsup X_n$ 的取值"等。这一结论揭示了独立序列的"长期行为"具有确定性——要么几乎必然发生，要么几乎不可能发生。

## 分析

**前置依赖**：博雷尔-坎泰利引理、尾 $\sigma$-代数的定义、独立性的概念。

**数学内涵**：
- 设 $X_1, X_2, \ldots$ 是随机变量序列，$\mathcal{F}_n = \sigma(X_{n+1}, X_{n+2}, \ldots)$ 是尾部 $\sigma$-代数。
- 尾 $\sigma$-代数 $\mathcal{T} = \bigcap_{n=1}^\infty \mathcal{F}_n$。
- 尾事件 $A \in \mathcal{T}$ 满足：$A$ 的发生与否不依赖于 $X_1, \ldots, X_n$ 的取值（对任意 $n$）。
- Kolmogorov 0-1 律：若 $X_1, X_2, \ldots$ 独立，则对任意 $A \in \mathcal{T}$，$P(A) \in \{0, 1\}$。

**结构**：
1. 证明尾事件与任意有限个随机变量生成的事件独立。
2. 利用 $\pi$-$\lambda$ 引理或单调类定理证明尾事件与自身独立。
3. 由 $P(A) = P(A \cap A) = P(A)^2$ 得 $P(A) \in \{0, 1\}$。

## 思考过程

Kolmogorov 0-1 律的证明思路非常巧妙。核心想法是：如果一个尾事件 $A$ 不依赖于前 $n$ 个随机变量，那么 $A$ 与 $\sigma(X_1, \ldots, X_n)$ 独立。由于这一性质对任意 $n$ 成立，$A$ 与 $\sigma(X_1, X_2, \ldots)$ 独立——即 $A$ 与自身独立！因此 $P(A) = P(A \cap A) = P(A)P(A) = P(A)^2$，解得 $P(A) = 0$ 或 $1$。

## 证明过程

**定理**（Kolmogorov 0-1 律）：设 $X_1, X_2, \ldots$ 是独立随机变量序列，$\mathcal{T} = \bigcap_{n=1}^\infty \sigma(X_{n+1}, X_{n+2}, \ldots)$ 是尾 $\sigma$-代数。则对任意 $A \in \mathcal{T}$，$P(A) \in \{0, 1\}$。

**证明**：

### 1. 准备工作

对任意 $n$，$A \in \mathcal{T} \subseteq \sigma(X_{n+1}, X_{n+2}, \ldots)$，因此 $A$ 与 $\sigma(X_1, \ldots, X_n)$ 独立（由 $X_i$ 的独立性）。

### 2. 构造代数

令 $\mathcal{A} = \bigcup_{n=1}^\infty \sigma(X_1, \ldots, X_n)$。$\mathcal{A}$ 是代数（但未必是 $\sigma$-代数），且 $\sigma(\mathcal{A}) = \sigma(X_1, X_2, \ldots)$。

对任意 $n$，$A \in \mathcal{T}$ 与 $\sigma(X_1, \ldots, X_n)$ 独立，故 $A$ 与 $\mathcal{A}$ 中任意事件独立。

### 3. 应用 $\pi$-$\lambda$ 引理

由 $\pi$-$\lambda$ 引理，$A$ 与 $\sigma(\mathcal{A}) = \sigma(X_1, X_2, \ldots)$ 独立。特别地，由于 $A \in \sigma(X_1, X_2, \ldots)$，$A$ 与自身独立。

### 4. 得出结论

由 $A$ 与自身独立：
$$P(A) = P(A \cap A) = P(A) \cdot P(A) = P(A)^2$$

因此 $P(A) = 0$ 或 $P(A) = 1$。$\square$

**应用示例**：
- 级数 $\sum_{n=1}^\infty X_n$ 收敛的事件是尾事件，故其概率为 $0$ 或 $1$。
- $\limsup_{n \to \infty} X_n$ 的取值是尾事件（$\limsup_{n \to \infty} X_n = \lim_{n \to \infty} \sup_{k \geq n} X_k$ 不依赖于前有限项），故 $P(\limsup X_n = \infty) \in \{0, 1\}$。
- $\lim_{n \to \infty} \bar{X}_n$ 的存在性是尾事件，因此在独立同分布情形下，样本均值的极限要么几乎必然存在，要么几乎必然不存在。