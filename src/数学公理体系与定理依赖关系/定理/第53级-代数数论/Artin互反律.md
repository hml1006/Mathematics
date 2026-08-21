# 类域论（Artin 互反律）

> **一句话大白话**：阿贝尔扩张的伽罗瓦群和理想类群其实是"同一个人"的两种长相——把素数的分裂行为翻译成有限交换群的对账，是类域论贯通数论的中枢桥梁。
>
> **小例子**：对 $\mathbb{Q}$ 的阿贝尔扩张 $K$，每个未分歧素数 $p$ 对应一个 Frobenius 元素，其 Artin 符号完全决定 $p$ 在 $K$ 中如何分裂；互反律给出 Gal$(K/\mathbb{Q})$ 与理想类群间的同构。

## 一、定理介绍

> **前置依赖**：Galois 扩张与 Frobenius 自同构、理想类群与射线类群、二次互反律与幂剩余互反律、Hecke L-函数及其解析性质、Chebotarev 密度定理

Artin 互反律（Artin Reciprocity Law）是类域论（Class Field Theory）的核心定理，由 Emil Artin 于 1927 年证明。它被广泛认为是 19 世纪数论最伟大的成就之一，也是代数数论中最深刻的结果之一。

类域论的目标是描述数域 $K$ 的所有 **Abel 扩张**（即 Galois 群为 Abel 群的 Galois 扩张）的结构。Artin 互反律给出了一个惊人的答案：$K$ 的每个 Abel 扩张都对应于 $K$ 的某个**广义理想类群**（射线类群）的商，且 Galois 群与射线类群之间的同构由**Artin 映射**给出。

Artin 互反律统一并推广了此前所有的互反律：
- **二次互反律**（Gauss, Legendre）：关于二次剩余的基本定律。
- **幂剩余互反律**（Eisenstein, Kummer）：关于高次幂剩余的推广。
- **Artin 互反律**：最一般的形式，涵盖所有 Abel 扩张。

这一定理的证明经历了 Takagi 的存在性定理、Artin 的 L-函数方法等多个阶段，最终由 Artin 利用 Hecke L-函数的解析性质给出了纯代数证明。

## 二、原理思路

### 从二次互反律到一般互反律

二次互反律可以表述为：对不同的奇素数 $p, q$，
$$\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2} \cdot \frac{q-1}{2}}.$$

在类域论的语言中，二次互反律描述的是 $\mathbb{Q}$ 的二次扩张 $\mathbb{Q}(\sqrt{d})/\mathbb{Q}$ 的分裂行为。素数 $p$ 在 $\mathbb{Q}(\sqrt{d})$ 中的分解由 Legendre 符号 $\left(\frac{d}{p}\right)$ 决定，而二次互反律保证了这些局部信息的整体相容性。

Artin 的洞察是：对一般的 Abel 扩张 $L/K$，存在一个从 $K$ 的理想群到 $\text{Gal}(L/K)$ 的**Artin 映射**，它将素理想 $\mathfrak{p}$ 映为 **Frobenius 自同构** $\left(\frac{L/K}{\mathfrak{p}}\right)$。Artin 互反律断言这个映射是满射，且其核恰好是某个射线类群中的主理想——即 Artin 映射诱导了射线类群到 Galois 群的同构。

### Frobenius 自同构

设 $L/K$ 是数域的 Galois 扩张，$\mathfrak{P}$ 是 $\mathcal{O}_L$ 中在 $\mathfrak{p} \subset \mathcal{O}_K$ 上的非分歧素理想。**Frobenius 自同构** $\left(\frac{L/K}{\mathfrak{P}}\right) \in \text{Gal}(L/K)$ 是唯一满足
$$\left(\frac{L/K}{\mathfrak{P}}\right)(x) \equiv x^{N(\mathfrak{p})} \pmod{\mathfrak{P}}$$
对所有 $x \in \mathcal{O}_L$ 成立的自同构。

当 $L/K$ 是 Abel 扩张时，Frobenius 自同构只依赖于 $\mathfrak{p}$（不依赖于 $\mathfrak{P}$ 的选取），记为 $\left(\frac{L/K}{\mathfrak{p}}\right)$。

### Artin 映射

定义 **Artin 映射**：
$$\Phi_{L/K}: I_K(\mathfrak{m}) \to \text{Gal}(L/K), \quad \mathfrak{p} \mapsto \left(\frac{L/K}{\mathfrak{p}}\right),$$
其中 $I_K(\mathfrak{m})$ 是与模 $\mathfrak{m}$ 互素的分式理想群。

Artin 互反律断言：存在模 $\mathfrak{m}$（称为**导子**的倍数），使得 $\Phi_{L/K}$ 诱导出射线类群到 Galois 群的同构：
$$\text{Cl}_\mathfrak{m}(K) / H \xrightarrow{\sim} \text{Gal}(L/K),$$
其中 $H$ 是某个包含主射线理想群 $P_\mathfrak{m}$ 的子群。

## 三、定理的严格表述

**定理（Artin 互反律）：**

设 $K$ 是数域，$L/K$ 是有限 Abel 扩张，$G = \text{Gal}(L/K)$。

**(1) Artin 映射的存在性：** 存在 $\mathcal{O}_K$ 的一个非零理想 $\mathfrak{m}$（称为**模**），使得 Artin 映射
$$\Phi_{L/K}: I_K(\mathfrak{m}) \to G, \quad \mathfrak{p} \mapsto \left(\frac{L/K}{\mathfrak{p}}\right)$$
（对与 $\mathfrak{m}$ 互素的素理想 $\mathfrak{p}$ 取 Frobenius 自同构，并乘性延拓到整个理想群）是满射群同态。

**(2) 互反律：** 设 $\mathfrak{f} = \mathfrak{f}(L/K)$ 是 $L/K$ 的**导子**（conductor），即满足上述性质的最小模。则 $\Phi_{L/K}$ 诱导出**射线类群**到 $G$ 的同构：
$$\text{Cl}_\mathfrak{f}(K) / \Phi_{L/K}^{-1}(1) \xrightarrow{\sim} G.$$

等价地，$\ker(\Phi_{L/K})$ 包含主射线理想群 $P_{K,\mathfrak{f}}^+$，且
$$I_K(\mathfrak{f}) / (P_{K,\mathfrak{f}}^+ \cdot \ker(\Phi_{L/K})) \cong G.$$

**(3) 存在性定理（Takagi）：** 反之，对 $K$ 的每个模 $\mathfrak{m}$ 和射线类群 $\text{Cl}_\mathfrak{m}(K)$ 的每个子群 $H \supseteq P_{K,\mathfrak{m}}^+$，存在唯一的 Abel 扩张 $L/K$ 使得 $L$ 在 $\mathfrak{m}$ 的有限素因子处非分歧，且 $\Phi_{L/K}$ 的核为 $H$。

**推论（存在性对应）：** Artin 映射建立了以下一一对应：
$$\left\{\begin{array}{c} K \text{ 的有限 Abel 扩张} \\ L/K \text{（在同构意义下）} \end{array}\right\} \longleftrightarrow \left\{\begin{array}{c} K \text{ 的射线类群} \\ \text{的有限指数开子群} \end{array}\right\}.$$

## 四、证明过程

Artin 互反律的证明有多种方法。以下概述 Artin 的原始证明思路。

### 第一步：约化到循环扩张

由于每个有限 Abel 群都是循环群的直积，可以将 Artin 互反律约化到 $G = \text{Gal}(L/K)$ 为循环群的情形。

### 第二步：循环扩张的构造

设 $G = \langle \sigma \rangle$ 是 $n$ 阶循环群。需要构造 Artin 映射并证明互反律。

**关键工具：Artin L-函数。** 对 $G$ 的每个特征 $\chi: G \to \mathbb{C}^\times$，定义 **Artin L-函数**：
$$L(s, \chi, L/K) = \prod_{\mathfrak{p}} \frac{1}{1 - \chi\left(\frac{L/K}{\mathfrak{p}}\right) N(\mathfrak{p})^{-s}},$$
其中积取遍 $K$ 中在 $L$ 中非分歧的素理想。

### 第三步：L-函数的解析性质

需要证明：对非平凡特征 $\chi \neq 1$，$L(s, \chi, L/K)$ 在 $s = 1$ 处解析且非零。

**Artin 的方法：** 将 $L(s, \chi, L/K)$ 与 Hecke L-函数联系起来。利用诱导表示和 Brauer 定理，可以将 Artin L-函数表示为 Hecke L-函数的乘积（的有理次幂）。由于 Hecke L-函数在 $s=1$ 处的解析性质已知（非零），从而得到 Artin L-函数的相应性质。

### 第四步：Chebotarev 密度定理的应用

由 Chebotarev 密度定理，Frobenius 自同构在 $G$ 中的分布是均匀的。具体地，对 $G$ 的每个共轭类 $C$，满足 $\left(\frac{L/K}{\mathfrak{p}}\right) \in C$ 的素理想 $\mathfrak{p}$ 的（Dirichlet）密度为 $|C|/|G|$。

对 Abel 扩张，每个共轭类只有一个元素，所以每个 $\sigma \in G$ 都是某个素理想的 Frobenius 自同构。这说明 Artin 映射是**满射**。

### 第五步：互反律的证明

设 $H = \ker(\Phi_{L/K})$。需要证明 $H \supseteq P_{K,\mathfrak{f}}^+$（对某个模 $\mathfrak{f}$）。

考虑 L-函数的乘积：
$$\zeta_L(s) = \prod_\chi L(s, \chi, L/K)^{\chi(1)},$$
其中积取遍 $G$ 的所有不可约特征。对 Abel 群，$\chi(1) = 1$。

在 $s \to 1$ 时，$\zeta_L(s)$ 有单极点（因为 $L$ 也是数域）。$\zeta_K(s)$ 也有单极点。因此
$$\frac{\zeta_L(s)}{\zeta_K(s)} = \prod_{\chi \neq 1} L(s, \chi, L/K)$$
在 $s = 1$ 处解析且非零。

由此推出每个 $L(1, \chi, L/K) \neq 0$（$s=1$ 处的阶的精确分析）。

利用 $L(1, \chi)$ 的非零性和对数密度的计算，可以证明：主射线理想群 $P_{K,\mathfrak{f}}^+$ 包含在 $H$ 中。

因此 Artin 映射诱导出 $\text{Cl}_\mathfrak{f}(K) / (H/P_{K,\mathfrak{f}}^+) \cong G$。$\blacksquare$

## 五、应用与意义

### 1. 素数分裂的完全描述

Artin 互反律完全描述了素数在 Abel 扩张中的分裂行为。素数 $\mathfrak{p}$ 在 $L/K$ 中完全分裂当且仅当 $\left(\frac{L/K}{\mathfrak{p}}\right) = 1$，即 $\mathfrak{p}$ 属于 Artin 映射的核。由互反律，这等价于 $\mathfrak{p}$ 属于某个射线类群的特定子群——一个纯粹的"同余条件"。

### 2. 二次互反律的推广

当 $K = \mathbb{Q}$，$L = \mathbb{Q}(\sqrt{d})$ 时，Artin 互反律退化为经典的二次互反律（及其补充律）。对一般的 Abel 扩张，Artin 互反律是二次互反律的最自然推广。

### 3. Kronecker-Weber 定理

作为 Artin 互反律的推论，**Kronecker-Weber 定理**断言：$\mathbb{Q}$ 的每个有限 Abel 扩张都包含在某个分圆域 $\mathbb{Q}(\zeta_n)$ 中。这可以看作 Artin 互反律在 $K = \mathbb{Q}$ 时的具体表现。

### 4. 非 Abel 推广：Langlands 纲领

Artin 互反律描述的是 Abel 扩张（交换 Galois 群）。对非 Abel 扩张，**Langlands 纲领**提出了深刻的推广：将 Galois 表示与自守表示联系起来。Artin 互反律可以看作 Langlands 互反猜想在 1 维表示时的情形。

### 5. 计算数论

Artin 互反律在计算中有直接应用：
- 判定素数在给定的 Abel 扩张中的分裂行为。
- 构造具有指定 Galois 群的 Abel 扩张（通过射线类域构造）。
- 计算类域论中的导子和 Artin 映射。

### 6. 对现代数学的深远影响

Artin 互反律和类域论的发展深刻影响了 20 世纪数学的多个方向：
- **上同调方法：** 类域论可以用群上同调重新表述（Tate 的全局类域论）。
- **局部类域论：** 局部域 $K_v$ 的 Abel 扩张由 $K_v^\times$ 的闭子群描述（局部 Artin 映射）。
- **几何类域论：** 代数曲线上的类域论（Arakelov 几何、几何 Langlands 纲领）。
