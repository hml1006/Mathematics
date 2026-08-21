# Fatou 引理

> **一句话大白话**：对于非负波形的一族函数，先求"最小可能极限"再积分，不会比先积分再求下极限更绿——极限的积分不超过积分取下限。
>
> **小例子**：噪音函数越来越小的情形下，Fatou 引理给出了"最小值与积分的次序"之间的单向不等式。

## 一、定理介绍

> **前置依赖**：Lebesgue 积分与可测函数、下极限、单调收敛定理、逐点收敛与单调序列

设 $\{f_n\}$ 为非负可测函数列，则

$$
\int \liminf_{n\to\infty}f_n\,d\mu \le \liminf_{n\to\infty}\int f_n\,d\mu.
$$

## 二、原理思路

构造后阶下确界 $g_n=\inf_{k\ge n}f_k$，它单调递增地收敛到 $\liminf f_n$。由 $g_n\le f_k$（$k\ge n$）可得 $\int g_n\le\inf_{k\ge n}\int f_k$，再对 $g_n$ 用单调收敛定理取极限即得结论。

## 三、定理的严格表述

设 $f_n\ge0$ 可测，则

$$
\int\liminf_{n\to\infty}f_n\,d\mu \le \liminf_{n\to\infty}\int f_n\,d\mu.
$$

## 四、证明过程

1. **单调序列**：$g_n=\inf_{k\ge n}f_k$ 非降，$g_n\uparrow\liminf f_n$。
2. **控制**：$g_n\le f_k$（$k\ge n$），故 $\int g_n\le\inf_{k\ge n}\int f_k$。
3. **取极限**：$\int\liminf f_n=\lim\int g_n\le\liminf\int f_k$。

## 五、应用与意义

Fatou 引理是积分理论与概率论中的基本不等式，为控制收敛定理、鞅收敛、逐项积分期望交换提供了工具。它的实质是"极限的最小值不被积分放大"，在分析中出现"非负性"假设以排除负值导致的不等式反转，是 Lebesgue 积分体系与单调收敛定理并列的三大极限性质之一。