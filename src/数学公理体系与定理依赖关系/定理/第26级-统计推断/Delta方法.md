# Delta方法

> **一句话大白话**：估计量本身约成正态时，给它套一个光滑函数 $g$ 仍是约正态的，只是方差要乘上导数的平方 $[g'(\theta)]^2$——就像小振幅线性化：$\sqrt n(g(\hat\theta)-g(\theta))\to N(0,[g'(\theta)]^2\sigma^2)$。
>
> **小例子**：$X_i\sim Poi(\lambda)$，MLE $\hat\lambda=\bar X$ 有渐近方差 $\lambda/n$。用 $g=\log$，则 $\sqrt n(\log\hat\lambda-\log\lambda)\to N(0,\frac1\lambda)$，方差稳定为 $1/\lambda$。

## 介绍

Delta 方法（Delta Method）是数理统计中用于推导统计量渐近分布的重要工具。该方法的核心理念是：若一个统计量 $\hat{\theta}$ 渐近正态，则其光滑函数变换 $g(\hat{\theta})$ 也渐近正态，且渐近方差可通过 Delta 方法计算。具体而言，若 $\sqrt{n}(\hat{\theta} - \theta) \xrightarrow{d} N(0, \sigma^2)$，且 $g$ 在 $\theta$ 处可导且 $g'(\theta) \neq 0$，则 $\sqrt{n}(g(\hat{\theta}) - g(\theta)) \xrightarrow{d} N(0, [g'(\theta)]^2\sigma^2)$。Delta 方法在方差稳定化变换、参数估计的渐近分布推导和置信区间构造中广泛应用，是渐近统计理论中最基本的工具之一。

## 分析

**前置依赖**：中心极限定理、连续映射定理、Slutsky 引理、Taylor 展开。

**数学内涵**：
- 单变量情形：$\sqrt{n}(g(\hat{\theta}) - g(\theta)) \xrightarrow{d} N(0, [g'(\theta)]^2\sigma^2)$。
- 多变量情形：$\sqrt{n}(g(\hat{\theta}) - g(\theta)) \xrightarrow{d} N(0, \nabla g(\theta)^T \Sigma \nabla g(\theta))$。
- 二阶 Delta 方法：当 $g'(\theta) = 0$ 时，需用二阶展开，极限分布可能为卡方分布。
- 要求 $g$ 在 $\theta$ 处具有足够光滑性。

**结构**：
1. 单变量 Delta 方法。
2. 多变量 Delta 方法。
3. 二阶 Delta 方法。
4. 应用示例。

## 思考过程

Delta 方法的直观思想来自一阶 Taylor 展开。当 $\hat{\theta}$ 接近 $\theta$ 时：
$$g(\hat{\theta}) \approx g(\theta) + g'(\theta)(\hat{\theta} - \theta)$$

由于 $\hat{\theta}$ 在 $\theta$ 附近以 $\sqrt{n}$ 速率收敛，$g(\hat{\theta})$ 的渐近分布由线性近似决定。一阶项 $g'(\theta)(\hat{\theta} - \theta)$ 的渐近分布乘以 $g'(\theta)$ 即可得到 $g(\hat{\theta})$ 的渐近分布。

如果 $g'(\theta) = 0$，则一阶近似退化为常数，需要用到二阶 Taylor 展开，此时极限分布为卡方分布或更复杂的混合分布。

Delta 方法的一个重要应用是方差稳定化变换。例如，对于泊松分布 $X \sim \text{Poisson}(\lambda)$，$\sqrt{n}(\bar{X} - \lambda) \xrightarrow{d} N(0, \lambda)$，方差依赖于 $\lambda$。通过变换 $g(\lambda) = \sqrt{\lambda}$，有 $g'(\lambda) = 1/(2\sqrt{\lambda})$，渐近方差变为常数 $1/4$，实现了方差稳定。

## 证明过程

**定理**（单变量 Delta 方法）：设 $\{\hat{\theta}_n\}$ 是一列估计量，满足
$$\sqrt{n}(\hat{\theta}_n - \theta) \xrightarrow{d} N(0, \sigma^2)$$
其中 $\sigma^2 > 0$。设 $g: \mathbb{R} \to \mathbb{R}$ 在 $\theta$ 处可导，且 $g'(\theta) \neq 0$。则
$$\sqrt{n}(g(\hat{\theta}_n) - g(\theta)) \xrightarrow{d} N(0, [g'(\theta)]^2\sigma^2)$$

**证明**：

### 1. 一阶 Taylor 展开

由于 $g$ 在 $\theta$ 处可导，由 Taylor 定理：
$$g(\hat{\theta}_n) = g(\theta) + g'(\theta)(\hat{\theta}_n - \theta) + o_p(|\hat{\theta}_n - \theta|)$$

其中余项 $o_p(|\hat{\theta}_n - \theta|)$ 表示当 $\hat{\theta}_n \to \theta$ 时，该余项比 $|\hat{\theta}_n - \theta|$ 更快趋于 0（依概率）。

### 2. 移项并缩放

移项得：
$$g(\hat{\theta}_n) - g(\theta) = g'(\theta)(\hat{\theta}_n - \theta) + o_p(|\hat{\theta}_n - \theta|)$$

两边乘以 $\sqrt{n}$：
$$\sqrt{n}(g(\hat{\theta}_n) - g(\theta)) = g'(\theta)\sqrt{n}(\hat{\theta}_n - \theta) + \sqrt{n} \cdot o_p(|\hat{\theta}_n - \theta|)$$

### 3. 处理余项

由于 $\sqrt{n}(\hat{\theta}_n - \theta) \xrightarrow{d} N(0, \sigma^2)$，有 $\hat{\theta}_n - \theta = O_p(1/\sqrt{n})$，即 $|\hat{\theta}_n - \theta| = O_p(1/\sqrt{n})$。

因此 $\sqrt{n} \cdot o_p(|\hat{\theta}_n - \theta|) = \sqrt{n} \cdot o_p(O_p(1/\sqrt{n})) = o_p(1)$，即余项依概率收敛到 0。

### 4. 应用 Slutsky 引理

由 Slutsky 引理：
$$\sqrt{n}(g(\hat{\theta}_n) - g(\theta)) = g'(\theta)\sqrt{n}(\hat{\theta}_n - \theta) + o_p(1) \xrightarrow{d} g'(\theta) \cdot N(0, \sigma^2) = N(0, [g'(\theta)]^2\sigma^2)$$

$\square$

---

**定理**（多变量 Delta 方法）：设 $\{\hat{\boldsymbol{\theta}}_n\}$ 是 $\mathbb{R}^k$ 中的一列估计量，满足
$$\sqrt{n}(\hat{\boldsymbol{\theta}}_n - \boldsymbol{\theta}) \xrightarrow{d} N(\boldsymbol{0}, \Sigma)$$
设 $g: \mathbb{R}^k \to \mathbb{R}^m$ 在 $\boldsymbol{\theta}$ 处可微，梯度矩阵 $\nabla g(\boldsymbol{\theta}) \in \mathbb{R}^{m \times k}$ 在 $\boldsymbol{\theta}$ 处连续。则
$$\sqrt{n}(g(\hat{\boldsymbol{\theta}}_n) - g(\boldsymbol{\theta})) \xrightarrow{d} N(\boldsymbol{0}, \nabla g(\boldsymbol{\theta})^T \Sigma \nabla g(\boldsymbol{\theta}))$$

**证明**：与单变量情形类似，使用多变量 Taylor 展开：
$$g(\hat{\boldsymbol{\theta}}_n) = g(\boldsymbol{\theta}) + \nabla g(\boldsymbol{\theta})^T (\hat{\boldsymbol{\theta}}_n - \boldsymbol{\theta}) + o_p(\|\hat{\boldsymbol{\theta}}_n - \boldsymbol{\theta}\|)$$

乘以 $\sqrt{n}$ 后应用 Slutsky 引理即得。$\square$

---

**定理**（二阶 Delta 方法）：设 $\sqrt{n}(\hat{\theta}_n - \theta) \xrightarrow{d} N(0, \sigma^2)$，而 $g$ 在 $\theta$ 处二阶可导且 $g'(\theta) = 0$，$g''(\theta) \neq 0$。则
$$n(g(\hat{\theta}_n) - g(\theta)) \xrightarrow{d} \frac{g''(\theta)\sigma^2}{2} \chi^2_1$$

**证明**：使用二阶 Taylor 展开：
$$g(\hat{\theta}_n) = g(\theta) + g'(\theta)(\hat{\theta}_n - \theta) + \frac{1}{2}g''(\theta)(\hat{\theta}_n - \theta)^2 + o_p((\hat{\theta}_n - \theta)^2)$$

由于 $g'(\theta) = 0$：
$$g(\hat{\theta}_n) - g(\theta) = \frac{1}{2}g''(\theta)(\hat{\theta}_n - \theta)^2 + o_p((\hat{\theta}_n - \theta)^2)$$

乘以 $n$：
$$n(g(\hat{\theta}_n) - g(\theta)) = \frac{1}{2}g''(\theta) \cdot n(\hat{\theta}_n - \theta)^2 + o_p(1)$$

由 $\sqrt{n}(\hat{\theta}_n - \theta) \xrightarrow{d} N(0, \sigma^2)$，知 $n(\hat{\theta}_n - \theta)^2 \xrightarrow{d} \sigma^2 \chi^2_1$，代入得结论。$\square$

---

**应用示例**：

**示例 1（方差稳定化变换）**：设 $X_1, \ldots, X_n \overset{\text{i.i.d.}}{\sim} \text{Poisson}(\lambda)$，由 CLT 知 $\sqrt{n}(\bar{X}_n - \lambda) \xrightarrow{d} N(0, \lambda)$。取 $g(\lambda) = \sqrt{\lambda}$，则 $g'(\lambda) = 1/(2\sqrt{\lambda})$，由 Delta 方法：
$$\sqrt{n}(\sqrt{\bar{X}_n} - \sqrt{\lambda}) \xrightarrow{d} N\left(0, \frac{1}{4\lambda} \cdot \lambda\right) = N\left(0, \frac{1}{4}\right)$$

即变换后的统计量渐近方差与 $\lambda$ 无关，实现了方差稳定。

**示例 2（相关系数的 Fisher 变换）**：设 $r$ 是样本相关系数，已知 $\sqrt{n}(r - \rho) \xrightarrow{d} N(0, (1-\rho^2)^2)$。取 Fisher 变换 $g(\rho) = \frac{1}{2}\ln\frac{1+\rho}{1-\rho} = \text{arctanh}(\rho)$，则 $g'(\rho) = 1/(1-\rho^2)$，由 Delta 方法：
$$\sqrt{n}(\text{arctanh}(r) - \text{arctanh}(\rho)) \xrightarrow{d} N(0, 1)$$

这使得相关系数的推断可以使用标准正态分布进行近似。