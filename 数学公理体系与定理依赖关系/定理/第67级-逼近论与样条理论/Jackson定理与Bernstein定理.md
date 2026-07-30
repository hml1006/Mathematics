# Jackson 定理与 Bernstein 定理

## 一、定理介绍

Jackson 定理与 Bernstein 定理是函数逼近论中刻画**逼近速度**与**函数光滑性**之间关系的两个核心结果。

- **Jackson 定理**：函数越光滑（具有更高的连续模或可微性），用代数多项式或三角多项式逼近的收敛速度就越快。它给出了最佳逼近误差 $E_n(f)$ 从上方控制的光滑性估计。

- **Bernstein 定理**：反过来，如果最佳逼近误差以一定速度衰减，则可以推断函数具有一定的光滑性。它给出了最佳逼近误差从下方控制的光滑性反推。

二者共同构成了逼近论中的"直接定理与逆定理"体系，是函数空间插值理论与逼近论之间的桥梁。

## 二、原理思路

**Jackson 定理的思路**：通过构造具体的逼近算子（如 Jackson 积分算子、卷积算子），利用函数的光滑性信息（连续性模、导数阶数）来估计逼近误差。光滑性越高，构造的积分核越能抵消高频分量，从而衰减更快。

**Bernstein 定理的思路**：若 $E_n(f)$ 快速衰减，则可以通过将 $f$ 分解为级数
$$
f = P_0 + \sum_{k=1}^{\infty} (P_k - P_{k-1}),
$$
其中 $P_k$ 是 $k$ 次最佳逼近多项式。由于每一项都是次数受控的多项式，且系数由 $E_k(f)$ 控制，从而可以估计 $f$ 的连续模或导数。

## 三、定理的严格表述

### 1. Jackson 定理

设 $f \in C[-\pi,\pi]$ 且 $2\pi$ 周期，$\omega(f,\delta)$ 为其连续模：
$$
\omega(f,\delta) = \sup_{|h| \leq \delta} \|f(\cdot + h) - f(\cdot)\|_\infty.
$$

记 $E_n^T(f)$ 为 $f$ 用次数不超过 $n$ 的三角多项式的最佳一致逼近误差。

**定理（Jackson 第一定理）**：存在仅依赖于阶数的常数 $C$，使得
$$
E_n^T(f) \leq C \, \omega\left(f, \frac{1}{n}\right), \quad n \geq 1.
$$

**定理（Jackson 第二定理）**：若 $f \in C^r[-\pi,\pi]$ 且 $r$ 阶导数 $f^{(r)}$ 连续，则
$$
E_n^T(f) \leq \frac{C_r}{n^r} \, \omega\left(f^{(r)}, \frac{1}{n}\right), \quad n \geq 1,
$$
其中 $C_r$ 是仅依赖于 $r$ 的常数。

特别地，若 $f \in C^r$ 且 $f^{(r)}$ 满足 $\alpha$ 阶 Lipschitz 条件（$0 < \alpha \leq 1$），则
$$
E_n^T(f) = O\left(\frac{1}{n^{r+\alpha}}\right).
$$

对于代数多项式在 $[-1,1]$ 上的逼近，类似结果为
$$
E_n(f) \leq C_r \, \omega\left(f^{(r)}, \frac{1}{n}\right) \left(\frac{\sqrt{1-x^2}}{n} + \frac{1}{n^2}\right)^r
$$
在逐点意义下成立。

### 2. Bernstein 定理

**定理（Bernstein 逆定理）**：设 $f \in C[-\pi,\pi]$ 为 $2\pi$ 周期函数。若对某个整数 $r \geq 0$ 和 $0 < \alpha < 1$，有
$$
E_n^T(f) = O\left(\frac{1}{n^{r+\alpha}}\right),
$$
则 $f \in C^r$ 且 $f^{(r)}$ 满足 $\alpha$ 阶 Lipschitz 条件，即 $f \in \mathrm{Lip}\, \alpha$ 在 $r=0$ 时成立。

更精确地，若
$$
\sum_{n=1}^{\infty} n^{r-1} E_n^T(f) < \infty,
$$
则 $f$ 是 $r$ 次连续可微的。

## 四、证明过程

### Jackson 定理证明概要

考虑 Jackson 核
$$
J_n(t) = \frac{1}{c_n} \left( \frac{\sin(nt/2)}{\sin(t/2)} \right)^4,
$$
其中 $c_n$ 选取使得 $\int_{-\pi}^{\pi} J_n(t) \, dt = 1$。$J_n$ 是一个非负的偶三角多项式。

定义 Jackson 算子
$$
(J_n f)(x) = \int_{-\pi}^{\pi} f(x+t) J_n(t) \, dt = \int_{-\pi}^{\pi} f(t) J_n(t-x) \, dt.
$$

由于 $J_n$ 是三角多项式，$J_n f$ 也是三角多项式。估计误差：
$$
|(J_n f)(x) - f(x)| = \left| \int_{-\pi}^{\pi} [f(x+t) - f(x)] J_n(t) \, dt \right|.
$$

利用连续模和 Jackson 核的矩估计：
$$
\int_{-\pi}^{\pi} |t|^k J_n(t) \, dt \leq C_k \left(\frac{1}{n}\right)^k,
$$
可得
$$
\|J_n f - f\|_\infty \leq C \, \omega\left(f, \frac{1}{n}\right).
$$

由于 $E_n^T(f) \leq \|J_n f - f\|_\infty$，Jackson 第一定理得证。

对于 $C^r$ 函数，利用关系
$$
\omega(f,\delta) \leq \delta \|f'\|_\infty
$$
以及逐阶逼近即可得到高阶 Jackson 估计。

### Bernstein 定理证明概要

取 $P_n \in \mathcal{T}_n$（次数不超过 $n$ 的三角多项式）使得
$$
\|f - P_n\|_\infty \leq 2 E_n^T(f).
$$

令 $Q_0 = P_1$，$Q_k = P_{2^k} - P_{2^{k-1}}$（$k \geq 1$），则
$$
f = P_1 + \sum_{k=1}^{\infty} Q_k.
$$

$Q_k$ 是次数不超过 $2^k$ 的三角多项式，且
$$
\|Q_k\|_\infty \leq \|f - P_{2^k}\|_\infty + \|f - P_{2^{k-1}}\|_\infty \leq C E_{2^{k-1}}^T(f).
$$

利用 Bernstein 关于三角多项式导数的不等式：若 $T$ 是次数不超过 $n$ 的三角多项式，则
$$
\|T'\|_\infty \leq n \|T\|_\infty,
$$
可得
$$
\|Q_k'\|_\infty \leq 2^k \|Q_k\|_\infty \leq C 2^k E_{2^{k-1}}^T(f).
$$

若 $E_n^T(f) = O(n^{-(1+\alpha)})$，则
$$
\sum_{k=1}^{\infty} \|Q_k'\|_\infty < \infty,
$$
故 $f' = \sum Q_k'$ 一致收敛，且可证 $f' \in \mathrm{Lip}\, \alpha$。高阶情形类似。

**证毕**。

## 五、应用与意义

1. **函数空间刻画**：Jackson-Bernstein 定理对将函数按光滑性分类（如 Hölder 空间、Sobolev 空间）具有核心意义。它们说明最佳逼近误差衰减率等价于函数的正则性。

2. **谱方法收敛性分析**：在谱方法和有限元方法中，Jackson 型估计用于证明当解足够光滑时，数值方法以代数甚至指数速度收敛。

3. **图像与信号处理**：小波、Fourier 逼近中的压缩效率与信号光滑性直接相关，Jackson-Bernstein 思想为压缩感知、图像去噪提供了理论框架。

4. **机器学习理论**：在逼近论与统计学习交叉领域，函数的逼近误差与光滑性的关系影响神经网络、核方法的样本复杂度与泛化能力。

5. **插值与拟合**：理解逼近速度有助于在实际应用中合理选择多项式次数、样条节点数目，以平衡计算成本与精度。
