# Box-Jenkins 方法的一步预测

> **一句话大白话**：给定到现在的历史数据，预测下一个时刻最准的做法是取"条件平均数"——把已知的过去和可估计的噪声代进去，得到最小均方误差意义下的最优预测。
>
> **小例子**：用过去 30 天的销售量预测明天，最优预测不是拍脑袋，而是按 ARMA 模型把近期销量和近几天"意外"（噪声残差）加权求和。

## 一、定理介绍

对 ARMA($p,q$) 过程 $\phi(B)X_t=\theta(B)\varepsilon_t$，给定 $\mathcal{F}_t = \{X_1,\dots,X_t\}$，最小均方误差一步预测为

$$
\hat{X}_{t+1|t} = \phi_1X_t + \cdots + \phi_pX_{t-p+1} + \theta_1\hat{\varepsilon}_t + \cdots + \theta_q\hat{\varepsilon}_{t-q+1},
$$

其中 $\hat{\varepsilon}_s = X_s - \hat{X}_{s|s-1}$ 为预测残差，且预测误差方差为 $\sigma^2$。

## 二、原理思路

在均方误差准则下，最优预测是条件期望 $\mathbb{E}[X_{t+1}\mid\mathcal{F}_t]$。由于 $\varepsilon_{t+1}$ 与 $\mathcal{F}_t$ 独立且条件期望为零，条件期望只保留可由过去确定的部分；不可观测的新息 $\varepsilon$ 用递推残差 $\hat{\varepsilon}$ 近似。

## 三、定理的严格表述

由 ARMA 方程

$$
X_{t+1} = \phi_1X_t + \cdots + \phi_pX_{t-p+1} + \varepsilon_{t+1} + \theta_1\varepsilon_t + \cdots + \theta_q\varepsilon_{t-q+1},
$$

取条件期望得最优一步预测

$$
\hat{X}_{t+1|t} = \mathbb{E}[X_{t+1}\mid\mathcal{F}_t] = \phi_1X_t + \cdots + \phi_pX_{t-p+1} + \theta_1\hat{\varepsilon}_t + \cdots + \theta_q\hat{\varepsilon}_{t-q+1},
$$

且一步预测误差 $e_{t+1|t} = X_{t+1} - \hat{X}_{t+1|t} = \varepsilon_{t+1}$，方差为 $\sigma^2$。

## 四、证明过程

1. **写出预测形式**：展开 $X_{t+1}$ 的 ARMA 表达式。
2. **最优预测**：由 $\varepsilon_{t+1}$ 与 $\mathcal{F}_t$ 独立、$\mathbb{E}[\varepsilon_{t+1}\mid\mathcal{F}_t]=0$，取条件期望消去 $\varepsilon_{t+1}$。
3. **残差递推**：$\varepsilon_s$ 不可观测，用 $\hat{\varepsilon}_s = X_s - \hat{X}_{s|s-1}$ 逐步估计。
4. **误差方差**：$e_{t+1|t}=\varepsilon_{t+1}$，故 $\text{Var}(e_{t+1|t})=\sigma^2$。
5. **多步推广**：$k$ 步预测按条件期望线性递推，$s>t$ 时 $\hat{\varepsilon}_{s|t}=0$。

## 五、应用与意义

Box-Jenkins 方法的一步（及多步）预测是时间序列预测的支柱，广泛应用于经济预测、销售预测、信号处理等。它确立了"最小均方误差"框架下条件期望即最优预测的原则，并通过残差递推将不可观测的新息转化为可计算量，是模型识别、估计与预测一体化的理论核心。