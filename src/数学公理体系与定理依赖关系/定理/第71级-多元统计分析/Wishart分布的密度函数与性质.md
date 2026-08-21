# Wishart 分布的密度函数与性质

> **一句话大白话**：Wishart 分布是多元正态样本协方差矩阵（的 $n$ 倍）的概率分布，是卡方分布在多维情形的推广：标准卡方 $\chi^2$ 是"单个随机数的平方和"，而 Wishart 是"向量与其转置的外积之和"。
>
> **小例子**：对二维正态样本，$\boldsymbol{W}=\sum\boldsymbol{X}_i\boldsymbol{X}_i^\top$ 是一个 $2\times2$ 对称矩阵，其三个独立元素（对角两项与交叉项）共同服从 Wishart 分布，对角元分别近似比例的 $\chi^2$ 分布。

## 一、定理介绍

> **前置依赖**：多元正态分布、Cholesky 分解、Jacobian 行列式、Stiefel 流形、Gamma 函数。

Wishart 分布 $W_p(n,\boldsymbol{\Sigma})$ 描述随机矩阵 $\boldsymbol{W}=\sum_{i=1}^n\boldsymbol{X}_i\boldsymbol{X}_i^\top$ 的分布，其中 $\boldsymbol{X}_i\sim N_p(\boldsymbol{0},\boldsymbol{\Sigma})$。它是一元 $\chi^2$ 分布的多维推广，也是多元正态总体协方差矩阵估计、Hotelling $T^2$ 检验以及多元方差分析的理论基础。该定理给出了 Wishart 分布的显式密度函数，并刻画了其期望与可加性等关键性质。

## 二、原理思路

证明采用矩阵变量的变量变换法：从 $\boldsymbol{X}$ 的密度出发，通过 Cholesky 分解 $\boldsymbol{W}=\boldsymbol{T}^\top\boldsymbol{T}$（$\boldsymbol{T}$ 为上三角、对角元为正），并在 Stiefel 流形 $V_{n,p}=\{\boldsymbol{U}\in\mathbb{R}^{n\times p}:\boldsymbol{U}^\top\boldsymbol{U}=\boldsymbol{I}_p\}$ 上积掉正交部分。关键计算是 Stiefel 流形的体积公式与 Jacobian 行列式 $\prod_{i=1}^p t_{ii}^{n-i}$，最终整合出 Wishart 密度；一般 $\boldsymbol{\Sigma}$ 情形由标准化 $\boldsymbol{Y}_i=\boldsymbol{\Sigma}^{-1/2}\boldsymbol{X}_i$ 与线性变换的 Jacobian 得出。

## 三、定理的严格表述

设 $\boldsymbol{X}_1,\dots,\boldsymbol{X}_n$ 独立同分布于 $N_p(\boldsymbol{0},\boldsymbol{\Sigma})$，$\boldsymbol{W}=\sum_{i=1}^n\boldsymbol{X}_i\boldsymbol{X}_i^\top$。则 $\boldsymbol{W}$ 的概率密度函数为：
$$
f(\boldsymbol{W})=\frac{|\boldsymbol{W}|^{(n-p-1)/2}\exp(-\frac{1}{2}\operatorname{tr}(\boldsymbol{\Sigma}^{-1}\boldsymbol{W}))}{2^{np/2}\pi^{p(p-1)/4}|\boldsymbol{\Sigma}|^{n/2}\prod_{i=1}^p\Gamma(\frac{n+1-i}{2})},\quad \boldsymbol{W}\succ0.
$$

**期望性质**：$\mathbb{E}[\boldsymbol{W}]=n\boldsymbol{\Sigma}$。
**可加性**：若 $\boldsymbol{W}_1\sim W_p(n_1,\boldsymbol{\Sigma})$ 与 $\boldsymbol{W}_2\sim W_p(n_2,\boldsymbol{\Sigma})$ 独立，则 $\boldsymbol{W}_1+\boldsymbol{W}_2\sim W_p(n_1+n_2,\boldsymbol{\Sigma})$。

## 四、证明过程

**证明（变量变换法）：**

**步骤 1：标准情形。** 当 $\boldsymbol{\Sigma}=\boldsymbol{I}_p$ 时，$\boldsymbol{X}$ 的密度为 $(2\pi)^{-np/2}\exp(-\frac{1}{2}\operatorname{tr}(\boldsymbol{X}^\top\boldsymbol{X}))$。

**步骤 2：Cholesky 分解与 Jacobian。** 令 $\boldsymbol{W}=\boldsymbol{T}^\top\boldsymbol{T}$，则 $\boldsymbol{X}=\boldsymbol{U}\boldsymbol{T}$（$\boldsymbol{U}\in V_{n,p}$），变换 $\boldsymbol{X}\to(\boldsymbol{U},\boldsymbol{T})$ 的 Jacobian 为 $\prod_{i=1}^p t_{ii}^{n-i}$。

**步骤 3：Stiefel 流形积分。** Stiefel 流形体积 $\operatorname{Vol}(V_{n,p})=\frac{2^p\pi^{np/2}}{\Gamma_p(n/2)}$，其中 $\Gamma_p(a)=\pi^{p(p-1)/4}\prod_{i=1}^p\Gamma(a-(i-1)/2)$。在流形上积分并替换 $w_{ii}=t_{ii}$ 得：
$$
f(\boldsymbol{W})=\int_{V_{n,p}}(2\pi)^{-np/2}\exp(-\frac{1}{2}\operatorname{tr}(\boldsymbol{W}))\prod_{i=1}^p w_{ii}^{(n-i)/2}\,d\boldsymbol{U}
=\frac{|\boldsymbol{W}|^{(n-p-1)/2}\exp(-\frac{1}{2}\operatorname{tr}(\boldsymbol{W}))}{2^{np/2}\pi^{p(p-1)/4}\prod_{i=1}^p\Gamma(\frac{n+1-i}{2})}.
$$

**步骤 4：一般情形。** 令 $\boldsymbol{Y}_i=\boldsymbol{\Sigma}^{-1/2}\boldsymbol{X}_i\sim N_p(\boldsymbol{0},\boldsymbol{I}_p)$，则 $\boldsymbol{W}_Y=\sum\boldsymbol{Y}_i\boldsymbol{Y}_i^\top\sim W_p(n,\boldsymbol{I}_p)$，且 $\boldsymbol{W}=\boldsymbol{\Sigma}^{1/2}\boldsymbol{W}_Y\boldsymbol{\Sigma}^{1/2}$。由 Jacobian $|\boldsymbol{\Sigma}|^{n/2}$ 即得一般密度公式。$\square$

**性质的验证：**
- 期望：$\mathbb{E}[\boldsymbol{W}]=\sum_i\mathbb{E}[\boldsymbol{X}_i\boldsymbol{X}_i^\top]=n\boldsymbol{\Sigma}$。
- 可加性：若 $\boldsymbol{X}_1,\dots,\boldsymbol{X}_{n_1+n_2}\sim N_p(\boldsymbol{0},\boldsymbol{\Sigma})$ 独立，则 $\boldsymbol{W}_1+\boldsymbol{W}_2=\sum_{i=1}^{n_1+n_2}\boldsymbol{X}_i\boldsymbol{X}_i^\top\sim W_p(n_1+n_2,\boldsymbol{\Sigma})$。$\square$

## 五、应用与意义

Wishart 分布是样本协方差矩阵（乘自由度后）的精确分布，在多元统计推断中无处不在：Hotelling $T^2$ 统计量的分布、多元回归的误差协方差估计、似然比检验的分布都依赖它。可加性使高自由度 Wishart 可分解为低自由度之和，帮助建立卡方近似的极限理论。它与卡方、Beta 型（Wilks Lambda）及其乘法相关分布共同构成多元假设检验的分布基础。