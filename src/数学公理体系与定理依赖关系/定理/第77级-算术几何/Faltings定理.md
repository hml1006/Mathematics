# Faltings 定理

> **一句话大白话**：亏格 $\ge2$ 的光滑代数曲线在数域上的有理点只有**有限多个**。曲线越"复杂"（亏格越高），有理点反而越稀少——高的亏格会"压抑"有理点的繁殖。
>
> **小例子**：Fermat 曲线 $x^n+y^n=1$（$n\ge3$）的亏格 $g=\frac{(n-1)(n-2)}2\ge1$；当 $n\ge4$ 时 $g\ge3>1$，故有理点有限。事实上 $n\ge3$ 时唯一 "有理点" 是平凡解，这正是 Fermat 大定理所断言。

## 一、定理介绍

Faltings 定理（1983）由 Faltings 证明原 Mordell 猜想：设 $C$ 是数域 $K$ 上亏格 $g\ge2$ 的不可约光滑代数曲线，则 $C(K)$ 是有限集。这是算术几何跨时代的成就，Faltings 因之获 1986 Fields 奖。它一举解决了 Fermat、Mordell 等的核心计数猜想。

## 二、原理思路

思路是"用小高度定位"：把曲线 $C$ 嵌入其 Jacobi 簇 $J(C)$（$g$ 维 Abel 簇）。Mordell-Weil 定理保证 $J(C)(K)$ 有限生成。关键是证明 $C(K)$ 的点在高度上有界——即不能用无穷多个"越来越高"的点，于是只有有限个。为达此目的引入 Faltings 高度（模高）与 Tate 猜想（等源分类）。

## 三、定理的严格表述

设 $K$ 为数域，$C/K$ 为亏格 $g\ge2$ 的光滑不可约代数曲线。则有理点集 $C(K)$ 是有限集。

## 四、证明过程

**证明思路（Faltings 框架）：**

**步骤 1：Cartesian 嵌入。** 选基点将 $C$ 嵌入其 Jacobi 簇 $J(C)$（$g$ 维 Abel 簇）。由 Mordell-Weil 定理，$J(C)(K)$ 是有限生成。——目标是证明 $C(K)$ 在 $J(C)(K)$ 内高度有界。$\blacksquare$

**步骤 2：Faltings 高度。** 对 Abel 簇 $A/K$ 定义 Faltings 高度 $h_F(A)$（模空间上的高度）。Faltings 证明了：固定维数与极化的 Abel 簇，$h_F(A)$ 有**下界**；且 $A\subseteq J(C)$ 时，$h_F(A)$ 与 $C(K)$ 点 $\times$ 的 Néron-Tate 高度相关（即曲线点的高度被 Abel 子簇高度的下界夹住）。$\blacksquare$

**步骤 3：Tate 猜想/等源分类。** Faltings 证明对 $\ell$：自然映射
$$\operatorname{End}_K(A)\otimes_\mathbb{Z}\mathbb{Q}_\ell\to\operatorname{End}_{G_K}(T_\ell(A))\otimes_{\mathbb{Z}_\ell}\mathbb{Q}_\ell$$
是同构。此给出 Abel 簇的等源分类：给定维数 $g$ 与极化的 Abel 簇，在 $K$ 上的等源类有限。$\blacksquare$

**步骤 4：有限性论证。** 令 $\{C\times P:P\in C(K)\}$（$C(K)$ 中点对应的 Abel 子簇族）高度被一致下界控制（步骤 2 与 3），故只能是有限的等源类；配合等源实例的有限性，推出 $C(K)$ 有限。$\square$

## 五、应用与意义

Faltings 定理是算术几何的分水岭：它终结了 Mordell 猜想，并给出 $\mathbb{Q}$ 上亏格 $\ge2$ 曲线有理点有限的根本约束。它直接证明 Fermat 大定理的非代数部分（亏格分类排除无穷族），为现代"有效 Mordell"（Bombieri-Pila、Chabauty-Kim）提供了出发点，并贯穿 Abel 簇、等源、Tate 模、精细丢番图几何与"子品种定理"（Vojta 视角），是当代算术几何的核心基石。