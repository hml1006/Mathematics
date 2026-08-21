# Marčenko-Pastur定律
>
> **一句话大白话**：样本协方差矩阵（$X X^T$、行数与列数按固定比例）的经验谱分布，收敛到一个由比例决定的"MP 分布"。
>
> **小例子**：$p\times n$ 高斯 $\Sigma=0$，$X X^T/n$ 当 $p/n\to c$ 时其谱分布趋于权重
$$
\rho_c(x)=(1-\frac1c)^+\delta_0+\frac{\sqrt{(x-a)_+(b-x)_+}}{2\pi c x},\; a=(1-\sqrt c)^2,\; b=(1+\sqrt c)^2.
$$

## 一、定理介绍

> **前置依赖**：样本协方差矩阵、经验谱测度、Stieltjes变换、矩方法、自一致方程

Marčenko–Pastur定律（MP，Marčenko–Pastur 1967）给出白化样本协方差矩阵经验谱分布在高维极限的极限本征：对 $p\times n$ 数据 $X$（iid 适正：均值零、协方差 $\Sigma$），当 $p,n\to\infty$、$p/n\to c\in(0,\infty)$ 时，$X\Sigma X^{\top}$ 的经验谱收敛到 MP 分布（参数 $c$、密度形如上述）。这是高维统计/随机矩阵协方差谱的基础。

## 二、原理思路

极限谱通过 Stieltjes 变换 / 自由概率（半圆样积）计算：$X X^{\top}/n$ 的特征值对应 $X^{\top}X/n$（$n$ 尖端矩阵）的谱；用 trace 的矩与 Marcinkiewicz 恒等给出 Stieltjes 变换 $m$ 满足的二次方程，解出密度。上下界 $b=(1+\sqrt c)^2$、$a=(1-\sqrt c)^2$ 来自最大的极限特征值之位置。

## 三、定理的严格表述

设 $X$ 为 $p\times n$ 实/复矩阵，条目 iid、期望 $0$、方差 $1$（或更一般独立同分布模），且 $p/n\to c>0$。令 $\mu_n$ 为 $Y_n=\frac{1}{n}X X^{\top}$ 的经验谱测度。则几乎必然
$$
\mu_n\Rightarrow\mu_{c},
$$
其中 $\mu_c=(1-\tfrac1c)_+\delta_0+\mu^{\mathrm{ac}}_c$ 且
$$
\frac{d\mu^{\mathrm{ac}}_c}{dx}=\frac{\sqrt{(x-a)_+(b-x)_+}}{2\pi c x}\mathbf 1_{x>0},\quad a=(1-\sqrt c)^2,\;b=(1+\sqrt c)^2.
$$

## 四、证明过程

用随机矩阵方法：(1) 把谱问题转成矩/积分；(2) 引入 Stieltjes 变换 $m_n(z)=\int\frac{d\mu_n}{x-z}$，用分化+=矩法或自一致方程（Marchenko–Pastur z-方程）得到 $m\simeq\Big(\dots\Big)$ 满足式；(3) 取极限 $n\to\infty$ 得 $c$ 相关方程并反演得密度；(4) 用 Borel–Cantelli/蔫轱辘得到 a.s. 弱收敛。

## 五、应用与意义

MP 定律刻画高维样本协方差的谱，是主成分分析（PCA）、大数/稀疏协方差估计、信号处理（CS 与随机矩阵理论）与免费概率建模的基石，也在数据科学的"谱位碎片逃逸"现象与分类器研究中频繁引用。