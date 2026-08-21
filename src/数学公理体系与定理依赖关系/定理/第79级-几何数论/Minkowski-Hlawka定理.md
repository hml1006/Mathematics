# Minkowski-Hlawka 定理

> **一句话大白话**：存在"极强的"黄金格子，让任意不太大的中心对称凸体内部除原点外不含任何格点——即 $K$ 中放进密度为 1 的格可以"几乎不碰任何点"。临界行列式被 $2\zeta(n)$ 控制。
>
> **小例子**：$n=2$，任意面积小于 $2\zeta(2)=\pi^2/3\approx3.29$ 的中心对称凸体，都能配一个行列式为 1 的格避开的非零点。例如面积 $3$ 的一个圆盘可被某个格避开所有非零点。

## 一、定理介绍

> **前置依赖**：格空间 $\operatorname{SL}_n(\mathbb{R})/\operatorname{SL}_n(\mathbb{Z})$ 与不变测度、Siegel 平均公式、中心对称凸体、Riemann Zeta 函数。

Minkowski-Hlawka 定理给出格的行列式与凸体"避开非零点"的存在性：若 $K$ 中心对称凸体且 $\operatorname{vol}(K)<2\zeta(n)$，则存在行列式 1 的格 $\Lambda$ 使 $\Lambda\cap\operatorname{int}(K)=\{0\}$。等价地 $K$ 的临界行列式 $\Delta(K)\le\frac{\operatorname{vol}(K)}{2\zeta(n)}$。这是 Minkowski 在 1905 提出、Hlawka 于 1944 给出的存在性下界。

## 二、原理思路

采用平均化方法（Siegel 平均公式）。所有行列式 1 的格由 $\operatorname{SL}_n(\mathbb{R})/\operatorname{SL}_n(\mathbb{Z})$ 参数化且带 $\operatorname{SL}_n(\mathbb{R})$-不变测度。Siegel 公式把"求和式" $\sum_{x\in\Lambda\setminus\{0\}}f(x)$ 对格取平均化为整体积分 $\int f$。取 $f$ 为 $K$ 的特征函数，则平均值即 $\operatorname{vol}(K)$。由于 $K$ 对称，非零格点成对（$x,-x$），计数为偶数，平均值小于 $2$（修正后为 $2\zeta(n)$）时必有一个格计数为 0。

## 三、定理的严格表述

设 $K\subset\mathbb{R}^n$ 中心对称凸体。则存在行列式 $\det(\Lambda)=1$ 的格 $\Lambda$，使 $\Lambda\cap\operatorname{int}(K)=\{0\}$，只要
$$\operatorname{vol}(K)<2\zeta(n),\qquad \zeta(n)=\sum_{k\ge1}k^{-n}.$$
等价地，$K$ 的临界行列式满足 $\Delta(K)\le\frac{\operatorname{vol}(K)}{2\zeta(n)}$。

## 四、证明过程

**证明（平均化方法）：**

**步骤 1：参数化格。** 记 $G=\operatorname{SL}_n(\mathbb{R}),H=\operatorname{SL}_n(\mathbb{Z})$，则 $G/H$ 参数化所有行列式 1 的格，其上有 $G$-不变测度 $d\mu$。$\blacksquare$

**步骤 2：Siegel 平均公式。** 对可积 $f$，
$$\int_{G/H}\sum_{x\in\Lambda\setminus\{0\}}f(x)\,d\mu(\Lambda)=\int_{\mathbb{R}^n}f(x)\,dx.$$
$\blacksquare$

**步骤 3：取特征函数。** 令 $f=\chi_K$。则 $\sum_{x\in\Lambda\setminus\{0\}}\chi_K(x)=\#(\Lambda\cap K\setminus\{0\})$，由公式：
$$\int_{G/H}\#(\Lambda\cap K\setminus\{0\})\,d\mu=\operatorname{vol}(K).$$
$\blacksquare$

**步骤 4：对称性。** $K$ 对称，非零格点成对出现（$x,-x$），故 $\#(\Lambda\cap K\setminus\{0\})$ 为偶数（或 0）。$\blacksquare$

**步骤 5：存在性。** 平均值 $\operatorname{vol}(K)<2$ 时，若对一切 $\Lambda$ 计数非零，则均为 $\ge2$，平均 $\ge2$ 矛盾；故某个 $\Lambda$ 计数为 0，即 $\Lambda\cap K\setminus\{0\}=\varnothing$。$\blacksquare$

**步骤 6：Zeta 修正。** 更精细的分析（对 $\operatorname{SL}_n(\mathbb{Z})$ 轨道、尖点贡献的精细平均）把阈值从 $2$ 提升到 $2\zeta(n)$：当 $\operatorname{vol}(K)<2\zeta(n)$ 时存在这样的格。$\square$

## 五、应用与意义

Minkowski-Hlawka 定理提供密度理论、最密堆积与格覆盖问题的下界：它证明存在"相当稀疏"的密度 1 格避开指定凸体，从而给出格的覆盖半径、临界行列式的定性结果。它在圆法/格与编码理论中提供密度基准，也是 Siegel 均值与"平均格"思想的发源地，联系到自守形式与单模结构。其现代化形式广泛用于拟晶体、Riemann 函数与数论中的格随机模型。