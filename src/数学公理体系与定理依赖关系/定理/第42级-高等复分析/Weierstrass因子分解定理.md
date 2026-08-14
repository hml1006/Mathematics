# Weierstrass 因子分解定理

## 介绍

Weierstrass 因子分解定理（Weierstrass factorization theorem）是复分析中的基本定理，由 Karl Weierstrass 在 1876 年建立。该定理断言：任意整函数 $f$（复平面上全纯的函数）可以表示为无穷乘积形式，其因子由 $f$ 的零点决定。该定理是整函数结构理论的核心，揭示了整函数与其零点之间的关系，是研究整函数增长性质的基础。

## 分析

**前置依赖**：全纯函数、整函数、零点、无穷乘积、收敛性、Taylor 展开。

**定理内容**：设 $f$ 是整函数，$f(0) \neq 0$（否则考虑 $f(z)/z^m$），$\{a_n\}$ 是 $f$ 的非零零点（按重数计）。则存在整函数 $g$ 和非负整数 $m$ 使得
$$f(z) = z^m e^{g(z)} \prod_{n=1}^\infty E_{p_n}\left(\frac{z}{a_n}\right)$$
其中 $E_p(z) = (1-z) \exp\left(z + \frac{z^2}{2} + \cdots + \frac{z^p}{p}\right)$ 是 Weierstrass 初等因子，$p_n$ 是使级数 $\sum (|z|/|a_n|)^{p_n+1}$ 收敛的整数。

**Weierstrass 初等因子**：
$$E_0(z) = 1 - z$$
$$E_p(z) = (1-z) \exp\left(z + \frac{z^2}{2} + \cdots + \frac{z^p}{p}\right),\quad p \ge 1$$
当 $|z| \le 1$ 时，$|1 - E_p(z)| \le C|z|^{p+1}$。

**数学内涵**：Weierstrass 定理表明，整函数本质上由其零点决定（模一个非零整函数因子 $e^{g(z)}$）。这与多项式由根决定类似，但无穷乘积需要收敛因子来保证收敛性。

**证明策略**：构造无穷乘积 $\prod E_{p_n}(z/a_n)$ 使其收敛，然后证明 $f(z)$ 除以该乘积得到的函数是整函数且无零点，从而可表示为 $e^{g(z)}$。

## 思考过程

Weierstrass 定理的构造基于一个关键观察：直接乘积 $\prod (1 - z/a_n)$ 通常不收敛（因为 $\sum 1/|a_n|$ 发散），但通过引入指数收敛因子 $E_p(z)$，可以加速收敛。

初等因子 $E_p(z)$ 的性质：当 $|z| < 1$ 时，$\log E_p(z)$ 的幂级数展开从 $z^{p+1}$ 项开始，因此 $|1 - E_p(z)| \le C|z|^{p+1}$。选择 $p_n$ 使得 $\sum (r/|a_n|)^{p_n+1} < \infty$，则乘积在 $|z| < r$ 上一致收敛。

## 证明过程

**定理**（Weierstrass 因子分解定理）：设 $f$ 是整函数，$\{a_n\}$ 是其非零零点（按重数计），$m$ 是 $0$ 处零点的重数。则存在整函数 $g$ 使得
$$f(z) = z^m e^{g(z)} \prod_{n=1}^\infty E_{p_n}\left(\frac{z}{a_n}\right)$$

**证明**：

**步骤 1**：构造收敛因子。对每个零点 $a_n$，选择非负整数 $p_n$ 使得级数
$$\sum_{n=1}^\infty \left(\frac{r}{|a_n|}\right)^{p_n+1}$$
对每个 $r > 0$ 收敛（例如取 $p_n = n$ 或 $p_n = \lfloor \log |a_n| \rfloor$）。

**步骤 2**：定义无穷乘积。令
$$P(z) = \prod_{n=1}^\infty E_{p_n}\left(\frac{z}{a_n}\right)$$
由 Weierstrass 初等因子的估计，对任意 $R > 0$，当 $|z| \le R$ 时，
$$\sum_{n=1}^\infty \left|1 - E_{p_n}\left(\frac{z}{a_n}\right)\right| \le C \sum_{n=1}^\infty \left(\frac{R}{|a_n|}\right)^{p_n+1} < \infty$$
故乘积在 $\mathbb{C}$ 上局部一致收敛，$P(z)$ 是整函数，零点集恰为 $\{a_n\}$。

**步骤 3**：构造整函数 $g$。考虑函数
$$h(z) = \frac{f(z)}{z^m P(z)}$$
$h$ 是整函数且无零点（因为分子分母的零点抵消）。由整函数的性质，$h(z) = e^{g(z)}$ 对某个整函数 $g$ 成立。

**步骤 4**：代入即得
$$f(z) = z^m e^{g(z)} \prod_{n=1}^\infty E_{p_n}\left(\frac{z}{a_n}\right)$$

**步骤 5**：当 $f$ 有有限个零点时，取 $p_n = 0$，即得多项式分解。$\square$

**推论**：$\sin(\pi z)$ 的 Weierstrass 乘积展开为
$$\sin(\pi z) = \pi z \prod_{n=1}^\infty \left(1 - \frac{z^2}{n^2}\right)$$
这由 $\sin(\pi z)$ 的零点 $z = n$（$n \in \mathbb{Z}$）和 $g(z) = \log \pi$ 得到。