# Atiyah-Singer指标定理

> **一句话大白话**：一个椭圆算子的"指标"（解空间的维数减去伴随核维数）看似纯分析，却可以用流形的拓扑量（Char数 × Todd类积分）来算——两个隔行如隔山的世界被一座桥接通。
>
> **小例子**：对 $\partial/\partial\bar z$（Dolbeault 算子）指标定理化为 Riemann–Roch：$\dim H^0-\dim H^1=\int_M \mathrm{ch}(\mathcal E)\,\mathrm{td}(TM)$；Gauss–Bonnet、极限情形等经典结论都是它的特例。

## 介绍

Atiyah-Singer指标定理（Atiyah–Singer Index Theorem）是20世纪数学中最深刻的定理之一，由 Michael Atiyah 和 Isadore Singer 在1963年证明。该定理断言：紧流形上椭圆算子的解析指标（核的维数减去余核的维数）等于拓扑指标（由流形和算子符号类决定的示性数）。具体地，对紧流形 $M$ 上的椭圆伪微分算子 $D$，有

$$
\mathrm{ind}(D) = \dim \ker D - \dim \mathrm{coker} D = \int_M \mathrm{ch}(\sigma(D)) \cdot \hat{A}(TM),
$$

其中 $\mathrm{ch}$ 是陈特征，$\hat{A}$ 是 $\hat{A}$-类。指标定理统一了分析（椭圆算子的指标）与拓扑（示性类），在微分几何、拓扑、理论物理中有着深远影响。重要特例包括 Gauss-Bonnet 定理、Hirzebruch 符号差定理和 Riemann-Roch 定理。

## 分析

**前置依赖**：椭圆算子与 Fredholm 指标、伪微分算子的符号、示性类（Chern 特征、Todd 类、$\hat{A}$-类）、热核渐近展开、K-理论。

**定理的精确表述**：设 $M$ 是紧致定向光滑流形，$E, F$ 是 $M$ 上的向量丛，$D: \Gamma(E) \to \Gamma(F)$ 是椭圆伪微分算子。则 $D$ 是 Fredholm 算子，且

$$
\mathrm{ind}(D) = \dim \ker D - \dim \mathrm{coker} D = \int_{T^*M} \mathrm{ch}(\sigma(D)) \cdot \pi^* \mathrm{Td}(TM \otimes \mathbb{C}),
$$

其中 $\sigma(D)$ 是 $D$ 的符号，$\mathrm{ch}$ 是陈特征，$\mathrm{Td}$ 是 Todd 类，$T^*M$ 是余切丛。

**等价形式**（de Rham 复形版本）：

$$
\chi(M) = \sum_{i=0}^n (-1)^i \dim H^i_{\mathrm{dR}}(M) = \int_M e(TM),
$$

其中 $\chi(M)$ 是 Euler 示性数，$e(TM)$ 是 Euler 类。

**依赖的概念**：椭圆算子、Fredholm 算子、示性类、K-理论、伪微分算子。

**证明策略**：使用 K-理论和嵌入方法，将一般流形上的指标问题约化为球面上的标准算子。

## 思考过程

Atiyah-Singer 指标定理的证明思路是使用"分裂原理"和"嵌入方法"：

1. 将 $M$ 嵌入到 Euclidean 空间 $\mathbb{R}^N$ 中。
2. 构造一个"指标"的 K-理论值，证明它只依赖于算子的符号类。
3. 利用热核方法或狄拉克算子方法计算指标。

热核方法的证明思路尤其优美：考虑热方程 $\partial_t u + D^*D u = 0$ 和 $\partial_t v + DD^* v = 0$，其热核的迹给出

$$
\mathrm{ind}(D) = \mathrm{Tr}(e^{-t D^*D}) - \mathrm{Tr}(e^{-t DD^*}) = \int_M (K_t(x,x) - K'_t(x,x)) \, d\mathrm{vol}.
$$

当 $t \to 0$ 时，热核的渐近展开给出局部示性类，积分后即得拓扑指标。

## 证明过程

**定理**（Atiyah-Singer 指标定理）：对紧流形 $M$ 上的椭圆算子 $D: \Gamma(E) \to \Gamma(F)$，有

$$
\mathrm{ind}(D) = \int_M \mathrm{ch}(\sigma(D)) \cdot \hat{A}(TM),
$$

其中 $\mathrm{ind}(D) = \dim \ker D - \dim \mathrm{coker} D$。

**证明概要**（热核方法）：

**步骤 1：指标的热核表示。**

考虑 Laplace 型算子 $\Delta_+ = D^*D$ 和 $\Delta_- = DD^*$。设 $K_t^+(x,y)$ 和 $K_t^-(x,y)$ 分别是热方程 $\partial_t u + \Delta_+ u = 0$ 和 $\partial_t v + \Delta_- v = 0$ 的热核。则

$$
\mathrm{ind}(D) = \mathrm{Tr}(e^{-t\Delta_+}) - \mathrm{Tr}(e^{-t\Delta_-}) = \int_M \left( \mathrm{tr} K_t^+(x,x) - \mathrm{tr} K_t^-(x,x) \right) d\mathrm{vol}.
$$

**步骤 2：热核的渐近展开。**

当 $t \to 0^+$ 时，热核有渐近展开

$$
K_t(x,x) \sim (4\pi t)^{-n/2} \sum_{k=0}^\infty a_k(x) t^k,
$$

其中 $a_k(x)$ 是由算子符号的曲率决定的局部不变量。

**步骤 3：局部指标定理。**

对 Dirac 型算子，可以证明

$$
\lim_{t \to 0} \left( \mathrm{tr} K_t^+(x,x) - \mathrm{tr} K_t^-(x,x) \right) = \mathrm{ch}(\sigma(D)) \cdot \hat{A}(TM) \big|_{\text{top form}}.
$$

**步骤 4：$t$ 无关性。**

由于 $\mathrm{ind}(D)$ 与 $t$ 无关，取极限 $t \to 0$ 即得

$$
\mathrm{ind}(D) = \int_M \mathrm{ch}(\sigma(D)) \cdot \hat{A}(TM).
$$

$\square$

**推论**（重要特例）：
- **Gauss-Bonnet 定理**：$\chi(M) = \frac{1}{(2\pi)^n} \int_M \mathrm{Pf}(\Omega)$，其中 $\mathrm{Pf}$ 是 Pfaffian，$\Omega$ 是曲率形式。
- **Hirzebruch 符号差定理**：$\tau(M) = \frac{1}{3} \int_M p_1(M)$，其中 $p_1$ 是第一 Pontryagin 类。
- **Riemann-Roch 定理**：对 Riemann 面上的全纯线丛 $L$，$\mathrm{ind}(\bar{\partial}_L) = \deg L + 1 - g$。