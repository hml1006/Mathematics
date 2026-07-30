# Runge 逼近定理

## 介绍

Runge 逼近定理（Runge's approximation theorem）是复分析中的基本逼近定理，由 Carl Runge 在 1885 年证明。该定理断言，在紧集上解析的函数可以用有理函数（甚至多项式）一致逼近，其逼近精度取决于紧集的补集在扩充复平面中的连通性。该定理是复分析中逼近理论的基础，也是函数论中许多构造性证明的工具。

## 分析

**前置依赖**：全纯函数、Laurent 展开、Cauchy 积分公式、一致收敛、紧集。

**定理内容**：设 $K \subset \mathbb{C}$ 是紧集，$f$ 在 $K$ 的某个邻域上全纯。则：
1. **有理函数逼近**：存在有理函数序列 $R_n$，其极点位于 $K$ 的补集 $\mathbb{C} \setminus K$ 中，使得 $R_n$ 在 $K$ 上一致收敛到 $f$。
2. **多项式逼近**：若 $\mathbb{C} \setminus K$ 是连通的（即 $K$ 的补集无界连通），则存在多项式序列 $p_n$ 在 $K$ 上一致收敛到 $f$。

**数学内涵**：Runge 定理揭示了全纯函数的局部性质与全局逼近之间的关系。多项式逼近要求补集连通，这排除了 $K$ 有"洞"的情形——当 $K$ 有洞时，需要有理函数（在洞中放置极点）来逼近。

**证明策略**：利用 Cauchy 积分公式将 $f$ 表示为沿 $K$ 边界的积分，然后用 Riemann 和逼近积分。将积分核 $1/(\zeta - z)$ 展开为有理函数或多项式级数，利用紧集上的一致收敛性。

## 思考过程

Runge 定理的证明思路：对 $K$ 上的全纯函数 $f$，存在 $K$ 的邻域 $\Omega$ 使得 $f$ 在 $\Omega$ 上全纯。取 $\Omega$ 中的有限多边形的并覆盖 $K$，由 Cauchy 积分公式，
$$f(z) = \frac{1}{2\pi i} \int_\Gamma \frac{f(\zeta)}{\zeta - z} \, d\zeta,\quad z \in K$$
其中 $\Gamma$ 是 $\Omega$ 中包围 $K$ 的曲线。将积分用 Riemann 和逼近，即得有理函数逼近。若 $\mathbb{C} \setminus K$ 连通，每个 $1/(\zeta - z)$ 可在 $K$ 上被多项式一致逼近（因为 $\zeta$ 在 $K$ 的外部），从而 $f$ 可被多项式逼近。

## 证明过程

**定理**（Runge 逼近定理）：设 $K \subset \mathbb{C}$ 是紧集，$f$ 在 $K$ 的邻域上全纯。

**步骤 1**：有理函数逼近。存在有理函数列 $R_n$，极点在 $\mathbb{C} \setminus K$ 中，使得 $R_n \rightrightarrows f$ 在 $K$ 上。

**步骤 2**：多项式逼近。若 $\mathbb{C} \setminus K$ 连通，则存在多项式列 $p_n$ 使得 $p_n \rightrightarrows f$ 在 $K$ 上。

**证明**：

**步骤 1**：存在 $\Omega \supset K$ 使得 $f$ 在 $\Omega$ 上全纯。取 $\Omega$ 中的有限多边形的并 $\Omega'$，使得 $K \subset \Omega' \subset \Omega$，且 $\partial\Omega'$ 由有限条线段组成。

**步骤 2**：由 Cauchy 积分公式，对 $z \in K$，
$$f(z) = \frac{1}{2\pi i} \int_{\partial\Omega'} \frac{f(\zeta)}{\zeta - z} \, d\zeta$$

**步骤 3**：将积分表示为 Riemann 和的极限。将 $\partial\Omega'$ 分为有限个小段，在每个小段上取中点 $\zeta_j$，则
$$f(z) = \lim_{n\to\infty} \frac{1}{2\pi i} \sum_j \frac{f(\zeta_j)}{\zeta_j - z} \Delta\zeta_j$$
每个项 $1/(\zeta_j - z)$ 是 $z$ 的有理函数，极点在 $\zeta_j \in \mathbb{C} \setminus K$ 中。故 $f$ 可被有理函数一致逼近。

**步骤 4**：若 $\mathbb{C} \setminus K$ 连通，则对每个 $\zeta_j$，函数 $1/(\zeta_j - z)$ 可在 $K$ 上被多项式一致逼近。这是因为 $\zeta_j$ 属于 $\mathbb{C} \setminus K$ 的同一个连通分支（无界分支），存在从 $\zeta_j$ 到 $\infty$ 的路径，将 $1/(\zeta_j - z)$ 展开为关于 $1/(\zeta_j - z)$ 的幂级数。

**步骤 5**：具体地，对 $\zeta_j$ 远离 $K$ 时，$1/(\zeta_j - z) = \frac{1}{\zeta_j} \sum_{n=0}^\infty (z/\zeta_j)^n$ 是多项式的一致收敛级数。对 $\zeta_j$ 在 $K$ 附近但不在 $K$ 中，可通过路径移动将极点移至无穷远。$\square$

**推论**：若 $K$ 是紧集且 $\mathbb{C} \setminus K$ 连通，则 $K$ 上全纯的函数可被多项式一致逼近。特别地，对任意圆盘 $D$ 上的全纯函数，可在 $D$ 的紧子集上被多项式一致逼近。