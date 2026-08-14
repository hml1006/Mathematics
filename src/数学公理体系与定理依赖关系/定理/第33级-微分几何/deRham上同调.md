# de Rham 上同调

## 一、定理介绍

de Rham 上同调是微分几何和代数拓扑中的核心概念，由 Georges de Rham 于 1931 年系统发展。它通过微分形式的外微分算子定义流形的上同调群，将局部微分信息与全局拓扑性质联系起来。

de Rham 定理（将在后续章节详述）证明了 de Rham 上同调与奇异上同调（实系数）同构，建立了微分几何与代数拓扑之间的深刻桥梁。de Rham 上同调是 Hodge 理论、指标定理和现代数学物理的基础工具。

## 二、原理思路

**核心思想**：闭形式模去恰当形式得到上同调群，反映了流形上"局部为零但全局非零"的微分形式的存在性。

**关键观察**：
1. Poincaré 引理：局部上，闭形式都是恰当的（$\mathbb{R}^n$ 上 $H^k = 0$ 对 $k \geq 1$）
2. 全局上，闭形式不一定恰当，上同调群衡量了这种"缺陷"
3. 外微分 $d$ 满足 $d^2 = 0$，因此恰当形式 $\subset$ 闭形式，商空间定义良好
4. de Rham 上同调是微分同胚不变量，实际上是拓扑不变量

**证明策略**：
- 构造 de Rham 复形并验证 $d^2 = 0$
- 利用 Mayer-Vietoris 序列计算上同调
- 通过 Poincaré 引理证明 contractible 空间的上同调平凡

## 三、定理的严格表述

**定义（de Rham 复形）**：设 $M$ 是光滑流形。令 $\Omega^k(M)$ 为 $M$ 上光滑 $k$-形式的空间。外微分算子 $d: \Omega^k(M) \to \Omega^{k+1}(M)$ 满足：
1. $d$ 是 $\mathbb{R}$-线性的
2. $d(\omega \wedge \eta) = d\omega \wedge \eta + (-1)^k \omega \wedge d\eta$（$\omega$ 是 $k$-形式）
3. $d^2 = d \circ d = 0$

序列 $\cdots \xrightarrow{d} \Omega^{k-1}(M) \xrightarrow{d} \Omega^k(M) \xrightarrow{d} \Omega^{k+1}(M) \xrightarrow{d} \cdots$ 称为 **de Rham 复形**。

**定义（de Rham 上同调）**：
- $k$-次 **闭形式**空间：$Z^k(M) = \ker(d: \Omega^k(M) \to \Omega^{k+1}(M)) = \{\omega \in \Omega^k(M) : d\omega = 0\}$
- $k$-次 **恰当形式**空间：$B^k(M) = \text{im}(d: \Omega^{k-1}(M) \to \Omega^k(M)) = \{d\eta : \eta \in \Omega^{k-1}(M)\}$

由于 $d^2 = 0$，$B^k(M) \subset Z^k(M)$。第 $k$ 次 **de Rham 上同调群**定义为
$$H^k_{\text{dR}}(M) = Z^k(M) / B^k(M)$$

**基本定理**：

1. **同伦不变性**：若 $f, g: M \to N$ 光滑同伦，则 $f^* = g^*: H^k_{\text{dR}}(N) \to H^k_{\text{dR}}(M)$。特别地，若 $M$ 可缩（contractible），则 $H^k_{\text{dR}}(M) = 0$（$k \geq 1$），$H^0_{\text{dR}}(M) = \mathbb{R}$。

2. **Poincaré 引理**：$\mathbb{R}^n$ 上，$H^k_{\text{dR}}(\mathbb{R}^n) = 0$（$k \geq 1$）。

3. **Mayer-Vietoris 序列**：若 $M = U \cup V$（$U, V$ 开），则有长正合序列
$$\cdots \to H^k_{\text{dR}}(M) \to H^k_{\text{dR}}(U) \oplus H^k_{\text{dR}}(V) \to H^k_{\text{dR}}(U \cap V) \xrightarrow{\delta} H^{k+1}_{\text{dR}}(M) \to \cdots$$

4. **Poincaré 对偶**：若 $M$ 是 $n$ 维紧致定向流形，则 $H^k_{\text{dR}}(M) \cong (H^{n-k}_{\text{dR}}(M))^*$。

5. **de Rham 定理**：$H^k_{\text{dR}}(M) \cong H^k(M; \mathbb{R})$（奇异上同调），且环结构对应（杯积对应楔积）。

## 四、证明过程

**定理（Poincaré 引理）**：$H^k_{\text{dR}}(\mathbb{R}^n) = 0$（$k \geq 1$）。

**证明**：需要证明 $\mathbb{R}^n$ 上每个闭 $k$-形式是恰当的。

**步骤 1**：构造同伦算子。定义 $H: \Omega^k(\mathbb{R}^n) \to \Omega^{k-1}(\mathbb{R}^n)$ 如下。对 $k$-形式 $\omega = \sum_I a_I(x) dx^I$，
$$H\omega = \sum_I \left(\int_0^1 t^{k-1} a_I(tx) \, dt\right) \iota_R (dx^I)$$
其中 $R = \sum x^i \frac{\partial}{\partial x^i}$ 是径向向量场，$\iota_R$ 是内乘算子。

**步骤 2**：验证同伦公式。直接计算可得
$$dH\omega + Hd\omega = \omega - \omega(0)$$
其中 $\omega(0)$ 是 $\omega$ 在原点的值（视为常值形式）。

**步骤 3**：闭形式的恰当性。若 $d\omega = 0$ 且 $k \geq 1$，则 $\omega(0) = 0$（因为常值 $k$-形式在 $k \geq 1$ 时在原点为零）。因此 $\omega = dH\omega$，即 $\omega$ 是恰当的。$\square$

**定理（Mayer-Vietoris 序列）**：

**证明**：设 $M = U \cup V$，$\{ \rho_U, \rho_V \}$ 是从属于覆盖 $\{U, V\}$ 的单位分解。

**步骤 1**：定义映射。
- $r: \Omega^k(M) \to \Omega^k(U) \oplus \Omega^k(V)$，$r(\omega) = (\omega|_U, \omega|_V)$
- $s: \Omega^k(U) \oplus \Omega^k(V) \to \Omega^k(U \cap V)$，$s(\alpha, \beta) = \alpha|_{U \cap V} - \beta|_{U \cap V}$
- $\delta: \Omega^k(U \cap V) \to \Omega^{k+1}(M)$，$\delta(\omega) = d(\rho_V \omega)$ 在 $U$ 上，$-d(\rho_U \omega)$ 在 $V$ 上

**步骤 2**：验证正合性。在 $\Omega^k(U \cap V)$ 处正合：若 $\omega \in \Omega^k(U \cap V)$ 且 $s(\alpha, \beta) = \omega$，则 $\alpha - \beta = \omega$ 在 $U \cap V$ 上。定义 $\gamma = \rho_U \alpha + \rho_V \beta$（在 $M$ 上），则 $d\gamma$ 限制到 $U \cap V$ 等于 $d\omega$。

**步骤 3**：诱导上同调映射。由于 $r, s, \delta$ 与 $d$ 交换，诱导出上同调群的映射。长正合序列的正合性通过标准同调代数论证验证。$\square$

**定理（同伦不变性）**：若 $f \simeq g: M \to N$，则 $f^* = g^*$ 在 $H^k_{\text{dR}}$ 上。

**证明**：设 $F: M \times [0,1] \to N$ 是同伦，$F(x, 0) = f(x)$，$F(x, 1) = g(x)$。

定义同伦算子 $K: \Omega^k(M \times [0,1]) \to \Omega^{k-1}(M)$ 为 $K\omega = \int_0^1 \iota_{\partial/\partial t} \omega \, dt$。

则 $dK + Kd = i_1^* - i_0^*$，其中 $i_t: M \to M \times \{t\}$ 是包含映射。

因此 $F^* = i_1^* F^* - i_0^* F^* = (dK + Kd)F^*\omega = d(KF^*\omega) + K(dF^*\omega)$。

若 $d\omega = 0$，则 $g^*\omega - f^*\omega = d(KF^*\omega)$，即 $g^*[\omega] = f^*[\omega]$ 在 $H^k_{\text{dR}}(M)$ 中。$\square$

## 五、应用与意义

de Rham 上同调在现代数学中有广泛应用：

1. **代数拓扑**：通过 de Rham 定理，提供了计算奇异上同调的微分几何方法。

2. **Hodge 理论**：在紧致 Riemann 流形上，每个上同调类有唯一的调和形式代表元（Hodge 定理）。

3. **指标定理**：Atiyah-Singer 指标定理将椭圆算子的指标与上同调类联系起来。

4. **特征类**：Chern 类、Pontryagin 类和 Euler 类通过曲率形式表示为 de Rham 上同调类。

5. **辛几何**：辛流形的 symplectic 形式是闭 2-形式，其上同调类决定了流形的全局性质。

6. **数学物理**：在规范理论中，规范场的场强是曲率形式，Chern-Simons 形式与上同调密切相关。

7. **复几何**：Dolbeault 上同调是 de Rham 上同调的复类比，Hodge 分解将 de Rham 上同调分解为 Dolbeault 上同调的直和。

de Rham 上同调的推广包括：带系数的上同调、紧支集上同调、相对上同调、以及层上同调。
