# 非标准测度论中的Loeb测度构造

> **一句话大白话**：把一个内部（非标准）测度 $\mu$ 对每个集合取标准部分 $\text{st}(\mu(A))$，就能"洗"出一个普通的标准测度 $\mu_L$，它记下每个集合"真实的大小"，可测集的家族也自动扩成一个 $\sigma$-代数。这就像把一把用超级分的"非标尺" 换算成普通尺——每段长度取标准读数，整体就变成一把能严格做概率的普通尺。
>
> **小例子**：在二进制序列空间 $\{0,1\}^{\mathbb{N}}$ 上，取无限大的 $N$ 与有限空间 $X_N=\{0,1\}^N$ 及其均匀测度 $\mu_N$（每点测度 $2^{-N}$）。定义 $\mu(A)=|A|/2^N$，则 Loeb 测度 $\mu_L$ 对任一标准柱集 $C=\{x:x_1=a_1,\dots,x_k=a_k\}$ 给出 $\mu_L(C)=2^{-k}$，恰为标准的独立均匀乘积测度。无限大的硬币试验由此有了严谨的概率模型。

## 一、定理介绍

Loeb 测度构造（Loeb Measure Construction）是 Peter Loeb（1975）提出的非标准测度论核心方法：由内部测度空间 $(X,\mathcal{A},\mu)$——其中 $\mu$ 取值于超实数 $^*[0,\infty]$——通过逐点取标准部分得到前测度 $\mu_L^0$，再由 Carathéodory 扩张得到标准 $\sigma$-有限测度 $\mu_L$。它把非标准的"计数/均匀"结构转化为经典测度论中的可用对象，是现代随机过程、遍历论与随机分析（尤其 Wiener 测度与 Itô 积分）的非标准工具基础。

## 二、原理思路

关键是把"取标准部分"与"测度扩张"两步结合：（1）在内部代数 $\mathcal{A}$ 上把 $\mu_L^0(A)=\text{st}(\mu(A))$ 定义为一个取值于 $[0,\infty]$ 的前测度，利用无限小之和仍为无限小验证有限可加性；（2）验证 $\sigma$-可加性，其中可数并需要依赖内部测度与超滤/饱和性处理"无限大自然"的边界情形；（3）由 Carathéodory 扩张定理把 $\mu_L^0$ 唯一地扩张到 $\sigma(\mathcal{A})$。

## 三、定理的严格表述

**定理（Loeb 测度构造）**：设 $(X,\mathcal{A},\mu)$ 是内部测度空间，$\mu$ 为有限内部测度（即 $\mu(X)$ 是有限超实数）。则存在标准测度空间 $(X,\mathcal{A}_L,\mu_L)$，使得：
1. $\mathcal{A}_L$ 是包含 $\mathcal{A}$ 的 $\sigma$-代数（可取 $\sigma(\mathcal{A})$）；
2. $\mu_L$ 是 $\mathcal{A}_L$ 上的 $\sigma$-有限测度；
3. 对任意 $A\in\mathcal{A}$，$\mu_L(A)=\text{st}(\mu(A))$。

## 四、证明过程

**证明（前测度加 Carathéodory 扩张）**：

**步骤1（定义前测度）**：在 $\mathcal{A}$ 上定义 $\mu_L^0(A)=\text{st}(\mu(A))$，其中 $\text{st}$ 为标准部分函数。

**步骤2（验证有限可加性）**：对不相交 $A,B\in\mathcal{A}$，因 $\mu$ 是内部测度，$\mu(A\cup B)=\mu(A)+\mu(B)$。取标准部分：
$$
\mu_L^0(A\cup B)=\text{st}\bigl(\mu(A)+\mu(B)\bigr)=\text{st}(\mu(A))+\text{st}(\mu(B))=\mu_L^0(A)+\mu_L^0(B),
$$
因 $\mu(A),\mu(B)$ 有限且两个无限小之和仍为无限小。

**步骤3（验证 $\sigma$-可加性）**：设 $\{A_n\}_{n\in\mathbb{N}}\subset\mathcal{A}$ 两两不相交且 $\bigcup_{n=1}^{\infty}A_n\in\mathcal{A}$，需证
$$
\mu_L^0\biggl(\bigcup_{n=1}^{\infty}A_n\biggr)=\sum_{n=1}^{\infty}\mu_L^0(A_n).
$$
**步骤4（单调性与下界）**：对任意 $N$，$\bigcup_{n=1}^{N}A_n\subseteq\bigcup_{n=1}^{\infty}A_n$，故 $\mu\bigl(\bigcup_{n=1}^{N}A_n\bigr)\le\mu\bigl(\bigcup_{n=1}^{\infty}A_n\bigr)$，取标准部分得
$$
\sum_{n=1}^{N}\mu_L^0(A_n)\le\mu_L^0\biggl(\bigcup_{n=1}^{\infty}A_n\biggr),
$$
令 $N\to\infty$ 得 $\le$ 方向。

**步骤5（反向不等式）**：设 $B=\bigcup_{n=1}^{\infty}A_n$，考虑
$$
S=\{n\in{}^*\mathbb{N}:\mu\bigl(B\setminus\bigcup_{k=1}^{n}A_k\bigr)>0\}.
$$
若 $S$ 含所有标准自然数，则存在无限大 $\nu$ 使 $\mu(B\setminus\bigcup_{k=1}^{\nu}A_k)>0$；但由内部测度性质，$B\setminus\bigcup_{k=1}^{\nu}A_k$ 是无限小（对无限大 $\nu$ 而言），其内部测度为无限小，矛盾。故 $\mu_L^0(B\setminus\bigcup_{k=1}^{n}A_k)\to0$，由此 $\ge$ 方向成立，$\sigma$-可加性得证。

**步骤6（Carathéodory 扩张）**：由 Carathéodory 扩张定理，$\mu_L^0$ 唯一地扩张到 $\mathcal{A}_L=\sigma(\mathcal{A})$ 上，得到 $\sigma$-有限测度 $\mu_L$，且对内部可测集满足 $\mu_L(A)=\text{st}(\mu(A))$。$\square$

**步骤7（性质）**：Loeb 测度 $\mu_L$ 是完备的（所有 $\mu_L$-零测集的子集均可测）；外部集虽非内部集，仍可为 Loeb 可测。

## 五、应用与意义

Loeb 测度为非标准分析架起通往概率论与随机分析的桥梁：它从超限均匀结构构造出标准乘积测度与 Wiener 测度，是构造 Brown 运动、Itô 积分与遍历论模型的非标准基础。Loeb 测度兼具"内部测度的组合便利"与"标准测度的可测性严谨"，已成为非标准测度论、随机分析与动力系统研究中不可替代的工具。