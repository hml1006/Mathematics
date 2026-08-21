# R-变换的加法公式
>
> **一句话大白话**：在自由独立性下，两个随机变量和的谱（自由卷积）对应的"R-变换"就是各自 R-变换的加法——把非交换的加法谱映成了简单加法。
>
> **小例子**：若 $a,b$ 自由独立，则 $\mathcal R_{a+b}(z)=\mathcal R_a(z)+\mathcal R_b(z)$，其中 $\mathcal R_X$ 是 $X$ 的 R-变换（自由矩的生成函数族）。

## 一、定理介绍

R-变换（Voiculescu）是自由概率中的"对数特征"— 对自由独立变量，**和的谱**经 R-变换线性化：$\mathcal R_{a+b}=\mathcal R_a+\mathcal R_b$。它把自由卷积的复杂密度操作翻译为函数加法，是把半圆（$\mathcal R_s(z)=z$）与自由独立的谱合成统一处理的工具。

## 二、原理思路

R-变换对随机变量 $X$ 按矩定义：$\mathcal R_X(z)=\sum_{n\ge0}\alpha_{n+1}z^n$，其中自由累积量 $\alpha_n$（free cumulants）由 $\alpha_{n}\big\vert$ 的非交叉 chord 收缩定义，$\alpha$ 线性作用于自由独立变量。因此对自由独立 $a,b$，其 $n$-累积量相加：$\alpha_{a+b}=\alpha_a+\alpha_b$，累加回 R-生成函数即得加法公式。

## 三、定理的严格表述

设 $(\mathcal A,\varphi)$ 为 $C^*$-概率空间，对 $X\in\mathcal A$ 定义 R-变换 $\mathcal R_X(z)=\sum_{n\ge0}\alpha_{n+1}(X)z^n$（自由累积量 $\alpha_n$）。则对自由独立的 $a,b\in\mathcal A$：
$$
\mathcal R_{a+b}(z)=\mathcal R_a(z)+\mathcal R_b(z)
$$
（作为 $\mathbb C$ 中序列/幂级数，在收敛意义下成立）。特别地，$\mathcal R_{s}(z)=z$（半圆分布）。

## 四、证明过程

第一步定义自由累积量 $\alpha_k$ 的联（经非交叉集与特征多项式 $\mathcal R(g_X)$）；第二步验证 $\alpha$ 的自由线性：$\alpha_n(a+b)=\alpha_n(a)+\alpha_n(b)$（因非交叉收缩的独立交合）；第三步把 $\alpha$ 映回 R-幂级数，得到逐项相加。加上矩的适定/收敛条件，得到谱层面的等号。

## 五、应用与意义

R-变换加法是计算自由独立之和谱的通用工具（半圆例、Marchenko–Pastur 的白谱等），是自由概率应用于随机矩阵相加、通信（AWGN 速率）与自由卷积谱合成（FHT vs 经典卷积）的数学核心，也是自由无限可除理论的出发点。