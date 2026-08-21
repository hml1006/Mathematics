# Carathéodory定理

> **一句话大白话**：点的凸包的每个点，都"撑"在至多 $d+1$ 个原点上：想表示一个凸组合，$d+1$ 个点就够了，再多就是多余。
>
> **小例子**：平面上（$d=2$）某个点 $x$ 在 $\operatorname{conv}(S)$ 里，那么它必在 $S$ 中"某 $\le3$ 个点"的凸组合里——平面三角形已足够撑住任何凸包中的点。

## 一、定理介绍

Carathéodory 定理说明凸包中的点都能用最少的（至多 $d+1$ 个）点线性表示，是 Carathéodory、Radon、Helly "三合一组"定理的支柱，也是"极小的凸内部表示"的结果。

## 二、原理思路

取 $x\in\operatorname{conv}(S)$ 的一个最短凸组合表示 $x=\sum_{i=1}^m\lambda_ix_i$（$\sum\lambda_i=1$，最小 $m$）。若 $m>d+1$，向量系 $x_i-x$（在 $\mathbb{R}^d$ 中，共 $m$ 个，$\ge d+2>d$ 个）必线性相关，存在不全为零的 $\mu_i$ 使 $\sum\mu_i=0$、$\sum\mu_ix_i=0$。取 $t=\min\{\lambda_i/\mu_i:\mu_i>0\}$ 使 $\lambda_i-t\mu_i\ge0$ 且至少一项向零，得到更短表示，与最小性矛盾。

## 三、定理的严格表述

（Carathéodory 定理）设 $S\subseteq\mathbb{R}^d$，$x\in\operatorname{conv}(S)$。则存在 $S$ 中至多 $d+1$ 个点 $x_1,\dots,x_k$（$k\le d+1$），使得 $x\in\operatorname{conv}(\{x_1,\dots,x_k\})$。

## 四、证明过程

**证：**

1. **最短表示。** $x\in\operatorname{conv}(S)$，取表示 $x=\sum_{i=1}^m\lambda_ix_i$，$\lambda_i\ge0$，$\sum\lambda_i=1$，且 $m$ 最小。若 $m\le d+1$ 已完成。

2. **线性相关。** 设 $m>d+1$。向量 $x_i-x\in\mathbb{R}^d$ 共 $m>d$ 个，故线性相关：存在不全为零的 $\mu_i$ 使 $\sum\mu_i=0$、$\sum\mu_ix_i=0$。

3. **消去一项。** 对 $t\ge0$，系数 $\lambda_i-t\mu_i$ 之和仍为 $1$ 且$\sum(\lambda_i-t\mu_i)x_i=x$。取 $t=\min\{\lambda_i/\mu_i:\mu_i>0\}>0$，则所有系数非负且至少有一个向零（消去该项），得 $m-1$ 项表示，矛盾。

4. **结论。** 故 $m\le d+1$。$\square$

## 五、应用与意义

Carathéodory 定理是"凸包的最小生成"标准结论，应用于非线性规划（最优点在凸包的极小面）、线性规划的基可行解、以及图论中树与匹配的整数多项式表示。它与 Radon、Helly 一起构成离散凸几何的核心理论框架。