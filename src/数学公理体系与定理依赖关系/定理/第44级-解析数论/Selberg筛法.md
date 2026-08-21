# Selberg筛法

> **一句话大白话**：挑数的时候给"幸存者"按最优权重打分，把 $\lambda_d$ 当变元做二次极小化，从而在奇偶性问题上给出比简单乘法筛更紧的上下界。
>
> **小例子**：估算孪生数和 Goldbach 问题中"$n$ 与 $n+h$ 同为素数"的个数的上界时，Selberg 权重 $(\sum_{d\mid n}\lambda_d)^2$ 能让误差项显著更小。

## 介绍

Selberg 筛法由 Atle Selberg 在 20 世纪 40 年代提出，是解析数论中最强大的筛法工具之一。与经典的 Brun 筛法相比，Selberg 筛法通过引入二次型优化技巧（即 Selberg 的"上界筛法"），能够给出更精确的素数分布上界估计。筛法的基本问题是估计满足某些同余条件的整数集合的大小，特别地，可用于估计孪生素数、素数间隙等问题中的素数计数。

## 分析

**前置依赖**：素数分布、Möbius 函数、Dirichlet 卷积、初等数论。

**定理内容**：设 $\mathcal{A}$ 是正整数集合，$\mathcal{P}$ 是素数集合，$\mathcal{A}_d = \{a \in \mathcal{A} \mid d \mid a\}$。设 $X > 0$，$r_d$ 满足 $|\mathcal{A}_d| = \frac{X}{f(d)} + r_d$，其中 $f$ 是积性函数。则 Selberg 筛法给出：
$$S(\mathcal{A}, \mathcal{P}, z) \leq \frac{X}{G(z)} + O\left(\sum_{d < z^2} 3^{\omega(d)} |r_d|\right)$$
其中 $S(\mathcal{A}, \mathcal{P}, z)$ 是 $\mathcal{A}$ 中不被任何小于 $z$ 的素数整除的元素的个数，$G(z) = \sum_{d < z} \frac{1}{f(d)}$。

**数学内涵**：
- Selberg 筛法通过选择最优的权重 $\lambda_d$ 来最小化上界。
- 权重满足 $\lambda_1 = 1$，且 $\lambda_d = 0$ 对 $d \geq z$。
- 核心不等式：$\left(\sum_{d \mid n} \lambda_d\right)^2 \geq 0$，从而 $\sum_{d \mid n} \mu(d) \leq \left(\sum_{d \mid n} \lambda_d\right)^2$。

**证明策略**：
1. 利用 $\sum_{d \mid n} \mu(d)$ 作为特征函数（$n=1$ 时为 1，否则为 0）。
2. 用 $\left(\sum_{d \mid n} \lambda_d\right)^2$ 给出上界，其中 $\lambda_d$ 是待定系数。
3. 通过二次型最小化确定最优 $\lambda_d$。
4. 估计主项和余项。

## 思考过程

Selberg 筛法的核心创新在于用二次型优化替代了 Brun 筛法中的复杂组合推理。具体来说，注意到
$$1_{\gcd(n, P(z)) = 1} = \sum_{d \mid \gcd(n, P(z))} \mu(d)$$
其中 $P(z) = \prod_{p < z} p$。Selberg 的核心观察是：对任意实数 $\lambda_d$ 满足 $\lambda_1 = 1$，
$$\sum_{d \mid n} \mu(d) \leq \left(\sum_{d \mid n} \lambda_d\right)^2$$
这一不等式允许我们通过选择最优的 $\lambda_d$ 来获得尽可能紧的上界。

## 证明过程

**定理**（Selberg 筛法基本引理）：设 $\lambda_d$ 是实数，$\lambda_1 = 1$，$\lambda_d = 0$ 对所有 $d \geq z$，则
$$\sum_{\substack{n \leq x \\ \gcd(n, P(z)) = 1}} 1 \leq \sum_{n \leq x} \left(\sum_{d \mid n} \lambda_d\right)^2$$

**证明**：对任意 $n$，若 $\gcd(n, P(z)) = 1$，则 $\sum_{d \mid n} \mu(d) = 1$。由不等式：
$$1 = \left(\sum_{d \mid n} \mu(d)\right)^2 \leq \left(\sum_{d \mid n} \lambda_d\right)^2$$
其中 $\lambda_d$ 满足条件。对 $n$ 求和即得。$\square$

**定理**（Selberg 上界筛法）：设 $\mathcal{A} = \{n \leq X\}$，$f(d) = d/\varphi(d)$ 对 $d$ 无平方因子，则
$$S(\mathcal{A}, \mathcal{P}, z) \leq \frac{X}{\sum_{d < z} \frac{\mu(d)^2}{f(d)}} + O(z^2)$$

**证明**：

### 1. 展开上界

展开平方和：
$$\sum_{n \leq X} \left(\sum_{d \mid n} \lambda_d\right)^2 = \sum_{d_1, d_2} \lambda_{d_1} \lambda_{d_2} \sum_{\substack{n \leq X \\ d_1 \mid n, d_2 \mid n}} 1 = \sum_{d_1, d_2} \lambda_{d_1} \lambda_{d_2} \left(\frac{X}{[d_1, d_2]} + O(1)\right)$$

### 2. 主项

主项为：
$$X \sum_{d_1, d_2} \frac{\lambda_{d_1} \lambda_{d_2}}{[d_1, d_2]} = X \sum_{d_1, d_2} \frac{\lambda_{d_1} \lambda_{d_2}}{d_1 d_2} \gcd(d_1, d_2)$$

令 $g(d) = \gcd(d_1, d_2)$，$d_1 = g a$，$d_2 = g b$，则 $\gcd(a, b) = 1$，$1/[d_1, d_2] = 1/(gab)$。

### 3. 最优选择

令 $\lambda_d = \mu(d) \frac{d}{\varphi(d)} \frac{y_d}{X}$，其中 $y_d$ 待定。通过变分法，最优选择为：
$$\lambda_d = \frac{\mu(d) d}{\varphi(d)} \frac{G(z)}{G(d)}$$
其中 $G(z) = \sum_{d < z} \frac{\mu(d)^2}{f(d)}$。

### 4. 代入计算

将最优 $\lambda_d$ 代入，主项简化为 $X / G(z)$。余项估计为 $O(z^2)$。$\square$

**推论**（孪生素数估计）：设 $\pi_2(x)$ 表示不超过 $x$ 的孪生素数对个数，则
$$\pi_2(x) \ll \frac{x}{(\log x)^2}$$

**证明**：令 $\mathcal{A} = \{n(n+2) \mid n \leq x\}$，$z = \sqrt{x}$，应用 Selberg 筛法。筛函数的渐近估计给出上界。$\square$

**意义**：Selberg 筛法在解析数论中有广泛应用，包括素数间隙、孪生素数、算术级数中的素数分布等问题。其二次型优化思想也被后来的 Goldston-Pintz-Yıldırım 筛法（用于证明素数间隙有界）所继承
## 相关条目

- [Selberg 筛法（第75级-解析数论）](../第75级-解析数论/Selberg筛法.md)：与本条目为同一定理，另收录于第75级-解析数论，可交叉参考。
