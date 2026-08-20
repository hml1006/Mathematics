# 力迫与Martin公理

> **一句话大白话**：Martin 公理（$MA$）是一条"中等强度"的公设：对度量空间配得上 force 的闭集的交集，若每族可数就不空，从而统一了大量看起来不相干的独立命题；配合 $2^{\aleph_0}$ 相当大时，它的推论像"可数可加测度处处成立"。
>
> **小例子**：$MA+\neg \mathrm{CH}$ 可推出"可数个开逼近的树都有分支""$\mathfrak p=\mathfrak c$"等；它是 $\mathrm{CH}$ 的友好替代，常用于证明在 ZFC 中独立的命题。

## 介绍

Martin公理（Martin's Axiom，MA）由Donald A. Martin和Robert M. Solovay于1970年提出，是力迫法理论的直接产物。MA是连续统假设CH的一种"弱化"替代：它断言当偏序集满足可数链条件（c.c.c.）时，对任意少于 $2^{\aleph_0}$ 个稠密集，存在一个与之相交的滤子。MA + $\lnot$CH（即 $2^{\aleph_0} > \aleph_1$ 且MA成立）构成一个比ZFC + CH更强的理论，它蕴含大量组合数学、拓扑学和泛函分析中的结论，同时避免了CH的一些反直觉推论。MA是力迫法在组合集合论中最深刻的应用之一。

## 分析

**前置依赖**：ZFC公理系统、力迫法、偏序集、可数链条件（c.c.c.）、稠密集、滤子、泛型、基数、连续统假设。

**定理内容**（Martin公理MA）：对任意满足可数链条件（c.c.c.）的偏序集 $\mathbb{P} = (P, \leq)$ 和任意少于 $2^{\aleph_0}$ 个 $\mathbb{P}$ 的稠密子集族 $\{D_\alpha\}_{\alpha < \kappa}$（$\kappa < 2^{\aleph_0}$），存在 $\mathbb{P}$ 上的滤子 $G$，使得 $G \cap D_\alpha \neq \varnothing$ 对所有 $\alpha < \kappa$ 成立。

**数学内涵**：
- c.c.c.条件：$\mathbb{P}$ 中不存在大小超过 $\aleph_0$ 的不交族（即所有反链都是可数的）。
- MA是CH的"极大化"版本：在CH（$2^{\aleph_0} = \aleph_1$）下，MA可由力迫法基本性质直接推出，故MA在ZFC中不独立于CH。
- MA + $\lnot$CH（$2^{\aleph_0} > \aleph_1$）是一个比ZFC更丰富的理论，它蕴含许多组合的结果。
- MA($\kappa$) 表示MA对少于 $\kappa$ 个稠密集成立；MA即MA($2^{\aleph_0}$)。

**证明策略**：
- MA本身是通过力迫法的"迭代力迫"技术构造的，它是对力迫法中泛型存在性的极大化推广。
- 证明MA与CH的关系：若CH成立，则MA自动成立（因为 $\kappa \leq \aleph_1$，力迫法的Rasiowa-Sikorski引理保证存在性）。
- 证明MA + $\lnot$CH相对于ZFC的一致性：通过有限支撑迭代力迫构造一个模型，其中 $2^{\aleph_0} = \aleph_2$ 且MA成立。
- 应用MA证明组合结论（如 $\aleph_1$ 不是Lebesgue可测集的并等）。

## 思考过程

Martin公理的核心思想是"泛型存在性"的推广：在力迫法中，我们只需要一个与可数多个稠密集相交的滤子（Rasiowa-Sikorski引理），而MA要求与任意少于 $2^{\aleph_0}$ 个稠密集相交。当 $2^{\aleph_0} > \aleph_1$ 时，MA给出了比ZFC更强的组合推论。

MA最著名的推论之一是：在MA + $\lnot$CH下，$\aleph_1$ 个Lebesgue零测集的并仍然是零测集（即Lebesgue测度是 $\aleph_1$-可加的）。这推翻了在CH下可能成立的"覆盖引理"的反直觉结论。因此，MA + $\lnot$CH被许多数学家认为是一种"更自然"的集合论假设。

## 证明过程

**定理**（Martin公理的一致性）：若ZFC一致，则ZFC + MA + $\lnot$CH一致。

**证明**（迭代力迫法纲）：

### 1. 构造目标

从ZFC的可数传递模型 $M$ 出发，构造一个力迫扩张 $M[G]$，使得 $M[G] \models 2^{\aleph_0} = \aleph_2$ 且 $M[G] \models \text{MA}$。

### 2. 力迫概念的枚举

在 $M$ 中，所有c.c.c.偏序集的数量为 $\aleph_2$。枚举所有c.c.c.偏序集 $\{\mathbb{P}_\alpha\}_{\alpha < \aleph_2}$。

### 3. 有限支撑迭代力迫

构造一个长度为 $\aleph_2$ 的迭代力迫 $\langle \mathbb{Q}_\alpha, \dot{\mathbb{R}}_\alpha \rangle_{\alpha < \aleph_2}$：
- $\mathbb{Q}_0$ 是平凡偏序。
- 在阶段 $\alpha$，选择 $\dot{\mathbb{R}}_\alpha$ 使得 $\mathbb{Q}_{\alpha+1} = \mathbb{Q}_\alpha * \dot{\mathbb{R}}_\alpha$ 是c.c.c.的，且 $\dot{\mathbb{R}}_\alpha$ 对应于 $\mathbb{P}_\alpha$（若 $\mathbb{P}_\alpha$ 在 $\mathbb{Q}_\alpha$ 扩张后仍是c.c.c.的）。
- 极限阶段取有限支撑。

### 4. 迭代的c.c.c.性质

有限支撑迭代保持c.c.c.性质：若每个 $\dot{\mathbb{R}}_\alpha$ 强制是c.c.c.的，则整个迭代 $\mathbb{Q}_{\aleph_2}$ 也是c.c.c.的。

### 5. 基数保持性

由于 $\mathbb{Q}_{\aleph_2}$ 是c.c.c.的，所有基数在扩张中保持不变。因此 $\aleph_1^M$ 和 $\aleph_2^M$ 在 $M[G]$ 中仍然是 $\aleph_1$ 和 $\aleph_2$。

### 6. MA的验证

在最终扩张 $M[G]$ 中，对任意c.c.c.偏序集 $\mathbb{P} \in M[G]$ 和任意少于 $2^{\aleph_0} = \aleph_2$ 个稠密集，存在某个阶段 $\alpha$ 使得 $\mathbb{P}$ 已被处理。由构造，存在泛型滤子与所有稠密集相交。$\square$

**定理**（MA的推论）：在MA + $\lnot$CH下，以下命题成立：

1. **Lebesgue测度的 $\aleph_1$-可加性**：$\aleph_1$ 个零测集的并仍然是零测集。
2. **Suslin假设**：Suslin线不存在（即每个稠密全序集要么有可数子集要么有不可数子集，等价于每个树高为 $\aleph_1$ 的树要么有可数链要么有不可数反链）。
3. **白色原则（Whitehead Problem）**：每个Whitehead群是自由的（这是代数中的结论，由Shelah证明依赖于MA）。
4. **Baire性质**：每个 $\Sigma_2^1$ 集（投影集）具有Baire性质。

**证明**（以Lebesgue测度的 $\aleph_1$-可加性为例）：

设 $\{A_\alpha\}_{\alpha < \aleph_1}$ 是零测集。对每个 $\alpha$，存在开覆盖 $U_{\alpha,n}$ 使得 $\mu(U_{\alpha,n}) < 2^{-n}$。考虑偏序集 $\mathbb{P}$ 为所有有限部分函数 $p: \aleph_1 \times \omega \to \omega$，使得 $\bigcup_{\beta \in \text{dom}(p)} U_{\beta, p(\beta, \cdot)}$ 的测度可控。$\mathbb{P}$ 是c.c.c.的。由MA，存在滤子 $G$ 与 $\aleph_1$ 个稠密集相交，从而构造出覆盖 $\bigcup_\alpha A_\alpha$ 的零测集。$\square$