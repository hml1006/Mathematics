# Krylov子空间方法

> **一句话大白话**：解巨型线性方程组时，不直接算逆矩阵，而是"从初始猜逐次乘系数矩阵"生出一串子空间（Krylov空间），再在里面挑最优近似解——像在一列越来越深的"幂次走廊"里逐步逼近真解，又快又不存巨型矩阵。
>
> **小例子**：对 $Ax=b$，令 $\mathcal{K}_m(b,A)=\mathrm{span}\{b,Ab,\dots,A^{m-1}b\}$，在其中投影求近似 $x_m$；如共轭梯度（对称正定时）就在这走廊里每步取"误差最小"处，几小步就贴到解上。

## 介绍

Krylov子空间方法（Krylov Subspace Methods）是求解大型稀疏线性方程组 $Ax = b$ 和特征值问题的一类最有效的迭代方法。Krylov子空间方法的理论基础是 Krylov 子空间 $\mathcal{K}_k(A, v) = \mathrm{span}\{v, Av, A^2v, \ldots, A^{k-1}v\}$。通过在此子空间中寻找近似解，Krylov 方法只需使用矩阵-向量乘积，不需要显式访问矩阵元素，特别适合大型稀疏问题。最重要的 Krylov 方法包括：共轭梯度法（CG，对称正定）、GMRES（一般非对称）、MINRES（对称不定）、BiCGSTAB（非对称）和 Lanczos 方法（特征值问题）。

## 分析

**前置依赖**：Krylov 子空间的定义、Gram-Schmidt 正交化与 Arnoldi 过程、Lanczos 三对角化、最小二乘与 QR 分解、条件数与预处理。

**定义**：对矩阵 $A \in \mathbb{R}^{n \times n}$ 和向量 $v \in \mathbb{R}^n$，$k$ 维 Krylov 子空间定义为

$$
\mathcal{K}_k(A, v) = \mathrm{span}\{v, Av, A^2v, \ldots, A^{k-1}v\}.
$$

**Krylov 方法的一般框架**：给定初始解 $x_0$，初始残差 $r_0 = b - Ax_0$，在第 $k$ 步寻找 $x_k \in x_0 + \mathcal{K}_k(A, r_0)$ 使得残差满足某种最优性条件。

**核心定理**：
1. **Arnoldi 过程**：生成 $\mathcal{K}_k$ 的一组正交基，将 $A$ 约化为上 Hessenberg 矩阵。
2. **Lanczos 过程**：对称情形的 Arnoldi 过程，将 $A$ 约化为三对角矩阵。
3. **GMRES 最优性**：在 $\mathcal{K}_k$ 中最小化 $L^2$-残差。
4. **CG 最优性**：在 $\mathcal{K}_k$ 中最小化 $A$-范数误差。

**依赖的概念**：Krylov 子空间、Arnoldi 过程、Lanczos 过程、GMRES、MINRES、预处理。

## 思考过程

Krylov 子空间方法的核心思想是：在逐步扩大的 Krylov 子空间中寻找最优解。由于 $A^k r_0$ 包含了 $A$ 的谱信息，随着 $k$ 增大，子空间越来越丰富，近似解也越来越精确。

Arnoldi 过程通过 Gram-Schmidt 正交化构造 Krylov 子空间的标准正交基，同时将 $A$ 投影到上 Hessenberg 矩阵 $H_k$。GMRES 方法就是在该投影上求解最小二乘问题。

对于对称矩阵，Lanczos 过程将 $A$ 投影到三对角矩阵 $T_k$，CG 方法利用 $A$ 的正定性高效求解。

Krylov 方法的收敛速度取决于矩阵的谱分布，预处理技术（如 ILU、SSOR、多重网格）通过改善谱性质来加速收敛。

## 证明过程

**定理**（Arnoldi 过程）：设 $A \in \mathbb{R}^{n \times n}$，$v_1 \in \mathbb{R}^n$ 满足 $\|v_1\| = 1$。Arnoldi 过程生成 $\mathcal{K}_k(A, v_1)$ 的标准正交基 $V_k = [v_1, \ldots, v_k]$ 和上 Hessenberg 矩阵 $H_k \in \mathbb{R}^{k \times k}$，满足

$$
A V_k = V_k H_k + h_{k+1,k} v_{k+1} e_k^T = V_{k+1} \tilde{H}_k,
$$

其中 $\tilde{H}_k \in \mathbb{R}^{(k+1) \times k}$ 是 $H_k$ 加上最后一行的扩展。

**证明**：

**步骤 1：初始化。**

取 $v_1 = r_0 / \|r_0\|$。

**步骤 2：迭代正交化。**

对 $j = 1, 2, \ldots, k$：
1. 计算 $w = A v_j$。
2. 对 $i = 1, \ldots, j$，$h_{i,j} = v_i^T w$，$w = w - h_{i,j} v_i$。
3. $h_{j+1,j} = \|w\|$，若 $h_{j+1,j} = 0$ 则停止（已找到不变子空间）。
4. $v_{j+1} = w / h_{j+1,j}$。

**步骤 3：验证关系。**

由构造，$A v_j = \sum_{i=1}^{j+1} h_{i,j} v_i$，写成矩阵形式即 $A V_k = V_{k+1} \tilde{H}_k$。$\square$

**定理**（GMRES 最优性）：GMRES 方法在第 $k$ 步的解 $x_k$ 满足

$$
\|b - A x_k\|_2 = \min_{x \in x_0 + \mathcal{K}_k(A, r_0)} \|b - A x\|_2.
$$

**证明**：

**步骤 1：参数化。**

设 $x_k = x_0 + V_k y$，其中 $y \in \mathbb{R}^k$，$V_k$ 是 $\mathcal{K}_k(A, r_0)$ 的标准正交基（由 Arnoldi 过程生成）。则残差为

$$
r_k = b - A x_k = r_0 - A V_k y = \beta v_1 - V_{k+1} \tilde{H}_k y = V_{k+1} (\beta e_1 - \tilde{H}_k y),
$$

其中 $\beta = \|r_0\|$，$e_1 = (1, 0, \ldots, 0)^T \in \mathbb{R}^{k+1}$。

**步骤 2：最小二乘问题。**

由于 $V_{k+1}$ 的列标准正交，$\|r_k\|_2 = \|\beta e_1 - \tilde{H}_k y\|_2$。因此，最小化 $\|r_k\|_2$ 等价于求解 $(k+1) \times k$ 的最小二乘问题

$$
\min_{y \in \mathbb{R}^k} \|\beta e_1 - \tilde{H}_k y\|_2.
$$

这可以通过 $\tilde{H}_k$ 的 QR 分解高效求解。$\square$

**推论**（CG 方法）：对对称正定矩阵 $A$，CG 方法在第 $k$ 步的解 $x_k$ 满足

$$
\|x_k - x^*\|_A = \min_{x \in x_0 + \mathcal{K}_k(A, r_0)} \|x - x^*\|_A,
$$

且收敛速度为 $2\left(\frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}\right)^k$，其中 $\kappa = \kappa(A)$ 是条件数。

**推论**（预处理）：Krylov 方法的收敛速度取决于矩阵的谱性质。通过预处理 $M^{-1}Ax = M^{-1}b$（或 $M^{-1/2} A M^{-1/2} \tilde{x} = \tilde{b}$），可以降低条件数，加速收敛。常用的预处理技术包括 Jacobi、SSOR、ILU 和不完全 Cholesky 分解。