# Gelfond-Schneider 定理

> **一句话大白话**：如果把一个"不是 0 也不是 1"的代数数取其"非有理次"的幂，得到的一定是超越数。"挺好的数" + "无理指数" = "陌生的超越数"。
>
> **小例子**：$2^{\sqrt2}$ 是超越数（Hilbert 第七问题）；$e^\pi$ 是超越数，因 $e^\pi=(-1)^{-i}$（$\alpha=-1,\beta=-i$ 均为代数数）。$2^i,\ \pi^{\sqrt2}$ 等也都超越。而 $2^{\frac12}=\sqrt2$（$\beta$ 为有理）则仍代数。

## 一、定理介绍

> **前置依赖**：代数数与超越数的定义、Siegel 引理、最大模原理、代数数的范数与高度估计。

Gelfond-Schneider 定理由 Gelfond 与 Schneider 于 1934 年独立证明，解决了 Hilbert 第七问题。它断言：若 $\alpha,\beta$ 为代数数，$\alpha\neq0,1$，$\beta$ 非有理数，则 $\alpha^\beta$ 超越。这是时代数逼近理论最重要的成果之一。

## 二、原理思路

是"有效超越性"的现代技术典例。设 $\gamma=\alpha^\beta$ 为代数数。构造含许多参数的指数多项式（辅助函数）$F(z)=\sum c_{m,n}\alpha^{mz}\gamma^{nz}$，用 Siegel 引理选系数使其在 $z=1,\dots,L$ 处有 $L$ 阶零点且系数有界。利用复分析最大模原理得 $F$ 在这些零点附近小；而另一端 $F(t)$ 又是代数数（指数项线性无关），由代数数论范数估计得其非零时不得太小。上界与下界经参数选取矛盾，迫使 $F\equiv0$，再与系数非平凡矛盾。

## 三、定理的严格表述

设 $\alpha$、$\beta$ 为代数数，$\alpha\neq0,1$，且 $\beta$ 不是有理数（$\beta\notin\mathbb{Q}$）。则 $\alpha^\beta$ 是超越数。

**推论：**
- $2^{\sqrt2}$ 超越（Hilbert 第七问题）；
- $e^\pi$ 超越（$e^\pi=(-1)^{-i}$）；
- $\log_\alpha\beta$（代数数 $\alpha\neq0,1$、$\beta\neq0,1$）若非有理代数数则超越。

## 四、证明过程

**证明（概要）：**

**步骤 1：反证假设。** 假设 $\gamma=\alpha^\beta$ 为代数数，于是 $\alpha,\beta,\gamma$ 代数，$\alpha\neq0,1$，$\beta\notin\mathbb{Q}$。$\blacksquare$

**步骤 2：辅助函数。** 令 $K=\mathbb{Q}(\alpha,\beta,\gamma)$，$[K:\mathbb{Q}]=d$。选整数 $L,H$，考虑
$$F(z)=\sum_{m=0}^{L-1}\sum_{n=0}^{L-1}c_{m,n}\alpha^{mz}\gamma^{nz},$$
系数 $c_{m,n}$ 待定。$\blacksquare$

**步骤 3：Siegel 引理选系数。** 存在非零整数数组使 $F^{(k)}(\ell)=0,\ 0\le k\le L-1,\ 1\le\ell\le L$，且 $\max|c_{m,n}|\le C_1L^{L^2/2}$。即 $F$ 在 $z=1,\dots,L$ 各有 $L$ 阶零点。$\blacksquare$

**步骤 4：最大模估值。** 由复分析中最大模原理，对 $t=L+1,\dots,2L$，
$$|F(t)|\le C_2L^{-L}\max_{|z|\le2L}|F(z)|.$$

**步骤 5：上界与下界。** 上界：结合导数约束可取 $|F(t)|\le C_3L^{-L}H^{L^2}C^L$。下界：$F(t)=\sum c_{m,n}\alpha^{mt}\gamma^{nt}$ 为代数数（因 $\beta\notin\mathbb{Q}$ 使指数项 $K$-线性无关），由范数/共轭估计，若 $F(t)\neq0$ 则 $|F(t)|\ge C_4^{-L^2}H^{-L^2}$。$\blacksquare$

**步骤 6：参数矛盾。** 取 $L$ 充分大、$H\approx L^L$，使步骤 5 上界 $<$ 下界，于是迫使 $F(t)=0$ 对所有 $t=1,\dots,2L$ 成立。$\blacksquare$

**步骤 7：结论矛盾。** 若 $F(t)=0$ 对 $2L$ 个不同点成立，则非零指数多项式 $F$ 有至少 $2L$ 个零点。但 $F$ 有 $L^2$ 项，其零点多到超过（$2L>L^2-1$ 对充分大 $L$）$F$ 多项式零点数的界，矛盾，故 $F\equiv0$、所有系数 $c_{m,n}=0$，与系数非平凡性矛盾。因此 $\gamma$ 不能是代数数，$\alpha^\beta$ 超越。$\square$

## 五、应用与意义

Gelfond-Schneider 定理是大放异彩的超越数定理，彻底回答 Hilbert 第七问题，确立自身与 Schneider 的独立证明。它把广泛代数指数的超越性归为一枚约束。应用于：特定组合幂（$2^{\sqrt2},\ e^\pi$）的代数无关性判断、Lambert 型问题、准算法与丢番图逼近的现代推进。它与 Baker 线性型理论交汇，形成高效性的重要分支（有效超越性与 effective estimates）。