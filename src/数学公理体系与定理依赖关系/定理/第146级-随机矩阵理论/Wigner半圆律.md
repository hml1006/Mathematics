# Wigner半圆律

> **一句话大白话**：随机 Hermite 矩阵的特征值，在尺寸趋大时会"摊平"成一条半圆形的谱分布，与它内部的独立同分布条目几乎无关。
>
> **小例子**：$n\times n$ 的 GUE（或其他 Wigner 矩阵）的经验谱分布 $\mu_n$，当 $n\to\infty$ 时收敛到密度 $\rho(x)=\frac{1}{2\pi}\sqrt{4-x^2}$（$|x|\le2$）——半圆曲线。

## 一、定理介绍

> **前置依赖**：Wigner随机矩阵、经验谱测度、矩方法与迹、Catalan数与非交叉配对、Carleman矩判定

Wigner半圆律（Wigner 1955）断言：对一类适度条件的随机 Hermite 矩阵（Wigner 矩阵：独立（在对称条件下同分布）的实/复条目、对角与次对角尺度适当），其经验谱分布 $\mu_n$ 几乎必然收敛到 **半圆分布**——密度 $\rho(x)=\frac{1}{2\pi}\sqrt{4-x^2}$（支持 $[-2,2]$）。这是随机矩阵理论的第一条普适性定理。

## 二、原理思路

半圆律经矩方法证明：估计经验谱矩 $\frac1n\sum_i\lambda_i^k$ 的均值（trace 期望），四舍五入到图同构 — 非交叉配对（Catalan 结构）主导贡献，得到半圆分布矩 $m_{2k}=\mathrm{Cat}_k$（Catalan 数）、$m_{2k+1}=0$。再由矩的局部分散性（Wigner 的方差估计）加上 Carleman/矩判定，推出分布收敛；用 Borel–Cantelli 得到几乎必然收敛。

## 三、定理的严格表述

设 $H_n$（$n\times n$ Hermite 或对称实矩阵）为 Wigner 矩阵：$\mathrm{E}\,H_{ij}=0$、$\mathrm{Var}\,H_{ij}=1$（$i\ne j$），$\sup_{i\le n}\mathrm{E}|H_{ii}|$ 与次对角矩有界。令 $\mu_n=\frac1n\sum_{\lambda_i\le x}\delta$ 为经验谱测度。则存在 $\mu_n\Rightarrow\mu_{\mathrm{semi}}$（a.s.）对正态化（$\frac1{\sqrt n}H_n$ 或对次对角方差归一）成立，其中
$$
d\mu_{\mathrm{semi}}=\frac{1}{2\pi}\sqrt{4-x^2}\,\mathbf 1_{|x|\le2}\,dx.
$$

## 四、证明过程

矩原法：(1) 利用期望对非交叉配对计数（无向图与 $\lambda$ 幂的迹）估计 $\mathrm{E}\,\mathrm{tr}H^{2k}\sim n\cdot\mathrm{Cat}_k$；(2) 精细 Ihrgu 估计 $\mathrm{Var}$ 次级项（$\sim n^2$ 尺度下可忽略）；(3) 用 Carleman 条件保证矩序列确定唯一分布，得到有限迹矩趋于 Catalan 矩；(4) 由 Chebyshev+Borel–Cantelli 或 WDD 定理得到几乎必然弱收敛。

## 五、应用与意义

半圆律开启了随机矩阵普适性研究，是量子混沌、统计（GUE/GOE）、信号处理领域经验谱分析的基础。它与自由概率（半圆即自由高斯）、Wigner 猜测（邻近间距）和特征值统计的更精细普适定理紧密相连。
## 相关条目

- [Wigner 半圆律（第64级-随机矩阵理论）](../第64级-随机矩阵理论/Wigner半圆律.md)：与本条目为同一定理，另收录于第64级-随机矩阵理论，可交叉参考。
