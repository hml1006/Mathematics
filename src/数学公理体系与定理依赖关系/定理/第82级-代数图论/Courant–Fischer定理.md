# Courant–Fischer 定理

> **一句话大白话**：对称矩阵的第 $k$ 个特征值不用解方程，它等于"在所有 $k$ 维子空间里，把最大可能的 Rayleigh 商压到最低"的那个值；换个方向看，也是"在所有 $(n-k+1)$ 维子空间里，把最小可能的 Rayleigh 商抬到最高"的那个值。

> **小例子**：$k=1$ 时它退化为 Rayleigh 商的最小值等于最小特征值；$k=n$ 时退化为最大值等于最大特征值。中间的那些特征值则由"维数计数"锁定，这正是 Cheeger 不等式中 $\mu_2=\min_{\mathbf x\perp\mathbf 1}\frac{\mathbf x^TL\mathbf x}{\|\mathbf x\|^2}$ 的来源。

## 一、定理介绍

> **前置依赖**：谱定理、Rayleigh 商、维数公式、二次型的正交对角化、拉格朗日乘子法。

Courant–Fischer 极小极大定理由 Richard Courant（1920）与 Ernst Fischer（1905）分别建立，是对称矩阵（更一般地，自伴算子）变分原理的**完整形式**。Rayleigh 原理只刻画了两个极端特征值（最小与最大），而实际问题（图的谱、主成分分析、微分算子的特征值、结构稳定性）中需要的是**每一个**特征值的变分刻画。Courant–Fischer 给出的答案是把"第 $k$ 个"这一序数信息翻译成"子空间维数"，从而把特征值问题完全转化为优化问题。

它的意义体现在：

1. **无需解特征方程**：特征值可由优化问题逼近（子空间迭代、Lanczos 算法、幂法）并具有数值稳定性；
2. **单调性与扰动**：由极小极大形式立刻得到特征值对矩阵单调（$\lambda_k(A+B)\ge\lambda_k(A)$ 当 $B\succeq0$）与 Weyl 扰动不等式；
3. **交错定理**：主子矩阵的特征值与原矩阵特征值交错（Cauchy 交错定理）由本定理立即推出；
4. **几何与分析中的桥梁**：图的 Cheeger 常数、Laplace 特征值、变分特征值问题都通过本定理与二次型（能量）挂钩，见 [Cheeger不等式](./Cheeger不等式.md)。

## 二、原理思路

1. **只处理二次型**：由谱定理，$A$ 有正交规范特征基 $u_1,\dots,u_n$，任务是用子空间维数刻画第 $k$ 个特征值 $\lambda_k$。
2. **上界方向用"顺最优子空间"**：取 $V_0=\operatorname{span}\{u_1,\dots,u_k\}$，在 $V_0$ 中 Rayleigh 商不超过 $\lambda_k$，故"最优 $k$ 维子空间的商的上确界" $\le\lambda_k$。
3. **下界方向用维数计数**：任何 $k$ 维子空间 $V$ 必与"只含 $k$ 阶以上特征方向的 $(n-k+1)$ 维子空间"相交，交中非零向量的 Rayleigh 商 $\ge\lambda_k$，故 $V$ 上的上确界 $\ge\lambda_k$。
4. **换方向得极大极小形式**：把同一直觉反过来用（取 $u_1,\dots,u_k$ 张成的 $k$ 维子空间作比较，取 $(n-k+1)$ 维子空间作极小），得到对偶表述。
5. **推广**：把 $\mathbb R^n$ 换成 Hilbert 空间、把 Rayleigh 商换成 $a(x,x)/\|x\|^2$，即为自伴算子的变分特征值原理。

## 三、定理的严格表述

设 $A\in\mathbb R^{n\times n}$ 对称，特征值按递增排列
$$
\lambda_1\le\lambda_2\le\cdots\le\lambda_n ,
$$
对应的正交规范特征向量为 $u_1,\dots,u_n$。记 Rayleigh 商
$$
R(x)=\frac{x^{\mathsf T}Ax}{x^{\mathsf T}x},\qquad x\ne0 .
$$
对 $1\le k\le n$，记 $\mathcal V_k$ 为 $\mathbb R^n$ 中一切 $k$ 维子空间的集合，$\mathcal W_{n-k+1}$ 为一切 $(n-k+1)$ 维子空间的集合。

**定理（Courant–Fischer 极小极大原理）**：
$$
\lambda_k=\min_{V\in\mathcal V_k}\ \max_{0\ne x\in V}R(x)=\max_{W\in\mathcal W_{n-k+1}}\ \min_{0\ne x\in W}R(x).
$$

**推论 1（Rayleigh 原理）**：$k=1$ 与 $k=n$ 给出
$$
\lambda_1=\min_{x\ne0}R(x),\qquad \lambda_n=\max_{x\ne0}R(x).
$$

**推论 2（单调性与 Weyl 不等式）**：若 $B$ 对称，则
$$
\lambda_k(A)+\lambda_1(B)\ \le\ \lambda_k(A+B)\ \le\ \lambda_k(A)+\lambda_n(B).
$$

**推论 3（Cauchy 交错定理）**：设 $A_m$ 是 $A$ 的 $m\times m$ 主子矩阵（$m<n$），其特征值为 $\mu_1\le\cdots\le\mu_m$，则
$$
\lambda_k\le\mu_k\le\lambda_{k+n-m},\qquad k=1,\dots,m .
$$

**推论 4（图 Laplacian 的 $\mu_2$ 刻画）**：设 $L$ 为连通 $d$-正则图的 Laplacian，则
$$
\mu_2=\min_{\substack{\mathbf x\ne0\\ \mathbf x\perp\mathbf 1}}\frac{\mathbf x^{\mathsf T}L\mathbf x}{\mathbf x^{\mathsf T}\mathbf x}.
$$
（式中的最右端即"代数连通度"的变分定义。）

## 四、证明过程

**证明（定理）。** 分两个不等式方向。

**步骤 1（极小子空间给出上界）。** 取 $V_0=\operatorname{span}\{u_1,\dots,u_k\}\in\mathcal V_k$。对 $0\ne x=\sum_{i=1}^{k}c_iu_i$，
$$
R(x)=\frac{\sum_{i=1}^{k}\lambda_ic_i^2}{\sum_{i=1}^{k}c_i^2}\ \le\ \lambda_k ,
$$
故 $\max_{x\in V_0}R(x)\le\lambda_k$，于是
$$
\min_{V\in\mathcal V_k}\max_{x\in V}R(x)\ \le\ \lambda_k .
$$

**步骤 2（维数计数给出下界）。** 任取 $V\in\mathcal V_k$，令 $W_0=\operatorname{span}\{u_k,u_{k+1},\dots,u_n\}$，则 $\dim W_0=n-k+1$。由子空间维数公式
$$
\dim(V\cap W_0)\ \ge\ \dim V+\dim W_0-n=k+(n-k+1)-n=1 ,
$$
故存在 $0\ne x\in V\cap W_0$。写 $x=\sum_{i=k}^{n}c_iu_i$，则
$$
R(x)=\frac{\sum_{i\ge k}\lambda_ic_i^2}{\sum_{i\ge k}c_i^2}\ \ge\ \lambda_k ,
$$
于是 $\max_{x\in V}R(x)\ge\lambda_k$。因 $V$ 任意，
$$
\min_{V\in\mathcal V_k}\max_{x\in V}R(x)\ \ge\ \lambda_k .
$$
两步合起来即得极小极大等式。

**步骤 3（极大极小形式）。** 取 $W_1=\operatorname{span}\{u_k,\dots,u_n\}\in\mathcal W_{n-k+1}$：对 $0\ne x\in W_1$ 由步骤 2 的估计 $R(x)\ge\lambda_k$，故 $\min_{x\in W_1}R\ge\lambda_k$，即 $\max_W\min_{x\in W}R\ge\lambda_k$。反之任取 $W\in\mathcal W_{n-k+1}$，令 $V_1=\operatorname{span}\{u_1,\dots,u_k\}$，则 $\dim(V_1\cap W)\ge1$，取 $0\ne x\in V_1\cap W$，由步骤 1 的估计 $R(x)\le\lambda_k$，故 $\min_{x\in W}R\le\lambda_k$，即 $\max_W\min_{x\in W}R\le\lambda_k$。两步合起来给出极大极小等式。$\square$

**证明（推论 2）。** 由 Courant–Fischer 的极小极大形式，
$$
\lambda_k(A+B)=\min_{V\in\mathcal V_k}\max_{x\in V}\frac{x^{\mathsf T}Ax}{x^{\mathsf T}x}+\frac{x^{\mathsf T}Bx}{x^{\mathsf T}x}
\ \ge\ \min_{V}\max_{x\in V}\Bigl(R_A(x)+\lambda_1(B)\Bigr)=\lambda_k(A)+\lambda_1(B),
$$
（因为 $x^{\mathsf T}Bx/x^{\mathsf T}x\ge\lambda_1(B)$）右边不等式同理由 $\lambda_n(B)$ 给出。$\square$

**证明（推论 3）。** 把 $\mathbb R^m$ 通过坐标嵌入 $\mathbb R^n$（补零），则 $\mu_k=\min_{V\subset\mathbb R^m,\dim V=k}\max_{x\in V}R_A(x)$，把允许的子空间类从 $\mathbb R^m$ 的 $k$ 维子空间放大到 $\mathbb R^n$ 的 $k$ 维子空间，极小值不增，故 $\lambda_k\le\mu_k$。对 $-A$ 与补指标（$m-k+1$ 对应 $n-m+k$）重复同一论证，得 $\mu_k\le\lambda_{k+n-m}$。$\square$

## 五、应用与意义

- **图谱与扩张**：图的第二小 Laplace 特征值 $\mu_2$ 由本定理化为带约束的优化问题，是 Fiedler 向量算法与 [Cheeger不等式](./Cheeger不等式.md) 的出发点。
- **数值线性代数**：子空间迭代、Lanczos 与 Davidson 方法都以极小极大原理为收敛性分析基础；特征值的单调性与扰动界由推论 2 提供。
- **主成分分析与统计**：样本协方差矩阵的主特征向量最大化方差（$k=1$ 情形），后续主成分由 $k=2,3,\dots$ 的极小极大问题给出，决定了降维的最优性。
- **微分算子与 PDE**：Sturm–Liouville 与 Laplace–Beltrami 算子的第 $k$ 个特征值有同型变分刻画，是特征值估计与 nodal 域研究的工具，见 [对称张量的谱定理](../第119级-连续介质力学/对称张量的谱定理.md)。

## 课堂问答

**老师**：Rayleigh 商只给了最小、最大两个特征值，那中间的 $\lambda_k$ 怎么刻画？

**学生**：用子空间维数。$\lambda_k=\min_{V\in\mathcal{V}_k}\max_{0\ne x\in V}R(x)=\max_{W\in\mathcal{W}_{n-k+1}}\min_{0\ne x\in W}R(x)$，其中 $R(x)=\frac{x^TAx}{x^Tx}$，$\mathcal{V}_k$ 是全部 $k$ 维子空间的集合。$k=1$ 退化为 $\lambda_1=\min R$，$k=n$ 退化为 $\lambda_n=\max R$。

**老师（追问）**：两个方向的证明分别靠什么？

**学生**：上界取"顺最优子空间" $V_0=\operatorname{span}\{u_1,\dots,u_k\}$，其中 $R(x)\le\lambda_k$，故极小值 $\le\lambda_k$；下界靠维数计数：任何 $k$ 维子空间 $V$ 与 $W_0=\operatorname{span}\{u_k,\dots,u_n\}$ 必有交（$\dim(V\cap W_0)\ge k+(n-k+1)-n=1$），交中向量满足 $R(x)\ge\lambda_k$，故极小值 $\ge\lambda_k$。两个方向合并即得。这正是 Cheeger 不等式中 $\mu_2=\min_{\mathbf{x}\perp\mathbf{1}}\frac{\mathbf{x}^TL\mathbf{x}}{\|\mathbf{x}\|^2}$ 的来源。

**老师（拓展）**：这条变分原理能推出哪些有用推论？

**学生**：至少三条：单调性与 Weyl 不等式 $\lambda_k(A)+\lambda_1(B)\le\lambda_k(A+B)\le\lambda_k(A)+\lambda_n(B)$；Cauchy 交错定理 $\lambda_k\le\mu_k\le\lambda_{k+n-m}$（主子矩阵特征值交错）；以及特征值扰动界。它们让子空间迭代、Lanczos 与主成分分析（$k=1$ 最大化方差）都有严格的最优性依据。

## 相关条目

- [图的谱定理](./图的谱定理.md)：对称/正规矩阵的谱分解，是本定理的前提。
- [Cheeger不等式](./Cheeger不等式.md)：用 $\mu_2$ 的极小极大刻画夹逼等周常数。
- [Perron-Frobenius定理](./Perron-Frobenius定理.md)：非负矩阵最大特征值的变分刻画（Collatz–Wielandt 公式）与本定理平行。
- [Rayleigh商的变分原理](../第31级-泛函分析/Rayleigh商的变分原理.md)：本定理在 Hilbert 空间自伴算子上的推广形式。
- [对称张量的谱定理](../第119级-连续介质力学/对称张量的谱定理.md)：连续介质力学中特征值变分刻画的用法。
