# CR 几何基础

> **一句话大白话**：当"全纯结构"只在一个实数子流形（如空间降维后的"边界"）的表面一层成立时，研究这种"只沿切方向复、法方向是实"的几何叫 CR 几何——它是多复变在低维边界上的投影几何，像只保留复平面在墙壁上的影子。
>
> **小例子**：把多复变函数限制到实超曲面 $M=\{\rho=0\}$，其"复切空间"由 $X$ 满足 $X\rho=0$、$X=\partial/\partial\bar z$ 型生成；CR 结构正是沿着 $M$ 的复子束，Levi 形式的正负决定 $M$ 的"外凸/内凹"，CR 函数由此定义。

## 一、定理介绍

> **前置依赖**：Cauchy–Riemann 方程、复流形与实子流形、Levi 形式、Frobenius 定理、$\bar{\partial}_b$ 算子的次椭圆估计。

CR 几何（CR Geometry）研究的是复流形实子流形上的"全纯几何"，是介于多复变函数论、微分几何与偏微分方程之间的核心领域。"CR"代表"Cauchy–Riemann"，因为 CR 流形的本质是在实子流形上保留了 Cauchy–Riemann 方程的某种"切向"结构。

CR 几何的萌芽可追溯到 Poincaré（1907）对 $\mathbb{C}^2$ 中实超曲面的研究。Poincaré 发现 $\mathbb{C}^2$ 中实超曲面的双全纯等价问题有非平凡的局部不变量（Poincaré 不变量），与单复变中 Riemann 映射定理的"刚性"形成鲜明对比。现代 CR 几何理论由 Cartan、Tanaka、Chern–Moser（1974）等人系统发展。

CR 流形的中心定理包括：CR 嵌入定理（Boutet de Monvel，1974；Khenkin 等）、Chern–Moser 不变量理论、CR 函数的延拓定理等。

## 二、原理思路

CR 几何的核心思想是：在实子流形 $M \subset \mathbb{C}^n$ 上，考虑"复切空间"$H_p M = T_p M \cap J(T_p M)$，其中 $J$ 为 $\mathbb{C}^n$ 的复结构。这一分布上自然带有 $J$ 限制的结构，给出了 CR 流形的几何骨架。

**关键观察**：
1. 在 $M$ 上沿复切方向的 Cauchy–Riemann 方程有意义。$M$ 上的 CR 函数是沿复切方向满足 CR 方程的函数。
2. 当 $M$ 为实超曲面时，复切空间的余维数为 1，CR 结构由单一向量场（或 1-形式）刻画。
3. Levi 形式是 CR 流形的基本不变量，决定了几何与分析性质。
4. 边界 $\partial \Omega$（$\Omega \subset \mathbb{C}^n$ 为域）自然地带有 CR 结构，将多复变函数论与 CR 几何联系。

**核心定理**：
- **CR 嵌入定理**：在适当条件下（严格伪凸、可嵌性），抽象 CR 流形可全纯嵌入到 $\mathbb{C}^N$。
- **Chern–Moser 不变量**：严格伪凸 CR 流形有完整的局部不变量系，由曲率型量构成。
- **CR 函数延拓定理**：在严格伪凸超曲面上的 CR 函数可全纯延拓到一侧。

## 三、定理的严格表述

### CR 流形的定义

设 $M$ 是 $2m+k$ 维光滑流形。$M$ 上的 **CR 结构** 是一个复分布 $H^{1,0} M \subset \mathbb{C} \otimes TM$，满足：

1. $\dim_\mathbb{C} H^{1,0}_p M = m$（每点处复维数 $m$）；
2. $H^{1,0} M \cap \overline{H^{1,0} M} = \{0\}$（即"水平"分布为复子分布）；
3. 闭性（Frobenius 型条件）：若 $X, Y \in \Gamma(H^{1,0} M)$，则 $[X, Y] \in \Gamma(H^{1,0} M)$。

数 $m$ 称为 CR 维数，$k$ 称为 CR 余维数。当 $k = 1$ 时，$M$ 称为 **CR 超流形**。

### CR 函数

设 $(M, H^{1,0})$ 为 CR 流形。$M$ 上的连续函数 $f$ 称为 **CR 函数**，若对所有 $X \in \Gamma(H^{1,0} M)$，有 $Xf = 0$。等价地，$f$ 沿复切方向满足 Cauchy–Riemann 方程。

### Levi 形式

设 $(M, H^{1,0})$ 为 CR 超流形，$\xi$ 为 $H^{1,0} M$ 的局部定义 1-形式。**Levi 形式** 定义为
$$\mathcal{L}(Z, \bar{Z}) = -i \, d\xi(Z, \bar{Z}), \quad Z \in H^{1,0}.$$
若 $\mathcal{L}$ 在所有点处为正定/半正定，称 $M$ 为严格伪凸/伪凸 CR 流形。

### 主要定理

**定理 A（CR 函数延拓，Hans Lewy 定理）**：设 $\Omega \subset \mathbb{C}^n$ 为开集，$M \subset \partial \Omega$ 为 $C^2$ 实超曲面片，$p \in M$ 为严格伪凸点（即 Levi 形式在 $p$ 处正定）。则存在 $p$ 的邻域 $U$，使得任意在 $M$ 上的 CR 函数 $f$（在适当函数空间中）可延拓为 $\Omega \cap U$ 上的全纯函数。

**定理 B（Chern–Moser 局部不变量）**：在 $\mathbb{C}^{n+1}$ 中 $C^\infty$ 严格伪凸 CR 超曲面上，存在完备的局部 CR 不变量系，由 4 阶张量（Chern–Moser 张量）及其协变导数构成。当 $n \geq 2$ 时，Chern–Moser 张量消失是局部 CR 等价于球面 $S^{2n+1}$ 的充分必要条件。

**定理 C（Boutet de Monvel 嵌入定理，1974）**：设 $M$ 为 $2n+1$ 维紧致 $C^\infty$ 严格伪凸 CR 流形，$n \geq 2$。若 $M$ 不与 $S^{2n+1}$ 局部 CR 等价（"非球面条件"），则存在全纯嵌入 $\Phi: M \to \mathbb{C}^N$。

## 四、证明过程

### Hans Lewy 延拓定理证明概要

设 $M = \partial \Omega$ 在 $p = 0$ 处严格伪凸，$f$ 为 $M$ 上 CR 函数。

**步骤 1：法式化**。通过局部双全纯坐标变换，将 $M$ 在 $0$ 处化为"标准形式"
$$M = \{(z, w) \in \mathbb{C}^n \times \mathbb{C} : \text{Im}\, w = |z|^2 + O(|z|^3, |z| \text{Re}\, w, (\text{Re}\, w)^2)\}.$$
此时 Levi 形式即 $\sum |z_j|^2$，为严格正定。

**步骤 2：利用 Bishop 盘或全纯延拓构造**。考虑一族嵌在 $M$ 中或与 $M$ 相切的全纯圆盘 $\{D_t\}$，由 CR 性质 $f|_{D_t}$ 满足 Cauchy–Riemann，从而 $f$ 沿 $D_t$ 全纯。Bishop 证明严格伪凸性使 $\{D_t\}$ 充满 $M$ 一侧的楔形邻域 $W$。

**步骤 3：楔形延拓**。$f$ 在 $W$ 上定义为这些圆盘上全纯函数的一致极限，从而全纯延拓到 $W$。

**步骤 4：全纯凸包论证**。进一步利用全纯凸包将延拓扩张到完整的一侧 $\Omega \cap U$。$\square$

### Chern–Moser 不变量构造概要

**步骤 1：法式化**。利用双全纯变换将 $M$ 在 $p$ 处化为法式
$$\text{Im}\, w = |z|^2 + \sum \varphi_\alpha(z, \bar{z}, \text{Re}\, w).$$

**步骤 2：消去低阶项**。通过适当选取全纯变换，消去 1, 2, 3 阶项，使余项从 4 阶开始。

**步骤 3：4 阶余项的不变性**。剩余 4 阶张量 $T_{\alpha \bar{\beta} \gamma \bar{\delta}}(p)$（Chern–Moser 张量）在允许的变换下不变，构成局部不变量。

**步骤 4：完备性**。Chern–Moser 证明 $T$ 及其高阶协变导数（关于 Tanaka–Webster 联络）构成完备不变量系。$\square$

### Boutet de Monvel 嵌入定理概要

通过构造 $M$ 上的 Szegő 投影与核函数，证明在"非球面"条件下，存在足够多 CR 函数的全纯延拓，将这些函数作为嵌入坐标。证明需要深入的微局部分析与 CR 上 $\bar{\partial}_b$ 算子的次椭圆估计。$\square$

## 五、应用与意义

CR 几何在现代数学与物理中具有独特地位：

1. **多复变函数论的自然边界**：域 $\Omega \subset \mathbb{C}^n$ 的边界 $\partial \Omega$ 自然为 CR 流形，其 CR 结构决定了 $\Omega$ 上的全纯函数性质。Levi 问题、$\bar{\partial}$-Neumann 问题等都依赖于边界 CR 结构。

2. **边界全纯不变量**：Chern–Moser 不变量是 CR 流形的基本局部不变量，对应于单复变中的"零"不变量（Riemann 映射定理使所有边界局部等价），体现多复变的"刚性"。

3. **偏微分方程**：CR 函数等价于 Kohn–Rossi $\bar{\partial}_b$ 算子的核。$\bar{\partial}_b$ 的次椭圆性是次椭圆 PDE 理论的典范例子，推动了 Hörmander 次椭圆算子理论。

4. **几何控制论与刚性**：Burns–Epstein、Ebenfelt 等的 CR 刚性定理、Loewner 链理论等在 CR 几何中发展，并在共形几何中产生对应物。

5. **物理学应用**：在广义相对论中，类空无穷远的 CR 结构（Penrose 的 $\mathscr{I}^+$）是基本不变量。在弦理论中，世界面 CR 结构与紧致化相关。

6. **工程与计算**：CR 流形理论在计算机视觉（形状分析）、信号处理（多线性系统）有应用。CR 嵌入定理为高维数据降维提供几何框架。
