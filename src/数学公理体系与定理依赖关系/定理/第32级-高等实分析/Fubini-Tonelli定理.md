# Fubini-Tonelli定理

> **一句话大白话**：多元积分可以"一层一层地算"——先后对 $y$ 求再对 $x$ 求，或者调换次序，结果都一个样；只要函数不取负号或积分绝对收敛，先算哪层都行。
>
> **小例子**：$\int_0^1\int_0^1 x^2 y\,dx\,dy$ 先积 $x$ 或先积 $y$ 都得出同一数值 $\frac16$；Tonelli说非负情形必然如此，Fubini则放宽到"绝对可积"的符号可变情形。

## 介绍

Fubini-Tonelli定理是测度论和积分理论中最重要的定理之一，它将多重积分的计算转化为累次积分。Tonelli 定理（正函数版本）断言：非负可测函数的累次积分可以交换次序，结果等于乘积空间上的积分。Fubini 定理（可积函数版本）断言：若乘积空间上的函数可积，则其累次积分存在且相等。这两个定理合在一起，为重积分和累次积分的互换提供了严谨的理论依据，是概率论、偏微分方程和调和分析中不可或缺的工具。

## 分析

**定理的精确表述**：设 $(X, \mathcal{M}, \mu)$ 和 $(Y, \mathcal{N}, \nu)$ 是 $\sigma$-有限测度空间，$(X \times Y, \mathcal{M} \otimes \mathcal{N}, \mu \times \nu)$ 是乘积测度空间。

**Tonelli 定理（非负函数）**：若 $f: X \times Y \to [0, \infty]$ 是 $\mathcal{M} \otimes \mathcal{N}$-可测函数，则：
1. 对每个 $x \in X$，$y \mapsto f(x, y)$ 是 $\mathcal{N}$-可测的；
2. 对每个 $y \in Y$，$x \mapsto f(x, y)$ 是 $\mathcal{M}$-可测的；
3. $x \mapsto \int_Y f(x, y) \, d\nu(y)$ 是 $\mathcal{M}$-可测的；
4. $y \mapsto \int_X f(x, y) \, d\mu(x)$ 是 $\mathcal{N}$-可测的；
5. 累次积分相等：

$$
\int_X \int_Y f(x, y) \, d\nu(y) \, d\mu(x) = \int_Y \int_X f(x, y) \, d\mu(x) \, d\nu(y) = \int_{X \times Y} f \, d(\mu \times \nu).
$$

**Fubini 定理（可积函数）**：若 $f: X \times Y \to \mathbb{R}$（或 $\mathbb{C}$）是 $\mu \times \nu$-可积的（即 $\int_{X \times Y} |f| \, d(\mu \times \nu) < \infty$），则：
1. 对 $\mu$-几乎每个 $x$，$y \mapsto f(x, y)$ 是 $\nu$-可积的；
2. 对 $\nu$-几乎每个 $y$，$x \mapsto f(x, y)$ 是 $\mu$-可积的；
3. $x \mapsto \int_Y f(x, y) \, d\nu(y)$ 是 $\mu$-可积的（在 $\mu$-几乎处处定义的意义下）；
4. 累次积分等于重积分，如 Tonelli 定理中的等式所示。

**关键要点**：

- Tonelli 定理不要求可积性，只要求可测性和非负性——即使积分值为无穷，等式仍然成立。
- Fubini 定理要求绝对可积性，这是保证累次积分存在且相等的充分条件。
- $\sigma$-有限条件是本质的——在非 $\sigma$-有限测度空间中，Fubini 定理可能失效。
- 截面可测性（$f(x, \cdot)$ 和 $f(\cdot, y)$ 的可测性）是乘积可测函数的自然性质。

## 思考过程

Fubini-Tonelli 定理的证明基于单调类定理和简单函数逼近：

1. **从特征函数开始**：首先对 $f = \chi_{A \times B}$ 验证结论成立，此时重积分等于 $\mu(A)\nu(B)$，累次积分也等于 $\mu(A)\nu(B)$。

2. **推广到可测矩形**：利用单调类定理，将结论推广到 $\mathcal{M} \otimes \mathcal{N}$ 上的任意可测集的特征函数。

3. **推广到简单函数**：由线性性，结论对非负简单函数成立。

4. **Tonelli 定理**：对非负可测函数 $f$，取简单函数列 $f_n \uparrow f$，利用单调收敛定理。

5. **Fubini 定理**：对可积函数 $f$，分解为 $f = f^+ - f^-$，分别应用 Tonelli 定理。

## 证明过程

**证明**：我们给出乘积测度的构造和 Fubini-Tonelli 定理的证明概要。

**步骤 1**：乘积测度的构造。定义 $\pi$-系 $\mathcal{P} = \{A \times B \mid A \in \mathcal{M}, B \in \mathcal{N}\}$。对 $E \in \sigma(\mathcal{P}) = \mathcal{M} \otimes \mathcal{N}$，定义截面

$$
E_x = \{y \in Y \mid (x, y) \in E\}, \quad E^y = \{x \in X \mid (x, y) \in E\}.
$$

可以证明 $E_x \in \mathcal{N}$，$E^y \in \mathcal{M}$。定义 $\lambda(E) = \int_X \nu(E_x) \, d\mu(x) = \int_Y \mu(E^y) \, d\nu(y)$，则 $\lambda$ 是 $\mathcal{M} \otimes \mathcal{N}$ 上的测度，称为乘积测度 $\mu \times \nu$。

**步骤 2**：Tonelli 定理——特征函数情形。对 $f = \chi_E$（$E \in \mathcal{M} \otimes \mathcal{N}$），由乘积测度的定义，$\int_{X \times Y} \chi_E \, d(\mu \times \nu) = (\mu \times \nu)(E) = \int_X \nu(E_x) \, d\mu(x) = \int_X \int_Y \chi_E(x, y) \, d\nu(y) \, d\mu(x)$。类似地可得另一个次序的累次积分。

**步骤 3**：Tonelli 定理——非负简单函数。由线性性，结论对非负简单函数成立。

**步骤 4**：Tonelli 定理——非负可测函数。设 $f \ge 0$ 可测，取非负简单函数列 $f_n \uparrow f$。对每个 $f_n$ 应用步骤 3，然后由单调收敛定理：

$$
\int_{X \times Y} f \, d(\mu \times \nu) = \lim_{n \to \infty} \int_{X \times Y} f_n \, d(\mu \times \nu) = \lim_{n \to \infty} \int_X \int_Y f_n(x, y) \, d\nu(y) \, d\mu(x).
$$

由于 $\int_Y f_n(x, y) \, d\nu(y) \uparrow \int_Y f(x, y) \, d\nu(y)$（对每个 $x$，由单调收敛定理），再次应用单调收敛定理得

$$
\int_X \int_Y f(x, y) \, d\nu(y) \, d\mu(x) = \lim_{n \to \infty} \int_X \int_Y f_n(x, y) \, d\nu(y) \, d\mu(x) = \int_{X \times Y} f \, d(\mu \times \nu).
$$

**步骤 5**：Fubini 定理。设 $f \in L^1(\mu \times \nu)$，则 $|f|$ 满足 Tonelli 定理的条件，故

$$
\int_{X \times Y} |f| \, d(\mu \times \nu) = \int_X \int_Y |f(x, y)| \, d\nu(y) \, d\mu(x) < \infty.
$$

因此对 $\mu$-几乎每个 $x$，$\int_Y |f(x, y)| \, d\nu(y) < \infty$，即 $f(x, \cdot)$ 是 $\nu$-可积的。对 $f = f^+ - f^-$ 分别应用 Tonelli 定理即得结论。$\square$

**应用**：Fubini-Tonelli 定理在概率论中用于计算期望的迭代（$\mathbb{E}[X] = \mathbb{E}[\mathbb{E}[X \mid Y]]$），在调和分析中用于处理卷积 $f * g$ 的积分，在偏微分方程中用于交换积分和微分算子。