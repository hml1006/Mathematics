# Dedekind ζ 函数

> **一句话大白话**：Riemann ζ 函数只管整数一个世界；Dedekind ζ 函数把它推广到"数域"这个大数字王国，把所有理想的"倒数幂和"加起来，从而度量这个世界里素理想的分布规律。
>
> **小例子**：对高斯整数域 $\mathbb{Q}(i)$，$\zeta_{\mathbb{Q}(i)}(s)=\zeta(s)\,L(s,\chi_{-4})$；它在 $s=1$ 的留数由类数公式给出，描述了 $\mathbb{Z}[i]$ 中素理想的分母规律。

## 一、定理介绍

Dedekind $\zeta$ 函数是 Riemann $\zeta$ 函数在数域上的自然推广，由 Dedekind 在 1870 年代引入。对数域 $K$，Dedekind $\zeta$ 函数 $\zeta_K(s)$ 编码了 $K$ 的整数环 $\mathcal{O}_K$ 中理想分布的全部信息，是研究数域算术性质的最强大的解析工具。

当 $K = \mathbb{Q}$ 时，$\zeta_K(s)$ 退化为经典的 Riemann $\zeta$ 函数 $\zeta(s) = \sum_{n=1}^\infty n^{-s}$。对一般的数域 $K$，$\zeta_K(s)$ 将 $\mathbb{Q}$ 上素数的分布信息替换为 $K$ 上素理想的分布信息。

Dedekind $\zeta$ 函数最重要的性质包括：
1. **解析延拓：** $\zeta_K(s)$ 可以解析延拓到整个复平面，仅在 $s = 1$ 处有一个单极点。
2. **函数方程：** $\zeta_K(s)$ 满足一个优美的函数方程，将 $s$ 与 $1-s$ 联系起来。
3. **解析类数公式：** $\zeta_K(s)$ 在 $s = 1$ 处的留数精确地给出了 $K$ 的类数 $h_K$、调节子 $R_K$ 等基本算术不变量。

这些结果将数域的算术性质（代数信息）与解析函数的性质（解析信息）深刻地联系在一起，是解析数论和代数数论交叉的核心。

## 二、原理思路

### 从 Riemann ζ 函数到 Dedekind ζ 函数

Riemann $\zeta$ 函数 $\zeta(s) = \sum_{n=1}^\infty n^{-s}$ 有两个基本的表示：

**Dirichlet 级数：** $\zeta(s) = \sum_{n=1}^\infty n^{-s}$（$\text{Re}(s) > 1$）。

**Euler 乘积：** $\zeta(s) = \prod_p (1 - p^{-s})^{-1}$（$\text{Re}(s) > 1$），积取遍所有素数。

Euler 乘积反映了 $\mathbb{Z}$ 中整数的唯一分解定理。

对数域 $K$，$\mathcal{O}_K$ 中理想（而非元素）有唯一分解。因此 Dedekind $\zeta$ 函数用**理想**替代**整数**：

$$\zeta_K(s) = \sum_{\mathfrak{a}} N(\mathfrak{a})^{-s} = \prod_{\mathfrak{p}} (1 - N(\mathfrak{p})^{-s})^{-1},$$

其中第一个和取遍 $\mathcal{O}_K$ 的所有非零理想，第二个积取遍所有非零素理想，$N(\mathfrak{a}) = |\mathcal{O}_K/\mathfrak{a}|$ 是理想范数。

### 解析延拓的方法

解析延拓的核心思想是将离散的和（Dirichlet 级数）与连续的积分联系起来。

**对 $K = \mathbb{Q}$：** Riemann 利用 $\Gamma$ 函数和 Poisson 求和公式（或 theta 函数的变换公式）得到了 $\zeta(s)$ 的解析延拓和函数方程。

**对一般 $K$：** 需要更复杂的工具。Hecke 引入了**Hecke theta 函数**和**Poission 求和公式在 adele 上的推广**，得到了 $\zeta_K(s)$ 的解析延拓和函数方程。Tate 的论文（1950）用 adele 和 idele 的语言给出了最优雅的处理。

### 函数方程

定义**完备化 Dedekind $\zeta$ 函数**：
$$\xi_K(s) = |d_K|^{s/2} \Gamma_{\mathbb{R}}(s)^{r_1} \Gamma_{\mathbb{C}}(s)^{r_2} \zeta_K(s),$$

其中 $\Gamma_{\mathbb{R}}(s) = \pi^{-s/2} \Gamma(s/2)$，$\Gamma_{\mathbb{C}}(s) = 2(2\pi)^{-s} \Gamma(s)$，$d_K$ 是 $K$ 的判别式，$r_1, r_2$ 是实、复嵌入数。

则 $\xi_K(s)$ 满足函数方程：
$$\xi_K(s) = \xi_K(1-s).$$

## 三、定理的严格表述

**定理（Dedekind ζ 函数的基本性质）：**

设 $K$ 是 $n$ 次数域，$r_1$ 个实嵌入，$r_2$ 对复共轭嵌入（$n = r_1 + 2r_2$），$d_K$ 为判别式。

**(1) 收敛与 Euler 乘积：** 对 $\text{Re}(s) > 1$，
$$\zeta_K(s) = \sum_{\mathfrak{a} \neq 0} N(\mathfrak{a})^{-s} = \prod_{\mathfrak{p}} (1 - N(\mathfrak{p})^{-s})^{-1}$$
绝对收敛。

**(2) 解析延拓：** $\zeta_K(s)$ 可以解析延拓到整个复平面 $\mathbb{C}$，仅在 $s = 1$ 处有一个单极点，留数为
$$\text{Res}_{s=1} \zeta_K(s) = \frac{2^{r_1}(2\pi)^{r_2} h_K R_K}{w_K \sqrt{|d_K|}},$$
其中 $h_K$ 为类数，$R_K$ 为调节子，$w_K$ 为单位根个数。

**(3) 函数方程：** 定义 $\Gamma_{\mathbb{R}}(s) = \pi^{-s/2}\Gamma(s/2)$，$\Gamma_{\mathbb{C}}(s) = 2(2\pi)^{-s}\Gamma(s)$。则完备化 $\zeta$ 函数
$$\Lambda_K(s) = |d_K|^{s/2} \Gamma_{\mathbb{R}}(s)^{r_1} \Gamma_{\mathbb{C}}(s)^{r_2} \zeta_K(s)$$
满足函数方程
$$\Lambda_K(s) = \Lambda_K(1-s).$$

**(4) 零点分布：** $\zeta_K(s)$ 的零点包括：
- **平凡零点：** 由 $\Gamma$ 因子在 $s = 0, -1, -2, \ldots$ 处的极点引起的零点。
- **非平凡零点：** 位于临界带 $0 < \text{Re}(s) < 1$ 中。由函数方程，非平凡零点关于 $\text{Re}(s) = 1/2$ 对称。

**(5) 广义 Riemann 猜想（GRH）：** $\zeta_K(s)$ 的所有非平凡零点都在临界线 $\text{Re}(s) = 1/2$ 上。

## 四、证明过程

### 第一步：Dirichlet 级数与 Euler 乘积

由理想唯一分解定理，$\mathcal{O}_K$ 的每个非零理想唯一地写成素理想之积。因此
$$\sum_{\mathfrak{a}} N(\mathfrak{a})^{-s} = \prod_{\mathfrak{p}} \left(\sum_{k=0}^\infty N(\mathfrak{p})^{-ks}\right) = \prod_{\mathfrak{p}} (1 - N(\mathfrak{p})^{-s})^{-1}.$$

对 $\text{Re}(s) > 1$，$N(\mathfrak{p}) \geq 2$，级数绝对收敛。

### 第二步：解析延拓（Hecke 的方法）

利用 Minkowski 嵌入将 $\mathcal{O}_K$ 的理想映为 $\mathbb{R}^n$ 中的格。对每个理想类 $C \in \text{Cl}(K)$，定义部分 $\zeta$ 函数：
$$\zeta_K(s, C) = \sum_{\mathfrak{a} \in C} N(\mathfrak{a})^{-s}.$$

则 $\zeta_K(s) = \sum_{C \in \text{Cl}(K)} \zeta_K(s, C)$。

对固定的理想类 $C$，取 $\mathfrak{b} \in C^{-1}$，则 $\mathfrak{a} \in C \iff \mathfrak{a}\mathfrak{b}$ 是主理想。写 $\mathfrak{a}\mathfrak{b} = (\alpha)$，$\alpha \in \mathfrak{b}^{-1}$。

$$\zeta_K(s, C) = N(\mathfrak{b})^s \sum_{\alpha \in \mathfrak{b}^{-1}/\mathcal{O}_K^\times} |N_{K/\mathbb{Q}}(\alpha)|^{-s}.$$

利用 Minkowski 嵌入，将和式转化为格上的求和。定义 theta 函数：
$$\theta_C(t) = \sum_{\alpha \in \mathfrak{b}^{-1}} e^{-t \sum_{i} |\sigma_i(\alpha)|^2},$$

利用 Poisson 求和公式得到 $\theta_C(t)$ 的变换公式：$\theta_C(1/t) = c \cdot t^{n/2} \cdot \theta_{C'}(t)$。

由此通过 Mellin 变换得到 $\zeta_K(s, C)$ 的解析延拓和函数方程。

### 第三步：解析类数公式

$\zeta_K(s)$ 在 $s = 1$ 处的留数可以通过计算 $\zeta_K(s, C)$ 在 $s = 1$ 处的留数得到。

利用格点计数的渐近公式（Minkowski 区域的体积），
$$\#\{\alpha \in \mathfrak{b}^{-1} : |N_{K/\mathbb{Q}}(\alpha)| \leq X\} \sim \frac{2^{r_1}(2\pi)^{r_2}}{w_K \sqrt{|d_K|}} R_K \cdot X.$$

由此得到
$$\text{Res}_{s=1} \zeta_K(s) = \frac{2^{r_1}(2\pi)^{r_2} h_K R_K}{w_K \sqrt{|d_K|}}.$$

### 第四步：函数方程

由 theta 函数的变换公式和 Mellin 变换的性质，得到完备化 $\zeta$ 函数 $\Lambda_K(s)$ 满足 $\Lambda_K(s) = \Lambda_K(1-s)$。$\blacksquare$

## 五、应用与意义

### 1. 解析类数公式

解析类数公式将 $\zeta_K(s)$ 在 $s=1$ 处的留数与 $h_K, R_K, w_K, d_K$ 联系起来，是计算类数的基本工具。特别地：
$$h_K = \frac{w_K \sqrt{|d_K|}}{2^{r_1}(2\pi)^{r_2} R_K} \text{Res}_{s=1} \zeta_K(s).$$

### 2. 素理想分布

$\zeta_K(s)$ 的零点分布控制了 $K$ 中素理想的分布。**素理想定理**（数域上的素数定理）断言：
$$\pi_K(x) = \#\{\mathfrak{p} : N(\mathfrak{p}) \leq x\} \sim \frac{x}{\log x},$$
其证明依赖于 $\zeta_K(s)$ 在 $\text{Re}(s) = 1$ 上无零点（与 Riemann 素数定理的证明类似）。

在 GRH 下，误差项可以改进为 $O(x^{1/2} \log x)$。

### 3. Artin L-函数

对 Galois 扩张 $L/K$ 和 $\text{Gal}(L/K)$ 的表示 $\rho$，**Artin L-函数** $L(s, \rho, L/K)$ 是 Dedekind $\zeta$ 函数的推广。当 $\rho$ 是平凡表示时，$L(s, \rho) = \zeta_K(s)$。

Artin 猜想断言：对不可约表示 $\rho \neq 1$，$L(s, \rho)$ 在整个复平面上解析。这是 Langlands 纲领的核心猜想之一。

### 4. 特殊值与算术

$\zeta_K(s)$ 在非正整数处的特殊值包含深刻的算术信息：
- **Siegel-Klingen 公式：** $\zeta_K(-n)$ 与 $K$ 的代数 K-群有关。
- **Lichtenbaum 猜想：** $\zeta_K(s)$ 的特殊值与 étale 上同调群的大小有关。
- **BSD 猜想（椭圆曲线）：** 椭圆曲线的 $L$-函数在 $s=1$ 处的行为与有理点群的秩有关，是 Dedekind $\zeta$ 函数理论的深远推广。

### 5. 谱解释

Dedekind $\zeta$ 函数的非平凡零点有**谱解释**：它们是某个（假设存在的）自伴算子的特征值。这一观点由 Hilbert-Pólya 猜想提出，在随机矩阵理论（Montgomery-Odlyzko 猜想、Keating-Snaith 猜想）中得到支持。

### 6. Tate 论文与 adele 方法

Tate (1950) 的博士论文用 adele 和 idele 的语言重新证明了 Dedekind $\zeta$ 函数的解析延拓和函数方程。这一方法：
- 将 Poisson 求和公式推广到 adele 环上的 Schwartz-Bruhat 函数。
- 用 idele 上的积分表示 $\zeta_K(s)$。
- 为全局类域论提供了最自然的解析框架。

Tate 的方法已成为现代数论的标准工具，被广泛应用于自守形式、Langlands 纲领等领域。
