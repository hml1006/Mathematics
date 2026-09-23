# Siegel 平均公式

> **一句话大白话**：把所有"行列式为 1 的格"拿来取平均，落在任意区域 $S$ 中的非零格点数，平均起来恰好等于 $S$ 的体积——格点就好像均匀随机地撒在整个空间里。
>
> **小例子**：取 $S$ 为面积 $1$ 的小方块，则"平均格"在 $S$ 内的非零格点数为 $1$；取 $S=[-1,1]^2$（面积 $4$）时平均计数为 $4$。

## 一、定理介绍

> **前置依赖**：格与幺模格、格空间 $\operatorname{SL}_n(\mathbb{R})/\operatorname{SL}_n(\mathbb{Z})$ 与 $G$-不变测度、Haar 测度与基本域、展开技巧（unfolding）、Fubini 定理

Siegel 平均公式（Siegel 均值定理，Siegel's mean value theorem，C. L. Siegel，1945）是几何数论与自守形式理论中最基本的"平均化"工具。它断言：只要在格空间上取适当规范的 $G$-不变测度，"格点计数"的期望就等于对应的连续体积。

它的价值在于把离散的格点求和 $\sum_{v\in\Lambda\setminus\{0\}}f(v)$ 对全体格取平均后，变成 $\mathbb{R}^n$ 上一个普通积分 $\int f$。于是许多关于格的极值问题（是否存在"好格"）可以用测度论和概率论处理：若平均计数小于某个阈值，就必然存在一个格使计数取到小值。

它是 Minkowski–Hlawka 定理、格的最密堆积与覆盖、格点极限分布定理、以及单模格空间体积计算（Siegel 质量公式方向）的共同基础。

## 二、原理思路

核心想法有两层：

1. **参数化与平均化**：行列式为 $1$ 的格与齐性空间 $\mathcal{L}=G/H$（$G=\operatorname{SL}_n(\mathbb{R})$，$H=\operatorname{SL}_n(\mathbb{Z})$）一一对应，其上的 $G$-不变测度继承自 Haar 测度。"对格取平均"就是在 $\mathcal{L}$ 上积分。

2. **展开技巧（unfolding）**：$\mathbb{Z}^n\setminus\{0\}$ 中每个向量 $v=kw$（$k\ge 1$，$w$ 本原）都对应一次 $H$-轨道。把 $\sum_{v}f(vg)$ 按 $H$ 的轨道展开，求和式的平均就化为单个函数 $f(e_1g)$ 在 $G$ 上的积分；再用 $g\mapsto e_1g$ 把 $G$ 对 $e_1$ 的轨道空间 $P_0\backslash G$ 与 $\mathbb{R}^n\setminus\{0\}$ 等同，测度随之分解为 Lebesgue 测度。最后对"倍数" $k$ 求和得到 $\zeta(n)$，其与测度规范的常数一并被 Siegel 规范吸收为 $1$。

## 三、定理的严格表述

（Siegel 平均公式）设 $n\ge 2$，$G=\operatorname{SL}_n(\mathbb{R})$，$H=\operatorname{SL}_n(\mathbb{Z})$，$\mathcal{L}=G/H$ 为所有行列式 $1$ 的格构成的空间。则存在 $\mathcal{L}$ 上唯一的（相差常数倍）$G$-不变测度 $\mu$，取 Siegel 规范后满足：对任意 $f\in L^1(\mathbb{R}^n)$，

$$
\int_{\mathcal{L}}\Big(\sum_{v\in\Lambda\setminus\{0\}}f(v)\Big)\,d\mu(\Lambda)=\int_{\mathbb{R}^n}f(x)\,dx .
$$

特别地，取 $f=\chi_S$（$S$ 有界可测、边界零测），则非零格点计数的平均等于体积：

$$
\int_{\mathcal{L}}\#(\Lambda\cap S\setminus\{0\})\,d\mu(\Lambda)=\operatorname{vol}(S).
$$

## 四、证明过程

**步骤 1：约化到紧支光滑函数。** 由线性性与控制收敛定理，只需对 $f\in C_c^\infty(\mathbb{R}^n)$ 证明。此时 $F(g)=\sum_{v\ne 0}f(vg)$ 在 $H\backslash G$ 上良定义（因 $f$ 紧支，和有限）且可积。

**步骤 2：按本原向量分解。** 每个非零整向量 $v$ 唯一地写成 $v=kw$，其中 $k\ge1$，$w$ 本原（各坐标互素）。于是

$$
F(g)=\sum_{k\ge1}\sum_{w\ \text{本原}}f(kwg).
$$

**步骤 3：展开技巧。** $H$ 传递地作用在本原整向量集合上，稳定化子为 $P_H=\{h\in H: e_1h=e_1\}$，故本原向量与 $H/P_H$ 一一对应：$w=e_1h$。对固定的 $k$，求和 $\sum_{w}f(kwg)=\sum_{h\in H/P_H}f(ke_1hg)$ 关于 $H$ 左作用不变，标准展开给出

$$
\int_{H\backslash G}\sum_{w\ \text{本原}}f(kwg)\,dg=\int_{P_H\backslash G}f(ke_1g)\,dg .
$$

**步骤 4：测度的分解。** 记 $P_0=\{g\in G: e_1g=e_1\}\cong \mathbb{R}^{n-1}\rtimes \operatorname{SL}_{n-1}(\mathbb{R})$，它是可单位模的，$P_H=P_0\cap H$ 在 $P_0$ 中余体积有限，记 $c_0=\operatorname{vol}(P_H\backslash P_0)$。由 $P_H\backslash G\to P_0\backslash G$ 是有限纤维丛，

$$
\int_{P_H\backslash G}f(ke_1g)\,dg=c_0\int_{P_0\backslash G}f(ke_1g)\,dg .
$$

又 $e_1g$ 使 $P_0\backslash G\cong \mathbb{R}^n\setminus\{0\}$ 成为 $G$-同构（$G$ 由右乘作用），而 $G$ 保 Lebesgue 测度 $dx$（因 $\det g=1$），故推前测度为 $dx$ 的常数倍，记常数为 $c_1$：

$$
\int_{P_0\backslash G}f(ke_1g)\,dg=c_1\int_{\mathbb{R}^n}f(kx)\,dx .
$$

**步骤 5：对倍数求和与规范化。** 合并步骤 3、4 并对 $k$ 求和，换元 $x\mapsto kx$ 给出

$$
\int_{\mathcal{L}}F(g)\,dg=\sum_{k\ge1}c_0c_1\int_{\mathbb{R}^n}f(kx)\,dx=c_0c_1\Big(\sum_{k\ge1}\frac{1}{k^n}\Big)\int_{\mathbb{R}^n}f(x)\,dx .
$$

由 $n\ge2$，$\zeta(n)=\sum_{k\ge1}k^{-n}$ 收敛，故右端为常数 $C_n=c_0c_1\zeta(n)\in(0,\infty)$ 乘以 $\int f$。由于 $G$-不变测度只相差一个常数倍，定义 Siegel 规范测度 $d\mu=dg/C_n$，即得

$$
\int_{\mathcal{L}}F\,d\mu=\int_{\mathbb{R}^n}f(x)\,dx .
$$

对一般的 $f\in L^1$，取 $f_j\in C_c^\infty$ 逼近并用控制收敛定理即得。$\blacksquare$

## 五、应用与意义

**理论意义：**

1. **Minkowski–Hlawka 定理**：取 $f=\chi_K$，平均值 $=\operatorname{vol}(K)$；对称性使每个格的非零格点数成对出现，当 $\operatorname{vol}(K)<2\zeta(n)$ 时必存在某个格使 $K$ 内非零格点数为 $0$。

2. **格点的极限分布**：格空间上的随机格模型使"随机格的点过程"在归一化后趋于 Poisson 过程，Siegel 公式是最低阶矩的计算基础。

3. **单模格空间的体积**：$\operatorname{vol}(\mathcal{L})$ 与 $\zeta$ 值、基本单位、类数之间的关系可由该规范化确定，是 Siegel 质量公式的起点。

**应用领域：** 几何数论（临界行列式、覆盖半径、最密堆积下界）、自守形式与 Eisenstein 级数（退化主级数的常数项）、随机矩阵与格密码学中的格分布模型。

**推广：** 对一般的半单群 $G$ 与算术子群 $\Gamma$，同型的"展开公式"给出 Eisenstein 级数与轨道积分的均值公式，是 Langlands 纲领与迹公式的核心机制之一。
