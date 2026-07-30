# Kodaira 嵌入定理

## 一、定理介绍

Kodaira 嵌入定理是复几何与代数几何中最为深刻的结果之一，由日本数学家小平邦彦（Kunihiko Kodaira）于 1954 年证明。该定理给出了紧复流形可作为光滑射影代数簇嵌入射影空间的充分必要条件，从而在紧复流形的"复几何"刻画与"代数几何"刻画之间架起了桥梁。

定理断言：紧复流形 $X$ 是射影代数的（即可以全纯嵌入到某复射影空间 $\mathbb{CP}^N$ 中），当且仅当 $X$ 上存在正的全纯线丛（positive holomorphic line bundle）。这一结果使复几何中"正性"的微分几何概念（曲率为正）与代数几何中"丰富线丛"（ample line bundle）的概念完全等价，是 Hodge 理论、Kähler 几何与层上同调理论结合的典范成果。

## 二、原理思路

### 基本思想

嵌入定理的核心思路是利用线丛的整体截面构造全纯嵌入。

设 $L$ 为 $X$ 上的正全纯线丛。对于充分大的 $m$，考虑张量幂 $L^{\otimes m}$ 的整体截面空间 $H^0(X, L^{\otimes m})$。该空间的每个截面 $s$ 定义了 $X$ 到射影空间的"有理映射"：

$$\Phi_{|L^{\otimes m}|}: X \dashrightarrow \mathbb{P}(H^0(X, L^{\otimes m})^*)$$

目标是证明：当 $m$ 充分大时，该映射是良定义的全纯嵌入。

### 关键步骤

1. **截面分离点**：对任意 $p \neq q \in X$，存在 $s \in H^0(X, L^{\otimes m})$ 使 $s(p) = 0$ 但 $s(q) \neq 0$（或反之），即截面可分离点。

2. **截面分离切向量**：对任意 $p \in X$ 和任意切向量 $v \in T_pX$，存在过 $p$ 的截面 $s$（即 $s(p)=0$）使得 $ds_p(v) \neq 0$，从而嵌入是非退化的。

3. **正性的作用**：正线丛的曲率形式 $\Theta$ 是正的 $(1,1)$-形式，可用来控制 $\bar\partial$-问题的可解性，从而构造所需截面。

4. **Kodaira 消没定理**：$L$ 正蕴含 $H^q(X, L^{\otimes m} \otimes K) = 0$（$q > 0, m$ 充分大），使得截面空间的维数可由 Riemann-Roch 公式精确计算，截面数量充足。

## 三、定理的严格表述

**定义（正全纯线丛）** 设 $X$ 为紧 Kähler 流形，$L$ 为其上的全纯线丛，$h$ 为 $L$ 上的 Hermitian 度量。设局部坐标下 $h = e^{-\varphi}$，则称 $L$ 是**正的**（positive），若其曲率形式

$$\Theta(L, h) = \bar\partial \partial \varphi$$

是 $X$ 上的正 $(1,1)$-形式，即 $\sqrt{-1}\,\Theta(L, h) > 0$。等价地，$c_1(L)$ 可由正 $(1,1)$-形式代表。

**定理（Kodaira 嵌入定理）** 设 $X$ 为紧复流形。则下列条件等价：

1. 存在正全纯线丛 $L \to X$；
2. 存在全纯嵌入 $\iota: X \hookrightarrow \mathbb{CP}^N$（即 $X$ 是射影代数流形）；
3. $X$ 上存在丰富线丛（ample line bundle）。

更进一步，若 $L$ 正，则存在 $m_0 > 0$，使得对所有 $m \geq m_0$，张量幂 $L^{\otimes m}$ 诱导的全纯映射

$$\Phi_m: X \to \mathbb{P}(H^0(X, L^{\otimes m})^*)$$

是全纯嵌入。

## 四、证明过程

设 $L$ 为正全纯线丛，取定其 Hermitian 度量 $h$ 使曲率为正。设 $\omega = \sqrt{-1}\,\Theta(L,h)$ 为对应的 Kähler 形式。

### 步骤 1：构造局部截面

对任意点 $p \in X$，取局部全纯坐标 $z = (z_1, \dots, z_n)$（$n = \dim_\mathbb{C} X$）。选取局部全纯标架 $e$，使 $|e(p)|_h^2 = e^{-\varphi(p)}$。

**引理（局部消灭引理 / Kodaira 引理）** 存在常数 $C > 0$ 与 $m$ 充分大，使得对任意点 $p$ 与任意 $v \in T_pX$，存在整体截面 $s \in H^0(X, L^{\otimes m})$ 满足：
- $s(p) = 0$；
- $\bar\partial s$ 在 $p$ 附近的 $L^2$-范数可控；
- $ds_p(v) \neq 0$。

证明要点：使用 $\bar\partial$-技术的 $L^2$ 估计。设 $\eta$ 为支于 $p$ 附近的光滑截尾函数。令 $f = \bar\partial(\eta e^{\otimes m})$ 为 $L^{\otimes m}$-值的 $(0,1)$-形式，利用 Kodaira 消没定理的 $L^2$ 估计求解 $\bar\partial u = f$，得整体截面 $s = \eta e^{\otimes m} - u$。正性给出加权 $L^2$ 估计：

$$\int_X |u|^2 e^{-m\varphi} \omega^n \leq \frac{C}{m} \int_X |f|^2 e^{-m\varphi} \omega^n$$

当 $m \to \infty$，右端可任意小，从而保证 $s$ 在 $p$ 附近的行为可控。

### 步骤 2：分离点

设 $p \neq q \in X$。由局部消灭引理，存在 $m$ 充分大与截面 $s_p, s_q \in H^0(X, L^{\otimes m})$，使 $s_p$ 在 $p$ 附近非零而 $s_p(q) = 0$，$s_q$ 在 $q$ 附近非零而 $s_q(p) = 0$。于是 $H^0(X, L^{\otimes m})$ 中存在分离 $p, q$ 的截面。

### 步骤 3：分离切向量

对 $p \in X$ 与 $v \in T_pX$，由局部消灭引理，存在截面 $s \in H^0(X, L^{\otimes m})$ 使 $s(p) = 0$ 但 $ds_p(v) \neq 0$。因此 $\Phi_m$ 在 $p$ 处的微分为单射。

### 步骤 4：由消没定理保证整体截面充分多

由 Kodaira 消没定理：$H^q(X, L^{\otimes m} \otimes K_X) = 0$ 对 $q > 0$ 与 $m \geq 1$ 成立（其中 $K_X$ 为典则丛）。结合 Riemann-Roch-Hirzebruch 定理：

$$h^0(X, L^{\otimes m}) = \int_X \text{ch}(L^{\otimes m})\,\text{td}(T_X) = \frac{m^n}{n!}\int_X c_1(L)^n + O(m^{n-1})$$

当 $m \to \infty$ 时 $h^0 \to \infty$，截面空间维数充分大，保证上述构造可在大 $m$ 下完成。

### 步骤 5：综合

由步骤 2、3，当 $m$ 充分大时 $\Phi_m$ 是良定义的全纯映射，且为单射且浸入。由于 $X$ 紧，$\Phi_m$ 为闭嵌入，故为全纯嵌入。

### 反向：嵌入蕴含正性

若 $\iota: X \hookrightarrow \mathbb{CP}^N$ 为全纯嵌入，取 $L = \iota^*\mathcal{O}_{\mathbb{CP}^N}(1)$，配备 FS 度量（Fubini-Study）的拉回，则 $L$ 是正全纯线丛。其曲率为 $\iota^*\omega_{FS} > 0$。

## 五、应用与意义

### 1. 复几何与代数几何的统一

Kodaira 嵌入定理表明，紧复流形能否被代数化，等价于是否存在正线丛。这是 Kähler 几何与射影代数几何之间的核心桥梁。

### 2. Chow 定理的结合

结合 Chow 定理（$\mathbb{CP}^N$ 中的紧复子流形必为代数簇），Kodaira 嵌入定理给出了"紧复流形为代数流形"的内在判据，使代数几何方法可用于一般 Kähler 流形。

### 3. 丰富线丛的判别

在代数几何中，丰富线丛的判别（Nakai-Moishezon 判据、Seshadri 判据）与 Kodaira 嵌入定理紧密相关，是双有理几何与极小模型纲领的基础。

### 4. Calabi-Yau 流形与弦理论

许多 Calabi-Yau 流形通过 Kodaira 嵌入定理被证明是射影的，使其成为代数几何的研究对象。这是弦理论中紧化的几何基础。

### 5. Hodge 理论的基础

嵌入定理保证了射影 Kähler 流形具有 Hodge 结构，为 Hodge 理论、周期映射与 Torelli 型问题的研究提供了前提。

### 6. 高维复几何的分类

Kodaira 维数、典范丛的正性等概念，皆基于 Kodaira 嵌入定理建立的框架，是双有理几何分类理论的核心。
