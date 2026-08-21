# Hodge分解定理

> **一句话大白话**：流形上的任何"微分形式"都能唯一地拆成三块："无痕迹分"（调和、既是闭又是余闭）+ "闭合可微"部分 + "微调"部分——像把任意向量分解成三个互相垂直的分量，全空间由这三类正交拼接。
>
> **小例子**：在紧流形 $M$ 上，任意 $p$-形式 $\omega$ 可唯一写为 $\omega = h + d\alpha + \delta\beta$（$h$ 调和、$d$ 外微分、$\delta$ 余微分）；$L^2$ 正交直和结构像把函数空间劈成调和核加两块余空间。

## 介绍

Hodge分解定理（Hodge Decomposition Theorem）是 Hodge 理论的核心结果，由 William Hodge 在1930年代建立。该定理断言：在紧致定向 Riemann 流形 $M$ 上，微分形式的 de Rham 复形可以正交分解为调和形式、恰当形式和余恰当形式的直和。具体地，对任意 $k$-形式 $\omega$，存在唯一的分解

$$
\omega = \alpha + d\beta + d^*\gamma,
$$

其中 $\alpha$ 是调和形式（$\Delta \alpha = 0$），$d\beta$ 是恰当形式，$d^*\gamma$ 是余恰当形式。Hodge分解定理建立了 de Rham 上同调与调和形式之间的同构，深刻揭示了流形的分析性质与拓扑性质之间的联系。

## 分析

**前置依赖**：微分形式与外微分、Hodge 星算子与余微分、Hodge Laplacian 的椭圆性、椭圆算子的 Fredholm 理论与正则性、de Rham 上同调。

**定理的精确表述**：设 $(M, g)$ 是紧致定向 Riemann 流形（无边），$\Omega^k(M)$ 是 $k$-形式空间，具有 $L^2$ 内积 $\langle \omega, \eta \rangle = \int_M \omega \wedge *\eta$。Hodge Laplacian 定义为 $\Delta = d d^* + d^* d$。则

$$
\Omega^k(M) = \mathcal{H}^k(M) \oplus d\Omega^{k-1}(M) \oplus d^*\Omega^{k+1}(M),
$$

其中 $\mathcal{H}^k(M) = \{\omega \in \Omega^k(M) : \Delta \omega = 0\}$ 是调和 $k$-形式空间。分解是 $L^2$-正交的。

**等价结果**：$\mathcal{H}^k(M) \cong H^k_{\mathrm{dR}}(M)$，即调和形式空间与 de Rham 上同调群同构。

**依赖的概念**：Hodge 星算子、余微分 $d^*$、Hodge Laplacian、椭圆算子正则性、Sobolev 空间。

**证明策略**：利用椭圆算子的正则性理论，证明 $\Delta$ 是椭圆算子，其核是有限维的，且 $\Delta$ 的像在 $\Omega^k(M)$ 中是闭的，从而得到正交分解。

## 思考过程

Hodge 分解定理的证明依赖于椭圆算子理论。Hodge Laplacian $\Delta$ 是椭圆算子，在紧流形上具有有限维核和闭像。由椭圆正则性，$\Delta \omega = 0$ 的解是光滑的。

分解的正交性来源于 $d$ 和 $d^*$ 的伴随关系：$\mathrm{Im}(d) \perp \mathrm{Im}(d^*)$，因为 $\langle d\beta, d^*\gamma \rangle = \langle d^2\beta, \gamma \rangle = 0$。

Hodge 定理的深远意义在于：它揭示了上同调类的"调和代表元"的存在性和唯一性，这使得我们可以用分析的方法研究拓扑问题。

## 证明过程

**定理**（Hodge 分解定理）：设 $(M, g)$ 是紧致定向 Riemann 流形，则

$$
\Omega^k(M) = \mathcal{H}^k(M) \oplus d\Omega^{k-1}(M) \oplus d^*\Omega^{k+1}(M),
$$

其中 $\mathcal{H}^k(M) = \ker \Delta$。

**证明**：

**步骤 1：$\Delta$ 是椭圆算子。**

在局部坐标下，$\Delta$ 的主符号为 $\sigma(\Delta)(x, \xi) = |\xi|^2 \cdot \mathrm{id}$，非退化，故 $\Delta$ 是椭圆算子。

**步骤 2：$\ker \Delta$ 是有限维的。**

由椭圆算子的正则性，$\ker \Delta$ 中的元素都是光滑的。由紧流形上椭圆算子的 Fredholm 性质，$\ker \Delta$ 是有限维的。

**步骤 3：$\Delta$ 的像在 $\Omega^k(M)$ 中是闭的。**

由椭圆算子理论，$L^2$ 空间中的椭圆算子有闭像。因此 $\Delta(\Omega^k(M)) \subset L^2\Omega^k(M)$ 是闭的。

**步骤 4：正交分解。**

由泛函分析，$\Omega^k(M) = \ker \Delta \oplus \overline{\mathrm{Im}(\Delta)} = \ker \Delta \oplus \mathrm{Im}(\Delta)$（因为像闭）。而 $\mathrm{Im}(\Delta) = \mathrm{Im}(d d^*) + \mathrm{Im}(d^* d) = d\Omega^{k-1} \oplus d^*\Omega^{k+1}$，因为 $d\Omega^{k-1} \perp d^*\Omega^{k+1}$。

**步骤 5：验证正交性。**

对任意 $\omega \in \mathcal{H}^k(M)$，$\langle \omega, d\beta \rangle = \langle d^*\omega, \beta \rangle = 0$ 因为 $d^*\omega = 0$（由 $\Delta\omega = 0$ 可得 $d\omega = d^*\omega = 0$）。类似地 $\langle \omega, d^*\gamma \rangle = 0$。且 $\langle d\beta, d^*\gamma \rangle = \langle d^2\beta, \gamma \rangle = 0$。$\square$

**推论**（Hodge 同构）：紧定向 Riemann 流形上，每个 de Rham 上同调类有唯一的调和代表元，即

$$
H^k_{\mathrm{dR}}(M) \cong \mathcal{H}^k(M).
$$

**证明**：设 $[\omega] \in H^k_{\mathrm{dR}}(M)$，由 Hodge 分解，$\omega = \alpha + d\beta + d^*\gamma$。由于 $d\omega = 0$ 且 $d\alpha = 0$，得 $d d^*\gamma = 0$，故 $\langle d^*\gamma, d^*\gamma \rangle = \langle d d^*\gamma, \gamma \rangle = 0$，即 $d^*\gamma = 0$。因此 $\omega = \alpha + d\beta$，$[\omega] = [\alpha]$。由分解的唯一性，$\alpha$ 是唯一的调和代表元。$\square$
## 相关条目

- [Hodge 分解定理（第58级-复几何）](../第58级-复几何/Hodge分解定理.md)：相关条目——本条目为 Riemann 流形上微分形式的 Hodge 分解；第58级条目为紧 Kähler 流形上按 (p,q)-型的细化分解。
