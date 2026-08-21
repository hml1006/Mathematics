# Noether定理

> **一句话大白话**：每一个连续的"对称性"（让拉格朗日量不变）都对应一个守恒量——平移对称 → 动量守恒，时间对称 → 能量守恒，转动对称 → 角动量守恒；"对称性与守恒律"由此打通。
>
> **小例子**：对作用量 $S=\int L\,dt$ 的连续对称群，存在守恒电流 $J$；例如 $L=\frac12 m\dot x^2$ 对平移不变给出 $\partial_t(m\dot x)=0$，动量守恒。

## 介绍

Noether定理（Noether's Theorem）是理论物理学中最重要的定理之一，由 Emmy Noether 在1918年证明。该定理揭示了物理系统中的连续对称性与守恒量之间的一一对应关系：每个连续对称性对应一个守恒量。具体地，如果一个物理系统的作用量在某个连续变换群下不变，则存在一个相应的守恒量。Noether定理架起了对称性与守恒律之间的桥梁，在经典力学、场论、量子力学和广义相对论中都有深远影响。例如，时间平移对称性导致能量守恒，空间平移对称性导致动量守恒，空间旋转对称性导致角动量守恒。

## 分析

**前置依赖**：Lagrangian 力学与作用量原理、Euler-Lagrange 方程、连续对称性、变分法与分部积分（Stokes 定理）。

**定理的精确表述**（经典场论版本）：设 $L(\phi, \partial_\mu \phi)$ 是 Lagrangian 密度，作用量 $S = \int L \, d^4x$ 在单参数连续变换群 $\phi(x) \to \phi(x) + \varepsilon \delta\phi(x)$（其中 $\varepsilon$ 无穷小）下不变。则存在守恒流 $j^\mu$ 满足

$$
\partial_\mu j^\mu = 0,
$$

其中

$$
j^\mu = \frac{\partial L}{\partial(\partial_\mu \phi)} \delta\phi - K^\mu,
$$

而 $K^\mu$ 是 Lagrangian 密度的变化项（当 Lagrangian 变化一个全散度时）。

**依赖的概念**：Lagrangian 力学、作用量原理、对称性、守恒律、变分法。

**证明策略**：利用作用量在变换下的不变性，结合 Euler-Lagrange 方程，通过变分计算导出守恒流。

## 思考过程

Noether定理的证明基于一个简单的观察：如果作用量在连续变换下不变，那么将变换参数视为变量，作用量的一阶变分为零。通过分部积分，这个变分可以写成边界项与体项之和。体项由 Euler-Lagrange 方程给出（在运动方程上为零），因此边界项必须为零，这恰好给出了守恒流的散度为零。

关键等式是：

$$
\delta S = \int \left[ \frac{\partial L}{\partial \phi} \delta\phi + \frac{\partial L}{\partial(\partial_\mu \phi)} \partial_\mu(\delta\phi) \right] d^4x = 0.
$$

在运动方程上，第一项可以改写，最终得到 $\partial_\mu j^\mu = 0$。

## 证明过程

**定理**（Noether定理）：设 Lagrangian 密度 $L(\phi, \partial_\mu \phi)$ 在无穷小变换 $\phi \to \phi + \varepsilon \delta\phi$ 下作用量不变，即 $\delta S = 0$。则存在守恒流 $j^\mu$ 满足 $\partial_\mu j^\mu = 0$。

**证明**：

**步骤 1：变分计算。**

作用量的变分为

$$
\delta S = \int \left[ \frac{\partial L}{\partial \phi} \delta\phi + \frac{\partial L}{\partial(\partial_\mu \phi)} \partial_\mu(\delta\phi) \right] d^4x.
$$

**步骤 2：利用 Euler-Lagrange 方程。**

在运动方程上，$\frac{\partial L}{\partial \phi} = \partial_\mu \frac{\partial L}{\partial(\partial_\mu \phi)}$，代入得

$$
\delta S = \int \left[ \partial_\mu \frac{\partial L}{\partial(\partial_\mu \phi)} \delta\phi + \frac{\partial L}{\partial(\partial_\mu \phi)} \partial_\mu(\delta\phi) \right] d^4x = \int \partial_\mu \left( \frac{\partial L}{\partial(\partial_\mu \phi)} \delta\phi \right) d^4x.
$$

**步骤 3：定义守恒流。**

若 $\delta S = 0$（变换是对称性），则

$$
\int \partial_\mu \left( \frac{\partial L}{\partial(\partial_\mu \phi)} \delta\phi \right) d^4x = 0.
$$

由于这对任意积分区域成立，被积函数必为零：

$$
\partial_\mu \left( \frac{\partial L}{\partial(\partial_\mu \phi)} \delta\phi \right) = 0.
$$

定义 $j^\mu = \frac{\partial L}{\partial(\partial_\mu \phi)} \delta\phi$，则 $\partial_\mu j^\mu = 0$。

**步骤 4：更一般的情况。**

如果 Lagrangian 变化一个全散度，即 $\delta L = \varepsilon \partial_\mu K^\mu$，则守恒流修正为

$$
j^\mu = \frac{\partial L}{\partial(\partial_\mu \phi)} \delta\phi - K^\mu.
$$

仍然满足 $\partial_\mu j^\mu = 0$。$\square$

**推论**（经典力学中的守恒律）：
- 时间平移不变性 $\Rightarrow$ 能量守恒：$H = \sum_i p_i \dot{q}^i - L$。
- 空间平移不变性 $\Rightarrow$ 动量守恒：$P = \sum_i p_i$。
- 空间旋转不变性 $\Rightarrow$ 角动量守恒：$L = \sum_i r_i \times p_i$。

**例**（Klein-Gordon 场）：对 $L = \frac{1}{2}(\partial_\mu \phi \partial^\mu \phi - m^2 \phi^2)$，平移对称性 $\phi(x) \to \phi(x + a)$ 给出能量-动量张量 $T_{\mu\nu} = \partial_\mu \phi \partial_\nu \phi - \eta_{\mu\nu} L$，满足 $\partial^\mu T_{\mu\nu} = 0$。
## 相关条目

- [Noether 定理（第150级-数学物理）](../第150级-数学物理/Noether定理.md)：与本条目为同一定理，另收录于第150级-数学物理，可交叉参考。
