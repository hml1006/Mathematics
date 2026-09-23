# Lévy连续性定理

> **一句话大白话**：随机变量序列依分布收敛，当且仅当它们的特征函数逐点收敛到一个在原点连续的函数；换句话说，验证分布收敛只需验证一个普通函数列的收敛。

> **小例子**：设 $X_n$ 为 $n$ 个独立同分布零均值单位方差随机变量之和除以 $\sqrt n$。其特征函数满足 $\varphi_n(t)=\left[\varphi(t/\sqrt n)\right]^{n}\to e^{-t^{2}/2}$，而 $e^{-t^{2}/2}$ 在原点连续且是标准正态的特征函数，由本定理立即得 $X_n\Rightarrow N(0,1)$，这正是一个"用特征函数做数值与理论验证"的典型场景。

## 一、定理介绍

> **前置依赖**：特征函数、特征函数唯一性定理、依分布收敛、连续性定理、胎紧性、控制收敛定理。

Lévy 连续性定理由法国数学家 Paul Lévy 在 1925 年出版的《Calcul des probabilités》中提出，是特征函数方法的收官之作，与"特征函数唯一决定分布"并列为概率论极限理论的两大支柱。在它之前，证明依分布收敛的通用手段是分布函数的逐点收敛（或测度的弱收敛），但分布函数往往没有显式表达式，即便有也不便于处理卷积与和式。Lévy 的洞察是：把概率测度的问题搬到特征函数（即 Fourier 变换）这一侧，因为独立和的分布对应特征函数的**乘积**，卷积变成了逐点乘法，收敛性问题随之化为分析学中的函数收敛问题。

定理的表述有一个关键的、常被初学者忽视的条件：极限函数必须在原点连续（等价于它是某个概率测度的特征函数）。如果只要求 $\varphi_n$ 逐点收敛，极限可能不是一个概率测度的特征函数——典型反例是 $X_n$ 服从均值为 $0$、方差为 $n$ 的正态分布，此时 $\varphi_n(t)=e^{-nt^{2}/2}\to\mathbb{1}_{\{t=0\}}$，它在原点不连续，而 $X_n$ 显然不收敛于任何随机变量（概率质量"逃逸到无穷"）。因此原点连续性正是排除"质量逃逸"的胎紧（tightness）条件。在计算数学中，该定理是把数值求得的 Fourier 变换、数值反演结果与目标分布收敛性联系起来的理论依据，也用于检验 Monte Carlo 与谱方法近似的分布极限。

## 二、原理思路

1. 先从"$\varphi$ 在原点连续"这一条件榨出**胎紧性**：用截断不等式把尾概率 $\mathbb{P}(|X_n|\ge 2/\varepsilon)$ 用特征函数在原点邻域上的积分平均值控制，再让 $\varepsilon\to0$ 并结合 $\varphi_n\to\varphi$、$\varphi(0)=1$，得到对 $n$ 一致的小尾概率。

2. 胎紧性意味着序列相对紧（Prokhorov 定理）：$\{X_n\}$ 的每个子列都有进一步子列依分布收敛到某随机变量。对任一这样的极限 $X'$，由其连续性定理的"正方向"（依分布收敛推出特征函数逐点收敛）知 $X'$ 的特征函数就是 $\varphi$。

3. 由特征函数唯一性定理，所有子列极限的分布相同，故整个序列依分布收敛到该极限分布；这解决了"存在性"。反向命题用控制收敛定理（或 Vitali）直接得到，并可用截断把收敛加强为在紧集上一致。

## 三、定理的严格表述

设 $X_n$（$n\ge1$）与 $X$ 为实值随机变量，特征函数分别为

$$
\varphi_n(t)=\mathbb{E}\left[e^{itX_n}\right],\qquad \varphi(t)=\mathbb{E}\left[e^{itX}\right],\qquad t\in\mathbb{R}.
$$

**（Lévy 连续性定理）** 若

$$
\varphi_n(t)\longrightarrow\varphi(t)\qquad\text{对每个 }t\in\mathbb{R},
$$

且 $\varphi$ 在 $t=0$ 处连续，则存在随机变量 $X$ 以 $\varphi$ 为特征函数（即 $\varphi$ 是概率测度的特征函数），并且

$$
X_n\ \xrightarrow{\ d\ }\ X .
$$

反之，若 $X_n\xrightarrow{\ d}X$，则 $\varphi_n(t)\to\varphi(t)$ 对每个 $t$ 成立，且收敛在任意紧集上一致。

**截断不等式**：对任意随机变量 $Y$ 与 $\varepsilon>0$，

$$
\mathbb{P}\left(|Y|\ge\frac{2}{\varepsilon}\right)\le\frac{1}{\varepsilon}\int_{-\varepsilon}^{\varepsilon}\left(1-\mathrm{Re}\,\varphi_Y(t)\right)dt .
$$

## 四、证明过程

**步骤 1（截断不等式的推导）。** 记 $\varphi_Y$ 为 $Y$ 的特征函数。由 $\mathrm{Re}\,\varphi_Y(t)=\mathbb{E}[\cos(tY)]$ 与 Fubini 定理，

$$
\int_{-\varepsilon}^{\varepsilon}\left(1-\mathrm{Re}\,\varphi_Y(t)\right)dt=\mathbb{E}\left[\int_{-\varepsilon}^{\varepsilon}\left(1-\cos(tY)\right)dt\right]=\mathbb{E}\left[2\varepsilon-\frac{2\sin(\varepsilon Y)}{Y}\right].
$$

对 $|y|\ge 2/\varepsilon$，记 $u=\varepsilon y$，则 $|u|\ge2$，而 $\frac{\sin u}{u}\le\frac12$（因 $|u|\ge2$ 时 $|\sin u|\le1\le|u|/2$），故被积函数

$$
2\varepsilon-\frac{2\sin(\varepsilon y)}{y}=2\varepsilon\left(1-\frac{\sin u}{u}\right)\ge 2\varepsilon\cdot\frac12=\varepsilon .
$$

于是 $\int_{-\varepsilon}^{\varepsilon}(1-\mathrm{Re}\,\varphi_Y)\,dt\ge\varepsilon\,\mathbb{P}(|Y|\ge2/\varepsilon)$，即得截断不等式。

**步骤 2（胎紧性）。** 由假设 $\mathrm{Re}\,\varphi_n(t)\to\mathrm{Re}\,\varphi(t)$ 且 $\varphi$ 在 $0$ 连续、$\varphi(0)=1$，故被积函数满足

$$
\left(1-\mathrm{Re}\,\varphi_n(t)\right)\longrightarrow\left(1-\mathrm{Re}\,\varphi(t)\right)\quad\text{逐点},\qquad 0\le1-\mathrm{Re}\,\varphi_n(t)\le2 .
$$

由控制收敛定理，$\int_{-\varepsilon}^{\varepsilon}(1-\mathrm{Re}\,\varphi_n(t))dt\to\int_{-\varepsilon}^{\varepsilon}(1-\mathrm{Re}\,\varphi(t))dt$。又 $\varphi$ 在 $0$ 连续且 $\varphi(0)=1$，故当 $\varepsilon\to0$ 时右端趋于 $0$。于是对任意 $\eta>0$ 先取定小 $\varepsilon$ 使 $\int_{-\varepsilon}^{\varepsilon}(1-\mathrm{Re}\,\varphi)\le\varepsilon\eta/2$，再取 $N$ 使 $n\ge N$ 时积分不超过 $\varepsilon\eta$，由截断不等式得

$$
\mathbb{P}\left(|X_n|\ge\frac{2}{\varepsilon}\right)\le\eta\qquad\text{对一切 }n\ge N .
$$

有限个 $n<N$ 的分布各自胎紧，故整个序列 $\{X_n\}$ 胎紧。

**步骤 3（子列极限的特征函数）。** 由 Prokhorov 定理，胎紧序列存在依分布收敛的子列 $X_{n_k}\Rightarrow X'$。对任意 $t$，$x\mapsto e^{itx}$ 有界连续，由依分布收敛的定义（Portmanteau 定理或弱收敛的等价刻画）

$$
\varphi_{n_k}(t)=\mathbb{E}\left[e^{itX_{n_k}}\right]\longrightarrow\mathbb{E}\left[e^{itX'}\right]=:\varphi_{X'}(t).
$$

另一方面由假设 $\varphi_{n_k}(t)\to\varphi(t)$，故 $\varphi_{X'}=\varphi$ 逐点成立，即 $\varphi$ 确实是 $X'$ 的特征函数（这也解释了为什么原点连续性不可去掉）。

**步骤 4（唯一性与全序列收敛）。** 设另有子列 $X_{m_k}\Rightarrow X''$，同法得 $\varphi_{X''}=\varphi=\varphi_{X'}$。由特征函数唯一性定理，$X'$ 与 $X''$ 同分布，故所有子列极限的分布相同。若全序列 $X_n$ 不依分布收敛到该分布，则存在有界连续函数 $g$ 与 $\varepsilon_0>0$ 及子列 $n_k$ 使 $|\mathbb{E}g(X_{n_k})-\mathbb{E}g(X)|\ge\varepsilon_0$；但该子列仍胎紧，可再取子列收敛到与 $X$ 同分布的极限，与上式矛盾。故 $X_n\xrightarrow{\ d\ }X$。

**步骤 5（反向命题）。** 设 $X_n\xrightarrow{\ d\ }X$。对固定 $t$，函数 $x\mapsto e^{itx}$ 有界连续，故 $\varphi_n(t)=\mathbb{E}[e^{itX_n}]\to\mathbb{E}[e^{itX}]=\varphi(t)$。若要在紧集 $[-T,T]$ 上一致，取截断 $X_n^{M}=X_n\mathbf{1}_{\{|X_n|\le M\}}$，对 $|t|\le T$ 有 $|e^{itX_n}-e^{itX_n^M}|\le 2\mathbf{1}_{\{|X_n|>M\}}$，而 $\mathbb{P}(|X_n|>M)$ 对 $n$ 一致小（步骤 2 的胎紧性），并用 $e^{itx}$ 在 $[-M,M]$ 上的一致连续性，即可把逐点收敛提升为紧集上的一致收敛。$\square$

## 五、应用与意义

- 中心极限定理与稳定分布：把独立和的极限问题化为特征函数乘积的逐点极限，是 CLT、无穷可分分布与稳定律的标准证明框架。
- 数值反演与计算：在傅里叶/FFT 数值反演分布密度时，可用本定理验证数值特征函数列的收敛性并提供误差控制的理论保证。
- Monte Carlo 与随机算法：检验采样经验分布的极限行为、证明马尔可夫链蒙特卡洛的渐近正态性。
- 反例识别：强调原点连续性条件，避免把"特征函数逐点收敛"误当作"分布收敛"，防止概率质量向无穷逃逸的典型错误。

## 相关条目

- [连续性定理](../第24级-概率论基础/连续性定理.md)：与本定理内容对应的经典表述与基础证明。
- [特征函数唯一性定理](../第24级-概率论基础/特征函数唯一性定理.md)：本证明步骤 4 唯一性的依据。
- [中心极限定理](../第24级-概率论基础/中心极限定理.md)：本定理最著名的应用场景。
- [连续映射定理](../第26级-统计推断/连续映射定理.md)：依分布收敛的连续性传递，常与本定理配合使用。
- [蒙特卡洛方法的收敛性](./蒙特卡洛方法的收敛性.md)：数值模拟的分布收敛保证。
- [Ulam胎紧定理](../第41级-随机过程/Ulam胎紧定理.md)：胎紧性与相对紧性的测度论基础。
- [紧性准则](../第41级-随机过程/紧性准则.md)：序列相对紧性的判定工具。
