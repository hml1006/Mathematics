# Weierstrass M 判别法

## 介绍

Weierstrass M 判别法（Weierstrass M-Test）由德国数学家卡尔·魏尔斯特拉斯（Karl Weierstrass）提出，是判断函数项级数一致收敛性的重要方法。该方法通过将函数项级数的每项用常数级数的对应项控制，将一致收敛性问题转化为常数项级数的收敛性问题，是分析中最常用的判别法之一。

## 分析

**定理内容**：设函数项级数 $\sum_{n=1}^{\infty} u_n(x)$ 在集合 $E$ 上有定义，且存在常数序列 $\{M_n\}$，满足：
1. $|u_n(x)|\le M_n$ 对任意 $x\in E$ 和 $n\in\mathbb{N}$ 成立；
2. $\sum_{n=1}^{\infty} M_n$ 收敛；

则 $\sum_{n=1}^{\infty} u_n(x)$ 在 $E$ 上绝对一致收敛（即既绝对收敛又一致收敛）。

**前置知识**：
- 比较判别法（常数项级数）

**数学内涵**：
Weierstrass M 判别法的核心思想是"优级数"（majorant series）方法。常数项级数 $\sum M_n$ 称为 $\sum u_n(x)$ 的优级数。如果优级数收敛，则原函数项级数不仅逐点绝对收敛，而且在整个集合上一致收敛。该判别法简洁实用，但要求 $u_n(x)$ 在 $E$ 上一致有界，有时这个条件过于苛刻。

## 思考过程

由一致收敛的 Cauchy 准则，$\sum u_n(x)$ 在 $E$ 上一致收敛当且仅当对任意 $\varepsilon>0$，存在 $N$，使得当 $n>m>N$ 时，对任意 $x\in E$ 有 $|\sum_{k=m+1}^n u_k(x)|<\varepsilon$。

由条件 $|u_n(x)|\le M_n$ 和三角不等式：
$$\left|\sum_{k=m+1}^n u_k(x)\right| \le \sum_{k=m+1}^n |u_k(x)| \le \sum_{k=m+1}^n M_k$$

由于 $\sum M_n$ 收敛，其部分和是 Cauchy 列，因此存在 $N$ 使得当 $n>m>N$ 时 $\sum_{k=m+1}^n M_k<\varepsilon$，从而一致收敛。

## 证明过程

**证明**：

设 $|u_n(x)|\le M_n$ 对任意 $x\in E$ 成立，且 $\sum_{n=1}^{\infty} M_n$ 收敛。

由一致收敛的 Cauchy 准则，对任意 $\varepsilon>0$，由于 $\sum M_n$ 收敛，存在 $N$，使得当 $n>m>N$ 时，
$$\sum_{k=m+1}^n M_k < \varepsilon$$

则对任意 $x\in E$，当 $n>m>N$ 时，
$$\left|\sum_{k=m+1}^n u_k(x)\right| \le \sum_{k=m+1}^n |u_k(x)| \le \sum_{k=m+1}^n M_k < \varepsilon$$

再由一致收敛的 Cauchy 准则，$\sum_{n=1}^{\infty} u_n(x)$ 在 $E$ 上一致收敛。

**绝对收敛性**：对任意 $x\in E$，由比较判别法，$\sum |u_n(x)|$ 收敛，故原级数绝对收敛。

$\square$