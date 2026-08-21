# Lax-Milgram定理

> **一句话大白话**：在希尔伯特空间里，只要双线性形式"连续、强制（椭性）"，那么对应的变分方程对任意右端都有且只有一个解——把一般椭圆方程的"弱解存在唯一"统一收进一套通用判据。
>
> **小例子**：泊松方程 $-u''=f$（附边界条件）写成变分形式 $a(u,v)=\int u'v'$，该双线性形式满足连续+强制，于是据Lax-Milgram对任意 $f$ 都能保证弱解存在唯一。

## 介绍

Lax-Milgram定理是泛函分析中关于双线性形式的变分问题的核心定理。它断言：在 Hilbert 空间上，满足强制性（coercivity）和有界性的双线性形式，对应的变分问题存在唯一解。这个定理是偏微分方程弱解理论（特别是椭圆型 PDE）的基石，为有限元方法提供了严格的理论基础。

## 分析

**前置依赖**：Riesz 表示定理、Hilbert 空间与内积、双线性形式的有界性与强制性、正交补与闭值域

**定理的精确表述**：设 $H$ 是 Hilbert 空间，$a: H \times H \to \mathbb{R}$ 是双线性形式，满足：

1. **有界性**：存在 $M > 0$ 使得 $|a(u, v)| \le M \|u\| \|v\|$ 对所有 $u, v \in H$ 成立；
2. **强制性（或称椭圆性，coercivity）**：存在 $\alpha > 0$ 使得 $a(u, u) \ge \alpha \|u\|^2$ 对所有 $u \in H$ 成立。

则对任意连续线性泛函 $f \in H^*$，变分问题

$$
\text{求 } u \in H \text{ 使得 } a(u, v) = f(v), \quad \forall v \in H
$$

存在唯一解 $u \in H$，且 $\|u\| \le \frac{1}{\alpha} \|f\|$。

**关键要点**：

- 强制性条件 $a(u, u) \ge \alpha \|u\|^2$ 是保证解存在性和唯一性的核心条件。
- 定理不要求 $a$ 对称——这比 Riesz 表示定理（要求内积，即对称正定双线性形式）更一般。
- 如果 $a$ 是对称的，则解 $u$ 还最小化能量泛函 $J(u) = \frac{1}{2}a(u, u) - f(u)$（Dirichlet 原理）。
- 解的先验估计 $\|u\| \le \|f\|/\alpha$ 是偏微分方程定性理论的基础。

## 思考过程

Lax-Milgram 定理的证明基于 Riesz 表示定理和 Banach 不动点定理（或 Lax-Milgram 引理），具体思路如下：

1. **转化为算子方程**：对每个固定的 $u \in H$，$v \mapsto a(u, v)$ 是 $H$ 上的连续线性泛函。由 Riesz 表示定理，存在唯一的 $A u \in H$ 使得 $a(u, v) = \langle A u, v \rangle$ 对所有 $v \in H$ 成立。$A: H \to H$ 是有界线性算子。

2. **验证算子的性质**：$A$ 满足 $\|A u\| \le M \|u\|$（有界性）和 $\langle A u, u \rangle \ge \alpha \|u\|^2$（强制性）。

3. **证明 $A$ 可逆**：需要证明 $A$ 是满射。利用强制性，$A$ 是单射且值域是闭的。若 $A$ 不是满射，则存在非零 $w \in \operatorname{Range}(A)^\perp$，计算 $\langle A w, w \rangle$ 导出矛盾。

4. **得到解**：由 Riesz 表示定理，存在 $y \in H$ 使得 $f(v) = \langle y, v \rangle$。则 $u = A^{-1} y$ 即为所求。

## 证明过程

**证明**：设 $H$ 是 Hilbert 空间，$a(\cdot, \cdot)$ 满足有界性和强制性条件，$f \in H^*$。

**步骤 1**：定义算子 $A: H \to H$。对固定的 $u \in H$，映射 $v \mapsto a(u, v)$ 是 $H$ 上的连续线性泛函（由有界性），其范数 $\le M \|u\|$。由 Riesz 表示定理，存在唯一的 $A u \in H$ 使得

$$
a(u, v) = \langle A u, v \rangle, \quad \forall v \in H.
$$

**步骤 2**：$A$ 的有界性。由 Riesz 表示定理的范数保持性，$\|A u\| = \|a(u, \cdot)\| \le M \|u\|$，故 $\|A\| \le M$，$A$ 连续。

**步骤 3**：$A$ 的强制性。由 $a$ 的强制性，

$$
\langle A u, u \rangle = a(u, u) \ge \alpha \|u\|^2.
$$

由此可得 $\|A u\| \ge \alpha \|u\|$（因为 $\|A u\| \|u\| \ge \langle A u, u \rangle \ge \alpha \|u\|^2$），故 $A$ 是单射且值域闭。

**步骤 4**：$A$ 是满射。设 $R = \operatorname{Range}(A)$。若 $R \neq H$，则存在非零 $w \in R^\perp$。由 $A$ 的定义，

$$
\alpha \|w\|^2 \le a(w, w) = \langle A w, w \rangle = 0,
$$

因为 $A w \in R$ 而 $w \in R^\perp$。故 $\|w\| = 0$，矛盾。因此 $R = H$，$A$ 是双射。

**步骤 5**：$A^{-1}$ 有界。由 $\|A u\| \ge \alpha \|u\|$ 得 $\|A^{-1} y\| \le \frac{1}{\alpha} \|y\|$。

**步骤 6**：求解变分问题。由 Riesz 表示定理，存在 $y \in H$ 使得 $f(v) = \langle y, v \rangle$ 对所有 $v \in H$ 成立。令 $u = A^{-1} y$，则

$$
a(u, v) = \langle A u, v \rangle = \langle y, v \rangle = f(v), \quad \forall v \in H.
$$

且 $\|u\| \le \frac{1}{\alpha} \|y\| = \frac{1}{\alpha} \|f\|$。

**步骤 7**：唯一性。若 $u_1, u_2$ 都是解，则 $a(u_1 - u_2, v) = 0$ 对所有 $v \in H$ 成立。取 $v = u_1 - u_2$，由强制性得 $\alpha \|u_1 - u_2\|^2 \le a(u_1 - u_2, u_1 - u_2) = 0$，故 $u_1 = u_2$。$\square$

**应用——椭圆边值问题**：考虑 Poisson 方程 $-\Delta u = f$ 在 $\Omega$ 上，$u|_{\partial\Omega} = 0$。其弱形式为：求 $u \in H_0^1(\Omega)$ 使得

$$
\int_\Omega \nabla u \cdot \nabla v \, dx = \int_\Omega f v \, dx, \quad \forall v \in H_0^1(\Omega).
$$

双线性形式 $a(u, v) = \int_\Omega \nabla u \cdot \nabla v$ 在 $H_0^1(\Omega)$ 上满足有界性和强制性（Poincaré 不等式），由 Lax-Milgram 定理知弱解存在唯一。