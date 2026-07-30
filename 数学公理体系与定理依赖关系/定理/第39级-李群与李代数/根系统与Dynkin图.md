# 根系统与 Dynkin 图

## 介绍

根系统与 Dynkin 图是半单李代数分类理论的核心工具。根系统是欧几里得空间中的一组向量，满足特定的反射对称性，它完整地编码了半单李代数的结构信息。Dynkin 图则是根系统的图形化表示，通过简洁的图示分类了所有有限维复半单李代数。该理论由 Wilhelm Killing 和 Élie Cartan 在 19 世纪末至 20 世纪初建立，并由 Eugene Dynkin 在 20 世纪 40 年代完善为最终的图论形式。

## 分析

**前置依赖**：半单李代数、Cartan 子代数、根、Killing 型、欧几里得空间、反射变换。

**定理内容**：设 $\mathfrak{g}$ 是有限维复半单李代数，$\mathfrak{h}$ 是 $\mathfrak{g}$ 的 Cartan 子代数（即极大可交换子代数，且 $\text{ad}_H$ 对 $H \in \mathfrak{h}$ 是半单的）。则 $\mathfrak{g}$ 关于 $\mathfrak{h}$ 有根空间分解：
$$\mathfrak{g} = \mathfrak{h} \oplus \bigoplus_{\alpha \in \Phi} \mathfrak{g}_\alpha$$
其中 $\Phi \subset \mathfrak{h}^*$ 是根系统，满足：
1. $\Phi$ 是有限集，张成 $\mathfrak{h}^*$。
2. 对 $\alpha \in \Phi$，$\dim \mathfrak{g}_\alpha = 1$。
3. 对 $\alpha \in \Phi$，$k\alpha \in \Phi$ 当且仅当 $k = \pm 1$。
4. 对 $\alpha, \beta \in \Phi$，$\beta - \frac{2(\beta,\alpha)}{(\alpha,\alpha)}\alpha \in \Phi$（反射不变性）。
5. 对 $\alpha, \beta \in \Phi$，$\frac{2(\beta,\alpha)}{(\alpha,\alpha)} \in \mathbb{Z}$（整性条件）。

**Dynkin 图**：对每个根系统，通过选择一组单根（即构成基的根，使得每个根可唯一表示为单根的整系数线性组合，且系数全正或全负），可以构造 Dynkin 图。Dynkin 图是一个有多个节点的图，其中：
- 每个节点对应一个单根。
- 节点间用 $0,1,2,3$ 条边连接，边数由 $\frac{4(\alpha,\beta)^2}{(\alpha,\alpha)(\beta,\beta)}$ 决定。
- 若边数大于 1，则用箭头指向较短的根。

**分类定理**：所有有限维复半单李代数（从而所有连通紧李群）的 Dynkin 图只能是以下类型之一：
$$A_n\ (n\ge 1),\ B_n\ (n\ge 2),\ C_n\ (n\ge 3),\ D_n\ (n\ge 4),\ E_6,\ E_7,\ E_8,\ F_4,\ G_2$$

**数学内涵**：根系统将半单李代数的结构问题转化为欧几里得空间中的组合/几何问题。Dynkin 图则进一步将分类简化为图论问题。这一分类是数学中最为优雅和深刻的分类结果之一，它统一了看似不同的数学对象。

**证明策略**：分类的证明分为两步。首先，证明每个半单李代数对应一个抽象的根系统。然后，分类所有可能的不可约根系统，证明它们正好对应上述 Dynkin 图。分类的关键是利用单根之间的夹角和长度比关系，通过组合论证枚举所有可能的图。

## 思考过程

根系统的发现源于对半单李代数结构的研究。取 Cartan 子代数 $\mathfrak{h}$，则 $\mathfrak{g}$ 在 $\mathfrak{h}$ 的伴随作用下分解为根空间。每个根 $\alpha \in \mathfrak{h}^*$ 对应一个非零的 $\mathfrak{g}_\alpha$，其中的元素 $E_\alpha$ 满足 $[H, E_\alpha] = \alpha(H)E_\alpha$。

根系统满足的反射性质来自 $\mathfrak{sl}_2$-三元组的结构：对每个根 $\alpha$，存在 $H_\alpha \in \mathfrak{h}$，$E_\alpha \in \mathfrak{g}_\alpha$，$E_{-\alpha} \in \mathfrak{g}_{-\alpha}$ 构成 $\mathfrak{sl}_2$ 的子代数。这个子代数的表示理论给出了根系统上的整性条件（即 $\frac{2(\beta,\alpha)}{(\alpha,\alpha)} \in \mathbb{Z}$）。

Dynkin 图通过单根之间的夹角来编码根系统的结构：
- 单根之间的夹角只能是 $90^\circ, 120^\circ, 135^\circ, 150^\circ$。
- 分别对应边数 $0, 1, 2, 3$。
- 长度比由边数决定：1 边时等长，2 边时 $\sqrt{2}:1$，3 边时 $\sqrt{3}:1$。

## 证明过程

**定理**（半单李代数的根空间分解）：设 $\mathfrak{g}$ 是有限维复半单李代数，$\mathfrak{h}$ 是 Cartan 子代数。则
$$\mathfrak{g} = \mathfrak{h} \oplus \bigoplus_{\alpha \in \Phi} \mathfrak{g}_\alpha$$
其中 $\Phi = \{\alpha \in \mathfrak{h}^* \setminus \{0\} \mid \mathfrak{g}_\alpha \neq 0\}$，$\mathfrak{g}_\alpha = \{X \in \mathfrak{g} \mid [H,X] = \alpha(H)X,\ \forall H \in \mathfrak{h}\}$。

**证明概要**：

**步骤 1**：由于 $\mathfrak{h}$ 中元素在 $\mathfrak{g}$ 上的作用可同时对角化（因为 $\mathfrak{h}$ 交换且 $\text{ad}_H$ 半单），存在根空间分解。

**步骤 2**：由 Killing 型的非退化性，$\Phi$ 张成 $\mathfrak{h}^*$。

**步骤 3**：对 $\alpha \in \Phi$，$[\mathfrak{g}_\alpha, \mathfrak{g}_\beta] \subseteq \mathfrak{g}_{\alpha+\beta}$（约定 $\mathfrak{g}_0 = \mathfrak{h}$）。

**步骤 4**：对 $\alpha \in \Phi$，存在 $H_\alpha \in [\mathfrak{g}_\alpha, \mathfrak{g}_{-\alpha}] \subset \mathfrak{h}$，$E_\alpha \in \mathfrak{g}_\alpha$，$E_{-\alpha} \in \mathfrak{g}_{-\alpha}$ 使得 $\{H_\alpha, E_\alpha, E_{-\alpha}\}$ 同构于 $\mathfrak{sl}_2(\mathbb{C})$。

**步骤 5**：由 $\mathfrak{sl}_2$ 表示理论，$\beta(H_\alpha) = \frac{2(\beta,\alpha)}{(\alpha,\alpha)} \in \mathbb{Z}$，且反射 $s_\alpha(\beta) = \beta - \beta(H_\alpha)\alpha \in \Phi$。

**定理**（Dynkin 图分类）：所有有限维复单李代数对应的不可约根系统分类如下：

| 类型 | Dynkin 图 | 李代数 | 维数 |
|------|-----------|--------|------|
| $A_n$ | $\circ-\circ-\cdots-\circ$ | $\mathfrak{sl}_{n+1}$ | $n(n+2)$ |
| $B_n$ | $\circ-\circ-\cdots-\circ\Rightarrow\circ$ | $\mathfrak{so}_{2n+1}$ | $n(2n+1)$ |
| $C_n$ | $\circ-\circ-\cdots-\circ\Leftarrow\circ$ | $\mathfrak{sp}_{2n}$ | $n(2n+1)$ |
| $D_n$ | $\circ-\circ-\cdots-\circ$ 带分支 | $\mathfrak{so}_{2n}$ | $n(2n-1)$ |
| $E_6$ | 特殊图 | $\mathfrak{e}_6$ | 78 |
| $E_7$ | 特殊图 | $\mathfrak{e}_7$ | 133 |
| $E_8$ | 特殊图 | $\mathfrak{e}_8$ | 248 |
| $F_4$ | $\circ-\circ\Rightarrow\circ-\circ$ | $\mathfrak{f}_4$ | 52 |
| $G_2$ | $\circ\Leftarrow\circ$ | $\mathfrak{g}_2$ | 14 |

**证明思路**：通过分析单根之间的夹角和长度比，列出所有可能的 Coxeter 图，然后排除那些不能对应根系统的图（通过可对称化条件和整性条件）。剩余的图正好是上述列表。$\square$

**推论**：每个有限维复半单李代数唯一地分解为单李代数的直和，其分类由 Dynkin 图完全决定。连通紧李群的分类也由相同的 Dynkin 图给出。