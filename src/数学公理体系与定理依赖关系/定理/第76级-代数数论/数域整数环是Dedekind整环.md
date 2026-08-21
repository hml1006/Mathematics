# 数域整数环是 Dedekind 整环

> **一句话大白话**：数域 $K$ 的代数整数环 $\mathcal{O}_K$（所有满足整系数多项式且首项为 1 的元素）一定是一座"构造极佳"的环：Noether、整闭、维数为 1 这三条同时成立，即所谓 Dedekind 整环。
>
> **小例子**：$\mathbb{Q}(\sqrt{-5})$ 的整数环 $\mathbb{Z}[\sqrt{-5}]$ 不是唯一析因整环（$6$ 有两种分解），但它仍是 Dedekind 整环——元素的唯一分解失去了，理想的唯一分解却仍然成立。这正是代数数论的起点。

## 一、定理介绍

Dedekind 整环是代数数论的基本对象。该定理断言：任何数域的代数整数环 $\mathcal{O}_K$ 都是 Dedekind 整环，即同时满足三条刻画：(1) Noether；(2) 整闭（取分式域中最大程度可满足的次数整元都在环中）；(3) 每个非零素理想都是极大理想（Krull 维数为 1）。这条定理保证了 $\mathcal{O}_K$ 中"理想唯一分解"等强大性质的成立。

## 二、原理思路

三条性质的证明各自动用不同的工具：
- **Noether 性**本质源于 $\mathcal{O}_K$ 是有限生成 $\mathbb{Z}$-模（秩 $\le[K:\mathbb{Q}]$），而 $\mathbb{Z}$ 自身是 Noether 环；
- **整闭性**来自分解/共轭技巧：整元在嵌入下的共轭仍是整元，其基本对称函数（迹、范数）是整数，从而整元满足的首一多项式可以约化；
- **维数为 1** 依靠范数取整：对每个非零素理想 $\mathfrak p$，$\mathfrak p\cap\mathbb{Z}$ 是非零素理想 $p\mathbb{Z}$，于是 $\mathcal{O}_K/\mathfrak p$ 是有限域，从而 $\mathfrak p$ 极大。

## 三、定理的严格表述

设 $K$ 为数域（$\mathbb{Q}$ 的有限扩张），$\mathcal{O}_K$ 为 $K$ 的代数整数环。则 $\mathcal{O}_K$ 是 Dedekind 整环：

1. $\mathcal{O}_K$ 是 Noether 环（每个理想有限生成）。
2. $\mathcal{O}_K$ 在 $K$ 中整闭（$\mathcal{O}_K$ 中的元素在 $K$ 内关于它自身的整元就是 $\mathcal{O}_K$ 自身）。
3. 每个非零素理想 $\mathfrak p\subset\mathcal{O}_K$ 是极大理想，即 $\dim\mathcal{O}_K=1$。

## 四、证明过程

**证明：**

**性质 1（Noether 性）。** $\mathcal{O}_K$ 是有限生成 $\mathbb{Z}$-模（取 $K$ 的一组基 $\alpha_1,\dots,\alpha_n$，则 $\sum_i\mathbb{Z}\alpha_i\subseteq\mathcal{O}_K$，且 $\mathcal{O}_K$ 作为子模有限生成）。因 $\mathbb{Z}$ 是 Noether 环，有限生成模的子模有限生成，故 $\mathcal{O}_K$ 的每个理想（即子模）有限生成，$\mathcal{O}_K$ 是 Noether 环。$\blacksquare$

**性质 2（整闭性）。** 设 $\alpha\in K$ 在 $\mathcal{O}_K$ 上整，即存在首一多项式 $f(x)=x^n+c_{n-1}x^{n-1}+\cdots+c_0$（$c_i\in\mathcal{O}_K$）使 $f(\alpha)=0$。取 $\alpha$ 在 $K$ 上的全体共轭 $\alpha^{(1)},\dots,\alpha^{(n)}$ 及 $c_i$ 的共轭，作对称函数（幂和或基本对称多项式），可得 $\alpha$ 是 $\mathbb{Z}$ 上整：存在首一多项式 $g(x)\in\mathbb{Z}[x]$ 使 $g(\alpha)=0$（此为"若某个代数整数环上整，则在 $\mathbb{Z}$ 上整"的著名论断）。故 $\alpha\in\mathcal{O}_K$。$\blacksquare$

**性质 3（维数为 1）。** 设 $\mathfrak p\subset\mathcal{O}_K$ 为非零素理想，取非零 $a\in\mathfrak p$。范数 $N(a)=\prod_{i=1}^n\sigma_i(a)\in\mathbb{Z}$（因 $a$ 整且非零，$N(a)\neq0$）。因 $\sigma_i(a)$ 皆为 $\mathfrak p$ 的元素嵌入的共轭（理想共轭），有 $N(a)\in\mathfrak p\cap\mathbb{Z}$，于是 $\mathfrak p\cap\mathbb{Z}$ 是非零素理想 $p\mathbb{Z}$。故 $\mathcal{O}_K/\mathfrak p$ 是有限生成 $\mathbb{Z}/p\mathbb{Z}$-模（因 $\mathcal{O}_K$ 有限生成 $\mathbb{Z}$-模），从而是有限环、且为整环（$\mathfrak p$ 素），故为有限整环，即域。所以 $\mathfrak p$ 是极大理想。$\blacksquare$

由性质 1–3，$\mathcal{O}_K$ 是 Dedekind 整环。$\square$

## 五、应用与意义

该定理是代数数论一切理想论的基础。它直接引出两个核心推论：任意非零真理想唯一分解为素理想的乘积，以及理想类群 $Cl(K)$ 是有限阿贝尔群（类数有限）。Dedekind 整环的三条公理也构成抽象代数中可一般处理的理想类结构，被推广到 Dedekind 概形、算术曲线与算术几何，是现代算术代数几何的根基。