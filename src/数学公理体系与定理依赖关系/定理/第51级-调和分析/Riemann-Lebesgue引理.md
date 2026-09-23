# Riemann-Lebesgue引理

> **一句话大白话**：一个可积函数的高频傅里叶分量一定越来越小，振荡越快、正负抵消越彻底，最终任何频率上的振幅都趋于零。

> **小例子**：取 $f(x)=\mathbf{1}_{[a,b]}(x)$（矩形脉冲），则 $\hat f(\xi)=\frac{e^{-ia\xi}-e^{-ib\xi}}{i\xi}$，显然 $|\hat f(\xi)|\le\frac2{|\xi|}\to0$，这正是引理最朴素的模型。

## 一、定理介绍

> **前置依赖**：Fourier变换与逆变换公式、$L^1$ 空间与可积函数、简单函数逼近与稠密性、一致连续性。

Riemann–Lebesgue 引理的历史可追溯到 Riemann 1854 年关于三角级数与积分理论的论文，他在讨论三角级数系数的性质时指出了振荡积分的衰减现象；1902 年 Lebesgue 建立测度与积分理论后，该结论被推广到任意 $L^1$ 函数，成为傅里叶分析的入门定理。它回答的问题是：一个仅仅可积（甚至很不光滑）的函数，它的傅里叶变换在无穷远处会有怎样的行为？答案是"必定趋于零"。这在直觉上很自然：高频因子 $e^{-i\xi\cdot x}$ 的剧烈振荡使积分中的正负部分相互抵消；反过来，衰减速度又刻画了函数的光滑性，这构成了调和分析中"光滑性与衰减对偶"的第一条线索。引理说明 $\hat f$ 属于 $C_0(\mathbb{R}^n)$，从而为 $L^1$ 的傅里叶变换确定了像空间，是反演公式、Plancherel 理论与各类乘子定理的前提。

## 二、原理思路

1. 先在最特殊的函数——区间（矩形）的特征函数上直接计算：一次直接积分即可得到显式表达式，从中读出 $O(1/|\xi|)$ 的衰减。
2. 利用阶梯函数（简单函数）的线性性质：有限线性组合的变换仍是有限线性组合，衰减性质保持。
3. 用稠密性逼近一般 $L^1$ 函数：任意可积函数都能被阶梯函数在 $L^1$ 范数下逼近，把积分劈成"阶梯部分 + 小余项"，用三角不等式把余项压到任意小，再令 $|\xi|\to\infty$ 让阶梯部分的变换趋于零。
4. 顺带证明 $\hat f$ 的一致连续性，从而确认 $\hat f\in C_0(\mathbb{R}^n)$。

## 三、定理的严格表述

设 $f\in L^1(\mathbb{R}^n)$，其傅里叶变换定义为

$$
\hat f(\xi)=\int_{\mathbb{R}^n}f(x)\,e^{-i\xi\cdot x}\,dx,\qquad \xi\in\mathbb{R}^n,
$$

该积分绝对收敛，故 $\hat f$ 处处有定义且 $|\hat f(\xi)|\le\|f\|_{L^1}$。则 $\hat f$ 在 $\mathbb{R}^n$ 上一致连续，且当 $|\xi|\to\infty$ 时

$$
\hat f(\xi)\to0,\qquad\text{即}\qquad\lim_{|\xi|\to\infty}\int_{\mathbb{R}^n}f(x)e^{-i\xi\cdot x}dx=0 .
$$

换言之 $\hat f\in C_0(\mathbb{R}^n)$（在无穷远处消失的连续函数空间），且映射 $f\mapsto\hat f$ 是 $L^1\to C_0$ 的连续线性算子。

## 四、证明过程

**步骤 1（矩形特征函数的计算）。** 先取 $n=1$，$f=\mathbf{1}_{[a,b]}$。直接积分得

$$
\hat f(\xi)=\int_a^b e^{-i\xi x}dx=\frac{e^{-i\xi a}-e^{-i\xi b}}{i\xi}\quad(\xi\neq0),
$$

于是 $|\hat f(\xi)|\le\frac{2}{|\xi|}\to0$。对 $n$ 维矩形 $R=I_1\times\cdots\times I_n$，特征函数分解为乘积，$\hat{\mathbf 1}_R(\xi)=\prod_{j=1}^n\widehat{\mathbf 1}_{I_j}(\xi_j)$；当 $|\xi|\to\infty$ 时必有某个分量 $|\xi_j|\to\infty$，故

$$
|\hat{\mathbf 1}_R(\xi)|\le\frac{2}{|\xi_j|}\to0 .
$$

**步骤 2（阶梯函数与线性组合）。** 设 $g=\sum_{k=1}^{m}c_k\mathbf 1_{R_k}$ 为阶梯函数。由变换的线性性

$$
\hat g(\xi)=\sum_{k=1}^{m}c_k\widehat{\mathbf 1}_{R_k}(\xi),
$$

每个 $\widehat{\mathbf 1}_{R_k}(\xi)\to0$，有限和仍趋于 $0$，故 $\hat g(\xi)\to0$；此外 $|\hat g(\xi)|\le\sum_k|c_k||R_k|$ 一致有界。

**步骤 3（稠密性逼近）。** 设 $f\in L^1$，$\varepsilon>0$。由阶梯函数在 $L^1(\mathbb{R}^n)$ 中稠密，存在阶梯函数 $g$ 使 $\|f-g\|_{L^1}<\frac\varepsilon2$。于是对一切 $\xi$，

$$
|\hat f(\xi)|\le|\widehat{f-g}(\xi)|+|\hat g(\xi)|\le\|f-g\|_{L^1}+|\hat g(\xi)|<\frac\varepsilon2+|\hat g(\xi)| .
$$

由步骤 2 取 $R>0$ 使 $|\xi|>R$ 时 $|\hat g(\xi)|<\frac\varepsilon2$，则 $|\hat f(\xi)|<\varepsilon$。由 $\varepsilon$ 任意，$\lim_{|\xi|\to\infty}\hat f(\xi)=0$。

**步骤 4（一致连续性）。** 对 $\xi,\eta\in\mathbb{R}^n$，

$$
|\hat f(\xi)-\hat f(\eta)|\le\int_{\mathbb{R}^n}|f(x)|\,\bigl|e^{-i\xi\cdot x}-e^{-i\eta\cdot x}\bigr|\,dx .
$$

被积函数被 $2|f(x)|$ 控制，且当 $\xi-\eta\to0$ 时对每个 $x$ 趋于零，由控制收敛定理该积分随 $|\xi-\eta|\to0$ 一致趋于零（界只与 $f$ 有关而与 $\xi$ 无关），故 $\hat f$ 一致连续。结合步骤 3，$\hat f\in C_0(\mathbb{R}^n)$。

$\square$

## 五、应用与意义

- 傅里叶反演与像空间：说明 $L^1$ 的傅里叶变换落在 $C_0$ 中，为反演公式与 $L^1$ 卷积代数理论提供基础。
- 光滑性与衰减的对偶：函数越光滑、导数越可积，$\hat f$ 衰减越快，本引理是该对应关系最弱的一端。
- 乘子与奇异积分：Fourier 乘子定理与奇异积分算子理论中"乘子在无穷远处的值"以本引理为起点。
- 概率论：特征函数在无穷远处趋于零，是证明中心极限定理与稳定分布的常用工具。
- 逼近与求和：在 Fejér 求和、Bochner–Riesz 平均的收敛性讨论中用于处理高频尾部。

## 相关条目

- [Fourier变换与逆变换公式](./Fourier变换与逆变换公式.md)：本引理是其反演理论中高频部分衰减的基本依据。
- [Plancherel定理](./Plancherel定理.md)：$L^2$ 版本的等距性质，与 $L^1$ 情形的本引理互为补充。
- [Parseval恒等式](./Parseval恒等式.md)：频域能量恒等式，常与本引理配合估计截断误差。
- [Fourier变换的L2理论](./Fourier变换的L2理论.md)：把本引理的思想延伸到平方可积函数。
- [Young卷积不等式](./Young卷积不等式.md)：同为 $L^p$ 卷积分析的基本估计。
