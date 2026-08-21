# Fourier 变换的 $L^2$ 理论（Plancherel 定理）

> **一句话大白话**：在"平方可积"这个空间里，傅里叶变换是一个"保长度的等距映射"——时域的能量和频域的能量完全相等，于是傅里叶变换在这里可逆，几乎像一个完美的"时针 ↔ 频率"坐标切换。
>
> **小例子**：Plancherel 定理说 $\int |f|^2\,dx=\int|\hat f(\xi)|^2\,d\xi$（严格到归一化因子），且有 $\mathcal{F}f=\lim$ 意义下的等距延拓——把信号变换到频域不减不增能量，反过来也能还原。

## 一、定理介绍

> **前置依赖**：$L^1$ 上的 Fourier 变换与逆变换、Schwartz 空间及其稠密性、卷积运算与控制收敛定理、Hilbert 空间等距算子的稠密延拓、极化恒等式

Fourier 变换最初在 $L^1(\mathbb{R}^n)$ 上通过积分
$$\hat{f}(\xi) = \int_{\mathbb{R}^n} f(x) e^{-2\pi i x \cdot \xi}\, dx$$
定义，但 $L^1$ 上的 Fourier 变换理论存在局限：$L^1$ 不是自反空间，Fourier 变换的像空间描述不简洁。Plancherel 定理的核心贡献在于将 Fourier 变换延拓到 $L^2(\mathbb{R}^n)$ 上，并证明它是 $L^2$ 到自身的等距同构（差一个常数因子）。这一结果奠定了 $L^2$ 上调和分析的基础，使得 Fourier 变换成为 Hilbert 空间上的酉算子，从而可以运用正交分解、谱理论等强大工具。

Plancherel 定理是连接经典 Fourier 分析与现代泛函分析的桥梁，在量子力学（位置-动量对偶）、偏微分方程（Sobolev 空间的 Fourier 刻画）、信号处理（Parseval 恒等式）等领域都有根本性的应用。

## 二、原理思路

**核心困难**：$L^2(\mathbb{R}^n)$ 中的函数未必属于 $L^1(\mathbb{R}^n)$，因此 Fourier 变换的积分定义对一般的 $L^2$ 函数没有意义。

**解决策略——稠密延拓法**：

1. **在稠密子集上定义**：$L^1 \cap L^2$ 在 $L^2$ 中稠密，而 $L^1 \cap L^2$ 中的函数 Fourier 变换有良好定义。
2. **在稠密子集上建立等式**：对 $f \in L^1 \cap L^2$，证明 $\|\hat{f}\|_2 = \|f\|_2$（Plancherel 等式）。这可以通过先对 Gauss 函数验证，再利用卷积逼近来完成。
3. **连续延拓**：等距映射在稠密子集上一致连续，因此可以唯一地连续延拓到整个 $L^2$ 空间。
4. **证明满射**：利用 Fourier 逆变换在 Schwartz 空间 $\mathcal{S}$ 上的已知结果，结合 $\mathcal{S}$ 在 $L^2$ 中的稠密性，证明延拓后的 Fourier 变换是满射。

**关键洞察**：Fourier 变换在 $L^2$ 上的本质是一个 Hilbert 空间的等距算子，由泛函分析中等距算子在完备空间上的延拓理论保证了一切良好性质。

## 三、定理的严格表述

**定理（Plancherel 定理）**：设 $f \in L^2(\mathbb{R}^n)$。则存在唯一的函数 $\hat{f} \in L^2(\mathbb{R}^n)$，使得对任意 $g \in L^1(\mathbb{R}^n) \cap L^2(\mathbb{R}^n)$，当 $f = g$ 几乎处处时，$\hat{f}$ 与经典 Fourier 变换 $\hat{g}(\xi) = \int_{\mathbb{R}^n} g(x) e^{-2\pi i x \cdot \xi}\, dx$ 一致。并且：

**(1) Plancherel 等式（$L^2$ 等距性）**：
$$\|\hat{f}\|_{L^2(\mathbb{R}^n)} = \|f\|_{L^2(\mathbb{R}^n)}, \quad \forall f \in L^2(\mathbb{R}^n).$$

即
$$\int_{\mathbb{R}^n} |\hat{f}(\xi)|^2\, d\xi = \int_{\mathbb{R}^n} |f(x)|^2\, dx.$$

**(2) Parseval 等式（内积保持）**：对任意 $f, g \in L^2(\mathbb{R}^n)$，
$$\langle \hat{f}, \hat{g} \rangle_{L^2} = \langle f, g \rangle_{L^2},$$

即
$$\int_{\mathbb{R}^n} \hat{f}(\xi) \overline{\hat{g}(\xi)}\, d\xi = \int_{\mathbb{R}^n} f(x) \overline{g(x)}\, dx.$$

**(3) Fourier 逆变换**：映射 $\mathcal{F}: L^2(\mathbb{R}^n) \to L^2(\mathbb{R}^n)$，$f \mapsto \hat{f}$ 是 $L^2(\mathbb{R}^n)$ 上的酉算子，其逆算子为
$$\mathcal{F}^{-1}g(x) = \int_{\mathbb{R}^n} g(\xi) e^{2\pi i x \cdot \xi}\, d\xi \quad (\text{在 } L^2 \text{ 极限意义下}).$$

## 四、证明过程

**第一步：在 $L^1 \cap L^2$ 上建立 Plancherel 等式。**

设 $f \in L^1(\mathbb{R}^n) \cap L^2(\mathbb{R}^n)$。定义截断函数 $f_R(x) = f(x) \cdot \chi_{B(0,R)}(x)$，则 $f_R \in L^1(\mathbb{R}^n)$ 且 $f_R \to f$ 于 $L^2$ 中（由控制收敛定理）。

考虑卷积 $f_R * \tilde{f}_R$，其中 $\tilde{f}_R(x) = \overline{f_R(-x)}$。由 Fourier 变换的性质：
$$\widehat{f_R * \tilde{f}_R}(\xi) = \hat{f}_R(\xi) \cdot \overline{\hat{f}_R(\xi)} = |\hat{f}_R(\xi)|^2.$$

由于 $f_R * \tilde{f}_R \in L^1(\mathbb{R}^n)$ 且连续，利用 Fourier 逆变换在零点取值：
$$(f_R * \tilde{f}_R)(0) = \int_{\mathbb{R}^n} |\hat{f}_R(\xi)|^2\, d\xi.$$

另一方面，直接计算：
$$(f_R * \tilde{f}_R)(0) = \int_{\mathbb{R}^n} f_R(y) \overline{f_R(y)}\, dy = \int_{\mathbb{R}^n} |f_R(x)|^2\, dx.$$

因此
$$\int_{\mathbb{R}^n} |\hat{f}_R(\xi)|^2\, d\xi = \int_{\mathbb{R}^n} |f_R(x)|^2\, dx.$$

令 $R \to \infty$。由于 $f_R \to f$ 于 $L^2$ 中，右边趋于 $\|f\|_2^2$。由 Fourier 变换在 $L^1$ 上的有界性，$\hat{f}_R \to \hat{f}$ 一致收敛，结合单调收敛可得左边趋于 $\|\hat{f}\|_2^2$。因此
$$\|\hat{f}\|_2 = \|f\|_2, \quad \forall f \in L^1 \cap L^2.$$

**第二步：连续延拓到 $L^2$。**

$L^1 \cap L^2$ 在 $L^2$ 中稠密（因为 $C_c^\infty(\mathbb{R}^n) \subset L^1 \cap L^2$ 且 $C_c^\infty$ 在 $L^2$ 中稠密）。映射 $\mathcal{F}: L^1 \cap L^2 \to L^2$ 是等距的，因此一致连续。由完备度量空间的连续延拓定理，$\mathcal{F}$ 可以唯一地延拓为 $\tilde{\mathcal{F}}: L^2(\mathbb{R}^n) \to L^2(\mathbb{R}^n)$，且延拓后仍保持等距性：
$$\|\tilde{\mathcal{F}}f\|_2 = \|f\|_2, \quad \forall f \in L^2(\mathbb{R}^n).$$

**第三步：证明满射性。**

Schwartz 空间 $\mathcal{S}(\mathbb{R}^n)$ 在 $L^2$ 中稠密，且 Fourier 变换 $\mathcal{F}: \mathcal{S} \to \mathcal{S}$ 是双射（经典结果），其逆变换为 $\mathcal{F}^{-1}g(x) = \int g(\xi) e^{2\pi i x \cdot \xi}\, d\xi$。

对任意 $g \in L^2$，取 $\{g_k\} \subset \mathcal{S}$ 使得 $g_k \to g$ 于 $L^2$ 中。令 $f_k = \mathcal{F}^{-1}g_k \in \mathcal{S}$。由 Plancherel 等式（在 $\mathcal{S}$ 上已成立），$\{f_k\}$ 是 $L^2$ 中的 Cauchy 列，因此 $f_k \to f$ 于 $L^2$ 中某处。由延拓的连续性，$\tilde{\mathcal{F}}f = g$。故 $\tilde{\mathcal{F}}$ 是满射。

**第四步：Parseval 等式。**

由极化恒等式
$$\langle f, g \rangle = \frac{1}{4}\sum_{k=0}^3 i^k \|f + i^k g\|_2^2$$
和 $\tilde{\mathcal{F}}$ 的线性及等距性，立即得到内积保持性。$\square$

## 五、应用与意义

1. **Sobolev 空间的 Fourier 刻画**：利用 Plancherel 定理，Sobolev 空间 $H^s(\mathbb{R}^n)$ 可以定义为
$$H^s(\mathbb{R}^n) = \{f \in L^2 : (1+|\xi|^2)^{s/2}\hat{f}(\xi) \in L^2\},$$
这为偏微分方程的正则性研究提供了基本工具。

2. **量子力学**：在量子力学中，Plancherel 定理保证了位置表象和动量表象之间的等价性。Heisenberg 不确定性原理的严格证明直接依赖于 Parseval 等式。

3. **信号处理**：Parseval 等式表明信号的时域能量等于频域能量，这是功率谱分析的数学基础。

4. **算子理论的基石**：Fourier 变换作为 $L^2$ 上的酉算子，使得卷积算子、微分算子等在 Fourier 侧变为乘法算子，极大地简化了算子分析。

5. **进一步发展的基础**：Plancherel 定理是建立 Fourier 乘子理论、Littlewood-Paley 理论、奇异积分理论等现代调和分析核心工具的出发点。
