# Riesz-Thorin插值定理

> **一句话大白话**：线性算子若在 $L^{p_0}$ 和 $L^{p_1}$ 两个极端指标上都"正经有界"，那么它在两者之间连成的整条弧线（$L^p$ 指标）上也都有界，且界跟着插值连续过度——"端点好，中间必然也好"。
>
> **小例子**：卷积算子若已在 $L^1$ 和 $L^\infty$ 上分别有界，则对任意 $1\le p\le\infty$ 它在 $L^p$ 上都有界，且范数可由两端范数插值得出——傅里叶分析的看家插值法。

## 介绍

Riesz-Thorin插值定理是调和分析和泛函分析中的一个经典插值定理，由 Marcel Riesz 提出，后由 G. O. Thorin 在 1939 年使用复分析方法完成证明。它断言：如果一个线性算子同时满足 $L^{p_0} \to L^{q_0}$ 和 $L^{p_1} \to L^{q_1}$ 的有界性，则它对中间指数 $L^{p_\theta} \to L^{q_\theta}$ 也是有界的，其中 $1/p_\theta = (1-\theta)/p_0 + \theta/p_1$，$1/q_\theta = (1-\theta)/q_0 + \theta/q_1$。这个定理是 Fourier 分析中许多重要不等式（如 Hausdorff-Young 不等式）的证明基础。

## 分析

**前置依赖**：三线定理（Phragmén-Lindelöf 原理）、$L^p$ 范数的对偶表示、Hölder 不等式、简单函数逼近

**定理的精确表述**：设 $(X, \mu)$ 和 $(Y, \nu)$ 是测度空间，$T$ 是简单函数空间上的线性算子，满足：

- $\|T f\|_{L^{q_0}} \le M_0 \|f\|_{L^{p_0}}$ 对所有简单函数 $f$ 成立；
- $\|T f\|_{L^{q_1}} \le M_1 \|f\|_{L^{p_1}}$ 对所有简单函数 $f$ 成立。

其中 $1 \le p_0, p_1, q_0, q_1 \le \infty$。则对任意 $\theta \in (0,1)$，定义

$$
\frac{1}{p_\theta} = \frac{1-\theta}{p_0} + \frac{\theta}{p_1}, \quad \frac{1}{q_\theta} = \frac{1-\theta}{q_0} + \frac{\theta}{q_1},
$$

存在常数 $M_\theta \le M_0^{1-\theta} M_1^\theta$ 使得

$$
\|T f\|_{L^{q_\theta}} \le M_\theta \|f\|_{L^{p_\theta}}
$$

对所有简单函数 $f$ 成立，从而 $T$ 可唯一延拓为 $L^{p_\theta} \to L^{q_\theta}$ 的有界线性算子。

**关键要点**：

- 与 Marcinkiewicz 插值不同，Riesz-Thorin 插值要求 $T$ 是线性算子（而非次线性），但给出的是精确的常数估计 $M_\theta \le M_0^{1-\theta} M_1^\theta$。
- 指数 $p_\theta, q_\theta$ 是调和平均（倒数意义下的线性插值）。
- 当 $p_0 = q_0$ 且 $p_1 = q_1$ 时，Riesz-Thorin 退化为 $L^p$ 空间的插值。
- 定理的证明使用复分析方法（Thorin 的三线定理），因此称为"复插值"。

## 思考过程

Riesz-Thorin 定理的证明基于复分析中的 Phragmén-Lindelöf 原理（三线定理）：

1. **对偶表示**：$L^q$ 范数可以通过对偶表示为 $\|T f\|_q = \sup_{\|g\|_{q'} = 1} |\int (T f) g \, d\nu|$。

2. **构造复变函数**：对固定 $f$ 和 $g$，定义参数化函数族 $f_z(x) = |f(x)|^{a(z)} \operatorname{sgn}(f(x))$ 和 $g_z(y) = |g(y)|^{b(z)} \operatorname{sgn}(g(y))$，其中 $a(z), b(z)$ 是 $z$ 的线性函数，使得在 $\operatorname{Re} z = 0$ 和 $\operatorname{Re} z = 1$ 上分别对应 $p_0, q_0$ 和 $p_1, q_1$ 情形。

3. **三线定理**：定义 $F(z) = \int (T f_z) g_z \, d\nu$，证明 $F(z)$ 是解析函数且在带形区域上有界。由三线定理，$\log |F(z)|$ 是凸函数，从而 $|F(\theta)| \le \sup_{\operatorname{Re} z=0} |F(z)|^{1-\theta} \sup_{\operatorname{Re} z=1} |F(z)|^\theta$。

4. **得出估计**：由 $F(z)$ 在边界上的估计，得到 $|F(\theta)| \le M_0^{1-\theta} M_1^\theta \|f\|_{p_\theta} \|g\|_{q_\theta'}$，从而 $\|T f\|_{q_\theta} \le M_\theta \|f\|_{p_\theta}$。

## 证明过程

**证明**：我们给出 Riesz-Thorin 定理的证明概要（Thorin 的复分析方法）。

**步骤 1**：对偶化。设 $f$ 是简单函数，$\|f\|_{p_\theta} = 1$。由 $L^q$ 范数的对偶表示，

$$
\|T f\|_{q_\theta} = \sup \left\{ \left| \int_Y (T f) g \, d\nu \right| \mid g \text{ 简单}, \|g\|_{q_\theta'} = 1 \right\},
$$

其中 $1/q_\theta + 1/q_\theta' = 1$。

**步骤 2**：参数化。设 $f$ 和 $g$ 是标准化的简单函数，$\|f\|_{p_\theta} = \|g\|_{q_\theta'} = 1$。将 $f$ 和 $g$ 表示为

$$
f = \sum_{j=1}^m a_j \chi_{A_j}, \quad g = \sum_{k=1}^n b_k \chi_{B_k},
$$

其中 $A_j$ 和 $B_k$ 是不交可测集，$a_j, b_k \in \mathbb{C}$。

定义函数 $a(z)$ 和 $b(z)$ 为 $z$ 的线性函数，满足

$$
\frac{1}{p(z)} = \frac{1-z}{p_0} + \frac{z}{p_1}, \quad \frac{1}{q'(z)} = \frac{1-z}{q_0'} + \frac{z}{q_1'}.
$$

其中 $q_0' = q_0/(q_0-1)$，$q_1' = q_1/(q_1-1)$。则 $p(\theta) = p_\theta$，$q'(\theta) = q_\theta'$。

定义参数化函数族

$$
f_z(x) = \sum_j |a_j|^{p_\theta / p(z)} \frac{a_j}{|a_j|} \chi_{A_j}(x), \quad
g_z(y) = \sum_k |b_k|^{q_\theta' / q'(z)} \frac{b_k}{|b_k|} \chi_{B_k}(y).
$$

（当 $a_j = 0$ 或 $b_k = 0$ 时相应项为零。）

**步骤 3**：验证边界条件。在 $\operatorname{Re} z = 0$ 上，$p(0) = p_0$，$q'(0) = q_0'$，且

$$
\|f_{it}\|_{p_0} = \left( \sum_j |a_j|^{p_\theta} \right)^{1/p_0} = \|f\|_{p_\theta}^{p_\theta/p_0} = 1,
$$
$$
\|g_{it}\|_{q_0'} = \left( \sum_k |b_k|^{q_\theta'} \right)^{1/q_0'} = \|g\|_{q_\theta'}^{q_\theta'/q_0'} = 1.
$$

类似地，在 $\operatorname{Re} z = 1$ 上，$\|f_{1+it}\|_{p_1} = 1$，$\|g_{1+it}\|_{q_1'} = 1$。

**步骤 4**：定义解析函数。令

$$
F(z) = \int_Y (T f_z) g_z \, d\nu.
$$

可以验证 $F(z)$ 是带形区域 $0 \le \operatorname{Re} z \le 1$ 上的有界解析函数。

**步骤 5**：应用三线定理。三线定理（Phragmén-Lindelöf 原理）断言：若 $F$ 在带形区域 $0 \le \operatorname{Re} z \le 1$ 上解析有界，则

$$
\log |F(z)| \le (1 - \operatorname{Re} z) \sup_{t \in \mathbb{R}} \log |F(it)| + \operatorname{Re} z \sup_{t \in \mathbb{R}} \log |F(1+it)|.
$$

在边界上，由 $T$ 的有界性，

$$
|F(it)| \le \|T f_{it}\|_{q_0} \|g_{it}\|_{q_0'} \le M_0 \|f_{it}\|_{p_0} \|g_{it}\|_{q_0'} = M_0,
$$
$$
|F(1+it)| \le \|T f_{1+it}\|_{q_1} \|g_{1+it}\|_{q_1'} \le M_1 \|f_{1+it}\|_{p_1} \|g_{1+it}\|_{q_1'} = M_1.
$$

**步骤 6**：插值。由三线定理，对 $z = \theta$，

$$
|F(\theta)| \le M_0^{1-\theta} M_1^\theta.
$$

但 $F(\theta) = \int (T f) g \, d\nu$，且 $\|f\|_{p_\theta} = \|g\|_{q_\theta'} = 1$，故

$$
\left| \int (T f) g \, d\nu \right| \le M_0^{1-\theta} M_1^\theta.
$$

对 $g$ 取上确界得 $\|T f\|_{q_\theta} \le M_0^{1-\theta} M_1^\theta \|f\|_{p_\theta}$。$\square$

**应用——Hausdorff-Young 不等式**：Fourier 变换 $\mathcal{F}: L^p(\mathbb{R}^n) \to L^{p'}(\mathbb{R}^n)$ 有界，其中 $1 \le p \le 2$，$1/p + 1/p' = 1$。这由 $\mathcal{F}: L^1 \to L^\infty$ 有界和 $\mathcal{F}: L^2 \to L^2$ 有界通过 Riesz-Thorin 插值得到。