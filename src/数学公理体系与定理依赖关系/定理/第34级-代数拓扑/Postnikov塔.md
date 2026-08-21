# Postnikov 塔

> **一句话大白话**：任意空间太复杂，Postnikov 塔把它一层层"打薄"——每一层只保留到某个维数为止的同伦信息，再逐层贴上更高维的同伦群，像剥洋葱又像盖塔楼，最终逼近原空间。
>
> **小例子**：一个空间 $X$ 的第一层 $X_{\le 1}$ 只关心 $\pi_1$，第二层 $X_{\le 2}$ 额外加入 $\pi_2$，每一层都是上一层的纤维化，逐层加高直到信息补全。

## 一、定理介绍

> **前置依赖**：同伦群、Eilenberg-MacLane 空间 $K(G, n)$、CW 复形与胞腔逼近定理、纤维化与弱同伦等价、上同调类（$k$-不变量的分类）

Postnikov 塔是同伦论中的基本构造，由 Solomon Lefschetz 和 Postnikov 于 1950 年代独立引入。它为任意拓扑空间提供了一个系统化的逼近方法，将空间的同伦信息分解为一系列主纤维化（principal fibrations），每层只包含一个同伦群的信息。

Postnikov 塔是计算同伦群、研究映射空间和分类纤维化的关键工具。它在代数拓扑、代数几何和数学物理中有广泛应用。

## 二、原理思路

**核心思想**：通过逐步"截断"高阶同伦群，将复杂空间分解为简单的 Eilenberg-MacLane 空间的纤维化序列。

**关键观察**：
1. Eilenberg-MacLane 空间 $K(G, n)$ 只有一个非平凡同伦群 $G$ 在第 $n$ 层
2. 任意空间 $X$ 可以通过 Postnikov 塔 $\{X_n\}$ 逼近，其中 $X_n$ 只包含 $\pi_1, \ldots, \pi_n$ 的信息
3. 从 $X_n$ 到 $X_{n-1}$ 的纤维化由 $K(\pi_n, n)$ 的主纤维化给出
4. 纤维化的分类由 $k$-不变量（Postnikov 不变量）给出，这些是上同调类

**证明策略**：
- 构造 Postnikov 塔：通过逐步杀死高阶同伦群
- 证明收敛性：$X \simeq \lim X_n$（在适当条件下）
- 计算 $k$-不变量：通过 obstruction theory

## 三、定理的严格表述

**定义（Eilenberg-MacLane 空间）**：拓扑空间 $K(G, n)$（$n \geq 1$，$G$ 是群，$n \geq 2$ 时 $G$ 交换）称为 **Eilenberg-MacLane 空间**，如果
$$\pi_i(K(G, n)) = \begin{cases} G & i = n \\ 0 & i \neq n \end{cases}$$

**定理（Postnikov 塔）**：设 $X$ 是单连通的 CW 复形（或更一般地，简单空间）。则存在：

1. **Postnikov 塔**：一列空间 $\{X_n\}_{n \geq 1}$ 和纤维化
$$\cdots \to X_n \xrightarrow{p_n} X_{n-1} \to \cdots \to X_2 \to X_1$$
满足：
- $\pi_i(X_n) = \pi_i(X)$ 对 $i \leq n$
- $\pi_i(X_n) = 0$ 对 $i > n$
- 存在映射 $f_n: X \to X_n$ 诱导同伦群的同构 $\pi_i(X) \cong \pi_i(X_n)$（$i \leq n$）

2. **主纤维化结构**：每个 $p_n: X_n \to X_{n-1}$ 是主 $K(\pi_n(X), n)$-纤维化，即有纤维化序列
$$K(\pi_n(X), n) \to X_n \xrightarrow{p_n} X_{n-1} \xrightarrow{k_n} K(\pi_n(X), n+1)$$
其中 $k_n$ 称为第 $n$ 个 **Postnikov 不变量**（或 $k$-不变量），是上同调类 $k_n \in H^{n+1}(X_{n-1}; \pi_n(X))$。

3. **收敛性**：若 $X$ 是 CW 复形，则 $X \simeq \lim_{\leftarrow} X_n$（弱同伦等价）。

4. **唯一性**：Postnikov 塔在纤维同伦等价意义下唯一，由 $k$-不变量 $\{k_n\}$ 完全决定。

## 四、证明过程

**构造 Postnikov 塔**：

**步骤 1**：杀死高阶同伦群。对空间 $X$，构造空间 $X_n$ 使得 $\pi_i(X_n) = \pi_i(X)$（$i \leq n$）且 $\pi_i(X_n) = 0$（$i > n$）。

方法：对每个 $i > n$ 和 $\pi_i(X)$ 的生成元，附着 $(i+1)$-维胞腔来"杀死"这些同伦群。具体地，设 $\{f_\alpha: S^i \to X\}$ 代表 $\pi_i(X)$ 的生成元，定义
$$X_n = X \cup_{\{f_\alpha\}} \bigcup_\alpha D^{i+1}$$
通过适当选择，可以使得 $\pi_i(X_n) = 0$ 对 $i > n$。

**步骤 2**：构造映射。通过胞腔逼近定理，可以构造映射 $f_n: X \to X_n$ 诱导同伦群的同构（在低维）。

**步骤 3**：主纤维化结构。考虑映射 $f_{n-1}: X \to X_{n-1}$ 和 $f_n: X \to X_n$。由于 $f_n$ 杀死的高阶同伦群比 $f_{n-1}$ 少，存在映射 $p_n: X_n \to X_{n-1}$ 使得 $f_{n-1} = p_n \circ f_n$。

**步骤 4**：纤维的分析。$p_n$ 的纤维 $F_n$ 满足 $\pi_i(F_n) = 0$（$i \neq n$）且 $\pi_n(F_n) = \pi_n(X)$。因此 $F_n \simeq K(\pi_n(X), n)$。

**步骤 5**：$k$-不变量的定义。纤维化 $F_n \to X_n \to X_{n-1}$ 的分类由映射 $k_n: X_{n-1} \to B F_n \simeq K(\pi_n(X), n+1)$ 给出。这个映射的同伦类 $[k_n] \in [X_{n-1}, K(\pi_n(X), n+1)] \cong H^{n+1}(X_{n-1}; \pi_n(X))$ 就是第 $n$ 个 Postnikov 不变量。

**收敛性证明**：

**步骤 1**：对任意 CW 复形 $K$，$[K, X] \cong [K, \lim X_n]$（在适当条件下）。

**步骤 2**：由于 $\pi_i(X) \cong \pi_i(X_n)$（$i \leq n$），映射 $X \to X_n$ 诱导同伦群的同构（在低维）。取极限，$X \to \lim X_n$ 诱导所有同伦群的同构，因此是弱同伦等价。

**示例**：

- **球面** $S^2$：$\pi_1(S^2) = 0$，$\pi_2(S^2) = \mathbb{Z}$，$\pi_3(S^2) = \mathbb{Z}$。Postnikov 塔的前几层：
  - $X_1 = *$（可缩空间）
  - $X_2 = K(\mathbb{Z}, 2) = \mathbb{CP}^\infty$
  - $X_3$ 是 $K(\mathbb{Z}, 3) \to X_3 \to \mathbb{CP}^\infty$ 的纤维化，$k$-不变量 $k_2 \in H^4(\mathbb{CP}^\infty; \mathbb{Z}) \cong \mathbb{Z}$ 是生成元

## 五、应用与意义

Postnikov 塔在同伦论中有广泛应用：

1. **同伦群计算**：通过 obstruction theory 逐步计算同伦群。

2. **映射空间**：$[X, Y]$ 可以通过 Postnikov 塔逐层计算，每层的 obstruction 在 $H^{n+1}(X; \pi_n(Y))$ 中。

3. **纤维化分类**：主纤维化的分类由 Postnikov 不变量给出。

4. **有理同伦论**：在有理系数下，Postnikov 塔简化为 Sullivan 模型，使得同伦论可以用交换微分分次代数研究。

5. **稳定同伦论**：Postnikov 塔的稳定版本用于研究谱序列和稳定同伦群。

6. **代数几何**：在 $\mathbb{A}^1$-同伦论中，Postnikov 塔用于研究代数簇的同伦性质。

7. **数学物理**：在拓扑量子场论中，Postnikov 塔用于分类拓扑相和缺陷。

Postnikov 塔的推广包括：equivariant Postnikov 塔、参数化 Postnikov 塔、以及 $\infty$-范畴论中的 Postnikov 塔。
