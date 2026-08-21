# Itô 引理

> **一句话大白话**：对随机过程求复合函数的微分时，不能像普通微积分那样只取一阶项——因为布朗运动的波动"平方后还有量"，会贡献一个额外二阶项 $dt$。
>
> **小例子**：股价 $S_t$ 用几何布朗运动刻化，其对数价格 $\log S_t$ 的漂移里会出现一个 $-\frac12\sigma^2$ 项，这正是 Itô 引理给出的二阶修正。

## 一、定理介绍

> **前置依赖**：Itô 积分、Brown 运动的二次变差、Taylor 展开、随机微分的形式运算、复合函数的链式法则

设 $X_t$ 为 Itô 过程 $dX_t = \mu_t dt + \sigma_t dW_t$，$f(t,x)\in C^{1,2}$。则 $Y_t = f(t,X_t)$ 仍是 Itô 过程，且

$$
dY_t = \Big(\frac{\partial f}{\partial t} + \mu_t\frac{\partial f}{\partial x} + \frac12\sigma_t^2\frac{\partial^2 f}{\partial x^2}\Big)dt + \sigma_t\frac{\partial f}{\partial x}dW_t.
$$

## 二、原理思路

关键在于布朗运动的二次变差 $(dW_t)^2 = dt$（$L^2$ 意义下）。对 $f$ 作二阶 Taylor 展开并代入 $dX_t$，二阶项 $(dX_t)^2=\sigma_t^2dt+o(dt)$ 的贡献不能忽略（量级仍为 $dt$），而 $(dt)^2$、$dt\,dW_t$ 为高阶无穷小，从而得到带二阶修正的微分公式。

## 三、定理的严格表述

设 $X_t$ 满足 $dX_t=\mu_t dt+\sigma_t dW_t$，$f(t,x)\in C^{1,2}$，则

$$
df(t,X_t) = \Big(\frac{\partial f}{\partial t} + \mu_t\frac{\partial f}{\partial x} + \frac12\sigma_t^2\frac{\partial^2 f}{\partial x^2}\Big)dt + \sigma_t\frac{\partial f}{\partial x}dW_t.
$$

多维情形：设 $dX_t^i=\mu_t^i dt+\sum_{j}\sigma_t^{ij}dW_t^j$，则

$$
df = \Big(\partial_t f + \sum_i\mu_t^i\partial_{x_i}f + \frac12\sum_{i,j}(\boldsymbol{\sigma}_t\boldsymbol{\sigma}_t^\top)_{ij}\partial_{x_ix_j}f\Big)dt + \sum_i\partial_{x_i}f\sum_j\sigma_t^{ij}dW_t^j.
$$

## 四、证明过程

1. **二次变差**：$(dW_t)^2=dt$，$(dt)^2=o(dt)$，$dt\,dW_t=o(dt)$。
2. **Taylor 展开**：对 $f$ 展开到二阶，代入 $dX_t=\mu_tdt+\sigma_tdW_t$。
3. **$(dX_t)^2$**：$(dX_t)^2=\sigma_t^2dt+o(dt)$。
4. **合并**：保留 $dt$ 阶项即得 Itô 公式。
5. **多维推广**：交叉二阶项由 $\boldsymbol{\sigma}\boldsymbol{\sigma}^\top$ 的矩阵内积给出。

## 五、应用与意义

Itô 引理是随机分析与金融数学的基石，用于推导资产价格模型、计算衍生品定价（Black-Scholes 方程）、随机控制（动态规划）与遍历估计。它揭示了随机微积分与经典微积分的本质差异，是所有建立在 Itô 积分之上的理论的核心运算规则。