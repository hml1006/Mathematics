# Lie 定理

> **一句话大白话**：可解李代数说白了就是"能同时变成上三角"的代数——它的所有元素能找同一个坐标系，让它们排成上三角阵，就像一串可逐步"剥开"的洋葱。
>
> **小例子**：所以严格上三角矩阵构成的代数（即幂零三角代数）是平凡可解的，而任意可解李代数在合适的基下每个 $X$ 都成为上三角矩阵 $\begin{pmatrix}\cdots&\cdots\\0&*\end{pmatrix}$。

## 介绍

Lie 定理（也称为 Lie 可解性定理）是李代数结构理论中的基本定理，它给出了可解李代数的特征刻画：一个有限维复李代数是可解的当且仅当其所有元素在某个基下同时是上三角矩阵。该定理由挪威数学家 Sophus Lie 在其创立连续群理论的奠基性工作中证明，是李代数可解性理论的核心结果。

## 分析

**前置依赖**：李代数的定义、可解李代数、导代数、上三角矩阵、旗、不变子空间、线性变换的三角化。

**定理内容**：设 $\mathfrak{g}$ 是域 $\mathbb{C}$ 上的有限维可解李代数，$V$ 是有限维 $\mathfrak{g}$-模（即 $\mathfrak{g}$ 到 $\mathfrak{gl}(V)$ 的李代数同态）。则存在 $V$ 的一组基，使得每个 $X \in \mathfrak{g}$ 在该基下的矩阵是上三角矩阵。

等价地，对可解李代数 $\mathfrak{g}$ 的任意有限维表示 $\rho: \mathfrak{g} \to \mathfrak{gl}(V)$，存在 $V$ 中的旗（即一列递增子空间）
$$0 = V_0 \subset V_1 \subset \cdots \subset V_n = V$$
使得每个 $V_i$ 是 $\mathfrak{g}$-不变子空间，且 $\dim V_i = i$。

**数学内涵**：Lie 定理表明，可解李代数的表示总可以同时三角化。这与 Engel 定理（幂零李代数的表示可以同时严格上三角化）形成平行对应。Lie 定理的结论反映了可解李代数的"可分解性"——其表示可以分解为一维不变子空间的逐次扩张。

**证明策略**：证明使用归纳法。关键在于证明存在一维 $\mathfrak{g}$-不变子空间（即公共特征向量）。这需要利用 $\mathfrak{g}$ 的可解性来构造这样的向量。具体地，取 $\mathfrak{g}$ 的余维数为 1 的理想 $\mathfrak{h}$（由可解性保证存在），由归纳假设，存在 $V$ 中的 $\mathfrak{h}$-不变旗。然后分析 $\mathfrak{g} = \mathfrak{h} \oplus \langle X \rangle$ 中 $X$ 的作用，证明可以找到 $X$ 的某个特征向量，扩展得到 $\mathfrak{g}$-不变旗。

## 思考过程

Lie 定理证明的关键在于利用可解李代数的结构性质：若 $\mathfrak{g}$ 是可解的，则 $\mathfrak{g}$ 的导代数 $[\mathfrak{g}, \mathfrak{g}]$ 是幂零的（实际上，$[\mathfrak{g}, \mathfrak{g}]$ 的李代数同态于某个可解李代数的子代数等）。

更直接地，证明思路如下：
1. 设 $\mathfrak{g}$ 是可解李代数，$\mathfrak{h} \subset \mathfrak{g}$ 是余维数为 1 的理想（这样的理想存在，因为 $\mathfrak{g}$ 可解意味着 $\mathfrak{g}/[\mathfrak{g},\mathfrak{g}]$ 是交换的且非零）。
2. 对 $\dim V$ 进行归纳。
3. 由归纳假设，在 $V$ 中存在 $\mathfrak{h}$-不变旗。
4. 关键是证明存在 $V$ 中的非零向量 $v$ 是 $\mathfrak{g}$ 中所有元素的公共特征向量。
5. 为此，取 $W = \{v \in V \mid \mathfrak{h}v \subseteq \mathbb{C}v\}$，即 $V$ 中为 $\mathfrak{h}$ 所有元素公共特征向量的子空间。
6. 设 $X \in \mathfrak{g} \setminus \mathfrak{h}$，则 $XW \subseteq W$。由于 $\mathbb{C}$ 是代数闭域，$X|_W$ 有特征向量 $v \in W$。
7. 则 $v$ 是 $\mathfrak{g}$ 中所有元素的公共特征向量，$\mathbb{C}v$ 是一维 $\mathfrak{g}$-不变子空间。
8. 对 $V/\mathbb{C}v$ 使用归纳假设，得到 $\mathfrak{g}$-不变旗。

## 证明过程

**定理**（Lie）：设 $\mathfrak{g}$ 是 $\mathbb{C}$ 上的有限维可解李代数，$V$ 是有限维 $\mathfrak{g}$-模。则存在 $V$ 中的旗
$$0 = V_0 \subset V_1 \subset \cdots \subset V_n = V$$
使得每个 $V_i$ 是 $\mathfrak{g}$-子模（即 $\mathfrak{g}$-不变子空间）。

**证明**：对 $\dim V$ 进行归纳。$\dim V = 0$ 或 $1$ 时结论平凡。

**步骤 1**：寻找 $\mathfrak{g}$ 的余维数为 1 的理想。由于 $\mathfrak{g}$ 可解，$\mathfrak{g}/[\mathfrak{g},\mathfrak{g}]$ 是非零交换李代数。取 $\mathfrak{h} \subset \mathfrak{g}$ 使得 $\mathfrak{h} \supseteq [\mathfrak{g},\mathfrak{g}]$ 且 $\dim(\mathfrak{g}/\mathfrak{h}) = 1$。则 $\mathfrak{h}$ 是 $\mathfrak{g}$ 的理想（因为 $[\mathfrak{g}, \mathfrak{h}] \subseteq [\mathfrak{g},\mathfrak{g}] \subseteq \mathfrak{h}$），且余维数为 1。

**步骤 2**：对 $\mathfrak{h}$ 应用归纳假设。$\mathfrak{h}$ 是可解的（可解李代数的子代数仍可解），故存在 $V$ 中的 $\mathfrak{h}$-不变旗，特别地，存在非零向量 $v \in V$ 是 $\mathfrak{h}$ 中所有元素的公共特征向量：
$$Hv = \lambda(H)v,\quad \forall H \in \mathfrak{h}$$
其中 $\lambda: \mathfrak{h} \to \mathbb{C}$ 是线性函数。

**步骤 3**：构造 $\mathfrak{h}$-特征子空间。令
$$W = \{w \in V \mid Hw = \lambda(H)w,\ \forall H \in \mathfrak{h}\}$$
即 $\mathfrak{h}$ 的公共 $\lambda$-特征空间。它是 $V$ 的非零子空间。

**步骤 4**：证明 $W$ 是 $\mathfrak{g}$-不变的。取 $X \in \mathfrak{g} \setminus \mathfrak{h}$，对任意 $H \in \mathfrak{h}$ 和 $w \in W$，
$$H(Xw) = X(Hw) + [H,X]w = X(\lambda(H)w) + \lambda([H,X])w = \lambda(H)(Xw) + \lambda([H,X])w$$
由于 $[H,X] \in [\mathfrak{g},\mathfrak{g}] \subseteq \mathfrak{h}$，且 $\lambda$ 在 $\mathfrak{h}$ 上定义，最后一项需要进一步分析。

实际上，我们需要证明 $Xw \in W$。为此，对任意 $H \in \mathfrak{h}$ 和 $w \in W$，考虑 $H(Xw)$。由于 $\mathfrak{h}$ 是理想，$[H,X] \in \mathfrak{h}$。但 $\lambda$ 在 $[\mathfrak{g},\mathfrak{g}]$ 上为零（因为 $\mathfrak{g}$ 可解，$\lambda$ 是 $\mathfrak{h}/[\mathfrak{g},\mathfrak{g}]$ 上的线性函数，而 $[\mathfrak{g},\mathfrak{g}] \subseteq \mathfrak{h}$ 且 $\lambda([\mathfrak{g},\mathfrak{g}]) = 0$）。故 $H(Xw) = \lambda(H)(Xw)$，即 $Xw \in W$。

**步骤 5**：取 $X$ 在 $W$ 上的特征向量。$X|_W: W \to W$ 是线性变换，在 $\mathbb{C}$ 上有特征值 $\mu$ 和特征向量 $v_0 \in W$。则 $\mathbb{C}v_0$ 是 $\mathfrak{g}$-不变子空间（由 $\mathfrak{h}$ 和 $X$ 共同生成）。

**步骤 6**：归纳完成。在 $V_1 = \mathbb{C}v_0$ 上，$\mathfrak{g}$ 的作用是标量乘。考虑商模 $V/V_1$，由归纳假设，存在 $V/V_1$ 中的 $\mathfrak{g}$-不变旗。拉回得到 $V$ 中的 $\mathfrak{g}$-不变旗，且包含 $V_1$。$\square$

**推论**：若 $\mathfrak{g}$ 是 $\mathbb{C}$ 上的可解李代数，则 $\mathfrak{g}$ 的每个不可约表示是一维的。