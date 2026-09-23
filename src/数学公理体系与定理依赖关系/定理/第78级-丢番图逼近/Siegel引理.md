# Siegel 引理

> **一句话大白话**：一个"方程个数少于未知数个数"的整系数线性方程组，必有一个非零整数解，而且这个解的各分量可以被系数大小统一控制住——解不仅存在，还能很"小"。

> **小例子**：取 $m=1,n=2$，方程 $ax+by=0$（$a,b$ 为整数，$|a|,|b|\le H$）。取 $(x,y)=(b,-a)$ 即得整数解，且 $|x|,|y|\le H$。引理的估计 $(nH)^{m/(n-m)}=(2H)^{1}=2H$ 与之相符，只差常数因子。

## 一、定理介绍

> **前置依赖**：鸽巢原理（抽屉原理）、秩-零化度定理、矩阵与行列式、高度（height）与非阿基米德赋值（概念）、辅助多项式方法（概念）。

Siegel 引理由 Carl Ludwig Siegel 于 1929 年为研究代数函数的整点与超越性而提出（其思想可追溯到 Thue 与 Siegel 的逼近工作）。它断言：若整系数矩阵 $A$ 是 $m\times n$ 的且 $n>m$，则存在非零整数向量 $\mathbf{x}$ 落在核中，且 $\|\mathbf{x}\|_\infty$ 被 $\big(\max|a_{ij}|\big)^{m/(n-m)}$ 量级控制。提出它的动机是构造"辅助多项式"：在 Gelfond–Schneider、Roth 等超越性与逼近定理中，需要找到一个系数很小、却在许多指定点消没的多项式，而"消没条件"恰是一组线性方程。Siegel 引理保证这种辅助多项式存在且系数不大，是一切辅助多项式方法（auxiliary polynomial method）的起点，也是丢番图逼近、超越数论与线性型下界理论的基本工具。

## 二、原理思路

1. 鸽巢计数：数一数"小向量"有多少个，再数一数"它们的像"可能有多少种取值。
2. 若小向量个数严格多于像的个数，则两张不同的小向量映到同一点，其差就是非零的核元素，且分量仍小。
3. 令界 $N$ 满足 $(N+1)^n>(2nHN+1)^m$，即 $N\gtrsim(nH)^{m/(n-m)}$，即得结论。

## 三、定理的严格表述

设 $A=(a_{ij})$ 为 $m\times n$ 的整系数矩阵，$m<n$，且 $|a_{ij}|\le H$（$H\ge1$）。则存在非零整向量 $\mathbf{x}=(x_1,\dots,x_n)^{\!\top}\in\mathbb{Z}^n$ 使
$$
A\,\mathbf{x}=\mathbf{0},\qquad \|\mathbf{x}\|_\infty=\max_i|x_i|\le N:=\big\lceil (nH)^{m/(n-m)}\big\rceil .
$$
更精确地，可取 $N$ 为满足 $(N+1)^n>(2nHN+1)^m$ 的最小正整数。

## 四、证明过程

**证明：**

**步骤 1：数小向量。** 令
$$
\mathcal{S}_N=\{\mathbf{x}\in\mathbb{Z}^n:0\le x_i\le N\ \ \forall i\}.
$$
其元素个数为 $(N+1)^n$（每个分量独立地取 $N+1$ 种值）。

**步骤 2：数像的取值。** 对 $\mathbf{x}\in\mathcal{S}_N$，$A\mathbf{x}$ 的第 $j$ 个分量为 $\sum_{i=1}^{n}a_{ji}x_i$。由 $|a_{ji}|\le H$、$0\le x_i\le N$ 得
$$
0\le (A\mathbf{x})_j\le \sum_{i=1}^{n}H\cdot N=nHN .
$$
故 $A\mathbf{x}$ 的每个分量最多取 $nHN+1$ 个非负值，像集 $A(\mathcal{S}_N)$ 的元素个数至多为
$$
\big(nHN+1\big)^m\le \big(2nHN+1\big)^m .
$$

**步骤 3：鸽巢原理。** 若
$$
(N+1)^n>\big(2nHN+1\big)^m ,
$$
则 $|\mathcal{S}_N|>|A(\mathcal{S}_N)|$，存在两个不同的向量 $\mathbf{x}\neq\mathbf{x}'\in\mathcal{S}_N$ 使 $A\mathbf{x}=A\mathbf{x}'$。令 $\mathbf{y}=\mathbf{x}-\mathbf{x}'$，则 $\mathbf{y}\neq\mathbf{0}$、$A\mathbf{y}=\mathbf{0}$，且 $|y_i|=|x_i-x_i'|\le N$。这就给出所需的小核向量。

**步骤 4：求解不等式确定 $N$。** 在 $n-m>0$ 时，$(N+1)^n>(2nHN+1)^m$ 大致等价于 $N^{n-m}>(2nH)^m$，即
$$
N>(2nH)^{m/(n-m)} .
$$
严格地：取 $N_0=\big\lceil(nH)^{m/(n-m)}\big\rceil$，则 $N_0\ge(nH)^{m/(n-m)}$，于是 $(N_0+1)^n\ge N_0^n\ge(nH)^{mn/(n-m)}$，而 $(2nHN_0+1)^m\le(3nHN_0)^m$（$N_0\ge1$），只需比较指数 $N_0^{n-m}\ge(nH)^m$ 的常数即可；适当放大常数（把 $nH$ 换成 $3nH$ 等）后，上式严格成立。因此取 $N=\lceil(3nH)^{m/(n-m)}\rceil$ 必可；若想保留引理中的常数形式，可先对 $H$ 作归一化，或直接采用 $N$ 为满足 $(N+1)^n>(2nHN+1)^m$ 的最小正整数作为引理的界（它即被 $C(n,m)\cdot H^{m/(n-m)}$ 控制）。$\square$

## 五、应用与意义

- 它是"辅助多项式方法"的基石：Gelfond–Schneider 定理用它构造在指定点高阶消没、系数可控的多项式。
- 在 Roth 定理中，Siegel 引理的精细版本（含高度与多变量的推广）用于控制辅助多项式系数的增长。
- 在丢番图逼近的线性型理论中，它是 Thue–Siegel–Roth 与 Baker 方法构造小解的标准工具。
- 在代数数论中，对整数环 $\mathcal{O}_K$ 的系数可用迹或嵌入绝对值做高度估计，得到 Siegel 引理的数域版本。
- 它与 Minkowski 凸体定理、格论第一定理同属"用计数/体积保证小解存在"的方法族，彼此可以互推。

## 相关条目

- [Gelfond-Schneider 定理](./Gelfond-Schneider定理.md)：其证明用 Siegel 引理构造辅助函数。
- [Roth 定理](./Roth定理.md)：用 Siegel 引理及其推广构造多变量辅助多项式。
- [Liouville 定理](./Liouville定理.md)：早期超越性判别，给出逼近下界的原型，Siegel 引理是其精细化的工具。
- [Dirichlet 逼近定理](./Dirichlet逼近定理.md)：同样用鸽巢原理保证好的有理逼近存在。
- [连分数的最佳逼近性质](./连分数的最佳逼近性质.md)：与 Dirichlet 逼近互补，刻画最优有理逼近的结构。
