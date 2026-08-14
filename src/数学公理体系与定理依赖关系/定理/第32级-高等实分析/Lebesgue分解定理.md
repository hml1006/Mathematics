# Lebesgue分解定理

## 介绍

Lebesgue分解定理是测度论中关于两个测度之间关系的基本定理。它断言：给定两个 $\sigma$-有限测度 $\mu$ 和 $\nu$，$\nu$ 可以唯一地分解为两个部分之和——一个关于 $\mu$ 绝对连续的部分 $\nu_a$ 和一个关于 $\mu$ 奇异的部分 $\nu_s$（即 $\nu_s$ 集中在某个 $\mu$-零测集上）。这个定理将测度之间的关系清晰地刻画为"光滑部分"和"奇异部分"的叠加，是 Radon-Nikodym 定理的自然延伸和补充。

## 分析

**定理的精确表述**：设 $\mu$ 和 $\nu$ 是 $\sigma$-有限测度空间 $(X, \mathcal{M})$ 上的测度。则存在唯一的分解

$$
\nu = \nu_a + \nu_s,
$$

其中 $\nu_a \ll \mu$（$\nu_a$ 关于 $\mu$ 绝对连续），$\nu_s \perp \mu$（$\nu_s$ 与 $\mu$ 奇异，即存在可测集 $N$ 使得 $\mu(N) = 0$ 且 $\nu_s(X \setminus N) = 0$）。

**等价表述**：存在唯一的可测函数 $f$ 和 $\mu$-零测集 $N$ 使得

$$
\nu(A) = \int_A f \, d\mu + \nu_s(A),
$$

其中 $\nu_s(A) = \nu(A \cap N)$。

**关键要点**：

- 分解是唯一的：$\nu_a$ 和 $\nu_s$ 由 $\mu$ 和 $\nu$ 唯一确定。
- 若 $\nu \ll \mu$，则 $\nu_s = 0$，Lebesgue 分解退化为 Radon-Nikodym 定理。
- 若 $\nu \perp \mu$，则 $\nu_a = 0$。
- 这个定理推广了 Radon-Nikodym 定理，将其适用范围从绝对连续情形推广到一般情形。

## 思考过程

Lebesgue 分解定理的证明依赖于 Radon-Nikodym 定理，通过构造一个"最大"的绝对连续部分来实现。

基本思路：
1. 考虑 $\lambda = \mu + \nu$，则 $\mu \ll \lambda$ 且 $\nu \ll \lambda$。
2. 由 Radon-Nikodym 定理，存在 $f, g$ 使得 $\mu(A) = \int_A f \, d\lambda$，$\nu(A) = \int_A g \, d\lambda$。
3. 令 $N = \{x \mid f(x) = 0\}$，则 $\mu(N) = 0$。定义 $\nu_s(A) = \nu(A \cap N)$，$\nu_a(A) = \nu(A \setminus N) = \int_{A \setminus N} g \, d\lambda$。
4. 验证 $\nu_a \ll \mu$ 且 $\nu_s \perp \mu$。

## 证明过程

**证明**：设 $\mu$ 和 $\nu$ 是 $(X, \mathcal{M})$ 上的 $\sigma$-有限测度。

**步骤 1**：化归到有限测度情形。与 Radon-Nikodym 定理的证明类似，通过 $\sigma$-有限性将问题分解到有限测度集上处理。不妨设 $\mu$ 和 $\nu$ 都是有限测度。

**步骤 2**：构造参考测度。令 $\lambda = \mu + \nu$，则 $\lambda$ 是有限测度，且 $\mu \ll \lambda$，$\nu \ll \lambda$。由 Radon-Nikodym 定理，存在可测函数 $f, g \ge 0$ 使得

$$
\mu(A) = \int_A f \, d\lambda, \quad \nu(A) = \int_A g \, d\lambda, \quad \forall A \in \mathcal{M}.
$$

**步骤 3**：定义奇异集。令 $N = \{x \in X \mid f(x) = 0\}$。则

$$
\mu(N) = \int_N f \, d\lambda = 0.
$$

**步骤 4**：定义分解。对任意 $A \in \mathcal{M}$，定义

$$
\nu_a(A) = \nu(A \setminus N) = \int_{A \setminus N} g \, d\lambda,
$$
$$
\nu_s(A) = \nu(A \cap N) = \int_{A \cap N} g \, d\lambda.
$$

显然 $\nu = \nu_a + \nu_s$，且 $\nu_s(N) = \nu(N)$，而 $\mu(N) = 0$，故 $\nu_s \perp \mu$。

**步骤 5**：验证 $\nu_a \ll \mu$。设 $\mu(A) = 0$。则 $\int_A f \, d\lambda = 0$，故 $f = 0$ $\lambda$-几乎处处在 $A$ 上，即 $A \subset N$（在 $\lambda$-几乎处处意义下）。因此 $\lambda(A) = 0$（因为 $f = 0$ 在 $A$ 上，$\mu(A) = \int_A f \, d\lambda = 0$ 自动成立，但我们需要 $\lambda(A) = 0$）。

更精确地：$\mu(A) = \int_A f \, d\lambda = 0$ 意味着 $f = 0$ $\lambda$-几乎处处在 $A$ 上，即 $A \setminus N$ 是 $\lambda$-零测集。由于 $\nu \ll \lambda$，$\nu(A \setminus N) = 0$，故 $\nu_a(A) = \nu(A \setminus N) = 0$。

**步骤 6**：唯一性。假设有两种分解 $\nu = \nu_a + \nu_s = \nu_a' + \nu_s'$，则 $\nu_a - \nu_a' = \nu_s' - \nu_s$。左边关于 $\mu$ 绝对连续，右边与 $\mu$ 奇异，故两边必须同时为零。因此 $\nu_a = \nu_a'$，$\nu_s = \nu_s'$。$\square$

**推论**：对任意 $\sigma$-有限测度 $\mu$ 和 $\nu$，存在 $\mu$-零测集 $N$ 使得 $\nu|_N \perp \mu$ 且 $\nu|_{X \setminus N} \ll \mu$。这是 Lebesgue 分解定理的最常用形式。

**应用**：在概率论中，Lebesgue 分解定理用于将概率分布分解为连续部分（有密度函数）和奇异部分（如 Cantor 分布）。在统计中，它用于区分不同的概率测度类型。