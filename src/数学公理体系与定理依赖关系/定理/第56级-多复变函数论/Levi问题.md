# Levi问题

> **一句话大白话**：问"什么样开区域才是全纯域（每个解析地定义的对象都能全域延拓）"？答案：只要区域是"伪凸的"（边界向里凹/满足 Levi 条件是充分合适的），——把'能在界上维持的光滑性'与'能否全域全纯延拓'划上等号，是多复变的根本判定问题。
>
> **小例子**：如 $\mathbb{C}^2$ 里的厚"环体"型区域因中心向里凹往往非全纯域；Levi问题断言——区域是全纯域 ⇔ 它伪凸（在边界内点附近有光滑定义函数时其 Levi 形式半正定），多复变从此把"几何凸性"与"全纯延拓能力"绑定。

## 一、定理介绍

> **前置依赖**：全纯凸性、Levi 形式与伪凸性、多重次调和穷竭函数、Hartogs 现象、$\bar{\partial}$ 方程的 $L^2$ 估计。

Levi 问题（Levi Problem）是多复变函数论中最核心的问题之一，由 Eugenio Elia Levi 于 1911 年提出。它探讨的是：**伪凸性是否等价于全纯凸性**，即伪凸域上是否存在足够多的全纯函数。

在单复变中，任何开集 $\Omega \subset \mathbb{C}$ 都是全纯凸的（由黎曼映射定理或更基本的构造可知），因此伪凸性与全纯凸性的等价性问题并不显现。但在多复变中，由于 Hartogs 现象等特有现象的出现，区域上的全纯函数性质变得复杂而深刻。Levi 问题揭示了多复变函数论中几何条件（伪凸性）与分析条件（全纯凸性）之间的深层等价关系，是连接几何、分析与拓扑的桥梁。

该问题历经四十余年，最终由 Oka（1953）、Bremermann（1954）、Norguet（1954）等人独立给出肯定回答。

## 二、原理思路

Levi 问题的核心思想是将"几何凸性"与"全纯函数的存在性"联系起来。

**关键观察**：
1. 在 $\mathbb{C}^n$ 中，并非所有开集都拥有丰富的全纯函数。Hartogs 现象表明，某些区域上的全纯函数会自动延拓到更大的区域，从而原区域上"无新的"全纯函数。
2. 全纯凸性（holomorphic convexity）是分析条件：区域 $\Omega$ 是全纯凸的，指对任意紧集 $K \subset \Omega$，其全纯凸包 $\hat{K}_\Omega = \{z \in \Omega : |f(z)| \leq \sup_K |f|, \forall f \in \mathcal{O}(\Omega)\}$ 仍是紧的。
3. 伪凸性（pseudoconvexity）是几何条件：由 Levi 形式刻画，反映边界附近的全纯凸性质。

**证明思路**：
- 证明全纯凸域一定是伪凸域（较容易的方向）。
- 反方向（伪凸域 $\Rightarrow$ 全纯凸域）是核心难题。需要构造足够多的全纯函数，使全纯凸包有界。常用方法包括 Oka 的层次构造、$L^2$ 估计（Hörmander）、以及 $\bar{\partial}$ 方程的求解。

## 三、定理的严格表述

**Levi 问题的解（Levi–Oka 定理）**：设 $\Omega \subset \mathbb{C}^n$ 是开集，则以下条件等价：

1. （全纯凸性）$\Omega$ 是全纯凸的，即对任意紧集 $K \subset \Omega$，全纯凸包
   $$\hat{K}_\Omega = \{z \in \Omega : |f(z)| \leq \sup_K |f|, \ \forall f \in \mathcal{O}(\Omega)\}$$
   在 $\Omega$ 中是紧的。

2. （Levi 伪凸性）$\Omega$ 是 Levi 伪凸的。即存在一个 $C^2$ 的穷竭函数 $\varphi: \Omega \to \mathbb{R}$（即 $\{z \in \Omega : \varphi(z) < c\}$ 对所有 $c$ 都相对紧），使得 Levi 形式
   $$L_\varphi(z; \xi) = \sum_{j,k=1}^{n} \frac{\partial^2 \varphi}{\partial z_j \partial \bar{z}_k}(z) \xi_j \bar{\xi}_k \geq 0, \quad \forall z \in \Omega, \ \xi \in \mathbb{C}^n$$
   即 $\varphi$ 是多重次调和的。

3. （边界局部伪凸性，当 $\Omega$ 有 $C^2$ 边界时）在每点 $p \in \partial \Omega$，Levi 形式 $L_\rho(p; \cdot)$ 在复切空间上非负，其中 $\rho$ 是局部定义函数。

更精确地，Levi 问题断言：**伪凸域必为全纯凸域**（另一个方向较直接）。

## 四、证明过程

**证明概要**（采用 Oka 方法与 Hörmander 的 $L^2$ 方法的精神）：

### 方向一：全纯凸 $\Rightarrow$ Levi 伪凸性

设 $\Omega$ 全纯凸。利用全纯凸性可构造一个连续的穷竭函数，并通过 Levi-Krzoska 定理或直接利用全纯函数族族的正则性，得到多重次调和穷竭函数，从而 $\Omega$ 是伪凸的。

### 方向二：Levi 伪凸 $\Rightarrow$ 全纯凸（核心难点）

设 $\Omega$ 是 Levi 伪凸域。需证：对任意紧集 $K \subset \Omega$ 及任意点 $p \in \Omega \setminus \hat{K}_\Omega$，存在 $f \in \mathcal{O}(\Omega)$ 使 $|f(p)| > \sup_K |f|$，并证明 $\hat{K}_\Omega$ 紧。

**步骤 1（穷竭函数的多重次调和性）**：由伪凸性，存在光滑的多重次调和穷竭函数 $\varphi$。可假设 $\varphi$ 严格多次调和且 $\varphi \to +\infty$（当 $z \to \partial \Omega$ 或 $|z| \to \infty$）。

**步骤 2（$\bar{\partial}$ 方程的可解性）**：利用 Hörmander 的 $L^2$ 理论。给定 $(0,1)$-形式 $g = \sum_j g_j \, d\bar{z}_j$ 满足 $\bar{\partial} g = 0$，存在 $u$ 使
$$\bar{\partial} u = g, \qquad \int_\Omega |u|^2 e^{-\varphi} \, dV \leq \int_\Omega |g|^2 e^{-\varphi} \, dV,$$
其中 $\varphi$ 为多重次调和穷竭函数。这一 $L^2$ 估计是关键工具。

**步骤 3（全纯函数的构造）**：对 $p \in \Omega$ 与紧集 $K$，希望构造 $f \in \mathcal{O}(\Omega)$ 使 $|f(p)| > \sup_K |f|$。利用 $\bar{\partial}$ 方法的标准技巧：先构造近似全纯的函数（带极点的"芽"），再用 $\bar{\partial}$ 方程修正其非全纯部分，得到真正的全纯函数。

具体地，考虑权函数 $\varphi_N = N \log |z - p|^2 + \varphi$，通过求解 $\bar{\partial}$ 方程消去奇点，构造 $f$ 满足在 $p$ 处取大值、在 $K$ 上保持有界的全纯函数。

**步骤 4（紧致性）**：由 $\varphi$ 为穷竭函数，对紧集 $K$，存在 $c$ 使 $K \subset \{\varphi \leq c\}$。利用极值原理性质可证 $\hat{K}_\Omega \subset \{\varphi \leq c\}$，从而 $\hat{K}_\Omega$ 有界且闭于 $\Omega$，故紧。

**步骤 5**：综上，$\hat{K}_\Omega$ 紧，即 $\Omega$ 全纯凸。$\square$

历史注：Oka 利用 Weierstrass 预备定理与"准逆"（ inverse de Oka）构造性地证明了该结论（针对无界域需先经修改），Bremermann 利用核函数与逼近，Norguet 利用 $\bar{\partial}$ 技巧。1955 年后，Hörmander 引入的 $L^2$ 估计给出最为简洁统一的证明。

## 五、应用与意义

Levi 问题的解决具有深远影响：

1. **理论意义**：它确立了多复变函数论中"几何（伪凸性）"与"分析（全纯函数存在性）"的等价性，是多复变理论成熟的标志之一。这一等价性使得我们可以从几何角度研究全纯函数论，反之亦然。

2. **Stein 流形理论的基础**：Levi 问题的结论是 Stein 流形理论的核心。Stein 流形即"全纯凸 + 全纯分离 + 局部全纯坐标"的复流形，本质上对应"非紧复流形上的 Levi 问题"。

3. **$\bar{\partial}$ 方程理论**：Levi 问题的现代证明（Hörmander 方法）直接推动了 $\bar{\partial}$-Neumann 问题的 $L^2$ 理论的发展，成为多复变与偏微分方程交汇的核心。

4. **复几何与代数几何**：在复几何中，Levi 问题的思想被推广到流形上的伪凸性（如 Grauert 的 Levi 问题），是紧 Kähler 流形、Stein 流形等理论的基础。

5. **应用领域**：在量子场论、弦理论中涉及的复几何结构，以及信号处理与控制论中的多复变方法，都依赖于 Levi 问题建立的几何—分析对应。
