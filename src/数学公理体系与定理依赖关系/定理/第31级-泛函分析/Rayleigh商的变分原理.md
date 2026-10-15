# Rayleigh 商的变分原理

> **一句话大白话**：自伴算子的最大、最小特征值，正好是 Rayleigh 商在单位球上的最大、最小值——求特征值可以变成求函数的极值。
>
> **小例子**：对实对称矩阵 $A$，$\lambda_{\min}=\min_{x\ne0}\frac{x^{\top}Ax}{x^{\top}x}$、$\lambda_{\max}=\max_{x\ne0}\frac{x^{\top}Ax}{x^{\top}x}$，极值在对应特征向量处取得。

## 介绍

Rayleigh 商的变分原理源于 Lord Rayleigh 对振动系统频率的研究，后由 Ritz、Courant、Fischer 等人发展成完整的极值刻画。它把自伴算子的特征值问题转化为二次型的极值问题：算子的 Rayleigh 商

$$R(x)=\frac{\langle Ax,x\rangle}{\langle x,x\rangle}$$

的极值恰由算子的谱给出。最小、最大（按序）特征值分别是 Rayleigh 商在单位球上的下确界与上确界。

这一原理是变分法与谱理论的桥头堡。在偏微分方程中，它把求特征值（如 Sturm–Liouville 问题、Laplace 算子的第一特征值）转化为能量泛函的极小化；在数值计算中，它给出幂法、Rayleigh 商迭代等算法；在量子力学中，基态能量即 Hamilton 算子的最小 Rayleigh 商。

Courant–Fischer 极小极大原理是其精细形式，把每一个特征值（而不只是首末两个）都写成特定维数子空间上的极值。

## 分析

**前置依赖**：自伴（Hermite）算子、谱定理（紧自伴算子）、特征值与特征向量、正交基展开、二次型的取值、极值的取得（紧性）

**定理内容（有限维版本）**：设 $A$ 是 $n$ 维内积空间上的自伴算子，特征值按大小排列为

$$\lambda_1\le\lambda_2\le\cdots\le\lambda_n,$$

对应正交单位特征向量 $v_1,\dots,v_n$。则对一切 $x\ne0$，

$$\lambda_1\le\frac{\langle Ax,x\rangle}{\langle x,x\rangle}\le\lambda_n,$$

且下、上确界分别在 $x\perp\operatorname{span}\{v_1\}$ 之外的 $v_1$ 与 $v_n$ 处取得，即

$$\lambda_1=\min_{x\ne0}\frac{\langle Ax,x\rangle}{\langle x,x\rangle},\qquad \lambda_n=\max_{x\ne0}\frac{\langle Ax,x\rangle}{\langle x,x\rangle}.$$

**定理内容（Courant–Fischer 极小极大原理）**：记 $\mathcal V_k$ 为一切 $k$ 维子空间，则

$$\lambda_k=\min_{V\in\mathcal V_k}\ \max_{0\ne x\in V}\frac{\langle Ax,x\rangle}{\langle x,x\rangle}=\max_{W\in\mathcal V_{n-k+1}}\ \min_{0\ne x\in W}\frac{\langle Ax,x\rangle}{\langle x,x\rangle}.$$

**关键要点**：

- 若 $A$ 是紧自伴算子（无穷维），特征值 $\lambda_k\to0$，上述极小极大刻画给出所有特征值，最值仍在特征向量处取得；
- 极值的取得依赖单位球在相应有限维子空间（或紧算子情形）上的紧性；
- 自伴性是本质的，非自伴算子的 Rayleigh 商可能取复值且不反映特征值。

## 思考过程

核心观察是：自伴算子的二次型在正交特征基下变成对角形式。既然 $A$ 有正交单位特征基 $\{v_i\}$，任何 $x$ 都可以展开为 $x=\sum_i c_i v_i$，于是

$$\langle Ax,x\rangle=\sum_i \lambda_i|c_i|^2,\qquad \langle x,x\rangle=\sum_i|c_i|^2.$$

Rayleigh 商因此是以 $|c_i|^2$ 为权的特征值加权平均，必然夹在 $\lambda_1$ 与 $\lambda_n$ 之间；取权集中在 $v_1$ 或 $v_n$ 上即可达到两端。这既给出了不等式，也给出了极值点。

Courant–Fischer 的思想是"用子空间维数对特征值排序"：要让 Rayleigh 商整体偏小，就选 $k$ 维子空间并看它里面的最大值；这个最大值的下确界只能由"装得下前 $k$ 个特征方向"的子空间达到，于是等于 $\lambda_k$。证明的关键是维数计数：$k$ 维子空间必与 $\operatorname{span}\{v_k,\dots,v_n\}$（维数 $n-k+1$）相交非零。

## 证明过程

**步骤 1：对角化二次型。** 由谱定理，自伴算子 $A$ 存在正交单位特征基 $v_1,\dots,v_n$，对应实特征值 $\lambda_1\le\cdots\le\lambda_n$。对 $x=\sum_i c_i v_i$（$c_i=\langle x,v_i\rangle$），

$$\langle Ax,x\rangle=\Big\langle\sum_i c_i\lambda_i v_i,\sum_j c_j v_j\Big\rangle=\sum_{i=1}^n\lambda_i|c_i|^2,\qquad \langle x,x\rangle=\sum_{i=1}^n|c_i|^2.$$

**步骤 2：加权平均估计。** 因 $\lambda_1\le\lambda_i\le\lambda_n$，

$$\lambda_1\sum_i|c_i|^2\le\sum_i\lambda_i|c_i|^2\le\lambda_n\sum_i|c_i|^2,$$

除以 $\sum_i|c_i|^2=\|x\|^2>0$ 得

$$\lambda_1\le\frac{\langle Ax,x\rangle}{\langle x,x\rangle}\le\lambda_n.$$

**步骤 3：极值可达。** 取 $x=v_1$，则 $\langle Av_1,v_1\rangle=\lambda_1\|v_1\|^2$，商为 $\lambda_1$；取 $x=v_n$ 得商为 $\lambda_n$。结合步骤 2，即得最小值为 $\lambda_1$、最大值为 $\lambda_n$。

**步骤 4：Courant–Fischer 上界方向。** 取 $V_0=\operatorname{span}\{v_1,\dots,v_k\}\in\mathcal V_k$。对 $0\ne x\in V_0$，展开后只有 $i\le k$ 的项非零，故

$$\frac{\langle Ax,x\rangle}{\langle x,x\rangle}=\frac{\sum_{i\le k}\lambda_i|c_i|^2}{\sum_{i\le k}|c_i|^2}\le\lambda_k.$$

于是 $\min_{V\in\mathcal V_k}\max_{0\ne x\in V}(\cdots)\le\lambda_k$。

**步骤 5：Courant–Fischer 下界方向与维数计数。** 任取 $V\in\mathcal V_k$。考虑子空间 $U=\operatorname{span}\{v_k,v_{k+1},\dots,v_n\}$，$\dim U=n-k+1$。由维数公式 $\dim(V\cap U)\ge k+(n-k+1)-n=1$，故存在 $0\ne x\in V\cap U$。对此 $x$，展开式中只有 $i\ge k$ 的项非零，故

$$\frac{\langle Ax,x\rangle}{\langle x,x\rangle}=\frac{\sum_{i\ge k}\lambda_i|c_i|^2}{\sum_{i\ge k}|c_i|^2}\ge\lambda_k.$$

因此 $\max_{0\ne x\in V}(\cdots)\ge\lambda_k$，对一切 $V\in\mathcal V_k$ 成立，取下确界得

$$\min_{V\in\mathcal V_k}\ \max_{0\ne x\in V}\frac{\langle Ax,x\rangle}{\langle x,x\rangle}\ge\lambda_k.$$

与步骤 4 合并即得第一式。第二式由对 $-A$ 应用第一式（特征值变号、序颠倒）得到。$\square$

**步骤 6：紧自伴算子情形（附注）。** 若 $A$ 是 Hilbert 空间上的紧自伴算子，则 $A$ 有可列个实特征值 $\lambda_1\ge\lambda_2\ge\cdots\to0$（按绝对值排列）及对应的正交特征向量；此时

$$\lambda_1=\max_{\|x\|=1}\langle Ax,x\rangle,\qquad \lambda_k=\max_{x\perp v_1,\dots,v_{k-1},\ \|x\|=1}\langle Ax,x\rangle,$$

极值由紧性（单位球在有限维投影下相对紧）保证可取得。这正是 Rayleigh–Ritz 方法与 Sturm–Liouville 特征展开的基础。

## 课堂问答

**老师**：Rayleigh 商与自伴算子的特征值有什么联系？

**学生**：$\lambda_1=\min_{x\ne0}\frac{\langle Ax,x\rangle}{\langle x,x\rangle}$、$\lambda_n=\max_{x\ne0}\frac{\langle Ax,x\rangle}{\langle x,x\rangle}$，极值在对应特征向量处取得。更精细地，Courant-Fischer 给出 $\lambda_k=\min_{V\in\mathcal{V}_k}\max_{0\ne x\in V}R(x)$，其中 $\mathcal{V}_k$ 为一切 $k$ 维子空间。

**老师（追问）**：为什么 Rayleigh 商必落在 $\lambda_1$ 与 $\lambda_n$ 之间？

**学生**：在正交特征基下 $x=\sum_ic_iv_i$，于是 $R(x)=\frac{\sum_i\lambda_i|c_i|^2}{\sum_i|c_i|^2}$，这是以 $|c_i|^2$ 为权的特征值加权平均，自然夹在最小与最大之间；取 $x=v_1$ 或 $x=v_n$ 达到两端。

**老师（拓展）**：Courant-Fischer 的维数论证怎么走？

**学生**：任取 $k$ 维子空间 $V$，它与 $\operatorname{span}\{v_k,\dots,v_n\}$（维数 $n-k+1$）必有非零交，交中任一 $x$ 给 $R(x)\ge\lambda_k$，故 $\max_VR\ge\lambda_k$；取 $V=\operatorname{span}\{v_1,\dots,v_k\}$ 得 $\le\lambda_k$。注意自伴性是本质的，非自伴算子的 Rayleigh 商可能取复值且不反映特征值。

## 相关条目

- [谱定理紧自伴算子](./谱定理紧自伴算子.md)：提供正交特征基，是本变分原理展开二次型的前提。
- [有界算子的谱定理](./有界算子的谱定理.md)：把 Rayleigh 商的最值推广为谱的上下确界。
