# Radon定理

> **一句话大白话**：$\mathbb{R}^d$ 里任意 $d+2$ 个点都能劈成两拨，使得两拨各自的凸(包)凑到同一个点——"$d+2$ 个点必有交叉劈分"。
>
> **小例子**：平面（$d=2$）上任意 $4$ 个点总可以分成两对（或一组），使两条线段（凸包）相交或共点——如凸四边形对角线相交，或"两个三角形共顶点"。

## 一、定理介绍

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