# Fokker-Planck 方程的推导

> **一句话大白话**：随机过程的概率密度会随时间演化，它服从一条“对流＋扩散”方程：像河水一样被漂移推着走，又像墨水一样被波动慢慢摊开。
>
> **小例子**：描述污染物在水流中的浓度分布，它一边随水流移动，一边因随机扩散弥散，Fokker-Planck 方程就描述这个密度的演化。

## 一、定理介绍

> **前置依赖**：Itô 引理、随机过程的概率密度、测试函数方法与弱形式、分部积分、期望的密度表示

设 $X_t$ 满足 $dX_t=\mu(t,X_t)dt+\sigma(t,X_t)dW_t$，$p(t,x)$ 为其概率密度。则 $p$ 满足 Fokker-Planck 方程（亦称 Kolmogorov 前向方程）：

$$
\frac{\partial p}{\partial t} = -\frac{\partial}{\partial x}\big(\mu(t,x)p\big) + \frac12\frac{\partial^2}{\partial x^2}\big(\sigma^2(t,x)p\big).
$$

## 二、原理思路

用测试函数方法的弱形式推导：对任意紧支光滑 $\phi$，由 Itô 引理得到 $\frac{d}{dt}\mathbb{E}[\phi(X_t)]$ 的表达式，再用用 $p$ 的表示 $\mathbb{E}[\phi(X_t)]=\int\phi(x)p(t,x)dx$ 与其等价代入，经过分部积分把所有的导数从 $\phi$ 搬到 $p$ 上，由 $\phi$ 的任意性得到 $p$ 的偏微分方程。

## 三、定理的严格表述

对任意 $C_0^\infty$ 测试函数 $\phi$，密度 $p(t,x)$ 满足弱形式

$$
\frac{d}{dt}\int\phi\, p\, dx = \int\Big(\mu\partial_x\phi + \frac12\sigma^2\partial_{xx}\phi\Big)p\,dx,
$$

对右边做分部积分（边界项消失）并令 $\phi$ 任意，得强形式

$$
\frac{\partial p}{\partial t} = -\partial_x(\mu p) + \frac12\partial_{xx}(\sigma^2 p).
$$

## 四、证明过程

1. **Itô 引理作用于 $\phi$**：$\frac{d}{dt}\mathbb{E}[\phi(X_t)]=\mathbb{E}\big[\mu\phi'+\frac12\sigma^2\phi''\big]$。
2. **代入密度**：两边写为 $\int(\mu\phi'+\frac12\sigma^2\phi'')\phi p\,dx$（弱形式）。
3. **分部积分**：把 $\phi'$、$\phi''$ 的导数转嫁给 $p$，边界项因紧支消失。
4. **任意性**：$\phi$ 任意，故 $p$ 满足对应的前向方程。

## 五、应用与意义

Fokker-Planck 方程是随机过程理论向偏微分方程过渡的桥梁，广泛应用于统计物理（扩散）、金融（期权密度）、神经科学与群体生物学（概率分布演化）。它给出密度的宏观演化视角，与 Kolmogorov 后向方程互为对偶，也是数值求解平稳分布、估计首次离时等数量化的基础工具。