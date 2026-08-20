# Stone-Weierstrass定理

> **一句话大白话**：只要一族连续函数"分得开点、不全部等于零、对逼近封闭（含常数且对线性组合和乘积封闭）"，它就能均匀逼近任何连续函数——基本就是"多项式可以面无表情逼近一切"的宏大升级版。
>
> **小例子**：经典韦尔斯特拉斯说多项式能均匀逼近 $[a,b]$ 上任意连续函数；Stone-Weierstrass把这家伙推广:只含常数且分离点的代数都能逼近所有连续函数，例如用"三角多项式"逼近周期函数。

## 介绍

Stone-Weierstrass定理是逼近论中最重要的定理之一，由 Marshall Stone 在 1937 年推广了 Weierstrass 逼近定理而得到。它断言：在紧致 Hausdorff 空间 $X$ 上，如果 $C(X)$ 的一个子代数 $A$ 分离点、包含常数函数且在共轭下封闭（复情形），则 $A$ 在 $C(X)$ 中一致稠密。这个定理揭示了连续函数空间的结构，是函数逼近理论、C*-代数理论和拓扑学的基础工具。

## 分析

**定理的精确表述（实版本）**：设 $X$ 是紧致 Hausdorff 空间，$C(X, \mathbb{R})$ 是所有实值连续函数在一致范数下构成的 Banach 代数。设 $A \subset C(X, \mathbb{R})$ 是子代数，满足：

1. **分离点**：对任意不同的 $x, y \in X$，存在 $f \in A$ 使得 $f(x) \neq f(y)$；
2. **包含常数**：常数函数 $1$ 属于 $A$。

则 $A$ 在 $C(X, \mathbb{R})$ 中一致稠密，即 $\overline{A} = C(X, \mathbb{R})$。

**复版本**：设 $X$ 是紧致 Hausdorff 空间，$C(X, \mathbb{C})$ 是复值连续函数空间。设 $A \subset C(X, \mathbb{C})$ 是子代数，满足分离点条件、包含常数函数，且对共轭封闭（即若 $f \in A$，则 $\bar{f} \in A$）。则 $A$ 在 $C(X, \mathbb{C})$ 中一致稠密。

**关键要点**：

- 分离点条件是本质的——若不分离点，则 $A$ 只能逼近那些在 $X$ 的某个等价关系下不变的函数。
- 包含常数函数也是必要的——否则 $A$ 只能逼近在某个点取零值的函数。
- 复版本中需要共轭封闭条件，否则存在反例（例如 $X$ 是单位圆盘，$A$ 是多项式代数，它不能逼近 $\bar{z}$）。
- 经典 Weierstrass 逼近定理（多项式在闭区间上一致逼近连续函数）是 Stone-Weierstrass 定理的特例。

## 思考过程

Stone-Weierstrass 定理的证明（以实版本为例）分为几个层面：

1. **构造格点函数**：首先证明 $A$ 在逐点格点运算下封闭——即对任意 $f \in \overline{A}$，$|f| \in \overline{A}$。这需要构造一列多项式一致逼近绝对值函数。

2. **逼近上半连续函数**：利用分离点条件和常数函数，可以构造 $A$ 中的函数逼近任意特征函数（通过 Urysohn 引理的思想），然后逼近任意连续函数。

3. **Kakutani-Krein 定理的证明思路**：另一种证明是利用 $A$ 的闭包 $\overline{A}$ 是 $C(X)$ 的闭子代数，且满足分离点、包含常数条件。对任意 $f \in C(X)$ 和 $\varepsilon > 0$，对每个 $x \in X$，存在 $g_x \in \overline{A}$ 使得 $g_x(x) = f(x)$。由连续性，存在邻域 $U_x$ 使得 $g_x(y) > f(y) - \varepsilon$ 在 $U_x$ 上成立。由紧致性，有限覆盖，取这些 $g_x$ 的最大值（由格点性质，最大值仍在 $\overline{A}$ 中），得到 $h_\varepsilon \in \overline{A}$ 满足 $h_\varepsilon > f - \varepsilon$。类似地，从下方逼近，最终得到 $f \in \overline{A}$。

## 证明过程

**证明**：我们给出实版本的证明。

**引理 1**：存在多项式列 $p_n(t)$ 在 $[-1, 1]$ 上一致收敛到 $|t|$，且 $p_n(0) = 0$。

**证明**：考虑 $|t| = \sqrt{t^2} = \sqrt{1 - (1 - t^2)}$。由二项式展开，$\sqrt{1 - s} = 1 - \sum_{k=1}^\infty c_k s^k$，在 $[0, 1]$ 上一致收敛。取部分和即可构造 $p_n$。$\square$

**引理 2**：若 $A$ 是满足条件的闭子代数，则对任意 $f \in A$，$|f| \in A$。

**证明**：对 $f \in A$，存在 $M$ 使得 $|f| \le M$。令 $g = f/M \in A$，则 $|g| \le 1$。由引理 1，$p_n(g) \to |g|$ 一致收敛，且 $p_n(g) \in A$（因为 $A$ 是代数）。故 $|g| \in \overline{A} = A$，从而 $|f| = M|g| \in A$。$\square$

**推论**：若 $f, g \in A$，则 $\max(f, g) = \frac{1}{2}(f + g + |f - g|) \in A$，$\min(f, g) = \frac{1}{2}(f + g - |f - g|) \in A$。

**主定理证明**：设 $A$ 是满足分离点条件和包含常数条件的闭子代数（否则取闭包）。需要证明 $A = C(X)$。

对任意 $f \in C(X)$ 和 $\varepsilon > 0$，我们构造 $h \in A$ 使得 $\|f - h\|_\infty < \varepsilon$。

**步骤 1**：对任意 $x \in X$，存在 $g_x \in A$ 使得 $g_x(x) = f(x)$。由分离点条件和常数函数，对任意 $y \neq x$，存在 $h_{xy} \in A$ 使得 $h_{xy}(x) \neq h_{xy}(y)$。令

$$
g_{xy}(z) = \frac{f(x) - f(y)}{h_{xy}(x) - h_{xy}(y)}(h_{xy}(z) - h_{xy}(x)) + f(x),
$$

则 $g_{xy} \in A$，$g_{xy}(x) = f(x)$，$g_{xy}(y) = f(y)$。

**步骤 2**：固定 $x$。对每个 $y \neq x$，存在邻域 $U_y$ 使得 $g_{xy}(z) > f(z) - \varepsilon$ 对所有 $z \in U_y$ 成立。$\{U_y\}_{y \neq x} \cup \{x\}$ 覆盖 $X$，由紧致性，存在有限子覆盖 $U_{y_1}, \ldots, U_{y_n}$。令 $g_x = \max(g_{xy_1}, \ldots, g_{xy_n}) \in A$，则 $g_x(x) = f(x)$，且 $g_x(z) > f(z) - \varepsilon$ 对所有 $z \in X$ 成立。

**步骤 3**：对每个 $x \in X$，取邻域 $V_x$ 使得 $g_x(z) < f(z) + \varepsilon$ 对所有 $z \in V_x$ 成立（由 $g_x$ 和 $f$ 的连续性及 $g_x(x) = f(x)$）。$\{V_x\}_{x \in X}$ 覆盖 $X$，由紧致性，存在有限子覆盖 $V_{x_1}, \ldots, V_{x_m}$。令 $h = \min(g_{x_1}, \ldots, g_{x_m}) \in A$。

**步骤 4**：验证 $h$ 满足要求。对任意 $z \in X$，$z$ 属于某个 $V_{x_i}$，故 $g_{x_i}(z) < f(z) + \varepsilon$，从而 $h(z) \le g_{x_i}(z) < f(z) + \varepsilon$。另一方面，每个 $g_{x_j}(z) > f(z) - \varepsilon$，故 $h(z) > f(z) - \varepsilon$。因此 $\|h - f\|_\infty < \varepsilon$。$\square$

**复版本证明概要**：设 $A$ 是满足分离点、包含常数和共轭封闭条件的复子代数。令 $A_{\mathbb{R}} = \{ \operatorname{Re} f \mid f \in A \}$，则 $A_{\mathbb{R}}$ 是实值连续函数子代数，满足分离点和包含常数条件。由实版本，$A_{\mathbb{R}}$ 在 $C(X, \mathbb{R})$ 中稠密。对任意 $f \in C(X, \mathbb{C})$，$f = u + iv$，$u, v \in C(X, \mathbb{R})$。存在 $u_n, v_n \in A_{\mathbb{R}}$ 逼近 $u, v$，则 $u_n + i v_n \in A$ 逼近 $f$。$\square$

**应用**：三角多项式在 $C([0, 2\pi])$ 中一致稠密（Weierstrass 三角逼近定理）。这直接来自 Stone-Weierstrass 定理：取 $A$ 为由 $\{e^{inx}\}_{n \in \mathbb{Z}}$ 张成的代数，它分离点、包含常数、共轭封闭。