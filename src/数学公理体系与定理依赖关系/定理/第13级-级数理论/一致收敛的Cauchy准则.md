# 一致收敛的 Cauchy 准则

> **一句话大白话**：只要一列函数"靠后任意两项处处差得任意小"，它们就必定有同一个极限函数——不用知道极限在哪，光看函数们是否整体抱成团。
>
> **小例子**：$f_n(x)=\frac{x}{n}$ 在 $[0,1]$ 上，任意两点之间 $|f_n(x)-f_m(x)|\le\frac1N$ 可任意小，所以一致收敛到常数函数 $0$。

## 介绍

一致收敛的 Cauchy 准则（Cauchy Criterion for Uniform Convergence）是函数列和函数项级数理论中的基本准则，给出了判断函数列是否一致收敛的充要条件。该准则不需要知道极限函数，仅通过函数列本身的性质即可判断一致收敛性，是 Weierstrass M 判别法等工具的理论基础。

## 分析

**前置依赖**：函数列极限定义、一致收敛定义、数列的 Cauchy 收敛准则、sup 范数

**定理内容**：设 $\{f_n\}$ 是定义在集合 $E$ 上的函数列。则 $\{f_n\}$ 在 $E$ 上一致收敛当且仅当对任意 $\varepsilon>0$，存在正整数 $N$，使得当 $n,m>N$ 时，对任意 $x\in E$ 都有
$$|f_n(x)-f_m(x)|<\varepsilon$$

**等价形式（函数项级数）**：函数项级数 $\sum_{n=1}^{\infty} u_n(x)$ 在 $E$ 上一致收敛当且仅当对任意 $\varepsilon>0$，存在 $N$，使得当 $n>m>N$ 时，对任意 $x\in E$ 都有
$$\left|\sum_{k=m+1}^{n} u_k(x)\right|<\varepsilon$$

**前置知识**：
- 函数列极限定义：$\{f_n\}$ 在 $E$ 上逐点收敛到 $f$，若对任意 $x\in E$ 和 $\varepsilon>0$，存在 $N(x,\varepsilon)$ 使 $|f_n(x)-f(x)|<\varepsilon$
- 一致收敛定义：$\{f_n\}$ 在 $E$ 上一致收敛到 $f$，若对任意 $\varepsilon>0$，存在 $N(\varepsilon)$，使得当 $n>N$ 时，对任意 $x\in E$ 有 $|f_n(x)-f(x)|<\varepsilon$

**数学内涵**：
一致收敛的 Cauchy 准则与数列的 Cauchy 准则类似，但需要一致地控制所有 $x\in E$ 上的误差。该准则将一致收敛性问题转化为函数列在 sup 范数下的 Cauchy 性问题：$\{f_n\}$ 在 $E$ 上一致收敛当且仅当 $\{f_n\}$ 在 sup 范数下是 Cauchy 列。

## 思考过程

**必要性**：若 $\{f_n\}$ 一致收敛到 $f$，则对任意 $\varepsilon>0$，存在 $N$，使得当 $n>N$ 时，对任意 $x\in E$ 有 $|f_n(x)-f(x)|<\varepsilon/2$。从而当 $n,m>N$ 时，$|f_n(x)-f_m(x)|\le|f_n(x)-f(x)|+|f_m(x)-f(x)|<\varepsilon$。

**充分性**：若 $\{f_n\}$ 满足 Cauchy 条件，则对每个固定的 $x$，$\{f_n(x)\}$ 是 Cauchy 列，由实数 Cauchy 准则，$\{f_n(x)\}$ 收敛，设极限为 $f(x)$。可以证明收敛是一致的。

## 证明过程

**证明**：

**必要性**：设 $\{f_n\}$ 在 $E$ 上一致收敛到 $f$。则对任意 $\varepsilon>0$，存在 $N$，使得当 $n>N$ 时，对任意 $x\in E$ 有 $|f_n(x)-f(x)|<\varepsilon/2$。

从而当 $n,m>N$ 时，对任意 $x\in E$：
$$|f_n(x)-f_m(x)|\le|f_n(x)-f(x)|+|f_m(x)-f(x)|<\varepsilon/2+\varepsilon/2=\varepsilon$$

**充分性**：设 $\{f_n\}$ 满足一致 Cauchy 条件，即对任意 $\varepsilon>0$，存在 $N$，使得当 $n,m>N$ 时，对任意 $x\in E$ 有 $|f_n(x)-f_m(x)|<\varepsilon$。

对每个固定的 $x\in E$，$\{f_n(x)\}$ 是 Cauchy 列，由实数 Cauchy 收敛准则，$\{f_n(x)\}$ 收敛。设 $f(x)=\lim_{n\to\infty}f_n(x)$。

现在证明 $\{f_n\}$ 一致收敛到 $f$。对任意 $\varepsilon>0$，取 $N$ 使得当 $n,m>N$ 时，对任意 $x\in E$ 有 $|f_n(x)-f_m(x)|<\varepsilon/2$。

固定 $n>N$ 和 $x\in E$，令 $m\to\infty$，则 $f_m(x)\to f(x)$，由极限的保不等式性：
$$|f_n(x)-f(x)|=\lim_{m\to\infty}|f_n(x)-f_m(x)|\le\varepsilon/2<\varepsilon$$

因此当 $n>N$ 时，对任意 $x\in E$ 有 $|f_n(x)-f(x)|<\varepsilon$，即 $\{f_n\}$ 一致收敛到 $f$。

$\square$