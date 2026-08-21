# Mordell-Weil 定理

> **一句话大白话**：椭圆曲线在数域上的有理点构成一个"有限生成"的阿贝尔群——它由有限个点（生成元）的和生成，再外加一些（有限个）"转几圈就回到原点"的挠点。曲线上的点远看无穷多，其实只在一个"有限秩的盒子"里生长。
>
> **小例子**：$E:y^2=x^3+1$ 的有理点满足 $E(\mathbb{Q})\cong\mathbb{Z}/6\mathbb{Z}$（纯挠群，秩为 0）：由点 $P=(0,1)$ 生成，$6P=\mathcal{O}$。而 $y^2=x^3-x$ 则有秩 1 的无理点生成族。

## 一、定理介绍

Mordell-Weil 定理说：设 $E$ 是数域 $K$ 上的椭圆曲线，则 $E(K)$ 是有限生成阿贝尔群。1928 年 Weil 把 Mordell（1922，$\mathbb{Q}$ 情形）的结果推广到任意数域与 Abel 簇。由此可引入类型参数纯量：秩与挠子群，是现代算术几何的基点。

## 二、原理思路

证明分三个部分：弱 Mordell-Weil 定理（$E(K)/mE(K)$ 有限）、高度函数（下降法）、以及"下降调幅"的组合。核心是"无限下降法"——反复把一个点写为 $m$ 倍点加上有限个代表元，用高度（坐标的"大小"）约束保证每次下降后剩余点落在有限集合，最终所有点都由有限个生成元表出。

## 三、定理的严格表述

设 $E$ 是数域 $K$ 上的椭圆曲线。则 $E(K)$ 是有限生成阿贝尔群：
$$E(K)\cong\mathbb{Z}^{r}\oplus E(K)_{\text{tors}},$$
其中 $r=\operatorname{rank}(E/K)\ge0$ 是秩，$E(K)_{\text{tors}}$ 是有限挠子群。

## 四、证明过程

**证明策略：**

**步骤 1：弱 Mordell-Weil 定理。** 证明对某个 $m\ge2$，$E(K)/mE(K)$ 是有限群。取 Kummer 理论：对正合列 $0\to E[m]\to E\xrightarrow{[m]}E\to0$ 取 Galois 上同调得长正合列，从而 Kummer 映射 $\kappa:E(K)/mE(K)\hookrightarrow H^1(G_K,E[m])$。结合有限性论证（类数有限、Dirichlet 单位定理）可知像落在有限子群中，故 $E(K)/mE(K)$ 有限。$\blacksquare$

**步骤 2：高度函数。** 定义规范高度（Néron-Tate 高度）$\hat{h}:E(K)\to\mathbb{R}_{\ge0}$，满足：$\hat{h}(P)=0\iff P$ 为挠点；对 $M>0$，集合 $\{P:\hat{h}(P)\le M\}$ 有限；$\hat{h}([m]P)=m^2\hat{h}(P)$；配对 $\langle P,Q\rangle=\hat{h}(P+Q)-\hat{h}(P)-\hat{h}(Q)$ 是双线性形式。

**引理（无限下降引理）** 若 $A/mA$ 有限且 $h$ 满足上述性质，则 $A$ 有限生成。
**证明：** 取 $A/mA$ 代表元 $Q_1,\dots,Q_s$。对任意 $P\in A$ 反复写 $P=mP_1+Q_{i_1}$，$P_1=mP_2+Q_{i_2}$，\dots，$n$ 步后
$$P=m^nP_n+\sum_{k=1}^{n}m^{k-1}Q_{i_k}.$$
由高度性质：$\hat{h}(P_n)=\frac1{m^{2n}}\hat{h}\big(m^nP_n\big)$，当 $n$ 大时 $\hat{h}(P_1)$ 型量有界，故 $P_n$ 只能取有限个值，于是 $P$ 由 $Q_i$ 与这些有限个元素生成。$\blacksquare$

**步骤 3：总结。** 结合弱定理（$E(K)/mE(K)$ 有限）与无限下降引理，$E(K)$ 有限生成。秩 $r$ 为自由部分秩，挠子群有限（由复乘/模形式理论可具体计算）。$\square$

## 五、应用与意义

Mordell-Weil 定理把椭圆曲线有理点结构归结为两个有限不变量（秩与挠群），是算术几何支柱之一。它支撑弱 Mordell-Weil 与 2-下降、Birch–Swinnerton-Dyer 猜想的表述（$L(E,s)$ 的零点阶 = 秩），并推广到高维 Abel 簇与 Jacobian，是 Faltings（Mordell 猜想）、Chabauty、以及现代"有效 Mordell"研究的基础。