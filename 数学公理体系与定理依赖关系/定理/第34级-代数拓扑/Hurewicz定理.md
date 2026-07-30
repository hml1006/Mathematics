# Hurewicz定理

## 介绍

Hurewicz定理是代数拓扑中连接同伦论与同调论的核心定理，由 Witold Hurewicz 在 1935 年提出。它断言：对于道路连通的空间 $X$，第一个同调群 $H_1(X)$ 是基本群 $\pi_1(X)$ 的 Abel 化（即 $\pi_1(X)$ 模去换位子子群）。对于 $n \ge 2$，若 $X$ 是 $(n-1)$-连通的（即 $\pi_k(X) = 0$ 对所有 $k < n$ 成立），则 $H_n(X) \cong \pi_n(X)$。这个定理建立了同伦群与同调群之间的桥梁，使得我们可以用更容易计算的同调群来获取同伦群的信息。

## 分析

**定理的精确表述**：

**Hurewicz 定理（经典版本）**：设 $X$ 是道路连通拓扑空间，则存在自然同态

$$
h: \pi_1(X, x_0) \to H_1(X)
$$

称为 Hurewicz 同态，使得 $h$ 是满射且 $\ker h$ 是 $\pi_1(X)$ 的换位子子群 $[\pi_1(X), \pi_1(X)]$。因此

$$
H_1(X) \cong \pi_1(X) / [\pi_1(X), \pi_1(X)] = \pi_1(X)^{\text{ab}}.
$$

**高维 Hurewicz 定理**：设 $X$ 是 $(n-1)$-连通的（$n \ge 2$），即 $\pi_k(X) = 0$ 对所有 $k < n$ 成立。则 Hurewicz 同态

$$
h_n: \pi_n(X, x_0) \to H_n(X)
$$

是同构，且 $H_k(X) = 0$ 对所有 $k < n$ 成立。

**Hurewicz 同态的构造**：将每个 $[\gamma] \in \pi_1(X)$ 对应到 $\gamma$ 作为 $1$-闭链的同调类。对高维，将 $\pi_n(X)$ 中的映射 $f: S^n \to X$ 对应到 $f_*([S^n])$，其中 $[S^n]$ 是 $S^n$ 的基本类。

**关键要点**：

- $H_1(X)$ 是 $\pi_1(X)$ 的 Abel 化——这是计算 $H_1$ 的常用方法。
- 高维 Hurewicz 定理给出了第一个非平凡同伦群与同调群的同构。
- 条件 $\pi_k(X) = 0$ 对 $k < n$ 是本质的——没有这个条件，定理不成立。
- 对 $n \ge 2$，$\pi_n(X)$ 是 Abel 群，这与 Hurewicz 定理一致。

## 思考过程

Hurewicz 定理的证明思路：

1. **构造 Hurewicz 同态**：将基本群元素 $[\gamma]$ 映射到 $\gamma$ 作为奇异 $1$-闭链的同调类。需要验证这个映射是良定义的群同态。

2. **证明 $\ker h = [\pi_1, \pi_1]$**：核心是证明 $h$ 的核恰好是换位子子群，即 $\gamma$ 的 $1$-闭链为零同调类当且仅当 $\gamma$ 是换位子的乘积。

3. **高维情况**：利用相对同调群和 Hurewicz 定理的相对版本，通过归纳法证明。

## 证明过程

**证明**：我们给出 $n = 1$ 情形的证明概要。

**步骤 1**：定义 Hurewicz 同态 $h: \pi_1(X, x_0) \to H_1(X)$。对 $[\gamma] \in \pi_1(X)$，$\gamma: [0, 1] \to X$ 是闭道路，$\gamma$ 作为奇异 $1$-单形，$\partial \gamma = \gamma(1) - \gamma(0) = x_0 - x_0 = 0$，故 $\gamma$ 是 $1$-闭链，定义 $h([\gamma]) = [\gamma] \in H_1(X)$。

**步骤 2**：验证 $h$ 是良定义的群同态。若 $\gamma_1 \simeq \gamma_2$（保持基点同伦），则同伦 $H$ 给出 $2$-链，其边缘为 $\gamma_1 - \gamma_2$（加上一些常值道路），故 $[\gamma_1] = [\gamma_2]$ 在 $H_1$ 中。因此 $h$ 良定义。

对群运算：$h([\gamma_1] \cdot [\gamma_2]) = h([\gamma_1 * \gamma_2])$。在 $H_1$ 中，$[\gamma_1 * \gamma_2] = [\gamma_1] + [\gamma_2]$（因为 $\gamma_1 * \gamma_2$ 与 $\gamma_1 + \gamma_2$ 相差一个 $2$-边缘）。故 $h$ 是同态。

**步骤 3**：证明 $h$ 是满射。$H_1(X)$ 的任何元素可表示为 $\sum n_i \sigma_i$，其中 $\sigma_i: \Delta^1 \to X$ 是道路。通过连接这些道路的端点，可以构造一条闭道路，其同调类等于该元素。故 $h$ 满射。

**步骤 4**：证明 $\ker h = [\pi_1, \pi_1]$。若 $[\gamma] \in [\pi_1, \pi_1]$，则 $\gamma$ 是换位子的乘积，每个换位子 $\alpha\beta\alpha^{-1}\beta^{-1}$ 在 $H_1$ 中为零（因为 $H_1$ 是 Abel 群），故 $h([\gamma]) = 0$。反之，若 $h([\gamma]) = 0$，则 $\gamma = \partial \tau$ 对某个 $2$-链 $\tau$。通过将 $\tau$ 分解为奇异 $2$-单形的和，可以证明 $\gamma$ 同伦于换位子的乘积。$\square$

**高维 Hurewicz 定理（$n \ge 2$）**：设 $X$ 是 $(n-1)$-连通的。证明的思路是考虑相对同调群 $H_n(X, X^{n-1})$ 和相对同伦群 $\pi_n(X, X^{n-1})$，其中 $X^{n-1}$ 是 $X$ 的 $(n-1)$-骨架。利用相对 Hurewicz 定理，证明 $\pi_n(X, X^{n-1}) \cong H_n(X, X^{n-1})$，然后通过正合序列得到 $\pi_n(X) \cong H_n(X)$。

**应用**：
- 计算 $H_1$：若 $\pi_1(X) = \langle a, b \mid aba^{-1}b^{-1} \rangle$（环面），则 $H_1 \cong \mathbb{Z} \oplus \mathbb{Z}$。
- 若 $X$ 单连通，则 $H_1(X) = 0$，且 $\pi_2(X) \cong H_2(X)$。
- 对 $S^n$（$n \ge 2$），$\pi_n(S^n) \cong \mathbb{Z}$（由 Hurewicz 定理和 $H_n(S^n) \cong \mathbb{Z}$）。