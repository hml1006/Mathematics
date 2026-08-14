# Lax-Milgram 定理 PDE 应用

## 介绍

Lax–Milgram 定理是泛函分析中关于双线性形式的存在性定理，由 Peter Lax 和 Arthur Milgram 在 1954 年提出。它是 PDE 理论中变分法（弱解方法）的核心工具，用于证明椭圆型 PDE 在 Sobolev 空间中弱解的存在唯一性。该定理将 PDE 的求解转化为双线性形式的适定性问题，是有限元方法的数学基础。

## 分析

**前置依赖**：Hilbert 空间、Riesz 表示定理、双线性形式、强制性和有界性、Sobolev 空间 $H^1$。

**定理内容**：设 $H$ 是实 Hilbert 空间，$a: H \times H \to \mathbb{R}$ 是双线性形式，满足：
1. **有界性**（连续性）：存在 $M > 0$ 使得 $|a(u,v)| \le M\|u\|\|v\|$ 对所有 $u,v \in H$。
2. **强制性**（椭圆性）：存在 $\alpha > 0$ 使得 $a(u,u) \ge \alpha\|u\|^2$ 对所有 $u \in H$。

则对任意有界线性泛函 $f \in H^*$，存在唯一的 $u \in H$ 使得
$$a(u,v) = f(v),\quad \forall v \in H$$

**PDE 应用**：考虑椭圆型边值问题
$$\begin{cases}
-\nabla \cdot (A(x)\nabla u) + b(x) \cdot \nabla u + c(x)u = f, & x \in \Omega \\
u = 0, & x \in \partial\Omega
\end{cases}$$
其中 $A(x)$ 是一致椭圆矩阵。其变分形式为：求 $u \in H_0^1(\Omega)$ 使得
$$a(u,v) = \int_\Omega fv \, dx,\quad \forall v \in H_0^1(\Omega)$$
其中
$$a(u,v) = \int_\Omega (A(x)\nabla u \cdot \nabla v + b(x) \cdot \nabla u \, v + c(x)uv) \, dx$$

**数学内涵**：Lax–Milgram 定理是 Riesz 表示定理的推广。Riesz 定理处理内积，而 Lax–Milgram 处理更一般的双线性形式。在 PDE 中，它提供了将微分方程转化为弱形式并保证解存在唯一的一般框架。

**证明策略**：对每个固定的 $u$，$v \mapsto a(u,v)$ 是 $H$ 上的有界线性泛函，由 Riesz 定理，存在 $Au \in H$ 使得 $a(u,v) = (Au, v)$。然后证明 $A$ 是有界线性算子且满足强制性条件，从而 $A$ 可逆。由 Riesz 定理，$f$ 对应 $w \in H$，则 $u = A^{-1}w$ 即为所求。

## 思考过程

Lax–Milgram 定理的证明巧妙地将双线性形式问题转化为算子方程问题。具体步骤：
1. 由 Riesz 表示定理，对每个 $u$，存在 $Au$ 使得 $a(u,v) = (Au, v)$。
2. $A$ 是线性有界算子，且强制性 $a(u,u) \ge \alpha\|u\|^2$ 意味着 $\|Au\| \ge \alpha\|u\|$，故 $A$ 是单射且值域闭。
3. 证明 $A$ 是满射：若 $A$ 的值域 $R(A) \neq H$，则存在非零 $w \perp R(A)$，但 $a(w,w) = (Aw,w) = 0$，与强制性矛盾。
4. 因此 $A$ 是双射，由 Riesz 定理找到 $u$ 使得 $Au = f$ 的 Riesz 代表元。

## 证明过程

**定理**（Lax–Milgram）：设 $H$ 是 Hilbert 空间，$a: H \times H \to \mathbb{R}$ 是有界强制的双线性形式，则对任意 $f \in H^*$，存在唯一的 $u \in H$ 使得 $a(u,v) = f(v)$ 对所有 $v \in H$ 成立。

**证明**：

**步骤 1**：定义算子 $A: H \to H$。对固定的 $u \in H$，映射 $v \mapsto a(u,v)$ 是 $H$ 上的有界线性泛函（因为 $|a(u,v)| \le M\|u\|\|v\|$）。由 Riesz 表示定理，存在唯一的 $Au \in H$ 使得
$$a(u,v) = (Au, v),\quad \forall v \in H$$

**步骤 2**：$A$ 是线性有界算子。线性性：$A(\lambda u_1 + u_2) = \lambda Au_1 + Au_2$ 由双线性性和 Riesz 表示的唯一性保证。有界性：
$$\|Au\| = \sup_{\|v\|=1} |(Au,v)| = \sup_{\|v\|=1} |a(u,v)| \le M\|u\|$$

**步骤 3**：$A$ 是单射且值域闭。由强制性，
$$\alpha\|u\|^2 \le a(u,u) = (Au,u) \le \|Au\|\|u\|$$
故 $\|Au\| \ge \alpha\|u\|$。因此 $A$ 是单射。若 $Au_n \to w$，则 $\{Au_n\}$ 是 Cauchy 列，由 $\|u_n - u_m\| \le \alpha^{-1}\|Au_n - Au_m\|$，$\{u_n\}$ 也是 Cauchy 列，$u_n \to u$，由连续性 $Au = w$，故值域 $R(A)$ 闭。

**步骤 4**：$A$ 是满射。假设 $R(A) \neq H$，则存在非零 $w \in R(A)^\perp$。但
$$\alpha\|w\|^2 \le a(w,w) = (Aw,w) = 0$$
矛盾。故 $R(A) = H$，$A$ 是双射。

**步骤 5**：存在唯一性。对任意 $f \in H^*$，由 Riesz 定理，存在 $w \in H$ 使得 $f(v) = (w,v)$。令 $u = A^{-1}w$，则
$$a(u,v) = (Au,v) = (w,v) = f(v)$$
唯一性由 $A$ 的单射性保证。$\square$

**PDE 应用**：对椭圆算子 $Lu = -\Delta u + cu$（$c \ge 0$），定义
$$a(u,v) = \int_\Omega (\nabla u \cdot \nabla v + cuv) \, dx$$
在 $H_0^1(\Omega)$ 上，$a$ 有界且强制（由 Poincaré 不等式），故对任意 $f \in L^2(\Omega)$，存在唯一的 $u \in H_0^1(\Omega)$ 满足
$$\int_\Omega (\nabla u \cdot \nabla v + cuv) \, dx = \int_\Omega fv \, dx,\quad \forall v \in H_0^1(\Omega)$$
即 Poisson 方程 $-\Delta u + cu = f$ 存在唯一的弱解。$\square$