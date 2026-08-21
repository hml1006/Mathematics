# Dirichlet算术级数定理

> **一句话大白话**：任意两个互素的数 $a,d$，等差数列 $a,\,a+d,\,a+2d,\dots$ 里藏着无穷多个素数——靠的是 Dirichlet 特征构造的 $L$ 函数在 $s=1$ 处取非零值。
>
> **小例子**：$4k+1$ 与 $4k+3$ 两个口袋里都各有无数个素数；核心一步是证明 $L(1,\chi)\neq 0$，对每个非主特征 $\chi$ 都成立。

## 介绍

Dirichlet 算术级数定理由 Dirichlet 于 1837 年证明，是解析数论的奠基性成果之一。该定理断言：对任意互素的正整数 $a$ 和 $q$，算术级数 $a, a+q, a+2q, a+3q, \ldots$ 包含无穷多个素数。换句话说，素数在模 $q$ 的每个互素剩余类中均匀分布。Dirichlet 为此引入了 Dirichlet 特征和 L 函数，开启了解析数论的研究。

## 分析

**前置依赖**：Euler 乘积、Zeta 函数、群特征标、Dirichlet L 函数。

**定理内容**：设 $a, q$ 是正整数，$\gcd(a, q) = 1$，则存在无穷多个素数 $p$ 满足 $p \equiv a \pmod{q}$。

**数学内涵**：
- 素数在模 $q$ 的 $\varphi(q)$ 个互素剩余类中渐近均匀分布。
- 等价于 $\sum_{p \equiv a \pmod{q}} \frac{1}{p}$ 发散。
- 定理的证明引入 Dirichlet L 函数 $L(s, \chi)$，并证明 $L(1, \chi) \neq 0$ 对非主特征 $\chi$ 成立。

**证明策略**：
1. 引入模 $q$ 的 Dirichlet 特征 $\chi$，利用正交关系筛选剩余类。
2. 定义 Dirichlet L 函数 $L(s, \chi) = \sum_{n=1}^\infty \chi(n) n^{-s}$，对 $\operatorname{Re}(s) > 1$ 绝对收敛。
3. 证明 $L(1, \chi) \neq 0$ 对所有非主特征 $\chi$ 成立。
4. 利用 $\sum_{p \equiv a \pmod{q}} \frac{1}{p^s}$ 的解析行为推出结论。

## 思考过程

Dirichlet 的核心思想是使用特征标来"筛选"出特定的剩余类。利用正交关系：
$$\frac{1}{\varphi(q)} \sum_{\chi \bmod q} \chi(a)^{-1} \chi(n) = \begin{cases}
1, & n \equiv a \pmod{q} \\
0, & \text{否则}
\end{cases}$$

将素数计数问题转化为对 $\sum_{\chi} \chi(a)^{-1} \log L(s, \chi)$ 的分析。定理的关键难点在于证明 $L(1, \chi) \neq 0$ 对实特征（即值为 $\pm 1$ 的特征）也成立，这需要更精细的数论论证。

## 证明过程

**定理**（Dirichlet）：设 $\gcd(a, q) = 1$，则存在无穷多个素数 $p \equiv a \pmod{q}$。

**证明**：

### 1. Dirichlet 特征

设 $\widehat{G}$ 是模 $q$ 的 Dirichlet 特征群，主特征 $\chi_0$ 满足 $\chi_0(n) = 1$ 若 $\gcd(n, q)=1$，否则为 0。

正交关系：
$$\sum_{\chi \in \widehat{G}} \chi(a)^{-1} \chi(n) = \begin{cases}
\varphi(q), & n \equiv a \pmod{q} \\
0, & \text{否则}
\end{cases}$$

### 2. Dirichlet L 函数

对 $\operatorname{Re}(s) > 1$，
$$L(s, \chi) = \sum_{n=1}^\infty \frac{\chi(n)}{n^s} = \prod_p \frac{1}{1 - \chi(p) p^{-s}}$$

### 3. 关键引理

**引理**：$L(1, \chi) \neq 0$ 对所有非主特征 $\chi$ 成立。

*证明概要*：
- 考虑乘积 $\prod_{\chi} L(s, \chi)$。
- 若存在实特征 $\chi_1$ 使得 $L(1, \chi_1) = 0$，则 $L(s, \chi_1)$ 在 $s=1$ 处有零点，导致 $\prod_{\chi} L(s, \chi)$ 在 $s=1$ 附近的行为与 $\zeta(s)$ 矛盾。
- 对复特征，$L(1, \chi) = 0$ 会导致 $L(1, \overline{\chi}) = 0$，结合 $\prod_{\chi} L(s, \chi)$ 的正则性推出矛盾。$\square$

### 4. 级数的发散性

考虑：
$$\sum_{p \equiv a \pmod{q}} \frac{1}{p^s} = \frac{1}{\varphi(q)} \sum_{\chi} \chi(a)^{-1} \sum_p \frac{\chi(p)}{p^s} + O(1)$$

而
$$\sum_p \frac{\chi(p)}{p^s} = \log L(s, \chi) + O(1)$$

当 $s \to 1^+$ 时：
- 对 $\chi = \chi_0$，$L(s, \chi_0) \sim \zeta(s) \sim \frac{1}{s-1}$，故 $\log L(s, \chi_0) \to \infty$。
- 对 $\chi \neq \chi_0$，$L(1, \chi) \neq 0$ 且有限，故 $\log L(s, \chi)$ 有界。

因此：
$$\sum_{p \equiv a \pmod{q}} \frac{1}{p^s} \sim \frac{1}{\varphi(q)} \log \frac{1}{s-1} \to \infty \quad (s \to 1^+)$$

这表明 $\sum_{p \equiv a \pmod{q}} \frac{1}{p}$ 发散，从而存在无穷多个满足条件的素数。$\square$

**推论**：素数在模 $q$ 的互素剩余类中渐近均匀分布：$\pi(x; q, a) \sim \frac{x}{\varphi(q) \log x}$。$\square$
## 相关条目

- [Dirichlet 算术级数定理（第75级-解析数论）](../第75级-解析数论/Dirichlet算术级数定理.md)：与本条目为同一定理，另收录于第75级-解析数论，可交叉参考。
