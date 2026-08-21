# Schur 函数的对称性与正交性

> **一句话大白话**：Schur 函数是"最对称"的对称函数——它们构成 Hall 内积的正交基，且每个关于某划分的 Schur 函数在行为、正交性上都"互不相干"：$\langle s_\lambda,s_\mu\rangle=\delta_{\lambda\mu}$。
>
> **小例子**：在 3 个变量下，$s_{(2,1)}=x_1^2x_2+x_1x_2^2+x_1^2x_3+x_1x_3^2+x_2^2x_3+x_2x_3^2+2x_1x_2x_3$ 关于三变量对称；$s_{(2,1)}$ 与 $s_{(3)}$ 在 Hall 内积下正交。

## 一、定理介绍

> **前置依赖**：Schur 函数与半标准 Young 表、Jacobi-Trudi 行列式与 Vandermonde 行列式、Hall 内积、Cauchy 恒等式与幂和对称函数。

Schur 函数（半标准 Young 表的权重）是 $GL(n)$ 不可约表示的特征标，是对称函数环 $\Lambda$ 的一组基。本定理说明：(1) $s_\lambda$ 是对称的（对变量置换不变）；(2) 在 Hall 内积下 $\{s_\lambda\}$ 正交归一（$\langle s_\lambda,s_\mu\rangle=\delta_{\lambda\mu}$）。

## 二、原理思路

- **对称性**由 Jacobi-Trudi/行列式比法证明：$s_\lambda=\frac{\det(x_i^{\lambda_j+n-j})}{\det(x_i^{n-j})}$，分子分母同为交替（Vandermonde），对置换作标记变换后比值不变。
- **正交性**依赖 Hall 内积与 Cauchy 恒等式 $\prod_{i,j}\frac1{1-x_iy_j}=\sum_\lambda s_\lambda(x)s_\lambda(y)$。同式展开为幂和 $\exp(\sum_k p_k(x)p_k(y)/k)=\sum_\lambda\frac1{z_\lambda}p_\lambda(x)p_\lambda(y)$，结合 $\{p_\lambda\}$ 的正交性（$\langle p_\lambda,p_\mu\rangle=\delta_{\lambda\mu}z_\lambda$）导出。

## 三、定理的严格表述

设 $s_\lambda(x_1,\dots,x_n)$ 为划分 $\lambda$ 的 Schur 函数。

1. **对称性**：$s_\lambda$ 是 $x_1,\dots,x_n$ 的对称函数。
2. **正交性**：对 Hall 内积 $\langle\cdot,\cdot\rangle$，$\langle s_\lambda,s_\mu\rangle=\delta_{\lambda\mu}$（Kronecker delta）。

## 四、证明过程

**证明：**

**对称性：** $s_\lambda=\frac{\det(x_i^{\lambda_j+n-j})_{i,j=1}^n}{\det(x_i^{n-j})_{i,j=1}^n}$，分母为 Vandermonde $\prod_{i<j}(x_i-x_j)$。对置换 $\sigma\in S_n$，将 $x_i$ 换为 $x_{\sigma(i)}$ 时分子分母同乘 $\text{sgn}(\sigma)$（对策列的逆序因子），故比值不变，$s_\lambda$ 对称。$\blacksquare$

**正交性：** 定义 Hall 内积 $\langle p_\lambda,p_\mu\rangle=\delta_{\lambda\mu}z_\lambda$，$z_\lambda=\prod_i i^{m_i}m_i!$。

**引理（Cauchy 恒等式）：** $\prod_{i,j}\frac1{1-x_iy_j}=\sum_\lambda s_\lambda(x)s_\lambda(y)$。同时 $=\exp\big(\sum_{k\ge1}\frac{p_k(x)p_k(y)}k\big)=\sum_\lambda\frac1{z_\lambda}p_\lambda(x)p_\lambda(y)$。$\blacksquare$

由 Cauchy 恒等式两端相等，
$$\sum_\lambda s_\lambda(x)s_\lambda(y)=\sum_\lambda\frac1{z_\lambda}p_\lambda(x)p_\lambda(y).$$
对 $\{s_\mu(y)\}$ 与 $\{p_\nu(x)\}$ 分别作基展开、结合 $\{p_\nu\}$ 的 $\delta_{\lambda\mu}z_\lambda$ 正交性（逐项比较系数），即得 $s_\lambda$ 在 Hall 内积下正交：$\langle s_\lambda,s_\mu\rangle=\delta_{\lambda\mu}$。$\square$

## 五、应用与意义

Schur 函数的对称性与正交性使其成为对称函数理论与表示的基岩：正交基保证 $s_\lambda$ 的唯一展开，使 Littlewood-Richardson 系数、Kostka 数良定义。它同时作为 $GL(n)$ 与 $S_n$ 的不可约特征标，连接组合（Young 表）、表示论、代数几何（Schubert 计算）与概率（Plancherel 测度）。Jacobi-Trudi 与 Cauchy 恒等式更深入矩形与超越恒等式的结构。