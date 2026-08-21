# 测地线与Jacobi场

> **一句话大白话**：测地线是曲面的"最直最短路"（走直线式地不拐弯），而Jacobi场则是"把一条测地线轻轻推一点"后另一条测地线的偏离响应——它们一起回答"两条近路会怎样散开或聚拢"，这是曲率最生活化的入口。
>
> **小例子**：在球面上取赤道作测地线，把经线向两侧轻推得到Jacobi场；沿测地线 $J''+R(J,\gamma')\gamma'=0$，场的大小增长正好写真曲率对"身边近路"的推挤与拉扯，散开/闭合由曲率符号决定。

## 介绍

测地线（Geodesic）和 Jacobi 场（Jacobi Field）是黎曼几何中研究流形局部和全局性质的核心工具。测地线是 Riemann 流形上"最直"的曲线，其切向量沿曲线平行移动，等价于满足测地线方程 $\nabla_{\dot{\gamma}} \dot{\gamma} = 0$ 的曲线。Jacobi 场是沿测地线的变分向量场，它描述了相邻测地线的偏离行为，满足 Jacobi 方程。Jacobi 场通过曲率张量刻画了测地线的"散开"或"聚拢"趋势，是比较定理、共轭点和割点理论的基础。

## 分析

**前置依赖**：Levi-Civita 联络与协变导数、Riemann 曲率张量、能量泛函的一阶与二阶变分、指数映射、二阶线性常微分方程理论。

**定义**：设 $(M, g)$ 是 Riemann 流形。

1. **测地线**：曲线 $\gamma: I \to M$ 称为测地线，如果 $\nabla_{\dot{\gamma}(t)} \dot{\gamma}(t) = 0$ 对所有 $t \in I$。在局部坐标下，测地线方程为
   $$
   \ddot{x}^k + \Gamma^k_{ij} \dot{x}^i \dot{x}^j = 0,
   $$
   其中 $\Gamma^k_{ij}$ 是 Christoffel 符号。

2. **Jacobi 场**：设 $\gamma$ 是测地线，沿 $\gamma$ 的向量场 $J(t)$ 称为 Jacobi 场，如果它满足 Jacobi 方程
   $$
   \nabla_{\dot{\gamma}} \nabla_{\dot{\gamma}} J + R(J, \dot{\gamma}) \dot{\gamma} = 0.
   $$

**依赖的概念**：Levi-Civita 联络、曲率张量、指数映射、变分法。

**核心性质**：
- 测地线是局部距离最短的曲线（在足够小的邻域内）。
- Jacobi 场对应于测地线的单参数变分，且 $J(t)$ 完全由初始条件 $J(0)$ 和 $\nabla_{\dot{\gamma}} J(0)$ 决定。
- 共轭点：沿测地线 $\gamma$ 的点 $\gamma(a)$ 和 $\gamma(b)$ 称为共轭的，如果存在非零 Jacobi 场 $J$ 使得 $J(a) = 0 = J(b)$。

## 思考过程

测地线和 Jacobi 场的关系可以通过变分微积分理解：考虑测地线 $\gamma$ 的一个变分 $\gamma_s(t)$，其中 $\gamma_0(t) = \gamma(t)$，变分向量场为 $J(t) = \partial_s \gamma_s(t)|_{s=0}$。能量泛函 $E(s) = \frac{1}{2} \int |\dot{\gamma}_s(t)|^2 dt$ 的一阶变分为零（因为 $\gamma$ 是测地线），二阶变分给出

$$
\frac{d^2}{ds^2}\Big|_{s=0} E(s) = \int \left( |\nabla_{\dot{\gamma}} J|^2 - R(J, \dot{\gamma}, \dot{\gamma}, J) \right) dt.
$$

Jacobi 方程正是这个二阶变分问题的 Euler-Lagrange 方程。因此，Jacobi 场刻画了测地线在变分下的"稳定性"。

## 证明过程

**定理**（Jacobi 场的变分刻画）：设 $\gamma: [0, L] \to M$ 是测地线，$\gamma_s(t)$ 是 $\gamma$ 的变分，变分向量场为 $J(t)$。则 $\gamma$ 的能量泛函的二阶变分为

$$
\frac{d^2}{ds^2}\Big|_{s=0} E(s) = \int_0^L \left( |\nabla_{\dot{\gamma}} J|^2 - R(J, \dot{\gamma}, \dot{\gamma}, J) \right) dt - g(\nabla_{\dot{\gamma}} J(0), J(0)) + g(\nabla_{\dot{\gamma}} J(L), J(L)).
$$

**证明**：

**步骤 1：一阶变分。**

设变分 $\gamma_s(t)$ 满足 $\gamma_0(t) = \gamma(t)$，$\partial_s \gamma_s(t)|_{s=0} = J(t)$。能量 $E(s) = \frac{1}{2} \int_0^L g(\dot{\gamma}_s, \dot{\gamma}_s) dt$，则

$$
E'(s) = \int_0^L g(\nabla_s \dot{\gamma}_s, \dot{\gamma}_s) dt = \int_0^L g(\nabla_t \partial_s \gamma_s, \dot{\gamma}_s) dt.
$$

利用 $\nabla_s \dot{\gamma}_s = \nabla_t \partial_s \gamma_s$，分部积分得

$$
E'(0) = g(J(L), \dot{\gamma}(L)) - g(J(0), \dot{\gamma}(0)) - \int_0^L g(J(t), \nabla_t \dot{\gamma}(t)) dt.
$$

由于 $\gamma$ 是测地线，$\nabla_t \dot{\gamma} = 0$，若固定端点则 $J(0) = J(L) = 0$，故 $E'(0) = 0$。

**步骤 2：二阶变分。**

计算 $E''(s)$，在 $s=0$ 处有

$$
E''(0) = \int_0^L \left( g(\nabla_t J, \nabla_t J) - g(R(J, \dot{\gamma})\dot{\gamma}, J) \right) dt + \text{边界项}.
$$

其中曲率项来自交换 $\nabla_s$ 和 $\nabla_t$：$\nabla_s \nabla_t \partial_s \gamma_s - \nabla_t \nabla_s \partial_s \gamma_s = R(\partial_s \gamma_s, \partial_t \gamma_s) \partial_s \gamma_s$。$\square$

**定理**（Jacobi 方程的解）：沿测地线 $\gamma$，Jacobi 方程 $\nabla_{\dot{\gamma}} \nabla_{\dot{\gamma}} J + R(J, \dot{\gamma}) \dot{\gamma} = 0$ 是二阶线性 ODE，其解空间维数为 $2n$，且由初始条件 $J(0)$ 和 $\nabla_{\dot{\gamma}} J(0)$ 唯一确定。

**证明**：沿 $\gamma$ 选取平行正标架 $\{e_i(t)\}$，令 $J(t) = \sum_i J^i(t) e_i(t)$。则 $\nabla_{\dot{\gamma}} J = \sum_i \dot{J}^i e_i$，$\nabla_{\dot{\gamma}} \nabla_{\dot{\gamma}} J = \sum_i \ddot{J}^i e_i$。Jacobi 方程化为

$$
\ddot{J}^i + \sum_j R^i_j(t) J^j = 0,
$$

其中 $R^i_j(t) = g(R(e_j, \dot{\gamma})\dot{\gamma}, e_i)$。这是二阶线性常微分方程组，由标准 ODE 理论，解空间维数为 $2n$。$\square$

**推论**（共轭点与指数映射）：设 $\gamma$ 是测地线，$\gamma(0) = p$，则 $\gamma(a)$ 是 $\gamma(0)$ 沿 $\gamma$ 的共轭点当且仅当 $d\exp_p|_{a\dot{\gamma}(0)}$ 退化，即指数映射 $\exp_p$ 在 $a\dot{\gamma}(0)$ 处不是局部微分同胚。