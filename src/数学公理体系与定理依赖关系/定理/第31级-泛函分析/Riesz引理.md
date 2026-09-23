# Riesz 引理

> **一句话大白话**：在一个真闭子空间外面，总能找到一个单位向量，它离这个子空间的"距离"几乎等于 $1$——无穷维空间里"正交方向"虽可能不存在，但"近似正交方向"永远存在。
>
> **小例子**：在 $\mathbb R^3$ 里取闭子空间（平面）$Y$，取平面外单位法向量 $x$，则 $\operatorname{dist}(x,Y)=1$；Riesz 引理保证一般赋范空间中能取到距离任意接近 $1$ 的方向。

## 介绍

Riesz 引理（Riesz's lemma），又称 Riesz 逼近引理，由 Frigyes Riesz 于 1918 年提出，是赋范线性空间几何的基本工具。它断言：若 $Y$ 是赋范空间 $X$ 的一个真闭子空间，则对每个 $\varepsilon\in(0,1)$ 都存在单位向量 $x\in X$ 使得 $\operatorname{dist}(x,Y)\ge1-\varepsilon$。

这一定理的意义在于，它揭示了无穷维赋范空间与有限维的本质差别：在有限维中，单位球是紧的，且总能找到与子空间正交的单位向量（当空间是内积空间时距离恰为 $1$）；而在一般赋范空间中，"距离等于 $1$"未必达到，但"距离接近 $1$"总可以达到。

Riesz 引理最重要的推论是：无穷维赋范空间的闭单位球不紧（因为可以构造一列单位向量两两距离 $\ge1-\varepsilon$，从而没有收敛子列）。它是紧算子理论、Fredholm 理论、Banach–Alaoglu 定理意义分析的基础。

## 分析

**前置依赖**：赋范线性空间、闭子空间、点到集合的距离、单位球与单位向量、紧性与有限维空间的特征

**定理内容**：设 $(X,\|\cdot\|)$ 是赋范线性空间，$Y\subsetneq X$ 是 $X$ 的真闭子空间。则对任意 $\varepsilon\in(0,1)$，存在 $x\in X$ 满足

$$\|x\|=1,\qquad \operatorname{dist}(x,Y):=\inf_{y\in Y}\|x-y\|\ge1-\varepsilon.$$

**关键要点**：

- 一般只能做到 $1-\varepsilon$，不能取到 $1$；这一现象与空间是否"严格凸"或"希尔伯特"有关；
- $Y$ 必须是闭的，否则 $\operatorname{dist}(x,Y)=0$ 可能对某些 $x\notin Y$ 成立；
- 取极限形式：$\inf\{\operatorname{dist}(x,Y):x\in X,\|x\|=1\}$ 在真闭子空间时为正（对 $\varepsilon$ 任意小时）。

## 思考过程

证明的关键是"沿着到子空间的方向做归一化"。取 $x_0\in X\setminus Y$。因 $Y$ 闭，$d:=\operatorname{dist}(x_0,Y)>0$（若 $d=0$，则有 $y_k\in Y$ 使 $y_k\to x_0$，由闭性 $x_0\in Y$，矛盾）。

接下来选 $y_0\in Y$ 使 $\|x_0-y_0\|$ 略大于 $d$——具体地小于 $d/(1-\varepsilon)$。这总是可能的，因为 $d$ 是下确界。然后令

$$x=\frac{x_0-y_0}{\|x_0-y_0\|}.$$

关键是估计 $\|x-y\|$ 对任意 $y\in Y$。由于 $Y$ 是子空间，$y_0+\|x_0-y_0\|\,y\in Y$，于是 $x_0-(y_0+\|x_0-y_0\|\,y)$ 正是形如 $x_0-y'$（$y'\in Y$）的向量，其范数 $\ge d$。把 $\|x_0-y_0\|$ 提出去就得到对 $\|x-y\|$ 的下界，从而由选取 $y_0$ 的方式得到 $\ge1-\varepsilon$。要点是"用子空间对线性组合封闭"来把任意 $y$ 转成 $x_0$ 到 $Y$ 的距离。

## 证明过程

**步骤 1：$x_0$ 到 $Y$ 的距离为正。** 取 $x_0\in X\setminus Y$，令

$$d=\operatorname{dist}(x_0,Y)=\inf_{y\in Y}\|x_0-y\|.$$

若 $d=0$，则存在 $y_k\in Y$ 使 $\|x_0-y_k\|\to0$，即 $y_k\to x_0$；由 $Y$ 闭得 $x_0\in Y$，与 $x_0\notin Y$ 矛盾。故 $d>0$。

**步骤 2：选取近最优的 $y_0$。** 由下确界的定义，存在 $y_0\in Y$ 使

$$\|x_0-y_0\|<\frac{d}{1-\varepsilon}$$

（因为 $d/(1-\varepsilon)>d$，而 $d$ 是下确界，故在附近必有点）。注意 $\|x_0-y_0\|\ge d>0$，可作归一化。

**步骤 3：归一化得单位向量。** 令

$$x=\frac{x_0-y_0}{\|x_0-y_0\|},\qquad \|x\|=1.$$

**步骤 4：估计到 $Y$ 的距离。** 对任意 $y\in Y$，因 $Y$ 是线性子空间，$y_0+\|x_0-y_0\|\,y\in Y$，故

$$d\le\big\|x_0-\big(y_0+\|x_0-y_0\|\,y\big)\big\|=\|x_0-y_0\|\,\Big\|\frac{x_0-y_0}{\|x_0-y_0\|}-y\Big\|=\|x_0-y_0\|\,\|x-y\|.$$

于是

$$\|x-y\|\ge\frac{d}{\|x_0-y_0\|}>\frac{d}{d/(1-\varepsilon)}=1-\varepsilon.$$

由于 $y\in Y$ 任意，$\operatorname{dist}(x,Y)\ge1-\varepsilon$。$\square$

**推论（无穷维闭单位球不紧）**：设 $X$ 无穷维。取 $x_1$ 为单位向量，令 $Y_1=\operatorname{span}\{x_1\}$（有限维故闭）。由 Riesz 引理取单位向量 $x_2$ 使 $\operatorname{dist}(x_2,Y_1)\ge1/2$，特别地 $\|x_2-x_1\|\ge1/2$。归纳地，令 $Y_k=\operatorname{span}\{x_1,\dots,x_k\}$（闭），取单位向量 $x_{k+1}$ 使 $\operatorname{dist}(x_{k+1},Y_k)\ge1/2$。则 $\{x_k\}$ 中任意两点距离 $\ge1/2$，没有收敛子列，故闭单位球不紧。这说明"有界闭集紧"是有限维空间的特征性质。

## 相关条目

- [Fredholm二择一定理](./Fredholm二择一定理.md)：$T$ 为紧算子时，$\lambda I-T$ 的核为有限维、值域闭等结论依赖本引理。
- [Riesz表示定理](./Riesz表示定理.md)：同以 Riesz 命名，但刻画的是 Hilbert 空间上连续线性泛函的表示。
