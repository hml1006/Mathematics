# Ramanujan图的构造

> **一句话大白话**：能不能用最少的边造出扩张性最好的正则图？能——Ramanujan 图除了最大特征值外，其余特征值都落在 $|\lambda|\le2\sqrt{d-1}$ 的理论最优区间。LPS 用数论（四元数、模 $q$）显式把它们造了出来。
>
> **小例子**：对素数 $p\equiv1\pmod4$、$q\equiv1\pmod4$ 且 $p$ 为模 $q$ 的二次剩余，LPS 构造给出一族 $(p+1)$-正则 Ramanujan 图 $X^{p,q}$，顶点数 $q(q^2-1)/2$，谱间隙顶到 $2\sqrt p$。

## 一、定理介绍

> **前置依赖**：Alon–Boppana 定理、Cayley 图、Lagrange 四平方和定理、特征标理论、Weil 猜想（Ramanujan 猜想）。

Ramanujan 图是"最优展开图"：对于 $d$-正则图，Alon–Boppana 定理指出第二大特征值至少为 $2\sqrt{d-1}-o(1)$，故满足 $|\lambda|\le2\sqrt{d-1}$（除 $\lambda_1=d$）的图达到谱间隙的理论下界。Lubotzky–Phillips–Sarnak 用四元数与数论分支和构造出无穷族此类图。

## 二、原理思路

构造把 $PSL(2,q)$ 作为底群、以 Jacobi 四平方和恒等式解 $a_0^2+a_1^2+a_2^2+a_3^2=p$ 得到的 $p+1$ 个元素作生成集，定义 Cayley 图。Cayley 图的特征值可由生成集的不可约特征标求和给出，而这个和恰是可由 Deligne 证明的 Weil 猜想（Ramanujan 猜想的数论版本）以 $2\sqrt p$ 严格控制的 Kloosterman 型指数和。

## 三、定理的严格表述

（Lubotzky–Phillips–Sarnak, 1988）设 $p,q$ 是素数，$p\equiv q\equiv1\pmod4$，且 $p$ 是模 $q$ 的二次剩余。则存在 $(p+1)$-正则图 $X^{p,q}$ 满足：

1. $X^{p,q}$ 有 $q(q^2-1)/2$ 个顶点（$q$ 为奇素数时）。
2. $X^{p,q}$ 是 Ramanujan 图：除最大特征值 $p+1$ 外，所有特征值 $\lambda$ 满足 $|\lambda|\le2\sqrt p$。
3. $X^{p,q}$ 的围长 $g\ge2\log_p q-\log_p4$。

## 四、证明过程

**证（概述）：**

1. **群。** $PSL(2,q)$ 是 $2\times2$ 行列式 $1$ 矩阵模 $q$ 且商掉 $\pm I$ 的群，阶为 $q(q^2-1)/2$。

2. **生成元。** 由 Lagrange 四平方和定理，$a_0^2+a_1^2+a_2^2+a_3^2=p$ 有 $8(p+1)$ 个整数解；把每个解 $(a_0,a_1,a_2,a_3)$ 映射为矩阵
   $$
   \begin{bmatrix}a_0+a_1\sqrt{-1}&a_2+a_3\sqrt{-1}\\-a_2+a_3\sqrt{-1}&a_0-a_1\sqrt{-1}\end{bmatrix}\quad(\bmod q),
   $$
   在 $PSL(2,q)$ 中恰给出 $p+1$ 个元素，连同逆元组成对称生成集 $S$。

3. **Cayley 图。** $X^{p,q}=\operatorname{Cay}(PSL(2,q),S)$，因 $S$ 对称而 $(p+1)$-正则。

4. **特征值。** Cayley 图的特征值由特征标给出：
   $$
   \lambda_\chi=\sum_{s\in S}\chi(s)\quad(\chi\text{ 为不可约特征标}).
   $$

5. **Kloosterman 与 Weil 猜想。** 非平凡特征标下 $\bigl|\sum_{s\in S}\chi(s)\bigr|\le2\sqrt p$，这正是 Ramanujan 条件；上界由 Deligne 证明的 Weil 猜想（Ramanujan 猜想）保证。

6. **围长。** 若 $X^{p,q}$ 有长 $2k$ 的圈，则模 $q$ 下存在 $a_0^2+a_1^2+a_2^2+a_3^2=p^k$ 的非平凡解，需 $p^k\ge q$，故 $g\ge2\log_p q-\log_p4$。$\square$

## 五、应用与意义

LPS 构造是首次显式构造出 Ramanujan 图族，在图论、数论（四平方和、Kloosterman 和、Weil 猜想）与表示论（$PSL(2,q)$ 的特征标）之间架起深刻桥梁。Ramanujan 图作为最优展开图，广泛用于设计高容错通信网络、纠错码（expander codes）、伪随机数生成器与去随机化方法。

## 课堂问答

**老师**：$d$-正则图里，凭什么说 $|\lambda|\le2\sqrt{d-1}$ 就是"最优"？这个数从哪里冒出来的？

**学生**：它正好卡在 Alon–Boppana 下界的极限上，不能再小。对 $d$-正则图，除平凡特征值 $d$ 外第二大特征值绝对值至少是 $2\sqrt{d-1}-o(1)$，所以把上界也定在 $2\sqrt{d-1}$ 就是理论最优，这样的图叫 Ramanujan 图。LPS 构造的 $X^{p,q}=\operatorname{Cay}(PSL(2,q),S)$ 有 $q(q^2-1)/2$ 个顶点，除 $p+1$ 外全部 $|\lambda|\le2\sqrt p$。

**老师（追问）**：生成集 $S$ 是怎么来的？为什么恰好是 $p+1$ 个元素？

**学生**：来自 Lagrange 四平方和 $a_0^2+a_1^2+a_2^2+a_3^2=p$ 的解，把 $(a_0,a_1,a_2,a_3)$ 映成矩阵 $\begin{bmatrix}a_0+a_1\sqrt{-1}&a_2+a_3\sqrt{-1}\\-a_2+a_3\sqrt{-1}&a_0-a_1\sqrt{-1}\end{bmatrix}\pmod q$。解有 $8(p+1)$ 组，在 $PSL(2,q)$ 里约化后恰得 $p+1$ 个元素，连同逆元构成对称生成集，所以图是 $(p+1)$-正则。容易搞错的是：$8(p+1)$ 是整数解个数，而非群元素个数，商掉单位和同伴后才是 $p+1$。

**老师（拓展）**：那"所有非平凡特征值都 $\le2\sqrt p$"这一步靠什么保证？

**学生**：靠特征标公式 $\lambda_\chi=\sum_{s\in S}\chi(s)$：Cayley 图的每个不可约特征标给一个特征值。非平凡 $\chi$ 下这个和是 Kloosterman 型指数和，其上界 $|\sum_{s\in S}\chi(s)|\le2\sqrt p$ 正是 Deligne 证明的 Weil 猜想（Ramanujan 猜想的数论版本）。围长下界也顺带得到：若存在长 $2k$ 的圈，则 $a_0^2+\cdots+a_3^2=p^k$ 模 $q$ 有非平凡解，需 $p^k\ge q$，故 $g\ge2\log_p q-\log_p4$。
