# Wold 分解定理

> **一句话大白话**：任何一个平稳序列都能拆成两半——一半是可以由历史噪声线性叠加出来的新息部分，另一半是"有规律、能精确预测"的确定性部分，这两部分互不干扰。
>
> **小例子**：某城市的日气温可看做"长期季节规律（确定性）+ 当天的随机扰动（白噪声的叠加）"两部分之和。

## 一、定理介绍

> **前置依赖**：协方差平稳过程、Hilbert 空间与正交投影、正交性与白噪声、nova 表示与平方可和级数、张成子空间

Wold 分解定理断言：任一零均值协方差平稳过程 $\{X_t\}$ 可唯一分解为

$$
X_t = \sum_{j=0}^{\infty}\psi_j\varepsilon_{t-j} + V_t,
$$

其中 $\{\varepsilon_t\}$ 是新息白噪声（$\psi_0=1$，$\sum_j\psi_j^2<\infty$），$V_t$ 是确定性分量，与所有 $\varepsilon_s$ 不相关。

## 二、原理思路

在 Hilbert 空间 $\mathcal{H}_t = \overline{\operatorname{span}}\{X_s: s\le t\}$ 中，将 $X_t$ 正交投影到其过去上，残差即新息 $\varepsilon_t$。反复投影可把 $X_t$ 展成新息的历史线性组合，剩下的与所有新息正交的部分即确定性分量 $V_t$。

## 三、定理的严格表述

设 $\{X_t\}$ 为用 Hilbert 空间刻画的零均值协方差平稳过程，令 $\mathcal{H}_t = \overline{\operatorname{span}}\{X_s: s\le t\}$，$\varepsilon_t = X_t - \mathcal{P}_{\mathcal{H}_{t-1}}X_t$。则存在唯一分解

$$
X_t = \sum_{j=0}^{\infty}\psi_j\varepsilon_{t-j} + V_t,
$$

其中 $\varepsilon_t$ 为白噪声，$\sum_j\psi_j^2<\infty$，$\gamma(0) = \sigma^2\sum_j\psi_j^2 + \operatorname{Var}(V_t)$，且 $V_t$ 与所有 $\varepsilon_s$（$-\infty<s<\infty$）不相关。

## 四、证明过程

1. **构造新息**：$\varepsilon_t = X_t - \mathcal{P}_{\mathcal{H}_{t-1}}X_t$，其与 $\mathcal{H}_{t-1}$ 正交，故为白噪声。
2. **MA 表示**：反复投影将 $X_t$ 展成 $\varepsilon_{t-1},\varepsilon_{t-2},\dots$ 的线性组合加正交余项 $V_t$。
3. **平方可和**：$\gamma(0) = \sigma^2\sum_j\psi_j^2 + \operatorname{Var}(V_t)<\infty$ 给出 $\sum_j\psi_j^2<\infty$。
4. **唯一性**：若有两种分解，则二者之差为既是 MA 表示差又是确定性差，由正交性推出 $\psi_j=\psi_j'$ 等。

## 五、应用与意义

Wold 分解揭示了平稳序列的结构：任何平稳过程在有限方差意义下都可用可列个新息线性表出。它是 ARMA 模型的理论根基，说明在宽平稳框架下"能用线性模型建模的部分"就是新息部分，而确定性趋势需单独处理，从而指导去趋势与差分等预处理。