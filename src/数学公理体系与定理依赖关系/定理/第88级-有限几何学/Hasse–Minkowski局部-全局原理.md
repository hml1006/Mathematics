# Hasse–Minkowski 局部-全局原理

> **一句话大白话**：一个有理系数的二次方程（二次型）在有理数里有没有解，只要看它在每个"局部世界"（实数与所有 $p$ 进数）里有没有解就够了——局部处处有解，则整体必有解。
>
> **小例子**：$x^2+y^2+z^2=6$ 在 $\mathbb{R}$ 与每个 $\mathbb{Q}_p$ 上都有解，由本原理它在 $\mathbb{Q}$ 中也有有理解（如 $(1,1,2)$）；而 $x^2+y^2+z^2=-1$ 在 $\mathbb{R}$ 无解，故在 $\mathbb{Q}$ 必无解。

## 一、定理介绍

> **前置依赖**：二次型与等价、p进数与局部域、Hilbert 符号、Hasse-Minkowski 定理、二次互反律。

Hasse–Minkowski 定理（又称 Hasse 原理或局部–全局原理）由 Helmut Hasse 在 1920 年代建立，它把二次型的有理性问题完全"局部化"。受 Hensel 的 $p$ 进方法启发，Hasse 发现二次型的等价与表示只由每个局部域 $\mathbb{Q}_p$ 与 $\mathbb{R}$ 上的行为决定，并由此推出：局部处处等价的二次型整体等价，局部处处可表示的元素整体可表示。这一原理是代数数论与算术几何的里程碑：它首次系统地展示了"局部信息决定整体"的思想，直接通向类域论、Hasse 范数定理，以及后来对"局部–全局原则失效"的研究（Brauer–Manin 障碍）。对二次型而言，它把判定与分类问题变成有限步的计算。

## 二、原理思路

1. 用 Hilbert 符号 $(\cdot,\cdot)_p$ 把二次型在每个局部域上的信息编码为一组不变量（维数、判别式、Hasse 不变量），这些量在等价下不变且构成完全的局部不变量。
2. 证明"局部等价推出整体等价"：对维数作归纳，用 Witt 消去定理与二次互反律保证的乘积公式 $\prod_p(a,b)_p=1$ 消除局部障碍，逐步把两个二次型同时消去一个公共分量。
3. 由等价性推出表示问题：$q$ 在 $\mathbb{Q}$ 上表示 $a$ 当且仅当每个 $q_p$ 都表示 $a$，其关键在于对 $q\perp\langle -a\rangle$ 判定"是否等向"，再化归为等价问题。

## 三、定理的严格表述

设 $q,q'$ 为 $\mathbb{Q}$ 上维数相同的非退化二次型。则

$$
q \cong_{\mathbb{Q}} q' \quad\Longleftrightarrow\quad q\cong_{\mathbb{Q}_p} q'\ \text{对所有素数 } p,\ \text{且}\ q\cong_{\mathbb{R}} q'.
$$

等价的表示形式：设 $q$ 为 $\mathbb{Q}$ 上非退化二次型，$a\in\mathbb{Q}^{\times}$，则

$$
a\ \text{被}\ q\ \text{在}\ \mathbb{Q}\ \text{上表示} \iff a\ \text{被}\ q\ \text{在}\ \mathbb{Q}_p\ \text{上表示}(\forall p)\ \text{且被}\ \mathbb{R}\ \text{上表示}.
$$

## 四、证明过程

**步骤 1（局部不变量的良定义）。** 设非退化二次型 $q\cong\langle a_1,\dots,a_n\rangle$，记判别式 $d=a_1\cdots a_n$，并定义 Hasse 不变量

$$
c_p(q)=\prod_{1\le i<j\le n}(a_i,a_j)_p ,
$$

其中 $(\cdot,\cdot)_p$ 为 Hilbert 符号。计算表明：$q\cong q'$ 在 $\mathbb{Q}_p$ 上成立，当且仅当二者维数相同、$d$ 相同且 $c_p$ 相同。故 $(\dim,d,c_p)$ 是完全的局部不变量。

**步骤 2（乘积公式）。** 由二次互反律可导出：对所有 $a,b\in\mathbb{Q}^{\times}$，

$$
\prod_{p\le\infty} (a,b)_p = 1 ,
$$

乘积遍历全部素数与 $p=\infty$（即 $\mathbb{R}$）。这是诸局部不变量之间唯一的整体约束。

**步骤 3（归纳消去公共分量）。** 设 $q,q'$ 处处局部等价。对维数 $n$ 归纳。由步骤 1、2 及"局部处处表示"可构造 $a\in\mathbb{Q}^{\times}$ 同时被 $q$ 与 $q'$ 表示，于是

$$
q\cong a\perp q_1,\qquad q'\cong a\perp q_1' .
$$

由 Witt 消去定理，$q_1\cong q_1'$ 在每个局部域上成立；归纳假设给出 $q_1\cong q_1'$（整体），故 $q\cong q'$。递推到底即证完。

**步骤 4（表示情形）。** 设 $a$ 在 $\mathbb{Q}_p$（所有 $p$）与 $\mathbb{R}$ 上都被 $q$ 表示。考虑二次型 $q\perp\langle -a\rangle$：它在每个局部域上都表示 $0$（即等向），由步骤 3 的整体等价/等向性判定知 $q\perp\langle-a\rangle$ 在 $\mathbb{Q}$ 上等向，即存在 $v$ 使 $q(v)=a$，故 $a$ 被 $q$ 在 $\mathbb{Q}$ 上表示。反向是显然的。$\square$

## 五、应用与意义

- 完全解决有理数上二次型的等价与表示问题，是二次型算术理论的基石。
- 引出"局部–全局原理"这一方法论，影响类域论、Hasse 范数定理以及椭圆曲线的 Brauer–Manin 障碍研究。
- 与 Minkowski 的几何数论互补：局部可解性由 $p$ 进分析判定，整体计数由 Minkowski 凸体定理给出。

## 相关条目

- [Hasse-Minkowski定理](../第53级-代数数论/Hasse-Minkowski定理.md)：同一定理的代数数论表述与完整证明。
- [p进数与局部域](../第53级-代数数论/p进数与局部域.md)：局部域与 $p$ 进分析的基础。
- [二次型的Minkowski约化定理](../第79级-几何数论/二次型的Minkowski约化定理.md)：二次型的几何数论视角。
- [Bruck-Ryser定理](./Bruck-Ryser定理.md)：同为有限几何中用数论不变量排除存在性的定理。
