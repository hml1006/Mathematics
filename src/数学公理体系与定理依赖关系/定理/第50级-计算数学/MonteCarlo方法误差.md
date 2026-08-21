# Monte Carlo方法误差

> **一句话大白话**：用"撒随机点统计命中比例"来估算积分或概率，误差约随点数开根号而一起变小——多撒100倍的点，误差才缩到1/10，想更准得多撒点，但好处是维数高了也不怕"维数灾难"。
>
> **小例子**：估计圆的面积可往正方形里随机撒点的命中率；Monte Carlo误差约为 $\sigma/\sqrt{N}$，$N$ 越大越稳，而且对高维积分同为 $O(1/\sqrt{N})$，不随维数暴涨。

## 介绍

Monte Carlo 方法（Monte Carlo Method）是一类通过随机采样来估计数学问题数值解的算法，由 Stanislaw Ulam、John von Neumann 等人于1940年代在 Los Alamos 国家实验室创立。Monte Carlo 方法的基本思想是利用大数定律，用样本均值来估计总体均值。Monte Carlo 方法的误差分析基于中心极限定理：积分估计的误差随样本量 $N$ 的增加以 $O(1/\sqrt{N})$ 的速度衰减。这个收敛速度与问题维度无关，使得 Monte Carlo 方法在高维问题中具有独特的优势。

## 分析

**前置依赖**：独立随机采样、大数定律、中心极限定理、方差与置信区间。

**定理的精确表述**：设 $f: [0,1]^d \to \mathbb{R}$ 是平方可积函数，$I = \int_{[0,1]^d} f(x) dx$。Monte Carlo 估计量为

$$
\hat{I}_N = \frac{1}{N} \sum_{i=1}^N f(X_i),
$$

其中 $X_i$ 是 $[0,1]^d$ 上的独立均匀随机变量。则

1. **无偏性**：$\mathbb{E}[\hat{I}_N] = I$。
2. **方差**：$\mathrm{Var}(\hat{I}_N) = \frac{\sigma^2}{N}$，其中 $\sigma^2 = \mathrm{Var}(f(X)) = \int f^2 - I^2$。
3. **均方误差**：$\mathbb{E}[(\hat{I}_N - I)^2] = \frac{\sigma^2}{N}$。
4. **渐近正态性**：$\sqrt{N}(\hat{I}_N - I) \xrightarrow{d} \mathcal{N}(0, \sigma^2)$。

**依赖的概念**：大数定律、中心极限定理、方差、置信区间、随机采样。

**证明策略**：直接应用大数定律和中心极限定理。

## 思考过程

Monte Carlo 方法的误差分析的核心是统计估计理论。估计量的方差为 $\sigma^2/N$，因此标准差为 $\sigma/\sqrt{N}$，这给出了误差的典型量级 $O(1/\sqrt{N})$。

与确定性数值积分方法（如梯形法则误差 $O(N^{-2/d})$）相比，Monte Carlo 方法的 $O(1/\sqrt{N})$ 收敛速度与维度 $d$ 无关，因此当 $d$ 较大时，Monte Carlo 方法优于确定性方法。

方差缩减技术（如重要性采样、控制变量法、分层采样）可以降低 $\sigma^2$，从而加速收敛。中心极限定理保证了误差的渐近正态分布，由此可以构造置信区间。

## 证明过程

**定理**（Monte Carlo 误差估计）：设 $f(X)$ 的方差 $\sigma^2 < \infty$，则

$$
\mathbb{P}\left(|\hat{I}_N - I| \ge \frac{z_{\alpha/2} \sigma}{\sqrt{N}}\right) \approx \alpha,
$$

其中 $z_{\alpha/2}$ 是标准正态分布的上 $\alpha/2$ 分位数。

**证明**：

**步骤 1：无偏性和方差。**

由定义，$\mathbb{E}[\hat{I}_N] = \frac{1}{N} \sum_{i=1}^N \mathbb{E}[f(X_i)] = I$。

由于 $X_i$ 独立，$\mathrm{Var}(\hat{I}_N) = \frac{1}{N^2} \sum_{i=1}^N \mathrm{Var}(f(X_i)) = \frac{\sigma^2}{N}$。

**步骤 2：中心极限定理。**

由中心极限定理，$\sqrt{N}(\hat{I}_N - I) / \sigma \xrightarrow{d} \mathcal{N}(0, 1)$。因此对充分大的 $N$，

$$
\mathbb{P}\left(|\hat{I}_N - I| \ge \frac{z_{\alpha/2} \sigma}{\sqrt{N}}\right) \approx \alpha.
$$

**步骤 3：方差的估计。**

在实际应用中，$\sigma^2$ 未知，需用样本方差估计：

$$
\hat{\sigma}^2 = \frac{1}{N-1} \sum_{i=1}^N (f(X_i) - \hat{I}_N)^2.
$$

则 $\hat{\sigma}^2$ 是 $\sigma^2$ 的一致估计，可代入置信区间公式。$\square$

**推论**（收敛速度）：Monte Carlo 方法的均方误差为 $\sigma^2/N$，收敛速度为 $O(1/\sqrt{N})$。要达到误差 $\varepsilon$，需要的样本量约为 $N \approx \sigma^2/\varepsilon^2$。

**注**（重要性采样）：若直接采样方差过大，可使用重要性采样：选择概率密度 $g(x)$，估计量为

$$
\hat{I}_N = \frac{1}{N} \sum_{i=1}^N \frac{f(X_i) w(X_i)}{g(X_i)},
$$

其中 $X_i \sim g$，$w(x)$ 是权重函数。适当选择 $g$ 可以显著降低方差。