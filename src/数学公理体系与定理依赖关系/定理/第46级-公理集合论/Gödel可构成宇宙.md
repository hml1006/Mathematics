# Gödel可构成宇宙

> **一句话大白话**：Gödel 从序数出发"逐层"造出来最小的一串宇宙 $L=\bigcup_\alpha L_\alpha$，只有那些"能用定义造出来"的集合——在这个宝藏箱里 $V=L$（可构成性公理）且 $\mathrm{CH}$、$\mathrm{AC}$、$\mathrm{GCH}$ 全部天然成立。
>
> **小例子**：$L$ 里 $2^{\aleph_0}=\aleph_0^{\aleph_0}$ 被 $=\aleph_1$ 框住，$\mathrm{CH}$ 恒真；$V=L$ 是 $\mathrm{CH}$ 一致性的第一条证据，也是"内模型纲领"的原型。

## 介绍

Gödel可构成宇宙（Gödel's Constructible Universe），记作 $\mathbf{L}$，是Kurt Gödel于1938年提出的一个内模型。Gödel构造了 $\mathbf{L}$ 以证明ZFC公理系统的相对一致性，并证明了连续统假设（CH）在 $\mathbf{L}$ 中成立。$\mathbf{L}$ 是ZFC的最小内模型，其核心思想是：只使用已被定义出来的集合来构造新集合，即"从低到高"逐层定义集合。$\mathbf{L}$ 的构造是集合论历史上最深刻的思想之一，它开创了内模型理论，并深刻地影响了后来力迫法和集合论公理体系的发展。

## 分析

**前置依赖**：ZFC公理系统、序数、von Neumann层级、可定义性、绝对性、哥德尔数。

**定理内容**（Gödel）：存在一个ZFC的可传递类 $\mathbf{L}$，满足：
1. $\mathbf{L}$ 是ZFC的内模型（即 $\mathbf{L} \models \text{ZFC}$）。
2. $\mathbf{L}$ 是ZFC的最小的包含所有序数的可传递内模型（即若 $M$ 是ZFC的可传递内模型且 $\text{Ord} \subseteq M$，则 $\mathbf{L} \subseteq M$）。
3. 在 $\mathbf{L}$ 中连续统假设成立：$\mathbf{L} \models 2^{\aleph_0} = \aleph_1$。
4. 在 $\mathbf{L}$ 中广义连续统假设成立：$\mathbf{L} \models 2^{\aleph_\alpha} = \aleph_{\alpha+1}$ 对所有序数 $\alpha$ 成立。

**数学内涵**：
- $\mathbf{L}$ 的构造是通过对序数的超穷递归完成的：$\mathbf{L}_0 = \varnothing$，$\mathbf{L}_{\alpha+1} = \text{Def}(\mathbf{L}_\alpha)$（$\mathbf{L}_\alpha$ 的可定义子集），极限序数时取并。
- $\text{Def}(X)$ 表示 $X$ 的所有可以用公式（带参数）在 $X$ 中定义出的子集。
- $\mathbf{L} = \bigcup_{\alpha \in \text{Ord}} \mathbf{L}_\alpha$。
- $\mathbf{L}$ 中CH成立的关键原因在于 $\mathbf{L}$ 中每个实数的构造都对应一个可数序数，从而 $\mathbb{R} \cap \mathbf{L}$ 可被 $\aleph_1$ 良序。

**证明策略**：
1. 通过超穷递归定义 $\mathbf{L}_\alpha$ 层级，并证明每一层满足相关性质。
2. 验证 $\mathbf{L}$ 满足ZFC的所有公理（利用可定义性封闭性）。
3. 证明 $\mathbf{L}$ 中CH成立：构造 $\mathbf{L}$ 中实数的 $\Sigma_1$ 良序，证明其序型为 $\aleph_1$。
4. 证明 $\mathbf{L}$ 的最小性。

## 思考过程

Gödel可构成宇宙 $\mathbf{L}$ 的核心思想是"限制性"——只通过可定义性来构造集合，而不使用选择公理提供的任意选择。这自然地产生了ZFC的"最小"内模型。有趣的是，在 $\mathbf{L}$ 中，选择公理和连续统假设都自动成立，虽然它们独立于ZFC。这说明：如果ZFC是一致的，那么ZFC+CH也是一致的。

$\mathbf{L}$ 的构造是内模型理论的奠基性工作，它展示了如何通过"可定义性"的层级来构建一个"精简"的集合论宇宙。后来，Silver、Jensen等人在此基础上发展出了更精细的 $\mathbf{L}$ 理论（如 $\square$ 原理、$\diamondsuit$ 原理等）。

## 证明过程

**定理**（Gödel可构成宇宙）：存在可传递类 $\mathbf{L}$ 满足 $\mathbf{L} \models \text{ZFC}$，且 $\mathbf{L} \models \text{CH}$。

**证明**：

### 1. $\mathbf{L}$ 的构造

通过超穷递归定义 $\mathbf{L}_\alpha$：
- $\mathbf{L}_0 = \varnothing$
- $\mathbf{L}_{\alpha+1} = \text{Def}(\mathbf{L}_\alpha)$，其中 $\text{Def}(X) = \{Y \subseteq X \mid Y \text{ 在 } X \text{ 中可用带参数的 } \in\text{-公式定义}\}$
- $\mathbf{L}_\lambda = \bigcup_{\alpha < \lambda} \mathbf{L}_\alpha$（$\lambda$ 为极限序数）

定义 $\mathbf{L} = \bigcup_{\alpha \in \text{Ord}} \mathbf{L}_\alpha$。

### 2. $\mathbf{L}$ 是ZFC的内模型

验证 $\mathbf{L}$ 满足ZFC公理：
- **外延公理**：由于 $\mathbf{L}$ 是传递类，外延公理自动成立。
- **对集公理**：若 $a, b \in \mathbf{L}$，则存在 $\alpha$ 使得 $a, b \in \mathbf{L}_\alpha$，则 $\{a,b\} \in \mathbf{L}_{\alpha+1}$。
- **并集公理**：若 $a \in \mathbf{L}_\alpha$，则 $\bigcup a \subseteq \mathbf{L}_\alpha$，且 $\bigcup a \in \mathbf{L}_{\alpha+1}$。
- **幂集公理**：对 $a \in \mathbf{L}$，$\mathcal{P}(a) \cap \mathbf{L}$ 在 $\mathbf{L}$ 中即是幂集。
- **无穷公理**：$\omega \in \mathbf{L}_{\omega+1}$。
- **分离公理模式**：对任意公式 $\phi$，$\{x \in a \mid \phi^\mathbf{L}(x)\} \in \mathbf{L}$。
- **替换公理模式**：$\mathbf{L}$ 中可定义函数的像仍在 $\mathbf{L}$ 中。
- **选择公理**：$\mathbf{L}$ 的构造本身给出了一个全局良序。

### 3. $\mathbf{L}$ 中CH成立

**引理**：存在一个 $\mathbf{L}$ 上的 $\Sigma_1$ 良序 $<_\mathbf{L}$，使得对任意 $\alpha$，$<_\mathbf{L}$ 限制在 $\mathbf{L}_\alpha$ 上是 $\mathbf{L}_{\alpha+1}$ 的元素。

定义 $<_\mathbf{L}$ 如下：$x <_\mathbf{L} y$ 当且仅当 $x$ 在构造中出现的层级早于 $y$，或同一层级时在某个编码中更小。

**CH的证明**：在 $\mathbf{L}$ 中，$\mathbb{R} \subseteq \mathbf{L}_{\omega_1}$。每个实数对应一个 $\mathbf{L}_{\omega_1}$ 中的元素，而 $|\mathbf{L}_{\omega_1}| = \aleph_1$（因为 $\mathbf{L}_{\alpha}$ 的基数为 $|\alpha|$ 对无穷 $\alpha$ 成立）。因此 $2^{\aleph_0} \leq \aleph_1$，而 $\aleph_1 \leq 2^{\aleph_0}$ 是显然的，故 $2^{\aleph_0} = \aleph_1$。

### 4. $\mathbf{L}$ 的最小性

若 $M$ 是ZFC的可传递内模型且 $\text{Ord} \subseteq M$，则对每个序数 $\alpha$，$\text{Def}(\mathbf{L}_\alpha)^M = \text{Def}(\mathbf{L}_\alpha)$（由绝对性），因此 $\mathbf{L}_\alpha \subseteq M$ 对所有 $\alpha$ 成立，故 $\mathbf{L} \subseteq M$。$\square$

**推论**：若ZFC一致，则ZFC + CH一致。$\square$