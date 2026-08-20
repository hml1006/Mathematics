# 诱导表示与Frobenius互反律

> **一句话大白话**：给一个小群的一个表示"升格"成大群的一个表示（诱导），背后和"大群表示里某个小块的频次数"是同一枚硬币的两面——互反律把"由小放大"和"由大找小"画上了等号。
>
> **小例子**：对 $H\le G$，从 $H$ 的表示诱导出的表示中，大群每个不可约表示的"出现次数"，恰恰等于把它限制回 $H$ 时分解出原表示多少次——一句互换公式就交代清楚。

## 介绍

诱导表示（Induced Representation）是群表示论中由子群表示构造大群表示的基本方法。给定群 $G$ 的子群 $H$ 和 $H$ 的表示 $W$，诱导表示 $\operatorname{Ind}_H^G W$ 是 $G$ 的一个表示，它是在某种意义下"最自由"地扩展 $W$ 到 $G$ 上的表示。Frobenius 互反律（Frobenius Reciprocity）是诱导表示理论的核心定理，它建立了诱导和限制之间的伴随关系，是计算诱导表示的特征标和分析表示结构的基本工具。

## 分析

**前置依赖**：群表示论、特征标理论、子群、陪集、张量积。

**数学内涵**：

**定义**：设 $H \subseteq G$ 是有限群的子群，$(\sigma, W)$ 是 $H$ 的表示。**诱导表示** $\operatorname{Ind}_H^G W$ 定义为
$$
\operatorname{Ind}_H^G W = \{f: G \to W \mid f(hg) = \sigma(h) f(g), \forall h \in H, g \in G\}
$$
$G$ 的作用为 $(g \cdot f)(x) = f(xg)$。

**等价定义**：$\operatorname{Ind}_H^G W \cong \mathbb{C}[G] \otimes_{\mathbb{C}[H]} W$。

**Frobenius 互反律**：设 $H \subseteq G$ 是子群，$V$ 是 $G$ 的表示，$W$ 是 $H$ 的表示。则有自然同构：
$$
\operatorname{Hom}_G(V, \operatorname{Ind}_H^G W) \cong \operatorname{Hom}_H(\operatorname{Res}_H^G V, W)
$$
其中 $\operatorname{Res}_H^G V$ 是 $V$ 限制到 $H$ 上的表示。

**在特征标层面**：设 $\chi$ 是 $V$ 的特征标，$\psi$ 是 $W$ 的特征标，则
$$
\langle \operatorname{Ind}_H^G \psi, \chi \rangle_G = \langle \psi, \operatorname{Res}_H^G \chi \rangle_H
$$

**数学内涵**：Frobenius 互反律表明，诱导和限制是一对伴随函子：$\operatorname{Ind}_H^G$ 是 $\operatorname{Res}_H^G$ 的左伴随。

**证明策略**：通过构造明确的同构映射或利用特征标公式计算内积。

## 思考过程

诱导表示可以理解为"从 $H$ 到 $G$ 的表示扩张"：$H$ 的表示 $W$ 通过诱导得到 $G$ 的表示 $\operatorname{Ind}_H^G W$，其维数为 $[G:H] \cdot \dim W$。

Frobenius 互反律的直观含义是：$G$ 的表示 $V$ 分解中包含 $\operatorname{Ind}_H^G W$ 的重数，等于 $V$ 限制到 $H$ 上后包含 $W$ 的重数。这大大简化了表示分解的计算——将 $G$ 上的问题转化为 $H$ 上的问题。

诱导表示的不可约性判定（Mackey 定理）是 Frobenius 互反律的重要补充，它给出了诱导表示不可约的充要条件。

## 证明过程

### 诱导表示的构造

**定义**（诱导表示）：设 $H \subseteq G$，$(\sigma, W)$ 是 $H$ 的表示。定义
$$
\operatorname{Ind}_H^G W = \{f: G \to W \mid f(hg) = \sigma(h) f(g), \forall h \in H, g \in G\}
$$
$G$ 的作用为 $(g \cdot f)(x) = f(xg)$。

**等价构造**：设 $g_1, \ldots, g_m$ 是 $H$ 在 $G$ 中的陪集代表元（$m = [G:H]$），则
$$
\operatorname{Ind}_H^G W \cong \bigoplus_{i=1}^m g_i \otimes W \cong \mathbb{C}[G] \otimes_{\mathbb{C}[H]} W
$$

### 诱导表示的特征标公式

**定理 1**：设 $\psi$ 是 $H$ 的表示 $W$ 的特征标，则诱导表示 $\operatorname{Ind}_H^G W$ 的特征标为：
$$
\operatorname{Ind}_H^G \psi(g) = \frac{1}{|H|} \sum_{\substack{x \in G \\ x^{-1}gx \in H}} \psi(x^{-1}gx)
$$

**证明**：通过陪集分解和迹的显式计算可得。$\square$

### Frobenius 互反律

**定理 2**（Frobenius 互反律）：设 $H \subseteq G$ 是有限群的子群，$V$ 是 $G$ 的表示，$W$ 是 $H$ 的表示。则：
$$
\operatorname{Hom}_G(V, \operatorname{Ind}_H^G W) \cong \operatorname{Hom}_H(\operatorname{Res}_H^G V, W)
$$

**证明**：

**步骤 1**：定义映射 $\Phi: \operatorname{Hom}_G(V, \operatorname{Ind}_H^G W) \to \operatorname{Hom}_H(\operatorname{Res}_H^G V, W)$。

对 $\varphi: V \to \operatorname{Ind}_H^G W$，定义 $\Phi(\varphi): V \to W$ 为 $\Phi(\varphi)(v) = \varphi(v)(1)$（即取 $\varphi(v)$ 在单位元处的值）。

**步骤 2**：验证 $\Phi(\varphi)$ 是 $H$-等变的。对任意 $h \in H$，$v \in V$：
$$
\begin{aligned}
\Phi(\varphi)(h \cdot v) &= \varphi(h \cdot v)(1) = (h \cdot \varphi(v))(1) \quad (\varphi \text{ 是 } G\text{-等变的}) \\
&= \varphi(v)(1 \cdot h) = \varphi(v)(h) = \sigma(h)(\varphi(v)(1)) = \sigma(h)(\Phi(\varphi)(v))
\end{aligned}
$$

**步骤 3**：定义逆映射 $\Psi: \operatorname{Hom}_H(\operatorname{Res}_H^G V, W) \to \operatorname{Hom}_G(V, \operatorname{Ind}_H^G W)$。

对 $\alpha: V \to W$（$H$-等变），定义 $\Psi(\alpha)(v): G \to W$ 为 $\Psi(\alpha)(v)(g) = \alpha(g^{-1} \cdot v)$。

验证 $\Psi(\alpha)(v) \in \operatorname{Ind}_H^G W$：对 $h \in H$，
$$
\Psi(\alpha)(v)(hg) = \alpha((hg)^{-1} \cdot v) = \alpha(g^{-1}h^{-1} \cdot v) = \sigma(h)(\alpha(g^{-1} \cdot v)) = \sigma(h)(\Psi(\alpha)(v)(g))
$$

验证 $\Psi(\alpha)$ 是 $G$-等变的：
$$
\Psi(\alpha)(g \cdot v)(x) = \alpha(x^{-1}g \cdot v) = \Psi(\alpha)(v)(g^{-1}x) = (g \cdot \Psi(\alpha)(v))(x)
$$

**步骤 4**：验证 $\Phi \circ \Psi = \operatorname{id}$ 和 $\Psi \circ \Phi = \operatorname{id}$。

$\Phi(\Psi(\alpha))(v) = \Psi(\alpha)(v)(1) = \alpha(1^{-1} \cdot v) = \alpha(v)$。

$\Psi(\Phi(\varphi))(v)(g) = \Phi(\varphi)(g^{-1} \cdot v) = \varphi(g^{-1} \cdot v)(1) = (g^{-1} \cdot \varphi(v))(1) = \varphi(v)(g)$。

因此 $\Phi$ 和 $\Psi$ 互为逆映射，给出同构。$\square$

### 特征标层面的 Frobenius 互反律

**定理 3**：设 $\chi$ 是 $G$ 的表示 $V$ 的特征标，$\psi$ 是 $H$ 的表示 $W$ 的特征标。则
$$
\langle \operatorname{Ind}_H^G \psi, \chi \rangle_G = \langle \psi, \operatorname{Res}_H^G \chi \rangle_H
$$

**证明**：由定理 2 和特征标正交性关系，不可约分量的重数等于同态空间的维数：
$$
\langle \operatorname{Ind}_H^G \psi, \chi \rangle_G = \dim \operatorname{Hom}_G(V, \operatorname{Ind}_H^G W) = \dim \operatorname{Hom}_H(\operatorname{Res}_H^G V, W) = \langle \psi, \operatorname{Res}_H^G \chi \rangle_H
$$
$\square$

### 推论

**推论 1**（Mackey 不可约性判别法）：设 $H \subseteq G$，$W$ 是 $H$ 的不可约表示。则 $\operatorname{Ind}_H^G W$ 不可约当且仅当对所有 $g \in G \setminus H$，$W$ 与 $g \cdot W$（$gHg^{-1} \cap H$ 上的表示）没有公共不可约分量。

**推论 2**（诱导表示的维数）：$\dim \operatorname{Ind}_H^G W = [G:H] \cdot \dim W$。

**应用**：诱导表示和 Frobenius 互反律是群表示论中最基本的工具之一，用于构造群的所有不可约表示、分析表示的结构以及在数论（Artin L-函数）和物理中都有重要应用。$\square$