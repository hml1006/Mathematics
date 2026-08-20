# Hamiltonian力学与辛几何

> **一句话大白话**：把经典力学的相空间看成"别商空间"（辛流形），哈密顿量 $H$ 给出速度场 $X_H$，而这里的几何不变量就是辛形式 $\omega$——它保证了体积不变、泊松括号是李括号等机械理论的核心事实。
>
> **小例子**：$\mathbb{R}^{2n}$ 上的标准辛形式 $\omega=\sum dp_i\wedge dq_i$ 给出哈密顿方程 $\dot q=\partial H/\partial p,\ \dot p=-\partial H/\partial q$；Liouville 定理（相体积不变）本质是 $\mathcal L_{X_H}\omega=0$。

## 介绍

Hamiltonian力学与辛几何（Hamiltonian Mechanics and Symplectic Geometry）是经典力学在辛流形上的几何化表述。Hamiltonian力学由 William Rowan Hamilton 在1833年提出，将 Lagrange 力学中的二阶方程转化为相空间上的一阶方程。辛几何则是这种表述的自然几何框架——相空间是一个辛流形，Hamiltonian 向量场给出了动力学方程，Poisson 括号给出了可观测量的代数结构。这一理论架起了经典力学与几何之间的桥梁，是理解 Noether 定理、可积系统以及几何量子化的基础。

## 分析

**定理的精确表述**（Hamiltonian 方程）：设 $(M, \omega)$ 是辛流形，$H: M \to \mathbb{R}$ 是光滑函数（Hamiltonian）。则存在唯一的向量场 $X_H \in \mathfrak{X}(M)$ 满足

$$
\iota_{X_H} \omega = dH.
$$

在局部 Darboux 坐标 $(q^1, \ldots, q^n, p_1, \ldots, p_n)$ 下，$\omega = \sum_i dq^i \wedge dp_i$，Hamiltonian 方程为

$$
\dot{q}^i = \frac{\partial H}{\partial p_i}, \quad \dot{p}_i = -\frac{\partial H}{\partial q^i}.
$$

**依赖的概念**：辛流形、辛形式、Hamiltonian 向量场、Poisson 括号、Liouville 形式。

**核心性质**：
- **Liouville 定理**：Hamiltonian 流保持相空间体积（$\mathcal{L}_{X_H} \omega^n = 0$）。
- **Poisson 括号**：$\{F, G\} = \omega(X_F, X_G) = \sum_i \left(\frac{\partial F}{\partial q^i}\frac{\partial G}{\partial p_i} - \frac{\partial F}{\partial p_i}\frac{\partial G}{\partial q^i}\right)$。
- **能量守恒**：$\{H, H\} = 0$，即 $H$ 沿流守恒。
- **Poisson 定理**：若 $F, G$ 是首次积分，则 $\{F, G\}$ 也是首次积分。

## 思考过程

Hamiltonian 力学的核心思想是用几何语言描述动力学。辛形式 $\omega$ 提供了一个非退化闭的2-形式，它建立了切空间 $T_xM$ 与余切空间 $T_x^*M$ 之间的同构 $X \mapsto \iota_X\omega$。Hamiltonian 函数 $H$ 通过这个同构定义了速度场 $X_H$。

Darboux 定理说，局部上所有辛流形都是相同的——它们都可以表示为 $\mathbb{R}^{2n}$ 上的标准辛形式。这意味着辛几何的全局性质完全由拓扑决定，这与 Riemann 几何形成鲜明对比。

相空间 $(M, \omega)$ 上的 Poisson 括号 $\{\cdot, \cdot\}$ 给出了光滑函数环 $C^\infty(M)$ 上的 Lie 代数结构，而 Hamiltonian 流则给出了这个 Lie 代数的内蕴微分。

## 证明过程

**定理**（Darboux 定理）：设 $(M, \omega)$ 是 $2n$ 维辛流形。则对任意 $x \in M$，存在局部坐标 $(q^1, \ldots, q^n, p_1, \ldots, p_n)$ 使得

$$
\omega = \sum_{i=1}^n dq^i \wedge dp_i.
$$

**证明概要**（Moser 方法）：

**步骤 1：选择初始坐标。**
在 $x$ 附近取任意坐标 $(x^1, \ldots, x^{2n})$，使得 $\omega_x = \sum_i dx^i \wedge dx^{n+i}$。这总可以通过线性变换实现。

**步骤 2：构造插值。**
令 $\omega_0 = \omega_x$（常数形式），$\omega_1 = \omega$。定义 $\omega_t = (1-t)\omega_0 + t\omega_1$。对足够小的 $t$，$\omega_t$ 非退化。

**步骤 3：求解向量场。**
由 $\omega_t$ 闭，存在1-形式 $\alpha$ 使得 $\omega_1 - \omega_0 = d\alpha$。定义 $X_t$ 满足 $\iota_{X_t}\omega_t = -\alpha$。令 $\varphi_t$ 是 $X_t$ 的流，则 $\varphi_t^*\omega_t = \omega_0$。取 $\varphi_1$ 作为坐标变换即得 Darboux 坐标。$\square$

**定理**（Liouville 定理）：Hamiltonian 流 $\varphi_t$ 保持辛体积形式 $\omega^n = \omega \wedge \cdots \wedge \omega$。

**证明**：Lie 导数为

$$
\mathcal{L}_{X_H} \omega^n = n \omega^{n-1} \wedge \mathcal{L}_{X_H} \omega = n \omega^{n-1} \wedge d(\iota_{X_H} \omega) = n \omega^{n-1} \wedge d(dH) = 0.
$$

故 $\omega^n$ 沿流不变。$\square$

**推论**（Poisson 括号与 Jacobi 恒等式）：$\{F, \{G, H\}\} + \{G, \{H, F\}\} + \{H, \{F, G\}\} = 0$。

**证明**：由 $d\omega = 0$ 可推出 Jacobi 恒等式，或者直接计算：

$$
\{\{F, G\}, H\} = X_H(X_G(F) - X_F(G)) = X_H X_G(F) - X_H X_F(G),
$$

利用 $[X_F, X_G] = -X_{\{F, G\}}$（由 $\omega$ 闭可证），结合 $[X_H, X_G](F) = X_H X_G(F) - X_G X_H(F)$ 即可得证。$\square$