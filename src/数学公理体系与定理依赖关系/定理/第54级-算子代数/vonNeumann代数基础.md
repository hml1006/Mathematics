# von Neumann 代数基础

> **一句话大白话**：von Neumann 代数就是"一族可相加相乘、且取强极限也关在里面的算子大本营"，处处装满了"开关"（投影），核心是二次交换子定理。
>
> **小例子**：全体有界算子 $B(H)$（如 $H$ 有限维时的 $M_n(\mathbb{C})$）自身就是 von Neumann 代数；对角阵代数是 $M_n(\mathbb{C})$ 的一个交换子代数。

## 一、定理介绍

von Neumann 代数是算子代数理论中的一个核心概念，它是 Hilbert 空间上有界线性算子代数 $B(H)$ 的弱算子拓扑（或等价地，强算子拓扑）下的闭 *-子代数，且包含恒等算子。von Neumann 代数最早由 John von Neumann 在 1929 年至 1931 年间引入，当时称为"环"（Ringe），后来为与抽象的 C*-代数区分，改称为 von Neumann 代数。

von Neumann 代数与 C*-代数的主要区别在于拓扑条件：C*-代数要求范数拓扑下的闭性，而 von Neumann 代数要求更弱的弱算子拓扑下的闭性。这一更强的条件使得 von Neumann 代数具有更丰富的结构和更精细的分类。

## 二、原理思路

von Neumann 代数的理论基础建立在以下几个关键概念之上：

1. **算子拓扑**：$B(H)$ 上可以定义多种拓扑，从强到弱依次为：范数拓扑、强算子拓扑 (SOT)、弱算子拓扑 (WOT)、ultraweak 拓扑、ultrastrong 拓扑。von Neumann 代数关于 WOT 和 SOT 的闭性是等价的。

2. **交换子与双交换子**：对 $B(H)$ 的子集 $S$，其交换子 $S'$ 是所有与 $S$ 中元素交换的算子的集合。双交换子定理（von Neumann 双交换子定理）表明：包含恒等算子的 *-子代数 $M$ 是 von Neumann 代数当且仅当 $M = M''$。

3. **投影格**：von Neumann 代数中的投影算子（满足 $p = p^* = p^2$）构成一个完备格，这个格结构是分类的基础。

4. **正规泛函**：von Neumann 代数上的正规线性泛函是在 ultraweak 拓扑下连续的泛函，它们构成了 von Neumann 代数的预对偶空间。

## 三、定理的严格表述

**定义 1（von Neumann 代数）**：设 $H$ 是 Hilbert 空间，$B(H)$ 是 $H$ 上有界线性算子的代数。$B(H)$ 的子代数 $M$ 称为 von Neumann 代数，如果满足以下条件之一（它们等价）：
1. $M$ 在弱算子拓扑 (WOT) 下是闭的，且 $I \in M$
2. $M$ 在强算子拓扑 (SOT) 下是闭的，且 $I \in M$
3. $M = M''$（双交换子条件），其中 $M' = \{T \in B(H) : TS = ST, \forall S \in M\}$
4. $M$ 是某个自伴算子集 $S \subset B(H)$ 的交换子 $S'$

**定理 1（von Neumann 双交换子定理）**：设 $M$ 是 $B(H)$ 的包含恒等算子 $I$ 的 *-子代数。则以下条件等价：
1. $M$ 在弱算子拓扑下闭
2. $M$ 在强算子拓扑下闭
3. $M = M''$（即 $M$ 等于其双交换子）

**定理 2（投影的存在性）**：设 $M$ 是 von Neumann 代数，$E \in M$ 是任意非零元素。则存在非零投影 $p \in M$ 使得 $p \le E^*E / \|E^*E\|$。特别地，von Neumann 代数包含足够多的投影。

**定理 3（预对偶空间）**：设 $M$ 是 von Neumann 代数，则存在唯一的 Banach 空间 $M_*$（称为 $M$ 的预对偶），使得 $M_*^* \cong M$（等距同构）。$M_*$ 中的元素称为 $M$ 上的正规泛函。

**定理 4（Kaplansky 密度定理）**：设 $M$ 是 von Neumann 代数，$M_0$ 是 $M$ 的 *-子代数且 $M_0'' = M$。则 $M_0$ 的单位球在 $M$ 的单位球中关于强算子拓扑是稠密的。

## 四、证明过程

**定理 1 的证明（von Neumann 双交换子定理）**：

**步骤 1：(1) $\Rightarrow$ (3)**

设 $M$ 在 WOT 下闭。显然 $M \subset M''$。要证 $M'' \subset M$。

设 $T \in M''$，要证 $T \in M$（即 $T$ 在 WOT 下属于 $M$ 的闭包）。

取 $\xi_1, \ldots, \xi_n \in H$ 和 $\epsilon > 0$，要证存在 $A \in M$ 使得 $\|(T - A)\xi_i\| < \epsilon$，$i = 1, \ldots, n$。

考虑 $H^n = H \oplus \cdots \oplus H$（$n$ 个直和），定义 $\pi : B(H) \to B(H^n)$ 为 $\pi(A) = A \oplus \cdots \oplus A$。

令 $M^{(n)} = \pi(M)$，则 $M^{(n)}$ 是 $B(H^n)$ 的 *-子代数。

向量 $\xi = (\xi_1, \ldots, \xi_n) \in H^n$，$M^{(n)}\xi$ 是 $H^n$ 的闭凸子集（因为 $M$ 是 *-代数，$M^{(n)}\xi$ 是子空间）。

由投影定理，存在 $M^{(n)}\xi$ 中离 $T^{(n)}\xi = (T\xi_1, \ldots, T\xi_n)$ 最近的向量 $A_0\xi$，其中 $A_0 \in M^{(n)}$。

设 $P$ 是 $M^{(n)}\xi$ 上的正交投影，则 $P \in (M^{(n)})'$。

由于 $T \in M''$，$T^{(n)} \in (M^{(n)})''$，$T^{(n)}$ 与 $(M^{(n)})'$ 中元素交换，故 $T^{(n)}P = PT^{(n)}$。

因此 $T^{(n)}\xi = T^{(n)}P\xi = PT^{(n)}\xi \in M^{(n)}\xi$。

故存在 $A \in M$ 使得 $A\xi_i = T\xi_i$，$i = 1, \ldots, n$。这说明 $T$ 在 SOT（从而在 WOT）下属于 $M$ 的闭包。

**步骤 2：(3) $\Rightarrow$ (2)**

设 $M = M''$。对任意 $T \in M'$，$\ker T$ 和 $\text{ran}(T)$ 的性质：

若 $A \in M$，$\xi \in \ker T$，则 $T(A\xi) = A(T\xi) = 0$，故 $A(\ker T) \subset \ker T$。

这说明 $\ker T$ 在 $M$ 的作用下不变，故 $\ker T$ 上的正交投影 $P_{\ker T} \in M'$.

对任意 $\xi \in H$，$\xi - P_{\overline{M\xi}}\xi \perp M\xi$，特别地对所有 $A \in M$，$\langle \xi - P_{\overline{M\xi}}\xi, A\xi \rangle = 0$。

这说明 $P_{\overline{M\xi}} \in M'$，故 $\overline{M\xi}$ 在 $M$ 的作用下不变。

现在设 $T \in M''$，要证 $T$ 在 SOT 下属于 $M$。

对任意 $\xi \in H$，$\overline{M\xi}$ 是 $M$-不变子空间，其投影 $P \in M'$。

由于 $T \in M'' = (M')'$，$T$ 与 $P$ 交换，故 $T\xi = TP\xi = PT\xi \in \overline{M\xi}$。

因此对任意 $\epsilon > 0$，存在 $A \in M$ 使得 $\|T\xi - A\xi\| < \epsilon$。

对有限个向量 $\xi_1, \ldots, \xi_n$，考虑直和论证（同步骤 1），可得 $T$ 在 SOT 下属于 $M$。

**步骤 3：(2) $\Rightarrow$ (1)**

SOT 比 WOT 更强，故 SOT 闭蕴含 WOT 闭。$\square$

**定理 3 的证明（预对偶的存在性）**：

**步骤 1：正规泛函的定义**

$M$ 上的线性泛函 $\phi$ 称为正规的，如果对 $M$ 中任意有界递增网 $(x_\alpha)$ 且 $x_\alpha \nearrow x$（SOT 收敛），有 $\phi(x_\alpha) \to \phi(x)$。

等价地，$\phi$ 在 ultraweak 拓扑下连续。

**步骤 2：构造预对偶**

$M$ 作为 $B(H)$ 的子空间，继承 $B(H)$ 的 ultraweak 拓扑。

$B(H)$ 的预对偶是迹类算子空间 $L^1(H)$，通过配对 $\langle T, \rho \rangle = \text{tr}(T\rho)$ 实现 $B(H) \cong L^1(H)^*$。

$M_*$ 定义为 $M$ 上所有正规泛函的空间，可以证明 $M_* \cong M^* / M_\perp$，其中 $M_\perp$ 是 $M^*$ 中在 $M$ 上为零的泛函。

由 Banach 空间对偶理论，$M \cong M_*^*$。$\square$

## 五、应用与意义

von Neumann 代数在数学和物理学中有广泛的应用：

1. **因子分类**：von Neumann 代数的中心为 $\mathbb{C}I$ 时称为因子。Murray 和 von Neumann 将因子分为 I 型、II 型、III 型，这一分类在遍历理论和量子场论中有重要应用。

2. **遍历理论**：测度空间上的保测变换群作用产生 von Neumann 代数（群测度空间构造），遍历性质与因子的类型密切相关。

3. **量子统计力学**：von Neumann 代数为无穷多自由度的量子系统提供了严格的数学框架。Tomita-Takesaki 模理论描述了热平衡态的时间演化。

4. **局部量子物理**：在代数量子场论中，时空区域对应 von Neumann 代数，因果性条件表现为代数的交换性。

5. **随机矩阵理论**：自由概率论中，von Neumann 代数（特别是 II$_1$ 因子）是研究大随机矩阵极限行为的自然框架。

6. ** knot 理论**：Jones 多项式的发现源于 von Neumann 代数（II$_1$ 因子）的研究，展示了算子代数与低维拓扑的意外联系。

7. **非交换测度论**：von Neumann 代数可以视为"非交换测度空间"，II$_1$ 因子上的迹对应于有限测度，正规态对应于概率测度。

von Neumann 代数理论是 20 世纪数学的重要成就，它深刻联系了泛函分析、群论、遍历理论、几何和数学物理。
