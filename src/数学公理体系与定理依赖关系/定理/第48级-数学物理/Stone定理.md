# Stone定理

> **一句话大白话**：量子力学里"时间演化"本质是一个单参数酉群 $U(t)$，Stone 定理说"能连续运行且彼此可对易的一族酉算子，可以（且必然）由一个（无界自伴）生成元 $H$ 写成 $e^{-itH}$"——把演化与能量连起来。
>
> **小例子**：$U(t)=e^{-itH}$ 是强连续的酉群当且仅当 $H$ 是自伴算子；反过来说任何强连续单参数酉群都可表为某个自伴 $H$ 的指数，这定义了量子系统的哈密顿量。

## 介绍

Stone定理（Stone's Theorem）是泛函分析和量子力学中关于强连续单参数酉群的基本定理，由 Marshall Stone 在1932年证明。该定理断言：Hilbert空间 $\mathcal{H}$ 上的每个强连续单参数酉群 $\{U(t)\}_{t \in \mathbb{R}}$ 都唯一地对应于一个自伴算子 $A$，使得 $U(t) = e^{itA}$。反之，每个自伴算子 $A$ 通过指数映射生成一个强连续单参数酉群。Stone定理为量子力学中时间演化的数学描述提供了严格框架——系统的酉演化由 Hamiltonian 算子生成，是薛定谔方程解的数学基础。

## 分析

**前置依赖**：Hilbert 空间与酉算子、强连续单参数酉群、无界自伴算子与 Cayley 变换、谱定理。

**定理的精确表述**：设 $\{U(t)\}_{t \in \mathbb{R}}$ 是 Hilbert 空间 $\mathcal{H}$ 上的强连续单参数酉群，即：
1. 每个 $U(t): \mathcal{H} \to \mathcal{H}$ 是酉算子。
2. $U(0) = I$，$U(s + t) = U(s)U(t)$ 对所有 $s, t \in \mathbb{R}$。
3. 对每个 $x \in \mathcal{H}$，映射 $t \mapsto U(t)x$ 是连续的。

则存在唯一的自伴算子 $A$（可能无界）使得 $U(t) = e^{itA}$。算子 $A$ 的定义域为

$$
\mathcal{D}(A) = \left\{ x \in \mathcal{H} : \lim_{t \to 0} \frac{U(t)x - x}{it} \text{ 存在} \right\},
$$

且 $A$ 由 $Ax = \lim_{t \to 0} \frac{U(t)x - x}{it}$ 给出。反之，如果 $A$ 是自伴算子，则 $U(t) = e^{itA}$ 定义了一个强连续单参数酉群。

**依赖的概念**：自伴算子、酉算子、谱定理、强连续半群、Hilbert空间。

**证明策略**：利用谱定理定义 $A$ 为 $\int \lambda \, dE(\lambda)$，然后验证 $U(t) = \int e^{it\lambda} \, dE(\lambda)$。

## 思考过程

Stone定理的核心是自伴算子与酉群之间的"生成"关系。直观上，$U(t) = e^{itA}$ 的微分给出 $U'(0) = iA$，因此 $A$ 是酉群的"无穷小生成元"。

证明的难点在于从群 $\{U(t)\}$ 恢复出算子 $A$。Stone的原始证明使用谱分析，而现代证明常常利用谱定理直接构造。关键洞察是：单参数酉群的交换性 $U(s)U(t) = U(s+t)$ 等价于其生成元是自伴的。

## 证明过程

**定理**（Stone定理）：设 $\{U(t)\}_{t \in \mathbb{R}}$ 是 $\mathcal{H}$ 上的强连续单参数酉群。则存在唯一的自伴算子 $A$ 使得 $U(t) = e^{itA}$。

**证明**：

**步骤 1：定义生成元。**

定义算子 $A$ 为

$$
\mathcal{D}(A) = \left\{ x \in \mathcal{H} : \lim_{t \to 0} \frac{U(t)x - x}{it} \text{ 存在} \right\},
$$

对 $x \in \mathcal{D}(A)$，定义 $Ax = \lim_{t \to 0} \frac{U(t)x - x}{it}$。

**步骤 2：证明 $A$ 是闭稠定对称算子。**

由强连续性，$\mathcal{D}(A)$ 在 $\mathcal{H}$ 中稠密。对 $x, y \in \mathcal{D}(A)$，

$$
\langle Ax, y \rangle = \lim_{t \to 0} \left\langle \frac{U(t)x - x}{it}, y \right\rangle = \lim_{t \to 0} \left\langle x, \frac{U(-t)y - y}{-it} \right\rangle = \langle x, Ay \rangle.
$$

故 $A$ 对称。可以证明 $A$ 是闭算子。

**步骤 3：证明 $A$ 自伴。**

需要证明 $\mathcal{D}(A^*) = \mathcal{D}(A)$。等价地，证明 $A \pm iI$ 是满射。对任意 $y \in \mathcal{H}$，定义

$$
x = \int_0^\infty e^{-t} U(t)y \, dt.
$$

可以验证 $x \in \mathcal{D}(A)$ 且 $(A + iI)x = y$。故 $A + iI$ 满射，同理 $A - iI$ 满射，因此 $A$ 自伴。

**步骤 4：利用谱定理构造 $U(t)$。**

由谱定理，$A = \int_{\mathbb{R}} \lambda \, dE(\lambda)$。定义 $V(t) = \int_{\mathbb{R}} e^{it\lambda} \, dE(\lambda)$，则 $\{V(t)\}$ 是强连续单参数酉群，且由步骤1中的生成元也是 $A$。由生成元的唯一性，$U(t) = V(t) = e^{itA}$。$\square$

**推论**：Stone定理建立了酉表示与自伴算子之间的一一对应。在量子力学中，时间演化 $U(t) = e^{-iHt/\hbar}$ 由 Hamiltonian 算子 $H$ 生成，薛定谔方程 $i\hbar \frac{d}{dt}\psi = H\psi$ 的解正是 $U(t)\psi_0$。