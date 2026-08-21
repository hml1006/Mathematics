# Rauch比较定理

> **一句话大白话**：把"弯曲多少"比一比：若空间甲的曲率总是 ≥ 空间乙的曲率，那么甲里沿方向走散的"短路散步量"（Jacobi场长度）就 ≤ 乙的——曲率越大，几何越"聚拢"，散步越靠拢。用一个词的曲率上下界对照整支最短线族。
>
> **小例子**：在曲率 $\ge \kappa$ 的空间里，沿一条测地线的相邻路径比"曲率恰为 $\kappa$ 的标准空间（如球/双曲/欧氏）"走得更紧；比较定理给出 $|J|\le \sinh(\sqrt{-\kappa}\,s)$ 型的长度上界。

## 介绍

Rauch比较定理（Rauch Comparison Theorem）是黎曼几何中最重要的比较定理之一，由 H. E. Rauch 在1951年提出。该定理通过比较不同流形上的 Jacobi 场来建立截面曲率与测地线偏离速度之间的关系。具体地说，如果两个 Riemann 流形 $M$ 和 $\tilde{M}$ 沿测地线的截面曲率满足 $K_M \ge K_{\tilde{M}}$，则 $M$ 上的 Jacobi 场增长不超过 $\tilde{M}$ 上的 Jacobi 场。Rauch比较定理是后续许多比较定理（如 Toponogov 比较定理、Bishop–Gromov 体积比较定理）的基础，在几何分析中有着广泛的应用。

## 分析

**前置依赖**：Jacobi 场与 Jacobi 方程、截面曲率、测地线与弧长参数化、共轭点、Riccati 方程比较。

**定理的精确表述**（Rauch 比较定理）：设 $M$ 和 $\tilde{M}$ 是 Riemann 流形，$\gamma: [0, L] \to M$ 和 $\tilde{\gamma}: [0, L] \to \tilde{M}$ 是弧长参数化的测地线，$J$ 和 $\tilde{J}$ 是沿 $\gamma$ 和 $\tilde{\gamma}$ 的 Jacobi 场，满足：
1. $J(0) = \tilde{J}(0) = 0$，
2. $|\nabla_{\dot{\gamma}} J(0)| = |\nabla_{\dot{\tilde{\gamma}}} \tilde{J}(0)|$，
3. 对任意 $t \in [0, L]$，$K_M(\dot{\gamma}(t), J(t)) \le K_{\tilde{M}}(\dot{\tilde{\gamma}}(t), \tilde{J}(t))$。

则 $|J(t)| \ge |\tilde{J}(t)|$ 对所有 $t \in [0, L]$ 成立。

**依赖的概念**：Jacobi场、截面曲率、测地线、共轭点。

**证明策略**：考虑函数 $f(t) = |J(t)|^2 / |\tilde{J}(t)|^2$，通过 Jacobi 方程和曲率比较证明 $f(t)$ 的单调性。

## 思考过程

Rauch 比较定理的直观含义是：曲率越大，测地线越倾向于汇聚（Jacobi 场增长越慢）。这可以类比于球面上的测地线（正曲率）最终汇聚于对径点，而双曲平面上的测地线（负曲率）则快速发散。

证明的关键是构造比值函数 $f(t) = |J(t)|^2 / |\tilde{J}(t)|^2$，利用 Jacobi 方程和曲率条件证明 $f'(t) \ge 0$（或 $f'(t) \le 0$，取决于曲率比较方向）。这需要对 $f(t)$ 求导，并利用曲率比较条件。

## 证明过程

**定理**（Rauch 比较定理）：设 $M$ 和 $\tilde{M}$ 是 $n$ 维 Riemann 流形，$\gamma: [0, L] \to M$ 和 $\tilde{\gamma}: [0, L] \to \tilde{M}$ 是弧长参数化的测地线，$J$ 和 $\tilde{J}$ 是沿 $\gamma$ 和 $\tilde{\gamma}$ 的 Jacobi 场，满足 $J(0) = \tilde{J}(0) = 0$，$|\nabla_{\dot{\gamma}} J(0)| = |\nabla_{\dot{\tilde{\gamma}}} \tilde{J}(0)|$，且

$$
K_M(\dot{\gamma}(t), J(t)) \le K_{\tilde{M}}(\dot{\tilde{\gamma}}(t), \tilde{J}(t)).
$$

则 $|J(t)| \ge |\tilde{J}(t)|$ 对所有 $t \in [0, L]$ 成立。

**证明**：

**步骤 1：归一化。**

由于 $J(0) = 0$，我们有 $J(t) = t \nabla_{\dot{\gamma}} J(0) + o(t)$，故当 $t \to 0$ 时 $|J(t)| \sim t |\nabla_{\dot{\gamma}} J(0)|$。类似地 $|\tilde{J}(t)| \sim t |\nabla_{\dot{\tilde{\gamma}}} \tilde{J}(0)|$。由初始条件，$|J(t)|/|\tilde{J}(t)| \to 1$ 当 $t \to 0$。

**步骤 2：定义比较函数。**

令 $u(t) = |J(t)|^2$，$\tilde{u}(t) = |\tilde{J}(t)|^2$。由 Jacobi 方程和曲率条件，可得

$$
\frac{u''(t)}{u(t)} \ge \frac{\tilde{u}''(t)}{\tilde{u}(t)}.
$$

**步骤 3：利用 Riccati 方程。**

定义 $f(t) = \frac{u'(t)}{u(t)}$，则 $f'(t) = \frac{u''(t)}{u(t)} - \left(\frac{u'(t)}{u(t)}\right)^2$。由 Jacobi 方程和曲率条件，$f'(t) \ge \tilde{f}'(t)$，其中 $\tilde{f}(t) = \tilde{u}'(t)/\tilde{u}(t)$。

**步骤 4：积分比较。**

由 $f(0) = \tilde{f}(0)$（因为 $u(t) \sim t^2 |\nabla J(0)|^2$，$f(t) \sim 2/t$ 对两边相同），积分得 $f(t) \ge \tilde{f}(t)$。这等价于 $(\log u(t))' \ge (\log \tilde{u}(t))'$，再积分得 $\log u(t) \ge \log \tilde{u}(t)$，即 $u(t) \ge \tilde{u}(t)$。故 $|J(t)| \ge |\tilde{J}(t)|$。$\square$

**推论**（共轭点比较）：若 $K_M \ge \kappa$（即截面曲率有正下界），则 $M$ 中测地线的共轭距离不超过常曲率 $\kappa$ 空间中的共轭距离。特别地，若 $K_M \ge 1$，则共轭距离 $\le \pi$。

**推论**（体积比较）：Bishop–Gromov 体积比较定理：若 $\mathrm{Ric}_M \ge (n-1)\kappa$，则对任意 $p \in M$，体积比 $V(p, r)/V_\kappa(r)$ 是 $r$ 的非增函数，其中 $V_\kappa(r)$ 是常曲率 $\kappa$ 空间中半径为 $r$ 的球体积。