# Helly定理

> **一句话大白话**：一族凸集要么全部有个共同交点，要么有 $d+1$ 个"坏脾气"的设了障碍。在 $\mathbb{R}^d$ 里，只要任意 $d+1$ 个凸集都有公共点，整个族就必有一个公共点。
>
> **小例子**：平面上（$d=2$）一堆凸多边形，只要任意三个都有公共交点，那么所有多边形都交出同一个点——"三人有交 ⇒ 全有交"。

## 一、定理介绍

Helly 定理是离散凸几何的三大根基定理之一：在 $\mathbb{R}^d$ 中，一族凸集的整体相交性由"任意 $d+1$ 个"的局部相交性完全决定。它是覆盖与相交问题的核心工具。

## 二、原理思路

对集合数 $n>d+1$ 归纳。设 $A_i=\bigcap_{j\ne i}C_j\ne\varnothing$ 并选 $a_i\in A_i$，得到 $n$ 个点。由 Radon 定理，$n$ 个点可分成 $P,Q$ 使 $\operatorname{conv}(P)\cap\operatorname{conv}(Q)\ne\varnothing$，取 $x$ 在交中。对任意 $i$，$P\cup Q$ 中除 $a_i$ 外全在 $C_i$ 中且 $a_i$ 归属的那组在其余凸集里，又凸性保证 $\operatorname{conv}(P)\subseteq C_i$ 或 $\operatorname{conv}(Q)\subseteq C_i$，故 $x\in C_i$。

## 三、定理的严格表述

（Helly 定理）设 $\mathcal{F}=\{C_1,\dots,C_n\}$ 是 $\mathbb{R}^d$ 中一族凸集，$n\ge d+1$。若 $\mathcal{F}$ 中任意 $d+1$ 个凸集都有非空交集，则 $\bigcap_{i=1}^n C_i\ne\varnothing$。

## 四、证明过程

**证（归纳）：**

1. **基情况。** $n=d+1$ 时由条件直接成立。

2. **归纳假设。** 设结论对 $n-1$ 个凸集成立。

3. **选点。** 令 $A_i=\bigcap_{j\ne i}C_j$，由归纳假设 $A_i\ne\varnothing$，取 $a_i\in A_i$。

4. **Radon 分离。** 若 $n\ge d+2$，由 Radon 定理，$a_1,\dots,a_n$ 分成 $P,Q$ 使 $x\in\operatorname{conv}(P)\cap\operatorname{conv}(Q)$。

5. **公共点。** 任取 $i$。若 $a_i\in P$，则 $P$ 与 $Q$ 中除 $a_i$ 外的所有点都在 $C_i$（它们属于 $A_i$），且 $C_i$ 凸故 $\operatorname{conv}(Q\cup(P\setminus\{a_i\}))\subseteq C_i$；结合 $x\in\operatorname{conv}(P)$ 或适当选择使 $x\in C_i$。逐一得 $x\in\bigcap_i C_i$。$\square$

## 五、应用与意义

Helly 定理导出覆盖与相交的许多推论：凸体的 Radon/Carathéodory 最小覆盖、穿越（threshold）引理、以及在 $\mathbb{R}^d$ 中判断线性规划可行域的局部准则。它也是"汉斯-海利"类型的局部到全局准则在离散与计算几何（如有限集合的凸组合、共同割线）中的源头。