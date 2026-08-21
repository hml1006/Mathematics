# Skorokhod 积分的 Itô 引理推广

> **一句话大白话**：当积分对象"看未来"（非适应）时，Skorokhod 积分接管了随机微积分的角色，并给 Itô 引理增加一个纠正项：多出来的交叉导数密度修正了非因果性带来的偏差。
>
> **小例子**：某些对冲策略需要提前知道未来价格才能定值所求，这时只能用非适应积分；其复合函数的随机微分会多一项"用 Malliavin 导数描述的修正"。

## 一、定理介绍

Skorokhod 积分 $\delta(u)=\int_0^Tu_t\,\delta W_t$ 是 Malliavin 导数 $D$ 的伴生算子。对 $u\in\operatorname{dom}(\delta)$、$F\in\mathbb{D}^{1,2}$ 且 $Fu\in\operatorname{dom}(\delta)$，有分部积分公式

$$
F\delta(u) = \delta(Fu) + \int_0^T D_tF\cdot u_t\,dt.
$$

进一步，对 Skorokhod 过程 $X_t$，$Y_t=f(t,X_t)$ 有推广的 Itô 引理。

## 二、原理思路

分部积分公式本质上是 $D$ 与 $\delta$ 的对偶恒等式的直接推论：$\mathbb{E}[F\delta(u)]=\mathbb{E}\int_0^T D_tF\cdot u_t dt$。对 $X_t$ 用推广的 Itô 公式时，由于微分的积分是不适应积分，会出现来自 $[D,\delta]$ 交换产生的修正项（含 $D_t\sigma_s$ 与 $D_s(\partial_xf\,\sigma_t)$ 的积分），体现非因果性。

## 三、定理的严格表述

设 $u\in\operatorname{dom}(\delta)$，$F\in\mathbb{D}^{1,2}$ 且 $Fu\in\operatorname{dom}(\delta)$，则

$$
F\delta(u) = \delta(Fu) + \int_0^T D_tF\cdot u_t\,dt.
$$

设 $X_t = X_0 + \int_0^t\mu_s ds + \int_0^t\sigma_s\,\delta W_s$，$f\in C^{1,2}$，则

$$
df(t,X_t) = \Big(\partial_t f + \mu_t\partial_x f + \frac12\sigma_t^2\partial_{xx}f\Big)dt + \partial_xf\,\sigma_t\,\delta W_t + \Big(\int_0^t D_t\sigma_s\,D_s(\partial_xf\,\sigma_t)ds\Big)dt.
$$

## 四、证明过程

1. **对偶关系**：$\mathbb{E}[F\delta(u)]=\mathbb{E}\int_0^T D_tF\cdot u_t dt$。
2. **分部积分**：对 $\delta(Fu)$ 作用对偶公式并整理出 $F\delta(u)$ 与修正项。
3. **Itô 推广**：对 $f(t,X_t)$ 仿照 Itô 引理展开，但非适应的交换项 $\int D_t\cdot D_s(\cdot)ds\,dt$ 需保留。
4. **合并**：把适应部分与非适应部分分别整理成 $dt$ 项与 $\delta W_t$ 项。

## 五、应用与意义

Skorokhod 积分为非适应/前瞻性被积函数（如鞅表示中的奇异分数、扩散密度估计、粒子滤波的干扰项）提供了严格的积分框架，其推广的 Itô 引理使得对这类过程也能做复合计算。它与 Malliavin 计算互为表里，在随机偏微分方程、马尔可夫桥与金融领先对冲中扮演重要角色。