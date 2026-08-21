# Abel范畴

> **一句话大白话**：一个能"做加法、有核、能取商、行列互换也凑合"的范畴——宛如模块世界的抽象版；Abel 范畴上可以自然定义同调、正合列与导出函子。
>
> **小例子**：$\mathbf{Mod}_R$（$R$-模范畴）、$\mathbf{Ab}$、层范畴都是 Abel 范畴；正合列 $0\to A\to B\to C\to 0$ 完全在范畴语言里进行而不必管元素。

## 介绍

Abel范畴（Abelian Category）是范畴论中一种重要的范畴类型，它结合了加性范畴和某些良好性质，使得可以在其中进行同调代数运算。Abel范畴的概念由 Alexandre Grothendieck 在其1957年的里程碑论文《Sur quelques points d'algèbre homologique》中系统阐述。Abel范畴是核与余核都存在且满足某些相容性条件的加性范畴，其核心性质是：每个态射都有核和余核，且每个单态射都是余核，每个满态射都是核。典型例子包括：Abel群范畴 $\mathbf{Ab}$、环上的模范畴 $\mathbf{R\text{-}Mod}$、以及某些函子范畴。

## 分析

**前置依赖**：加性范畴、核与余核、单态射与满态射、正合序列。

**定义**：范畴 $\mathcal{A}$ 称为 **Abel范畴**，如果满足：
1. $\mathcal{A}$ 是加性范畴（存在零对象、有限双积、Hom集为Abel群且复合双线性）。
2. 每个态射都有核和余核。
3. 每个单态射都是其余核的核，每个满态射都是其核的余核。

**等价条件**：$\mathcal{A}$ 是Abel范畴当且仅当它是加性范畴且满足：
- 每个态射 $f: A \to B$ 有标准分解 $A \to \mathrm{Coim}(f) \to \mathrm{Im}(f) \to B$，且诱导态射 $\mathrm{Coim}(f) \to \mathrm{Im}(f)$ 是同构。

**依赖的概念**：加性范畴、核、余核、单态射、满态射、正合序列。

**基本定理**：
- **蛇形引理**：在Abel范畴中，给定短正合序列的行之间的交换图，存在连接态射使得核序列、余核序列和连接态射形成一个长正合序列。
- **五引理**：在Abel范畴中，如果交换图的两行正合且中间四个态射中有五个是双射，则第五个也是双射。
- **九引理**（3×3引理）：在Abel范畴中，如果三行正合、三列正合，则所有行和列都正合。

## 思考过程

Abel范畴的公理化是对Abel群范畴和模范畴中同调性质的抽象。其核心思想是：**一个好的范畴应该允许进行"正合性"推理**，而不需要关心具体对象是什么。

关键概念是**正合序列**：序列 $A \xrightarrow{f} B \xrightarrow{g} C$ 在 $B$ 处正合当且仅当 $\mathrm{Im}(f) = \ker(g)$。在Abel范畴中，我们可以证明：
- 每个态射 $f$ 可以分解为满态射（到 $\mathrm{Coim}(f)$）和单态射（从 $\mathrm{Im}(f)$ 出发）的复合。
- 同态基本定理（第一同构定理）成立：$\mathrm{Coim}(f) \cong \mathrm{Im}(f)$。

Abel范畴为同调代数提供了最自然的框架。在Abel范畴中，可以定义复形、同调、导出函子等一系列概念，并证明这些概念在范畴论层面具有泛性质。

## 证明过程

**定理**（Abel范畴的基本性质）：设 $\mathcal{A}$ 是Abel范畴，$f: A \to B$ 是任意态射。则
1. 若 $f$ 是单态射，则 $f = \ker(\mathrm{coker}(f))$。
2. 若 $f$ 是满态射，则 $f = \mathrm{coker}(\ker(f))$。
3. $\mathrm{coim}(f) \cong \mathrm{im}(f)$。

**证明**：

**步骤 1：基本分解。**

记 $k = \ker(f): K \to A$，$c = \mathrm{coker}(f): B \to C$。由定义，$f \circ k = 0$，$c \circ f = 0$。

由 $c \circ f = 0$，存在唯一的 $f': A \to \ker(c)$ 使得 $f = \ker(c) \circ f'$。记 $\mathrm{im}(f) = \ker(c)$，$m = \ker(c)$。

由 $f \circ k = 0$ 且 $m$ 是单态射，有 $f' \circ k = 0$。于是存在唯一的 $f'': \mathrm{coim}(f) \to \mathrm{im}(f)$ 使得 $f' = m' \circ f''$，其中 $m' = \mathrm{coker}(k)$ 是 $\mathrm{coim}(f)$。

**步骤 2：证明 $f''$ 是同构。**

由Abel范畴的定义，$\mathrm{coim}(f) \to \mathrm{im}(f)$ 是同构。这等价于每个单态射是余核、每个满态射是核。

具体地，考虑 $f$ 的分解：

$$
A \xrightarrow{q} \mathrm{coim}(f) \xrightarrow{\overline{f}} \mathrm{im}(f) \xrightarrow{m} B
$$

其中 $q = \mathrm{coker}(\ker(f))$ 是满态射，$m = \ker(\mathrm{coker}(f))$ 是单态射。由Abel范畴的定义，$\overline{f}$ 是同构。$\square$

**定理**（蛇形引理）：在Abel范畴 $\mathcal{A}$ 中，给定交换图

$$
\begin{CD}
0 @>>> A' @>>> A @>>> A'' @>>> 0 \\
@. @V{f'}VV @V{f}VV @V{f''}VV \\
0 @>>> B' @>>> B @>>> B'' @>>> 0
\end{CD}
$$

其中行正合，则存在长正合序列

$$
\ker(f') \to \ker(f) \to \ker(f'') \xrightarrow{\delta} \mathrm{coker}(f') \to \mathrm{coker}(f) \to \mathrm{coker}(f'').
$$

**证明概要**：

**步骤 1：构造核序列。**
由正合性和交换性，$\ker(f') \to \ker(f) \to \ker(f'')$ 正合。这通过拉回论证得到。

**步骤 2：构造余核序列。**
对偶地，$\mathrm{coker}(f') \to \mathrm{coker}(f) \to \mathrm{coker}(f'')$ 正合。

**步骤 3：构造连接态射 $\delta$。**
连接态射 $\delta: \ker(f'') \to \mathrm{coker}(f')$ 的构造是蛇形引理的核心。取 $x \in \ker(f'')$，通过满态射 $A \to A''$ 提升到 $a \in A$。由交换性，$f(a)$ 映到 $B''$ 中的零，故 $f(a) \in \mathrm{im}(B' \to B)$。取 $b' \in B'$ 使得 $f(a) = \varphi(b')$，则 $\delta(x) = [b'] \in \mathrm{coker}(f')$。

**步骤 4：验证正合性。**
可以验证 $\ker(f'') \xrightarrow{\delta} \mathrm{coker}(f')$ 的核等于 $\ker(f) \to \ker(f'')$ 的像，且 $\delta$ 的像等于 $\mathrm{coker}(f') \to \mathrm{coker}(f)$ 的核。$\square$

**推论**（五引理）：在Abel范畴中，若

$$
\begin{CD}
A_1 @>>> A_2 @>>> A_3 @>>> A_4 @>>> A_5 \\
@V{f_1}VV @V{f_2}VV @V{f_3}VV @V{f_4}VV @V{f_5}VV \\
B_1 @>>> B_2 @>>> B_3 @>>> B_4 @>>> B_5
\end{CD}
$$

行正合，且 $f_1, f_2, f_4, f_5$ 是同构，则 $f_3$ 也是同构。

**证明**：应用蛇形引理到适当的子图即可。$\square$