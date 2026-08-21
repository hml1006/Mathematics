# IFS吸引子的维数

> **一句话大白话**：当每个压缩映射是相似映射且满足开集条件（OSC）时，吸引子的维数不靠"量"而靠"解方程"：只要解出 $\sum_i r_i^s=1$ 里的 $s$，它就是 Hausdorff 维数。
>
> **小例子**：三个压缩比 $1/2$ 的相似映射生成 Sierpinski 三角形，方程 $3\cdot(1/2)^s=1$ 解得 $s=\log3/\log2$。

## 一、定理介绍

> **前置依赖**：IFS 吸引子的存在唯一性（Hutchinson 定理）、相似映射与压缩比、开集条件（OSC）、质量分布原理、Hausdorff 测度与维数定义

本定理（IFS 维数定理）给出相似 IFS 吸引子维数的精确公式：维数 $s$ 是方程 $\sum_{i=1}^m r_i^s=1$ 的唯一解。它把"分形的维数"从艰深的测度估计，化约为一个完全初等的代数方程。

## 二、原理思路

用"规范化测度"做上下界。上界：用第 $k$ 级的 $\prod_i r_i^{k}$-覆盖估计 $\mathcal{H}^s$ 趋于零。下界：构造满足 $\mu(B(x,r))\lesssim r^s$ 的均匀概率测度，由质量分布原理推出 $\mathcal{H}^s(A)>0$。开集条件（OSC）保证各压缩副本"不重叠得太狠"，使上下界恰好对上。

## 三、定理的严格表述

（IFS 维数定理）设 $\{f_1,\dots,f_m\}$ 是 $\mathbb{R}^n$ 上的 IFS，每个 $f_i$ 是压缩比为 $r_i$ 的相似压缩映射，且满足开集条件：存在非空有界开集 $V\subset\mathbb{R}^n$ 使 $\bigcup_i f_i(V)\subset V$ 且 $f_i(V)\cap f_j(V)=\varnothing\;(i\ne j)$。则吸引子 $A$ 的 Hausdorff 维数等于方程
$$
\sum_{i=1}^m r_i^s=1
$$
的唯一解。

## 四、证明过程

**证（思路与关键步骤）：**

**上界估计：** 吸引子 $A$ 由 $m^k$ 个压缩比为 $r_{i_1}\cdots r_{i_k}$ 的小副本覆盖。对任意 $s>0$，第 $k$ 级覆盖给出
$$
\mathcal{H}^s(A)\le\Bigl(\sum_{i=1}^m r_i^s\Bigr)^k
$$
若 $s$ 使 $\sum_i r_i^s<1$，令 $k\to\infty$ 得 $\mathcal{H}^s(A)=0$，故 $\dim_H A\le s_0$，其中 $s_0$ 是 $\sum_i r_i^s=1$ 的解。

**下界估计：** 在 $A$ 上构造自然概率测度 $\mu$，使每个第 $k$ 级基本副本的测度为 $\prod_j r_{i_j}^s$。由开集条件，这些小副本不严重重叠，可证存在 $c>0$ 使
$$
\mu(B(x,r))\le c\,r^{s_0},\quad\forall x\in A,\;0<r<1
$$
由质量分布原理：若存在概率测度 $\mu$ 支撑在 $A$ 上且 $\mu(B(x,r))\le c\,r^s$，则 $\mathcal{H}^s(A)\ge1/c>0$。故 $\mathcal{H}^{s_0}(A)>0$，从而 $\dim_H A\ge s_0$。

**综合：** 上下界合并得 $\dim_H A=s_0$，其中 $s_0$ 是 $\sum_i r_i^s=1$ 的唯一解。$\square$

## 五、应用与意义

本定理把维数计算变成"套公式"，是判定分形维数的最高效路径。经典分形（Cantor 集 $\log2/\log3$、Sierpinski 三角形 $\log3/\log2$、Koch 曲线 $\log4/\log3$）都由此式一望而见。开集条件的引进更是后续研究自相似集、Vicsek 分形等核心理论的出发点。