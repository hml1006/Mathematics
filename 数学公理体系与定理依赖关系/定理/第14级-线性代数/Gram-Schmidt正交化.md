# Gram-Schmidt 正交化

## 介绍

Gram-Schmidt 正交化方法由丹麦数学家约尔根·佩德森·格拉姆（Jørgen Pedersen Gram）和德国数学家埃尔哈德·施密特（Erhard Schmidt）提出，是内积空间中将线性无关组化为标准正交组的基本方法。该方法是构造正交基的标准工具，在数值线性代数、信号处理、量子力学等领域有重要应用。

## 分析

**定理内容**：设 $\{\mathbf{v}_1,\mathbf{v}_2,\ldots,\mathbf{v}_n\}$ 是内积空间 $V$ 中的一组线性无关向量，则存在一组标准正交向量 $\{\mathbf{u}_1,\mathbf{u}_2,\ldots,\mathbf{u}_n\}$，使得对每个 $k$，$\operatorname{span}\{\mathbf{v}_1,\ldots,\mathbf{v}_k\}=\operatorname{span}\{\mathbf{u}_1,\ldots,\mathbf{u}_k\}$。

**构造方法**：
$$\begin{aligned}
\mathbf{w}_1 &= \mathbf{v}_1, &
\mathbf{u}_1 &= \frac{\mathbf{w}_1}{\|\mathbf{w}_1\|} \\
\mathbf{w}_2 &= \mathbf{v}_2-\langle\mathbf{v}_2,\mathbf{u}_1\rangle\mathbf{u}_1, &
\mathbf{u}_2 &= \frac{\mathbf{w}_2}{\|\mathbf{w}_2\|} \\
&\vdots & &\vdots \\
\mathbf{w}_k &= \mathbf{v}_k-\sum_{j=1}^{k-1}\langle\mathbf{v}_k,\mathbf{u}_j\rangle\mathbf{u}_j, &
\mathbf{u}_k &= \frac{\mathbf{w}_k}{\|\mathbf{w}_k\|}
\end{aligned}$$

**前置知识**：
- 投影公式：$\operatorname{proj}_{\mathbf{u}}(\mathbf{v})=\frac{\langle\mathbf{v},\mathbf{u}\rangle}{\langle\mathbf{u},\mathbf{u}\rangle}\mathbf{u}$

**数学内涵**：
Gram-Schmidt 正交化的核心思想是：从第 $k$ 个向量 $\mathbf{v}_k$ 中减去它在已得到的前 $k-1$ 个正交方向上的投影，从而得到与前面所有向量正交的分量 $\mathbf{w}_k$，再归一化得到 $\mathbf{u}_k$。

## 思考过程

设已构造了标准正交向量 $\mathbf{u}_1,\ldots,\mathbf{u}_{k-1}$，它们张成的空间与 $\mathbf{v}_1,\ldots,\mathbf{v}_{k-1}$ 张成的空间相同。

考虑 $\mathbf{v}_k$ 在 $\operatorname{span}\{\mathbf{u}_1,\ldots,\mathbf{u}_{k-1}\}$ 上的正交投影：
$$\operatorname{proj}_{\operatorname{span}\{\mathbf{u}_1,\ldots,\mathbf{u}_{k-1}\}}(\mathbf{v}_k)=\sum_{j=1}^{k-1}\langle\mathbf{v}_k,\mathbf{u}_j\rangle\mathbf{u}_j$$

则 $\mathbf{w}_k=\mathbf{v}_k-\sum_{j=1}^{k-1}\langle\mathbf{v}_k,\mathbf{u}_j\rangle\mathbf{u}_j$ 垂直于所有 $\mathbf{u}_j$（$j<k$）。由于 $\{\mathbf{v}_1,\ldots,\mathbf{v}_k\}$ 线性无关，$\mathbf{w}_k\neq 0$，归一化即得 $\mathbf{u}_k$。

## 证明过程

**证明**：

对 $k$ 进行归纳。

**归纳基础**：$k=1$。令 $\mathbf{w}_1=\mathbf{v}_1$，由线性无关性知 $\mathbf{w}_1\neq 0$。令 $\mathbf{u}_1=\frac{\mathbf{w}_1}{\|\mathbf{w}_1\|}$，则 $\|\mathbf{u}_1\|=1$，且 $\operatorname{span}\{\mathbf{v}_1\}=\operatorname{span}\{\mathbf{u}_1\}$。

**归纳假设**：假设已构造了标准正交向量 $\mathbf{u}_1,\ldots,\mathbf{u}_{k-1}$，使得 $\operatorname{span}\{\mathbf{v}_1,\ldots,\mathbf{v}_{k-1}\}=\operatorname{span}\{\mathbf{u}_1,\ldots,\mathbf{u}_{k-1}\}$。

**归纳步骤**：构造 $\mathbf{u}_k$。

令
$$\mathbf{w}_k=\mathbf{v}_k-\sum_{j=1}^{k-1}\langle\mathbf{v}_k,\mathbf{u}_j\rangle\mathbf{u}_j$$

**验证正交性**：对任意 $i<k$，
$$\langle\mathbf{w}_k,\mathbf{u}_i\rangle=\langle\mathbf{v}_k,\mathbf{u}_i\rangle-\sum_{j=1}^{k-1}\langle\mathbf{v}_k,\mathbf{u}_j\rangle\langle\mathbf{u}_j,\mathbf{u}_i\rangle=\langle\mathbf{v}_k,\mathbf{u}_i\rangle-\langle\mathbf{v}_k,\mathbf{u}_i\rangle=0$$
因为 $\langle\mathbf{u}_j,\mathbf{u}_i\rangle=\delta_{ij}$。

**验证非零**：若 $\mathbf{w}_k=0$，则 $\mathbf{v}_k=\sum_{j=1}^{k-1}\langle\mathbf{v}_k,\mathbf{u}_j\rangle\mathbf{u}_j\in\operatorname{span}\{\mathbf{u}_1,\ldots,\mathbf{u}_{k-1}\}=\operatorname{span}\{\mathbf{v}_1,\ldots,\mathbf{v}_{k-1}\}$，与 $\{\mathbf{v}_1,\ldots,\mathbf{v}_k\}$ 线性无关矛盾。故 $\mathbf{w}_k\neq 0$。

令 $\mathbf{u}_k=\frac{\mathbf{w}_k}{\|\mathbf{w}_k\|}$，则 $\|\mathbf{u}_k\|=1$，且 $\operatorname{span}\{\mathbf{v}_1,\ldots,\mathbf{v}_k\}=\operatorname{span}\{\mathbf{u}_1,\ldots,\mathbf{u}_k\}$。

由归纳法，结论对所有 $k$ 成立。

$\square$