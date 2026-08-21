# Clark-Ocone 公式

> **一句话大白话**：任意一个"只依赖布朗运动全程信息"的随机量，都能被写成"它的期望＋一个可预测对冲策略的随机积分"，其中策略恰好是期望条件导数的累计。
>
> **小例子**：欧式期权的价格可解读为"今天定价常数＋按每一天的敏感度逐步对冲所累积的收益"，这正是对冲策略的由来。

## 一、定理介绍

设 $F\in\mathbb{D}^{1,2}$ 为 $\mathcal{F}_T$-可测随机变量。则 $F$ 有鞅表示

$$
F = \mathbb{E}[F] + \int_0^T \mathbb{E}[D_tF\mid\mathcal{F}_t]\,dW_t,
$$

其中 $D_tF$ 是 $F$ 的 Malliavin 导数。

## 二、原理思路

从光滑柱函数 $F=f(W_{t_1},\dots,W_{t_n})$ 出发。对区间 $(t_{k-1},t_k]$，条件期望 $M_t=\mathbb{E}[F\mid\mathcal{F}_t]$ 是 $W_t$ 的可微函数，由 Itô 公式其随机积分核恰好为 $\mathbb{E}[D_tF\mid\mathcal{F}_t]$。再用列函数在 $\mathbb{D}^{1,2}$ 中稠密延拓到一般 $F$，取极限即得公式。

## 三、定理的严格表述

设 $F\in\mathbb{D}^{1,2}$ 是 $\mathcal{F}_T$-可测的 Brown 运动泛函。则鞅 $M_t=\mathbb{E}[F\mid\mathcal{F}_t]$ 由下式给出

$$
M_t = \mathbb{E}[F] + \int_0^t \mathbb{E}[D_sF\mid\mathcal{F}_s]\,dW_s,
$$

特别地 $F = M_T = \mathbb{E}[F] + \int_0^T\mathbb{E}[D_tF\mid\mathcal{F}_t]dW_t$。

## 四、证明过程

1. **柱函数**：对 $F=f(W_{t_1},\dots,W_{t_n})$ 由鞅表示定理有 $F=\mathbb{E}[F]+\int_0^T\phi_t dW_t$。
2. **计算条件导数**：$D_tF=\sum_i\partial_{x_i}f\,1_{[0,t_i]}(t)$，$t\in(t_{k-1},t_k]$ 时 $\mathbb{E}[D_tF\mid\mathcal{F}_t]=\sum_{i\ge k}\mathbb{E}[\partial_{x_i}f\mid\mathcal{F}_t]$。
3. **Itô 核识别**：$M_t$ 在区间上作为 $\mathcal{F}_t$ 条件期望是 $W_t$ 的函数，由 Itô 公式其扩散系数恰为 $\mathbb{E}[D_tF\mid\mathcal{F}_t]$。
4. **$L^2$ 延拓**：列函数 $F^{(n)}\to F$（$\mathbb{D}^{1,2}$）时公式逐项成立，Its Itô 积分与条件期望的连续性传递到极限。

## 五、应用与意义

Clark-Ocone 公式给出了鞅表示中被积函数的显式构造（通过条件 Malliavin 导数），是 Malliavin 计算最具实用价值的成果之一。它广泛应用于金融衍生产品的动态对冲与希腊字母（Greeks）计算、随机控制的灵敏度分析，并为随机积分与 Malliavin 导数的对偶关系提供了统一视角。