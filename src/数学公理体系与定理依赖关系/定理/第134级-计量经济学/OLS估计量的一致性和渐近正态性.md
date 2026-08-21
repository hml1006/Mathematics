# OLS估计量的一致性和渐近正态性

> **一句话大白话**：只要样本足够大、误差是白噪声式的，普通最小二乘（OLS）就会"越估越准"（收敛到真值），而且估计误差近似服从正态分布，好让我们算置信区间和假设检验。
>
> **小例子**：回归 $y_i=x_i'\beta_0+\varepsilon_i$ 中，样本量 $n$ 越大，$\hat\beta_{\text{OLS}}$ 越贴近真实 $\beta_0$，且 $\sqrt{n}(\hat\beta_{\text{OLS}}-\beta_0)$ 趋近 $N(0,\sigma^2Q^{-1})$。

## 一、定理介绍

> **前置依赖**：大数定律、鞅差中心极限定理、Lindeberg条件、Slutsky定理、Hölder不等式

OLS 估计量的一致性与渐近正态性是经典线性回归的统计基石。在误差为鞅差序列、回归元二阶矩收敛于正定矩阵等正则条件下，OLS 估计 $\hat\beta_{\text{OLS}}$ 一致收敛于真值 $\beta_0$，且满足
$$
\sqrt{n}(\hat\beta_{\text{OLS}}-\beta_0)\xrightarrow{d} N(0,\sigma^2Q^{-1}),\qquad Q=\text{plim}\,\frac1n\sum_i x_ix_i'.
$$

## 二、原理思路

一致性：把估计误差写为 $S_n^{-1}\sum_i x_i\varepsilon_i$，其中 $S_n=\sum_ix_ix_i'$；由鞅差性质 $\mathbb{E}[x_i\varepsilon_i]=0$，大数定律使样本矩收敛、误差和趋于零，故误差趋于零。渐近正态性：把 $\frac1{\sqrt n}\sum_ix_i\varepsilon_i$ 视为鞅差阵列，用鞅差中心极限定理（条件方差收敛 + Lindeberg 条件）得 $N(0,\sigma^2Q)$，再经 Slutsky 定理得 $N(0,\sigma^2Q^{-1})$。

## 三、定理的严格表述

设 $y_i=x_i'\beta_0+\varepsilon_i$，$\{\varepsilon_i\}$ 关于滤子 $\{\mathcal{F}_{i-1}\}$ 为鞅差序列：$\mathbb{E}[\varepsilon_i|\mathcal{F}_{i-1}]=0$，$\mathbb{E}[\varepsilon_i^2|\mathcal{F}_{i-1}]=\sigma^2$。假设 $n^{-1}S_n\xrightarrow{p}Q$（正定），且 $\sup_i\mathbb{E}[|\varepsilon_i|^{2+\delta}|\mathcal{F}_{i-1}]<\infty$。则

1. $\hat\beta_{\text{OLS}}\xrightarrow{p}\beta_0$；
2. $\sqrt{n}(\hat\beta_{\text{OLS}}-\beta_0)\xrightarrow{d}N(0,\sigma^2Q^{-1})$。

## 四、证明过程

**步骤1：OLS 表达式。** $\hat\beta_{\text{OLS}}=S_n^{-1}\sum_ix_iy_i=\beta_0+S_n^{-1}\sum_ix_i\varepsilon_i$。

**步骤2：一致性。** 由 $\mathbb{E}[x_i\varepsilon_i]=0$ 与方差 $O(1/n)$，
$$
\frac1n\sum_ix_i\varepsilon_i\xrightarrow{p}0,\quad
\hat\beta_{\text{OLS}}-\beta_0=(S_n/n)^{-1}\cdot\tfrac1n\sum_ix_i\varepsilon_i\xrightarrow{p}Q^{-1}\cdot0=0.
$$

**步骤3：鞅差阵列。** 令 $\xi_{ni}=\frac1{\sqrt n}x_i\varepsilon_i$，则 $\mathbb{E}[\xi_{ni}|\mathcal{F}_{i-1}]=0$，构成鞅差阵列。

**步骤4：验证 CLT 条件。** 条件方差
$$
\sum_i\mathbb{E}[\xi_{ni}\xi_{ni}'|\mathcal{F}_{i-1}]=\tfrac1n\sum_ix_ix_i'\mathbb{E}[\varepsilon_i^2|\mathcal{F}_{i-1}]\xrightarrow{p}\sigma^2Q;
$$
Lindeberg 条件由 $\sup_i\mathbb{E}[|\varepsilon_i|^{2+\delta}]<\infty$ 与 Hölder 不等式保证。

**步骤5：应用鞅差 CLT。** $\frac1{\sqrt n}\sum_ix_i\varepsilon_i\xrightarrow{d}N(0,\sigma^2Q)$。

**步骤6：Slutsky 定理。** 由 $S_n/n\xrightarrow{p}Q$，
$$
\sqrt{n}(\hat\beta_{\text{OLS}}-\beta_0)\xrightarrow{d}Q^{-1}N(0,\sigma^2Q)=N(0,\sigma^2Q^{-1}).
$$

**结论（$\square$）**：OLS 一致且渐近正态。

## 五、应用与意义

这是经典计量经济推断的基石，为回归系数的置信区间、t/F 检验与诊断提供渐近理论保证。它确立"OLS 在正确设定下是最优线性无偏且渐近正态"的基准，横跨横截面、面板与时间序列回归的推断实践。