# Langlands-Tunnell 定理

> **一句话大白话**：任何一个"奇"的、射影像为可解群的二维复 Galois 表示，都一定来自某个模形式——即 Artin 猜想在可解二维情形成立。
>
> **小例子**：Wiles 把 $G_{\mathbb Q}\to GL_2(\mathbb F_3)$ 的剩余表示沿 $GL_2(\mathbb F_3)\hookrightarrow GL_2(\mathbb C)$ 看成复表示，它的射影像可解，由 Langlands–Tunnell 它是模的，从而为 R=T 提供初始模性输入。

## 一、定理介绍

> **前置依赖**：Galois 表示与 Artin 表示（奇表示的定义）、Artin $L$-函数与 Artin 猜想、权 $1$ 模形式及其 Galois 表示（Deligne–Serre）、Hecke 本征形式、可解群与射影表示、Langlands 循环基变换（cyclic base change for $GL_2$）、$GL_2$ 的 Langlands 对应。

Langlands–Tunnell 定理（Langlands 1980；Tunnell 1981）证明 Artin 猜想的一个基本情形：**射影像为可解群的奇二维复 Galois 表示都是模的**。即若 $\rho:G_{\mathbb Q}\to GL_2(\mathbb C)$ 连续、不可约、奇（$\det\rho(c)=-1$，其中 $c$ 为复共轭），且其射影像在 $PGL_2(\mathbb C)$ 中可解，则存在权 $1$ 的模形式（Hecke 本征形式）$f$，使 $\rho\cong\rho_f$，从而 $L(s,\rho)=L(s,f)$ 为全纯函数并满足函数方程。它是 Wiles 证明费马大定理时处理 $p=3$ 剩余表示的起点，也是 Serre 模性猜想在可解像情形的经典结论。

## 二、原理思路

按射影像（$PGL_2(\mathbb C)$ 的有限子群 $D_n,A_4,S_4$ 或 $A_5$）分类，逐类证明：

1. **二面体情形**：当射影像为二面体群时，$\rho$ 由某个二次扩域上的一维特征诱导，即 $\rho=\mathrm{Ind}_{K/\mathbb Q}\chi$；用 Hecke 的自守诱导直接给出对应的权 $1$ 模形式。
2. **四面体（$A_4$）与八面体（$S_4$）情形**：它们在某个可解扩张 $L/\mathbb Q$ 上"变为"两个一维特征之和，借用 Langlands 的**循环基变换**把 $L$ 上的自守形式下降回 $\mathbb Q$，得到 $\rho$ 的模性。
3. **二十面体（$A_5$）情形**：由 Tunnell 用迹公式与四元数代数上的自守形式处理（射影像 $A_5$ 不可解，但相应模性仍成立），补全所有可能的有限像情形。

可解像（即 $D_n,A_4,S_4$ 及其子群）的情形由 Langlands 的基变换方法统一处理；Wiles 所用正是这一情形。

## 三、定理的严格表述

设 $\rho:G_{\mathbb Q}\to GL_2(\mathbb C)$ 是连续的二维复 Galois 表示，记 $\bar\rho$ 为它到 $PGL_2(\mathbb C)$ 的合成（射影表示），$c\in G_{\mathbb Q}$ 为复共轭。

**Langlands–Tunnell 定理**：若

1. $\rho$ 不可约；
2. $\rho$ 是奇的，即 $\det\rho(c)=-1$；
3. $\bar\rho$ 的像（射影像）是可解群，

则 $\rho$ 是**模的**：存在权 $1$ 的 $GL_2(\mathbb Q)$ 自守表示，等价地存在权 $1$ 的 Hecke 本征新形式 $f$，使
$$
\rho\ \cong\ \rho_f,
$$
从而 Artin $L$-函数满足 $L(s,\rho)=L(s,f)$。

等价表述：Artin 猜想对"射影像可解"的奇二维表示成立。更一般地，对全实域 $F$ 与 $\rho:G_F\to GL_2(\mathbb C)$ 有同样结论。

## 四、证明过程

因 $\rho$ 连续且 $GL_2(\mathbb C)$ 的有限生成紧子群有限，$\rho$ 的像为有限群；记其射影像 $\bar G\trianglelefteq PGL_2(\mathbb C)$，则 $\bar G$ 是 $PGL_2(\mathbb C)$ 的有限子群，即二面体群 $D_n$、$A_4$、$S_4$ 或 $A_5$ 之一。按类讨论。

**步骤 1（二面体情形）。** 设 $\bar G=D_n$。此时存在指数 $2$ 的扩域 $K/\mathbb Q$（二次域）与 $G_K$ 的一维连续特征 $\chi$，使
$$
\rho\ \cong\ \mathrm{Ind}_{G_K}^{G_{\mathbb Q}}\chi .
$$
由 Hecke 理论（自守诱导），$\chi$ 作为 $GL_1(K)$ 的自守表示，经自守诱导给出 $GL_2(\mathbb Q)$ 的自守表示 $\pi=\mathrm{AI}_{K/\mathbb Q}(\chi)$，其 Galois 表示正是 $\rho$；对应的模形式权为 $1$。故 $\rho$ 模。$\square$

**步骤 2（四面体与八面体情形，Langlands 基变换）。** 设 $\bar G=A_4$ 或 $S_4$，它们都是可解群。取 $\rho$ 的核所定的有限 Galois 扩张 $L/\mathbb Q$（$\mathrm{Gal}(L/\mathbb Q)$ 可解），则 $\rho|_{G_L}$ 可约；由 $A_4,S_4$ 的二维复表示在适当子群上的分解可知，存在 $G_L$ 的一维连续特征 $\chi_1,\chi_2$ 使
$$
\rho|_{G_L}\ \cong\ \chi_1\oplus\chi_2 .
$$
这两个特征给出 $GL_2(L)$ 的对角自守表示 $\pi_L$，其 Galois 表示与 $\rho|_{G_L}$ 相符。对可解扩张 $L/\mathbb Q$ 使用 Langlands 的**循环基变换**（沿循环扩域塔逐步下降），把 $\pi_L$ 下降（descent）为 $GL_2(\mathbb Q)$ 的自守表示 $\pi$。基变换与 Galois 侧的限制–诱导相容，故 $\pi$ 的 Galois 表示恰为 $\rho$，即 $\rho=\rho_\pi$ 为模的。$\square$

**步骤 3（二十面体情形，Tunnell）。** 设 $\bar G=A_5$（不可解），此时步骤 2 中"分解为一维特征之和"不再成立。Tunnell 改用一个四元数代数 $B/\mathbb Q$ 上的自守形式与迹公式：利用 $A_5$ 的射影二维表示可提升为 $SL_2(\mathbb C)$（而非 $GL_2$）的表示这一事实，把 $\rho$ 与某个四元数代数 $B$ 的自守形式对应，再用迹公式比较两侧的迹，得到 $GL_2(\mathbb Q)$ 的自守表示，使其 Galois 表示同构于 $\rho$。$\square$

**步骤 4（合成）。** 四种射影像情形穷尽了 $PGL_2(\mathbb C)$ 的有限子群。于是在"射影像可解"（即排除 $A_5$，涵盖 $D_n,A_4,S_4$）的假设下结论成立；连同 Tunnell 对 $A_5$ 的结果，$\rho$ 都来自权 $1$ 模形式 $f$，且 $\det\rho=\det\rho_f$ 为奇特征，$L(s,\rho)=L(s,f)$ 全纯并满足函数方程。$\square$

**在 Wiles 证明中的作用。** 对半稳定椭圆曲线 $E/\mathbb Q$，剩余表示 $\bar\rho_{E,3}:G_{\mathbb Q}\to GL_2(\mathbb F_3)$ 的像含于 $GL_2(\mathbb F_3)$（阶 $48$，可解）。把 $\mathbb F_3\subset\mathbb C$ 嵌入后，复合
$$
\rho:G_{\mathbb Q}\longrightarrow GL_2(\mathbb F_3)\hookrightarrow GL_2(\mathbb C)
$$
是奇、射影像可解的二维复表示；由本定理它是模的，对应一个权 $1$ 模形式。再配合 Deligne–Serre 的模 $3$ 约化与 Hida 族的升降，可得 $\bar\rho_{E,3}$ 是权 $2$ 模的，从而为 R=T 定理提供所需的初始模性输入（$p=3$）。$\square$

## 五、应用与意义

- **Artin 猜想**：对可解射影像的奇二维情形给出完整解答，是 Artin 全纯性猜想为数不多的已知大类。
- **Serre 模性猜想**：给出像可解情形的模性，是 Wiles 之前该猜想的主要进展。
- **费马大定理**：为 $p=3$ 的剩余表示提供模性起点，配合 R=T 完成"3-5 切换"。
- **Langlands 纲领**：是 $GL_2$ 上 Langlands 对应与基变换理论的经典应用范例，推动自守表示下降问题的研究。

## 相关条目

- [R=T 定理](./R=T定理.md)：Langlands–Tunnell 为其提供 $p=3$ 的初始模性输入。
- [谷山-志村定理（模性定理）](./谷山-志村定理（模性定理）.md)：其证明以 Langlands–Tunnell 处理小素数情形。
- [Fermat 大定理的证明概要](./Fermat大定理的证明概要.md)：Wiles 证明中用到本定理。
