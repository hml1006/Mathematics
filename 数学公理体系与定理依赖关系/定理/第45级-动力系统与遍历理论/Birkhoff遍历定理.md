# Birkhoff遍历定理

## 介绍

Birkhoff遍历定理（Birkhoff Ergodic Theorem），又称逐点遍历定理（Pointwise Ergodic Theorem），是遍历理论中最基本的定理之一，由George David Birkhoff于1931年证明。该定理断言：在保测变换下，函数沿轨道的时间平均几乎处处等于其空间平均（当系统是遍历时）。这一定理为统计力学中"各态历经假设"提供了严格的数学基础，即系统的长时间平均等于系综平均。Birkhoff遍历定理是遍历理论乃至整个动力系统理论的基石。

## 分析

**前置依赖**：测度论、Lebesgue积分、概率空间、可测函数、保测变换、遍历性。

**定理内容**：设 $(X, \mathcal{F}, \mu)$ 是一个概率空间，$T: X \to X$ 是保测变换（即 $\mu(T^{-1}(A)) = \mu(A)$ 对所有 $A \in \mathcal{F}$ 成立）。对任意 $f \in L^1(X, \mu)$，极限
$$\lim_{n \to \infty} \frac{1}{n} \sum_{k=0}^{n-1} f(T^k(x))$$
对 $\mu$-几乎处处 $x \in X$ 存在。记该极限为 $\bar{f}(x)$，则 $\bar{f}$ 是 $T$-不变的（即 $\bar{f} \circ T = \bar{f}$，$\mu$-a.e.），且
$$\int_X \bar{f} \, d\mu = \int_X f \, d\mu$$
特别地，若 $T$ 是遍历的（即 $\mu(A) = 0$ 或 $1$ 对所有 $T^{-1}(A) = A$ 的 $A$ 成立），则 $\bar{f}$ 几乎处处等于常数 $\int_X f \, d\mu$。

**数学内涵**：
- 时间平均 $\frac{1}{n}\sum_{k=0}^{n-1} f(T^k(x))$ 是轨道 $\{T^k(x)\}$ 上函数值的前 $n$ 项算术平均。
- 空间平均 $\int_X f \, d\mu$ 是 $f$ 在整个空间上的积分平均。
- 遍历性条件是保证时间平均与空间平均相等的充要条件。
- 该定理适用于所有 $L^1$ 函数，不仅限于有界或连续函数。

**证明策略**：
1. 利用最大遍历引理（Maximal Ergodic Lemma）或Hopf的极大不等式。
2. 先证明极限的上界和下界几乎处处相等。
3. 构造 $T$-不变函数并验证其积分性质。

## 思考过程

Birkhoff遍历定理的证明核心是最大遍历引理，它本质上是一个覆盖引理，类似于实分析中的Vitali覆盖引理。该引理断言：对任意 $f \in L^1$，集合
$$E = \left\{ x \in X \mid \sup_{n \geq 1} \frac{1}{n} \sum_{k=0}^{n-1} f(T^k(x)) > 0 \right\}$$
满足 $\int_E f \, d\mu \geq 0$。这一看似简单的不等式是整个证明的关键。

从物理视角看，Birkhoff定理说明：只要系统是保测的，粒子在相空间中的长时间逗留时间分布就收敛到一个不变分布。这为理解统计力学和热力学提供了坚实的数学基础。

## 证明过程

**定理**（Birkhoff逐点遍历定理）：设 $(X, \mathcal{F}, \mu)$ 是概率空间，$T: X \to X$ 保测，$f \in L^1(X, \mu)$。则存在 $f^* \in L^1(X, \mu)$，$T$-不变，使得
$$\lim_{n \to \infty} \frac{1}{n} \sum_{k=0}^{n-1} f(T^k(x)) = f^*(x) \quad \mu\text{-a.e.}$$
且 $\int_X f^* \, d\mu = \int_X f \, d\mu$。

**证明**：

### 1. 极大遍历引理

**引理**（最大遍历引理）：对任意 $f \in L^1$，设
$$E = \left\{ x \in X \mid \sup_{n \geq 1} \frac{1}{n} \sum_{k=0}^{n-1} f(T^k(x)) > 0 \right\}$$
则 $\int_E f \, d\mu \geq 0$。

*证明*：令 $S_n(x) = \sum_{k=0}^{n-1} f(T^k(x))$，$M_n(x) = \max\{S_1(x), \ldots, S_n(x)\}$，$M_n^+(x) = \max\{0, M_n(x)\}$。对任意 $x$，有
$$S_{n+1}(x) = f(x) + S_n(T(x)) \leq f(x) + M_n^+(T(x))$$
若 $M_n^+(x) > 0$，则 $M_n^+(x) = S_k(x)$ 对某个 $k$，从而
$$M_n^+(x) \leq f(x) + M_n^+(T(x))$$
在集合 $\{M_n^+ > 0\}$ 上积分，利用保测性可得 $\int_{\{M_n^+ > 0\}} f \, d\mu \geq 0$。令 $n \to \infty$ 即得结果。$\square$

### 2. 极限的存在性

定义
$$\bar{f}(x) = \limsup_{n \to \infty} \frac{1}{n} S_n(x), \quad \underline{f}(x) = \liminf_{n \to \infty} \frac{1}{n} S_n(x)$$
显然 $\bar{f}$ 和 $\underline{f}$ 都是 $T$-不变的。只需证明 $\bar{f}(x) = \underline{f}(x)$ $\mu$-a.e.。

对任意 $a < b$，设 $E_{a,b} = \{x \mid \underline{f}(x) < a < b < \bar{f}(x)\}$。若 $\mu(E_{a,b}) = 0$ 对所有 $a, b$ 成立，则 $\bar{f} = \underline{f}$ $\mu$-a.e.。

### 3. 估计 $\mu(E_{a,b})$

假设 $\mu(E_{a,b}) > 0$。由于 $\bar{f}$ 是 $T$-不变的，$E_{a,b}$ 是 $T$-不变的。令 $g(x) = f(x) - b$，则
$$\sup_{n \geq 1} \frac{1}{n} \sum_{k=0}^{n-1} g(T^k(x)) > 0, \quad \forall x \in E_{a,b}$$
由最大遍历引理，$\int_{E_{a,b}} g \, d\mu \geq 0$，即 $\int_{E_{a,b}} f \, d\mu \geq b \mu(E_{a,b})$。

类似地，令 $h(x) = a - f(x)$，可得 $\int_{E_{a,b}} h \, d\mu \geq 0$，即 $\int_{E_{a,b}} f \, d\mu \leq a \mu(E_{a,b})$。

结合两式：$a \mu(E_{a,b}) \geq \int_{E_{a,b}} f \, d\mu \geq b \mu(E_{a,b})$，由于 $a < b$，必有 $\mu(E_{a,b}) = 0$。因此 $\bar{f} = \underline{f}$ $\mu$-a.e.，记共同极限为 $f^*$。

### 4. 积分性质

由控制收敛定理（或Fatou引理）和 $f \in L^1$ 可得
$$\int_X f^* \, d\mu = \lim_{n \to \infty} \int_X \frac{1}{n} \sum_{k=0}^{n-1} f(T^k(x)) \, d\mu = \int_X f \, d\mu$$
其中交换极限和积分由 $\frac{1}{n} \sum_{k=0}^{n-1} |f(T^k(x))|$ 的一致可积性保证。$\square$

**推论**（遍历性下的简化）：若 $T$ 是遍历的，则对任意 $f \in L^1$，
$$\lim_{n \to \infty} \frac{1}{n} \sum_{k=0}^{n-1} f(T^k(x)) = \int_X f \, d\mu \quad \mu\text{-a.e.}$$
即时间平均等于空间平均。$\square$