# Sobolev 空间定义

> **一句话大白话**：想让函数能"求导"却又允许它有尖角或跳跃，Sobolev 空间就按"弱导数也要平方可积"来收人：$W^{k,p}$ 表示连导数都敢积分到 $p$ 次的函数合集，导数概念因此被放宽却仍能用。
>
> **小例子**：$W^{k,p}(\Omega)=\{u\in L^p: D^\alpha u\in L^p,\ |\alpha|\le k\}$，其中 $D^\alpha u$ 取弱导数；如锯齿波 $|x|$ 属于 $H^1$（$=W^{1,2}$），尽管其点态导数在 0 处不存在。

## 介绍

Sobolev 空间是偏微分方程现代理论的核心函数空间，由 Sergei Sobolev 在 1930 年代引入。Sobolev 空间 $W^{k,p}(\Omega)$ 由所有直到 $k$ 阶的弱导数都属于 $L^p(\Omega)$ 的函数组成。它提供了研究 PDE 适定性的自然框架，使得 PDE 的解可以在广义函数意义下存在，同时又能保证足够的正则性。Sobolev 空间是现代偏微分方程理论和变分法的基石。

## 分析

**前置依赖**：Lebesgue 积分、$L^p$ 空间、分布（广义函数）、弱导数、完备度量空间。

**定理内容**：设 $\Omega \subseteq \mathbb{R}^n$ 是开集，$1 \le p \le \infty$，$k$ 为非负整数。

**弱导数的定义**：局部可积函数 $u \in L^1_{\text{loc}}(\Omega)$ 的 $\alpha$ 阶弱导数 $D^\alpha u$ 是满足下式的局部可积函数 $v$：
$$\int_\Omega v \varphi \, dx = (-1)^{|\alpha|} \int_\Omega u D^\alpha \varphi \, dx,\quad \forall \varphi \in C_c^\infty(\Omega)$$

**Sobolev 空间的定义**：
$$W^{k,p}(\Omega) = \{u \in L^1_{\text{loc}}(\Omega) \mid \text{对所有 } |\alpha| \le k,\ D^\alpha u \text{ 存在且 } D^\alpha u \in L^p(\Omega)\}$$
赋予范数
$$\|u\|_{W^{k,p}(\Omega)} = \left(\sum_{|\alpha| \le k} \|D^\alpha u\|_{L^p}^p\right)^{1/p},\quad 1 \le p < \infty$$
$$\|u\|_{W^{k,\infty}(\Omega)} = \max_{|\alpha| \le k} \|D^\alpha u\|_{L^\infty}$$

**$H^k(\Omega)$ 空间**：当 $p=2$ 时，记 $H^k(\Omega) = W^{k,2}(\Omega)$，它是 Hilbert 空间，内积为
$$(u,v)_{H^k} = \sum_{|\alpha| \le k} \int_\Omega D^\alpha u \cdot D^\alpha v \, dx$$

**数学内涵**：Sobolev 空间是 $C^k$ 空间的推广，但具有更好的完备性。$C^k$ 空间在 $W^{k,p}$ 范数下不完备，而 Sobolev 空间是 $C^k$ 或 $C_c^\infty$ 在该范数下的完备化。这使得我们可以用逼近方法处理 PDE。

**证明策略**：Sobolev 空间是 Banach 空间的证明依赖于 $L^p$ 空间的完备性。通过建立弱导数与 $L^p$ 收敛之间的关系，证明 Cauchy 列的极限的函数本身具有弱导数。

## 思考过程

Sobolev 空间的定义动机是解决 PDE 理论中函数空间不完备的问题。经典解要求函数有足够多的连续导数，但许多 PDE 的自然解并不满足这一条件。通过引入弱导数的概念，可以将 PDE 在分布意义下理解，从而在更大的函数类中寻找解。

弱导数的定义利用了分部积分公式：对 $\varphi \in C_c^\infty$，
$$\int_\Omega (D^\alpha u) \varphi \, dx = (-1)^{|\alpha|} \int_\Omega u D^\alpha \varphi \, dx$$
这个等式在经典情况下成立，现在我们用它来定义"导数"$D^\alpha u$。如果存在这样的 $v$，则称 $v$ 是 $u$ 的 $\alpha$ 阶弱导数。

$W^{k,p}$ 空间与 $C^k$ 空间的关键区别在于：
- $C^k$ 空间在 $W^{k,p}$ 范数下不完备
- $W^{k,p}$ 是完备化的结果
- 这使得极限运算在 Sobolev 空间中封闭

## 证明过程

**定理**：$W^{k,p}(\Omega)$ 在范数 $\|\cdot\|_{W^{k,p}}$ 下是 Banach 空间。

**证明**：

**步骤 1**：范数公理验证。$\|u\|_{W^{k,p}} = 0$ 当且仅当对所有 $|\alpha| \le k$，$\|D^\alpha u\|_{L^p} = 0$，即 $D^\alpha u = 0$ a.e.，从而 $u = 0$ a.e.。三角不等式和齐次性由 $L^p$ 范数的性质保证。

**步骤 2**：完备性。设 $\{u_m\}$ 是 $W^{k,p}(\Omega)$ 中的 Cauchy 列。则对每个 $|\alpha| \le k$，$\{D^\alpha u_m\}$ 是 $L^p(\Omega)$ 中的 Cauchy 列。由 $L^p$ 的完备性，存在 $u^{(\alpha)} \in L^p(\Omega)$ 使得 $D^\alpha u_m \to u^{(\alpha)}$ 在 $L^p$ 中。特别地，$u_m \to u = u^{(0)}$ 在 $L^p$ 中。

**步骤 3**：验证 $u^{(\alpha)} = D^\alpha u$。对任意 $\varphi \in C_c^\infty(\Omega)$，
$$\int_\Omega u^{(\alpha)} \varphi \, dx = \lim_{m \to \infty} \int_\Omega D^\alpha u_m \varphi \, dx = \lim_{m \to \infty} (-1)^{|\alpha|} \int_\Omega u_m D^\alpha \varphi \, dx = (-1)^{|\alpha|} \int_\Omega u D^\alpha \varphi \, dx$$
故 $u^{(\alpha)}$ 是 $u$ 的 $\alpha$ 阶弱导数。因此 $u \in W^{k,p}(\Omega)$，且 $u_m \to u$ 在 $W^{k,p}$ 中。$\square$

**定义**（$W_0^{k,p}(\Omega)$）：$W_0^{k,p}(\Omega)$ 是 $C_c^\infty(\Omega)$ 在 $W^{k,p}(\Omega)$ 中的闭包。它表示在边界上"消失"的 Sobolev 函数。

**例**：$H_0^1(\Omega) = W_0^{1,2}(\Omega)$ 是 Dirichlet 问题 $- \Delta u = f$ 变分提法的自然空间，其上的内积等价于 $(\nabla u, \nabla v)_{L^2}$。

**重要性质**：Sobolev 空间满足嵌入定理（Sobolev 嵌入定理），即当 $kp > n$ 时，$W^{k,p}(\Omega)$ 中的函数可嵌入到 $C(\overline{\Omega})$ 中，从而具有经典意义下的连续性。