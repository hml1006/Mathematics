# Malliavin 导数的基本性质（链式法则）

> **一句话大白话**：在不连续逼近的意义下，"对随机性的方向导数"也遵循普通的链式法则——复合函数对扰动的敏感度等于内外导数相乘。
>
> **小例子**：若衍生品价格是股票路径的函数，价格对"布朗扰动"的 Malliavin 导数，可拆成"价格对股票"乘"股票对扰动"两部分。

## 一、定理介绍

> **前置依赖**：Malliavin 导数的定义、光滑柱函数、导数算子的封闭性、稠密逼近与 $L^2$ 收敛、普通微分链式法则

设 $\varphi:\mathbb{R}^n\to\mathbb{R}$ 为 $C^1$ 且 $\partial_x\varphi$ 至少在多项式增长内，$\boldsymbol{F}=(F_1,\dots,F_n)$ 每个 $F_i\in\mathbb{D}^{1,2}$。则 $\varphi(\boldsymbol{F})\in\mathbb{D}^{1,2}$，且 Malliavin 导数满足链式法则：

$$
D_t\varphi(\boldsymbol{F}) = \sum_{i=1}^n\frac{\partial\varphi}{\partial x_i}(\boldsymbol{F})\,D_tF_i.
$$

## 二、原理思路

先对光滑柱函数（依赖有限多个时间点值的函数）直接验证链式法则——这时是普通微分的链式法则结合散射导数对指示函数的作用。再用柱函数在 $\mathbb{D}^{1,2}$ 中的稠密逼近一般 $F_i$，由导数算子 $D$ 的封闭性与适当的增长条件把等式传递到极限，并导出乘积法则。

## 三、定理的严格表述

设 $\varphi\in C^1$，$|\nabla\varphi(x)|\le C(1+\|x\|)$，$F_i\in\mathbb{D}^{1,2}$。则

$$
D_t\varphi(\boldsymbol{F}) = \sum_{i=1}^n\frac{\partial\varphi}{\partial x_i}(\boldsymbol{F})\,D_tF_i.
$$

特别地，乘积法则成立：

$$
D_t(FG) = G\,D_tF + F\,D_tG.
$$

## 四、证明过程

1. **柱函数情形**：$F_i=f_i(W_{s_1},\dots,W_{s_m})$，则 $D_tF_i=\sum_j\partial_{x_j}f_i\,1_{[0,s_j]}(t)$，代回即得链式法则。
2. **逼近**：取柱函数列 $F_i^{(k)}\to F_i$（$L^2$）且 $D_tF_i^{(k)}\to D_tF_i$（$L^2(\Omega\times[0,T])$）。
3. **增长条件**：$|\varphi(F^{(k)})-\varphi(F)|\le C(1+\|\cdot\|)\|F^{(k)}-F\|$ 保证 $L^2$ 收敛。
4. **封闭性**：$D$ 是闭算子，故极限即 $D_t\varphi(F)$。
5. **乘积法则**：取 $\varphi(x,y)=xy$ 即得。

## 五、应用与意义

Malliavin 导数的链式法则与乘积法则是 Malliavin 计算（随机变分法）的运算基石。它们被用于推导积分-分部积分公式、随机积分的对偶恒等式、以及金融中希腊字母（Greeks）的 Malliavin 积分表示，是连接随机分析与光滑性理论、正则性（非退化判别）的重要工具。