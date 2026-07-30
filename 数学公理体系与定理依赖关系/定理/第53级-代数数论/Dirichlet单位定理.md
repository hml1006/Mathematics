# Dirichlet 单位定理

## 一、定理介绍

Dirichlet 单位定理（Dirichlet Unit Theorem）是代数数论中关于数域整数环单位群结构的经典结果，由 Dirichlet 于 1846 年证明。该定理完全确定了数域 $K$ 的整数环 $\mathcal{O}_K$ 中可逆元（单位）群 $\mathcal{O}_K^\times$ 的抽象结构。

在 $\mathbb{Z}$ 中，单位群只有 $\{\pm 1\}$，是平凡的。但在一般的数域中，单位群可以非常丰富。例如在 $\mathbb{Z}[\sqrt{2}]$ 中，$1+\sqrt{2}$ 是单位（因为 $(1+\sqrt{2})(1-\sqrt{2}) = -1$），而且 $(1+\sqrt{2})^n$ 对任意 $n \in \mathbb{Z}$ 都是单位，因此单位群是无限的。

Dirichlet 单位定理告诉我们：$\mathcal{O}_K^\times$ 总是一个有限生成 Abel 群，其结构为
$$\mathcal{O}_K^\times \cong W_K \times \mathbb{Z}^r,$$
其中 $W_K$ 是 $K$ 中单位根的有限群，$r = r_1 + r_2 - 1$ 是**单位秩**（$r_1$ 为实嵌入数，$r_2$ 为复共轭嵌入对数）。

这一定理的证明是 Dirichlet 将鸽巢原理（或称抽屉原理）创造性地应用于数论的杰作，体现了几何直觉与代数结构的深刻统一。

## 二、原理思路

### 对数嵌入

证明的核心工具是**对数嵌入**（logarithmic embedding）。定义映射：
$$L: \mathcal{O}_K^\times \to \mathbb{R}^{r_1 + r_2}$$
$$L(\varepsilon) = (\log|\sigma_1(\varepsilon)|, \ldots, \log|\sigma_{r_1}(\varepsilon)|, 2\log|\sigma_{r_1+1}(\varepsilon)|, \ldots, 2\log|\sigma_{r_1+r_2}(\varepsilon)|).$$

由于 $\varepsilon$ 是单位，$|N_{K/\mathbb{Q}}(\varepsilon)| = 1$，即
$$\prod_{i=1}^{r_1} |\sigma_i(\varepsilon)| \cdot \prod_{j=1}^{r_2} |\sigma_{r_1+j}(\varepsilon)|^2 = 1.$$

取对数得：
$$\sum_{i=1}^{r_1} \log|\sigma_i(\varepsilon)| + \sum_{j=1}^{r_2} 2\log|\sigma_{r_1+j}(\varepsilon)| = 0.$$

因此 $L(\varepsilon)$ 落在超平面 $H: x_1 + x_2 + \cdots + x_{r_1+r_2} = 0$ 上，这是一个 $(r_1+r_2-1)$ 维的实向量空间。

### 证明思路

证明分为两步：

**第一步（核的计算）：** $L$ 的核恰好是 $K$ 中的单位根群 $W_K$。若 $L(\varepsilon) = 0$，则 $|\sigma_i(\varepsilon)| = 1$ 对所有嵌入成立。这意味着 $\varepsilon$ 的所有共轭的绝对值都为 1，从而 $\varepsilon$ 的极小多项式的根的绝对值全为 1。由 Kronecker 定理，$\varepsilon$ 必须是单位根。

**第二步（像是格）：** $L(\mathcal{O}_K^\times)$ 是 $H \cong \mathbb{R}^{r_1+r_2-1}$ 中的格（离散子群），且秩为 $r_1 + r_2 - 1$。这一步需要证明 $L(\mathcal{O}_K^\times)$ 既离散又余紧（cocompact）。离散性由 Minkowski 嵌入和几何数论得出；余紧性通过构造足够多的单位来证明，本质上用到了 Minkowski 定理在理想上的应用。

## 三、定理的严格表述

**定理（Dirichlet 单位定理）：**

设 $K$ 是 $n$ 次数域，$r_1$ 为 $K$ 的实嵌入数，$r_2$ 为 $K$ 的复共轭嵌入对数（$n = r_1 + 2r_2$）。设 $\mathcal{O}_K^\times$ 为 $\mathcal{O}_K$ 的单位群。则：

**(1) 结构定理：** $\mathcal{O}_K^\times$ 是有限生成 Abel 群，且
$$\mathcal{O}_K^\times \cong W_K \times \mathbb{Z}^r,$$
其中 $W_K$ 是 $K$ 中所有单位根构成的有限循环群，$r = r_1 + r_2 - 1$ 称为**单位秩**。

**(2) 基本单位组：** 存在 $\varepsilon_1, \varepsilon_2, \ldots, \varepsilon_r \in \mathcal{O}_K^\times$（称为**基本单位**或**基本单位系**），使得每个单位 $\varepsilon \in \mathcal{O}_K^\times$ 都可以唯一地表示为
$$\varepsilon = \zeta \cdot \varepsilon_1^{a_1} \varepsilon_2^{a_2} \cdots \varepsilon_r^{a_r},$$
其中 $\zeta \in W_K$，$a_1, a_2, \ldots, a_r \in \mathbb{Z}$。

**(3) 调节子：** 基本单位的对数嵌入 $L(\varepsilon_1), \ldots, L(\varepsilon_r)$ 构成 $H$ 中的格。去掉 $H$ 中任一个坐标后，这 $r$ 个向量构成的 $r \times r$ 矩阵的行列式的绝对值称为**调节子**（regulator）$R_K$，它是数域 $K$ 的重要不变量。

## 四、证明过程

### 第一步：$L$ 是同态且 $\ker(L) = W_K$

$L$ 显然是群同态 $\mathcal{O}_K^\times \to (\mathbb{R}^{r_1+r_2}, +)$。

设 $\varepsilon \in \ker(L)$，则对所有嵌入 $\sigma_i$，$|\sigma_i(\varepsilon)| = 1$。$\varepsilon$ 的所有 Galois 共轭的绝对值均为 1。

$\varepsilon$ 是代数整数，其极小多项式 $f(x) \in \mathbb{Z}[x]$ 的所有根（即 $\varepsilon$ 的共轭）的绝对值均为 1。对任意 $m \geq 1$，$\varepsilon^m$ 的所有共轭的绝对值也均为 1。

$\varepsilon^m$ 的极小多项式的系数由 $\varepsilon^m$ 的共轭的初等对称多项式给出，因此系数的绝对值有统一的界（只依赖于 $n = \deg f$）。由于系数是整数，只有有限种可能。因此 $\{\varepsilon^m : m \geq 1\}$ 只有有限个不同的极小多项式，从而 $\varepsilon$ 的幂中必有重复，即 $\varepsilon^a = \varepsilon^b$（$a > b$），从而 $\varepsilon^{a-b} = 1$，$\varepsilon$ 是单位根。

反之，若 $\varepsilon$ 是 $K$ 中的 $m$ 次单位根，则 $\varepsilon^m = 1$，$\sigma_i(\varepsilon)^m = 1$，$|\sigma_i(\varepsilon)| = 1$，$L(\varepsilon) = 0$。

因此 $\ker(L) = W_K$。由于 $K$ 中的单位根是 $x^m - 1$ 的根，只有有限个，$W_K$ 是有限循环群。

### 第二步：$L(\mathcal{O}_K^\times)$ 是 $H$ 中的离散子群

设 $\varepsilon \in \mathcal{O}_K^\times$，$L(\varepsilon) = (y_1, \ldots, y_{r_1+r_2})$。若 $L(\varepsilon)$ 在原点附近，即所有 $|y_i|$ 很小，则 $|\sigma_i(\varepsilon)|$ 接近 1。

$\varepsilon$ 的所有共轭的绝对值有界，从而 $\varepsilon$ 的极小多项式的系数有界（由 Newton 恒等式）。系数是整数，因此只有有限个可能的极小多项式，从而只有有限个可能的 $\varepsilon$。

这说明在 $H$ 中，$L(\mathcal{O}_K^\times)$ 的每个有界子集只包含有限个点，即 $L(\mathcal{O}_K^\times)$ 是离散的。

### 第三步：$L(\mathcal{O}_K^\times)$ 的秩为 $r_1 + r_2 - 1$

需要证明 $L(\mathcal{O}_K^\times)$ 在 $H$ 中的 $\mathbb{Z}$-秩恰好为 $r = r_1 + r_2 - 1$。

**秩 $\leq r$：** $L(\mathcal{O}_K^\times) \subset H$，$H$ 的维数为 $r$，所以离散子群的秩 $\leq r$。

**秩 $\geq r$：** 用 Minkowski 定理构造单位。考虑 Minkowski 空间中的"厚环"区域：
$$T = \{(x_1, \ldots, x_{r_1}, z_1, \ldots, z_{r_2}) : |x_i| \leq c_i, |z_j| \leq d_j\}$$
适当选择参数使 $T$ 的体积足够大，由 Minkowski 定理，$T$ 包含 $\mathcal{O}_K$ 的非零元素 $\alpha$。

通过精细的参数调节，可以证明：对 $H$ 中的任何充分大的紧集 $C$，存在单位 $\varepsilon \in \mathcal{O}_K^\times$ 使得 $L(\varepsilon) \in C$。

更具体地，对任意非零理想 $\mathfrak{a} \subset \mathcal{O}_K$，在 Minkowski 空间中考虑集合
$$S_t = \{v \in \mathbb{R}^{r_1} \times \mathbb{C}^{r_2} : |v_i| \leq t^{a_i}\}$$
其中 $a_i > 0$，$\sum a_i = 1$。当 $t$ 足够大时，$S_t$ 包含 $\mathfrak{a}$ 的非零元素 $\alpha$，且 $N(\alpha) \in \mathfrak{a}$ 的范数有界。

通过变化参数 $(a_1, \ldots, a_{r_1+r_2})$（在 $r_1+r_2-1$ 维单纯形中），可以得到 $L(\mathcal{O}_K^\times)$ 在 $r$ 个线性无关方向上都有非零分量，从而秩 $\geq r$。

综合得 $L(\mathcal{O}_K^\times)$ 的秩恰好为 $r = r_1 + r_2 - 1$。

### 第四步：结论

由 Abel 群的结构定理，$\mathcal{O}_K^\times / \ker(L) \cong L(\mathcal{O}_K^\times) \cong \mathbb{Z}^r$。因此
$$\mathcal{O}_K^\times \cong W_K \times \mathbb{Z}^r.$$
$\blacksquare$

## 五、应用与意义

### 1. 解析类数公式

Dirichlet 单位定理中的调节子 $R_K$ 出现在解析类数公式中：
$$\lim_{s \to 1} (s-1)\zeta_K(s) = \frac{2^{r_1}(2\pi)^{r_2} h_K R_K}{w_K \sqrt{|d_K|}}.$$
调节子度量了基本单位在 Minkowski 空间中的"分布密度"，是数域的重要算术不变量。

### 2. Pell 方程

当 $K = \mathbb{Q}(\sqrt{d})$（$d > 0$ 无平方因子）时，$r_1 = 2, r_2 = 0$，$r = 1$。$\mathcal{O}_K^\times \cong \{\pm 1\} \times \mathbb{Z}$。基本单位 $\varepsilon_0 > 1$ 给出了 Pell 方程 $x^2 - dy^2 = \pm 1$ 的最小正整数解，所有解由 $\varepsilon_0^n$ 给出。

### 3. 代数 K 理论

Dirichlet 单位定理可以看作代数 K 群 $K_1(\mathcal{O}_K)$ 的计算。在更一般的数论中，Borel 定理计算了数域整数环的高阶 K 群的秩，是 Dirichlet 定理的深远推广。

### 4. 单位群的计算

基本单位的计算是计算代数数论的核心任务。对二次域，基本单位可以通过连分数算法求得。对高次域，需要更复杂的算法（如 Voronoi 算法、Buchmann 的亚指数算法）。

### 5. 向 S-单位定理的推广

若允许在有限多个素理想处有极点，则得到 **S-单位群** $\mathcal{O}_{K,S}^\times$。S-单位定理断言 $\mathcal{O}_{K,S}^\times$ 是秩为 $r + |S|$ 的有限生成 Abel 群。S-单位方程 $x + y = 1$ 的有限性定理（Evertse, 1984）是 Diophantine 方程理论的基础工具。

### 6. Leopoldt 猜想

Leopoldt 猜想断言：$\mathcal{O}_K^\times$ 在 $p$-进对数嵌入下的像的 $\mathbb{Z}_p$-秩等于 $r_1 + r_2 - 1$（即不"坍缩"）。这对 Abel 扩张已被证明（Brumer），一般情形仍是开放问题。
