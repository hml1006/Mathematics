# Meta分析中的随机效应模型

> **一句话大白话**：把所有研究（各自质量不同、真实效应也不同）的结果按"研究内抽样误差 + 研究间真实异质性"两层噪声加权合并，得到总体效应估计；当研究间结果不一致时，用随机效应模型比固定效应更保险。
>
> **小例子**：10 个试验各自估计了某种药的效果，效果大小又不完全相同。随机效应模型假设每个试验的真实效应围绕一个"总体均数"波动，用 DerSimonian-Laird 估计研究间方差 $\tau^2$ 来加权重合并，给出总体效应及置信区间（常用 $I^2$ 度量异质性）。

## 一、定理介绍

> **前置依赖**：随机效应模型、加权最小二乘、Cochran Q统计量（矩估计）、中心极限定理

Meta 分析随机效应模型合并各研究的效应估计。设研究 $i$ 观测效应 $\hat\theta_i=\theta_i+e_i$，$e_i\sim N(0,v_i)$（研究内抽样误差）；真实效应 $\theta_i=\mu+\delta_i$，$\delta_i\sim N(0,\tau^2)$（研究间异质性）。模型为
$$
\hat\theta_i=\mu+\delta_i+e_i,\qquad \mathbb E[e_i]=0,\ \text{Var}(e_i)=v_i,\ \text{Var}(\delta_i)=\tau^2.
$$
总体效应 $\mu$ 的随机效应估计为加权均值，权重 $w_i=1/(v_i+\tau^2)$。

## 二、原理思路

固定效应的缺陷是忽略研究间真实差异、只给方差 $v_i$ 的逆加权，结果区间过窄且可能误导；随机效应在权重里加入研究间方差 $\tau^2$，给离散研究更大权重、更合理地反映不确定性。$\tau^2$ 常用 DerSimonian-Laird（矩）估计：用 $Q$ 统计量与维数差得到 $\tau^2=\max(0,\frac{Q-(k-1)}{\sum w-(\sum w^2/\sum w)})$，再以 $w_i=1/(v_i+\tau^2)$ 加权，得到 $\hat\mu=\frac{\sum w_i\hat\theta_i}{\sum w_i}$ 与对应置信区间。

## 三、定理的严格表述

设 $k$ 个研究，已知观测效应 $\hat\theta_i$ 与研究内方差 $v_i$。随机效应总体效应估计
$$
\hat\mu_{\text{RE}}=\frac{\sum_i w_i\hat\theta_i}{\sum_i w_i},\qquad w_i=\frac{1}{v_i+\hat\tau^2},
$$
其中异质性方差 $\hat\tau^2$ 由（e.g.）矩估计
$$
\hat\tau^2=\max\!\Big(0,\ \frac{Q-(k-1)}{\sum_i w_i-\frac{\sum_i w_i^2}{\sum_i w_i}}\Big),\qquad Q=\sum_i w_i(\hat\theta_i-\hat\theta)^2
$$
给出（$w_i=1/v_i$，$\hat\theta=\frac{\sum w_i\hat\theta_i}{\sum w_i}$）。其方差 $\text{Var}(\hat\mu)=1/\sum_iw_i$，据此构造置信区间；研究间占比 $I^2=\frac{Q-(k-1)}{Q}$。

## 四、证明过程

**步骤1：模型与权重逻辑。** 凌导总方差 $\text{Var}(\hat\theta_i)=v_i+\tau^2$；对模型最小化 $\chi^2=\sum\frac{(\hat\theta_i-\mu)^2}{v_i+\tau^2}$，得权重 $w_i=1/(v_i+\tau^2)$ 的加权最小二乘估计。

**步骤2：DerSimonian-Laird 估计 $\tau^2$。** 用 Cochran $Q$ 统计量（固定效应残差平方和）构造矩条件 $Q\approx (k-1)+\Big(\sum w-\frac{\sum w^2}{\sum w}\Big)\tau^2$，解得 $\hat\tau^2$（截断于 0）。

**步骤3：加权估计。** 代入 $w_i=1/(v_i+\hat\tau^2)$，$\hat\mu=\sum w_i\hat\theta_i/\sum w_i$ 为广义最小加权均值的标准解。

**步骤4：方差与推断。** 给定权重视作外生时，$\text{Var}(\hat\mu)=1/\sum_iw_i$，由加权均值中心极限/正态假设构造置信区间与显著性检验。

**步骤5：异质性度量。** 定义 $I^2=\frac{Q-(k-1)}{Q}\times100\%$ 刻画"总变异中研究间比例"，与 $\tau^2$ 互补刻画异质性强度。

**结论（$\square$）**：随机效应模型以 $1/(v_i+\tau^2)$ 加权合并研究、估计 $\mu$ 并量化异质性。

## 五、应用与意义

随机效应模型是临床与流行病学 Meta 分析的标准做法，当研究间存在真实异质性时给出更稳健的合并效应与更诚实的置信区间，广泛用于循证医学证据综合、系统综述与指南制定。DerSimonian-Laird 法、$I^2$ 与 $\tau^2$ 已成为 Meta 分析报告与解释的核心术语。