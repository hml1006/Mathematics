# Zadeh扩展原理

> **一句话大白话**：把经典函数"搬"到模糊集上：输入是一个边界模糊的"云"（模糊集）时，原理规定输出每一处的浓淡，等于所有能投影到那里的输入点的最大浓淡——经典运算因此可以原封不动地用在模糊数上。
>
> **小例子**：经典加法的模糊版，"大约 3"加"大约 5 ≈ 大约 8"，关键公式是 $\tilde f(A)(y)=\sup_{x:f(x)=y}\mu_A(x)$，即"输出点 $y$ 的隶属度 = 能通过 $f$ 到达 $y$ 的输入点的隶属度上确界"。

## 一、定理介绍

Zadeh 扩展原理把经典映射 $f:X\to Y$ 提升为模糊集之间的映射，使经典数学结构可整体移植到模糊框架。若 $A\in\mathcal F(X)$（$X$ 上模糊集），则
$$
\tilde f(A)(y)=\sup_{x\in f^{-1}(y)}\mu_A(x),\quad(\text{若 }f^{-1}(y)=\emptyset\text{ 则取 }0),
$$
对 $B\in\mathcal F(Y)$，$\tilde f^{-1}(B)(x)=\mu_B(f(x))$。由此模糊数等对象的四则运算可由经典对应运算逐点定义。

## 二、原理思路

原理依托"逐点最大关于取原像"的哲学：$f(A)$ 在某点 $y$ 的隶属度应"继承"所有能映射到 $y$ 的输入点的隶属度，取这些来源中最强的（上确界）。对 $\tilde f^{-1}$，原象天然逐点继承目标隶属度，所以是直接复合。这样扩展出的映射保留模糊集的包含、并与交等结构关系（$\tilde f$ 保持并，$\tilde f^{-1}$ 同时保持并与交、补），从而具有"良定义 + 次可加/保结构"的双重良好性。

## 三、定理的严格表述

设 $f:X\to Y$ 为普通映射，则：

1. $\tilde f:\mathcal F(X)\to\mathcal F(Y)$，$\tilde f(A)(y)=\begin{cases}\sup_{f^{-1}(y)}\mu_A,&f^{-1}(y)\ne\emptyset\\0,&f^{-1}(y)=\emptyset\end{cases}$；
2. $\tilde f^{-1}:\mathcal F(Y)\to\mathcal F(X)$，$\tilde f^{-1}(B)(x)=\mu_B(f(x))$。

并满足：$\tilde f(\bigcup_iA_i)=\bigcup_i\tilde f(A_i)$；$\tilde f^{-1}$ 保并与交与补；伴随关系 $\tilde f(A)\subseteq B\iff A\subseteq\tilde f^{-1}(B)$。

## 四、证明过程

**步骤1：验证良定义。** 对任意 $y$，若 $f^{-1}(y)\ne\emptyset$，$0\le\sup_{x\in f^{-1}(y)}\mu_A(x)\le1$，故 $\tilde f(A):Y\to[0,1]$，即 $\tilde f(A)\in\mathcal F(Y)$；$\tilde f^{-1}(B)$ 同理是 $X$ 上模糊集。

**步骤2：$\tilde f$ 保持并。** 由交换 sup 次序，
$$
\tilde f(\bigcup_iA_i)(y)=\sup_{f^{-1}(y)}\sup_i\mu_{A_i}(x)=\sup_i\sup_{f^{-1}(y)}\mu_{A_i}(x)=\big(\bigcup_i\tilde f(A_i)\big)(y).
$$

**步骤3：交的关系。** 一般 $\tilde f(\bigcap_iA_i)\subseteq\bigcap_i\tilde f(A_i)$，$f$ 为单射时取等（因 $f^{-1}(y)$ 至多单点）。

**步骤4：$\tilde f^{-1}$ 保结构。** $\tilde f^{-1}(B\cup C)(x)=\mu_{B\cup C}(f(x))=\max(\mu_B(f(x)),\mu_C(f(x)))(=\tilde f^{-1}(B)\cup\tilde f^{-1}(C))(x)$；交、补同理。

**步骤5：伴随关系。** $\tilde f(A)\subseteq B\iff\forall y,\sup_{f^{-1}(y)}\mu_A\le\mu_B(y)\iff\forall x,\mu_A(x)\le\mu_B(f(x))\iff A\subseteq\tilde f^{-1}(B)$。

**步骤6：扩展到模糊关系。** 诱导模糊关系 $R_f$（当 $y=f(x)$ 取 1，否则 0），扩展原理可视作经 $R_f$ 的模糊推理，推广到模糊关系合成。

**结论（$\square$）**：$f$ 良定地扩展为 $\tilde f,\tilde f^{-1}$ 并保持基本模糊集运算。

## 五、应用与意义

Zadeh 扩展原理是模糊数学的连接枢纽：它把确定性运算（加减乘除、函数求值）整体提升到模糊数/模糊集合，从而支撑模糊算术、模糊方程与模糊优化。它也是模糊控制中规则库在真值空间投影、模糊信息处理的理论基础。