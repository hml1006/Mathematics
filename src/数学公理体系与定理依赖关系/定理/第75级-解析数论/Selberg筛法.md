# Selberg 筛法

> **一句话大白话**：想数"剩下来没被小素数筛掉的数"，Selberg 筛法给出一个控制良好、可优化的上界——它能精确估算剔除满足若干同余条件的数后剩余的数量。
>
> **小例子**：数 $n\le x$ 中不被任何 $p<z$ 整除、且 $n\equiv a\pmod q$ 的个数 $S$，Selberg 上界给出 $S\le\frac{x}{\varphi(q)\log z}(1+o(1))+O(z^2)$。这就是"带算术约束的埃拉托色尼筛"的定量版本。

## 一、定理介绍

筛法是研究素数及相近数分布的组合工具。Selberg 在 1950 年代提出"上界筛法"：通过引入平方权重 $(\sum_{d|n}\lambda_d)^2$ 并变分优化选取 $\lambda_d$，得到比朴素包含-排除（Legendre）远强的一致上界。它是现代解析数论中不可或缺的技术，几乎见于一切素数年/孪生素数/无平方因子的定量估计。

## 二、原理思路

考虑 $S(\mathcal A,\mathcal P,z)=\#\{a\in\mathcal A:p\nmid a,\ \forall p<z\}$（跳过所有小于 $z$ 的素数）。构造一族实数 $\lambda_d$（$d\mid P(z)$，$P(z)=\prod_{p<z}p$）使 $\lambda_1=1$ 且 $\big(\sum_{d|n}\lambda_d\big)^2\ge1$ 当 $n=1$、$\ge0$ 一般地。于是
$$S\le\sum_{a\in\mathcal A}\Big(\sum_{d|(a,P(z))}\lambda_d\Big)^2=\sum_{d_1,d_2}\lambda_{d_1}\lambda_{d_2}\,\#\{a\in\mathcal A:[d_1,d_2]\mid a\}.$$
这是一个关于 $\lambda_d$ 的二次型；在约束 $\lambda_1=1$ 下解变分极小化，得到最优 $\lambda_d$，代入即得主项与误差项的分离。

## 三、定理的严格表述

设 $\mathcal A=\{n\le x:n\equiv a\pmod q\}$，$\mathcal P$ 为素数集，$z\le\sqrt x$，$P(z)=\prod_{p<z}p$。则
$$S(\mathcal A,\mathcal P,z)\le\frac{x}{\varphi(q)}\cdot\frac{1}{\log z}\left(1+O\left(\frac1{\log z}\right)\right)+O(z^2).$$

## 四、证明过程

**证明（概要）：**

**步骤 1：权重改造。** 取实数列 $\{\lambda_d\}$，$\lambda_1=1$，$d>z$ 时 $\lambda_d=0$。则对任意整数 $n$，
$$\left(\sum_{d\mid n}\lambda_d\right)^2\ge\begin{cases}1,&n=1,\\0,&n>1,\end{cases}$$
从而
$$S\le\sum_{a\in\mathcal A}\Big(\sum_{d|(a,P(z))}\lambda_d\Big)^2.$$

**步骤 2：展开。**
$$\sum_{a\in\mathcal A}\Big(\sum\lambda_d\Big)^2=\sum_{d_1,d_2}\lambda_{d_1}\lambda_{d_2}\,\#\{a\in\mathcal A:[d_1,d_2]\mid a\}=\sum_{d_1,d_2}\lambda_{d_1}\lambda_{d_2}\Big(\frac{x}{q[d_1,d_2]}+O(1)\Big).$$

**步骤 3：变分优化。** 主项为 $\frac{x}{q}\sum_{d_1,d_2}\frac{\lambda_{d_1}\lambda_{d_2}}{[d_1,d_2]}$。在 $\lambda_1=1$ 下用变分法（Selberg 的基本引理）取
$$\lambda_d=\mu(d)\frac{\log(z/d)}{\log z}\cdot\frac{d}{\varphi(d)}\prod_{p\mid d}\Big(1-\frac1p\Big)^{-1},$$
使上述二次型最小，得 $\sum_{d_1,d_2}\frac{\lambda_{d_1}\lambda_{d_2}}{[d_1,d_2]}\le\frac{1}{\log z}(1+O(1/\log z))$。

**步骤 4：代入可得**
$$S\le\frac{x}{\varphi(q)}\cdot\frac{1}{\log z}\Big(1+O\Big(\frac1{\log z}\Big)\Big)+O(z^2).$$
$\square$

## 五、应用与意义

Selberg 筛法是素数分布定量理论的两大主力工具之一（另一为大筛法）。它用于：（1）孪生素数与相减素数对的上界估计（经 Brun 思想改良）；（2）素数在短区间/算术级数中的界；（3）Goldbach 定理（Vinogradov 圆法与上界筛的结合）；（4）无平方因子数的分布。它还被推广为维数筛、半筛与组合筛（陈氏筛），在哥德巴赫猜想与陈景润定理等著名结果中承担关键上界角色。