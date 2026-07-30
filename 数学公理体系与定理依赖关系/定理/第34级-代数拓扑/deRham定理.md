# de Rham 定理

## 一、定理介绍

de Rham 定理是微分几何和代数拓扑之间的核心桥梁，由 Georges de Rham 于 1931 年证明。该定理断言：光滑流形的 de Rham 上同调（通过微分形式定义）与奇异上同调（通过拓扑定义，实系数）自然同构，且环结构对应。

de Rham 定理将局部的微分信息与全局的拓扑性质联系起来，是 Hodge 理论、指标定理和现代数学物理的基础。它表明流形的拓扑不变量可以通过分析工具（微分形式和外微分）来计算。

## 二、原理思路

**核心思想**：通过积分映射建立 de Rham 上同调到奇异上同调的同构。

**关键观察**：
1. 闭微分形式可以通过积分定义奇异上循环
2. 恰当形式的积分为零（由 Stokes 定理），因此积分映射在 de Rham 上同调上良定
3. Poincaré 引理保证局部上闭形式都是恰当的，这用于证明单射性
4. 通过 Mayer-Vietoris 序列和五引理证明满射性

**证明策略**：
- 构造积分同态 $I: H^k_{\text{dR}}(M) \to H^k(M; \mathbb{R})$
- 利用 Mayer-Vietoris 序列的五引理证明 $I$ 是同构
- 通过 Poincaré 引理处理 contractible 开集
- 验证环结构对应：楔积对应杯积

## 三、定理的严格表述

**定理（de Rham）**：设 $M$ 是光滑流形。则存在自然同构
$$I: H^k_{\text{dR}}(M) \xrightarrow{\cong} H^k(M; \mathbb{R})$$
其中左边是 de Rham 上同调，右边是实系数奇异上同调。

**积分映射**：对闭 $k$-形式 $\omega \in Z^k_{\text{dR}}(M)$ 和奇异 $k$-循环 $c = \sum a_i \sigma_i \in Z_k(M)$，定义
$$I([\omega])([c]) = \sum a_i \int_{\sigma_i} \omega$$

**定理的加强形式**：

1. **环同构**：$I$ 是环同构，即 $I([\omega] \wedge [\eta]) = I([\omega]) \cup I([\eta])$

2. **自然性**：对光滑映射 $f: M \to N$，下图交换：
$$\begin{array}{ccc}
H^k_{\text{dR}}(N) & \xrightarrow{I} & H^k(N; \mathbb{R}) \\
\downarrow f^* & & \downarrow f^* \\
H^k_{\text{dR}}(M) & \xrightarrow{I} & H^k(M; \mathbb{R})
\end{array}$$

3. **Poincaré 对偶**：若 $M$ 是 $n$ 维紧致定向流形，则 de Rham 上同调的 Poincaré 对偶对应于奇异上同调的 Poincaré 对偶。

## 四、证明过程

**证明**：分几步进行。

**步骤 1**：构造积分映射。对闭 $k$-形式 $\omega$ 和奇异 $k$-单形 $\sigma: \Delta^k \to M$，定义 $\int_\sigma \omega$ 为通常的微分形式积分。

对奇异 $k$-链 $c = \sum a_i \sigma_i$，定义 $\langle I(\omega), c \rangle = \sum a_i \int_{\sigma_i} \omega$。

**步骤 2**：验证良定性。若 $\omega = d\eta$ 是恰当的，由 Stokes 定理，
$$\int_\sigma d\eta = \int_{\partial \sigma} \eta$$
若 $c$ 是循环（$\partial c = 0$），则 $\langle I(d\eta), c \rangle = \langle \eta, \partial c \rangle = 0$。因此 $I$ 在 de Rham 上同调上良定。

若 $c = \partial b$ 是边界，对闭形式 $\omega$，
$$\langle I(\omega), \partial b \rangle = \langle \delta I(\omega), b \rangle = \langle I(d\omega), b \rangle = 0$$
因此 $I$ 在奇异同调上良定。

**步骤 3**：证明 $I$ 是同构（对 contractible 空间）。若 $M$ 可缩，则 $H^k_{\text{dR}}(M) = 0$（Poincaré 引理）且 $H^k(M; \mathbb{R}) = 0$（$k \geq 1$）。$I$ 显然是同构。

**步骤 4**：Mayer-Vietoris 论证。设 $M = U \cup V$，$U, V$ 开。有 de Rham 的 Mayer-Vietoris 序列和奇异上同调的 Mayer-Vietoris 序列，且积分映射与这些序列交换：
$$\begin{array}{ccccccc}
\cdots \to & H^k_{\text{dR}}(M) & \to & H^k_{\text{dR}}(U) \oplus H^k_{\text{dR}}(V) & \to & H^k_{\text{dR}}(U \cap V) & \to \cdots \\
& \downarrow I_M & & \downarrow I_U \oplus I_V & & \downarrow I_{U \cap V} & \\
\cdots \to & H^k(M; \mathbb{R}) & \to & H^k(U; \mathbb{R}) \oplus H^k(V; \mathbb{R}) & \to & H^k(U \cap V; \mathbb{R}) & \to \cdots
\end{array}$$

**步骤 5**：五引理。若 $I_U, I_V, I_{U \cap V}$ 是同构，由五引理，$I_M$ 也是同构。

**步骤 6**：归纳论证。对 $M$ 进行三角剖分或用有限个 contractible 开集覆盖，通过逐步应用 Mayer-Vietoris 序列和五引理，证明 $I_M$ 是同构。

**步骤 7**：环结构对应。需要证明 $I([\omega] \wedge [\eta]) = I([\omega]) \cup I([\eta])$。

对奇异单形 $\sigma: \Delta^{p+q} \to M$，
$$\langle I(\omega \wedge \eta), \sigma \rangle = \int_\sigma \omega \wedge \eta$$

由 Eilenberg-Zilber 定理和 Alexander-Whitney 映射，
$$\int_\sigma \omega \wedge \eta = \int_{\sigma \circ \lambda_p} \omega \cdot \int_{\sigma \circ \rho_q} \eta = \langle I(\omega) \cup I(\eta), \sigma \rangle$$

因此 $I$ 是环同构。$\square$

**推论**：de Rham 上同调是拓扑不变量（同伦不变量）。

## 五、应用与意义

de Rham 定理在数学中有深远影响：

1. **计算方法**：提供了通过微分形式计算拓扑不变量的方法，使得上同调的计算可以用分析工具（如 Hodge 理论）。

2. **Hodge 理论**：在紧致 Riemann 流形上，每个 de Rham 上同调类有唯一的调和形式代表元（Hodge 定理）。

3. **特征类**：Chern-Weil 理论通过曲率形式构造特征类，这些类是 de Rham 上同调类，通过 de Rham 定理对应于拓扑特征类。

4. **指标定理**：Atiyah-Singer 指标定理的证明中，de Rham 定理用于将分析指标与拓扑指标联系起来。

5. **数学物理**：在规范理论和量子场论中，de Rham 定理用于理解规范不变量和拓扑不变量的关系。

6. **复几何**：Hodge 分解定理将 de Rham 上同调分解为 Dolbeault 上同调的直和，是复几何的核心工具。

7. **同伦论**：de Rham 定理的推广（如 rational homotopy theory）用于研究流形的有理同伦类型。

de Rham 定理的推广包括：带平坦丛系数的 de Rham 定理、等变 de Rham 定理、以及非交换几何中的推广。
