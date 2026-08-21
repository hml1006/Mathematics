# Littlewood-Paley 分解理论

> **一句话大白话**：把一个函数的频率"切成一个个频带箱子"（每一档频率窗口），再单独看每箱的规范，全部加起来就等于原函数的整体大小——把复杂信号拆成"按频段的一段段"来逐个控制，统一在 S≥全 S。
>
> **小例子**：$\|f\|_{L^p}\approx(\sum_j\|\Delta_j f\|_{L^p}^2)^{1/2}$（$1<p<\infty$），其中 $\Delta_j$ 把频率锁进区间 $[2^j,2^{j+1}]$；"分段看频带再合并比较整体范数"，是估值、奇异积分与函数空间（Besov/Triebel-Lizorkin）的通用杠杆。

## 一、定理介绍

> **前置依赖**：Fourier 变换与逆变换、Plancherel 定理、单位分解（光滑截断函数）、Calderón-Zygmund 向量值奇异积分理论、Young 卷积不等式

Littlewood-Paley 分解理论是现代调和分析中最重要的工具之一，它提供了一种将函数按频率尺度进行分解的方法。其核心思想是：任何一个 $L^2$ 函数可以分解为一系列频率局部化的分量之和，每个分量只包含某个倍频程（dyadic band）内的频率信息，而这些分量的 $L^p$ 范数与原函数的 $L^p$ 范数之间存在等价关系。

Littlewood-Paley 理论最初由 Littlewood 和 Paley 在 1930 年代提出，后经 Marcinkiewicz、Zygmund、Stein 等人发展完善。它不仅是调和分析的基础工具，还在偏微分方程（特别是非线性 PDE 的先验估计）、函数空间理论（Besov 空间、Triebel-Lizorkin 空间的定义）和信号处理（小波分析的前身）中发挥着核心作用。

## 二、原理思路

**频率分解的直觉**：一个函数 $f$ 可以看作由不同频率的成分叠加而成。Littlewood-Paley 分解将频率空间 $\mathbb{R}^n$ 分成一系列环形区域（annuli）：
$$\mathbb{R}^n = B(0,1) \cup \bigcup_{j=0}^{\infty} \{2^j \le |\xi| < 2^{j+1}\}.$$

选取光滑的截断函数 $\varphi_0(\xi)$（支在 $|\xi| \le 2$ 上）和 $\varphi(\xi)$（支在 $1/2 \le |\xi| \le 2$ 上），使得
$$\varphi_0(\xi) + \sum_{j=0}^{\infty} \varphi(2^{-j}\xi) = 1, \quad \forall \xi \in \mathbb{R}^n.$$

定义频率投影算子：
$$\Delta_{-1}f = \mathcal{F}^{-1}[\varphi_0 \hat{f}], \quad \Delta_j f = \mathcal{F}^{-1}[\varphi(2^{-j}\cdot)\hat{f}], \quad j \ge 0.$$

则 $f = \sum_{j=-1}^{\infty} \Delta_j f$（在适当的函数空间中收敛）。

**核心定理的直觉**：Littlewood-Paley 定理断言，对 $1 < p < \infty$，
$$\|f\|_{L^p} \sim \left\|\left(\sum_{j=-1}^{\infty} |\Delta_j f|^2\right)^{1/2}\right\|_{L^p}.$$

这就是说，函数 $f$ 的 $L^p$ 范数等价于其各频率分量的"平方和函数"的 $L^p$ 范数。当 $p = 2$ 时，由 Plancherel 定理和频率支集几乎不交，这是显然的。对 $p \ne 2$，这非平凡——因为不同频率分量之间可能有复杂的相互作用。

**证明策略**：
1. $p = 2$ 时由 Plancherel 定理直接得到。
2. 利用 Calderón-Zygmund 奇异积分理论（或向量值极大函数不等式）将 $p = 2$ 的结果推广到 $1 < p < \infty$。
3. 关键工具是 Littlewood-Paley $g$-函数和 $g_\lambda^*$-函数的估计。

## 三、定理的严格表述

**定理（Littlewood-Paley 分解）**：选取 $\varphi_0 \in C_c^\infty(\mathbb{R}^n)$ 为径向函数，满足 $\varphi_0(\xi) = 1$ 当 $|\xi| \le 1$，$\text{supp}\,\varphi_0 \subset \{|\xi| \le 2\}$。令 $\varphi(\xi) = \varphi_0(\xi) - \varphi_0(2\xi)$，则 $\text{supp}\,\varphi \subset \{1/2 \le |\xi| \le 2\}$，且
$$\varphi_0(\xi) + \sum_{j=0}^{\infty} \varphi(2^{-j}\xi) = 1, \quad \forall \xi \in \mathbb{R}^n.$$

定义 Littlewood-Paley 投影 $\Delta_j f = \mathcal{F}^{-1}[\varphi(2^{-j}\cdot)\hat{f}]$（$j \ge 0$），$\Delta_{-1}f = \mathcal{F}^{-1}[\varphi_0 \hat{f}]$，以及低频截断 $S_j f = \sum_{k=-1}^{j-1} \Delta_k f$。

则以下结论成立：

**(1) 分解恒等式**：对 $f \in \mathcal{S}'(\mathbb{R}^n)$（ tempered distributions），
$$f = \sum_{j=-1}^{\infty} \Delta_j f \quad (\text{在 } \mathcal{S}' \text{ 中收敛}).$$

**(2) Littlewood-Paley 不等式**：对 $1 < p < \infty$，存在常数 $C_p > 0$ 使得对任意 $f \in L^p(\mathbb{R}^n)$，
$$C_p^{-1}\|f\|_{L^p} \le \left\|\left(\sum_{j=-1}^{\infty} |\Delta_j f(\cdot)|^2\right)^{1/2}\right\|_{L^p} \le C_p \|f\|_{L^p}.$$

**(3) 几乎正交性**：$\Delta_j \Delta_k = 0$ 当 $|j - k| \ge 2$（因为频率支集不交）。

**(4) Bernstein 不等式**：对任意多重指标 $\alpha$ 和 $1 \le p \le q \le \infty$，
$$\|\partial^\alpha \Delta_j f\|_{L^q} \le C 2^{j(|\alpha| + n/p - n/q)} \|f\|_{L^p}.$$

## 四、证明过程

**$p = 2$ 的情形**：

由 Plancherel 定理，
$$\|\Delta_j f\|_2^2 = \int_{\mathbb{R}^n} |\varphi(2^{-j}\xi)|^2 |\hat{f}(\xi)|^2\, d\xi.$$

由于 $\varphi_0(\xi)^2 + \sum_{j=0}^{\infty} \varphi(2^{-j}\xi)^2 = 1$（适当选取 $\varphi_0, \varphi$ 可使此式成立），
$$\sum_{j=-1}^{\infty} |\Delta_j f(x)|^2$$
的 $L^1$ 范数等于
$$\int_{\mathbb{R}^n} \left(\varphi_0(\xi)^2 + \sum_{j=0}^{\infty} \varphi(2^{-j}\xi)^2\right)|\hat{f}(\xi)|^2\, d\xi = \|f\|_2^2.$$

由 Fubini 定理，
$$\left\|\left(\sum_j |\Delta_j f|^2\right)^{1/2}\right\|_{L^2}^2 = \sum_j \|\Delta_j f\|_2^2 = \|f\|_2^2.$$

**$1 < p < \infty$ 的情形（利用 Calderón-Zygmund 理论）**：

定义 Littlewood-Paley $g$-函数：
$$g(f)(x) = \left(\sum_{j=-1}^{\infty} |\Delta_j f(x)|^2\right)^{1/2} = \left(\int_0^\infty |\psi_t * f(x)|^2 \frac{dt}{t}\right)^{1/2},$$
其中 $\psi_t(x) = t^{-n}\psi(x/t)$，$\hat{\psi}$ 支在某个环形区域内。

$g$-函数可以写成向量值奇异积分算子的形式：定义算子 $\vec{T}f(x) = \{\psi_{2^{-j}} * f(x)\}_{j}$，取值于 $\ell^2$。核 $\vec{K}(x) = \{\psi_{2^{-j}}(x)\}_j$ 满足 Calderón-Zygmund 核的向量值版本的条件：
- $|\vec{K}(x)|_{\ell^2} \le C/|x|^n$；
- $|\nabla \vec{K}(x)|_{\ell^2} \le C/|x|^{n+1}$。

由向量值 Calderón-Zygmund 理论，$\vec{T}$ 在 $L^2(\mathbb{R}^n; \ell^2)$ 上有界（由 Plancherel），因此由 Calderón-Zygmund 定理的向量值推广，$\vec{T}$ 在 $L^p(\mathbb{R}^n; \ell^2)$ 上有界，$1 < p < \infty$。这给出
$$\|g(f)\|_{L^p} = \|\vec{T}f\|_{L^p(\ell^2)} \le C_p \|f\|_{L^p}.$$

反向不等式通过类似的对偶论证或 $T^*T$ 方法得到。$\square$

**Bernstein 不等式的证明**：

$\Delta_j f$ 的频率支在 $\{2^{j-1} \le |\xi| \le 2^{j+1}\}$ 中。设 $\Phi_j = \mathcal{F}^{-1}[\varphi(2^{-j}\cdot)]$，则 $\Delta_j f = \Phi_j * f$，其中 $\Phi_j(x) = 2^{jn}\Phi(2^j x)$。

对 $|\alpha|$ 阶导数：$\partial^\alpha \Phi_j(x) = 2^{j(|\alpha|+n)}(\partial^\alpha \Phi)(2^j x)$，故 $\|\partial^\alpha \Phi_j\|_{L^1} = 2^{j|\alpha|}\|\partial^\alpha \Phi\|_{L^1}$。

由 Young 不等式：
$$\|\partial^\alpha \Delta_j f\|_{L^p} \le \|\partial^\alpha \Phi_j\|_{L^1} \|f\|_{L^p} = C 2^{j|\alpha|}\|f\|_{L^p}.$$

结合频率局部化带来的 $L^p \to L^q$ 改善（通过 $\Phi_j$ 的 $L^r$ 范数），得到完整的 Bernstein 不等式。$\square$

## 五、应用与意义

1. **Besov 空间与 Triebel-Lizorkin 空间**：Littlewood-Paley 分解是定义这些函数空间的基本工具。Besov 空间 $B^s_{p,q}$ 定义为
$$\|f\|_{B^s_{p,q}} = \left(\sum_{j=-1}^{\infty} (2^{js}\|\Delta_j f\|_{L^p})^q\right)^{1/q} < \infty.$$
当 $p = q = 2$ 时，$B^s_{2,2} = H^s$（Sobolev 空间）。

2. **非线性 PDE**：在 Navier-Stokes 方程、Euler 方程、非线性 Schrödinger 方程等的研究中，Littlewood-Paley 分解使得可以在不同频率尺度上分别估计非线性项，是现代 PDE 理论的标准工具。

3. **乘积估计与 Bony 抛物化**：Bony 利用 Littlewood-Paley 分解引入了抛物化（paraproduct）方法，将两个函数的乘积分解为
$$fg = T_f g + T_g f + R(f,g),$$
其中 $T_f g = \sum_j S_{j-1}f \cdot \Delta_j g$ 是抛物化项，$R(f,g)$ 是余项。这一分解在乘积的低正则性估计中至关重要。

4. **小波分析的数学基础**：Littlewood-Paley 分解可以看作连续频率分解的离散版本，它是小波多分辨率分析的理论先驱。

5. **Strichartz 估计**：在色散方程中，Littlewood-Paley 分解结合频率局部化的色散估计，通过平方和技巧得到全局的 Strichartz 估计。
