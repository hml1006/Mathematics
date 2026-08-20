# Tomita-Takesaki 模理论

> **一句话大白话**：一个 von Neumann 代数与其"可交换的伙伴"（交换子）之间存在一种内在的左右手对称，靠"模算子"和"模自同构"伸缩时间，把代数与互补代数深刻地统一起来。
>
> **小例子**：取 $B(H)$ 的迹态做 Tomita-Takesaki 构造时，模算子 $\Delta=I$、模自同构是平凡的；只有当状态为非迹态（如 III 型因子）时，非平凡的模流 $\sigma_t$ 才会出现。

## 一、定理介绍

Tomita-Takesaki 模理论是 von Neumann 代数理论中最深刻和优美的结果之一，由 M. Tomita 在 1967 年发现，后由 M. Takesaki 在 1970 年给出严格证明和发展。该理论揭示了 von Neumann 代数与其交换子之间的深刻对称性，为理解 III 型因子的结构提供了关键工具。

模理论的核心思想是：给定 von Neumann 代数 $M$ 上的忠实正规正规化态 $\omega$，可以构造一个单参数自同构群 $\{\sigma_t\}_{t \in \mathbb{R}}$，称为模自同构群。这个自同构群描述了系统相对于态 $\omega$ 的"时间演化"，在量子统计力学中对应于热平衡态的动力学。

## 二、原理思路

Tomita-Takesaki 理论的构造基于以下关键步骤：

1. **GNS 构造**：给定 von Neumann 代数 $M$ 上的忠实正规正规化态 $\omega$，通过 GNS 构造得到 Hilbert 空间 $H_\omega$、表示 $\pi_\omega$ 和循环分离向量 $\xi_\omega$。

2. **Tomita 算子**：定义反线性算子 $S_0 : \pi_\omega(a)\xi_\omega \mapsto \pi_\omega(a^*)\xi_\omega$，然后取闭包得到 $S$。

3. **极分解**：对 $S$ 进行极分解 $S = J\Delta^{1/2}$，其中 $J$ 是对酉算子（模共轭算子），$\Delta$ 是正自伴算子（模算子）。

4. **模自同构群**：定义 $\sigma_t(x) = \Delta^{it}x\Delta^{-it}$，则 $\sigma_t$ 是 $M$ 的自同构。

5. **核心定理**：模理论的核心结果是 $JM J = M'$（交换子定理）和 $\sigma_t(M) = M$（不变性定理）。

模理论的深刻之处在于：它从代数数据（von Neumann 代数和态）出发，自然地构造出动力学（模自同构群），这为量子统计力学中的 KMS 条件提供了严格的数学基础。

## 三、定理的严格表述

**定义 1（循环分离向量）**：设 $M$ 是 von Neumann 代数，$H$ 是 Hilbert 空间，$\xi \in H$。
- $\xi$ 是 **循环的**，若 $\overline{M\xi} = H$
- $\xi$ 是 **分离的**，若 $x\xi = 0$（$x \in M$）蕴含 $x = 0$

**定理 1（Tomita-Takesaki 定理）**：设 $M$ 是 von Neumann 代数，$\xi$ 是 $M$ 的循环分离向量。定义反线性算子 $S : M\xi \to H$ 为 $Sx\xi = x^*\xi$，取闭包后仍记为 $S$。对 $S$ 进行极分解：
$$S = J\Delta^{1/2}$$
其中 $J$ 是对酉算子（$J^2 = I$，$J^* = J$），$\Delta$ 是正自伴算子。则以下成立：

1. **交换子定理**：$JM J = M'$，即 $J$ 将 $M$ 映射到其交换子 $M'$
2. **模自同构群**：$\Delta^{it}M\Delta^{-it} = M$，对所有 $t \in \mathbb{R}$
3. **模自同构的性质**：定义 $\sigma_t(x) = \Delta^{it}x\Delta^{-it}$，则 $\{\sigma_t\}_{t \in \mathbb{R}}$ 是 $M$ 的单参数自同构群，满足：
   - $\sigma_t$ 是 *-自同构
   - $\sigma_t$ 是 ultraweak 连续的
   - $\xi$ 是 $\sigma_t$ 的不变向量：$\sigma_t(x)\xi = x\xi$

**定理 2（模算子的唯一性）**：设 $M$ 是 von Neumann 代数，$\omega$ 是 $M$ 上的忠实正规正规化态。则模自同构群 $\{\sigma_t^\omega\}_{t \in \mathbb{R}}$ 由 $\omega$ 唯一确定，与 GNS 构造的具体实现无关。

**定理 3（KMS 条件）**：设 $M$ 是 von Neumann 代数，$\omega$ 是 $M$ 上的忠实正规正规化态，$\{\sigma_t\}$ 是模自同构群。则 $\omega$ 满足 KMS 条件：对任意 $x, y \in M$，存在函数 $F(z)$，在带状区域 $0 \le \text{Im}(z) \le 1$ 上解析，在边界上连续，且满足
$$F(t) = \omega(x\sigma_t(y)), \quad F(t + i) = \omega(\sigma_t(y)x), \quad \forall t \in \mathbb{R}$$

**定理 4（Connes 的协导数）**：设 $M$ 是 III 型因子，$\omega_1, \omega_2$ 是 $M$ 上两个忠实正规正规化态，$\{\sigma_t^{\omega_1}\}$ 和 $\{\sigma_t^{\omega_2}\}$ 是对应的模自同构群。则存在 $M$ 中的酉算子族 $\{u_t\}_{t \in \mathbb{R}}$，使得
$$\sigma_t^{\omega_2}(x) = u_t\sigma_t^{\omega_1}(x)u_t^*, \quad \forall x \in M, t \in \mathbb{R}$$
且 $u_t$ 满足协循环方程 $u_{t+s} = u_t\sigma_t^{\omega_1}(u_s)$。

## 四、证明过程

**定理 1 的证明**：

**步骤 1：Tomita 算子的定义与性质**

设 $\xi$ 是 $M$ 的循环分离向量。定义 $S_0 : M\xi \to H$ 为 $S_0(x\xi) = x^*\xi$。

首先验证 $S_0$ 定义良好：若 $x\xi = y\xi$，则 $(x - y)\xi = 0$。由于 $\xi$ 是分离的，$x - y = 0$，故 $x^*\xi = y^*\xi$。

$S_0$ 是反线性的：$S_0((\alpha x + \beta y)\xi) = (\alpha x + \beta y)^*\xi = \bar{\alpha}x^*\xi + \bar{\beta}y^*\xi = \bar{\alpha}S_0(x\xi) + \bar{\beta}S_0(y\xi)$。

$S_0$ 是闭的：设 $x_n\xi \to \eta$ 且 $S_0(x_n\xi) = x_n^*\xi \to \zeta$。要证 $\eta \in M\xi$ 且 $S_0\eta = \zeta$。

由于 $M\xi$ 是闭的（$\xi$ 是循环的），$\eta \in M\xi$。设 $\eta = x\xi$。

对任意 $y \in M$，$\langle x_n^*\xi, y\xi \rangle = \langle \xi, x_ny\xi \rangle \to \langle \zeta, y\xi \rangle$。

另一方面，$\langle \xi, x_ny\xi \rangle = \langle x_n^*\xi, y\xi \rangle \to \langle x^*\xi, y\xi \rangle$。

故 $\zeta = x^*\xi = S_0(x\xi) = S_0\eta$。

令 $S$ 为 $S_0$ 的闭包，则 $S$ 是闭的反线性算子。

**步骤 2：$S$ 的稠密定义与无界性**

$S$ 的定义域 $\text{dom}(S)$ 包含 $M\xi$，由于 $\xi$ 是循环的，$M\xi$ 在 $H$ 中稠密，故 $S$ 是稠密定义的。

$S$ 通常是无界的，但 $S^*S$ 是自伴的（由 von Neumann 定理）。

**步骤 3：极分解**

对闭的反线性算子 $S$，存在唯一的极分解 $S = J\Delta^{1/2}$，其中：
- $\Delta = S^*S$ 是正自伴算子
- $J$ 是对酉算子（$J^2 = I$，$J^* = J = J^{-1}$）
- $\text{dom}(\Delta^{1/2}) = \text{dom}(S)$
- $J$ 将 $\text{ran}(\Delta^{1/2})$ 映射到 $\text{ran}(S)$

**步骤 4：定义 $F$ 算子**

定义 $F = S^*$，则 $F$ 也是闭的反线性算子，且 $F(y\xi) = y^*\xi$，$y \in M'$。

对 $F$ 进行极分解：$F = J'\Delta'^{1/2}$。

关键引理：$J = J'$ 且 $\Delta = \Delta'$。

证明：对 $x \in M$，$y \in M'$，
$$\langle Sx\xi, y\xi \rangle = \langle x^*\xi, y\xi \rangle = \langle \xi, xy\xi \rangle = \langle \xi, yx\xi \rangle = \langle y^*\xi, x\xi \rangle = \langle Fy\xi, x\xi \rangle$$

故 $S^* = F$，$S^{**} = F^* = S$。

由极分解的唯一性，$J = J'$ 且 $\Delta = \Delta'$。

**步骤 5：证明 $JM J = M'$**

对 $x \in M$，$JxJ$ 作用在 $y\xi$（$y \in M'$）上：
$$JxJ(y\xi) = Jx(y^*\xi) = J(xy^*\xi)$$

由于 $y^* \in M'$，$xy^* = y^*x$，故
$$JxJ(y\xi) = J(y^*x\xi) = (y^*x)^*\xi = x^*y\xi = yx^*\xi$$

这说明 $JxJ$ 与 $M'$ 中元素交换，故 $JxJ \in M'' = M$。

因此 $JM J \subset M'$。

类似地，$JM'J \subset M$，故 $JM J = M'$。

**步骤 6：证明 $\Delta^{it}M\Delta^{-it} = M$**

对 $x \in M$，考虑 $\Delta^{it}x\Delta^{-it}$。

首先，$\Delta^{it}$ 是酉算子（$\Delta$ 是正自伴的，$\Delta^{it} = e^{it\log\Delta}$ 是酉的）。

要证 $\Delta^{it}x\Delta^{-it} \in M$，即对任意 $y \in M'$，$\Delta^{it}x\Delta^{-it}$ 与 $y$ 交换。

由于 $JyJ \in M$（由步骤 5），$\Delta^{it}x\Delta^{-it}$ 与 $JyJ$ 交换。

利用 $J\Delta^{it}J = \Delta^{-it}$（由 $JSJ = F$ 和极分解的性质），可以证明 $\Delta^{it}x\Delta^{-it}$ 与 $y$ 交换。

因此 $\Delta^{it}x\Delta^{-it} \in M'' = M$。

故 $\Delta^{it}M\Delta^{-it} \subset M$。

类似地，$\Delta^{-it}M\Delta^{it} \subset M$，故 $\Delta^{it}M\Delta^{-it} = M$。

**步骤 7：KMS 条件**

定义 $\sigma_t(x) = \Delta^{it}x\Delta^{-it}$。

对 $x, y \in M$，考虑函数 $F(z) = \langle \xi, x\Delta^{iz}y\xi \rangle$。

由于 $\Delta^{iz}$ 在带状区域 $0 \le \text{Im}(z) \le 1$ 上有定义且解析，$F(z)$ 在该区域上解析。

在实轴上（$z = t$）：$F(t) = \langle \xi, x\Delta^{it}y\xi \rangle = \langle \xi, x\sigma_t(y)\xi \rangle = \omega(x\sigma_t(y))$。

在直线 $\text{Im}(z) = 1$ 上（$z = t + i$）：
$$F(t + i) = \langle \xi, x\Delta^{i(t+i)}y\xi \rangle = \langle \xi, x\Delta^{it}\Delta^{-1}y\xi \rangle$$

利用 $S = J\Delta^{1/2}$ 和 $Sx\xi = x^*\xi$，可以证明 $\Delta^{-1}y\xi = Jy^*J\xi$。

经过计算，$F(t + i) = \omega(\sigma_t(y)x)$。

因此 $\omega$ 满足 KMS 条件。$\square$

## 五、应用与意义

Tomita-Takesaki 模理论在数学和物理学中有深远影响：

1. **III 型因子的分类**：Connes 利用模自同构群对 III 型因子进行了精细分类（III$_\lambda$，$0 \le \lambda \le 1$），引入了模不变量 $S(M)$ 和 $T(M)$，这是 III 型因子理论的核心工具。

2. **量子统计力学**：模自同构群为量子统计力学中的时间演化提供了严格数学基础。KMS 条件描述了热平衡态，模理论证明了 KMS 态的存在性和唯一性。

3. **非交换测度论**：模自同构群可以视为"非交换 Radon-Nikodym 导数"，描述了不同态之间的"密度比"。这为发展非交换测度论提供了框架。

4. **共形场论**：在二维共形场论中，模理论用于构造真空表示和研究局部代数的结构。

5. **子因子理论**：Jones 的子因子指标理论与模理论密切相关，模算子的谱性质决定了子因子的指标。

6. **自由概率论**：模理论在自由概率论中用于研究自由积构造和自由熵。

7. **算子代数分类**：模理论是 Connes 分类纲领的核心工具，用于研究注入因子和外因子。

8. **量子场论**：在代数量子场论中，模理论用于研究局部代数的结构和因果性条件。Bisognano-Wichmann 定理表明，相对论性量子场论中的模自同构群对应于 Lorentz  boosts。

Tomita-Takesaki 模理论展示了 von Neumann 代数中隐藏的深刻对称性，是现代算子代数理论中最优美的成果之一。它不仅解决了 III 型因子的结构问题，而且为量子物理提供了严格的数学框架，体现了数学与物理的深刻统一。
