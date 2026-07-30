# Riemann–Roch 定理

## 介绍

Riemann–Roch 定理是 Riemann 面和代数曲线理论中最深刻的定理之一，由 Bernhard Riemann（1857）和他的学生 Gustav Roch（1865）建立。该定理给出了 Riemann 面上具有指定零点和极点的亚纯函数空间维数的计算公式。它统一了 Riemann 面理论中的许多经典结果，是代数几何、复分析和数论交叉领域的基石，其推广（如 Hirzebruch–Riemann–Roch 定理、Grothendieck–Riemann–Roch 定理）在现代数学中影响深远。

## 分析

**前置依赖**：Riemann 面、除子、线丛、亚纯函数、亏格、层上同调、典范除子。

**定理内容**：设 $X$ 是紧 Riemann 面，亏格为 $g$，$D$ 是 $X$ 上的除子。则
$$\ell(D) - i(D) = \deg D - g + 1$$
其中：
- $\ell(D) = \dim H^0(X, \mathcal{O}(D))$，即具有除子 $D$ 所允许的零点和极点的亚纯函数空间的维数。
- $i(D) = \ell(K - D)$，其中 $K$ 是典范除子（即 $X$ 上全纯 1-形式的除子）。
- $\deg D$ 是除子 $D$ 的次数。

**等价形式**：$\ell(D) - \ell(K - D) = \deg D - g + 1$。

**数学内涵**：Riemann–Roch 定理给出了 Riemann 面上亚纯函数存在性的精确计数。$\ell(D)$ 是拟找的亚纯函数空间的维数，$i(D)$ 是校正项。当 $\deg D > 2g - 2$ 时，$i(D) = 0$，公式简化为 $\ell(D) = \deg D - g + 1$。

**证明策略**：经典证明利用 Riemann 面的三角剖分和调和函数理论。现代证明使用层上同调理论，将 $\ell(D)$ 和 $i(D)$ 解释为线丛 $\mathcal{O}(D)$ 的上同调维数，然后利用 Serre 对偶和 Euler 示性数的 Riemann–Roch 公式。

## 思考过程

Riemann–Roch 定理的核心思想是：求具有指定零点和极点的亚纯函数等价于求线丛 $\mathcal{O}(D)$ 的全局截面。对于 Riemann 球面 $\mathbb{P}^1$（$g=0$），公式简化为 $\ell(D) = \deg D + 1$（当 $\deg D \ge 0$），这对应于有理函数空间中 Lagrange 插值定理。

对于一般 Riemann 面，亏格 $g$ 的出现反映了拓扑复杂性对亚纯函数存在性的限制。当 $D$ 的次数很大时，$\ell(D) \approx \deg D - g + 1$，即每增加一个极点（增加 $\deg D$），就多一个自由参数。

## 证明过程

**定理**（Riemann–Roch）：设 $X$ 是亏格为 $g$ 的紧 Riemann 面，$D$ 是除子，则
$$\ell(D) - \ell(K - D) = \deg D - g + 1$$

**证明**（层上同调方法）：

**步骤 1**：线丛 $\mathcal{O}(D)$ 的 Euler 示性数定义为
$$\chi(\mathcal{O}(D)) = \dim H^0(X, \mathcal{O}(D)) - \dim H^1(X, \mathcal{O}(D))$$

**步骤 2**：由 Serre 对偶定理，$H^1(X, \mathcal{O}(D)) \cong H^0(X, \Omega^1 \otimes \mathcal{O}(-D))^* = H^0(X, \mathcal{O}(K - D))^*$，故
$$\dim H^1(X, \mathcal{O}(D)) = \ell(K - D)$$

**步骤 3**：Riemann–Roch 公式等价于 $\chi(\mathcal{O}(D)) = \deg D - g + 1$。由于 $\chi$ 是 $\mathcal{O}(D)$ 的拓扑不变量，只需对 $D = 0$ 和 $D = [p]$ 验证。

**步骤 4**：$D = 0$ 时，$\mathcal{O}(0) = \mathcal{O}_X$ 是结构层，$H^0(X, \mathcal{O}) = \mathbb{C}$（紧 Riemann 面上的全局全纯函数只有常数），故 $\ell(0) = 1$。由 Serre 对偶，$\ell(K) = g$。代入公式：
$$1 - g = 0 - g + 1$$
成立。

**步骤 5**：$D = [p]$ 时（一个点），$\deg D = 1$。利用除子加法的可加性，$\chi(\mathcal{O}(D)) = \chi(\mathcal{O}) + 1 = 1 - g + 1 = 2 - g$，代入公式成立。

**步骤 6**：由 $\chi$ 在短正合列下的可加性，上述公式对所有除子成立。$\square$

**推论**：
1. 典范除子 $K$ 的次数为 $\deg K = 2g - 2$。
2. 若 $\deg D > 2g - 2$，则 $\ell(K - D) = 0$，故 $\ell(D) = \deg D - g + 1$。
3. 若 $\deg D < 0$，则 $\ell(D) = 0$。