# GMRES的收敛性

> **一句话大白话**：解一般（不必对称）线性方程组时，GMRES 在所有能组合出的 $k$ 维近似解里挑"残差最小"的那个，并给出可用的残差上界估计。
>
> **小例子**：对非对称矩阵，GMRES 在第 $k$ 步把残差压缩到 $\|r_k\|_2\le \kappa(V)\cdot C^k \,\|r_0\|$ 以内，只要 $A$ 的 Jordan 块不"太坏"，收敛就快。

## 一、定理介绍

GMRES（广义极小残差法）求解一般非对称线性方程组 $Ax=b$：它把近似解局限在 Krylov 子空间 $x_0+\mathcal{K}_k$，选择使二范数残差 $\|b-Ax\|_2$ 最小的迭代点。其收敛性质的两个方面：其一是残差最小的最优性（一一对应于一个最小二乘问题），其二是收敛上界的刻画——涉及 $A$ 的谱（Jordan 结构）与规范化因子，是理解非对称 Krylov 收敛性的核心定理。

## 二、原理思路

GMRES 用 Arnoldi 过程在 $\mathcal{K}_k$ 上建立正交基 $Q_k$ 及 Hessenberg 形式 $H_k$，把残差极小问题转化为小规模最小二乘。理论收敛性通过"多项式刻画"：存在 $p\in\mathbb{P}_k$，$p(0)=1$ 使 $r_k=p(A)r_0$，其最优性又转化为 $A$ 在 $r_0$ 上的作用；进而可用 $A$ 的特征值（或对可对角化情形用特征向量矩阵条件数 $\kappa(V)$）给出显式上界。对于 Jordan 块严重的矩阵，收敛可能慢，需配合预条件。

## 三、定理的严格表述

设 $A\in\mathbb{R}^{n\times n}$ 可逆，$Ax=b$，$x_0$ 初值，$r_0=b-Ax_0$。GMRES 第 $k$ 步的残差为
$$
r_k=\arg\min_{\substack{p\in\mathbb{P}_k\\p(0)=1}}\|p(A)r_0\|_2.
$$
（该式即 GMRES 的最优性刻画。）

**可对角化收敛上界**：若 $A=X\operatorname{diag}(\lambda_i)X^{-1}$（特征值互异），则
$$
\|r_k\|_2\le\kappa_2(X)\,\min_{p\in\mathbb{P}_k,p(0)=1}\max_{i}|\tilde p(\lambda_i)|\,\|r_0\|_2,
$$
其中 $\kappa_2(X)=\|X\|_2\|X^{-1}\|_2$。特别地，若 $\lambda_i$ 落在以 $c$ 为心、$d$ 为半径（$|c|>d$）的圆盘 $\Gamma$ 外（即 $\lambda_i$ 均远离 $0$），则存在 $K<1$ 使
$$
\frac{\|r_k\|_2}{\|r_0\|_2}\le \kappa_2(X)\left(\frac{d}{|c|}\right)^{k}=\kappa_2(X)\,K^k,\quad K=\frac{d}{|c|}.
$$

## 四、证明过程

1. **最优性刻画**。由 GMRES 的构造，$x_k-x_0\in\mathcal{K}_k(A,r_0)$，故存在次数 $\le k$ 的多项式 $q$ 使 $x_k-x_0=q(A)r_0$，即 $r_k=b-Ax_k=p(A)r_0$，其中 $p(t)=1-tq(t)$。残差极小等价于在所有满足 $p(0)=1$、$\deg p\le k$ 的多项式中最小化 $\|p(A)r_0\|_2$。

2. **对角化代入**。$A=X\operatorname{diag}(\lambda_i)X^{-1}$ 时 $p(A)=Xp(\operatorname{diag}(\lambda_i))X^{-1}$，故
   $$
   \|p(A)r_0\|_2\le\kappa_2(X)\|p(\operatorname{diag}(\lambda_i))\|\,\|r_0\|_2=\kappa_2(X)\max_i|p(\lambda_i)|\,\|r_0\|_2.
   $$
3. **圆外区域的 Chebyshev 型多项式**。当特征值位于以 $c$ 为心、$d$ 为半径的圆盘之外（$|c|>d$），取任意 $\lambda$ 于该圆盘外，构造 $p(t)=\dfrac{T_k\left(\frac{c}{d}(1-t/c)\cdot\right)}{T_k(c/d)}$ 型的移位 Chebyshev 多项式，满足 $p(0)=1$ 且在圆盘边界上模最大，从而沿边界 $\max_i|p(\lambda_i)|\le T_k$ 的分母界。代入得到 $\max_i|p(\lambda_i)|\le(d/|c|)^k$ 量级的因子（$\frac{d}{|c|}=\frac{1}{|c/d|}<1$）。

4. **合并**。取最小的 $K=\frac{d}{|c|}$，代入第 2 步即得收敛上界。$\blacksquare$

**注。** $K$ 越接近 $0$，越远离单位圆盘的点收敛越快；但对重 Jordan 块或特征值贴近原点，GMRES 可能出现"停滞+跳变"的伪收敛模式，此时需预条件或不同 Krylov 方向。

## 五、应用与意义

- **非对称系统**：工程中大流量、反应动力学、有限元非对称刚度方程的标准求解器。
- **预条件**：上界中的 $\kappa_2(X)$ 与谱信息提示用右/左预条件改善谱分布，是高效实现的核心。
- **重启版 GMRES(m)**：为控制内存与迭代数而重新启动，理论收敛界帮助选择重启长度与预条件。
- **启发 LCM**：作为非对称 Krylov 最优残差准则的范式，影响 QMR、BiCGSTAB 等方法的设计与理解。