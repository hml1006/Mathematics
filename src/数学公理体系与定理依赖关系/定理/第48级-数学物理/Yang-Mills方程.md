# Yang-Mills方程

> **一句话大白话**：把 Maxwell 的电磁方程推广到"非交换的规范场"：场强 $F=dA+A\wedge A$ 满足 $d_AF=\star JF$（运动方程）和 Bianchi 恒等式 $d_AF=0$；$A$ 与 $F$ 在规范变换下像"联络与曲率"。
>
> **小例子**：单位元上取联络 $A$ 时，Yang–Mills 方程即 $\nabla^{A}\!\star F_A=J$；自对偶解（$F=-*F$，四维）给出瞬子，一端联系着模空间的几何。

## 介绍

Yang-Mills方程（Yang-Mills Equations）是杨振宁和 Robert Mills 在1954年提出的非Abel规范场论的基本方程，是 Maxwell 方程的非Abel推广。Yang-Mills理论描述了一类由非交换李群（如 $SU(n)$）刻画的规范场（即"杨-米尔斯场"），其方程是规范势的 Euler-Lagrange 方程。Yang-Mills方程在现代物理学中扮演着核心角色——它是标准模型（$SU(3) \times SU(2) \times U(1)$ 规范群）的数学基础，描述了强相互作用和弱相互作用。在数学上，Yang-Mills方程是纤维丛上联络的变分方程，其解（Yang-Mills联络）是规范理论几何研究的核心对象。

## 分析

**定理的精确表述**：设 $G$ 是紧致李群，$P \to M$ 是 $G$-主丛，$A$ 是 $P$ 上的联络（规范势），$F_A = dA + A \wedge A$ 是曲率（场强）。Yang-Mills 作用量为

$$
S_{\mathrm{YM}}(A) = \int_M \|F_A\|^2 \, d\mathrm{vol} = \int_M \mathrm{Tr}(F_A \wedge *F_A).
$$

Yang-Mills 方程是作用量的 Euler-Lagrange 方程：

$$
d_A *F_A = 0,
$$

其中 $d_A$ 是协变外微分，$*$ 是 Hodge 星算子。结合 Bianchi 恒等式 $d_A F_A = 0$，Yang-Mills 场满足

$$
d_A F_A = 0, \quad d_A *F_A = 0.
$$

**依赖的概念**：主丛、联络、曲率、规范群、Hodge 对偶、Euler-Lagrange 方程。

**特殊情形**：
- 当 $G = U(1)$ 时，Yang-Mills 方程退化为真空 Maxwell 方程 $dF = 0$，$d*F = 0$。
- 在 4 维流形上，自对偶（$*F = F$）和反自对偶（$*F = -F$）联络自动满足 Yang-Mills 方程，称为**瞬子**。

## 思考过程

Yang-Mills方程是规范场论的非线性推广。与线性 Maxwell 理论不同，由于 $A \wedge A$ 项的存在，Yang-Mills 方程是非线性的，这带来了丰富的数学结构。

Yang-Mills 方程也可以从变分原理推导：作用量 $S_{\mathrm{YM}}(A)$ 在规范变换 $A \to g^{-1}Ag + g^{-1}dg$ 下不变，其临界点就是 Yang-Mills 联络。

在 4 维流形上，Yang-Mills 方程与流形的拓扑有深刻联系。特别地，瞬子（自对偶联络）的模空间是 4 维流形的不变量（Donaldson 不变量），这导致了 4 维拓扑的重大突破。

## 证明过程

**定理**（Yang-Mills 方程的变分推导）：Yang-Mills 作用量 $S_{\mathrm{YM}}(A) = \int_M \mathrm{Tr}(F_A \wedge *F_A)$ 的 Euler-Lagrange 方程是 $d_A *F_A = 0$。

**证明**：

**步骤 1：变分计算。**

考虑联络 $A$ 的无穷小变分 $A \to A + t\alpha$，其中 $\alpha$ 是 $\mathfrak{g}$-值的1-形式。曲率的变化为

$$
F_{A + t\alpha} = F_A + t(d_A \alpha) + t^2 (\alpha \wedge \alpha).
$$

一阶变分为

$$
\frac{d}{dt}\Big|_{t=0} S_{\mathrm{YM}}(A + t\alpha) = 2 \int_M \mathrm{Tr}(d_A \alpha \wedge *F_A).
$$

**步骤 2：分部积分。**

利用 $\mathrm{Tr}(d_A \alpha \wedge *F_A) = d\mathrm{Tr}(\alpha \wedge *F_A) - \mathrm{Tr}(\alpha \wedge d_A *F_A)$，由 Stokes 定理，边界项为零（假设 $\alpha$ 紧支或 $M$ 无边），得

$$
\frac{d}{dt}\Big|_{t=0} S_{\mathrm{YM}}(A + t\alpha) = -2 \int_M \mathrm{Tr}(\alpha \wedge d_A *F_A).
$$

**步骤 3：Euler-Lagrange 方程。**

由于 $\alpha$ 任意，变分为零要求

$$
d_A *F_A = 0.
$$

此即 Yang-Mills 方程。$\square$

**定理**（Bianchi 恒等式）：对任意联络 $A$，$d_A F_A = 0$。

**证明**：由 $F_A = dA + A \wedge A$，计算

$$
d_A F_A = dF_A + A \wedge F_A - F_A \wedge A = d(dA + A \wedge A) + A \wedge (dA + A \wedge A) - (dA + A \wedge A) \wedge A.
$$

由于 $d^2 = 0$，$d(A \wedge A) = dA \wedge A - A \wedge dA$，展开得

$$
d_A F_A = dA \wedge A - A \wedge dA + A \wedge dA + A \wedge A \wedge A - dA \wedge A - A \wedge A \wedge A = 0.
$$

$\square$

**推论**（自对偶解）：在 4 维定向 Riemann 流形上，若 $*F_A = \pm F_A$，则 $d_A *F_A = \pm d_A F_A = 0$，故自对偶和反自对偶联络自动满足 Yang-Mills 方程。这些解称为**瞬子**，其作用量由拓扑数决定：

$$
S_{\mathrm{YM}}(A) = 8\pi^2 |k|,
$$

其中 $k = \frac{1}{8\pi^2} \int_M \mathrm{Tr}(F_A \wedge F_A)$ 是第二陈数。