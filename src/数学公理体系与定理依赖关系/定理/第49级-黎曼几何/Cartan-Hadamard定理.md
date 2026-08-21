# Cartan-Hadamard定理

> **一句话大白话**：一个"处处都不往内弯"（截面曲率 ≤ 0）、又单连通的完整空间，长得就像给它铺伸展开——处处测地线（最短线）都能无限延伸，空间是某个欧氏空间的"拉平像"，拓扑上是"平摊开的一团"。
>
> **小例子**：马鞍状曲面（双曲结构）曲率非正，Cartan-Hadamard 说它整体等同于一个大平面在微分同胚意义下——从任意点都能沿所有方向无限走远，整个空间与 $\mathbb{R}^n$ 同胚。

## 介绍

Cartan-Hadamard定理（Cartan–Hadamard Theorem）是黎曼几何中关于非正曲率流形全局结构的基本定理。该定理断言：如果完备 Riemann 流形 $M$ 的截面曲率处处非正（$K \le 0$），则 $M$ 的万有覆盖 $\tilde{M}$ 微分同胚于 Euclidean 空间 $\mathbb{R}^n$。特别地，$M$ 的任意点处的指数映射是全局微分同胚，且 $M$ 是 $K(\pi_1(M), 1)$ 空间。Cartan-Hadamard定理是负曲率几何的基石，它刻画了非正曲率流形的基本拓扑性质。

## 分析

**前置依赖**：截面曲率、指数映射、Jacobi 方程与共轭点、完备性与 Hopf-Rinow 定理、覆盖空间理论。

**定理的精确表述**：设 $(M^n, g)$ 是完备 Riemann 流形，截面曲率 $K \le 0$ 处处成立。则对任意 $p \in M$，指数映射 $\exp_p: T_pM \to M$ 是覆盖映射。特别地，万有覆盖 $\tilde{M}$ 微分同胚于 $\mathbb{R}^n$。

**依赖的概念**：截面曲率、指数映射、共轭点、覆盖空间、完备性。

**证明策略**：证明在 $K \le 0$ 的条件下，$M$ 上没有共轭点（即指数映射的微分处处非退化），因此指数映射是局部微分同胚。再由完备性，它是覆盖映射。

## 思考过程

Cartan-Hadamard 定理的核心是曲率非正时 Jacobi 场的性质。回忆 Jacobi 方程

$$
\nabla_{\dot{\gamma}} \nabla_{\dot{\gamma}} J + R(J, \dot{\gamma}) \dot{\gamma} = 0.
$$

当 $K \le 0$ 时，$R(J, \dot{\gamma}, \dot{\gamma}, J) \le 0$，因此 Jacobi 方程类似"弹性力"方程 $\ddot{J} + \text{(非正项)} J = 0$，其解不会振荡，从而不会出现非平凡 Jacobi 场在两端点为零的情况——即没有共轭点。

这个定理揭示了负曲率与正曲率的根本区别：正曲率使测地线汇聚（产生共轭点），导致流形紧致（Bonnet-Myers）；负曲率使测地线发散，导致流形非紧且万有覆盖为 $\mathbb{R}^n$。

## 证明过程

**定理**（Cartan-Hadamard）：设 $(M^n, g)$ 是完备 Riemann 流形，$K \le 0$。则对任意 $p \in M$，$\exp_p: T_pM \to M$ 是覆盖映射。

**证明**：

**步骤 1：证明 $\exp_p$ 是局部微分同胚。**

只需证明沿任意从 $p$ 出发的测地线 $\gamma(t) = \exp_p(tv)$ 没有共轭点。设 $J(t)$ 是沿 $\gamma$ 的 Jacobi 场，$J(0) = 0$，$J \not\equiv 0$。考虑函数 $f(t) = |J(t)|^2$。计算

$$
f'(t) = 2g(\nabla_{\dot{\gamma}} J, J),
$$
$$
f''(t) = 2g(\nabla_{\dot{\gamma}} \nabla_{\dot{\gamma}} J, J) + 2|\nabla_{\dot{\gamma}} J|^2.
$$

由 Jacobi 方程 $\nabla_{\dot{\gamma}} \nabla_{\dot{\gamma}} J = -R(J, \dot{\gamma}) \dot{\gamma}$，代入得

$$
f''(t) = -2R(J, \dot{\gamma}, \dot{\gamma}, J) + 2|\nabla_{\dot{\gamma}} J|^2 \ge 2|\nabla_{\dot{\gamma}} J|^2 \ge 0,
$$

其中不等号使用了 $K \le 0$ 即 $R(J, \dot{\gamma}, \dot{\gamma}, J) \le 0$。

**步骤 2：分析 $f(t)$ 的凸性。**

由 $f''(t) \ge 0$，$f(t)$ 是凸函数。又 $f(0) = 0$，$f'(0) = 0$（因为 $J(0) = 0$，可证 $\nabla_{\dot{\gamma}} J(0)$ 与 $\dot{\gamma}$ 垂直，且 $J(t) = t \nabla_{\dot{\gamma}} J(0) + o(t)$，故 $f'(0) = 0$）。因此对 $t > 0$，$f(t) > 0$（除非 $J \equiv 0$）。故 $J(t) \neq 0$ 对所有 $t > 0$，即 $p$ 沿 $\gamma$ 没有共轭点。

因此 $\exp_p$ 在每点处的微分非退化，$\exp_p$ 是局部微分同胚。

**步骤 3：证明 $\exp_p$ 是覆盖映射。**

由于 $M$ 完备，$\exp_p$ 定义在整个 $T_pM$ 上。由覆盖空间理论，局部微分同胚的完备 Riemann 流形之间的指数映射是覆盖映射当且仅当它是满射且具有路径提升性质。由完备性，$\exp_p$ 是满射，且由于 $T_pM$ 是单连通的，$\exp_p$ 是覆盖映射。

**步骤 4：万有覆盖的结构。**

因此 $\tilde{M} = T_pM \cong \mathbb{R}^n$，且 $M = \tilde{M} / \Gamma$，其中 $\Gamma \cong \pi_1(M)$ 是离散子群，自由作用在 $\mathbb{R}^n$ 上。$\square$

**推论**：若 $M$ 是完备单连通 Riemann 流形，$K \le 0$，则 $M$ 微分同胚于 $\mathbb{R}^n$。此时 $M$ 称为 Hadamard 流形。

**推论**：在 Hadamard 流形中，任意两点有唯一测地线连接，且测地线三角形满足比较定理（CAT(0) 空间性质）。