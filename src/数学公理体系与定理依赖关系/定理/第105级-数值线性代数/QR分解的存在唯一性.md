# QR分解的存在唯一性

> **一句话大白话**：凡是"列满秩"的矩阵，都能被唯一分解成一个正交矩阵和一个上三角矩阵的乘积——正交部分刻画"方向"，上三角部分刻画"相对大小"。
>
> **小例子**：对 $A=\begin{pmatrix}1&0\\1&1\end{pmatrix}$，有 $A=QR$，其中 $Q=\frac1{\sqrt2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}$，$R=\begin{pmatrix}\sqrt2&1/\sqrt2\\0&1/\sqrt2\end{pmatrix}$，且 $R$ 对角元为正时分解唯一。

## 一、定理介绍

QR 分解是数值线性代数的基础工具：对（列满秩的）实矩阵 $A$，存在正交矩阵 $Q$（$Q^\top Q=I$）与上三角矩阵 $R$（对角元非负，适当规格化）使得 $A=QR$。它统一地用于最小二乘问题、线性方程组（householder 消去）、特征问题（QR 算法）与迭代方法（Krylov 子空间）的推导与舍入误差分析，是一把"万能的分解利器"。

## 二、原理思路

等价于 Gram–Schmidt 正交化：$A$ 的列被依次正交归一化为 $Q$ 的列，正交化过程中的系数存入 $R$。由于正交化在"列方向上逐步进行"，$R$ 为上三角。存在性可由经典的修改的 Gram–Schmidt、Householder 反射或 Givens 旋转构造；唯一性则来自列满秩下每列方向唯一确定，结合 $R$ 对角元符号的规格化约定。

## 三、定理的严格表述

设 $A\in\mathbb{R}^{m\times n}$，$\operatorname{rank}(A)=n$（列满秩）。则存在正交矩阵 $Q\in\mathbb{R}^{m\times n}$（$Q^\top Q=I_n$）与上三角矩阵 $R\in\mathbb{R}^{n\times n}$（对角线元素为正）使得
$$
A=Q R.
$$
且在该约定（$r_{ii}>0$）下，分解**唯一**：若 $A=\tilde Q\tilde R$ 也满足 $\tilde Q$ 正交、$\tilde R$ 上三角且 $\tilde r_{ii}>0$，则 $\tilde Q=Q$、$\tilde R=R$，$R$ 的对角元为 $\prod$ 意义下的列范数。

## 四、证明过程

**存在性（Gram–Schmidt）.** 记 $A$ 的列为 $a_1,\dots,a_n$。经典 Gram–Schmidt：
$$
q_1=\frac{a_1}{\|a_1\|},\qquad r_{1j}=a_j^\top q_1\ (j\le n),
$$
对 $i=2,\dots,n$：先 $\tilde a_i=a_i-\sum_{k<i}(a_i^\top q_k)q_k$，令 $r_{ki}=a_i^\top q_k$，$r_{ii}=\|\tilde a_i\|>0$（列满秩），$q_i=\tilde a_i/r_{ii}$。整理即得 $a_i=\sum_{k\le i} r_{ki}q_k$，故 $A=QR$，$Q$ 列正交（$Q^\top Q=I$），$R$ 上三角，对角元为正。

**唯一性.** 设 $A=Q_1R_1=Q_2R_2$。因 $R_1,R_2$ 可逆（对角元正），$Q_1^\top Q_2=R_1R_2^{-1}$。左端 $Q_1^\top Q_2$ 是正交矩阵（正交矩阵之积），右端 $R_1R_2^{-1}$ 是上三角矩阵（上三角之逆仍上三角，乘积仍上三角且对角元为正）。一个既正交又上三角且对角元为正的矩阵必为单位阵：正交性给出列范数 $1$，对上三角阵推出对角元（正）全为 $1$，往上回代推出非对角元 $0$。故 $R_1R_2^{-1}=I$，$R_1=R_2$，进而 $Q_1=Q_2$。$\blacksquare$

**注（秩亏情况）** 若 $\operatorname{rank}(A)<n$，可用 Householder/列旋转得到含更多结构的分解，或接受 $R$ 出现 $0$ 对角元；实际中常用修改的 Gram–Schmidt 改善数值稳定性，用 Householder 也好，但都归结为同一存在唯一性骨架。

## 五、应用与意义

- **最小二乘**：解最小二乘 $\min\|Ax-b\|$ 转化为解 $Rx=Q^\top b$ 的三角方程组，稳定且高效。
- **QR 算法**：$A=QR$、再 $A'=RQ$ 的迭代构造特征值算法，其最优收敛性依赖分解的稳定性（见 QR 收敛性定理）。
- **正交投影与 Krylov**：提供正交基，是 Arnoldi/GMRES 等 Krylov 方法的正交化基础。
- **数值稳定性**：相比法方程 $A^\top Ax=A^\top b$ 的病态条件数平方，QR 分解的条件数约为 $\kappa(A)$ 一次方，显著改善舍入。