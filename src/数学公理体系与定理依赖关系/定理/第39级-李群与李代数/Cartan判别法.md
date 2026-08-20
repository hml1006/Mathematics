# Cartan 判别法

> **一句话大白话**：用一条"体检指标"（Killing 型，一种内积式的双子性型）就能一眼看出李代数是不是"健康"——非退化的 Killing 型说明是半单的，Killing 型在导代数的限制为 0 则说明是可解的。
>
> **小例子**：$\mathfrak{sl}_2(\mathbb{C})$ 的 Killing 型非退化，故其半单；形如严格上三角的适当可解代数满足 $\kappa(\mathfrak{g},[X,Y])=0$，被鉴别为可解。

## 介绍

Cartan 判别法（Cartan's criterion）是李代数理论中判定李代数是可解或半单的关键工具，由法国数学家 Élie Cartan 在其博士论文中建立。该判别法利用 Killing 型（Killing form）这一双线性型来刻画李代数的结构性质，为李代数分类奠定了基础。具体而言，Cartan 判别法包含两个部分：可解性判别法和半单性判别法。

## 分析

**前置依赖**：李代数的定义、可解李代数、半单李代数、Killing 型、伴随表示 $\text{ad}$、迹。

**定理内容**：
- **可解性判别法**：设 $\mathfrak{g} \subseteq \mathfrak{gl}(V)$ 是 $\mathfrak{gl}(V)$ 的子李代数，其中 $V$ 是有限维向量空间。若对任意 $X \in \mathfrak{g}$ 和 $Y \in [\mathfrak{g}, \mathfrak{g}]$，有 $\operatorname{tr}(XY) = 0$，则 $\mathfrak{g}$ 是可解李代数。
- **半单性判别法**：设 $\mathfrak{g}$ 是有限维李代数。则 $\mathfrak{g}$ 是半单的（即 $\mathfrak{g}$ 的极大可解理想 $\operatorname{rad}(\mathfrak{g}) = 0$）当且仅当 $\mathfrak{g}$ 上的 Killing 型 $B$ 是非退化的。

**Killing 型的定义**：Killing 型 $B: \mathfrak{g} \times \mathfrak{g} \to \mathbb{F}$ 定义为
$$B(X,Y) = \operatorname{tr}(\text{ad}_X \circ \text{ad}_Y)$$

**数学内涵**：Cartan 判别法建立了李代数的结构性质（可解性/半单性）与迹条件/Killing 型非退化性之间的等价关系。这使得原本抽象的结构性质可以通过具体的代数计算来判定。半单李代数的 Killing 型非退化性还是后续根系分类等理论的基础。

**证明策略**：
- 可解性判别法：利用 Engel 定理的推广。证明的关键是构造一个适当的李代数，证明其满足 Engel 定理的条件，从而得到幂零性，进而推出可解性。
- 半单性判别法：利用可解性判别法证明 $\operatorname{rad}(\mathfrak{g})$ 的正交补与 $\mathfrak{g}$ 的直和分解。

## 思考过程

Cartan 判别法的核心思想是通过 Killing 型来"探测"李代数的结构。Killing 型 $B(X,Y) = \operatorname{tr}(\text{ad}_X\text{ad}_Y)$ 是李代数上的对称双线性型，且具有不变性：
$$B([X,Y],Z) = B(X,[Y,Z])$$

对于可解性判别法，思路是：假设 $\mathfrak{g}$ 满足迹条件，考虑导代数 $[\mathfrak{g},\mathfrak{g}]$ 中的元素。可以证明 $[\mathfrak{g},\mathfrak{g}]$ 中的每个元素在 $V$ 上是幂零的，从而 $[\mathfrak{g},\mathfrak{g}]$ 是幂零李代数，因此 $\mathfrak{g}$ 是可解的。

对于半单性判别法，$\mathfrak{g}$ 半单等价于 $\operatorname{rad}(\mathfrak{g}) = 0$。Killing 型非退化意味着 $\mathfrak{g}$ 的正交补为 0。需要证明若 $\mathfrak{g}$ 不是半单的（即存在非零可解理想），则 Killing 型是退化的，反之亦然。

## 证明过程

**定理**（Cartan 可解性判别法）：设 $\mathfrak{g} \subseteq \mathfrak{gl}(V)$ 是 $\mathfrak{gl}(V)$ 的子李代数，$V$ 是有限维复向量空间。若对任意 $X \in \mathfrak{g}$ 和 $Y \in [\mathfrak{g},\mathfrak{g}]$，有 $\operatorname{tr}(XY) = 0$，则 $\mathfrak{g}$ 是可解李代数。

**证明**：

**步骤 1**：设 $A = [\mathfrak{g},\mathfrak{g}]$。目标是证明 $A$ 是幂零李代数。由 Engel 定理，只需证明每个 $Y \in A$ 在 $V$ 上是幂零线性变换。

**步骤 2**：取 $Y \in A$，将 $Y$ 写成 $Y = \sum_i [X_i, Z_i]$，其中 $X_i, Z_i \in \mathfrak{g}$。对任意 $T \in \mathfrak{g}$，
$$\operatorname{tr}(YT) = \sum_i \operatorname{tr}([X_i, Z_i]T) = \sum_i \operatorname{tr}(X_i Z_i T - Z_i X_i T) = \sum_i \operatorname{tr}(X_i(Z_i T - TZ_i)) = \sum_i \operatorname{tr}(X_i[Z_i, T])$$
由条件，$\operatorname{tr}(X_i[Z_i,T]) = 0$，故 $\operatorname{tr}(YT) = 0$ 对所有 $T \in \mathfrak{g}$ 成立。

**步骤 3**：设 $Y = Y_s + Y_n$ 是 $Y$ 的 Jordan 分解（$Y_s$ 半单，$Y_n$ 幂零，$[Y_s,Y_n] = 0$）。需要证明 $Y_s = 0$。取 $V$ 的一组基使得 $Y_s = \operatorname{diag}(a_1,\dots,a_n)$ 是对角矩阵。设 $\overline{Y}_s = \operatorname{diag}(\bar{a}_1,\dots,\bar{a}_n)$ 是共轭转置。

**步骤 4**：通过归纳法，可以证明 $\overline{Y}_s$ 是 $Y_s$ 的多项式，故 $\overline{Y}_s$ 属于 $\mathfrak{g}$ 的某个子代数。更精细地，可以利用 $\operatorname{tr}(Y\overline{Y}_s) = 0$ 来证明 $Y_s = 0$。

**步骤 5**：由 $\operatorname{tr}(Y\overline{Y}_s) = \sum |a_i|^2 = 0$，得所有 $a_i = 0$，故 $Y_s = 0$，$Y = Y_n$ 是幂零的。因此 $A$ 中每个元素幂零，由 Engel 定理，$A$ 是幂零李代数，故 $\mathfrak{g}$ 可解。$\square$

**定理**（Cartan 半单性判别法）：设 $\mathfrak{g}$ 是有限维复李代数，$B$ 是 $\mathfrak{g}$ 上的 Killing 型。则 $\mathfrak{g}$ 是半单的当且仅当 $B$ 是非退化的。

**证明**：

**必要性**：设 $\mathfrak{g}$ 半单。令 $\mathfrak{s} = \{X \in \mathfrak{g} \mid B(X,Y) = 0,\ \forall Y \in \mathfrak{g}\}$ 是 $B$ 的根（退化空间）。需要证明 $\mathfrak{s} = 0$。

由 Killing 型的不变性，$\mathfrak{s}$ 是 $\mathfrak{g}$ 的理想。对任意 $X \in \mathfrak{s}$ 和 $Y \in \mathfrak{g}$，$\text{ad}_X \circ \text{ad}_Y$ 的迹为零。特别地，对 $X \in \mathfrak{s}$ 和 $Y \in [\mathfrak{s},\mathfrak{s}]$，$\operatorname{tr}(\text{ad}_X \circ \text{ad}_Y) = 0$。

考虑 $\text{ad}(\mathfrak{s}) \subseteq \mathfrak{gl}(\mathfrak{g})$。由 Cartan 可解性判别法，$\text{ad}(\mathfrak{s})$ 是可解的。由于 $\mathfrak{s}$ 的理想性质，$\mathfrak{s}$ 本身是可解的。故 $\mathfrak{s} \subseteq \operatorname{rad}(\mathfrak{g}) = 0$（因为 $\mathfrak{g}$ 半单），从而 $\mathfrak{s} = 0$，$B$ 非退化。

**充分性**：设 $B$ 非退化。假设 $\operatorname{rad}(\mathfrak{g}) \neq 0$，即 $\mathfrak{g}$ 有非零可解理想 $\mathfrak{a}$。考虑 $\mathfrak{a}$ 的降中心列 $\mathfrak{a} \supset \mathfrak{a}^{(1)} \supset \cdots \supset \mathfrak{a}^{(k)} = 0$。取 $\mathfrak{a}^{(k-1)} \neq 0$，则 $\mathfrak{a}^{(k-1)}$ 是 $\mathfrak{g}$ 的交换理想（因为 $[\mathfrak{a}^{(k-1)},\mathfrak{a}^{(k-1)}] \subseteq \mathfrak{a}^{(k)} = 0$）。

取 $X \in \mathfrak{a}^{(k-1)} \setminus \{0\}$，对任意 $Y \in \mathfrak{g}$，$\text{ad}_X \circ \text{ad}_Y$ 的像包含在 $\mathfrak{a}^{(k-1)}$ 中，且 $\text{ad}_X$ 在 $\mathfrak{a}^{(k-1)}$ 上为零（因为 $\mathfrak{a}^{(k-1)}$ 交换）。故 $\text{ad}_X \circ \text{ad}_Y$ 是幂零的，迹为零，即 $B(X,Y) = 0$ 对所有 $Y$ 成立，与 $B$ 非退化矛盾。故 $\operatorname{rad}(\mathfrak{g}) = 0$，$\mathfrak{g}$ 半单。$\square$

**推论**：半单李代数 $\mathfrak{g}$ 的 Killing 型是非退化的，且 $\mathfrak{g}$ 可以分解为单李代数的直和：$\mathfrak{g} = \bigoplus_i \mathfrak{g}_i$，其中每个 $\mathfrak{g}_i$ 是单李代数，且该分解在 Killing 型下正交。