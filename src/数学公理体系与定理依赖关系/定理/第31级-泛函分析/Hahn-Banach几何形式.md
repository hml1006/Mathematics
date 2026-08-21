# Hahn-Banach几何形式

> **一句话大白话**：两个"互不相交本来就没缘分"的凸集（或点与集），总能用一条平直的超平面把它们分开——平面代数里"画条线隔开两个灯泡"，推广到无限维也照样能做到。
>
> **小例子**：平面中任取一个不在凸集 $K$ 里的点，当 $K$ 凸且闭时，必能找到一条直线把点与 $K$ 严格隔开——这是"支撑/分离超平面"思想的雏形。

## 介绍

Hahn-Banach几何形式（也称为凸集分离定理）是泛函分析中最重要的几何结论之一。它断言：在赋范线性空间中，两个不相交的非空凸集（其中一个为开集）可以被一个闭超平面严格分离。这个定理本质上是 Hahn-Banach 延拓定理的几何化表述，它将线性泛函的延拓问题转化为凸集分离问题，为凸分析、优化理论和经济学的均衡理论提供了核心工具。

## 分析

**前置依赖**：Hahn-Banach 延拓定理、Minkowski 泛函（次线性泛函）、凸集与开集、线性泛函的连续性判别

**定理的精确表述**：设 $X$ 是赋范线性空间，$A, B \subset X$ 是非空凸集，$A \cap B = \varnothing$，$A$ 是开集。则存在非零连续线性泛函 $f \in X^*$ 和实数 $\alpha \in \mathbb{R}$ 使得

$$
f(a) < \alpha \le f(b), \quad \forall a \in A, \forall b \in B.
$$

这个超平面 $\{x \in X \mid f(x) = \alpha\}$ 称为分离超平面。

**更一般的形式**：若 $A$ 和 $B$ 都是闭凸集，$A$ 紧致，$B$ 闭，且 $A \cap B = \varnothing$，则存在 $f \in X^*$ 和 $\alpha, \beta \in \mathbb{R}$ 使得

$$
f(a) \le \alpha < \beta \le f(b), \quad \forall a \in A, \forall b \in B.
$$

**关键要点**：

- 定理的几何本质是：在凸集之间可以插入一个超平面。
- 分离的严格性（$f(a) < \alpha$ 而不是 $f(a) \le \alpha$）依赖于其中一个凸集是开的。
- 若两个凸集都是闭的且其中一个紧致，则可以得到严格分离（$f(a) \le \alpha < \beta \le f(b)$）。
- 在有限维空间中，两个不相交的凸集总可以被超平面分离（不一定严格）。

## 思考过程

几何形式的证明基于 Hahn-Banach 延拓定理，通过构造 Minkowski 泛函（一个由开凸集诱导的次线性泛函）来实现。

基本思路如下：

1. **构造 Minkowski 泛函**：对于开凸集 $A$ 包含原点，定义 $\mu_A(x) = \inf\{t > 0 \mid x \in tA\}$。这是一个次线性泛函，且 $A = \{x \mid \mu_A(x) < 1\}$。

2. **转化为延拓问题**：在某个一维子空间上定义线性泛函，使其被 Minkowski 泛函控制，然后用 Hahn-Banach 延拓定理延拓到整个空间。

3. **翻译为几何分离**：将延拓得到的线性泛函解释为分离超平面。

这个定理说明，分析中的延拓问题与几何中的分离问题本质上是等价的——这是 Hahn-Banach 定理深度的体现。

## 证明过程

**证明**：我们证明第一种形式（$A$ 开凸集，$A \cap B = \varnothing$，$A, B$ 凸）。

**步骤 1**：归化到 $A$ 包含原点。取 $a_0 \in A$，令 $A' = A - a_0 = \{a - a_0 \mid a \in A\}$，$B' = B - a_0 = \{b - a_0 \mid b \in B\}$。则 $0 \in A'$，$A'$ 是开凸集，$0 \notin B'$（因为 $A \cap B = \varnothing$）。

**步骤 2**：构造 Minkowski 泛函。对 $x \in X$，定义

$$
\mu(x) = \inf\{t > 0 \mid x \in tA'\}.
$$

验证 $\mu$ 是次线性泛函：$\mu(x + y) \le \mu(x) + \mu(y)$（因为若 $x \in tA'$，$y \in sA'$，则由凸性 $x + y \in (t+s)A'$），且 $\mu(\alpha x) = \alpha \mu(x)$ 对 $\alpha \ge 0$ 成立。此外，$A' = \{x \mid \mu(x) < 1\}$。

**步骤 3**：在 $B'$ 上定义线性泛函。取 $b_0 \in B'$（$b_0 \neq 0$），考虑一维子空间 $Y = \mathbb{R}b_0$。定义 $f: Y \to \mathbb{R}$ 为 $f(\alpha b_0) = \alpha \mu(b_0)$。则 $f$ 是线性泛函且在 $Y$ 上满足 $f(y) \le \mu(y)$（因为 $f(\alpha b_0) = \alpha \mu(b_0) = \mu(\alpha b_0)$ 对 $\alpha \ge 0$，而 $\alpha < 0$ 时 $f(\alpha b_0) = \alpha \mu(b_0) \le 0 \le \mu(\alpha b_0)$）。

**步骤 4**：延拓到整个空间。由 Hahn-Banach 延拓定理，存在线性泛函 $F: X \to \mathbb{R}$ 使得 $F|_Y = f$ 且 $F(x) \le \mu(x)$ 对所有 $x \in X$ 成立。

**步骤 5**：验证分离性质。由于 $F$ 连续（因为在包含原点的邻域上 $F(x) \le \mu(x) < 1$ 意味着 $F$ 有界），且：
- 对任意 $a \in A$，$a' = a - a_0 \in A'$，故 $\mu(a') < 1$，从而 $F(a') \le \mu(a') < 1$，即 $F(a) - F(a_0) < 1$。
- 对 $b_0 \in B'$，$F(b_0) = f(b_0) = \mu(b_0) \ge 1$（因为 $b_0 \notin A'$），故 $F(b_0) \ge 1$，即 $F(b_0 + a_0) - F(a_0) \ge 1$。

取 $\alpha = F(a_0) + 1$，则对任意 $a \in A$，$F(a) < \alpha$，而对任意 $b \in B$，$F(b) \ge \alpha$。由于 $A$ 是开集，可以进一步改进为严格不等式 $F(a) < \alpha$。

**步骤 6**：严格化。由于 $A$ 是开集，对任意 $a \in A$，存在邻域 $U_a \subset A$，由此可证 $F(a) < \alpha$。若存在 $a \in A$ 使得 $F(a) = \alpha$，则 $a$ 是 $A$ 的内点，存在邻域 $U$ 使得 $a \in U \subset A$，但 $F$ 在 $U$ 上取值可以大于 $\alpha$（因为 $F$ 非零），与 $F(A) \le \alpha$ 矛盾。故 $F(a) < \alpha$ 对所有 $a \in A$ 成立。$\square$

**推论（支撑超平面定理）**：设 $C$ 是闭凸集，$x_0 \notin C$，则存在 $f \in X^*$ 和 $\alpha \in \mathbb{R}$ 使得 $f(x_0) > \alpha$ 且 $f(x) \le \alpha$ 对所有 $x \in C$ 成立。