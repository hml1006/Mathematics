# GUE特征值关联函数
>
> **一句话大白话**：GUE 的特征值并不是独立散乱的，它们的任意多个联合分布都由一个行列式"核"精确掌控——这就是行列式点过程。
>
> **小例子**：$n$ 点 GUE 的 $k$-点关联函数 $R_k(x_1,\dots,x_k)=\det\big[\,K_n(x_i,x_j)\,\big]_{i,j}$，其中 $K_n(x,y)=n^{\frac12}\cdot\frac{\text{Cauchy-型核}}{\text{…}}$，规模化后趋于 sine/Airy 核。

## 一、定理介绍

GUE 特征值关联函数给出了厄米矩阵（GUE）特征值的有限阶联合统计的行列式结构：谱点构造成行列式点过程，其 $k$-点关联（连同边缘）由 Hermite 多项式的核 $K_{n}(x,y)$ 表达。当缩放转变（bulk → sine 核、edge → Airy 核）时给出普适行为，是 Mehta 公式在数学上的核心产物。

## 二、原理思路

GUE 特征值联合密度具有 Vandermonde 形式 $\propto e^{-\frac{n}{2}\sum \lambda_i^2}\prod_{i<j}(\lambda_i-\lambda_j)^2$。用 Hermite 多项式（正交多项式）展开 Vandermonde 行列式，得到行列式核表示：对任意 $k$，$k$-点关联 $R_k$ 等于相应 $k\times k$ 行列式 $\det[K_n]$。`K_n` 被写成 Christoffel–Darboux 核，缩放后收敛到 sine/Airy 核。

## 三、定理的严格表述

设 $\lambda_1,\dots,\lambda_n$ 为 $n\times n$ GUE 的（随机）特征值，其联合密度
$$
\rho^{(n)}=\frac1{Z_n}e^{-\frac n2\sum\lambda_i^2}\prod_{i<j}(\lambda_i-\lambda_j)^2.
$$
定义核
$$
K_n(x,y)=\frac{1}{\sqrt n}\,h_n^{-1}\,\big(h_{n+1}(x)h_n(y)-h_n(x)h_{n+1}(y)\big)e^{-\frac{n}{4}(x^2+y^2)},
$$
（$h_n$ 为归一 Hermite 多项式）。则对 Feature 值点过程，$k$-点关联为
$$
R_k(x_1,\dots,x_k)=\det\big[\,K_n(x_i,x_j)\,\big]_{1\le i,j\le k}.
$$

## 四、证明过程

用正交多项式法：由 Vandermonde 展开与 Christoffel–Darboux 买otics 计算 $R_k$ 的 fiddlings 行列式；用恒等 $\prod_{i<j}…=\det[\ldots]$ 与积分恒等推出 $\det[K_n]$ 的 $k$-点密度公式（Mehta / Gaudin 推演）。再以 Plancherel–Rotach 渐近（bulk：sine 核、edge：Airy 核）展示普适性。

## 五、应用与意义

关联函数的行列式形式使 GUE 的谱统计可显式处理（间距、间隙概率、谱形），是随机矩阵普适性、纠缠熵与自由概率校验的度量，也用于统计物理（二维色）与数学物理的非微扰新结构。