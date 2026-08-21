# 截面曲率 Ricci曲率 标量曲率

> **一句话大白话**：弯曲信息可以"分级压缩"：截面曲率看每一小片平面弯多少（最细），Ricci曲率按方向平均（中等粒度），标量曲率再平均成一束数字（最粗）——级联起来从细到粗概括曲率。
>
> **小例子**：单位球面截面曲率恒1，Ricci曲率恒$(n-1)$，标量曲率$n(n-1)$；三者依次由张量"缩并/跟踪"得到，就像先给每切平面打分、再按方向平均、最后全范围平均。

## 介绍

截面曲率（Sectional Curvature）、Ricci曲率（Ricci Curvature）和标量曲率（Scalar Curvature）是黎曼几何中从Riemann曲率张量导出的三个重要曲率概念，它们在不同层次上刻画了流形的弯曲程度。截面曲率反映了二维切平面方向的弯曲，是最基本的曲率概念；Ricci曲率是截面曲率在某个方向上的平均，在 Einstein 方程和比较定理中起核心作用；标量曲率则是 Ricci 曲率的迹，是完全平均化的曲率标量。这三个曲率概念共同构成了从局部到全局的曲率描述体系。

## 分析

**前置依赖**：Riemann 曲率张量及其对称性、标准正交基与缩并（迹）运算、极化恒等式、第二 Bianchi 恒等式。

**定义**：设 $(M, g)$ 是 $n$ 维 Riemann 流形，$p \in M$。

1. **截面曲率**：对 $T_pM$ 中线性无关的向量 $X, Y$，截面曲率为
   $$
   K(X, Y) = \frac{R(X, Y, Y, X)}{|X \wedge Y|^2} = \frac{g(R(X,Y)Y, X)}{g(X,X)g(Y,Y) - g(X,Y)^2}.
   $$

2. **Ricci曲率**：对单位向量 $X \in T_pM$，Ricci曲率为
   $$
   \mathrm{Ric}(X, X) = \sum_{i=1}^n K(X, e_i) = \sum_{i=1}^n R(X, e_i, e_i, X),
   $$
   其中 $\{e_i\}$ 是 $T_pM$ 的标准正交基。Ricci曲率张量是 $(0,2)$-张量，分量 $R_{ij} = \sum_k R^k_{ikj}$。

3. **标量曲率**：标量曲率是 Ricci 曲率的迹：
   $$
   S = \mathrm{tr}_g \mathrm{Ric} = \sum_{i=1}^n \mathrm{Ric}(e_i, e_i) = \sum_{i,j} R_{ijij}.
   $$

**依赖的概念**：Riemann曲率张量、标准正交基、迹、截面曲率的几何意义。

**核心关系**：截面曲率完全决定了曲率张量，Ricci曲率和标量曲率是截面曲率的逐次平均。

## 思考过程

这三个曲率概念的重要之处在于它们在不同精细度上描述了流形的弯曲：
- 截面曲率 $K(X,Y)$ 最精细，它给出了每个二维方向的弯曲信息。
- Ricci曲率 $\mathrm{Ric}(X,X)$ 是 $X$ 方向上的平均截面曲率，它出现在体积比较和 Bonnet-Myers 定理中。
- 标量曲率 $S$ 是全局平均曲率，出现在 Gauss-Bonnet 定理和 Einstein-Hilbert 作用量中。

在 Einstein 流形上，$\mathrm{Ric} = \lambda g$，此时 Ricci 曲率在每个方向上都相同。在常曲率空间（如球面、Euclidean 空间、双曲空间）中，截面曲率是常数。

## 证明过程

**定理**（截面曲率与曲率张量的关系）：设 $(M, g)$ 是 Riemann 流形，则曲率张量 $R$ 完全由截面曲率决定。

**证明**：

**步骤 1：曲率张量由截面曲率恢复。**

定义 $F(X,Y,Z,W) = R(X,Y,Z,W)$。由对称性，$F$ 是 $\Lambda^2 T_pM$ 上的对称双线性形式。截面曲率给出了 $F$ 在可分解双向量 $X \wedge Y$ 上的值：

$$
F(X \wedge Y, X \wedge Y) = K(X,Y) |X \wedge Y|^2.
$$

**步骤 2：极化恒等式。**

对任意双向量 $\alpha, \beta \in \Lambda^2 T_pM$，由极化

$$
F(\alpha, \beta) = \frac{1}{4} \left( F(\alpha + \beta, \alpha + \beta) - F(\alpha - \beta, \alpha - \beta) \right).
$$

因此截面曲率完全决定了 $F$，从而完全决定了曲率张量。$\square$

**定理**（Ricci曲率的几何意义）：设 $X$ 是单位切向量，则 $\mathrm{Ric}(X,X)$ 等于所有包含 $X$ 的二维方向截面曲率之和。

**证明**：选取标准正交基 $\{e_1, \ldots, e_n\}$ 使得 $e_1 = X$。则由定义

$$
\mathrm{Ric}(X,X) = \sum_{i=2}^n R(X, e_i, e_i, X) = \sum_{i=2}^n K(X, e_i).
$$

$\square$

**定理**（Einstein 流形）：若 $(M, g)$ 满足 $\mathrm{Ric} = \lambda g$ 对某个常数 $\lambda$，则标量曲率 $S = n\lambda$ 为常数。

**证明**：取迹得 $S = \mathrm{tr}_g \mathrm{Ric} = \mathrm{tr}_g (\lambda g) = n\lambda$。由第二 Bianchi 恒等式，$\nabla \mathrm{Ric} = 0$，故 $S$ 为常数。$\square$

**例**（常曲率空间）：截面曲率为常数 $c$ 的流形称为常曲率空间。此时

$$
R(X,Y)Z = c \left( g(Y, Z)X - g(X, Z)Y \right),
$$

且 $\mathrm{Ric}(X,Y) = (n-1)c \, g(X,Y)$，$S = n(n-1)c$。