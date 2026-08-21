# ARMA 过程的平稳性条件

> **一句话大白话**：一个 ARMA 过程要"温柔稳定"不爆炸、波动不随时间增大，就看它的特征多项式所有根是否都在单位圆外——根在圆外就平稳。
>
> **小例子**：足球比赛的比分输赢若用自回归描述，若系数让过去的冲击被"放大"（像滚雪球），过程就会越荡越大；反之则稳定回归到均值。

## 一、定理介绍

考虑 ARMA($p,q$) 过程 $\phi(B)X_t = \theta(B)\varepsilon_t$，其中 $\varepsilon_t$ 为白噪声，$\phi(z) = 1 - \phi_1z - \cdots - \phi_pz^p$。过程平稳的充分必要条件是 $\phi(z)$ 的所有根都落在单位圆外（模大于 1）。

## 二、原理思路

将 ARMA 过程改写为线性滤波 $X_t = \psi(B)\varepsilon_t = \sum_{j=0}^{\infty}\psi_j\varepsilon_{t-j}$。只要系数序列 $\{\psi_j\}$ 绝对可和，过程就是平稳的。而 $\psi_j$ 的衰减性由特征根决定：所有根在单位圆外等价于 $|\lambda_k|<1$，从而 $\psi_j$ 以几何速度衰减。

## 三、定理的严格表述

设 $\phi(z) = \prod_{k=1}^{p}(1-\lambda_kz)$，其中 $\lambda_k^{-1}$ 为 $\phi(z)=0$ 的根。ARMA($p,q$) 为平稳过程的充要条件是

$$
|\lambda_k^{-1}| > 1 \quad (\text{即 } |\lambda_k|<1) \text{ 对所有 } k,
$$

此时 $\psi_j$ 有界 $|\psi_j| \le Cr^j$（$0<r<1$），从而 $\sum_j |\psi_j| < \infty$，且协方差 $\gamma(h) = \sigma^2\sum_{j=0}^{\infty}\psi_j\psi_{j+h}$ 有限。类似地，$\theta$ 多项式根在单位圆外时过程可逆。

## 四、证明过程

1. **MA($\infty$) 表示**：$X_t = \frac{\theta(B)}{\phi(B)}\varepsilon_t = \sum_{j=0}^{\infty}\psi_j\varepsilon_{t-j}$。
2. **平稳条件**：若 $\sum_j|\psi_j|<\infty$，则 $\mathbb{E}[X_t]=0$，$\gamma(h) = \sigma^2\sum_j\psi_j\psi_{j+h}$ 有限且仅依赖 $h$。
3. **根与衰减**：由 $\psi_j = \sum_k c_k\lambda_k^j$，当所有 $|\lambda_k|<1$ 时 $\psi_j$ 几何衰减，绝对可和成立。
4. **必要性**：若存在 $|\lambda_1|\ge1$，则 $\psi_j$ 不衰减，$\sum_j|\psi_j|=\infty$，过程非平稳（含单位根时方差发散）。

## 五、应用与意义

平稳性条件是时间序列建模的前提——只有平稳过程才能进行稳定的统计推断与预测。它决定了 ARMA 模型的阶数判定、预测的可行性与谱分析的有效性，也是检验单位根（如 Dickey-Fuller 检验）、进行差分处理的理论基础。