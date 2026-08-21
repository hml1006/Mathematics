# 量子群 U_q(sl_2) 的表示分类

> **一句话大白话**：当参数 $q$ 不是单位根时，量子群 $U_q(\mathfrak{sl}_2)$ 的有限维不可约表示完全由"最高权"分类：对每个非负整数 $n$ 恰有一个 $(n+1)$ 维不可约表示 $V_n$。
>
> **小例子**：$n=0$ 时 $V_0$ 是一维平凡表示；$n=1$ 时 $V_1$ 是二维"基本表示"，其基为 $\{v_0,v_1\}$，$K$ 的作用为 $Kv_0=qv_0$、$Kv_1=q^{-1}v_1$——这是量子群世界中 $SU(2)$ 的自旋-$\tfrac12$ 表示。

## 一、定理介绍

> **前置依赖**：$U_q(\mathfrak{sl}_2)$ 的定义、q-整数与 q-阶乘、最高权方法、经典 $\mathfrak{sl}_2$ 表示论。

量子群 $U_q(\mathfrak{sl}_2)$ 是经典李代数 $\mathfrak{sl}_2$ 的量子形变，由生成元 $E,F,K$ 满足量子关系给出。该定理断言：在 $q$ 非单位根的"generic"情形，其有限维不可约表示由最高权 $q^n$ 分类，结构完全类比经典 $\mathfrak{sl}_2$ 表示论，只是用 $q$-整数替换普通整数。它是量子群表示论的基础，也是 Jones 多项式等量子不变量的来源。

## 二、原理思路

证明利用 $K$ 的可对角化与关系 $KEK^{-1}=q^2E$ 导出的权空间移动：$E$ 把权空间 $V_\lambda$ 映到 $V_{q^2\lambda}$，$F$ 映到 $V_{q^{-2}\lambda}$。由有限维性取"最高权"，构造权链 $v_k=\frac{1}{[k]!}F^k v_0$，并利用 $[E,F]=\frac{K-K^{-1}}{q-q^{-1}}$ 归纳计算 $E\cdot v_k$，最后由 $F\cdot v_n=0$ 确定参数 $\lambda=q^n$。

## 三、定理的严格表述

设 $q$ 不是单位根（$q^n\neq1$ 对任意 $n\in\mathbb{N}$）。则 $U_q(\mathfrak{sl}_2)$ 的有限维不可约表示由最高权分类：对每个非负整数 $n$，存在唯一的 $(n+1)$ 维不可约表示 $V_n$，基为 $\{v_0,\dots,v_n\}$，作用为：
$$
K\cdot v_k=q^{n-2k}v_k,
$$
$$
E\cdot v_k=\begin{cases}\frac{q^{n-k+1}-q^{-(n-k+1)}}{q-q^{-1}}v_{k-1},&k>0,\\0,&k=0,\end{cases}\qquad
F\cdot v_k=\begin{cases}\frac{q^{k+1}-q^{-(k+1)}}{q-q^{-1}}v_{k+1},&k<n,\\0,&k=n.\end{cases}
$$

## 四、证明过程

**证明：**

**步骤 1：最高权向量。** $K$ 的作用可对角化，故 $V=\bigoplus_\lambda V_\lambda$（$V_\lambda=\{v:Kv=\lambda v\}$）。

**步骤 2：权空间移动。** 由 $KEK^{-1}=q^2E$，$E\cdot V_\lambda\subseteq V_{q^2\lambda}$、$F\cdot V_\lambda\subseteq V_{q^{-2}\lambda}$。

**步骤 3：取最高权。** 因 $V$ 有限维，取 $|\lambda|$ 最大者，则 $E\cdot V_\lambda=0$；设 $v_0\in V_\lambda$ 非零且 $E\cdot v_0=0$。

**步骤 4：生成权链。** 定义 $v_k=\frac{1}{[k]!}F^k v_0$，其中 $[k]!=[1]\cdots[k]$，$[k]=\frac{q^k-q^{-k}}{q-q^{-1}}$。则 $K\cdot v_k=q^{-2k}\lambda v_k$，且有限维性给出 $v_{n+1}=0$、$v_n\neq0$。

**步骤 5：确定参数。** 由 $[E,F]=\frac{K-K^{-1}}{q-q^{-1}}$ 归纳得 $E\cdot v_k=\frac{\lambda q^{-(k-1)}-\lambda^{-1}q^{(k-1)}}{q-q^{-1}}v_{k-1}$。由 $0=E\cdot v_{n+1}\propto(\lambda q^{-n}-\lambda^{-1}q^n)v_n$ 得 $\lambda=q^n$（$q$ 非单位根）。

**步骤 6：构造与唯一性。** 此时作用如定理所述并满足量子关系，故 $V_n$ 是不可约 $(n+1)$ 维表示；任何不可约表示的最高权必须为 $q^n$，故全部为 $V_n$。$\square$

## 五、应用与意义

该定理是量子群表示论的支柱。经典情形（$q\to1$）退化为 $\mathfrak{sl}_2$ 表示分类，量子情形引入了 $R$-矩阵与辫子结构。由此分类衍生的量子维数（对 $q$ 为单位根时出现的截断表示）是构造纽结不变量（量子 $6j$-符号、Jones 多项式、Jones-Wenzl 投影子）的基础，在低维拓扑、共形场论与量子计算（拓扑量子计算、围棋码）中都有重要地位。