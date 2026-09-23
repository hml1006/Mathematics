# Cayley-Hamilton 定理

> **一句话大白话**：每个方阵都是"自己特征多项式的根"——把矩阵本身代进它的特征多项式里算，结果恰好是零矩阵。

> **小例子**：二阶矩阵 $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ 的特征多项式为 $p(\lambda)=\lambda^2-5\lambda-2$，于是 $A^2-5A-2I=0$；由此可将任意高次幂 $A^k$ 用 $I,A$ 线性表示。

## 一、定理介绍

> **前置依赖**：行列式展开定理、行列式乘积定理、矩阵的迹、可逆矩阵等价条件。

Cayley–Hamilton 定理是线性代数中连接矩阵、特征多项式与矩阵代数的核心命题：任意 $n$ 阶方阵都满足自身的特征多项式方程。它意味着矩阵幂序列 $\{I,A,A^2,\dots\}$ 只有 $n$ 个线性无关元素，因此任何矩阵解析函数（如矩阵指数 $e^{At}$）都可由 $I,A,\dots,A^{n-1}$ 线性组合表示。

在控制理论中，该定理是把能控性、能观性判据从"无穷多个方向"压缩为"前 $n$ 个方向"的代数依据。

## 二、原理思路

设 $p_A(\lambda)=\det(\lambda I-A)$ 为 $A$ 的特征多项式。证明 $p_A(A)=0$ 有两条经典路线：

1. **对角化情形**：若 $A=P\Lambda P^{-1}$（$\Lambda$ 对角），则 $p_A(A)=P\,p_A(\Lambda)\,P^{-1}$，而对角矩阵的每个对角元 $\lambda_i$ 都满足 $p_A(\lambda_i)=0$，立得结论。
2. **一般情形（伴随矩阵法）**：把 $\mathrm{adj}(\lambda I-A)$ 写成关于 $\lambda$ 的矩阵多项式 $\sum_{k=0}^{n-1}\lambda^kB_k$，利用恒等式 $\mathrm{adj}(\lambda I-A)(\lambda I-A)=p_A(\lambda)I$ 比较 $\lambda$ 各次幂的系数，得到一族**常数矩阵**恒等式，再左乘 $A^k$ 求和即可整体相消。

路线 2 不依赖对角化，对任意方阵成立，下面采用它。

## 三、定理的严格表述

设 $A\in\mathbb{R}^{n\times n}$，其特征多项式为

$$
p_A(\lambda)=\det(\lambda I-A)=\lambda^n+a_{n-1}\lambda^{n-1}+\cdots+a_1\lambda+a_0 .
$$

其中 $a_{n-1}=-\operatorname{tr}A$，$a_0=(-1)^n\det A$。

**定理（Cayley–Hamilton）**：$A$ 满足自身的特征多项式，即

$$
p_A(A)=A^n+a_{n-1}A^{n-1}+\cdots+a_1A+a_0I=0 .
$$

**推论**：

1. $A$ 的最小多项式 $m_A$ 整除特征多项式 $p_A$。
2. 对任意 $k\ge0$，$A^k$ 是 $I,A,\dots,A^{n-1}$ 的常系数线性组合；等价地，$\{I,A,\dots,A^{n-1}\}$ 张成矩阵代数 $\mathbb{R}[A]$。
3. 若 $A$ 可逆，则 $A^{-1}=-\dfrac{1}{a_0}\bigl(A^{n-1}+a_{n-1}A^{n-2}+\cdots+a_1I\bigr)$，故 $A^{-1}\in\mathbb{R}[A]$。

## 四、证明过程

**引理（伴随矩阵恒等式）**：对任意方阵 $M$，$\mathrm{adj}(M)\,M=\det(M)\,I$。特别地取 $M=\lambda I-A$，得

$$
\mathrm{adj}(\lambda I-A)\,(\lambda I-A)=p_A(\lambda)\,I .
$$

这是伴随矩阵的基本性质，可直接由行列式展开定理（按行展开）验证。

**主证明**。由行列式展开定理，$\mathrm{adj}(\lambda I-A)$ 的每个元素都是关于 $\lambda$ 的、次数不超过 $n-1$ 的多项式，因此可唯一写成

$$
\mathrm{adj}(\lambda I-A)=\sum_{k=0}^{n-1}\lambda^k B_k,\qquad B_k\in\mathbb{R}^{n\times n}\ \text{为常矩阵}.
$$

把 $p_A(\lambda)=\sum_{k=0}^{n}a_k\lambda^k$（其中 $a_n=1$）与上式代入引理，得矩阵多项式恒等式

$$
\left(\sum_{k=0}^{n-1}\lambda^kB_k\right)(\lambda I-A)=\sum_{k=0}^{n}a_k\lambda^k\,I .
$$

左端展开为 $\sum_{k=0}^{n-1}\lambda^{k+1}B_k-\sum_{k=0}^{n-1}\lambda^k A B_k$。比较 $\lambda$ 的各次幂系数（约定 $B_{-1}=B_n=0$），得到 $n+1$ 个**常数矩阵**等式

$$
B_{k-1}-A B_k=a_k I,\qquad k=0,1,\dots,n .
$$

现对第 $k$ 式左乘 $A^k$：

$$
A^kB_{k-1}-A^{k+1}B_k=a_kA^k.
$$

对 $k=0,1,\dots,n$ 求和。左端为

$$
\sum_{k=0}^{n}A^kB_{k-1}-\sum_{k=0}^{n}A^{k+1}B_k
=\sum_{j=0}^{n-1}A^{j+1}B_j-\sum_{j=0}^{n-1}A^{j+1}B_j=0,
$$

其中两个求和的指标替换利用了 $B_{-1}=0$ 与 $B_n=0$。右端为

$$
\sum_{k=0}^{n}a_kA^k=p_A(A).
$$

因此 $p_A(A)=0$，定理得证。$\square$

**另证（可对角化情形的直接验证）**。若 $A=P\Lambda P^{-1}$，$\Lambda=\mathrm{diag}(\lambda_1,\dots,\lambda_n)$，则对任意多项式 $q$ 有 $q(A)=P\,q(\Lambda)\,P^{-1}$。由 $\det(\lambda_iI-A)=0$ 知 $p_A(\lambda_i)=0$，故 $p_A(\Lambda)=0$，从而 $p_A(A)=0$。又因具有互异特征值的矩阵在 $\mathbb{R}^{n\times n}$ 中稠密，而 $A\mapsto p_A(A)$ 关于矩阵元素连续，一般情形由连续性延拓得到。

**推论的证明**。由 $p_A(A)=0$ 且 $p_A$ 的首项系数为 $1$，最小多项式 $m_A$ 是使 $m_A(A)=0$ 的最低次首一多项式，故 $m_A\mid p_A$。又 $A^n=-\sum_{k<n}a_kA^k$，逐次递推即可把 $A^k$（$k\ge n$）降次。若 $A$ 可逆则 $a_0=(-1)^n\det A\ne0$，由 $A\bigl(A^{n-1}+a_{n-1}A^{n-2}+\cdots+a_1I\bigr)=-a_0I$ 得推论 3。$\square$

## 五、应用与意义

- **矩阵函数计算**：$e^{At}=\sum_{k\ge0}t^kA^k/k!$ 经定理可化为 $\sum_{k=0}^{n-1}c_k(t)A^k$，是求解线性系统状态响应与计算矩阵指数的标准方法。
- **能控性与能观性**：只需检验 $\{B,AB,\dots,A^{n-1}B\}$ 与 $\{C,CA,\dots,CA^{n-1}\}$ 的秩，即可判定系统能控、能观。
- **最小多项式与标准形**：定理给出特征多项式与最小多项式的整除关系，是 Jordan 标准形与有理标准形分类的代数基础。
- **递推与快速幂**：由 $A^k$ 的降次关系可得线性递推（如 Fibonacci），并支持 $O(\log k)$ 的快速幂计算。
