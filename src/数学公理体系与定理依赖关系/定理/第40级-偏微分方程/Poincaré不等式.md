# Poincaré 不等式

> **一句话大白话**：把函数减去它的平均值之后，剩下的"起伏"完全被它的导数（梯度）控制。
>
> **小例子**：一维 $\Omega=(0,1)$ 上，$\int_0^1(u-\bar u)^2\,dx\le\frac1{\pi^2}\int_0^1|u'|^2\,dx$，常数 $1/\pi^2$ 是最佳的。

## 介绍

在偏微分方程理论中，我们经常需要"用导数控制函数本身"。对整体不为零的函数这不可能（常数函数的导数恒为零而函数不为零），最自然的修正就是先减去平均值 $\bar u=\frac1{|\Omega|}\int_\Omega u$。Poincaré 不等式正是这一控制的精确陈述：

$$\|u-\bar u\|_{L^p(\Omega)}\le C\|\nabla u\|_{L^p(\Omega)}.$$

它是椭圆方程先验估计、Sobolev 空间的范数等价性、Lax–Milgram 方法中强制性（coercivity）验证等大量结论的基础工具。另一常见变体是对满足 $u|_{\partial\Omega}=0$ 的函数直接成立 $\|u\|_{L^p}\le C\|\nabla u\|_{L^p}$，称为 Friedrichs 不等式。

## 分析

**前置依赖**：Sobolev 空间定义、Sobolev 嵌入定理、Rellich–Kondrachov 紧嵌入定理、Hölder 不等式、弱导数与弱收敛。

**定理内容**：设 $\Omega\subset\mathbb{R}^n$ 为有界开集，边界充分光滑（例如 Lipschitz 边界），$1\le p<\infty$。则存在常数 $C=C(\Omega,n,p)>0$，使得对一切 $u\in W^{1,p}(\Omega)$ 有
$$\Big\|u-\frac1{|\Omega|}\int_\Omega u\Big\|_{L^p(\Omega)}\le C\|\nabla u\|_{L^p(\Omega)}.$$

**证明策略**：直接构造常数很难，但反证法极快：若不存在这样的 $C$，就能造出一列"平均值为零、$L^p$ 范数为 $1$、而梯度范数趋于 $0$"的函数；由紧嵌入取 $L^p$ 收敛子列，极限的弱梯度为零（故为常数），平均值为零（故为零），与范数为 $1$ 矛盾。

## 思考过程

反证法的逻辑链条是：

1. 设不等式不成立，则存在 $u_k\in W^{1,p}(\Omega)$ 使 $\|u_k-\bar u_k\|_{L^p}>k\|\nabla u_k\|_{L^p}$。
2. 归一化 $v_k=\dfrac{u_k-\bar u_k}{\|u_k-\bar u_k\|_{L^p}}$，则 $\|v_k\|_{L^p}=1$、$\bar v_k=0$，且 $\|\nabla v_k\|_{L^p}<1/k\to0$。
3. 由 $\|v_k\|_{W^{1,p}}$ 有界与紧嵌入 $W^{1,p}\hookrightarrow\hookrightarrow L^p$，取子列 $v_{k_j}\to v$ 于 $L^p$。
4. 对任意试探函数 $\varphi\in C_c^\infty(\Omega)$，$\int\nabla v\cdot\varphi=\lim_j\int\nabla v_{k_j}\cdot\varphi\le\|\nabla v_{k_j}\|_{L^p}\|\varphi\|_{L^{p'}}\to0$，故弱梯度 $\nabla v=0$，$v$ 是常数。
5. $\bar v=0$ 且 $v$ 常数 $\Rightarrow v=0$，但 $\|v\|_{L^p}=1$，矛盾。

每一步都真实可用，唯一"借用"的是紧嵌入定理（Rellich–Kondrachov）与弱梯度与 $L^p$ 收敛的相容性。

## 证明过程

**步骤 1：反设与归一化。**

设结论不成立，即对每个 $k\in\mathbb{N}$ 都存在 $u_k\in W^{1,p}(\Omega)$ 使
$$\|u_k-\bar u_k\|_{L^p(\Omega)}>k\|\nabla u_k\|_{L^p(\Omega)}.$$
因 $u_k-\bar u_k\ne 0$（否则左边为 $0$ 不可能严格大于右边非负数），可令
$$v_k=\frac{u_k-\bar u_k}{\|u_k-\bar u_k\|_{L^p(\Omega)}}.$$
则 $\|v_k\|_{L^p}=1$，且平均值
$$\bar v_k=\frac{\overline{u_k-\bar u_k}}{\|u_k-\bar u_k\|_{L^p}}=\frac{\bar u_k-\bar u_k}{\|u_k-\bar u_k\|_{L^p}}=0,$$
而 $\nabla v_k=\dfrac{\nabla u_k}{\|u_k-\bar u_k\|_{L^p}}$ 满足
$$\|\nabla v_k\|_{L^p}=\frac{\|\nabla u_k\|_{L^p}}{\|u_k-\bar u_k\|_{L^p}}<\frac1k. \tag{1}$$

**步骤 2：$W^{1,p}$ 范数有界与紧嵌入。**

由 $\|v_k\|_{L^p}=1$ 与 (1)，
$$\|v_k\|_{W^{1,p}}=\Big(\|v_k\|_{L^p}^p+\|\nabla v_k\|_{L^p}^p\Big)^{1/p}\le (1+k^{-p})^{1/p}\le 2^{1/p}.$$
故 $\{v_k\}$ 在 $W^{1,p}(\Omega)$ 中有界。由 Rellich–Kondrachov 紧嵌入定理（$\Omega$ 有界、边界 Lipschitz，$1\le p<\infty$ 时 $W^{1,p}(\Omega)\hookrightarrow\hookrightarrow L^p(\Omega)$），存在子列（仍记 $v_k$）与 $v\in L^p(\Omega)$ 使
$$v_k\to v\quad\text{于 }L^p(\Omega). \tag{2}$$

**步骤 3：极限的弱梯度为零。**

由 (2) 知 $\|v\|_{L^p}=1$。又由 (2) 对平均值 $\bar v_k\to\bar v$ 成立，结合 $\bar v_k=0$ 得
$$\bar v=0. \tag{3}$$
现证 $v\in W^{1,p}(\Omega)$ 且 $\nabla v=0$。由 (1) 知 $\{\nabla v_k\}$ 在 $L^p(\Omega;\mathbb{R}^n)$ 中有界，故可取子列弱收敛（$1<p<\infty$，空间自反；$p=1$ 时用 $L^1$ 的有界性与极限论证）到某 $w\in L^p(\Omega;\mathbb{R}^n)$。对任意 $\varphi\in C_c^\infty(\Omega;\mathbb{R}^n)$，
$$\int_\Omega w\cdot\varphi=\lim_k\int_\Omega \nabla v_k\cdot\varphi=-\lim_k\int_\Omega v_k\,\mathrm{div}\,\varphi=-\int_\Omega v\,\mathrm{div}\,\varphi,$$
其中第一步用弱收敛、第二步用弱导数的定义（分部积分）、第三步用 (2)。这说明 $w$ 就是 $v$ 的弱梯度，即 $\nabla v=w$ 且
$$\|\nabla v\|_{L^p}\le\liminf_k\|\nabla v_k\|_{L^p}=0$$
（范数的弱下半连续性）。故 $\nabla v=0$。

**步骤 4：导出矛盾。**

$\nabla v=0$ 于 $\Omega$（连通；若不连通可对每个连通分支重复论证，平均值仍按分支取）意味着 $v$ 在 $\Omega$ 上几乎处处为常数。结合 (3) 的 $\bar v=0$，得 $v=0$ 几乎处处，于是 $\|v\|_{L^p}=0$，与步骤 3 的 $\|v\|_{L^p}=1$ 矛盾。

因此反设不成立，存在 $C>0$ 使不等式对一切 $u\in W^{1,p}(\Omega)$ 成立。

**步骤 5：补充与变体。**

（i）**连通性**：若 $\Omega$ 不连通，则"常值"结论在每一连通分支上分别成立，而在每个分支上平均值均为零，故仍得 $v=0$，结论不变。

（ii）**Friedrichs 不等式**：若 $u\in W_0^{1,p}(\Omega)$（即 $u$ 是 $C_c^\infty(\Omega)$ 在 $W^{1,p}$ 范数下的闭包），则无需减平均值，直接有 $\|u\|_{L^p}\le C\|\nabla u\|_{L^p}$。证明同理：若不然取 $\|u_k\|_{L^p}=1$、$\|\nabla u_k\|_{L^p}\to0$，紧嵌入与弱收敛给出极限 $v$ 为常数，而 $W_0^{1,p}$ 中弱极限仍属 $W_0^{1,p}$，常数且具零边界迹只能为零，矛盾。

（iii）**最佳常数**：一维区间上可用 Fourier 级数算得最佳常数为 $1/\pi^2$（$p=2$），说明上面的 $C$ 一般不是最优的。

## 相关条目

- [Sobolev空间定义](./Sobolev空间定义.md)：不等式两边正是 $W^{1,p}$ 范数的两个组成部分。
- [Sobolev嵌入定理](./Sobolev嵌入定理.md)：紧嵌入 $W^{1,p}\hookrightarrow\hookrightarrow L^p$ 是证明的核心输入。
- [Lax-Milgram定理PDE应用](./Lax-Milgram定理PDE应用.md)：椭圆算子的强制性估计依赖 Poincaré 不等式。
