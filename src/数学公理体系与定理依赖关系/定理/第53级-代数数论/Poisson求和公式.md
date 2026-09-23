# Poisson 求和公式

> **一句话大白话**：把函数在所有整数点上的取值加起来，得到的和等于把它的傅里叶变换在所有整数点上的取值加起来——"实数上的周期化和"与"频率上的周期化和"是同一回事。
>
> **小例子**：取 $f(x)=e^{-\pi x^2}$，其傅里叶变换不变（$\hat f=f$），于是 $\sum_n e^{-\pi n^2}$ 与自己相等固然平凡；但代入缩放的 $\theta$ 函数可得 $\theta(1/t)=\sqrt t\,\theta(t)$，这给出 $\theta$ 函数的模变换，直接推出 $\Gamma(1/2)=\sqrt\pi$、$\zeta(2)$ 的估值与椭圆函数的变换律。

## 一、定理介绍

> **前置依赖**：Fourier变换与逆变换公式、Schwartz 空间与速降性、Fourier 级数及系数衰减、Fubini 定理、周期化与过渡（Poisson 核）技巧

Poisson 求和公式（Poisson summation formula）是连接"离散求和"与"连续傅里叶分析"的桥梁，其思想可追溯到 Euler 与 Poisson 对椭圆函数的研究。公式断言：对性质良好的函数 $f$，

$$
\sum_{n\in\mathbb Z}f(n)=\sum_{n\in\mathbb Z}\hat f(n),
$$

这里 $\hat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi ix\xi}\,\mathrm dx$。它把实数轴上的"采样值求和"与频域上的"采样值求和"等同起来，是 Φ-函数、θ 函数变换、以及数论中大量恒等式的统一来源。

在数论中，Poisson 公式是推导二次互反律、Gauss 和估值、$\zeta(2k)$ 计算、以及 Riemann $\zeta$ 函数函数方程的工具之一；在调和分析中，它是抽样定理（Shannon sampling theorem）与分析学中"尖锐化"（sharpness）论证的基础。它在更高层是局部紧交换群上的 Pontryagin 对偶下 Tate 的局部函数方程的特殊情形。

## 二、原理思路

证明的思想是"先把和变成周期函数"。定义 $f$ 的**周期化**

$$
F(x)=\sum_{k\in\mathbb Z}f(x+k).
$$

若 $f$ 速降，则 $F$ 是光滑的 $1$-周期函数。对 $F$ 作 Fourier 级数展开，其第 $n$ 个 Fourier 系数为

$$
c_n=\int_0^1 F(x)e^{-2\pi inx}\,\mathrm dx=\sum_k\int_0^1 f(x+k)e^{-2\pi inx}\,\mathrm dx.
$$

对每一项作平移 $y=x+k$（此时 $e^{-2\pi inx}=e^{-2\pi in(y-k)}=e^{-2\pi iny}$，因 $e^{2\pi ink}=1$），系数便化为 $\int_{\mathbb R}f(y)e^{-2\pi iny}\,\mathrm dy=\hat f(n)$。因 $f$ 速降，$\hat f$ 也速降，故 $\sum|c_n|<\infty$，$F$ 等于其 Fourier 级数；在 $x=0$ 取值即得 $\sum_k f(k)=F(0)=\sum_n\hat f(n)$。整条思路就是"周期化 → 展开 → 平移 → 认系数"。

## 三、定理的严格表述

**（Poisson 求和公式）** 设 $f\in\mathcal S(\mathbb R)$（Schwartz 函数），取 Fourier 变换约定

$$
\hat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi ix\xi}\,\mathrm dx,
$$

则

$$
\sum_{n\in\mathbb Z}f(n)=\sum_{n\in\mathbb Z}\hat f(n),
$$

且两个级数都绝对收敛。

**多维形式**：对 $f\in\mathcal S(\mathbb R^d)$、格 $\Lambda\subset\mathbb R^d$ 及其对偶格

$$
\Lambda^*=\{\xi\in\mathbb R^d:\ \xi\cdot\lambda\in\mathbb Z,\ \forall\lambda\in\Lambda\},
$$

有

$$
\sum_{\lambda\in\Lambda}f(\lambda)=\frac{1}{\mathrm{vol}(\mathbb R^d/\Lambda)}\sum_{\mu\in\Lambda^*}\hat f(\mu).
$$

当 $\Lambda=\mathbb Z^d$ 时 $\Lambda^*=\mathbb Z^d$、体积为 $1$，即得 $\sum_{n\in\mathbb Z^d}f(n)=\sum_{n\in\mathbb Z^d}\hat f(n)$。

## 四、证明过程

**步骤 1：周期化函数的存在与光滑性。**

设 $f\in\mathcal S(\mathbb R)$。因 $|f(x+k)|\le C_N(1+|x+k|)^{-N}$，对每个固定 $x$，级数

$$
F(x)=\sum_{k\in\mathbb Z}f(x+k)
$$

绝对收敛；对 $x$ 局部一致收敛，且逐项求导仍局部一致收敛，故 $F\in C^\infty$。显然 $F(x+1)=F(x)$，即 $F$ 是 $1$-周期光滑函数。

**步骤 2：计算 Fourier 系数。**

$F$ 的 Fourier 系数

$$
c_n=\int_0^1 F(x)e^{-2\pi inx}\,\mathrm dx=\sum_{k\in\mathbb Z}\int_0^1 f(x+k)e^{-2\pi inx}\,\mathrm dx.
$$

交换求和与积分合法（绝对收敛）。对第 $k$ 项令 $y=x+k$，则 $x=y-k$，$\mathrm dx=\mathrm dy$，$e^{-2\pi inx}=e^{-2\pi iny}e^{2\pi ink}=e^{-2\pi iny}$，积分区间变为 $[k,k+1]$：

$$
c_n=\sum_{k\in\mathbb Z}\int_k^{k+1}f(y)e^{-2\pi iny}\,\mathrm dy=\int_{\mathbb R}f(y)e^{-2\pi iny}\,\mathrm dy=\hat f(n).
$$

**步骤 3：系数速降，级数绝对收敛。**

因 $f\in\mathcal S$，其傅里叶变换 $\hat f\in\mathcal S$，特别地 $|\hat f(n)|\le C_N(1+|n|)^{-N}$ 对一切 $N$。取 $N=2$ 得 $\sum_n|c_n|=\sum_n|\hat f(n)|<\infty$。

**步骤 4：$F$ 等于其 Fourier 级数。**

由 $F\in C^1$（甚至 $C^\infty$）且 $\sum|c_n|<\infty$，Fourier 级数 $\sum_n c_ne^{2\pi inx}$ 一致绝对收敛到 $F$（Weierstrass 判别法给出连续性，标准结论给出与 $F$ 相等：两边作 Fourier 系数比较即可）。

**步骤 5：在 $x=0$ 取值。**

$$
F(0)=\sum_{k\in\mathbb Z}f(k),\qquad \sum_n c_ne^{2\pi in\cdot0}=\sum_n c_n=\sum_n\hat f(n).
$$

由步骤 4 两者相等，故

$$
\sum_{n\in\mathbb Z}f(n)=\sum_{n\in\mathbb Z}\hat f(n).
$$

**步骤 6：多维与一般格的推广。**

对 $\mathbb Z^d$ 重复步骤 1–5（把 $[0,1]$ 换为 $[0,1]^d$、平移换为 $k\in\mathbb Z^d$）即得多维情形。对一般格 $\Lambda$，取线性同构 $A:\mathbb Z^d\to\Lambda$，令 $g(u)=f(Au)$，对 $g$ 用 $\mathbb Z^d$ 版本并把 $d$ 维 Fourier 变换的伸缩关系 $\widehat{f\circ A}(\xi)=\frac{1}{|\det A|}\hat f(A^{-T}\xi)$ 代入即得一般公式。$\square$

**附注（收敛条件可放宽）**：对 $f,\hat f$ 均为速降之外的良函数（如 $f$ 连续、$\hat f$ 可积且 $f$ 有界变差），公式仍成立；对称求和（Cesàro 或 Abel 求和）下条件还可进一步放宽，这在 θ 函数与函数方程的应用中很重要。

## 五、应用与意义

**理论意义**：Poisson 求和公式是"采样"与"周期化"的对偶，是 Fourier 分析与数论之间的第一座桥。它也是 Tate 论文中局部函数方程与整体函数方程的雏形，在 Adèle 语言下它是加法群自对偶性的表现。

**应用领域**：
1. **θ 函数与模形式**：由 $f(x)=e^{-\pi x^2}$ 得 $\theta(1/t)=\sqrt t\,\theta(t)$，是模形式变换律与 Jacobi theta 函数的基础。
2. **Zeta 与 L 函数**：Poisson 公式用于推导 Riemann $\zeta$ 与 Dirichlet $L$ 函数的函数方程，以及 Gauss 和与二次互反律。
3. **抽样定理**：频带有限信号的 Shannon 采样定理本质上就是 Poisson 公式。
4. **编码与有限域**：MacWilliams 恒等式等代数编码中的 Fourier 恒等式是 Poisson 公式的有限群版本。
5. **格与几何数论**：格点计数、$\Theta$ 级数与 Epstein zeta 函数的解析性质由多维 Poisson 公式控制。

**推广**：局部紧交换群上的抽象 Poisson 求和、Weil 的显式公式、以及迹公式（Selberg 迹公式、Atiyah–Singer 指标定理的指标公式）都可视为 Poisson 求和公式在非交换与几何情形的深刻推广。

## 相关条目

- [DedekindZeta函数](./DedekindZeta函数.md)：其函数方程与解析延拓的推导使用 Poisson 求和与 θ 函数变换。
- [p进数与局部域](./p进数与局部域.md)：局部域的加法自对偶与 Tate 局部函数方程是 Poisson 求和的局部版本。
