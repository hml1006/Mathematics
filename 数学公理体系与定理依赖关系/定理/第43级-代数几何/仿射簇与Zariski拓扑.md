# 仿射簇与Zariski拓扑

## 介绍

仿射簇是代数几何中最基本的几何对象，定义为仿射空间 $\mathbb{A}^n_k$ 中多项式方程组零点的集合。Zariski拓扑是仿射簇上的一种拓扑结构，其闭集由代数集定义。这一框架将代数问题转化为几何语言，是代数几何的基石。通过对仿射簇的研究，我们可以利用交换代数工具（如理想、环、模）来研究几何对象的结构。

## 分析

**前置依赖**：多项式环、理想、仿射空间、拓扑空间基本概念。

**定理内容**：
- 仿射空间 $\mathbb{A}^n_k$ 上的 Zariski 拓扑定义为：闭集为所有形如 $V(S) = \{x \in \mathbb{A}^n_k \mid \forall f \in S, f(x) = 0\}$ 的代数集，其中 $S \subseteq k[x_1, \ldots, x_n]$。
- 对任意理想 $I \subseteq k[x_1, \ldots, x_n]$，$V(I)$ 是代数集。
- 反之，对任意代数集 $X$，定义其理想 $I(X) = \{f \in k[x_1, \ldots, x_n] \mid f(x) = 0, \forall x \in X\}$。
- Hilbert 零点定理（Nullstellensatz）建立了代数集与理想之间的对应关系。

**数学内涵**：
- Zariski 拓扑比通常的欧几里得拓扑更粗糙（开集更大），但它具有深刻的代数意义。
- 不可约代数集对应素理想，仿射簇通常定义为不可约代数集。
- 仿射簇的坐标环 $k[X] = k[x_1, \ldots, x_n]/I(X)$ 是整环，其分式域是函数域。

**证明策略**：
1. 验证 Zariski 拓扑满足拓扑公理：空集和全空间闭，有限并闭，任意交闭。
2. 建立 $V$ 和 $I$ 之间的 Galois 联络。
3. 利用 Hilbert 基定理证明 $k[x_1, \ldots, x_n]$ 是 Noetherian 环，从而每个代数集可由有限个多项式定义。

## 思考过程

Zariski 拓扑的核心思想在于将代数结构转化为拓扑结构。与通常的拓扑不同，Zariski 拓扑的非平凡开集非常"大"——例如 $\mathbb{A}^1_k$ 的 Zariski 开集是去掉有限个点的补集，这反映了多项式函数零点的代数性质。

这一拓扑结构虽然看起来简单，但它是代数几何中所有几何构造的基础。我们将在其上定义层、态射等概念，最终建立起代数几何的完整理论体系。Zariski 拓扑的另一个重要性质是拟紧性：每个开覆盖都有有限子覆盖，尽管它通常不是 Hausdorff 空间。

## 证明过程

**定理 1**：$\mathbb{A}^n_k$ 上的 Zariski 拓扑满足拓扑公理。

**证明**：

1. $\emptyset = V(1)$，$\mathbb{A}^n_k = V(0)$，故两者都是闭集。

2. 设 $\{V(I_\alpha)\}_{\alpha \in A}$ 是一族代数集，则
   $$\bigcap_{\alpha \in A} V(I_\alpha) = V\left(\sum_{\alpha \in A} I_\alpha\right)$$
   因为 $x$ 属于所有 $V(I_\alpha)$ 当且仅当对所有 $f \in I_\alpha$ 有 $f(x)=0$，即对所有 $\sum f_\alpha$（$f_\alpha \in I_\alpha$）有 $(\sum f_\alpha)(x)=0$。

3. 设 $V(I)$ 和 $V(J)$ 是两个代数集，则
   $$V(I) \cup V(J) = V(IJ) = V(I \cap J)$$
   因为 $x \in V(I) \cup V(J)$ 当且仅当对任意 $f \in I$ 有 $f(x)=0$ 或对任意 $g \in J$ 有 $g(x)=0$，这等价于对任意 $h \in IJ$ 有 $h(x)=0$。$\square$

**定理 2**（Hilbert 零点定理）：设 $k$ 是代数闭域，$I \subseteq k[x_1, \ldots, x_n]$ 是理想，则 $I(V(I)) = \sqrt{I}$，其中 $\sqrt{I} = \{f \mid f^m \in I \text{ 对某 } m\}$ 是 $I$ 的根。

**推论**：
- $V$ 和 $I$ 在不可约代数集与素理想之间建立了双射。
- 仿射簇 $\mathbb{A}^n_k$ 的闭子集与其坐标环的根理想一一对应。$\square$