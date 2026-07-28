# Cramér-Rao 下界

## 介绍

Cramér-Rao 下界（Cramér-Rao Lower Bound, CRLB）是数理统计中关于参数估计精度的基本定理，由瑞典统计学家哈拉尔德·克拉默（Harald Cramér）和印度统计学家卡利安普迪·拉奥（Calyampudi Radhakrishna Rao）在 1940 年代独立提出。该定理指出：在正则条件下，任何无偏估计量的方差不能低于 Fisher 信息量的倒数。Cramér-Rao 下界为评价估计量的效率提供了基准——如果某个无偏估计达到这一下界，则称其为有效估计量。该定理是点估计理论中最核心的结果之一，广泛应用于参数估计的最优性研究中。

## 分析

**前置依赖**：费舍尔信息不等式、无偏估计、Fisher 信息量、Cauchy-Schwarz 不等式。

**数学内涵**：
- 设 $X_1, \ldots, X_n$ 是独立同分布样本，密度为 $f(x;\theta)$。
- 基于 $n$ 个样本的 Fisher 信息量为 $I_n(\theta) = n I(\theta)$，其中 $I(\theta)$ 是单个样本的 Fisher 信息量。
- Cramér-Rao 下界：对 $\theta$ 的任意无偏估计 $\hat{\theta}$，$\text{Var}(\hat{\theta}) \geq 1/(n I(\theta))$。
- 对于多参数情形，下界为 $\text{Cov}(\hat{\theta}) \geq I(\theta)^{-1}$（矩阵不等式）。
- 正则条件包括：支撑集与 $\theta$ 无关、密度函数可微、积分与求导可交换。

**结构**：
1. 回顾费舍尔信息不等式。
2. 推广到 $n$ 个独立样本的情形。
3. 讨论达到下界的条件（指数族分布）。

## 思考过程

Cramér-Rao 下界是费舍尔信息不等式在 $n$ 个独立样本情形下的直接推广。对于独立同分布样本 $X_1, \ldots, X_n$，联合密度为 $\prod_{i=1}^n f(x_i;\theta)$，得分函数为 $S_n(\theta) = \sum_{i=1}^n \frac{\partial}{\partial\theta}\ln f(X_i;\theta) = \sum_{i=1}^n S_i(\theta)$。由独立性，$I_n(\theta) = \text{Var}(S_n) = n I(\theta)$。

对 $\theta$ 的任意无偏估计 $\hat{\theta}$，由 Cauchy-Schwarz 不等式，$\text{Var}(\hat{\theta}) \geq 1/I_n(\theta) = 1/(n I(\theta))$。

## 证明过程

**定理**（Cramér-Rao 下界）：设 $X_1, \ldots, X_n$ 是独立同分布随机变量，密度为 $f(x;\theta)$，满足正则条件。$\hat{\theta} = \hat{\theta}(X_1, \ldots, X_n)$ 是 $\theta$ 的无偏估计。则
$$\text{Var}(\hat{\theta}) \geq \frac{1}{n I(\theta)}$$
其中 $I(\theta) = E\left[\left(\frac{\partial}{\partial\theta}\ln f(X;\theta)\right)^2\right]$ 是单个样本的 Fisher 信息量。

**证明**：

### 1. 联合 Fisher 信息量

联合密度为 $L(\theta; x_1, \ldots, x_n) = \prod_{i=1}^n f(x_i;\theta)$。

得分函数为
$$S_n(\theta) = \frac{\partial}{\partial\theta}\ln L(\theta) = \sum_{i=1}^n \frac{\partial}{\partial\theta}\ln f(X_i;\theta) = \sum_{i=1}^n S_i(\theta)$$

由于 $X_i$ 独立，$\{S_i\}$ 独立同分布，$E[S_i] = 0$，$\text{Var}(S_i) = I(\theta)$。因此
$$E[S_n] = 0,\quad \text{Var}(S_n) = n I(\theta)$$

### 2. 协方差计算

由无偏性 $E[\hat{\theta}] = \theta$，两边对 $\theta$ 求导：
$$1 = \frac{\partial}{\partial\theta} \int \hat{\theta} L(\theta; x) d\mu(x) = \int \hat{\theta} \frac{\partial L}{\partial\theta} d\mu(x)$$
$$= \int \hat{\theta} \frac{\partial \ln L}{\partial\theta} \cdot L d\mu(x) = E[\hat{\theta} \cdot S_n]$$

因此 $\text{Cov}(\hat{\theta}, S_n) = E[\hat{\theta} \cdot S_n] - E[\hat{\theta}]E[S_n] = 1 - \theta \cdot 0 = 1$。

### 3. Cauchy-Schwarz 不等式

由 Cauchy-Schwarz 不等式：
$$1 = \text{Cov}(\hat{\theta}, S_n)^2 \leq \text{Var}(\hat{\theta}) \cdot \text{Var}(S_n) = \text{Var}(\hat{\theta}) \cdot n I(\theta)$$

因此
$$\text{Var}(\hat{\theta}) \geq \frac{1}{n I(\theta)}$$

$\square$

**推论**（多参数 Cramér-Rao 下界）：对参数向量 $\theta \in \mathbb{R}^k$，Fisher 信息矩阵为 $I(\theta)_{ij} = E\left[\frac{\partial \ln f}{\partial \theta_i} \frac{\partial \ln f}{\partial \theta_j}\right]$，则对 $\theta$ 的无偏估计 $\hat{\theta}$，
$$\text{Cov}(\hat{\theta}) \geq [n I(\theta)]^{-1}$$
（在矩阵正定意义下）。

**注记**：达到 Cramér-Rao 下界的估计量称为有效估计量。当且仅当分布族是指数族时，有效估计量存在。例如，正态分布 $N(\mu, \sigma^2)$ 中样本均值 $\bar{X}$ 是 $\mu$ 的有效估计量。