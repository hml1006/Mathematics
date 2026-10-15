# Radon定理

> **一句话大白话**：$\mathbb{R}^d$ 里任意 $d+2$ 个点都能劈成两拨，使得两拨各自的凸(包)凑到同一个点——"$d+2$ 个点必有交叉劈分"。
>
> **小例子**：平面（$d=2$）上任意 $4$ 个点总可以分成两对（或一组），使两条线段（凸包）相交或共点——如凸四边形对角线相交，或"两个三角形共顶点"。

## 一、定理介绍

> **前置依赖**：凸包与凸组合的定义、向量的线性相关、提升维数的嵌入技巧、凸组合系数非负和为 1 的性质

Radon 定理断言 $\mathbb{R}^d$ 中 $d+2$ 个点必有 Radon 划分：分成两个不相交子集使凸包相交。它是 Radon-Carathéodory-Helly 理论与 Helly 定理证明的关键引理。

## 二、原理思路

把点 $x_i$ 提升为 $d+1$ 维向量 $(x_i,1)$：$d+2$ 个 $d+1$ 维向量必线性相关，存在不全为零的 $\lambda_i$ 使 $\sum\lambda_ix_i=0$ 且 $\sum\lambda_i=0$。按 $\lambda_i$ 符号分为 $P,Q$，令 $s=\sum_{\lambda_i>0}\lambda_i=-\sum_{\lambda_i<0}\lambda_i>0$。由 $\sum\lambda_ix_i=0$ 得 $\sum_{\lambda_i>0}\lambda_ix_i=-\sum_{\lambda_i<0}\lambda_ix_i$，同除以 $s$ 得公共点 $p=\sum_{\lambda_i>0}\frac{\lambda_i}{s}x_i=\sum_{\lambda_i<0}\frac{-\lambda_i}{s}x_i$。

## 三、定理的严格表述

（Radon 定理）$\mathbb{R}^d$ 中任意 $d+2$ 个点可以划分为两个不相交子集 $P,Q$，使得 $\operatorname{conv}(P)\cap\operatorname{conv}(Q)\ne\varnothing$。

## 四、证明过程

**证：**

1. **线性相关。** 记 $d+2$ 个点为 $x_1,\dots,x_{d+2}$。向量 $(x_i,1)\in\mathbb{R}^{d+1}$ 共 $d+2>d+1$ 个，线性相关：存在不全为零的 $\lambda_i$ 使 $\sum\lambda_ix_i=0$、$\sum\lambda_i=0$。

2. **划分。** $P=\{x_i:\lambda_i>0\}$，$Q=\{x_i:\lambda_i<0\}$，$s=\sum_{\lambda_i>0}\lambda_i=-\sum_{\lambda_i<0}\lambda_i>0$。

3. **公共点。** 由 $\sum\lambda_ix_i=0$，$\sum_{\lambda_i>0}\lambda_ix_i=-\sum_{\lambda_i<0}\lambda_ix_i$；除以 $s$ 得
   $$
   p=\sum_{\lambda_i>0}\frac{\lambda_i}{s}x_i=\sum_{\lambda_i<0}\frac{-\lambda_i}{s}x_i,
   $$
   而 $p\in\operatorname{conv}(P)\cap\operatorname{conv}(Q)$（凸组合系数非负和为 $1$）。$\square$

## 五、应用与意义

Radon 定理是 Helly 定理证明的枢纽，并广泛用于剖分、碰撞检测与计算几何中的区间查排（其平面形式"凸四边形的两条对角线相交"）。它还是 Tverberg 定理的 $r=2$ 退化情形，构成离散几何"局部一致 → 全局相交"推理链的一环。

## 课堂问答

**老师**：$\mathbb R^d$ 中任意 $d+2$ 个点为什么一定能分成两拨使凸包相交？

**学生**：把点齐次化为 $\mathbb R^{d+1}$ 中的 $(x_i,1)$，$d+2>d+1$ 个必线性相关：存在不全为零的 $\lambda_i$ 使 $\sum\lambda_ix_i=0$ 且 $\sum\lambda_i=0$。按 $\lambda_i$ 的正负分成 $P,Q$，令 $s=\sum_{\lambda_i>0}\lambda_i=-\sum_{\lambda_i<0}\lambda_i>0$，则 $p=\sum_{P}\frac{\lambda_i}{s}x_i=\sum_{Q}\frac{-\lambda_i}{s}x_i\in\operatorname{conv}(P)\cap\operatorname{conv}(Q)$。

**老师（追问）**：为什么 $\mathbb R^{d+1}$ 里的相关性能保证 $\sum\lambda_i=0$？

**学生**：齐次化把每个点提升为 $(x_i,1)$，相关组合 $\sum\lambda_i(x_i,1)=0$ 的最后一维恰是 $\sum\lambda_i=0$，前 $d$ 维是 $\sum\lambda_ix_i=0$。"加一维"的技巧让仿射组合系数和为零自动满足。

**老师（拓展）**：它与 Tverberg、Borsuk–Ulam 有何联系？

**学生**：Radon 是 Tverberg 在 $r=2$ 的退化情形（$N=(d+1)(2-1)+1=d+2$）；$r=2$ 的 Tverberg 又等价于 $\mathbb Z_2$-等变的 Borsuk–Ulam（$S^{d+1}\to S^{d}$ 无等变映射），这正是 Sarkaria 框架的最小情形。
