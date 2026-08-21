# Dirichlet 单位定理

> **一句话大白话**：数域里的"单位"（整数环中可逆元素）尽管可以有无穷多个，但几乎都是有限个"基本单位"的整数倍，再乘上有限个单位根。基本单位个数恰好等于 $r_1+r_2-1$。
>
> **小例子**：$K=\mathbb{Q}(\sqrt{2})$，实数域（$r_1=2$），故单位群秩为 $1$：$\mathcal{O}_K^\times=\{\pm1\}\times\mathbb{Z}$，生成元（基本单位）可取 $\varepsilon=1+\sqrt2$，因为 $1+\sqrt2$ 可逆（$(1+\sqrt2)(-1+\sqrt2)=1$）。

## 一、定理介绍

> **前置依赖**：数域与实、复嵌入、代数整数环与范数、对数嵌入与格、Minkowski 凸体定理、Kronecker 定理。

Dirichlet 单位定理解释了数域单位群的结构：$\mathcal{O}_K^\times$ 是有限生成阿贝尔群，秩等于 $r_1+r_2-1$。它用嵌入与对数嵌入的格论方法，把"单位群有多大"这一问题转化为"一个超平面上格的格秩"问题。

## 二、原理思路

关键是用对数嵌入 $L:K^\times\to\mathbb{R}^{r_1+r_2}$，将单位群映射到一个格（离散子群），并安置在超平面 $H=\{(x_i):\sum x_i=0\}$（因 $\sum_i\log|\sigma_i(u)|=\log|N(u)|=0$）。于是只需证明 $L(\mathcal{O}_K^\times)$ 是 $H$ 中秩 $r_1+r_2-1$ 的完整格。上确界用 Minkowski 凸体定理构造足够多的独立单位；下确界（格性/离散性）使用范数约束给出。

## 三、定理的严格表述

设 $K$ 为数域，$r_1$ 为实嵌入个数，$r_2$ 为复嵌入（共轭）对数，$n=r_1+2r_2$。则
$$\mathcal{O}_K^\times\cong\mu(K)\times\mathbb{Z}^{r_1+r_2-1},$$
其中 $\mu(K)$ 是 $K$ 中的单位根集（有限循环群）。

## 四、证明过程

**证明（Minkowski 几何方法）：**

**步骤 1：定义嵌入。** 定义对数嵌入：
$$L(\alpha)=\big(\log|\sigma_1(\alpha)|,\dots,\log|\sigma_{r_1}(\alpha)|,\,2\log|\tau_1(\alpha)|,\dots,\,2\log|\tau_{r_2}(\alpha)|\big)\in\mathbb{R}^{r_1+r_2}.$$

**步骤 2：核与像。** 由范数 $|N(\alpha)|=1$ 对单位成立，得 $\sum_iL_i(\alpha)=0$，即 $L(\mathcal{O}_K^\times)\subseteq H$（超平面）。且 $\ker L=\mu(K)$：若 $L(\alpha)=0$，则对一切嵌入 $|\sigma(\alpha)|=1$，由 Kronecker 定理（代数整数全部共轭模为 1 则为单位根），$\alpha\in\mu(K)$。$\blacksquare$

**步骤 3：证明 $L(\mathcal{O}_K^\times)$ 是格。** 单位群经 $L$ 的像是紧集上的离散集（因 $\{u\in\mathcal{O}_K^\times:N(u)=1,\ L(u)\text{ 有界}\}$ 是有限集，Minkowski 理论保证），故它是 $H$ 中的离散子群，从而是格，秩 $\le r_1+r_2-1$。$\blacksquare$

**步骤 4：构造足够多的独立单位（满秩）。** 用 Minkowski 凸体定理证明：对任意给定区域约束，存在非零代数整数 $\alpha$ 使 $N(\alpha)<$ 小，从而能在一个"单位维数"方向上扩展。具体地，构造 $\alpha_1,\dots,\alpha_{r_1+r_2-1}$ 使 $L(\alpha_i)$ 是 $H$ 中格的一组 $\mathbb{Z}$-基（闭球覆盖与极限逼近的标准 Minkowski 论证），从而 $L(\mathcal{O}_K^\times)$ 在 $H$ 中秩恰为 $r_1+r_2-1$。$\blacksquare$

结合步骤 2–4 得 $\mathcal{O}_K^\times\cong\mu(K)\times\mathbb{Z}^{r_1+r_2-1}$。$\square$

## 五、应用与意义

Dirichlet 单位定理解析了"无限单位"的来源：有多实嵌入即仅有有限单位（全实域秩 $n-1$），虚域（$r_1=0$）秩减少。它直接导出 Pell 方程、无限阶基本单位、以及正则数域中 $h^-$（类数相对部分）的精细研究。它还连接类数公式（含 $h_K$ 与单位群的调和均值、L-函数特殊值），是解析类域论的枢纽，并通过 Minkowski 方法把几何数论与代数数论紧密缝合。
## 相关条目

- [Dirichlet 单位定理（第53级-代数数论）](../第53级-代数数论/Dirichlet单位定理.md)：与本条目为同一定理，另收录于第53级-代数数论，可交叉参考。
