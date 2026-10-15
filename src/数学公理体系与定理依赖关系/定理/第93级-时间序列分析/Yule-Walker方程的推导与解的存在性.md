# Yule-Walker 方程的推导与解的存在性

> **一句话大白话**：自回归过程的"骨架"——各阶滞后协方差——之间满足一组自洽方程，解出它就能求出未知的自回归系数和过程方差。
>
> **小例子**：用一个变量的前几期预测当前值，未知的几个权重系数恰好由测到的自协方差通过 Yule-Walker 方程组唯一解出。

## 一、定理介绍

> **前置依赖**：AR 过程的定义、自协方差函数、期望与正交性（因果性）、谱定理、可逆矩阵等价条件

对 AR($p$) 过程 $X_t = \phi_1X_{t-1} + \cdots + \phi_pX_{t-p} + \varepsilon_t$，其自协方差 $\gamma(h)$ 满足 Yule-Walker 方程。特别当 $h=1,\dots,p$ 时写成矩阵形式 $\boldsymbol{\Gamma}_p\boldsymbol{\phi} = \boldsymbol{\gamma}_p$，且解存在唯一当且仅当自协方差矩阵 $\boldsymbol{\Gamma}_p$ 正定。

## 二、原理思路

将 AR 方程两边同乘以 $X_{t-h}$ 并取期望，由因果性可知 $\varepsilon_t$ 与过去值正交，从而得到 $\gamma(h)$ 的线性递推关系。取 $h=1,\dots,p$ 即得矩阵方程组，正定的 $\boldsymbol{\Gamma}_p$ 保证了系数可逆求解。

## 三、定理的严格表述

对 $h\ge1$ 有

$$
\gamma(h) = \phi_1\gamma(h-1) + \phi_2\gamma(h-2) + \cdots + \phi_p\gamma(h-p).
$$

当 $h=1,\dots,p$ 时矩阵形式为

$$
\boldsymbol{\Gamma}_p\boldsymbol{\phi} = \boldsymbol{\gamma}_p,
$$

其中 $\boldsymbol{\Gamma}_p = [\gamma(|i-j|)]$，$\boldsymbol{\phi} = (\phi_1,\dots,\phi_p)^\top$，$\boldsymbol{\gamma}_p = (\gamma(1),\dots,\gamma(p))^\top$。$\boldsymbol{\Gamma}_p$ 正定时解存在唯一。

## 四、证明过程

1. **乘 $X_{t-h}$ 取期望**：由 $\mathbb{E}[\varepsilon_t X_{t-h}]=0$（$h\ge1$）得递推式。
2. **矩阵化**：将 $h=1,\dots,p$ 代入得 $\boldsymbol{\Gamma}_p\boldsymbol{\phi}=\boldsymbol{\gamma}_p$。
3. **存在唯一**：平稳过程的 $\boldsymbol{\Gamma}_p$ 正定，故 $\boldsymbol{\phi} = \boldsymbol{\Gamma}_p^{-1}\boldsymbol{\gamma}_p$ 存在唯一。
4. **确定 $\gamma(0)$**：乘 $X_t$ 取期望，利用 $\mathbb{E}[X_t\varepsilon_t]=\sigma^2$ 得 $\gamma(0) = \sum_i\phi_i\gamma(i) + \sigma^2$，与 Yule-Walker 方程联立求解。

## 五、应用与意义

Yule-Walker 方程是 AR 系数矩估计（Yule-Walker 估计）的理论依据，也在谱密度估计、偏自相关函数计算及模型定阶（利用 ACF/PACF）中起基础作用。其解的唯一性保证了估计的良定义性。

## 课堂问答

**老师**：AR 系数与自协方差之间为什么存在这组方程，解为什么唯一？

**学生**：结论是把 AR 方程两边乘 $X_{t-h}$ 取期望，由因果性 $\mathbb{E}[\varepsilon_tX_{t-h}]=0$（$h\ge1$）得 $\gamma(h)=\phi_1\gamma(h-1)+\cdots+\phi_p\gamma(h-p)$；取 $h=1,\dots,p$ 即 $\boldsymbol{\Gamma}_p\boldsymbol{\phi}=\boldsymbol{\gamma}_p$。平稳过程 $\boldsymbol{\Gamma}_p$ 正定，故 $\boldsymbol{\phi}=\boldsymbol{\Gamma}_p^{-1}\boldsymbol{\gamma}_p$ 存在唯一。误区：$\gamma(0)$ 不在此方程内，须另乘 $X_t$ 并用 $\mathbb{E}[X_t\varepsilon_t]=\sigma^2$ 得 $\gamma(0)=\sum_i\phi_i\gamma(i)+\sigma^2$ 联立。

**老师（追问）**：为什么 $\boldsymbol{\Gamma}_p$ 一定正定？

**学生**：$\boldsymbol{\Gamma}_p$ 是 $(X_1,\dots,X_p)$ 的协方差阵，对任意 $\boldsymbol{c}$ 有 $\boldsymbol{c}^\top\boldsymbol{\Gamma}_p\boldsymbol{c}=\operatorname{Var}(\boldsymbol{c}^\top\boldsymbol{X}_{1:p})\ge0$，平稳且无完全线性相关时严格正定，从而可逆、解唯一。

**老师（拓展）**：这套方程除了矩估计还有什么用？

**学生**：它统一了 AR 的 Yule-Walker 估计、谱密度 $\frac{\sigma^2}{2\pi|\phi(e^{-i\omega})|^2}$、偏自相关函数（Levinson-Durbin 递推解出各阶 $\phi_{kk}$）与 ACF/PACF 定阶，是 AR 建模的骨架。
