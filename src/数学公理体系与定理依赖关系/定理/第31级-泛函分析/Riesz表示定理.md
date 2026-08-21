# Riesz表示定理

> **一句话大白话**：希尔伯特空间上的每一个"连续线性测量"都可以用一个唯一的内在向量点乘来表示——"所有线性泛函归根到底都是跟某个向量做内积"，有限维如此，无限维也如此。
>
> **小例子**：对任意连续的线性泛函 $\ell$，存在唯一向量 $y$ 使得 $\ell(x)=\langle x,y\rangle$；例如在 $\mathbb{R}^n$ 里 $\ell(x)=a\cdot x$ 的核心就是 $y=a$。

## 介绍

Riesz表示定理（Riesz Representation Theorem）是泛函分析中关于 Hilbert 空间对偶空间的基本定理。它断言：Hilbert 空间 $H$ 上的每个连续线性泛函都可以唯一地表示为与某个固定向量的内积形式。换言之，Hilbert 空间 $H$ 的对偶空间 $H^*$ 与 $H$ 自身等距同构。这个定理揭示了 Hilbert 空间的自对偶性，是量子力学、偏微分方程和变分法中 Ritz-Galerkin 方法的理论基础。

## 分析

**前置依赖**：Hilbert 空间的完备性、正交分解定理（投影定理）、Cauchy-Schwarz 不等式、连续线性泛函的核是闭子空间

**定理的精确表述**：设 $H$ 是 Hilbert 空间（完备内积空间），$\varphi: H \to \mathbb{R}$（或 $\mathbb{C}$）是连续线性泛函。则存在唯一的 $y \in H$ 使得

$$
\varphi(x) = \langle x, y \rangle, \quad \forall x \in H,
$$

且 $\|\varphi\| = \|y\|$，其中 $\|\varphi\|$ 是泛函的算子范数。

**关键要点**：

- 该定理建立了 $H$ 与 $H^*$ 之间的共轭线性等距同构（复空间中是共轭线性，实空间中是线性）。
- 通常记这个同构为 $J: H \to H^*$，$(J(y))(x) = \langle x, y \rangle$。
- 在 $L^2$ 空间中，该定理退化为 $L^2$ 上的经典 Riesz 表示定理（即 $L^2$ 的对偶是 $L^2$ 自身）。
- 与 $L^p$ 空间 ($p \neq 2$) 的 Riesz 表示定理不同，Hilbert 空间版本不需要测度论工具。

## 思考过程

Riesz 表示定理的证明思路直观且优美：

1. **构造 $y$**：考虑 $\ker \varphi$。若 $\varphi \equiv 0$，取 $y = 0$。否则，$\ker \varphi$ 是 $H$ 的真闭子空间，其正交补 $\ker \varphi^\perp$ 是一维的。取 $z \in \ker \varphi^\perp$ 非零，令 $y = \overline{\varphi(z)} / \|z\|^2 \cdot z$。

2. **验证表示性**：对任意 $x \in H$，将 $x$ 分解为 $\ker \varphi$ 上的投影和 $\ker \varphi^\perp$ 上的投影，然后直接计算内积。

3. **范数相等**：由 Cauchy-Schwarz 不等式，$|\varphi(x)| = |\langle x, y \rangle| \le \|x\|\|y\|$，故 $\|\varphi\| \le \|y\|$。反之，取 $x = y$ 得 $\varphi(y) = \|y\|^2$，故 $\|\varphi\| \ge \|y\|$。

## 证明过程

**证明**：设 $H$ 是 Hilbert 空间，$\varphi \in H^*$。

**步骤 1**：平凡情形。若 $\varphi \equiv 0$，取 $y = 0$ 即满足条件。

**步骤 2**：非平凡情形。设 $\varphi \not\equiv 0$。$\ker \varphi$ 是 $H$ 的真闭子空间（因为 $\varphi$ 连续且非零）。由正交分解定理，$H = \ker \varphi \oplus (\ker \varphi)^\perp$，且 $(\ker \varphi)^\perp$ 是非零闭子空间。

取 $z \in (\ker \varphi)^\perp$ 且 $z \neq 0$。定义

$$
y = \frac{\overline{\varphi(z)}}{\|z\|^2} z.
$$

**步骤 3**：验证表示性。对任意 $x \in H$，$x$ 可唯一分解为 $x = u + \alpha z$，其中 $u \in \ker \varphi$，$\alpha \in \mathbb{R}$（或 $\mathbb{C}$）。则

$$
\varphi(x) = \varphi(u) + \alpha \varphi(z) = \alpha \varphi(z).
$$

另一方面，

$$
\langle x, y \rangle = \langle u + \alpha z, \frac{\overline{\varphi(z)}}{\|z\|^2} z \rangle = \frac{\varphi(z)}{\|z\|^2} \langle u, z \rangle + \frac{\alpha \varphi(z)}{\|z\|^2} \langle z, z \rangle.
$$

由于 $z \perp \ker \varphi$，$\langle u, z \rangle = 0$，且 $\langle z, z \rangle = \|z\|^2$，故

$$
\langle x, y \rangle = \alpha \varphi(z) = \varphi(x).
$$

**步骤 4**：范数相等。由 Cauchy-Schwarz 不等式，

$$
|\varphi(x)| = |\langle x, y \rangle| \le \|x\| \|y\|,
$$

故 $\|\varphi\| \le \|y\|$。另一方面，取 $x = y$，

$$
\varphi(y) = \langle y, y \rangle = \|y\|^2,
$$

故 $\|\varphi\| \ge \|y\|$。因此 $\|\varphi\| = \|y\|$。

**步骤 5**：唯一性。若存在 $y_1, y_2 \in H$ 使得 $\varphi(x) = \langle x, y_1 \rangle = \langle x, y_2 \rangle$ 对所有 $x \in H$ 成立，则 $\langle x, y_1 - y_2 \rangle = 0$ 对所有 $x \in H$ 成立。取 $x = y_1 - y_2$ 得 $\|y_1 - y_2\|^2 = 0$，故 $y_1 = y_2$。$\square$

**推论（Lax-Milgram 定理的准备工作）**：Riesz 表示定理保证了在 Hilbert 空间中，每个连续线性泛函对应于一个唯一的内积表示，这使得我们可以将变分问题转化为等价的算子方程。

**注**：在复 Hilbert 空间中，映射 $y \mapsto \langle \cdot, y \rangle$ 是共轭线性的，即 $\langle x, \alpha y \rangle = \bar{\alpha} \langle x, y \rangle$。因此 $H$ 与 $H^*$ 之间的同构是共轭线性同构。