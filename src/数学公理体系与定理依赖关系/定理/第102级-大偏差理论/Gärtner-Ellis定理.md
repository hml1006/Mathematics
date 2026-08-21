# Gärtner-Ellis定理

> **一句话大白话**：即使样本不再独立同分布，只要"对数矩生成函数的极限" $\Lambda(\theta)$ 存在且本质光滑，样本仍满足大偏差原理，速率函数同样是 Legendre 变换。
>
> **小例子**：对带依赖的序列或某些随机矩阵，若 $\Lambda_n(\theta)=\frac1n\log\mathbb E[e^{n\theta Z_n}]$ 收敛到光滑 $\Lambda$，即可得到与 Cramér 相同形式的 LDP。

## 一、定理介绍

> **前置依赖**：对数矩生成函数、Fenchel-Legendre 变换、本质光滑性、倾斜测度（测度变换）、中心极限定理。

设 $\{Z_n\}$ 为随机变量序列，定义
$$
\Lambda_n(\theta)=\frac1n\log\mathbb E[e^{n\theta Z_n}],\qquad\theta\in\mathbb R.
$$
假设对每个 $\theta$，极限 $\Lambda(\theta)=\lim_n\Lambda_n(\theta)$ 存在（允许取 $\infty$），$\Lambda$ 在 $\theta=0$ 邻域内有限且本质光滑（在 $\mathcal D_\Lambda=\{\theta:\Lambda<\infty\}$ 内部可微，且 $\lim_{\theta\to\partial\mathcal D_\Lambda}|\Lambda'(\theta)|=\infty$）。则 $\{Z_n\}$ 满足速率为 $n$ 的 LDP，速率函数为 Fenchel-Legendre 变换
$$
I(x)=\sup_{\theta\in\mathbb R}\{\theta x-\Lambda(\theta)\}.
$$

## 二、原理思路

思路与 Cramér 平行：上界仍用指数不等式，但以 $\Lambda_n\to\Lambda$ 取极限；下界用倾斜测度 $\frac{d\mathbb Q_n}{d\mathbb P}=\exp(n\theta_aZ_n-n\Lambda_n(\theta_a))$，使新测度下均值趋近 $a$。本质光滑条件保证 $\Lambda'(\theta)$ 在 $\mathcal D_\Lambda^\circ$ 上取遍整个实数轴，从而对每个 $x$ 都能找到 $\theta_x$ 使 $\Lambda'(\theta_x)=x$，下界对所有 $x$ 成立。

## 三、定理的严格表述

设 $\Lambda(\theta)=\lim_n\Lambda_n(\theta)$ 存在，$\Lambda$ 在 $\theta=0$ 邻域内有限且本质光滑。则对任意闭集 $C$、开集 $U$，
$$
\limsup_{n\to\infty}\frac1n\log\mathbb P(Z_n\in C)\le-\inf_{x\in C}I(x),\qquad
\liminf_{n\to\infty}\frac1n\log\mathbb P(Z_n\in U)\ge-\inf_{x\in U}I(x),
$$
其中 $I(x)=\sup_\theta\{\theta x-\Lambda(\theta)\}$。

## 四、证明过程

**步骤1：上界。** 对 $\theta>0$，$\mathbb P(Z_n\ge a)\le e^{-n(\theta a-\Lambda_n(\theta))}$，取 $n\to\infty$ 与 $\theta>0$ 上确界得
$$
\limsup_n\frac1n\log\mathbb P(Z_n\ge a)\le-\sup_{\theta>0}\{\theta a-\Lambda(\theta)\}.
$$
$\theta<0$ 一侧同理，再对闭集用有限覆盖推广。

**步骤2：倾斜测度。** 设 $\Lambda'(\theta_a)=a$，定义
$$
\frac{d\mathbb Q_n}{d\mathbb P}=\exp\big(n\theta_aZ_n-n\Lambda_n(\theta_a)\big).
$$
在 $\mathbb Q_n$ 下 $Z_n$ 的对数矩生成函数为 $\Lambda_n(\theta_a+\cdot)-\Lambda_n(\theta_a)\to\Lambda(\theta_a+\cdot)-\Lambda(\theta_a)$，均值趋近 $a$、方差由 $\Lambda''(\theta_a)/n$ 控制。

**步骤3：局部下界。**
$$
\mathbb P(Z_n\in(a,a+\delta))\ge e^{-n(\theta_a(a+\delta)-\Lambda_n(\theta_a))}\mathbb Q_n(Z_n\in(a,a+\delta)).
$$
由中心极限定理 $\mathbb Q_n(Z_n\in(a,a+\delta))$ 有正下界，故 $\liminf_n\frac1n\log\mathbb P(Z_n\in(a,a+\delta))\ge-I(a)$。

**步骤4：本质光滑。** 它保证对每个 $x$ 存在 $\theta_x$ 满足 $\Lambda'(\theta_x)=x$，使下界对所有 $x$ 成立，合成 LDP。$\square$

## 五、应用与意义

Gärtner-Ellis 定理把 Cramér 的独立同分布条件放宽为"对数矩生成函数极限存在且本质光滑"，可处理带依赖、时间非齐次序列及 $\mathbb R^d$ 情形。它是统计物理（相变）、随机矩阵与信息论中大偏差分析的核心工具，量化了独立性不足时稀有事件概率仍呈指数衰减的条件。