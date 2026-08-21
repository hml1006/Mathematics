# Glivenko-Cantelli 定理

> **一句话大白话**：样本再多也只是摸到了真实的分布函数，但当样本量趋于无穷时，经验分布函数这把"用样本画出的阶梯"会在整个数轴上同时（一致地）逼近真实的分布函数。
>
> **小例子**：投硬币 10 万次后，各点之下正面向上的比例所画的阶梯，几乎处处在所有位置都贴近真实概率分布。

## 一、定理介绍

> **前置依赖**：经验分布函数、分布函数的单调性与右连续性、强大数定律、分位点构造网格、几乎必然一致收敛

设 $X_1,\dots,X_n$ 独立同分布于分布函数 $F$，经验分布函数 $\hat{F}_n(x) = \frac{1}{n}\sum_{i=1}^n \mathbf{1}_{\{X_i\le x\}}$。Glivenko-Cantelli 定理断言 $\hat{F}_n$ 在 $\mathbb{R}$ 上一致地几乎必然收敛到 $F$：

$$
\sup_{x\in\mathbb{R}}|\hat{F}_n(x) - F(x)| \xrightarrow{\text{a.s.}} 0,\quad n\to\infty.
$$

## 二、原理思路

先用强大数定律得到每个固定点 $x$ 处 $\hat{F}_n(x)\to F(x)$ 几乎必然；随后借助 $F$ 的单调性，用有限个分位点网格把整条实数轴的偏差控制在这些网格点上偏差的最大值，从而把"逐点收敛"升级为"一致收敛"。

## 三、定理的严格表述

设 $\hat{F}_n(x) = \frac{1}{n}\sum_{i=1}^n\mathbf{1}_{\{X_i\le x\}}$ 为经验分布函数，则

$$
\mathbb{P}\Big(\lim_{n\to\infty}\sup_{x\in\mathbb{R}}|\hat{F}_n(x) - F(x)| = 0\Big) = 1.
$$

## 四、证明过程

1. **逐点收敛**：对固定 $x$，由强大数定律 $\hat{F}_n(x)\xrightarrow{\text{a.s.}}F(x)$。
2. **构造网格**：取 $\varepsilon>0$ 与有限点 $-\infty=x_0<x_1<\dots<x_k=\infty$，使 $F(x_j-) \le \frac{j\varepsilon}{3}\le F(x_j)$（$F$ 的 $\varepsilon/3$ 分位点）。
3. **控制区间**：对任意 $x$（落在相邻网格点间），可上/下限出偏差与网格点偏差之差不超过 $\frac{\varepsilon}{3}$。
4. **一致收敛**：对充分大的 $n$，网格点最大偏差 $<\frac{\varepsilon}{3}$，整体一致偏差 $<\frac{2\varepsilon}{3}$，由 $\varepsilon$ 任意得一致收敛。

## 五、应用与意义

Glivenko-Cantelli 定理是经验过程理论与非参数统计的基石，保证了"用样本分布逼近总体分布"在一致意义下可靠。它是 Kolmogorov-Smirnov 拟合优度检验、自助法（Bootstrap）以及众多数理统计一般理论（如 VC 理论中经验风险最小化）的重要前提。