# Pólya 计数定理

> **一句话大白话**：在群作用下给 $m$ 种颜色着色，不等价的方案数等于"每个群元不动点数目的平均值"——$N=\frac1{|G|}\sum_{g\in G}m^{\text{cyc}(g)}$。
>
> **小例子**：用 2 种颜色给 6 珠项链着色（旋转视为等价），$N=\frac16(2^6+2^1+2^2+2^3+2^2+2^1)=\frac{84}6=14$ 种不等价方案。

## 一、定理介绍

> **前置依赖**：群作用与轨道、Burnside 引理、置换的轮换分解。

Pólya 计数定理（Pólya 1927）把 Burnside 引理与群作用的轮换指标结合，给出在置换群作用下着色的等价类计数公式。它由 Burnside 引理直接导出，但因"轮换数"提法而显实用，是组合枚举的支柱。

## 二、原理思路

Burnside 引理说轨道数 $|A/G|=\frac1{|G|}\sum_g|A^g|$（不动点数平均）。对着色集 $A=C^X$，$f\in C^X$ 是 $g$-不动点当且仅当 $f$ 在每个轮换上取常值，故 $|A^g|=m^{\text{cyc}(g)}$。代入即得公式。带权版本把 $m^{\text{cyc}(g)}$ 换成轮换指标积。

## 三、定理的严格表述

设有限群 $G$ 作用于有限集 $X$，色集 $C$，$|C|=m$。设 $\text{cyc}(g)$ 为 $g$ 在 $X$ 上的轮换个数。则不等价的着色方案数为
$$N=|C^X/G|=\frac1{|G|}\sum_{g\in G}m^{\text{cyc}(g)}.$$
加权版：$\sum_{\text{轨道}}\prod_{x}w(\text{色}(x))=\frac1{|G|}\sum_g\prod_{c\in\text{cyc}(g)}\Big(\sum_{a\in C}w(a)^{|c|}\Big)$。

## 四、证明过程

**证明：**

**步骤 1：Burnside 引理。** 对群作用 $G\curvearrowright S$，$|S/G|=\frac1{|G|}\sum_g|S^g|$。

**证明（Burnside）：** 双计数 $\sum_g|S^g|=\sum_{s}|\text{Stab}(s)|=\sum_s\frac{|G|}{|\text{Orb}(s)|}=|G|\sum_{\text{orbits}}\sum_{s\in O}\frac1{|O|}=|G|\,|S/G|$（每个轨道贡献 $\sum_{s\in O}\frac1{|O|}=1$）。$\blacksquare$

**步骤 2：转成着色。** 着色集 $A=C^X$，作用 $(g\cdot f)(x)=f(g^{-1}x)$。待算 $|A/G|$。$\blacksquare$

**步骤 3：刻画 $A^g$。** $f\in A^g\iff$ 对任意 $x$、任意 $k$，$f(g^k x)=f(x)$，即 $f$ 在 $g$ 的每个轮换上为常数。设轮换为 $c_1,\dots,c_{\text{cyc}(g)}$，则 $|A^g|=m^{\text{cyc}(g)}$。$\blacksquare$

**步骤 4：代入。** $|A/G|=\frac1{|G|}\sum_g m^{\text{cyc}(g)}$。$\blacksquare$

**步骤 5：加权版。** 对生成函数 $Z_g=\prod_{c\in\text{cyc}(g)}(\sum_a w(a)^{|c|})$ 由同样的 Burnside 论证导出。$\square$

## 五、应用与意义

Pólya 计数定理是化学（异构体计数）、对称物体的组合枚举、以及带对称性的染色问题的标准工具。它把"模群作用的计数"归结为轮换指标的计算，成为枚举组合学与计算代数的基本算法。加权形式在"生成函数+群对称"建模（如多体 free-energy、对称函数）中作用显著，并与对称群表示论、Lyndon 词理论相连接。