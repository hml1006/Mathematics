# Freiman 定理

> **一句话大白话**：整数集若"和集不胀"（$|A+A|\le C|A|$），那么它就"装在一个低维广义算术级数里"——除非集合本来就是稠密线型，否则它一定是某个 GAP 的子集，且容解规模、维数仅由 $C$ 控制。
>
> **小例子**：$A=\{1,2,\dots,10\}$，$|A+A|=19$，$C$ 很小，$A$ 是 1 维 GAP $\{1+x:0\le x<10\}$ 的子集。若 $A$ 是正方形数 $n^2$（$n\le m$）则 $|A+A|\sim|A|^2$（大），非小和集。

## 一、定理介绍

Freiman 定理（Freiman 1973）刻画小和集结构：设 $A\subseteq\mathbb{Z}$，$|A+A|\le C|A|$，则 $A$ 含于一个维数 $\le d(C)$、规模 $\le f(C)|A|$ 的广义等差数列（GAP）内。它回答"什么是和集小"的结构问题，是 additive combinatorics / structure-of-sum-sets 的奠基石。

## 二、原理思路

路径（经 Ruzsa 建模 + Bogolyubov）：(1) 用 Freiman 同态把 $A$ 提升到 $\mathbb{Z}_p$（素数 $p$ 不大），保和集规模；(2) 在 $\mathbb{Z}_p$ 里 $|S+S|\le C|S|$ ⇒ $2S-2S$ 含大子群 $H$（$|H|\ge p/C$，Bogolyubov 引理）；(3) $H$ 可参数化为 GAP（子群的子集）；(4) 逆映回 $\mathbb{Z}$（Ruzsa 逆向提升/同构），把 $A$ 装进同型 GAP；(5) 控制维数与容解（Green-Ruzsa：$d\le C-1$，$|P|\le\exp(C^{O(1)})|A|$）。

## 三、定理的严格表述

设 $A\subseteq\mathbb{Z}$ 有限，$|A+A|\le C|A|$。则存在广义等差数列 $P=\{a_0+a_1x_1+\cdots+a_dx_d:0\le x_i<L_i\}$ 使：
1. $A\subseteq P$；
2. $|P|\le f(C)|A|$（$f(C)$ 仅依赖 $C$）；
3. $\dim P=d\le d(C)$（$d(C)$ 仅依赖 $C$；Green-Ruzsa：$d\le C-1$）。

## 四、证明过程

**证明思路：**

**步骤 1：建模引理（Ruzsa）。** 由 $|A+A|\le C|A|$，存在素数 $p\le C'|A|$ 与子集 $A'\subseteq A$（$|A'|\ge|A|/C'$）使 $A'$ 与 $\mathbb{Z}_p$ 中某子集 $S$ Freiman 同构。$\blacksquare$

**步骤 2：Bogolyubov 引理。** 在 $\mathbb{Z}_p$ 中 $|S+S|\le C|S|$ 时，$2S-2S$ 含非平凡子群 $H$，$|H|\ge p/C$。$\blacksquare$

**步骤 3：子群→GAP。** $H\subseteq\mathbb{Z}_p$ 是大子群可参数化为（低维）GAP（因其为循环圈的子集可由生成元与长度给出）。$\blacksquare$

**步骤 4：逆向映射。** 用 Freiman 同构的逆向把 $A'$装回 $\mathbb{Z}$，得到 $A'$ 在整数 GAP 内；再将 $A\setminus A'$ 吸收并略为扩容（吸收常数依赖 $C$）。$\blacksquare$

**步骤 5：维数与尺寸。** 通过分析 $C$ 与维数关系（Green-Ruzsa：$d\le C-1$；$|P|\le\exp(C^{O(1)})|A|$）确定 $d(C),f(C)$。$\square$

## 五、应用与意义

Freiman 定理是加性组合最深刻的结构定理，是"结构 vs 随机"二分的高端成品。它被用于 sum-product 定理、Szemerédi 定理的结构化推广、以及许多 additive 问题的分解。其高维版本与 Green-Ruzsa 化定把握了群论与随机化，被用于概率数论、常量-Ramsey 与近同盟结构；逆向 Freiman 是 additive combinatorics 教科书的核心阵地。