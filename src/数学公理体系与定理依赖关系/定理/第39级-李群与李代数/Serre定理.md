# Serre 定理

> **一句话大白话**：半单李代数不必从大桌子上一块块搭建，只要一张 Cartan 矩阵"说明书"配几条 Serre 关系就能"生成"出完整代数，相当于给每类李代数发一份统一的拼装图纸。
>
> **小例子**：$\mathfrak{sl}_2(\mathbb{C})$ 由生成元 $e,f,h$ 及关系 $[h,e]=2e$，$[h,f]=-2f$，$[e,f]=h$ 定义，这就是 Serre 关系在 $A_1$ 情形的具体体现。

## 介绍

Serre 定理（Serre's relations）是李代数理论中由 Jean-Pierre Serre 提出的一个基本结果，它给出了半单李代数的一组简洁的生成元和关系描述。具体而言，Serre 定理表明，每个有限维复半单李代数可以由其 Cartan 矩阵通过一组称为 Serre 关系（Serre relations）的生成元和关系来完全刻画。这一定理为半单李代数的分类和构造提供了统一的代数框架。

## 分析

**前置依赖**：半单李代数、根系统、Cartan 矩阵、单根、根空间分解、$\mathfrak{sl}_2$-三元组、Dynkin 图。

**定理内容**：设 $A = (a_{ij})$ 是 $n \times n$ Cartan 矩阵（即 $a_{ii}=2$，$a_{ij} \le 0$ 对 $i\neq j$，且 $a_{ij}=0 \iff a_{ji}=0$，$a_{ij}$ 为整数）。则存在唯一的（在同构意义下）有限维复半单李代数 $\mathfrak{g}(A)$，由生成元
$$e_i, f_i, h_i \quad (i=1,\dots,n)$$
和以下关系定义：
1. $[h_i, h_j] = 0$
2. $[h_i, e_j] = a_{ij}e_j$
3. $[h_i, f_j] = -a_{ij}f_j$
4. $[e_i, f_j] = \delta_{ij}h_i$
5. $\text{ad}_{e_i}^{1-a_{ij}}(e_j) = 0$ 对 $i \neq j$
6. $\text{ad}_{f_i}^{1-a_{ij}}(f_j) = 0$ 对 $i \neq j$

其中关系 5 和 6 称为 Serre 关系（或 Serre 长关系）。

**数学内涵**：Serre 定理表明，半单李代数完全由它的 Cartan 矩阵（或等价地，它的 Dynkin 图）决定。这为半单李代数的构造提供了显式的生成元和关系形式，也是量子群（quantum groups）的推广基础——量子群正是通过将 Serre 关系变形为量子 Serre 关系得到的。

**证明策略**：证明分为两个主要部分。首先，从给定的 Cartan 矩阵出发，通过自由李代数模去 Serre 关系构造一个李代数 $\mathfrak{g}(A)$。然后证明 $\mathfrak{g}(A)$ 是有限维半单李代数，且其 Cartan 子代数和根系统与给定的 Cartan 矩阵一致。证明的关键是构造 $\mathfrak{g}(A)$ 的根空间分解，并利用 Weyl 群的作用证明根空间的有限维性。

## 思考过程

Serre 定理的核心思想是：半单李代数完全由它的单根之间的夹角和长度比（即 Cartan 矩阵）决定。给定 Cartan 矩阵 $A$，我们可以构造一个李代数，其生成元对应每个单根 $e_i, f_i, h_i$，其中 $e_i$ 生成正根空间 $\mathfrak{g}_{\alpha_i}$，$f_i$ 生成负根空间 $\mathfrak{g}_{-\alpha_i}$，$h_i$ 生成 Cartan 子代数的一部分。

关系 1-4 是 $\mathfrak{sl}_2$-三元组的基本关系，描述了每个单根对应的 $\mathfrak{sl}_2$ 子代数。关系 5-6（Serre 关系）则编码了不同单根之间的相互作用。

Serre 关系 $\text{ad}_{e_i}^{1-a_{ij}}(e_j)=0$ 的直观意义是：当对 $e_j$ 反复施加 $e_i$ 的伴随作用超过一定次数时，结果为零。这个次数正好由 Cartan 矩阵元素 $a_{ij}$ 决定。这反映了根串理论的结论：从 $\beta$ 出发沿 $\alpha$ 方向的根串长度由 $\frac{2(\beta,\alpha)}{(\alpha,\alpha)}$ 决定。

## 证明过程

**定理**（Serre）：设 $A = (a_{ij})$ 是 $n \times n$ Cartan 矩阵。定义李代数 $\mathfrak{g}(A)$ 由生成元 $e_i, f_i, h_i$（$i=1,\dots,n$）和以下关系生成：
$$\begin{aligned}
&[h_i, h_j] = 0, \\
&[h_i, e_j] = a_{ij}e_j, \\
&[h_i, f_j] = -a_{ij}f_j, \\
&[e_i, f_j] = \delta_{ij}h_i, \\
&(\text{ad}_{e_i})^{1-a_{ij}}(e_j) = 0, \quad i \neq j, \\
&(\text{ad}_{f_i})^{1-a_{ij}}(f_j) = 0, \quad i \neq j.
\end{aligned}$$
则 $\mathfrak{g}(A)$ 是有限维复半单李代数，其 Cartan 矩阵为 $A$。

**证明概要**：

**步骤 1**：构造自由李代数 $F$，生成元为 $e_i, f_i, h_i$。设 $I$ 是由 Serre 关系生成的理想，令 $\mathfrak{g}(A) = F/I$。

**步骤 2**：定义 $\mathfrak{h} = \text{span}\{h_i\}$。由关系 1，$\mathfrak{h}$ 是交换子代数。由关系 2-3，$\mathfrak{h}$ 在 $\mathfrak{g}(A)$ 上的伴随作用是对角化的，且 $e_i, f_i$ 分别是权为 $\alpha_i, -\alpha_i$ 的根向量，其中 $\alpha_i \in \mathfrak{h}^*$ 满足 $\alpha_i(h_j) = a_{ji}$。

**步骤 3**：构造 $\mathfrak{g}(A)$ 的根空间分解。每个根可以表示为 $\alpha = \sum k_i \alpha_i$ 的线性组合。通过 Serre 关系，可以证明每个根空间是有限维的。

**步骤 4**：证明 $\mathfrak{g}(A)$ 的 Killing 型非退化（利用 Cartan 矩阵的可逆性），从而 $\mathfrak{g}(A)$ 是半单的。

**步骤 5**：证明 $\mathfrak{g}(A)$ 的根系统与给定的 Cartan 矩阵一致。这需要验证：
- 反射 $s_{\alpha_i}$ 保持根系统。
- 每个根 $\alpha$ 的"高度" $\sum k_i$ 是有限的。
- 根系统的维数等于 $n$。

**步骤 6**：唯一性。若 $\mathfrak{g}$ 是半单李代数，其 Cartan 子代数为 $\mathfrak{h}$，单根为 $\alpha_1,\dots,\alpha_n$，则选取 $e_i \in \mathfrak{g}_{\alpha_i}, f_i \in \mathfrak{g}_{-\alpha_i}, h_i = [e_i, f_i]$，它们满足 Serre 关系，故 $\mathfrak{g}$ 同构于 $\mathfrak{g}(A)$ 的商。利用有限维半单性证明该商是同构。

**唯一性**：设 $\mathfrak{g}$ 是有限维复半单李代数，Cartan 矩阵为 $A$。取 $\mathfrak{g}$ 的 Cartan 子代数 $\mathfrak{h}$，单根 $\alpha_i$，以及对应的 $\mathfrak{sl}_2$-三元组 $\{e_i, f_i, h_i\}$，其中 $[e_i, f_i] = h_i$，$\alpha_i(h_j) = a_{ji}$。可以验证 Serre 关系成立，故存在满同态 $\mathfrak{g}(A) \to \mathfrak{g}$。由 $\mathfrak{g}(A)$ 的半单性，该同态是同构。$\square$

**推论**：有限维复半单李代数到其 Cartan 矩阵（或 Dynkin 图）的对应是一一对应。因此，半单李代数的分类化为 Dynkin 图的分类。