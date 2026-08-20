# Hodge 分解定理

> **一句话大白话**：复流形上的"圈状微分形式"能按"复方向 (p,q) 层级"拆开，而且全域上同调正等于这些层级小房间的直和——非线性形式级数的"复数等级总账"，Hodge 数 $h^{p,q}$ 在此盖章，是复几何最上镜的刚性格言之一。
>
> **小例子**：对紧 Kähler 流形 $X$，有 $H^k(X,\mathbb{C})\simeq\bigoplus_{p+q=k}H^{p,q}$（Hodge 分解）且 $\overline{H^{p,q}}=H^{q,p}$；例：$H^1(C)$ 在亏格为 $g$ 的曲线上维数为 $2g=h^{1,0}+h^{0,1}$，各半送一空间。

## 一、定理介绍

Hodge 分解定理是 Kähler 几何中最优美的结果之一，由 William Hodge 在 1930-1941 年间提出并发展。该定理断言：在紧 Kähler 流形 $X$ 上，每个复系数 de Rham 上同调群 $H^k(X, \mathbb{C})$ 可以自然分解为 $(p, q)$-型 Dolbeault 上同调群的直和：

$$H^k(X, \mathbb{C}) = \bigoplus_{p + q = k} H^{p, q}(X)$$

其中 $H^{p,q}(X) \cong H^q(X, \Omega^p_X)$，且满足对称关系 $H^{p,q}(X) = \overline{H^{q,p}(X)}$。

这一定理将 Kähler 度量的"调和性"（实 Laplacian 与复 Laplacian 相差常数）转化为上同调的代数结构，是 Hodge 理论的核心。它使上同调具有自然的 Hodge 结构，是代数几何、复几何与代数拓扑之间相互作用的基础，也是镜面对称等弦理论问题的几何前提。

## 二、原理思路

### 基本思想

设 $(X, \omega)$ 为紧 Kähler 流形。复化的 de Rham 复形可分解为 $(p, q)$-型形式：

$$\mathcal{A}^k(X, \mathbb{C}) = \bigoplus_{p+q=k} \mathcal{A}^{p,q}(X)$$

外微分 $d = \partial + \bar\partial$（$\partial: \mathcal{A}^{p,q} \to \mathcal{A}^{p+1,q}$，$\bar\partial: \mathcal{A}^{p,q} \to \mathcal{A}^{p,q+1}$）。当度量 Kähler 时，三种 Laplacian 相等：

$$\Delta_d = 2\Delta_\partial = 2\Delta_{\bar\partial}$$

（**Kähler 恒等式**）

这蕴含：$\bar\partial$-闭形式成为 $\Delta_d$ 的调和形式时，自动具有 $(p, q)$-型。由此，调和 $k$-形式空间 $\mathcal{H}^k(X, \mathbb{C})$ 分解为 $\bigoplus \mathcal{H}^{p,q}$，再由 Hodge 定理建立与 Dolbeault 上同调的同构。

### 关键观察

1. **(p,q)-型在调和性下封闭**：由 $\Delta_d$ 与 $\Pi^{p,q}$（投影到 $(p,q)$-型）的交换性，调和 $k$-形式可分解为 $(p,q)$-型调和形式之和。

2. **复共轭对称**：复共轭 $u \mapsto \bar u$ 将 $\mathcal{H}^{p,q}$ 同构地映到 $\mathcal{H}^{q,p}$，给出 $H^{p,q} = \overline{H^{q,p}}$。

3. **Lefschetz 算子的交换性**：$L = \omega \wedge \bullet$ 与 $\Delta_d$ 交换，给出更精细的 Lefschetz 分解。

## 三、定理的严格表述

**定理（Hodge 分解）** 设 $(X, \omega)$ 为 $n$ 维紧 Kähler 流形。则对所有 $k \geq 0$，有：

1. **直和分解**：
$$H^k_{\text{dR}}(X, \mathbb{C}) = \bigoplus_{p+q=k} H^{p,q}(X)$$
其中 $H^{p,q}(X) \cong H^q(X, \Omega^p_X)$。

2. **调和代表元**：每个 $[\alpha] \in H^{p,q}(X)$ 有唯一的 $\Delta_d$-调和代表元 $\alpha \in \mathcal{A}^{p,q}(X)$。

3. **共轭对称**：$H^{p,q}(X) = \overline{H^{q,p}(X)}$，即若 $[\alpha] \in H^{p,q}$ 则 $[\bar\alpha] \in H^{q,p}$。

4. **维数关系**：$h^{p,q} = h^{q,p} = h^{n-p,n-q}$；$b_k = \sum_{p+q=k} h^{p,q}$（其中 $b_k$ 是第 $k$ 个 Betti 数，$h^{p,q} = \dim H^{p,q}$）。

**进一步性质**：

- **奇数 Betti 数偶性**：由 $b_{2k+1} = 2\sum_{p<q, p+q=2k+1} h^{p,q}$ 为偶数。
- **$h^{1,0}$ 与基本群**：$h^{1,0} = h^{0,1} = b_1 / 2$。

**Hodge 结构**：上述分解赋予 $H^k(X, \mathbb{Z})$ 自然地具有权为 $k$ 的纯 Hodge 结构，是 Hodge 理论的基本对象。

## 四、证明过程

### 步骤 1：Kähler 恒等式

**引理（Kähler 恒等式）** 在紧 Kähler 流形上：

$$\Delta_d = 2\Delta_\partial = 2\Delta_{\bar\partial}$$

即三个 Laplacian 重合（至多相差常数）。

证明：核心恒等式 $[\Lambda, \partial] = \sqrt{-1}\,\bar\partial^*$（其中 $\Lambda = L^*$ 为 Lefschetz 算子的伴随），需要 Kähler 条件 $d\omega = 0$。由该恒等式：

$$\Delta_{\bar\partial} = \bar\partial\bar\partial^* + \bar\partial^*\bar\partial = -\sqrt{-1}(\bar\partial[\Lambda, \partial] + [\Lambda, \partial]\bar\partial) = \sqrt{-1}[\Lambda, \bar\partial\partial + \partial\bar\partial] = \sqrt{-1}[\Lambda, d\partial]$$

类似地 $\Delta_\partial = \sqrt{-1}[\Lambda, \bar\partial\partial]$。再用 $\Delta_d = \partial\partial^* + \cdots + \bar\partial\bar\partial^* + \cdots$ 与 $[\Lambda, \partial] = \sqrt{-1}\,\bar\partial^*$, $[\Lambda, \bar\partial] = -\sqrt{-1}\,\partial^*$ 整理得 $\Delta_d = 2\Delta_\partial = 2\Delta_{\bar\partial}$。

### 步骤 2：(p,q)-型在调和性下封闭

由步骤 1，$\Delta_d$ 是 $\bar\partial$-Laplacian 的常数倍，$\Delta_d u = 0 \iff \Delta_{\bar\partial} u = 0$。又 $\Delta_{\bar\partial}$ 与投影 $\Pi^{p,q}$ 可交换（因 $\bar\partial$、$\bar\partial^*$ 保持 $(p,q)$-型），故：

$$\mathcal{H}^k(X, \mathbb{C}) = \ker\Delta_d = \bigoplus_{p+q=k} \ker \Delta_{\bar\partial}|_{\mathcal{A}^{p,q}} = \bigoplus_{p+q=k} \mathcal{H}^{p,q}(X)$$

### 步骤 3：与 de Rham 上同调的同构

由 Hodge 定理（实形式）：每个 $[\alpha] \in H^k_{\text{dR}}(X, \mathbb{C})$ 有唯一 $\Delta_d$-调和代表元 $h$。由步骤 2：

$$h = \sum_{p+q=k} h^{p,q}, \quad h^{p,q} \in \mathcal{H}^{p,q}(X)$$

定义 $H^{p,q}(X) := \{[h^{p,q}] : h^{p,q} \in \mathcal{H}^{p,q}(X)\}$，则有同构：

$$H^k_{\text{dR}}(X, \mathbb{C}) \cong \mathcal{H}^k(X, \mathbb{C}) = \bigoplus_{p+q=k} \mathcal{H}^{p,q}(X) \cong \bigoplus_{p+q=k} H^{p,q}(X)$$

### 步骤 4：$H^{p,q}(X) \cong H^q(X, \Omega^p_X)$

由 Dolbeault 定理（$\bar\partial$-Poincaré 引理 + 层上同调）：$H^q_{\bar\partial}(X, \Omega^p_X) \cong H^q(X, \Omega^p_X)$。而由 Hodge 定理（复形式）：

$$H^q_{\bar\partial}(X, \Omega^p_X) \cong \mathcal{H}^{p,q}(X)$$

故 $H^{p,q}(X) \cong H^q(X, \Omega^p_X)$。

### 步骤 5：共轭对称

复共轭 $u \mapsto \bar u$ 将 $(p,q)$-形式变为 $(q,p)$-形式。由 $\Delta_d$ 在实度量下是实算子（保持实形式），$\bar{\mathcal{H}^{p,q}} = \mathcal{H}^{q,p}$。

故 $H^{p,q} = \overline{H^{q,p}}$，给出 $h^{p,q} = h^{q,p}$。

### 步骤 6：Serre 对偶给出 $h^{p,q} = h^{n-p,n-q}$

由 Serre 对偶定理：

$$H^q(X, \Omega^p_X) \cong H^{n-q}(X, (\Omega^p_X)^* \otimes K_X)^* = H^{n-q}(X, \Omega^{n-p}_X)^*$$

（用 $(\Omega^p_X)^* \cong \Omega^{n-p}_X \otimes K_X^{-1}$ 与 $K_X = \Omega^n_X$，得 $(\Omega^p_X)^* \otimes K_X \cong \Omega^{n-p}_X$）。故 $h^{p,q} = h^{n-p,n-q}$。

### 步骤 7：奇数 Betti 数为偶数

$$b_{2m+1} = \sum_{p+q=2m+1} h^{p,q} = \sum_{p<q, p+q=2m+1} (h^{p,q} + h^{q,p}) = 2 \sum_{p<q, p+q=2m+1} h^{p,q}$$

为偶数。

## 五、应用与意义

### 1. Hodge 结构与周期映射

Hodge 分解赋予 $H^k(X, \mathbb{Z})$ 自然权为 $k$ 的纯 Hodge 结构，是 Hodge 结构理论的基础。周期映射将 Kähler 类的变化编码为周期域（Hodge 域 $D = G_\mathbb{R}/K$）中的变化，是 Griffiths 变分理论的核心。

### 2. Torelli 型问题

由 Hodge 分解可将"流形结构是否相同"的问题转化为"上同调的 Hodge 结构是否相同"，是经典 Torelli 定理（曲线情形）、Torelli 定理（$K3$ 曲面与 Abel 簇）等的基础。

### 3. 奇数 Betti 数偶性的拓扑应用

Hodge 分解蕴含紧 Kähler 流形的 $b_{2m+1}$ 为偶数。这给出 Kähler 流形（乃至同伦 Kähler 流形）的拓扑约束，例如 $S^3 \times S^3$ 不可能是 Kähler 的（因 $b_3 = 2$）。

### 4. Hodge 对称与镜面对称

镜面对称猜想断言：镜面 Calabi-Yau 对 $(X, Y)$ 满足 $h^{p,q}(X) = h^{n-p,q}(Y)$（特别是 $h^{1,1}(X) = h^{2,1}(Y)$ 与反之）。这基于 Hodge 分解的对称结构，是弦理论中重要的几何对应。

### 5. 非紧 Kähler 流形与 Hodge-结构退化

在族 $\pi: \mathcal{X} \to B$ 的 Kähler 流形上，Hodge 分解随 $b \in B$ 连续（甚至变化规则），是变分 Hodge 结构理论的基础，与 Schmid 的 $SL_2$ 表示论相联系。

### 6. Betti 数与 Euler 数的关系

Hodge 分解将 Euler 示性数表示为 $\chi(X) = \sum_{p,q} (-1)^{p+q} h^{p,q}$，与 Riemann-Roch 定理 $\chi(X, \mathcal{O}_X) = \sum_q (-1)^q h^{0,q} = \frac{1}{12}c_1 c_n + \cdots$（Noether 公式等）结合，给出几何与拓扑的深刻关联。

### 7. $h^{p,0}$ 的几何意义

- $h^{0,0} = 1$（连通紧流形）
- $h^{1,0}$：全纯 1-形式空间维数，刻画 Albanese 簇的维数
- $h^{n,0}$：全纯 $n$-形式空间维数，对 Calabi-Yau 流形为 1
- $h^{p,0}$ 给出双有理不变量

### 8. 与代数几何的桥梁

Kodaira 嵌入定理保证射影代数流形为 Kähler，从而具有 Hodge 分解；这使代数几何中 Lefschetz 定理、Hodge 理论可用，是复几何通向代数几何的关键工具。

### 9. Hodge 猜想

Hodge 分解使每个上同调类有 $(p,q)$-分量。**Hodge 猜想**断言：$H^{p,p}(X, \mathbb{Q})$ 中的类皆由代数闭链的 Chern 类生成（$p$ 偶情形）。这是 Clay 数学研究所千禧年问题之一，依赖 Hodge 分解的精致结构。
