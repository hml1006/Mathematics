# Bonnet-Myers定理

> **一句话大白话**：如果曲面的弯曲程度恒有正的下限（Ricci曲率 ≥ 正数），那么这个空间就"抱得紧"，直径和体积都被卡住，最多走到某个有限距离就走不动了——正曲率像"向内吸"把世界锁在有限大小里。
>
> **小例子**：二维球面曲率很正且有限，直径也不大；若 Ricci 曲率 $\ge (n-1)/r^2>0$，则流形直径 $\le \pi r$，推而广之像球一样"绷不住"地紧凑。

## 介绍

Bonnet-Myers定理（Bonnet–Myers Theorem）是黎曼几何中最经典的全局定理之一，它给出了 Ricci 曲率正的下界对流形直径和基本群的限制。该定理断言：如果完备 Riemann 流形 $M$ 的 Ricci 曲率满足 $\mathrm{Ric} \ge (n-1)\kappa > 0$（其中 $n = \dim M$），则 $M$ 是紧致的，其直径 $d(M) \le \pi/\sqrt{\kappa}$，且基本群 $\pi_1(M)$ 是有限的。Bonnet-Myers定理是曲率与拓扑之间深刻联系的典范，在几何分析中有着广泛的应用。

## 分析

**前置依赖**：Ricci 曲率、测地线与完备性、能量泛函的第二变分公式、Jacobi 场与平行向量场、Hopf-Rinow 定理与覆盖空间理论。

**定理的精确表述**：设 $(M^n, g)$ 是完备 Riemann 流形，$\mathrm{Ric} \ge (n-1)\kappa$ 对某个常数 $\kappa > 0$。则：
1. $M$ 是紧致流形。
2. $\mathrm{diam}(M) \le \pi/\sqrt{\kappa}$。
3. $\pi_1(M)$ 是有限的。

**依赖的概念**：Ricci曲率、完备性、直径、基本群、测地线、Jacobi场。

**证明策略**：利用 Ricci 曲率正的下界，通过 Jacobi 场的弧长比较，证明长度超过 $\pi/\sqrt{\kappa}$ 的测地线必然存在共轭点，从而不能是距离实现测地线。

## 思考过程

Bonnet-Myers 定理的证明核心是"弧长第二变分公式"。考虑长度 $L$ 的测地线 $\gamma$，沿 $\gamma$ 构造一个适当的变分向量场 $J(t)$，使得能量二阶变分为负——这意味着 $\gamma$ 不是最短的，因此长度不能超过 $\pi/\sqrt{\kappa}$。

具体地，对沿 $\gamma$ 的平行单位向量场 $E(t)$，取 $J(t) = \sin(\pi t/L) E(t)$。代入第二变分公式，利用 $\mathrm{Ric} \ge (n-1)\kappa$ 可得

$$
E''(0) \le \int_0^L \left( \frac{\pi^2}{L^2} \cos^2\frac{\pi t}{L} - (n-1)\kappa \sin^2\frac{\pi t}{L} \right) dt.
$$

当 $L > \pi/\sqrt{\kappa}$ 时，这个积分为负，从而存在更短的曲线。

## 证明过程

**定理**（Bonnet-Myers）：设 $(M^n, g)$ 是完备 Riemann 流形，$\mathrm{Ric} \ge (n-1)\kappa$，$\kappa > 0$。则 $\mathrm{diam}(M) \le \pi/\sqrt{\kappa}$。

**证明**：

**步骤 1：反证法假设。**

假设存在 $p, q \in M$ 使得 $d(p, q) = L > \pi/\sqrt{\kappa}$。由完备性，存在极小测地线 $\gamma: [0, L] \to M$ 连接 $p$ 和 $q$，弧长参数化，$|\dot{\gamma}(t)| \equiv 1$。

**步骤 2：构造变分向量场。**

沿 $\gamma$ 选取 $n-1$ 个平行的单位正交向量场 $E_1(t), \ldots, E_{n-1}(t)$，满足 $g(E_i(t), \dot{\gamma}(t)) = 0$。定义

$$
J_i(t) = \sin\left(\frac{\pi t}{L}\right) E_i(t).
$$

则 $J_i(0) = J_i(L) = 0$。

**步骤 3：计算第二变分。**

由第二变分公式，每个 $J_i$ 贡献

$$
I(J_i, J_i) = \int_0^L \left( |\nabla_{\dot{\gamma}} J_i|^2 - R(J_i, \dot{\gamma}, \dot{\gamma}, J_i) \right) dt.
$$

计算 $|\nabla_{\dot{\gamma}} J_i|^2 = \frac{\pi^2}{L^2} \cos^2\left(\frac{\pi t}{L}\right)$，$R(J_i, \dot{\gamma}, \dot{\gamma}, J_i) = \sin^2\left(\frac{\pi t}{L}\right) R(E_i, \dot{\gamma}, \dot{\gamma}, E_i)$。

**步骤 4：求和利用 Ricci 曲率下界。**

对所有 $i = 1, \ldots, n-1$ 求和，

$$
\sum_{i=1}^{n-1} I(J_i, J_i) = \int_0^L \left( (n-1)\frac{\pi^2}{L^2} \cos^2\frac{\pi t}{L} - \sin^2\frac{\pi t}{L} \sum_{i=1}^{n-1} R(E_i, \dot{\gamma}, \dot{\gamma}, E_i) \right) dt.
$$

由定义，$\sum_{i=1}^{n-1} R(E_i, \dot{\gamma}, \dot{\gamma}, E_i) = \mathrm{Ric}(\dot{\gamma}, \dot{\gamma})$。由条件 $\mathrm{Ric}(\dot{\gamma}, \dot{\gamma}) \ge (n-1)\kappa$，得

$$
\sum_{i=1}^{n-1} I(J_i, J_i) \le \int_0^L \left( (n-1)\frac{\pi^2}{L^2} \cos^2\frac{\pi t}{L} - (n-1)\kappa \sin^2\frac{\pi t}{L} \right) dt.
$$

**步骤 5：积分计算。**

$$
\int_0^L \cos^2\frac{\pi t}{L} dt = \frac{L}{2}, \quad \int_0^L \sin^2\frac{\pi t}{L} dt = \frac{L}{2}.
$$

代入得

$$
\sum_{i=1}^{n-1} I(J_i, J_i) \le (n-1) \left( \frac{\pi^2}{L^2} \cdot \frac{L}{2} - \kappa \cdot \frac{L}{2} \right) = \frac{(n-1)L}{2} \left( \frac{\pi^2}{L^2} - \kappa \right).
$$

当 $L > \pi/\sqrt{\kappa}$ 时，$\frac{\pi^2}{L^2} - \kappa < 0$，故 $\sum I(J_i, J_i) < 0$。因此存在某个 $i$ 使得 $I(J_i, J_i) < 0$，这意味着 $\gamma$ 不是极小测地线，矛盾。

**步骤 6：证明基本群有限。**

由直径有限，$M$ 紧致。考虑万有覆盖 $\tilde{M}$，诱导度量使 $\tilde{M}$ 完备且同样满足 $\mathrm{Ric} \ge (n-1)\kappa$。由 Bonnet-Myers 定理，$\tilde{M}$ 也紧致，故 $\pi_1(M)$ 作为覆盖变换群作用在紧致流形上，必为有限群。$\square$

**推论**：常曲率 $c > 0$ 的完备单连通 Riemann 流形必为球面 $S^n(c)$。特别地，$S^n$ 的直径不超过 $\pi/\sqrt{c}$。