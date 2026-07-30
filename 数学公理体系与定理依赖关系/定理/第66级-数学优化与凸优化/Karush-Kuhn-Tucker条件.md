# Karush-Kuhn-Tucker条件

## 一、定理介绍

Karush-Kuhn-Tucker（KKT）条件是约束优化问题中判断局部最优解的一组一阶必要条件。它推广了 Lagrange 乘数法，适用于同时含不等式约束与等式约束的问题。在凸优化问题且满足某种约束规范（如 Slater 条件）时，KKT 条件成为最优解的充分必要条件。

## 二、原理思路

1. 在最优解处，目标函数的梯度应能由活跃约束梯度的线性组合表示。
2. 不等式约束的乘子非负，且与约束函数值满足互补松弛条件 $\lambda_i g_i(x) = 0$。
3. 等式约束的乘子符号不受限制。
4. 对于凸问题，KKT 条件不仅是必要的，而且是充分的。

## 三、定理的严格表述

考虑优化问题

$$
\begin{aligned}
\min_{x \in \mathbb{R}^n} \quad & f(x) \\
\mathrm{s.t.} \quad & g_i(x) \leq 0, \quad i=1,\dots,m, \\
& h_j(x) = 0, \quad j=1,\dots,p,
\end{aligned}
$$

其中 $f, g_i, h_j$ 可微。

**KKT 条件**：点 $x^*$ 与乘子 $\lambda^* \in \mathbb{R}^m$、$\nu^* \in \mathbb{R}^p$ 满足

1. **平稳性（stationarity）**：

$$
\nabla f(x^*) + \sum_{i=1}^m \lambda_i^* \nabla g_i(x^*) + \sum_{j=1}^p \nu_j^* \nabla h_j(x^*) = 0.
$$

2. **原始可行性（primal feasibility）**：

$$
g_i(x^*) \leq 0 \quad (i=1,\dots,m), \qquad h_j(x^*) = 0 \quad (j=1,\dots,p).
$$

3. **对偶可行性（dual feasibility）**：

$$
\lambda_i^* \geq 0 \quad (i=1,\dots,m).
$$

4. **互补松弛性（complementary slackness）**：

$$
\lambda_i^* g_i(x^*) = 0 \quad (i=1,\dots,m).
$$

**KKT 必要性定理**：若 $x^*$ 为局部最优解，且某约束规范（如 LICQ、MFCQ 或 Slater 条件）成立，则存在 $(\lambda^*,\nu^*)$ 使上述 KKT 条件成立。

**KKT 充分性定理**：若 $f, g_i$ 为凸函数，$h_j$ 为仿射函数，且 $(x^*,\lambda^*,\nu^*)$ 满足 KKT 条件，则 $x^*$ 为全局最优解。

## 四、证明过程

**必要性**：设 $x^*$ 为局部最优解且某种约束规范成立。考虑在 $x^*$ 处的线性化可行方向锥。由局部最优的必要条件，目标函数沿任何可行方向的导数非负。Farkas 引理说明这一条件等价于存在非负乘子 $\lambda_i^* \geq 0$ 与任意乘子 $\nu_j^* \in \mathbb{R}$ 使得平稳性成立。互补松弛性来自活跃约束 $g_i(x^*)=0$ 与非活跃约束对应 $\lambda_i^*=0$ 的构造。

**充分性（凸情形）**：设 $f, g_i$ 凸、$h_j$ 仿射，$(x^*,\lambda^*,\nu^*)$ 满足 KKT 条件。对任意可行点 $x$，由凸性的一阶条件，

$$
f(x) \geq f(x^*) + \nabla f(x^*)^\top (x-x^*).
$$

利用平稳性替换 $\nabla f(x^*)$ 得

$$
\begin{aligned}
f(x) &\geq f(x^*) - \sum_{i=1}^m \lambda_i^* \nabla g_i(x^*)^\top (x-x^*) - \sum_{j=1}^p \nu_j^* \nabla h_j(x^*)^\top (x-x^*) \\
&\geq f(x^*) - \sum_{i=1}^m \lambda_i^* \bigl(g_i(x)-g_i(x^*)\bigr) - \sum_{j=1}^p \nu_j^* \bigl(h_j(x)-h_j(x^*)\bigr) \\
&= f(x^*) - \sum_{i=1}^m \lambda_i^* g_i(x) \geq f(x^*).
\end{aligned}
$$

其中第二个不等式再次利用凸性，等式利用互补松弛与等式约束可行性，最后的不等式利用 $\lambda_i^* \geq 0$ 与 $g_i(x) \leq 0$。故 $x^*$ 为全局最优解。

## 五、应用与意义

- KKT 条件是求解约束优化问题的代数判据，广泛应用于工程、经济与金融模型。
- 在凸优化中，KKT 条件与强对偶性等价：原问题与对偶问题解满足 KKT 条件当且仅当二者均最优且强对偶成立。
- 许多算法（如内点法、增广 Lagrange 法、序列二次规划）都以寻找满足 KKT 条件的点为目标。
- KKT 条件为经济学中的边际分析与定价提供了数学表达。
