# Shannon-McMillan-Breiman定理

> **一句话大白话**：随机生成的"长字符串"几乎所有样本长得几乎一样——每个典型序列的概率都接近 $e^{-n h}$，其中 $h$ 是熵（单位符号的复杂度），"典型集"的数目就约等于 $e^{n h}$。
>
> **小例子**：独立公平硬币（熵 $h=\ln 2$）的 $n$ 长序列，几乎所有结果概率都落在 $\approx e^{-n\ln 2}$ 附近，典型序列约有 $2^n$ 个。

## 介绍

Shannon-McMillan-Breiman定理（简称SMB定理）是信息论与遍历理论交叉领域的重要结果，由Claude Shannon（1948）、Brockway McMillan（1953）和Leo Breiman（1957）逐步完善。该定理描述了遍历信源中，长度为 $n$ 的符号序列的"典型集"的渐近大小，断言：对于平稳遍历过程，每符号的经验熵几乎处处收敛到过程的熵率。这一定理是信息论中"典型序列"概念的理论基础，在数据压缩、编码理论和统计力学中有着广泛的应用。

## 分析

**前置依赖**：测度论、概率论、信息论基础、熵、平稳过程、遍历理论、Birkhoff遍历定理、Kolmogorov-Sinai熵。

**定理内容**：设 $\{X_n\}_{n=1}^\infty$ 是取值于有限字母表 $A$ 上的平稳遍历随机过程，$H$ 是该过程的熵率。则对 $\mu$-几乎处处样本轨道 $\omega$，有
$$\lim_{n \to \infty} -\frac{1}{n} \log \mu(X_1^n = x_1^n(\omega)) = H$$
其中 $X_1^n = (X_1, \ldots, X_n)$，$x_1^n(\omega)$ 是 $\omega$ 的前 $n$ 个符号，$\mu$ 是过程的分布。收敛在 $L^1$ 意义下也成立。

**数学内涵**：
- 熵率 $H = \lim_{n \to \infty} \frac{1}{n} H(X_1^n)$，其中 $H(X_1^n)$ 是联合熵。
- 定理说明：对几乎所有的样本轨道，观测到该轨道前 $n$ 个符号的概率以指数速率 $e^{-nH}$ 衰减。
- 由此可导出"典型集"的概念：大小为约 $e^{nH}$ 的集合包含了几乎所有的概率质量。
- 这是无损压缩的"不可能低于熵率"的理论基础（Shannon信源编码定理）。

**证明策略**：
1. 将过程的熵率与Kolmogorov-Sinai熵联系起来，利用平移不变测度的性质。
2. 将 $-\log \mu(X_1^n)$ 视为 $n$ 个可测函数的和，并验证其满足次可加性。
3. 利用Kingman次可加遍历定理（或Birkhoff定理的变体）证明几乎处处收敛。

## 思考过程

SMB定理的深刻之处在于它将信息论中的熵与动力系统中的遍历理论联系起来。关键观察是：$-\log \mu(X_1^n)$ 可以写为
$$-\log \mu(X_1^n) = \sum_{k=0}^{n-1} -\log \mu(X_{k+1} \mid X_1^k)$$
其中 $\mu(X_{k+1} \mid X_1^k)$ 是条件概率。当过程是平稳的时，这些条件概率的负对数构成一个次可加过程，由Kingman定理即得收敛性。

从数据压缩的角度看，SMB定理意味着：任何无损压缩方案的平均码长都不能低于熵率，而存在一种方案（如算术编码）可以任意接近该下界。

## 证明过程

**定理**（Shannon-McMillan-Breiman）：设 $\mu$ 是有限字母表 $A$ 上的平稳遍历概率测度，$H$ 是 $\mu$ 的熵率。则对 $\mu$-几乎处处 $\omega$，
$$\lim_{n \to \infty} -\frac{1}{n} \log \mu(\omega_1^n) = H$$

**证明**：

### 1. 熵率的存在性

对平稳过程，联合熵 $H(X_1^n)$ 满足次可加性：
$$H(X_1^{m+n}) \leq H(X_1^m) + H(X_{m+1}^{m+n}) = H(X_1^m) + H(X_1^n)$$
由Fekete引理，熵率极限存在：
$$H = \lim_{n \to \infty} \frac{1}{n} H(X_1^n) = \inf_{n \geq 1} \frac{1}{n} H(X_1^n)$$

### 2. 条件概率表示

定义 $f_n(\omega) = -\log \mu(\omega_{n+1} \mid \omega_1^n)$，其中 $\mu(\omega_{n+1} \mid \omega_1^n)$ 是给定前 $n$ 个符号后第 $n+1$ 个符号的条件概率。则
$$-\log \mu(\omega_1^n) = \sum_{k=0}^{n-1} f_k(\omega)$$
其中 $f_0(\omega) = -\log \mu(\omega_1)$。

### 3. 次可加性

对平稳过程，$f_k(\omega)$ 是平稳序列（即 $f_k \circ T = f_{k+1}$，其中 $T$ 是左平移）。但 $-\log \mu(\omega_1^n)$ 本身不是可加函数，而是次可加的：
$$-\log \mu(\omega_1^{m+n}) \leq -\log \mu(\omega_1^m) - \log \mu(\omega_{m+1}^{m+n})$$

### 4. Kingman次可加遍历定理

**Kingman定理**：设 $\{g_n\}_{n \geq 1}$ 是可测函数序列，满足次可加性 $g_{m+n} \leq g_m + g_n \circ T^m$，且 $\inf_n \frac{1}{n} \int g_n \, d\mu > -\infty$，则存在 $T$-不变函数 $\phi$ 使得
$$\lim_{n \to \infty} \frac{1}{n} g_n(\omega) = \phi(\omega) \quad \mu\text{-a.e.}$$
且 $\int \phi \, d\mu = \lim_{n \to \infty} \frac{1}{n} \int g_n \, d\mu = \inf_n \frac{1}{n} \int g_n \, d\mu$。

取 $g_n(\omega) = -\log \mu(\omega_1^n)$，则 $g_n$ 满足次可加性，且
$$\frac{1}{n} \int g_n \, d\mu = \frac{1}{n} H(X_1^n) \to H$$
由Kingman定理，存在 $\mu$-a.e. 极限
$$\phi(\omega) = \lim_{n \to \infty} -\frac{1}{n} \log \mu(\omega_1^n)$$
且 $\int \phi \, d\mu = H$。

### 5. 利用遍历性确定极限

由于 $\mu$ 是遍历的，$\phi$ 是 $T$-不变的，故 $\phi$ 几乎处处为常数。又 $\int \phi \, d\mu = H$，因此 $\phi(\omega) = H$ $\mu$-a.e.。

### 6. $L^1$ 收敛性

由 $0 \leq -\frac{1}{n} \log \mu(\omega_1^n) \leq \log |A|$（$|A|$ 是字母表大小），有界性保证控制收敛定理适用，因此 $L^1$ 收敛也成立。$\square$

**推论**（典型集）：对任意 $\varepsilon > 0$，存在 $N$，使得对所有 $n \geq N$，存在集合 $T_n \subseteq A^n$（称为典型集），满足：
1. $|T_n| \leq e^{n(H+\varepsilon)}$，
2. $\mu(T_n) \geq 1 - \varepsilon$，
3. 对任意 $x_1^n \in T_n$，$e^{-n(H+\varepsilon)} \leq \mu(x_1^n) \leq e^{-n(H-\varepsilon)}$。$\square$