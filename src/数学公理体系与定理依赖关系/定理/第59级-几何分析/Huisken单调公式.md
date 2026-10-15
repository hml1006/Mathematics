# Huisken 单调公式

> **一句话大白话**：给平均曲率流配一个倒着跑的高斯热核当作"权重"，随着曲面收缩，这个加权面积（高斯密度积分）只会越来越小；而且它不变（取等）当且仅当曲面是不断缩小的完美球面。

> **小例子**：令 $\Phi_{x_0,t_0}(x,t)=(4\pi(t_0-t))^{-n/2}\exp\!\big(-\frac{|x-x_0|^2}{4(t_0-t)}\big)$，则沿平均曲率流

$$\frac{d}{dt}\int_{M_t}\Phi\,d\mu=-\int_{M_t}\Phi\Big|H\nu-\nabla^{\perp}\log\Phi\Big|^2d\mu\le0 .$$

## 一、定理介绍

> **前置依赖**：平均曲率流的第一变分公式与 $\partial_t\,d\mu=-H^2d\mu$、Laplace–Beltrami 算子与分部积分、热核与反向热方程、第二基本形式、coarea公式。

Huisken（1990）为平均曲率流引入了"反向热核加权"的单调量，这是平均曲率流理论中最重要的工具之一，被称为 Huisken 单调公式。它的意义在于：平均曲率流是一个退化的抛物方程，曲面会收缩、可能产生奇点，而单调量给了我们一个在奇点处仍有意义的"能量"，使得对奇点做爆破（blow-up）分析成为可能。

公式的简洁形式 $\dfrac{d}{dt}\int\Phi\,d\mu=-\int\Phi|H\nu-\nabla^\perp\log\Phi|^2d\mu$ 有鲜明的几何含义：右边度量的是"曲面的平均曲率向量 $H\nu$ 与加权函数梯度方向 $\nabla^\perp\log\Phi$ 的偏离"。取等意味着曲面恰好沿着反热核的梯度方向以平均曲率速度运动，而这只有收缩球面（或自相似收缩解）满足。

## 二、原理思路

1. **面积元的第一变分**：平均曲率流沿法向以速度 $-H\nu$ 运动，面积元满足 $\partial_t\,d\mu=-H^2d\mu$。
2. **权重满足反向热方程**：$\Phi$ 由倒向时间的热核构成，直接计算得 $\partial_t\Phi=-\Delta\Phi$（在 $\mathbb R^{n+1}$ 中取固定中心的反向热核，关于空间变量是调和共轭的热方程）。
3. **把两项合起来并配完全平方**：$\dfrac{d}{dt}\int\Phi\,d\mu=\int(\partial_t\Phi)\,\mathord{+}\,\Phi\,\partial_t d\mu$ 的贡献经分部积分后化为 $-\int\Phi|H\nu-\nabla^\perp\log\Phi|^2d\mu$。
4. **取等分析**：非负被积函数为零推出自相似方程 $H\nu=\nabla^\perp\log\Phi$，在紧致情形只有球面。

## 三、定理的严格表述

设 $M^n\subset\mathbb R^{n+1}$ 是紧致无边的 $n$ 维子流形，$F:M\times[0,T)\to\mathbb R^{n+1}$ 是平均曲率流

$$
\partial_tF=-H\nu,\qquad F(\cdot,0)=F_0,
$$

其中 $H$ 是平均曲率、$\nu$ 是单位法向量（约定使 $H\nu=\Delta F$）。对固定 $(x_0,t_0)\in\mathbb R^{n+1}\times(0,T)$ 定义**反向热核**

$$
\Phi_{x_0,t_0}(x,t)=\big(4\pi(t_0-t)\big)^{-n/2}\exp\Big(-\frac{|x-x_0|^2}{4(t_0-t)}\Big),\qquad t<t_0,
$$

记 $d\mu_t$ 为 $M_t$ 的面积元。**Huisken 单调公式**：

$$
\frac{d}{dt}\int_{M_t}\Phi\,d\mu_t=-\int_{M_t}\Phi\Big|H\nu-\nabla^{\perp}\log\Phi\Big|^2d\mu_t\ \le\ 0 ,
$$

其中 $\nabla^{\perp}\log\Phi$ 表示 $\nabla\log\Phi$ 在切空间上的正交投影。于是 $t\mapsto\int_{M_t}\Phi\,d\mu_t$ 单调不增；且等号在 $[t_1,t_2]$ 上成立当且仅当 $M_t$ 在该时段内是自相似收缩解（在紧致情形即收缩球面）。

## 四、证明过程

**步骤 1（面积元的第一变分）。** 法向速度为 $-H\nu$ 时，第一变分公式给出

$$
\frac{d}{dt}\,d\mu_t=-H^2\,d\mu_t .
$$

**步骤 2（权重的反向热方程）。** 直接对 $\Phi$ 求导并用 $\Delta_x|x-x_0|^2=2(n+1)$：

$$
\partial_t\Phi=-\Delta_{\mathbb R^{n+1}}\Phi .
$$

把 $\Delta\Phi$ 分解为切向与法向部分 $\Delta\Phi=\Delta_{M}\Phi+\langle\nabla^2\Phi\,\nu,\nu\rangle+H\langle\nabla\Phi,\nu\rangle$（Gauss 公式），并注意 $\nabla^{\perp}\log\Phi$ 是 $\nabla\log\Phi$ 的切向投影。

**步骤 3（合并两项并分部积分）。** 记 $I(t)=\int_{M_t}\Phi\,d\mu_t$。由步骤 1、2，

$$
\frac{d I}{dt}=\int_{M_t}\big(\partial_t\Phi+\Phi\,\partial_t\log d\mu_t\big)d\mu_t=\int_{M_t}\big(-\Delta\Phi-H^2\Phi\big)d\mu_t .
$$

在 $M_t$ 上对 $\Delta_{M}\Phi$ 分部积分（$M_t$ 闭，无边界项）：

$$
-\int_{M_t}\Delta_M\Phi\,d\mu_t=0 .
$$

把 $\Delta\Phi=\Delta_M\Phi+\langle\nabla^2\Phi\,\nu,\nu\rangle+H\langle\nabla\Phi,\nu\rangle$ 代入，并用 $\nabla\log\Phi=-\dfrac{x-x_0}{2(t_0-t)}$ 与 $\langle\nabla\log\Phi,\nu\rangle\nu=\nabla\log\Phi-\nabla^{\perp}\log\Phi$ 整理，得到

$$
\frac{d I}{dt}=\int_{M_t}\Big[-\langle\nabla^2\Phi\,\nu,\nu\rangle-H\langle\nabla\Phi,\nu\rangle-H^2\Phi\Big]d\mu_t .
$$

再用 $\langle\nabla^2\Phi\,\nu,\nu\rangle=\Phi\big(|\langle\nabla\log\Phi,\nu\rangle|^2-\frac{1}{2(t_0-t)}\big)$ 及 $\langle\nabla\log\Phi,\nu\rangle^2=|\nabla\log\Phi|^2-|\nabla^{\perp}\log\Phi|^2$ 消去 $\frac{1}{2(t_0-t)}$ 项，最后配方：

$$
\frac{d I}{dt}=-\int_{M_t}\Phi\Big|H\nu-\nabla^{\perp}\log\Phi\Big|^2d\mu_t .
$$

**步骤 4（取等条件）。** 被积函数非负，故 $\dfrac{dI}{dt}\le0$；等号成立当且仅当在 $\Phi>0$ 处

$$
H\nu=\nabla^{\perp}\log\Phi=-\frac{(x-x_0)^{\perp}}{2(t_0-t)} .
$$

这正是自相似收缩方程：曲面在时刻 $t$ 等于某个固定形状按比例 $\sqrt{2(t_0-t)}$ 的缩放。对紧致 $M$，Huisken 证明此类解只能是球面 $S^n$（结合曲率夹逼与 Hopf 引理）。$\square$

## 五、应用与意义

- **奇点分析**：单调量在爆破极限中给出局部"高斯密度"$\Theta$，用于分类平均曲率流的奇点（Huisken 的凸曲面收缩为一点、曲面变球面定理）。
- **非塌缩估计**：单调性等价于"高斯密度不增"，是平均曲率流的 $\kappa$-非塌缩定理的基础。
- **自相似解分类**：取等条件把自相似收缩解与单调量联系起来，是研究 shrinking soliton 的入口。

## 课堂问答

**老师**：平均曲率流的单调量是什么，为什么叫"单调公式"？

**学生**：以反向热核 $\Phi_{x_0,t_0}(x,t)=(4\pi(t_0-t))^{-n/2}\exp\left(-\frac{|x-x_0|^2}{4(t_0-t)}\right)$ 为权重，高斯密度满足 $\frac{d}{dt}\int_{M_t}\Phi\,d\mu_t=-\int_{M_t}\Phi\left|H\nu-\nabla^\perp\log\Phi\right|^2d\mu_t\le0$，故 $t\mapsto\int_{M_t}\Phi\,d\mu_t$ 单调不增。

**老师（追问）**：为什么权重必须取成反向热核？

**学生**：因为要同时用上两条结构：面积元沿流满足 $\partial_td\mu_t=-H^2d\mu_t$，而 $\Phi$ 满足 $\partial_t\Phi=-\Delta\Phi$。把 $\Delta\Phi$ 按切向与法向分解并分部积分，$\frac{1}{2(t_0-t)}$ 这一项被 $|\nabla\log\Phi|^2-|\nabla^\perp\log\Phi|^2$ 消去，剩下的正好配成完全平方 $|H\nu-\nabla^\perp\log\Phi|^2$。

**老师（拓展）**：取等条件说明什么？

**学生**：被积函数非负，取等给出 $H\nu=\nabla^\perp\log\Phi=-\frac{(x-x_0)^\perp}{2(t_0-t)}$，正是自相似收缩方程，紧致情形下 Huisken 证明只有球面。常见误区是把它当成面积单调性：这里加权的是高斯密度，不是面积；正是这个密度在爆破极限中收敛为 $\Theta$，成为 $\kappa$-非塌缩估计与奇点分类的基础。

## 相关条目

- [平均曲率流](./平均曲率流.md)：本公式的主战场。
- [第一变分公式](./第一变分公式.md)：面积元第一变分 $\partial_t d\mu=-H^2d\mu$ 的来源。
- [coarea公式](./coarea公式.md)：均匀化与单调量估计的常用工具。
- [曲率估计与单调公式](./曲率估计与单调公式.md)：单调公式在曲率估计中的应用。
