# Fisher-Tippett-Gnedenko定理

> **一句话大白话**：无论数据本身是什么分布，经过适当归一化后样本最大值的极限分布只可能长成三种样子：Gumbel（轻尾）、Fréchet（重尾）、Weibull（有界尾）。
>
> **小例子**：指数样本最大值标准化后收敛到 Gumbel，Pareto 样本的最大值标准化后收敛到 Fréchet，它们都属于这"三大极限类型"之一。

## 一、定理介绍

设 $X_1,\dots,X_n$ 为 i.i.d. 随机变量，分布函数 $F$，$M_n=\max\{X_1,\dots,X_n\}$。若存在归一化常数 $a_n>0$、$b_n\in\mathbb{R}$ 使 $(M_n-b_n)/a_n\xrightarrow{d}G$（$G$ 非退化），则 $G$ 必属于三种标准类型之一：Gumbel $G_0(x)=e^{-e^{-x}}$、Fréchet $G_{1,\alpha}(x)=e^{-x^{-\alpha}}(x>0)$、Weibull $G_{2,\alpha}(x)=e^{-(-x)^\alpha}(x<0)$。这一分类是极值理论的基础。

## 二、原理思路

关键在"可稳定性"。因 $M_{mn}=\max\{M_n^{(1)},\dots,M_n^{(m)}\}$ 且各组独立，极限分布 $G$ 必须满足极值类型方程 $G^m(x)=G(A(m)x+B(m))$。取对数令 $H=-\log G$，得 $mH(x)=H(A(m)x+B(m))$，用函数方程理论分三种情形求解 $H$ 的解析形式，分别对应 Gumbel、Weibull、Fréchet，进而统一为 GEV 分布。

## 三、定理的严格表述

令 $M_n=\max\{X_1,\dots,X_n\}$，$X_i$ i.i.d.。若存在 $a_n>0,b_n$ 使
$$
\frac{M_n-b_n}{a_n}\xrightarrow{d}G,\qquad n\to\infty,
$$
且 $G$ 非退化，则 $G$ 属于以下之一（经位置尺度变换）：
$$
G_0(x)=e^{-e^{-x}}\;(x\in\mathbb{R}),\quad
G_{1,\alpha}(x)=e^{-x^{-\alpha}}\;(x>0,\alpha>0),\quad
G_{2,\alpha}(x)=e^{-(-x)^\alpha}\;(x<0,\alpha>0).
$$
统一为 GEV 形式（$\xi=0$ 为 Gumbel，$\xi>0$ 为 Fréchet，$\xi<0$ 为 Weibull）：
$$
G_\xi(x)=\exp\left\{-\left[1+\xi\frac{x-\mu}{\sigma}\right]^{-1/\xi}\right\}.
$$

## 四、证明过程

**步骤1：稳定性方程。** 由 $M_{mn}=\max\{M_n^{(j)}\}$、独立性得 $\mathbb P(M_{mn}\le x)=[\mathbb P(M_n\le x)]^m$，迫使极限 $G$ 满足 $G^m(x)=G(A(m)x+B(m))$。

**步骤2：化对数。** 令 $H=-\log G$，$mH(x)=H(A(m)x+B(m))$，$H$ 非负单调递增。

**步骤3：分情形求解。**
- 若 $H(x)=0(\forall x\le\omega)$ 且 $\omega<\infty$：设 $H(x)=c(\omega-x)^\alpha$，解得 $A(m)=m^{-1/\alpha}$、$B(m)=\omega(1-m^{-1/\alpha})$，得 Weibull $G(x)=e^{-c(\omega-x)^\alpha}$。
- 若 $H(x)>0(\forall x)$ 且严格递减：设 $H(x)=e^{-x}$，解得 $A(m)=1$、$B(m)=\log m$，得 Gumbel $G(x)=e^{-e^{-x}}$。
- 若 $H(x)=0(x\le0)$ 且 $H(x)>0(x>0)$：设 $H(x)=x^{-\alpha}$，解得 $A(m)=m^{1/\alpha}$、$B(m)=0$，得 Fréchet $G(x)=e^{-x^{-\alpha}}$。

**步骤4：统一表示。** 通过位置尺度参数化把三族统一为 GEV。$\square$

## 五、应用与意义

Fisher-Tippett-Gnedenko 定理给出了"样本最大值的极限唯有三种类型"，是块极大值建模（GEV 拟合）的理论依据。它支撑重现期估计、金融 VaR 与水文学洪峰分析，是连接极值概率论与统计应用的核心支柱。