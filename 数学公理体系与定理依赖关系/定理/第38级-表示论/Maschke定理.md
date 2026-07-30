# Maschke定理

## 介绍

Maschke定理（Maschke's Theorem）是群表示论中的基本定理，由海因里希·马斯赫于 1899 年证明。该定理给出了群代数半单性的充要条件，断言：有限群 $G$ 在域 $k$ 上的群代数 $k[G]$ 是半单的（即每个有限维表示都是完全可约的）当且仅当 $k$ 的特征不整除 $G$ 的阶。Maschke定理是表示论的基础，它保证了在特征不整除群阶的条件下，有限维表示可以分解为不可约表示的直和。

## 分析

**前置依赖**：群论、表示论基础、群代数、模论、半单代数。

**数学内涵**：

**定理内容**：设 $G$ 是有限群，$k$ 是域。则以下条件等价：
1. 群代数 $k[G]$ 是半单的（即每个 $k[G]$-模是投射的）。
2. 每个有限维 $k[G]$-模是完全可约的（即可分解为不可约子模的直和）。
3. $\operatorname{char}(k) \nmid |G|$（$k$ 的特征不整除 $G$ 的阶）。

**特别地**，当 $\operatorname{char}(k) = 0$ 时（如 $k = \mathbb{C}$），条件自动满足。

**数学内涵**：Maschke定理表明，在特征不整除群阶的条件下，群表示论可以"线性化"——每个表示都可以分解为不可约表示的直和，大大简化了表示的分类。

**证明策略**：通过构造"平均算子"（averaging operator）证明任何子表示都有补表示。

## 思考过程

Maschke定理的核心是"平均技巧"：给定一个 $G$-不变子空间 $W \subseteq V$，取 $V$ 到 $W$ 的任意线性投影 $p$，然后通过群作用"平均化"得到 $G$-等变投影 $\tilde{p} = \frac{1}{|G|} \sum_{g \in G} g \circ p \circ g^{-1}$。这个平均投影的核就是 $W$ 的 $G$-不变补空间。

关键条件是 $|G|$ 在 $k$ 中可逆，即 $\operatorname{char}(k)$ 不整除 $|G|$。当特征整除 $|G|$ 时，平均算子无法定义，实际上存在非完全可约的表示（模表示论）。

## 证明过程

**定理**（Maschke定理）：设 $G$ 是有限群，$k$ 是域，$\operatorname{char}(k) \nmid |G|$。则每个有限维 $k[G]$-模是完全可约的。

**证明**：

**步骤 1**：设 $V$ 是有限维 $k[G]$-模，$W \subseteq V$ 是 $G$-不变子模。需要证明存在 $G$-不变子模 $U \subseteq V$ 使得 $V = W \oplus U$。

**步骤 2**：取任意线性投影 $p: V \to W$（即 $p$ 是 $k$-线性映射，$p|_W = \operatorname{id}_W$，$p^2 = p$）。$p$ 不一定与 $G$ 作用交换。

**步骤 3**：定义平均算子：
$$
\tilde{p}(v) = \frac{1}{|G|} \sum_{g \in G} g \cdot p(g^{-1} \cdot v)
$$
这里 $\frac{1}{|G|}$ 有意义因为 $\operatorname{char}(k) \nmid |G|$。

**步骤 4**：验证 $\tilde{p}$ 是 $G$-等变的（即与 $G$ 作用交换）：
$$
\begin{aligned}
\tilde{p}(h \cdot v) &= \frac{1}{|G|} \sum_{g \in G} g \cdot p(g^{-1}h \cdot v) \\
&= \frac{1}{|G|} \sum_{g' \in G} h g' \cdot p(g'^{-1} \cdot v) \quad (\text{令 } g' = h^{-1}g) \\
&= h \cdot \frac{1}{|G|} \sum_{g' \in G} g' \cdot p(g'^{-1} \cdot v) = h \cdot \tilde{p}(v)
\end{aligned}
$$

**步骤 5**：验证 $\tilde{p}$ 是到 $W$ 的投影：
- 对 $w \in W$，$g^{-1} \cdot w \in W$，故 $p(g^{-1} \cdot w) = g^{-1} \cdot w$，从而 $\tilde{p}(w) = \frac{1}{|G|} \sum_{g \in G} g \cdot (g^{-1} \cdot w) = \frac{1}{|G|} \sum_{g \in G} w = w$。
- 对任意 $v \in V$，$p(g^{-1} \cdot v) \in W$，故 $g \cdot p(g^{-1} \cdot v) \in W$，从而 $\tilde{p}(v) \in W$。
- $\tilde{p}^2 = \tilde{p}$（因为是到 $W$ 的投影）。

**步骤 6**：令 $U = \ker \tilde{p}$。由于 $\tilde{p}$ 是 $G$-等变的，$U$ 是 $G$-不变子模。且 $V = W \oplus U$（因为 $\tilde{p}$ 是投影）。

**步骤 7**：由归纳法，$V$ 可以分解为不可约子模的直和。$\square$

### 逆命题

**定理**（Maschke定理的逆）：若 $\operatorname{char}(k) \mid |G|$，则 $k[G]$ 不是半单的。

**证明**：考虑正则表示 $k[G]$，需要证明存在不可分解的子模。设 $p = \operatorname{char}(k)$，$G$ 的阶为 $p^a m$ 其中 $p \nmid m$。

关键观察：$k[G]$ 中的元素 $s = \sum_{g \in G} g$ 生成一个 $G$-不变子模，且 $s^2 = |G| s = 0$（因为 $\operatorname{char}(k) \mid |G|$）。因此 $\langle s \rangle$ 是 $k[G]$ 的子模，但它在 $k[G]$ 中没有 $G$-不变补模（可以通过分析 $s$ 的性质证明）。$\square$

### 推论

**推论 1**（复数域上的表示）：在复数域 $\mathbb{C}$ 上，有限群 $G$ 的每个有限维表示都是完全可约的。

**推论 2**（不可约分解）：在 Maschke 定理的条件下，每个有限维表示 $V$ 可以唯一地分解为不可约表示的直和：
$$
V \cong \bigoplus_i n_i V_i
$$
其中 $V_i$ 是互不相同的不可约表示，$n_i$ 是重数。

**推论 3**（群代数的结构）：$k[G] \cong \bigoplus_i \operatorname{End}_{k}(V_i)$ 作为 $k$-代数，其中 $V_i$ 取遍所有不可约 $k[G]$-模的同构类。

**应用**：Maschke定理是群表示论的基础，保证了特征零域上表示的完全可约性，为特征标理论、诱导表示等后续理论的发展奠定了基础。$\square$