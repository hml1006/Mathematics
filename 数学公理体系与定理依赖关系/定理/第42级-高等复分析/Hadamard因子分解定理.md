# Hadamard 因子分解定理

## 介绍

Hadamard 因子分解定理（Hadamard factorization theorem）是 Weierstrass 因子分解定理在有限阶整函数情形下的精确化，由法国数学家 Jacques Hadamard 在 1893 年建立。该定理表明，对于有限阶整函数，其因子分解中的整函数 $g(z)$ 退化为一个多项式，且初等因子的指数有统一的上界。该定理是整函数值分布理论（Nevanlinna 理论）和数论（Riemann $\zeta$ 函数）的基础工具。

## 分析

**前置依赖**：Weierstrass 因子分解定理、整函数的阶、增长性、亏格。

**定理内容**：设 $f$ 是有限阶 $\rho$ 的整函数，$\{a_n\}$ 是 $f$ 的非零零点（按重数计），$m$ 是 $0$ 处零点的重数。则 $f$ 可表示为
$$f(z) = z^m e^{P(z)} \prod_{n=1}^\infty E_{p}\left(\frac{z}{a_n}\right)$$
其中 $P(z)$ 是次数不超过 $\rho$ 的多项式，$p \le \rho$ 是某个非负整数（称为 $f$ 的亏格）。

**整函数的阶**：整函数 $f$ 的阶定义为
$$\rho = \limsup_{r \to \infty} \frac{\log \log M(r)}{\log r}$$
其中 $M(r) = \max_{|z| = r} |f(z)|$。

**数学内涵**：Hadamard 定理表明，有限阶整函数的零点分布和增长性之间有紧密联系。零点收敛指数（即 $\sum 1/|a_n|^\alpha$ 收敛的最小 $\alpha$）不超过阶 $\rho$，且 $f$ 完全由零点、阶和多项式 $P$ 决定。

**证明策略**：利用 Weierstrass 因子分解定理，然后利用整函数增长性的估计证明 $g(z)$ 是多项式。通过比较 $f$ 和乘积的增长阶，得到 $g$ 的阶不超过 $\rho$，从而 $g$ 是多项式。

## 思考过程

Hadamard 定理的核心思想是：有限阶整函数的增长性限制了其零点分布和因子分解中的指数因子。具体地：
- 零点收敛指数 $\rho_1 = \inf\{\alpha > 0 \mid \sum 1/|a_n|^\alpha < \infty\} \le \rho$。
- Weierstrass 乘积中的初等因子指数可取为 $p = \lfloor \rho \rfloor$（或 $p = \rho_1$）。
- 因子分解中的 $e^{g(z)}$ 必须是 $e^{P(z)}$，其中 $P$ 是多项式。

Riemann $\zeta$ 函数的 Hadamard 分解是数论中的重要应用：$\zeta(s)$ 的乘积展开给出了其零点与素数分布之间的深刻联系。

## 证明过程

**定理**（Hadamard 因子分解定理）：设 $f$ 是阶为 $\rho$ 的整函数，$m$ 是 $0$ 处零点的重数，$\{a_n\}$ 是非零零点。则
$$f(z) = z^m e^{P(z)} \prod_{n=1}^\infty E_{\lfloor \rho \rfloor}\left(\frac{z}{a_n}\right)$$
其中 $P(z)$ 是次数 $\le \rho$ 的多项式。

**证明**：

**步骤 1**：零点收敛指数。设 $n(r)$ 是 $|a_n| \le r$ 的零点个数。由 Jensen 公式，
$$\int_0^r \frac{n(t)}{t} \, dt \le \frac{1}{2\pi} \int_0^{2\pi} \log|f(re^{i\theta})| \, d\theta - \log|f(0)|$$
由 $f$ 的阶为 $\rho$，可证零点收敛指数 $\rho_1 \le \rho$，即 $\sum 1/|a_n|^{\rho+\varepsilon} < \infty$。

**步骤 2**：构造 Weierstrass 乘积。取 $p = \lfloor \rho \rfloor$，则 $p+1 > \rho$，故 $\sum (1/|a_n|)^{p+1} < \infty$。定义
$$P_1(z) = \prod_{n=1}^\infty E_{p}\left(\frac{z}{a_n}\right)$$
该乘积阶不超过 $\rho$。

**步骤 3**：由 Weierstrass 定理，$f(z) = z^m e^{g(z)} P_1(z)$，其中 $g$ 是整函数。比较阶：
$$\rho = \max(\rho(P_1), \rho(e^g))$$
由于 $\rho(P_1) \le \rho$，故 $\rho(e^g) \le \rho$。

**步骤 4**：$e^{g(z)}$ 的阶等于 $\rho(g)$（即 $g$ 的增长阶）。若 $\rho(g) < \infty$，则 $g$ 是多项式。由 $\rho(e^g) \le \rho$，$g$ 的次数不超过 $\rho$。

**步骤 5**：因此 $g(z) = P(z)$ 是多项式，次数 $\le \rho$。代入得
$$f(z) = z^m e^{P(z)} \prod_{n=1}^\infty E_{p}\left(\frac{z}{a_n}\right)$$
其中 $p = \lfloor \rho \rfloor$。$\square$

**例**（$\sin(\pi z)$ 的 Hadamard 分解）：$\sin(\pi z)$ 的阶为 $1$，零点为 $n \in \mathbb{Z}$，故
$$\sin(\pi z) = \pi z e^{P(z)} \prod_{n=1}^\infty \left(1 - \frac{z^2}{n^2}\right)$$
由对称性，$P(z)$ 是常数，由 $\lim_{z\to 0} \sin(\pi z)/z = \pi$ 得 $P(z) = 0$，故
$$\sin(\pi z) = \pi z \prod_{n=1}^\infty \left(1 - \frac{z^2}{n^2}\right)$$