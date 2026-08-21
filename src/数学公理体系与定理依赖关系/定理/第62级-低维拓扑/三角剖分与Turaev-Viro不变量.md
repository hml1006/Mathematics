# 三角剖分与 Turaev–Viro 不变量

> **一句话大白话**：把一个三维空间切成很多小四面体，给每条棱和面标上用量子符号算出的权数全加起来，结果与怎么切无关——切法变了数也不变，于是成为空间的"指纹"。
>
> **小例子**：用 $SU(2)$ 在 $q$ 为 4 次单位根时的 $6j$ 符号，对任意三角剖分求和得到 $TV(M)$；$S^3$ 的 Turaev–Viro 不变量可由此显式计算并与 RT 不变量关联。

## 一、定理介绍

> **前置依赖**：闭三维流形的三角剖分与 Pachner 移动、spherical fusion 范畴与量子维数、$6j$–符号与 Biedenharn–Elliott 恒等式、Witten–Reshetikhin–Turaev 不变量与 Dehn 手术。

Turaev–Viro 不变量是定义在闭三维流形上的拓扑不变量，由 Turaev 与 Viro 于 1992 年利用量子群表示论中的 $6j$–符号构造。与 Alexander 多项式等经典不变量不同，Turaev–Viro 不变量通过流形的三角剖分（更一般地，胞腔剖分）计算，并对剖分的选择保持不变。当取特定参数时，它与 Witten–Reshetikhin–Turaev 不变量有密切联系，并为三维流形的量子拓扑分类提供了有力工具。

## 二、原理思路

给定闭三维流形 $M$ 的一个三角剖分 $\mathcal{T}$，考虑其对偶 $2$–骨架中的每条边赋予量子群表示指标，每个四面体贡献一个 $6j$–符号，并对所有内部边的状态求和。具体地，利用半单 spherical fusion category $\mathcal{C}$（如量子群 $U_q(\mathfrak{sl}_2)$ 在根式单位处的表示范畴），对每个顶点、边、面赋予适当的量子维数权重。不变量的构造基于 $6j$–符号满足的 Pentagon 方程与正交归一关系，这些关系保证了状态和对三角细分（subdivision）不敏感，从而只依赖于 $M$ 的拓扑类型。

## 三、定理的严格表述

**定义（Turaev–Viro 不变量）.** 设 $M$ 为闭定向三维流形，$\mathcal{T}$ 为 $M$ 的有限三角剖分。设 $\mathcal{C}$ 为半单 spherical fusion category，$I$ 为其简单对象同构类集合，$d_i$ 为对象 $i$ 的量子维数。对每个边 $e$ 赋予标签 $i_e \in I$，要求每个三角形面的三条边标签可容（admissible），并对每个四面体 $\Delta$ 取其 $6j$–符号

$$
\begin{vmatrix}
i_1 & i_2 & i_3 \\
i_4 & i_5 & i_6
\end{vmatrix}_{\!\mathcal{C}}.
$$

定义状态权重

$$
W(s) = \prod_{v \in \mathcal{T}^{(0)}} d_{i_v}^{-2} \prod_{e \in \mathcal{T}^{(1)}} d_{i_e} \prod_{\Delta \in \mathcal{T}^{(3)}} \begin{vmatrix} i_1 & i_2 & i_3 \\ i_4 & i_5 & i_6 \end{vmatrix}_{\!\mathcal{C}},
$$

其中 $d_{i_v}$ 为与顶点关联的规范对象维数。Turaev–Viro 不变量定义为所有可容状态 $s$ 的权重之和：

$$
\mathrm{TV}_{\mathcal{C}}(M) = \sum_{s} W(s) \in \mathbb{C}.
$$

**定理（Turaev–Viro）.** 上述量 $\mathrm{TV}_{\mathcal{C}}(M)$ 不依赖于三角剖分 $\mathcal{T}$ 的选取，因此是闭三维流形 $M$ 的拓扑不变量。

**定理（与 WRT 不变量的关系）.** 当 $\mathcal{C}$ 为量子群 $U_q(\mathfrak{sl}_2)$ 在 $q = e^{\pi i / r}$ 处的表示范畴时，有

$$
\mathrm{TV}_{\mathcal{C}}(M) = |\mathrm{WRT}(M)|^2,
$$

其中 $\mathrm{WRT}(M)$ 为 Witten–Reshetikhin–Turaev 不变量。

## 四、证明过程

**剖分无关性证明概要.**

1. **Pachner 定理.** 任意两个闭三维流形的三角剖分可以通过有限次 Pachner 移动相互转化。三维 Pachner 移动共有 $2 \leftrightarrow 3$ 和 $1 \leftrightarrow 4$ 两种基本类型。

2. **$2 \leftrightarrow 3$ 移动下的不变性.** 该移动将两个相邻四面体替换为三个共享一条公共边的四面体。利用 $6j$–符号的 Biedenharn–Elliott 恒等式（即 Pentagon 方程），五个 $6j$–符号的乘积在两个配置下相等，故状态和在 $2 \leftrightarrow 3$ 移动下不变。

3. **$1 \leftrightarrow 4$ 移动下的不变性.** 该移动在单个四面体内部插入一个内点并将其细分为四个小四面体。通过 fusion category 的归一化条件与量子维数的乘积恒等式，新增顶点和边的贡献恰好抵消，状态和不改变。

4. **定向与流形同胚.** 由于不变量对任意 Pachner 移动保持不变，而同一流形的不同三角剖分可通过 Pachner 移动连接，因此 $\mathrm{TV}_{\mathcal{C}}(M)$ 只依赖于 $M$ 的 PL 同胚类；在三维情形，PL 同胚等价于拓扑同胚。

**与 WRT 关系证明概要（$U_q(\mathfrak{sl}_2)$ 情形）.** 利用 surgery presentation 将 $M$ 表为沿链环 $L$ 的 Dehn 手术结果。Turaev–Viro 不变量的状态和对三角剖分的求和可以重组为对链环 $L$ 的着色求和，该求和恰等于 $|WRT(L)|^2$ 的 surgery 公式。

## 五、应用与意义

Turaev–Viro 不变量是三维量子拓扑的核心不变量之一。它不仅能区分同调球面、检测某些流形的非平凡性，还与拓扑量子场论（TQFT）的构造直接相关：Turaev–Viro 不变量可扩展为二维曲面到一维向量空间的 TQFT 函子。此外，它在量子计算与凝聚态物理中有重要应用：Kitaev 的 toric code 模型和 Levin–Wen 弦网模型均建立在 fusion category 与 $6j$–符号之上，其基态简并度与 Turaev–Viro 型不变量密切相关。近年来，Turaev–Viro 不变量的数值计算也被用于探索三维流形的量子不变量与经典几何不变量（如双曲体积）之间的渐近关系。
