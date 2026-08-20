# Frobenius 可积性定理

> **一句话大白话**：一堆切片能否拼成一个完整的"薄片分层"（子流形），只看它们的切方向会不会互相"锁死打架"——若在求和后依旧保持封闭（对括号运算封闭），就能局部铺成一个有厚度的曲面族。
>
> **小例子**：平面上给定处处一族过点方向 $\mathcal D$，若对任意两条切向量 $X,Y$，$[X,Y]$ 仍落在 $\mathcal D$ 里，则这些方向能拼成真正的曲线族；否则（像在 $\mathbb R^3$ 中给"转圈又不闭合"的方向）就散架不可积。

## 一、定理介绍

Frobenius 可积性定理是微分几何和微分方程理论中的基本定理，由 Ferdinand Georg Frobenius 于 1877 年证明。该定理给出了完全可积分布（即切平面的光滑场）存在积分流形的充要条件，是研究叶状结构（foliation）和李群作用的基础工具。

Frobenius 定理在经典力学、控制论、热力学和广义相对论中有重要应用。它将偏微分方程组的可积性条件与几何的无挠条件联系起来，体现了几何与分析的深刻统一。

## 二、原理思路

**核心思想**：一个分布（切平面的光滑场）存在积分流形当且仅当该分布在李括号运算下封闭（即对合条件）。

**关键观察**：
1. 分布 $\Delta$ 的积分流形是指其切空间处处等于 $\Delta$ 的子流形
2. 如果存在积分流形，则 $\Delta$ 中向量场的李括号仍在 $\Delta$ 中（必要性）
3. 反过来，如果对合条件成立，可以通过逐步积分构造积分流形（充分性）

**证明策略**：
- 必要性：利用李括号的几何意义（交换子的无穷小生成元）
- 充分性：通过坐标变换将分布局部化为坐标平面的切空间
- 使用归纳法，逐步积分向量场构造坐标卡

## 三、定理的严格表述

**定义（分布）**：设 $M$ 是 $n$ 维光滑流形。$M$ 上的一个 $k$ 维**分布** $\Delta$ 是对每个 $p \in M$ 指定 $T_pM$ 的 $k$ 维子空间 $\Delta_p$ 的映射，使得局部存在 $k$ 个光滑向量场 $X_1, \ldots, X_k$ 满足 $\Delta_p = \text{span}\{X_1(p), \ldots, X_k(p)\}$。

**定义（对合分布）**：分布 $\Delta$ 称为**对合的**（involutive），如果对任意两个局部属于 $\Delta$ 的向量场 $X, Y$，它们的李括号 $[X, Y]$ 也属于 $\Delta$。即若 $X(p), Y(p) \in \Delta_p$ 对所有 $p$，则 $[X, Y](p) \in \Delta_p$。

**定义（积分流形）**：$k$ 维子流形 $N \subset M$ 称为分布 $\Delta$ 的**积分流形**，如果对任意 $p \in N$，$T_pN = \Delta_p$。

**定理（Frobenius）**：设 $\Delta$ 是光滑流形 $M$ 上的 $k$ 维光滑分布。则 $\Delta$ 是完全可积的（即 $M$ 的每点都有 $\Delta$ 的积分流形通过）当且仅当 $\Delta$ 是对合的。

**等价形式（Pfaff 系统）**：设 $\omega^1, \ldots, \omega^{n-k}$ 是 $M$ 上的线性无关的 1-形式。则方程组 $\omega^1 = \cdots = \omega^{n-k} = 0$ 有积分流形当且仅当
$$d\omega^\alpha \equiv 0 \pmod{\omega^1, \ldots, \omega^{n-k}}, \quad \alpha = 1, \ldots, n-k$$
即 $d\omega^\alpha = \sum_\beta \theta^\alpha_\beta \wedge \omega^\beta$ 对某些 1-形式 $\theta^\alpha_\beta$ 成立。

## 四、证明过程

**必要性证明**：设 $\Delta$ 有积分流形，$X, Y$ 是 $\Delta$ 中的向量场。

对任意 $p \in M$，设 $N$ 是通过 $p$ 的积分流形。由于 $X, Y$ 切于 $N$，在 $N$ 上可以选择局部坐标 $(x^1, \ldots, x^k)$ 使得 $X = \sum a^i \frac{\partial}{\partial x^i}$，$Y = \sum b^j \frac{\partial}{\partial x^j}$。

则 $[X, Y] = \sum_{i,j} \left(a^i \frac{\partial b^j}{\partial x^i} - b^i \frac{\partial a^j}{\partial x^i}\right) \frac{\partial}{\partial x^j}$

由于 $[X, Y]$ 是 $\frac{\partial}{\partial x^j}$ 的线性组合，$[X, Y](p) \in T_pN = \Delta_p$。因此 $\Delta$ 是对合的。$\square$

**充分性证明**：设 $\Delta$ 是 $k$ 维对合分布。对任意 $p \in M$，需要构造通过 $p$ 的积分流形。

**步骤 1**：选取局部坐标。在 $p$ 附近选取坐标 $(x^1, \ldots, x^n)$ 使得 $p$ 对应原点。由于 $\Delta_p$ 是 $k$ 维的，可以假设 $X_1 = \frac{\partial}{\partial x^1}, \ldots, X_k = \frac{\partial}{\partial x^k}$ 在 $p$ 处张成 $\Delta_p$。

**步骤 2**：对 $k$ 归纳。$k = 1$ 时，单个非零向量场 $X_1$ 的积分曲线存在（常微分方程解的存在性），这就是 1 维积分流形。

**步骤 3**：归纳步骤。假设对 $k-1$ 维对合分布结论成立。设 $\Delta$ 是 $k$ 维对合分布，由 $X_1, \ldots, X_k$ 局部生成。

首先，$X_1$ 生成局部流 $\phi_t$。通过坐标变换，可以假设 $X_1 = \frac{\partial}{\partial x^1}$。

**步骤 4**：投影分布。考虑超平面 $\Sigma = \{x^1 = 0\}$。将 $X_2, \ldots, X_k$ 投影到 $\Sigma$ 上：
$$\tilde{X}_j = X_j - (X_j x^1) X_1, \quad j = 2, \ldots, k$$
则 $\tilde{X}_j$ 切于 $\Sigma$（即 $\tilde{X}_j x^1 = 0$）。

**步骤 5**：验证对合性。计算 $[\tilde{X}_i, \tilde{X}_j]$：
$$[\tilde{X}_i, \tilde{X}_j] = [X_i - (X_i x^1)X_1, X_j - (X_j x^1)X_1]$$
展开后，由于 $[X_i, X_j] \in \Delta$ 和 $X_1 \in \Delta$，可以证明 $[\tilde{X}_i, \tilde{X}_j]$ 是 $\tilde{X}_2, \ldots, \tilde{X}_k$ 的线性组合。

**步骤 6**：应用归纳假设。$\tilde{\Delta} = \text{span}\{\tilde{X}_2, \ldots, \tilde{X}_k\}$ 是 $\Sigma$ 上的 $k-1$ 维对合分布。由归纳假设，存在 $\Sigma$ 的 $(k-1)$ 维积分流形 $N'$。

**步骤 7**：构造积分流形。令 $N = \bigcup_{|t| < \varepsilon} \phi_t(N')$。由于 $X_1 = \frac{\partial}{\partial x^1}$ 和 $\tilde{X}_j$ 的构造，$N$ 是 $k$ 维的，且 $T_qN = \Delta_q$ 对所有 $q \in N$。$\square$

**Pfaff 系统形式的证明**：

设 $\omega^1, \ldots, \omega^{n-k}$ 定义分布 $\Delta = \ker \omega^1 \cap \cdots \cap \ker \omega^{n-k}$。

$\Delta$ 对合等价于：对任意 $X, Y \in \Delta$，$[X, Y] \in \Delta$。

由 Cartan 公式，$d\omega(X, Y) = X\omega(Y) - Y\omega(X) - \omega([X, Y])$。

若 $X, Y \in \Delta$，则 $\omega(X) = \omega(Y) = 0$，因此 $d\omega(X, Y) = -\omega([X, Y])$。

$\Delta$ 对合意味着 $[X, Y] \in \Delta$，即 $\omega([X, Y]) = 0$，等价于 $d\omega(X, Y) = 0$ 对所有 $X, Y \in \Delta$。

这等价于 $d\omega \equiv 0 \pmod{\omega^1, \ldots, \omega^{n-k}}$。$\square$

## 五、应用与意义

Frobenius 定理在多个数学领域有重要应用：

1. **叶状结构理论**：Frobenius 定理是叶状结构存在性的基础。完全可积分布给出流形的叶状分解。

2. **李群与李代数**：李群的左不变分布自动对合（因为李括号封闭），因此李群可以叶状化为陪集空间。

3. **经典力学**：Hamilton 系统的可积性条件与 Frobenius 定理密切相关。完全可积系统存在作用量-角度变量。

4. **控制论**：非线性控制系统的可达性集与分布的对合性有关（Chow 定理）。

5. **热力学**：热力学第二定律的数学表述涉及 Pfaff 方程的可积性。

6. **广义相对论**：时空的叶状化（如 ADM 形式）需要 Frobenius 定理。

7. **PDE 理论**：一阶偏微分方程组的相容性条件由 Frobenius 定理给出。

该定理的推广包括：Stefan-Sussmann 定理（奇分布的叶状化）、无穷维 Frobenius 定理、以及超分布和广义分布的可积性理论。
