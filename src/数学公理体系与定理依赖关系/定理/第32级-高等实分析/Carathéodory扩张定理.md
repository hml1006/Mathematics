# Carathéodory扩张定理

> **一句话大白话**：只要你在"小积木"（半环/代数次）上给出了一块不打架、可数可加的"尺子"，它就一定能唯一地"长大"成覆盖整个可测空间的正式测度——测度的骨架一旦搭好，血肉自动长出来。
>
> **小例子**：先在直线上给区间 $(a,b]$ 指定长度 $b-a$，这把"尺子"满足一致性；Carathéodory扩张把它唯一延拓成整个波雷尔 $\sigma$-代数上的勒贝格测度。

## 介绍

Carathéodory扩张定理是测度论中最基本的构造性定理之一，由 Constantin Carathéodory 在 1918 年提出。它断言：定义在半环（或代数）上的 $\sigma$-有限预测度可以唯一地扩张到由该半环生成的 $\sigma$-代数上的一个完全测度。这个定理是现代测度论和 Lebesgue 测度构造的理论基础，提供了从简单集合类上的预测度构造出整个 $\sigma$-代数上测度的一般方法。

## 分析

**定理的精确表述**：设 $\mathcal{A}$ 是 $X$ 上的一个代数，$\mu_0: \mathcal{A} \to [0, \infty]$ 是 $\sigma$-可加预测度（即满足 $\mu_0(\varnothing) = 0$ 且对 $\mathcal{A}$ 中不交可列并属于 $\mathcal{A}$ 的集合列满足 $\sigma$-可加性）。令 $\mathcal{M} = \sigma(\mathcal{A})$ 是由 $\mathcal{A}$ 生成的 $\sigma$-代数。则：

1. 存在 $\mathcal{M}$ 上的测度 $\mu$ 使得 $\mu|_{\mathcal{A}} = \mu_0$；
2. 若 $\mu_0$ 是 $\sigma$-有限的（即 $X = \bigcup_{n=1}^\infty A_n$，$A_n \in \mathcal{A}$，$\mu_0(A_n) < \infty$），则 $\mu$ 是唯一的。

**构造方法**：通过外测度 $\mu^*(E) = \inf\left\{ \sum_{n=1}^\infty \mu_0(A_n) \mid A_n \in \mathcal{A}, E \subset \bigcup_{n=1}^\infty A_n \right\}$ 和 Carathéodory 可测集的定义来构造 $\mu$。

**关键要点**：

- 定理的核心是"扩张"——从代数的 $\sigma$-可加性推出 $\sigma$-代数上的完全测度。
- $\sigma$-有限条件保证了扩张的唯一性。
- 构造的关键是 Carathéodory 外测度概念和可测性的定义。
- Lebesgue 测度是 Carathéodory 扩张定理的一个特例：取 $\mathcal{A}$ 为 $\mathbb{R}$ 上的左闭右开区间代数，$\mu_0([a,b)) = b-a$。

## 思考过程

Carathéodory 扩张定理的证明思路分为三步：

1. **定义外测度**：利用 $\mu_0$ 通过可数覆盖定义 $\mu^*$，并验证 $\mu^*$ 是外测度（满足单调性、可数次可加性、$\mu^*(\varnothing)=0$）。

2. **定义可测集**：引入 Carathéodory 可测条件：$E$ 可测当且仅当对任意 $A \subset X$，$\mu^*(A) = \mu^*(A \cap E) + \mu^*(A \setminus E)$。证明所有可测集构成 $\sigma$-代数 $\mathcal{M}^*$，且 $\mu^*$ 限制在 $\mathcal{M}^*$ 上是完全测度。

3. **验证扩张**：证明 $\mathcal{A} \subset \mathcal{M}^*$ 且 $\mu^*|_{\mathcal{A}} = \mu_0$，从而 $\mathcal{M} = \sigma(\mathcal{A}) \subset \mathcal{M}^*$，$\mu = \mu^*|_{\mathcal{M}}$ 即为所求。

唯一性通过 $\sigma$-有限性条件下标准测度论论证（单调类定理或 $\pi$-$\lambda$ 定理）获得。

## 证明过程

**证明**：设 $\mathcal{A}$ 是 $X$ 上的代数，$\mu_0: \mathcal{A} \to [0, \infty]$ 是 $\sigma$-可加预测度。

**步骤 1**：定义外测度。对任意 $E \subset X$，定义

$$
\mu^*(E) = \inf\left\{ \sum_{n=1}^\infty \mu_0(A_n) \mid A_n \in \mathcal{A}, E \subset \bigcup_{n=1}^\infty A_n \right\}.
$$

其中 $\inf \varnothing = \infty$。验证 $\mu^*$ 是外测度：
- $\mu^*(\varnothing) = 0$（取 $A_n = \varnothing$ 覆盖空集）；
- 单调性：若 $E \subset F$，则 $\mu^*(E) \le \mu^*(F)$；
- 可数次可加性：对 $\{E_n\}$ 和 $\varepsilon > 0$，对每个 $n$ 取覆盖 $\{A_{n,k}\}$ 使得 $\sum_k \mu_0(A_{n,k}) \le \mu^*(E_n) + \varepsilon/2^n$，则 $\{A_{n,k}\}_{n,k}$ 覆盖 $\bigcup_n E_n$，从而 $\mu^*(\bigcup_n E_n) \le \sum_{n,k} \mu_0(A_{n,k}) \le \sum_n \mu^*(E_n) + \varepsilon$。

**步骤 2**：Carathéodory 可测集。定义 $\mathcal{M}^* = \{E \subset X \mid \forall A \subset X, \mu^*(A) = \mu^*(A \cap E) + \mu^*(A \setminus E)\}$。标准结论（Carathéodory 引理）：$\mathcal{M}^*$ 是 $\sigma$-代数，且 $\mu^*$ 限制在 $\mathcal{M}^*$ 上是完全测度。

**步骤 3**：证明 $\mathcal{A} \subset \mathcal{M}^*$。对任意 $A \in \mathcal{A}$ 和任意 $E \subset X$，需要证明 $\mu^*(E) \ge \mu^*(E \cap A) + \mu^*(E \setminus A)$（反向不等式自动成立）。对 $\varepsilon > 0$，取覆盖 $\{A_n\} \subset \mathcal{A}$ 使得 $E \subset \bigcup A_n$ 且 $\sum \mu_0(A_n) \le \mu^*(E) + \varepsilon$。由于 $A_n = (A_n \cap A) \cup (A_n \setminus A)$ 且 $A_n \cap A, A_n \setminus A \in \mathcal{A}$（因为 $\mathcal{A}$ 是代数），由 $\mu_0$ 的可加性，

$$
\mu_0(A_n) = \mu_0(A_n \cap A) + \mu_0(A_n \setminus A).
$$

因此 $\{A_n \cap A\}$ 覆盖 $E \cap A$，$\{A_n \setminus A\}$ 覆盖 $E \setminus A$，故

$$
\mu^*(E \cap A) + \mu^*(E \setminus A) \le \sum \mu_0(A_n \cap A) + \sum \mu_0(A_n \setminus A) = \sum \mu_0(A_n) \le \mu^*(E) + \varepsilon.
$$

令 $\varepsilon \to 0$ 即得 $\mathcal{A} \subset \mathcal{M}^*$。

**步骤 4**：$\mu^*|_{\mathcal{A}} = \mu_0$。对 $A \in \mathcal{A}$，显然 $\mu^*(A) \le \mu_0(A)$（取 $A$ 自身作为覆盖）。反向不等式：若 $A \subset \bigcup A_n$，$A_n \in \mathcal{A}$，则 $\{A \cap A_n\}$ 是 $A$ 的可数覆盖，且 $A = \bigcup (A \cap A_n)$。由 $\mu_0$ 在 $\mathcal{A}$ 上的 $\sigma$-可加性，

$$
\mu_0(A) = \mu_0\left(\bigcup (A \cap A_n)\right) \le \sum \mu_0(A \cap A_n) \le \sum \mu_0(A_n).
$$

取下确界得 $\mu_0(A) \le \mu^*(A)$。故 $\mu_0(A) = \mu^*(A)$。

**步骤 5**：扩张和唯一性。令 $\mu = \mu^*|_{\sigma(\mathcal{A})}$，由步骤 3-4，$\mu$ 是 $\sigma(\mathcal{A})$ 上的测度且 $\mu|_{\mathcal{A}} = \mu_0$。若 $\mu_0$ 是 $\sigma$-有限的，由 $\pi$-$\lambda$ 定理（或单调类定理），$\mu$ 在 $\sigma(\mathcal{A})$ 上是唯一的。$\square$

**应用——Lebesgue 测度的构造**：取 $\mathcal{A}$ 为 $\mathbb{R}$ 上有限个左闭右开区间 $[a,b)$ 的不交并组成的代数，$\mu_0([a,b)) = b-a$。Carathéodory 扩张定理给出 $\mathbb{R}$ 上的 Lebesgue 测度 $\mu$，且 $\mathcal{M} = \sigma(\mathcal{A})$ 包含所有 Borel 集。