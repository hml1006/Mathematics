# SVD分解定理

> **一句话大白话**：任何矩阵都能"旋转-拉伸-再旋转"：变成三个矩阵 $A=U\Sigma V^\top$，其中左右是两个正交变换，中间的 $\Sigma$ 是表示"各方向伸缩量"的奇异值的对角阵。
>
> **小例子**：对 $A=\begin{pmatrix}1&0\\0&2\end{pmatrix}$，$U=I$、$V=I$、$\Sigma=\operatorname{diag}(2,1)$——奇异值 $2,1$ 正是沿 $y,x$ 方向的拉伸量。

## 一、定理介绍

> **前置依赖**：对称半正定矩阵的谱定理、特征值分解、正交基的扩充、向量组正交归一化、矩阵的秩与秩公式。

奇异值分解（Singular Value Decomposition, SVD）是数值线性代数的"皇冠明珠"：任一 $m\times n$ 矩阵可分解为 $A=U\Sigma V^\top$，其中 $U\in\mathbb{R}^{m\times m}$、$V\in\mathbb{R}^{n\times n}$ 正交，$\Sigma$ 为 $m\times n$ 的"对角"阵，对角元为奇异值（$A$ 的奇异值为 $\sqrt{A^\top A}$ 的特征值）。SVD 同时给出秩的多项式判定、低秩近似（Eckart–Young）、灵敏性分析（条件数）与主成分分析（PCA）的理论基础。

## 二、原理思路

把矩阵视为线性映射，SVD 声称：总存在一组正交输入基（$V$ 的列，即右奇异向量）和一组正交输出基（$U$ 的列，即左奇异向量），使得映射在该对正交基下是"对角"，即把第 $j$ 个输入基向量映到 $\sigma_j$ 倍的第 $j$ 个输出基向量。$\sigma_j$ 正是 $A^\top A$（或 $AA^\top$）的特征值平方根；$V$ 的列是 $A^\top A$ 的特征向量，$U$ 的列由 $Av_i=\sigma_i u_i$ 决定，正交性由对称矩阵谱定理保证。

## 三、定理的严格表述

设 $A\in\mathbb{R}^{m\times n}$。则存在正交矩阵 $U\in\mathbb{R}^{m\times m}$、$V\in\mathbb{R}^{n\times n}$ 及矩阵 $\Sigma\in\mathbb{R}^{m\times n}$（$\Sigma_{ij}=0$ 当 $i\ne j$，$\Sigma_{ii}=\sigma_i\ge0$）使得
$$
A=U\Sigma V^\top,
$$
其中 $\sigma_1\ge\sigma_2\ge\cdots\ge\sigma_{\min(m,n)}\ge0$ 称为 $A$ 的奇异值，$\sigma_i=\sqrt{\lambda_i(A^\top A)}$。若 $r=\operatorname{rank}(A)$，则恰有 $\sigma_1\ge\cdots\ge\sigma_r>0$，$\sigma_{r+1}=\cdots=0$。

## 四、证明过程（正则值理论/特征分解法）

1. $A^\top A$ 是对称半正定矩阵，由谱定理可对角化：存在正交 $V=(v_1,\dots,v_n)$ 使
   $$
   A^\top A\,v_i=\lambda_i v_i,\quad \lambda_1\ge\cdots\ge\lambda_n\ge0.
   $$
   记 $\sigma_i=\sqrt{\lambda_i}$，令 $r$ 为 $\sigma_i>0$ 的个数。

2. 对 $i=1,\dots,r$ 定义 $u_i=Av_i/\sigma_i$。则 $\{u_i\}$ 规范正交：
   $$
   u_i^\top u_j=\frac{v_i^\top A^\top A v_j}{\sigma_i\sigma_j}=\frac{\sigma_j^2}{\sigma_i\sigma_j}\delta_{ij}.
   $$
3. 由秩公式，$r=\operatorname{rank}(A^\top A)=\operatorname{rank}(A)$，故 $\operatorname{rank}(u_1,\dots,u_r)=r$，将其扩充为 $\mathbb{R}^m$ 的标准正交基 $\{u_1,\dots,u_m\}$ 构成 $U$。
4. 验证分解：对 $j\le r$，$Av_j=\sigma_j u_j$；对 $j>r$（$\sigma_j=0$），$\|Av_j\|^2=v_j^\top A^\top A v_j=\sigma_j^2=0$，故 $Av_j=0$。于是对任意 $x=\sum_j c_j v_j$，
   $$
   Ax=\sum_{j=1}^{r}\sigma_j c_j u_j=U\Sigma V^\top x,
   $$
   即 $A=U\Sigma V^\top$。$\blacksquare$

**注。** 分解并非唯一（对重复奇异值可有正交旋转自由度），但奇异值稳定且唯一；可通过适当约定（如固定 $\sigma_i$ 排序、限定按需归一化）得到规范形式。

## 五、应用与意义

- **低秩近似（Eckart–Young）**：$A_k=\sum_{i=1}^k\sigma_i u_i v_i^\top$ 是 $A$ 的最优秩 $k$ 逼近，误差 $\sigma_{k+1}$，是主成分分析、图像压缩、数据降维的理论基础。
- **伪逆与最小二乘**：$A^+=V\Sigma^+ U^\top$ 给出 Moore–Penrose 伪逆，稳定求解最小二乘与病态方程组。
- **条件数与灵敏度**：$\kappa(A)=\sigma_{\max}/\sigma_{\min}$ 刻画矩阵对扰动的敏感度，是数值稳定性分析的核心量。
- **普遍应用**：推荐系统矩阵分解、信号处理、谱聚类、控制论中的系统辨识，皆以 SVD 为核心算子。