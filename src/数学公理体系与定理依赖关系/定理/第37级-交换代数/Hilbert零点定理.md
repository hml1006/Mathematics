# Hilbert零点定理

> **一句话大白话**：几何与代数的桥——一群多项式变零点构成的几何点集，其"代数根"（极值理想）与点集完全互相对应；"代数零点"与"几何零点"是同一件事，用代数算几何从此有据。
>
> **小例子**：在 $\mathbb{C}[x,y]$ 中多项式 $x^2+y^2$ 与 $\{x,y\}$ 在点 $(0,0)$ 处均有零点，而零点定理保证几何点集与完整版极值理想一一配对，如圆方程 $x^2+y^2=1$ 对应极值理想 $\langle x^2+y^2-1\rangle$。

## 介绍

Hilbert零点定理（Hilbert's Nullstellensatz）是代数几何中最基本的定理之一，由大卫·希尔伯特于 1893 年证明。该定理建立了多项式环中的理想与仿射空间中的代数集之间的一一对应关系，是代数几何中"字典"的核心部分。零点定理的德文名称"Nullstellensatz"字面意为"零点位置定理"，它精确刻画了多项式方程组有公共零点的条件。

## 分析

**前置依赖**：多项式环、理想、代数集、诺特环、Hilbert 基定理、域扩张。

**数学内涵**：

**定理内容**：设 $k$ 是代数闭域，$I \subseteq k[x_1, \ldots, x_n]$ 是理想。

1. **弱零点定理**：若 $I \ne k[x_1, \ldots, x_n]$，则 $V(I) \ne \varnothing$（即 $I$ 中的多项式在 $\mathbb{A}^n_k$ 中有公共零点）。
2. **强零点定理**：$I(V(I)) = \sqrt{I}$，其中 $\sqrt{I} = \{f \in k[x_1, \ldots, x_n] \mid f^m \in I \text{ 对某个 } m \ge 1\}$ 是 $I$ 的根。

**数学内涵**：零点定理建立了代数集与根理想之间的一一对应：
$$
\{\text{仿射代数集}\} \longleftrightarrow \{\text{根理想}\}
$$
这为代数几何奠定了理论基础。

**证明策略**：
- 弱零点定理：利用 Rabinowitsch 技巧或通过域扩张和 Zariski 引理。
- 强零点定理：通过 Rabinowitsch 技巧归结为弱零点定理。

## 思考过程

Hilbert零点定理的弱形式回答了一个基本问题：一组多项式方程何时有解？答案是：除非这组方程本身矛盾（即生成整个环），否则它们一定有公共零点。

强形式则更进一步：如果一个多项式 $f$ 在 $V(I)$ 的所有点上为零，那么 $f$ 的某个幂一定属于 $I$。这精确刻画了"在代数集上为零"这一几何概念所对应的代数对象。

Rabinowitsch 技巧是证明中的关键：通过引入一个新变量将问题转化为弱零点定理的形式。

## 证明过程

### Zariski 引理

**引理**（Zariski）：设 $k$ 是域，$L/k$ 是有限生成的域扩张。若 $L$ 是域，则 $L/k$ 是有限代数扩张（从而 $L$ 是 $k$ 的有限扩张）。

**证明**：用反证法。假设 $L = k(x_1, \ldots, x_n)$ 不是 $k$ 的有限代数扩张，则存在超越元。通过分析 $k[x_1, \ldots, x_n]$ 中的极大理想可导出矛盾。$\square$

### 弱零点定理

**定理 1**（弱零点定理）：设 $k$ 是代数闭域，$I \subseteq k[x_1, \ldots, x_n]$ 是真理想（$I \ne k[x_1, \ldots, x_n]$）。则 $V(I) \ne \varnothing$。

**证明**：

**步骤 1**：设 $I$ 是真理想，则 $I$ 包含在某个极大理想 $\mathfrak{m}$ 中。由 Hilbert 基定理，$k[x_1, \ldots, x_n]$ 是诺特环，故极大理想存在。

**步骤 2**：考虑商域 $L = k[x_1, \ldots, x_n]/\mathfrak{m}$。$L$ 是域，且 $L/k$ 是有限生成的（作为 $k$-代数）。由 Zariski 引理，$L/k$ 是有限代数扩张。

**步骤 3**：由于 $k$ 是代数闭域，$L/k$ 的有限代数扩张只能是 $L = k$。因此 $k[x_1, \ldots, x_n]/\mathfrak{m} \cong k$。

**步骤 4**：设 $\varphi: k[x_1, \ldots, x_n] \to k$ 是商映射，则对每个 $f \in I \subseteq \mathfrak{m}$，$\varphi(f) = 0$。令 $a_i = \varphi(x_i) \in k$，则对任意 $f \in I$，$f(a_1, \ldots, a_n) = 0$。故 $(a_1, \ldots, a_n) \in V(I)$，$V(I) \ne \varnothing$。$\square$

### 强零点定理

**定理 2**（强零点定理）：设 $k$ 是代数闭域，$I \subseteq k[x_1, \ldots, x_n]$ 是理想。则 $I(V(I)) = \sqrt{I}$。

**证明**：

显然 $\sqrt{I} \subseteq I(V(I))$（若 $f^m \in I$，则 $f$ 在 $V(I)$ 上为零）。需要证明 $I(V(I)) \subseteq \sqrt{I}$。

设 $f \in I(V(I))$，即 $f$ 在 $V(I)$ 的所有点上为零。需要证明 $f \in \sqrt{I}$，即存在 $m \ge 1$ 使得 $f^m \in I$。

**Rabinowitsch 技巧**：引入新变量 $y$，考虑扩大的多项式环 $k[x_1, \ldots, x_n, y]$ 中的理想：
$$
J = \langle I, 1 - y f \rangle
$$
其中 $I$ 视为 $k[x_1, \ldots, x_n, y]$ 中的理想（由 $I$ 中多项式生成，不涉及 $y$）。

**断言**：$J = k[x_1, \ldots, x_n, y]$，即 $1 \in J$。

*证明*：假设 $J$ 是真理想，则由弱零点定理，存在 $(a_1, \ldots, a_n, b) \in \mathbb{A}^{n+1}_k$ 使得 $J$ 中所有多项式在该点为零。特别地，对所有 $g \in I$，$g(a_1, \ldots, a_n) = 0$，故 $(a_1, \ldots, a_n) \in V(I)$。又 $1 - b f(a_1, \ldots, a_n) = 0$，但 $f(a_1, \ldots, a_n) = 0$（因为 $f \in I(V(I))$），故 $1 = 0$，矛盾。因此 $J = k[x_1, \ldots, x_n, y]$。$\square$

由断言，存在 $h_i, g_j \in k[x_1, \ldots, x_n, y]$ 和 $f_i \in I$ 使得：
$$
1 = \sum_i h_i f_i + g(1 - y f)
$$
考虑映射 $y \mapsto 1/f$，在 $k[x_1, \ldots, x_n, f^{-1}]$ 中，上式变为：
$$
1 = \sum_i h_i(x_1, \ldots, x_n, 1/f) f_i
$$
乘以 $f^m$ 消去分母（$m$ 充分大），得 $f^m \in I$。故 $f \in \sqrt{I}$。$\square$

### 推论

**推论 1**（代数集与根理想的一一对应）：设 $k$ 是代数闭域，则映射
$$
V: \{\text{根理想} \subseteq k[x_1, \ldots, x_n]\} \longleftrightarrow \{\text{仿射代数集} \subseteq \mathbb{A}^n_k\}: I
$$
是一一对应，且包含关系反转。

**推论 2**（极大理想）：
1. $k[x_1, \ldots, x_n]$ 中的极大理想一一对应于 $\mathbb{A}^n_k$ 中的点。
2. 每个极大理想形如 $\mathfrak{m} = \langle x_1 - a_1, \ldots, x_n - a_n \rangle$，其中 $(a_1, \ldots, a_n) \in \mathbb{A}^n_k$。

**应用**：Hilbert零点定理是代数几何的基石，建立了代数与几何之间的"字典"，为代数簇理论奠定了基础。$\square$