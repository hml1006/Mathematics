# Feynman路径积分

> **一句话大白话**：量子跃迁的振幅 = "所有可能路径的相位 $e^{iS/\hbar}$ 求和"——经典路径是相消中幸存的那条，其余互相抵消；$U(t)\propto\int\mathcal D[x]\,e^{iS[x]/\hbar}$ 把量子力学谱成"对轨迹的积分"。
>
> **小例子**：自由粒子的传播子 $\langle x_f|e^{-iHt}|x_i\rangle=\int_{x_i}^{x_f}\mathcal D[x]e^{iS[x]}$，高斯型积出 $\sqrt{\frac{m}{2\pi i\hbar t}}\,e^{im(x_f-x_i)^2/2\hbar t}$，与经典结果一致。

## 介绍

Feynman路径积分（Feynman Path Integral）是 Richard Feynman 在1948年提出的量子力学表述，它通过所有可能路径的振幅叠加来刻画量子系统的演化。路径积分的基本思想是：粒子从点 $x_a$ 到点 $x_b$ 的传播子（transition amplitude）等于所有可能路径的贡献之和，每条路径的贡献由作用量的指数 $e^{iS/\hbar}$ 给出。数学上，路径积分是定义在无限维函数空间上的积分，其严格化是泛函分析和概率论中的重要课题。路径积分在量子场论、统计力学和凝聚态物理中有着广泛的应用。

## 分析

**定理的精确表述**（Feynman路径积分公式）：在量子力学中，从 $(x_a, t_a)$ 到 $(x_b, t_b)$ 的传播子为

$$
K(x_b, t_b; x_a, t_a) = \int_{x(t_a)=x_a}^{x(t_b)=x_b} \mathcal{D}[x(t)] \, e^{iS[x(t)]/\hbar},
$$

其中 $S[x(t)] = \int_{t_a}^{t_b} L(x, \dot{x}, t) \, dt$ 是经典作用量，$\mathcal{D}[x(t)]$ 是路径空间的"测度"。

**等价形式**（时间分割）：将时间区间 $[t_a, t_b]$ 分割为 $N$ 等份，$\Delta t = (t_b - t_a)/N$，则

$$
K(x_b, t_b; x_a, t_a) = \lim_{N \to \infty} \left( \frac{m}{2\pi i \hbar \Delta t} \right)^{N/2} \int \cdots \int \exp\left( \frac{i}{\hbar} \sum_{j=0}^{N-1} \frac{m}{2} \frac{(x_{j+1} - x_j)^2}{\Delta t} \right) dx_1 \cdots dx_{N-1}.
$$

**依赖的概念**：作用量原理、Lagrangian、传播子、Schrödinger方程、高斯积分。

**核心关系**：路径积分满足 Schrödinger 方程，且与算符形式等价。

## 思考过程

Feynman路径积分的核心思想是量子力学的"求和over histories"诠释。在经典力学中，粒子遵循最小作用量原理，只走一条路径。在量子力学中，所有路径都有贡献，但相位 $e^{iS/\hbar}$ 使得相邻路径的贡献在偏离经典路径时因快速振荡而相消。

路径积分与 Schrödinger 方程的等价性可以通过时间分割法证明：在无穷小时间间隔内，传播子由自由粒子的传播子近似，代入 Schrödinger 方程验证即得。

路径积分的严格数学定义涉及 Wiener 测度（在虚时间 $t \to -i\tau$ 下，路径积分变为 Wiener 积分，即统计力学中的配分函数）。

## 证明过程

**定理**（路径积分与 Schrödinger 方程的等价性）：Feynman 路径积分定义的传播子 $K(x_b, t_b; x_a, t_a)$ 满足 Schrödinger 方程

$$
i\hbar \frac{\partial}{\partial t_b} K(x_b, t_b; x_a, t_a) = \hat{H} K(x_b, t_b; x_a, t_a),
$$

且初始条件 $K(x_b, t_a; x_a, t_a) = \delta(x_b - x_a)$。

**证明**：

**步骤 1：时间分割。** 

将时间区间 $[t_a, t_b]$ 分割为 $N$ 等份，每段 $\varepsilon = \Delta t / N$。传播子可写为

$$
K(x_b, t_b; x_a, t_a) = \int K(x_b, t_b; x_{N-1}, t_{N-1}) \cdots K(x_1, t_1; x_a, t_a) \, dx_1 \cdots dx_{N-1}.
$$

**步骤 2：无穷小传播子。**

对无穷小时间间隔 $\varepsilon$，传播子近似为

$$
K(x_{j+1}, t_j + \varepsilon; x_j, t_j) = \sqrt{\frac{m}{2\pi i\hbar \varepsilon}} \exp\left( \frac{i}{\hbar} \left[ \frac{m}{2} \frac{(x_{j+1} - x_j)^2}{\varepsilon} - V(x_j)\varepsilon \right] \right).
$$

**步骤 3：验证 Schrödinger 方程。**

考虑从 $t$ 到 $t + \varepsilon$ 的传播子：

$$
\psi(x, t+\varepsilon) = \int K(x, t+\varepsilon; y, t) \psi(y, t) \, dy.
$$

代入近似表达式，令 $y = x + \eta$：

$$
\psi(x, t+\varepsilon) = \sqrt{\frac{m}{2\pi i\hbar \varepsilon}} \int \exp\left( \frac{i m \eta^2}{2\hbar \varepsilon} \right) \exp\left( -\frac{i}{\hbar} V(x)\varepsilon \right) \psi(x+\eta, t) \, d\eta.
$$

**步骤 4：展开积分。**

对 $\psi(x+\eta, t)$ 做 Taylor 展开到 $\eta^2$ 阶，计算高斯积分

$$
\int_{-\infty}^\infty e^{i a \eta^2} \, d\eta = \sqrt{\frac{i\pi}{a}}, \quad \int_{-\infty}^\infty \eta e^{i a \eta^2} \, d\eta = 0, \quad \int_{-\infty}^\infty \eta^2 e^{i a \eta^2} \, d\eta = \frac{1}{2ia} \sqrt{\frac{i\pi}{a}}.
$$

代入得

$$
\psi(x, t+\varepsilon) = \psi(x, t) - \frac{i\varepsilon}{\hbar} \left[ -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} + V(x) \right] \psi(x, t) + O(\varepsilon^2).
$$

**步骤 5：取极限。**

整理得

$$
i\hbar \frac{\psi(x, t+\varepsilon) - \psi(x, t)}{\varepsilon} = \hat{H} \psi(x, t) + O(\varepsilon).
$$

令 $\varepsilon \to 0$ 即得 Schrödinger 方程 $i\hbar \partial_t \psi = \hat{H} \psi$。$\square$

**推论**：路径积分表述与算符表述等价。传播子满足 $K(x_b, t_b; x_a, t_a) = \langle x_b | e^{-i\hat{H}(t_b - t_a)/\hbar} | x_a \rangle$。