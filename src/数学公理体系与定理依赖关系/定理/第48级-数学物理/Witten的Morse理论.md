# Witten的Morse理论

> **一句话大白话**：Witten 给 Morse 函数加上一个"能标度"$f/t$ 并把拉普拉斯算子扭转成 $d+d^*$ 的"弯曲版本"，让同调只在临界点附近"活"着——于是原本靠临界点分类的 Morse 理论变成了超对称量子力学里的"真空态"问题。
>
> **小例子**：Witten 变形 $d_t=e^{-tf}de^{tf}$ 使拉普莱斯算子的核（同调）集中在临界点，指标的大小由临界点的 Morse 指标 $i(p)$ 唯一决定，从而给出 Morse 不等式的解析证明。

## 介绍

Witten的Morse理论（Witten's Morse Theory）是 Edward Witten 在1982年提出的将 Morse 理论与量子力学超对称性相结合的革命性方法。传统的 Morse 理论通过光滑函数 $f: M \to \mathbb{R}$ 的临界点来研究流形 $M$ 的拓扑，而 Witten 通过引入"扭曲的" de Rham 复形 $e^{-f/\hbar} d e^{f/\hbar}$ 以及参数 $\hbar \to 0$ 的极限，将 Morse 不等式解释为量子力学中基态简并度的指标。Witten 的方法不仅给出了 Morse 不等式的"物理"证明，还建立了 Morse 理论与瞬子、隧道效应和超对称量子力学之间的深刻联系，并导致了 Floer 同调论的诞生。

## 分析

**前置依赖**：Morse 函数与 Morse 引理、Morse 指标、de Rham 上同调、Hodge 理论与 Hodge Laplacian、自伴算子的谱分析。

**定理的精确表述**（Morse 不等式）：设 $M$ 是紧致光滑流形，$f: M \to \mathbb{R}$ 是 Morse 函数（所有临界点非退化）。令 $c_k$ 为 $f$ 的指标为 $k$ 的临界点个数，$b_k = \dim H^k_{\mathrm{dR}}(M)$ 为 $M$ 的第 $k$ 个 Betti 数。则

$$
c_k \ge b_k, \quad \sum_{j=0}^k (-1)^{k-j} c_j \ge \sum_{j=0}^k (-1)^{k-j} b_j.
$$

**Witten 的重新诠释**：考虑扭曲的微分算子 $d_t = e^{-tf} d e^{tf}$，其伴随 $d_t^*$ 为 $e^{tf} d^* e^{-tf}$。则 Witten Laplacian 为 $\Delta_t = (d_t + d_t^*)^2$。当 $t \to \infty$ 时，$\Delta_t$ 的零空间集中在临界点附近，且 $\ker \Delta_t \cong H^*(M)$。

**依赖的概念**：Morse 函数、临界点、Morse 指标、de Rham 上同调、超对称量子力学。

**证明策略**：通过 Hodge 理论，将 de Rham 上同调等同于调和形式，再通过 Witten Laplacian 的谱分析将调和形式集中在临界点附近。

## 思考过程

Witten 的洞察是：算子 $d_t = e^{-tf} d e^{tf}$ 是 de Rham 复形的"扭变"，其 Hodge 理论仍然给出上同调。当 $t$ 很大时，Witten Laplacian $\Delta_t = (d_t + d_t^*)^2$ 的势能项 $t^2\|df\|^2 + t \cdot \mathrm{Hess}(f)$ 迫使低能态局域在 $f$ 的临界点附近（因为 $\|df\|^2 = 0$ 恰好是临界点条件）。

在临界点附近，$\Delta_t$ 近似为 $n$ 个独立的谐振子 Hamilton 量的直和，其零能态对应于 Morse 指标。严格的分析表明，随着 $t \to \infty$，$\Delta_t$ 的零空间维数正好等于 Betti 数，而每个临界点附近各有一个"拟零模式"，从而得到 Morse 不等式。

## 证明过程

**定理**（Morse 不等式）：设 $M$ 是紧流形，$f$ 是 Morse 函数，$c_k$ 为指标 $k$ 的临界点个数，$b_k$ 为第 $k$ 个 Betti 数。则 $c_k \ge b_k$。

**Witten 证明概要**：

**步骤 1：构造 Witten 复形。**

定义 $d_t = e^{-tf} d e^{tf}$，其中 $d$ 是 de Rham 外微分。则 $d_t^2 = 0$，且复形 $(\Omega^*(M), d_t)$ 的上同调同构于 de Rham 上同调（因为乘以 $e^{\pm tf}$ 是链等价）。

**步骤 2：Witten Laplacian。**

定义 Witten Laplacian 为

$$
\Delta_t = d_t d_t^* + d_t^* d_t = \Delta + t^2 \|df\|^2 + t \cdot \mathcal{L}_{\nabla f},
$$

其中 $\Delta$ 是通常的 Hodge Laplacian，$\mathcal{L}_{\nabla f}$ 是与 Hessian 相关的 Lie 导数项。

**步骤 3：谱分析。**

当 $t \to \infty$ 时，势能项 $t^2\|df\|^2$ 迫使 $\Delta_t$ 的低能本征态集中在满足 $\|df\|^2 = 0$ 的点，即 $f$ 的临界点。在临界点 $p$ 附近，通过 Morse 引理选取坐标 $(x^1, \ldots, x^n)$ 使得

$$
f(x) = f(p) - \sum_{i=1}^k (x^i)^2 + \sum_{i=k+1}^n (x^i)^2,
$$

其中 $k$ 是 Morse 指标。局域化分析表明，在该临界点附近，$\Delta_t$ 近似为谐振子 Hamilton 量

$$
\Delta_t \approx \sum_{i=1}^k \left( -\partial_i^2 + t^2 (x^i)^2 + t \right) + \sum_{i=k+1}^n \left( -\partial_i^2 + t^2 (x^i)^2 - t \right).
$$

**步骤 4：零能态计数。**

谐振子的基态能由 $\sum_i (\pm t)$ 给出。在 $k$ 个"不稳定"方向上有 $+t$ 贡献，在 $n-k$ 个"稳定"方向上有 $-t$ 贡献。因此，在 $p$ 附近，$\Delta_t$ 在 $k$-形式上的基态能趋于零，而在其他形式上的能隙为 $O(t)$。

当 $t \to \infty$ 时，$\Delta_t$ 的零空间由这些局域化模式张成，其维数正好等于 Betti 数 $b_k$。而每个指标为 $k$ 的临界点贡献一个 $k$-形式的拟零模式，故 $c_k \ge b_k$。

**步骤 5：Morse 不等式的强形式。**

通过考虑 Witten 复形的"扭变"版本，还可以证明强 Morse 不等式以及 Morse 等式

$$
\sum_{k=0}^n (-1)^k c_k = \sum_{k=0}^n (-1)^k b_k = \chi(M).
$$

$\square$

**推论**（Floer 同调）：Witten 的 Morse 理论启发了 Floer 在无穷维环空间上发展 Morse 理论，从而得到 Floer 同调，这成为证明 Arnold 猜想和构造 3-流形不变量的关键工具。