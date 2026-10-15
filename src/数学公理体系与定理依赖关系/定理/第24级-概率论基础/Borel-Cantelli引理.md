# Borel-Cantelli 引理

> **一句话大白话**：如果一列事件的概率加起来是有限的，那么"同时发生无穷多次"这件事几乎不可能——因为"再来一次"的代价被总预算卡死了。
>
> **小例子**：抛一枚均匀硬币，第 $n$ 次要求连续 $n$ 次正面，其概率为 $2^{-n}$，总和 $\sum_{n\ge1}2^{-n}=1<\infty$，故这样的"连续 $n$ 次正面"几乎不可能发生无穷多次。

## 介绍

Borel-Cantelli 引理是概率论中关于事件序列"无穷多次发生"的基本工具，由法国数学家 Émile Borel 于 1909 年在研究正规数时提出，后由意大利数学家 Francesco Paolo Cantelli 于 1917 年推广到一般情形。本条目讨论的是"收敛部分"（第一 Borel-Cantelli 引理），即概率级数收敛蕴含上极限事件零概率。

该引理在强大数定律、重对数律、极限定理与随机图理论中反复出现，是证明"几乎必然"型结论最常用的入口。

## 分析

**前置依赖**：测度空间与概率空间、可数可加性、单调序列的连续性、级数收敛判别

**定理内容**：设 $(\Omega,\mathcal{F},P)$ 是概率空间，$\{A_n\}_{n\ge1}\subseteq\mathcal{F}$ 是一列事件。若

$$
\sum_{n=1}^{\infty}P(A_n)<\infty,
$$

则上极限事件

$$
\limsup_{n\to\infty}A_n=\bigcap_{N=1}^{\infty}\bigcup_{n=N}^{\infty}A_n
$$

满足 $P(\limsup_{n\to\infty}A_n)=0$，即 $A_n$ 几乎必然只发生有限多次。

**加强的逆命题（第二 Borel-Cantelli 引理）**：若 $\{A_n\}$ 相互独立且 $\sum_n P(A_n)=\infty$，则 $P(\limsup A_n)=1$。独立性与发散性缺一不可。

**前置知识**：
- 概率的可数可加性：两两不交事件的可数并可加
- 测度的上连续性：若 $B_N\downarrow B$ 则 $P(B_N)\downarrow P(B)$

## 思考过程

证明的想法非常直接：$\limsup A_n$ 落在任一"尾并" $\bigcup_{n\ge N}A_n$ 中。用次可加性（Boole 不等式）把尾并的概率压到级数的尾部，再让 $N\to\infty$，级数收敛意味着尾部趋于零。

关键点是：不需要独立性，也不需要事件之间任何相关性，仅仅"总概率有限"就足以否定"无穷多次发生"。这种普适性是它在证明中被频繁使用的原因。

## 证明过程

**步骤 1：写出尾并的包含关系**

对每个 $N\ge1$ 定义尾并 $B_N=\bigcup_{n=N}^{\infty}A_n$。显然 $B_1\supseteq B_2\supseteq\cdots$ 且

$$
\limsup_{n\to\infty}A_n=\bigcap_{N=1}^{\infty}B_N.
$$

**步骤 2：用次可加性估计 $P(B_N)$**

由概率的次可加性（Boole 不等式），

$$
P(B_N)=P\left(\bigcup_{n=N}^{\infty}A_n\right)\le\sum_{n=N}^{\infty}P(A_n).
$$

**步骤 3：利用级数收敛的尾部趋于零**

因 $\sum_{n=1}^{\infty}P(A_n)<\infty$，其余项满足 $\sum_{n=N}^{\infty}P(A_n)\to0$（$N\to\infty$）。故对任意 $\varepsilon>0$，存在 $N_0$ 使 $N\ge N_0$ 时 $P(B_N)\le\varepsilon$。

**步骤 4：用连续性从上取极限**

由 $B_N\downarrow\bigcap_{N}B_N=\limsup A_n$ 与概率的连续性，

$$
P(\limsup_{n\to\infty}A_n)=\lim_{N\to\infty}P(B_N)\le\lim_{N\to\infty}\sum_{n=N}^{\infty}P(A_n)=0.
$$

由于概率非负，得到 $P(\limsup A_n)=0$。证毕。

**步骤 5：逆命题的说明**

若再假设 $A_n$ 相互独立且级数发散，则 $\prod_{n\ge N}(1-P(A_n))=0$，即尾交的概率为零，取补得到 $P(\limsup A_n)=1$，此即第二 Borel-Cantelli 引理。

## 课堂问答

**老师**：一列事件"几乎必然只发生有限多次"，需要事件之间独立吗？

**学生**：不需要。只要 $\sum_{n=1}^{\infty}P(A_n)<\infty$，就有 $P(\limsup_{n\to\infty}A_n)=0$，这是第一 Borel-Cantelli 引理，对任意相关的事件列都成立。

**老师（追问）**：那么反过来，概率和发散就一定无穷多次发生吗？

**学生**：不能。仅 $\sum_n P(A_n)=\infty$ 不足以推出 $P(\limsup A_n)=1$；必须再加 $\{A_n\}$ 相互独立，才是第二引理。独立与发散缺一不可。

**老师（拓展）**：证明的抓手落在哪里？

**学生**：落在尾并的次可加性上，$P(B_N)=P\big(\bigcup_{n=N}^{\infty}A_n\big)\le\sum_{n=N}^{\infty}P(A_n)$，再用 $B_N\downarrow\limsup A_n$ 的连续性与级数尾部趋于零，即得结论。

## 相关条目

- [弱大数定律](./弱大数定律.md)：用 Chebyshev 不等式控制偏差概率
- [强大数定律](./强大数定律.md)：几乎必然收敛的经典结论
- [中心极限定理](./中心极限定理.md)：另一个极限定理的支柱
