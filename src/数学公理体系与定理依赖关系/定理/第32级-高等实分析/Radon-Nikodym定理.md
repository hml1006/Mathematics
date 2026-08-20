# Radon-Nikodym定理

> **一句话大白话**：只要一个测度"绝不把质量偷偷放到另一个测度的零集上"（绝对连续），它就能写成那个测度乘一个函数再整个积分出来的样子——质量分布可以"换算成密度"。
>
> **小例子**：若 $\nu$ 对 $\mu$ 绝对连续，则存在密度 $\frac{d\nu}{d\mu}=f$ 使 $\nu(A)=\int_A f\,d\mu$；例如 $\nu(A)=\int_A 2x\,dx$ 时 $f(x)=2x$，初等离散情形就是普通"权重比例"的推广。

## 介绍

Radon-Nikodym定理是实分析和测度论中最深刻的定理之一。它断言：如果 $\nu$ 关于 $\mu$ 绝对连续（即 $\mu(A) = 0$ 蕴含 $\nu(A) = 0$），则存在一个可测函数 $f$ 使得 $\nu$ 可以表示为 $\mu$ 乘以 $f$ 的积分。这个函数 $f$ 称为 Radon-Nikodym 导数 $d\nu/d\mu$。该定理是概率论中条件期望存在性的理论基础，也是统计中似然比概念和数学金融中测度变换（Girsanov 定理）的核心工具。

## 分析

**定理的精确表述**：设 $(X, \mathcal{M}, \mu)$ 是 $\sigma$-有限测度空间，$\nu$ 是 $\mathcal{M}$ 上的 $\sigma$-有限测度（或带符号测度），且 $\nu \ll \mu$（即 $\nu$ 关于 $\mu$ 绝对连续：$\mu(A) = 0 \Rightarrow \nu(A) = 0$）。则存在可测函数 $f: X \to [0, \infty)$（或 $\mathbb{R}$）使得对任意 $A \in \mathcal{M}$，

$$
\nu(A) = \int_A f \, d\mu.
$$

函数 $f$ 称为 $\nu$ 关于 $\mu$ 的 Radon-Nikodym 导数，记作 $f = \frac{d\nu}{d\mu}$。$f$ 在 $\mu$-几乎处处意义下唯一。

**关键要点**：

- $\sigma$-有限条件是本质的——若 $\mu$ 不是 $\sigma$-有限的，定理可能不成立。
- 绝对连续性 $\nu \ll \mu$ 是 $\nu$ 可表示为 $\mu$ 积分形式的必要条件。
- 若 $\nu$ 是带符号测度，$f$ 可取实数值（不一定非负）。
- 在概率论中，Radon-Nikodym 导数 $d\nu/d\mu$ 就是似然比（likelihood ratio）。

## 思考过程

Radon-Nikodym 定理的证明通常采用 Hilbert 空间方法或函数分析方法：

1. **考虑 $\mu + \nu$**：将 $\mu$ 和 $\nu$ 组合成一个新测度。如果 $\mu$ 和 $\nu$ 都是有限测度，考虑 $L^2(\mu + \nu)$ 空间。

2. **构造线性泛函**：定义 $\varphi(f) = \int f \, d\nu$，这是 $L^2(\mu + \nu)$ 上的连续线性泛函。由 Riesz 表示定理，存在 $g \in L^2(\mu + \nu)$ 使得 $\varphi(f) = \int f g \, d(\mu + \nu)$。

3. **推导表示式**：通过分析 $g$ 的性质，证明 $0 \le g \le 1$（$\mu + \nu$-几乎处处），且 $g$ 的适当变换给出 Radon-Nikodym 导数。

另一种经典证明使用 Hahn 分解定理和构造性方法，逐步从简单函数逼近。

## 证明过程

**证明**：我们给出基于 Hilbert 空间方法的证明（von Neumann 证明）。

**步骤 1**：化归到有限测度情形。若 $\mu$ 和 $\nu$ 是 $\sigma$-有限的，则存在可测集 $X_n \uparrow X$ 使得 $\mu(X_n) < \infty$ 且 $\nu(X_n) < \infty$。在每个 $X_n$ 上证明定理成立，再拼接得到整体结果。因此不妨设 $\mu$ 和 $\nu$ 都是有限测度。

**步骤 2**：定义 $\lambda = \mu + \nu$，则 $\lambda$ 是有限测度。考虑 Hilbert 空间 $L^2(\lambda)$。定义线性泛函 $\varphi: L^2(\lambda) \to \mathbb{R}$ 为

$$
\varphi(f) = \int f \, d\nu.
$$

由 Cauchy-Schwarz 不等式，$|\varphi(f)| \le \int |f| \, d\nu \le \int |f| \, d\lambda \le \|f\|_{L^2(\lambda)} \sqrt{\lambda(X)}$，故 $\varphi$ 连续。由 Riesz 表示定理，存在 $g \in L^2(\lambda)$ 使得

$$
\int f \, d\nu = \int f g \, d\lambda = \int f g \, d\mu + \int f g \, d\nu, \quad \forall f \in L^2(\lambda).
$$

**步骤 3**：分析 $g$ 的性质。整理得

$$
\int f (1 - g) \, d\nu = \int f g \, d\mu, \quad \forall f \in L^2(\lambda).
$$

取 $f = \chi_{E}$（$E$ 可测），得 $\nu(E) = \int_E g \, d\lambda$。由于 $\nu \ge 0$，$\int_E g \, d\lambda \ge 0$ 对所有 $E$ 成立，故 $g \ge 0$ $\lambda$-几乎处处。类似地，对任意 $E$，$\int_E (1 - g) \, d\nu \ge 0$，故 $1 - g \ge 0$ $\nu$-几乎处处，从而 $g \le 1$ $\nu$-几乎处处。

**步骤 4**：构造 Radon-Nikodym 导数。考虑 $A = \{x \in X \mid g(x) = 1\}$。则 $\nu(A) = \int_A g \, d\lambda = \int_A 1 \, d\lambda = \lambda(A) = \mu(A) + \nu(A)$，故 $\mu(A) = 0$。由 $\nu \ll \mu$，$\nu(A) = 0$。因此 $g < 1$ $\mu$-几乎处处。

在 $\{g < 1\}$ 上，由 $\int f (1 - g) \, d\nu = \int f g \, d\mu$ 得

$$
\int f \, d\nu = \int f \frac{g}{1 - g} \, d\mu.
$$

令 $h = \frac{g}{1 - g}$（在 $\{g = 1\}$ 上定义 $h = 0$），则 $h$ 是可测函数，且

$$
\nu(E) = \int_E h \, d\mu + \nu(E \cap A).
$$

由于 $\mu(A) = 0$ 且 $\nu \ll \mu$，$\nu(A) = 0$，故 $\nu(E) = \int_E h \, d\mu$。

**步骤 5**：唯一性。若 $h_1, h_2$ 都满足条件，则 $\int_E (h_1 - h_2) \, d\mu = 0$ 对所有 $E \in \mathcal{M}$ 成立，故 $h_1 = h_2$ $\mu$-几乎处处。$\square$

**推论**：若 $\nu \ll \mu$ 且 $\mu \ll \lambda$，则 $\frac{d\nu}{d\lambda} = \frac{d\nu}{d\mu} \cdot \frac{d\mu}{d\lambda}$ $\lambda$-几乎处处（链式法则）。

**应用**：在概率论中，条件期望 $\mathbb{E}(X \mid \mathcal{G})$ 的存在性可由 Radon-Nikodym 定理推出：令 $\nu(A) = \int_A X \, d\mathbb{P}$，则 $\nu \ll \mathbb{P}|_{\mathcal{G}}$，其 Radon-Nikodym 导数即为条件期望。