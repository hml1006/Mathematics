# RiemannZeta函数与Euler乘积

## 介绍

Riemann Zeta 函数是解析数论中最核心的函数，由 Leonhard Euler 在 18 世纪首次研究，后由 Bernhard Riemann 在 1859 年的著名论文中进行了系统分析。Zeta 函数定义为 $\zeta(s) = \sum_{n=1}^\infty n^{-s}$，对 $\operatorname{Re}(s) > 1$ 绝对收敛。Euler 乘积公式 $\zeta(s) = \prod_{p} (1 - p^{-s})^{-1}$ 将 Zeta 函数与素数分布联系起来，是解析数论的基石之一。

## 分析

**前置依赖**：无穷级数、无穷乘积、素数基本性质、复分析基础。

**定理内容**：
- 对 $\operatorname{Re}(s) > 1$，$\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}$ 绝对收敛。
- Euler 乘积：$\zeta(s) = \prod_{p \text{ 素数}} \frac{1}{1 - p^{-s}}$，对 $\operatorname{Re}(s) > 1$ 成立。
- $\zeta(s)$ 可解析延拓到整个复平面，仅在 $s = 1$ 处有一个留数为 1 的单极点。

**数学内涵**：
- Euler 乘积公式建立了 Zeta 函数与素数的联系，等价于算术基本定理的解析表达。
- $\zeta(s)$ 在 $\operatorname{Re}(s) = 1$ 上的零点分布与素数定理密切相关。
- Riemann 假设：$\zeta(s)$ 的所有非平凡零点都位于 $\operatorname{Re}(s) = 1/2$ 上。

**证明策略**：
1. 利用几何级数展开 $\frac{1}{1 - p^{-s}} = \sum_{k=0}^\infty p^{-ks}$。
2. 通过算术基本定理，将所有素数幂的乘积展开为所有正整数的和。
3. 利用绝对收敛性交换求和与求积顺序。

## 思考过程

Euler 乘积公式的推导本质上是算术基本定理的解析版本。每个正整数 $n$ 有唯一的素数分解 $n = \prod_p p^{e_p}$，因此 $\prod_p (1 - p^{-s})^{-1} = \prod_p \sum_{e=0}^\infty p^{-es} = \sum_{n=1}^\infty n^{-s}$。

这一公式的深刻之处在于它将 Zeta 函数的零点信息与素数分布联系起来。Riemann 认识到，如果能理解 $\zeta(s)$ 在复平面上的零点分布，就能精确描述素数的分布规律。这正是素数定理及其余项估计的出发点。

## 证明过程

**定理**（Euler 乘积）：对 $\operatorname{Re}(s) > 1$，
$$\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s} = \prod_{p \text{ 素数}} \frac{1}{1 - p^{-s}}$$

**证明**：

对每个素数 $p$，由几何级数：
$$\frac{1}{1 - p^{-s}} = \sum_{k=0}^\infty p^{-ks} = 1 + p^{-s} + p^{-2s} + \cdots$$

对 $\operatorname{Re}(s) > 1$，$\sum_{p} |p^{-s}|$ 收敛，故可逐项相乘。对所有素数取乘积：
$$\prod_{p \leq N} \frac{1}{1 - p^{-s}} = \prod_{p \leq N} \sum_{k=0}^\infty p^{-ks} = \sum_{n \in A_N} \frac{1}{n^s}$$

其中 $A_N$ 是所有仅含 $\leq N$ 的素因子的正整数集合。当 $N \to \infty$ 时，$A_N$ 趋于全体正整数，故
$$\prod_{p} \frac{1}{1 - p^{-s}} = \sum_{n=1}^\infty \frac{1}{n^s} = \zeta(s)$$

由于 $\operatorname{Re}(s) > 1$ 时级数绝对收敛，运算合法。$\square$

**推论**：对 $\operatorname{Re}(s) > 1$，
$$\sum_{p} \frac{1}{p^s} = \log \zeta(s) + O(1)$$

**证明**：对 Euler 乘积取对数，
$$\log \zeta(s) = -\sum_{p} \log(1 - p^{-s}) = \sum_{p} \sum_{k=1}^\infty \frac{p^{-ks}}{k} = \sum_{p} \frac{1}{p^s} + O\left(\sum_{p} \frac{1}{p^{2\sigma}}\right)$$
其中 $\sigma = \operatorname{Re}(s) > 1$，余项有界。$\square$