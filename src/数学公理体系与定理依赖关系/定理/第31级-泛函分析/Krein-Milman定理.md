# Krein-Milman定理

> **一句话大白话**：局部凸空间中每个凸紧集都能由它的"顶点"（极端点）拉起来重建——不管集合多古怪，端点足以把整个集合"撑"出来。
>
> **小例子**：一个三角形凸包的所有点都能由其三个顶点的凸组合生成；Krein-Milman正是说，任意凸紧集就是它极端点的凸包，只需收集"尖角点"即可。

## 介绍

Krein-Milman定理是泛函分析中关于凸集结构的核心定理。它断言：在局部凸拓扑向量空间中，一个紧致凸集等于其端点集的凸闭包。换言之，任何紧致凸集都可以由它的"角点"（端点）完全重构出来。这个定理揭示了凸集的极端结构，在泛函分析、Banach空间几何、优化理论和 Choquet 理论中具有基础性的地位。

## 分析

**定理的精确表述**：设 $X$ 是局部凸拓扑向量空间，$K \subset X$ 是非空紧致凸集。则

$$
K = \overline{\operatorname{conv}}(\operatorname{ext}(K)),
$$

其中 $\operatorname{ext}(K)$ 表示 $K$ 的端点集，$\overline{\operatorname{conv}}$ 表示凸闭包。

**端点定义**：$x \in K$ 称为 $K$ 的端点，若 $x = \lambda y + (1-\lambda)z$ 对某个 $y, z \in K$ 和 $\lambda \in (0,1)$ 成立，则必有 $x = y = z$。

**关键要点**：

- 紧致性条件是本质的——非紧致凸集可能没有端点（例如 $\mathbb{R}^2$ 中的开圆盘），或者端点集太小。
- 局部凸拓扑向量空间是定理成立所需的最一般框架。
- 定理的逆不成立：给定端点集，凸闭包不一定等于原来的集合（但若原集合是紧致凸集，则成立）。
- 在有限维空间中，这是 Minkowski 定理（每个紧致凸集是它顶点的凸组合）的推广。

## 思考过程

Krein-Milman定理的证明使用 Zorn 引理和 Hahn-Banach 分离定理，分两个主要步骤：

1. **存在性**：证明 $K$ 至少有一个端点。这通过考虑 $K$ 中关于某个连续线性泛函取最大值的点集（称为"暴露点"），并利用 Zorn 引理证明存在极小闭凸面，其端点就是 $K$ 的端点。

2. **重构性**：证明 $K$ 等于端点集的凸闭包。假设存在 $x_0 \in K$ 不在凸闭包中，则用 Hahn-Banach 分离定理分离 $x_0$ 和该凸闭包，再利用泛函的最大值点构造端点，导出矛盾。

## 证明过程

**证明**：设 $X$ 是局部凸拓扑向量空间，$K \subset X$ 是非空紧致凸集。

**引理 1**：$K$ 至少有一个端点。

**证明**：设 $\mathcal{F}$ 是 $K$ 的所有非空闭凸面（face）的集合，按包含关系偏序。由于 $K \in \mathcal{F}$，$\mathcal{F}$ 非空。若 $\{F_\alpha\}$ 是 $\mathcal{F}$ 中的全序链，则 $\bigcap_\alpha F_\alpha$ 非空（因为 $K$ 紧致且 $F_\alpha$ 是闭集，有限交性质保证非空），且是闭凸面。故 $\bigcap_\alpha F_\alpha$ 是链的下界。由 Zorn 引理，$\mathcal{F}$ 中存在极小元 $F_0$。

若 $F_0$ 不是单点集，则存在 $x \neq y \in F_0$。取 $f \in X^*$ 使得 $f(x) \neq f(y)$（Hahn-Banach 定理保证这种泛函存在）。令 $M = \max_{z \in F_0} f(z)$，则 $F' = \{z \in F_0 \mid f(z) = M\}$ 是 $F_0$ 的真闭凸面，与 $F_0$ 的极小性矛盾。故 $F_0$ 是单点集 $\{x_0\}$，$x_0$ 是端点。$\square$

**引理 2**：$\operatorname{ext}(K)$ 非空。

直接由引理 1 得到。

**主定理证明**：设 $C = \overline{\operatorname{conv}}(\operatorname{ext}(K))$。显然 $C \subset K$（因为 $K$ 是闭凸集且包含所有端点）。假设存在 $x_0 \in K \setminus C$。

由 Hahn-Banach 分离定理（局部凸空间中，点与闭凸集可分离），存在连续线性泛函 $f \in X^*$ 和 $\alpha \in \mathbb{R}$ 使得

$$
f(x_0) < \alpha \le f(c), \quad \forall c \in C.
$$

令 $M = \max_{x \in K} f(x)$（最大值在紧致集 $K$ 上达到），则 $M \ge \alpha$。定义

$$
K_f = \{x \in K \mid f(x) = M\}.
$$

$K_f$ 是非空闭凸面（称为 $K$ 关于 $f$ 的暴露面）。由引理 1，$K_f$ 包含端点。但 $K_f$ 的端点也是 $K$ 的端点（因为 $K_f$ 是 $K$ 的凸面），故 $\operatorname{ext}(K) \cap K_f \neq \varnothing$。

取 $e \in \operatorname{ext}(K) \cap K_f$，则 $f(e) = M \ge \alpha$。但 $e \in \operatorname{ext}(K) \subset C$，故 $f(e) \ge \alpha$，而 $f(x_0) < \alpha$。这与 $f(e) = \max_{x \in K} f(x) \ge f(x_0)$ 并不直接矛盾——真正的矛盾在于：$e \in C$ 意味着 $f(e) \ge \alpha$，但 $f(x_0) < \alpha$ 且 $x_0 \in K$，而 $f(e) = \max_K f \ge f(x_0)$，所以 $f(e) \ge f(x_0)$ 是自动成立的。我们需要重新审视。

更准确地：$x_0 \in K \setminus C$，由分离定理，存在 $f \in X^*$ 使得

$$
f(x_0) > \sup_{c \in C} f(c).
$$

由于 $f$ 在 $K$ 上达到最大值 $M$，且 $x_0 \in K$，故 $M \ge f(x_0) > \sup_C f$。令 $K_f = \{x \in K \mid f(x) = M\}$，则 $K_f \cap C = \varnothing$（因为 $C$ 上所有点的 $f$ 值都小于 $M$）。但 $K_f$ 是闭凸面，由引理 1 包含端点，而这些端点既是 $K_f$ 的端点也是 $K$ 的端点，故 $\operatorname{ext}(K) \cap K_f \neq \varnothing$，从而 $\operatorname{ext}(K) \cap K_f \subset C \cap K_f = \varnothing$，矛盾。因此 $K = C$。$\square$

**推论（Minkowski 定理）**：有限维空间中，紧致凸集等于其端点集的凸组合。

**应用**：Krein-Milman 定理在 $C^*$-代数理论中用于证明状态空间的结构定理，在 Banach 空间几何中用于刻画各种空间的单位球结构。