# Weitzenböck公式

> **一句话大白话**：同一个"拉普拉斯型"算子用不同方式写出来会相差一个纯曲率项；几何上的弯曲就藏在这两种写法的差额里。

> **小例子**：对 1-形式 $\alpha$，$\Delta_H\alpha=\nabla^*\nabla\alpha+\mathrm{Ric}(\alpha,\cdot)$；在平坦的 $\mathbb R^n$ 上 $\mathrm{Ric}=0$，两种拉普拉斯算子完全一致。

## 介绍

Weitzenböck 公式由奥地利数学家 Roland Weitzenböck 在 1923 年研究旋量场时给出，后经 Bochner、Lichnerowicz、Gårding 等人推广。它断言：Hodge–de Rham 拉普拉斯算子 $\Delta_H=\mathrm d\delta+\delta\mathrm d$ 与联络拉普拉斯算子 $\nabla^*\nabla$（"粗糙拉普拉斯"）只相差一个由曲率构成的零阶算子，即 $\Delta_H=\nabla^*\nabla+\mathcal R$。这个恒等式是黎曼几何与指标理论的枢纽。它的作用在于：$\Delta_H$ 的核是调和形式（其维数就是 Betti 数），而 $\nabla^*\nabla$ 的核是平行形式（往往只有常数）；Weitzenböck 项 $\mathcal R$ 定量刻画了两者的差别。当曲率项正定（例如 $\mathrm{Ric}>0$ 且讨论 1-形式），由最大值原理便可知没有非平凡调和形式，得到 Bochner 消没定理。对旋量丛则得到 Lichnerowicz 公式 $D^2=\nabla^*\nabla+\frac{1}{4}\mathrm{Scal}$，它是 Lichnerowicz 特征值估计、Atiyah–Singer 指标定理与 Seiberg–Witten 理论中"曲率强制指标消失"的技术核心。

## 分析

**前置依赖**：黎曼联络与协变导数、外微分与余微分、Hodge Laplacian、Riemann曲率张量的对称性、Clifford 代数与 Dirac 算子、Bochner 公式。

**定理内容**：设 $(M^n,g)$ 为黎曼流形，$\Omega^p(M)$ 为 $p$-形式丛，$\nabla$ 为诱导的 Levi-Civita 联络，$\nabla^*$ 为其 $L^2$ 形式伴随。则存在由 Riemann 曲率张量代数地定义的零阶自伴端同态 $\mathcal R_p\in\mathrm{End}(\Omega^p)$，使

$$
\Delta_H\alpha=\nabla^*\nabla\alpha+\mathcal R_p(\alpha),\qquad \alpha\in\Omega^p(M).
$$

对 $p=1$，曲率项就是 Ricci 曲率（视 $\mathrm{Ric}$ 为 $\Omega^1$ 上的端同态）。在自旋流形上还有 Lichnerowicz 公式

$$
D^2=\nabla^*\nabla+\frac{\mathrm{Scal}}{4},
$$

其中 $D$ 是 Dirac 算子，$\mathrm{Scal}$ 是数量曲率。

**推论**：若 $\mathrm{Ric}>0$ 且 $\alpha$ 是调和 1-形式，则在紧流形上 $\alpha=0$，从而 $b_1(M)=0$。

## 思考过程

关键认识是：$\Delta_H=\mathrm d\delta+\delta\mathrm d$ 与 $\nabla^*\nabla$ 都是"二阶"算子，它们的差因而形式上是一阶算子的组合；但曲率正是"二阶协变导数的交换子"，于是差实际上降为零阶。证明策略是取一点处的标准正交标架（$\nabla_i e_j=0$），把 $\mathrm d$ 与 $\delta$ 用 $\nabla$ 和楔积/内乘表示，再展开 $\Delta_H$，把 $\nabla_i\nabla_i$ 项凑成 $\nabla^*\nabla=-\sum_i\nabla_i\nabla_i$，剩下的就是用 Ricci 恒等式产生的曲率项。难点只在把曲率项的指标仔细收缩成 $\mathcal R_p$ 的规范形式。

## 证明过程

**步骤 1：取测地标架与局部表达式。** 在点 $p$ 取标准正交标架 $\{e_1,\dots,e_n\}$ 使 $\nabla_i e_j=0$，记 $\nabla_i=\nabla_{e_i}$。约定 $R(X,Y)=\nabla_X\nabla_Y-\nabla_Y\nabla_X-\nabla_{[X,Y]}$，$R_{ijkl}=\langle R(e_i,e_j)e_k,e_l\rangle$。

**步骤 2：$\mathrm d$ 与 $\delta$ 的局部形式。** 对 $p$-形式 $\alpha$，

$$
\mathrm d\alpha=\sum_i e_i\wedge\nabla_i\alpha,\qquad \delta\alpha=-\sum_i\iota_{e_i}\nabla_i\alpha,
$$

后者来自 $\nabla$ 与度量相容以及 $\nabla^*=-\sum_i\nabla_i$ 作用于取值于 $\Omega^p$ 的张量。

**步骤 3：展开 $\Delta_H$。** 计算

$$
\Delta_H\alpha=\mathrm d\delta\alpha+\delta\mathrm d\alpha
=\sum_{i,j}\Big(-e_i\wedge\nabla_i\big(\iota_{e_j}\nabla_j\alpha\big)-\iota_{e_i}\nabla_i\big(e_j\wedge\nabla_j\alpha\big)\Big).
$$

利用形式的 Clifford 关系 $e_i\wedge\iota_{e_j}+\iota_{e_j}e_i\wedge=\delta_{ij}$ 以及 $\nabla_i\nabla_j=\nabla_j\nabla_i+R_{ij}$（Ricci 恒等式，$R_{ij}$ 表示曲率算子），化简得

$$
\Delta_H\alpha=-\sum_i\nabla_i\nabla_i\alpha+\sum_{i,j}e_i\wedge\iota_{e_j}R_{ij}\alpha .
$$

**步骤 4：识别粗糙拉普拉斯与曲率项。** 令联络拉普拉斯

$$
\nabla^*\nabla\alpha=-\sum_i\nabla_i\nabla_i\alpha,
$$

并定义曲率端同态

$$
\mathcal R_p(\alpha):=\sum_{i,j}e_i\wedge\iota_{e_j}\,R_{ij}\alpha .
$$

则步骤 3 给出

$$
\Delta_H\alpha=\nabla^*\nabla\alpha+\mathcal R_p(\alpha).
$$

**步骤 5：$p=1$ 时曲率项就是 Ricci。** 对 1-形式 $\alpha=\sum_k\alpha_k e^k$，利用 $R_{ij}e^k=\sum_l R_{ijk}{}^l e^l$ 与 $\mathrm{Ric}_{jl}=\sum_i R_{iji}{}^k$ 的指标收缩，直接计算得

$$
\mathcal R_1(\alpha)=\sum_{j,l}\mathrm{Ric}_{jl}\alpha_l\,e^j=\mathrm{Ric}(\alpha,\cdot).
$$

**步骤 6：Lichnerowicz 公式。** 在自旋流形上 $D=\sum_i c(e_i)\nabla_i$，其中 $c$ 为 Clifford 乘法，满足 $c(e_i)c(e_j)+c(e_j)c(e_i)=-2\delta_{ij}$。展开

$$
D^2=\sum_{i,j}c(e_i)c(e_j)\nabla_i\nabla_j=-\sum_i\nabla_i\nabla_i+\sum_{i<j}c(e_i)c(e_j)\big(\nabla_i\nabla_j-\nabla_j\nabla_i\big).
$$

在自旋丛上由局部表示 $\nabla_i\nabla_j-\nabla_j\nabla_i=\frac{1}{4}\sum_{k,l}R_{ijkl}c(e_k)c(e_l)$，对指标收缩后后一项等于 $\frac{1}{4}\mathrm{Scal}$，于是

$$
D^2=\nabla^*\nabla+\frac{\mathrm{Scal}}{4}.
$$

**步骤 7：消没推论。** 取 $p=1$ 并设 $\mathrm{Ric}>0$、$\Delta_H\alpha=0$。在紧流形上积分

$$
0=\int_M\langle\Delta_H\alpha,\alpha\rangle=\int_M|\nabla\alpha|^2+\int_M\mathrm{Ric}(\alpha,\alpha)\ge0 .
$$

两项均非负、第二项正定，故 $\nabla\alpha=0$、$\alpha=0$，从而 $b_1(M)=0$。

证毕。

## 课堂问答

**老师**：陈述 Weitzenböck 公式，并说明 $p=1$ 时曲率项是什么。

**学生**：结论：Hodge-de Rham 拉普拉斯与联络拉普拉斯只差一个零阶曲率端同态
$$\Delta_H\alpha=\nabla^*\nabla\alpha+\mathcal R_p(\alpha),$$
其中 $\mathcal R_p$ 由 Riemann 张量代数地定义；$p=1$ 时 $\mathcal R_1=\mathrm{Ric}$，即 $\Delta_H\alpha=\nabla^*\nabla\alpha+\mathrm{Ric}(\alpha,\cdot)$。理由是两算子之差形式上是一阶，但曲率是二阶协变导数的交换子，使差降为零阶。误区是以为 $\mathcal R_p$ 依赖标架——它其实是良定的张量端同态。

**老师（追问）**：为什么它能推出 Bochner 消没定理？

**学生**：取 $p=1$、$\mathrm{Ric}>0$、$\Delta_H\alpha=0$，在紧流形上积分
$$0=\int_M\langle\Delta_H\alpha,\alpha\rangle=\int_M|\nabla\alpha|^2+\int_M\mathrm{Ric}(\alpha,\alpha)\ge0.$$
两项非负、第二项正定，故 $\nabla\alpha=0$ 且 $\alpha=0$，从而 $b_1(M)=0$。核心是曲率项正定把调和对象逼没。

**老师（拓展）**：旋量情形给出什么？

**学生**：Lichnerowicz 公式 $D^2=\nabla^*\nabla+\frac14\mathrm{Scal}$。它在 $\mathrm{Scal}>0$ 时给出 Dirac 算子无核、指标消失，是 Lichnerowicz 特征值估计与 Atiyah-Singer 指标定理"曲率强制指标为零"的技术核心，也通向 Seiberg-Witten 理论。

## 相关条目

- [Bochner公式](./Bochner公式.md)：函数与 1-形式情形的 Weitzenböck 恒等式，本公式是它的 $p$-形式推广。
- [Hodge分解定理](./Hodge分解定理.md)：调和形式的刻画依赖 $\Delta_H$ 的表达式。
- [Riemann曲率张量的对称性](./Riemann曲率张量的对称性.md)：曲率端同态 $\mathcal R_p$ 由 Riemann 张量的代数性质决定。
- [Riemann曲率张量](../第33级-微分几何/Riemann曲率张量.md)：Weitzenböck 项以 Riemann 张量为唯一输入。
