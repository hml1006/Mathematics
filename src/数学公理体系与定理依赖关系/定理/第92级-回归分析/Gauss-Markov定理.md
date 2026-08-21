# Gauss-Markov 定理

> **一句话大白话**：在所有只靠数据的线性组合来估计回归系数、又不会系统性偏掉的无偏算法里，最小二乘法给出的结果方差最小——它是最准的"线性无偏估计"。
>
> **小例子**：用身高预测体重时，无论是直接列方程、还是给每个样本加权求平均，只要保证估计不偏差，最小二乘得到的斜率与截距误差最小。

## 一、定理介绍

Gauss-Markov 定理是线性回归统计理论的核心基石。在线性回归模型 $\boldsymbol{Y} = \boldsymbol{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ 的经典假设下，最小二乘估计 $\hat{\boldsymbol{\beta}}_{\text{OLS}} = (\boldsymbol{X}^\top \boldsymbol{X})^{-1}\boldsymbol{X}^\top \boldsymbol{Y}$ 是所有线性无偏估计中最"高效"的，即它在协方差矩阵的半正定意义下最小。

## 二、原理思路

其思想源于将任意线性无偏估计 $\tilde{\boldsymbol{\beta}} = \boldsymbol{A}\boldsymbol{Y}$ 分解为"最小二乘分量＋正交扰动项"。由于无偏性迫使 $\boldsymbol{A}\boldsymbol{X} = \boldsymbol{I}$，扰动项 $\boldsymbol{D}$ 必须满足 $\boldsymbol{D}\boldsymbol{X} = \boldsymbol{0}$，而这个扰动只会额外增加方差而不会带来任何好处，从而证明 OLS 最优。

## 三、定理的严格表述

### 定理

设线性模型 $\boldsymbol{Y} = \boldsymbol{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ 满足：线性性、严格外生性 $\mathbb{E}[\boldsymbol{\varepsilon} \mid \boldsymbol{X}] = \boldsymbol{0}$、同方差 $\text{Var}(\varepsilon_i) = \sigma^2$、无自相关、且 $\text{rank}(\boldsymbol{X}) = p+1 < n$。则对任意线性无偏估计 $\tilde{\boldsymbol{\beta}}$：

$$
\text{Var}(\tilde{\boldsymbol{\beta}}) = \sigma^2 \boldsymbol{A}\boldsymbol{A}^\top = \sigma^2\big[(\boldsymbol{X}^\top \boldsymbol{X})^{-1} + \boldsymbol{D}\boldsymbol{D}^\top\big] \ge \text{Var}(\hat{\boldsymbol{\beta}}_{\text{OLS}}).
$$

即 $\hat{\boldsymbol{\beta}}_{\text{OLS}}$ 是最优线性无偏估计（BLUE）。

## 四、证明过程

1. **无偏条件**：$\mathbb{E}[\tilde{\boldsymbol{\beta}}] = \boldsymbol{A}\boldsymbol{X}\boldsymbol{\beta} = \boldsymbol{\beta}$ 对一切 $\boldsymbol{\beta}$ 成立，故 $\boldsymbol{A}\boldsymbol{X} = \boldsymbol{I}$。
2. **分解**：令 $\boldsymbol{D} = \boldsymbol{A} - (\boldsymbol{X}^\top \boldsymbol{X})^{-1}\boldsymbol{X}^\top$，则 $\boldsymbol{D}\boldsymbol{X} = \boldsymbol{0}$ 且 $\boldsymbol{X}^\top \boldsymbol{D}^\top = \boldsymbol{0}$。
3. **方差计算**：利用 $\text{Var}(\boldsymbol{Y}) = \sigma^2\boldsymbol{I}$ 得
   $$
   \text{Var}(\tilde{\boldsymbol{\beta}}) = \sigma^2\boldsymbol{A}\boldsymbol{A}^\top = \sigma^2[(\boldsymbol{X}^\top \boldsymbol{X})^{-1} + \boldsymbol{D}\boldsymbol{D}^\top].
   $$
4. **半正定比较**：由于 $\boldsymbol{D}\boldsymbol{D}^\top$ 半正定，对任意 $\boldsymbol{c}$ 有 $\boldsymbol{c}^\top \text{Var}(\tilde{\boldsymbol{\beta}})\boldsymbol{c} \ge \boldsymbol{c}^\top \text{Var}(\hat{\boldsymbol{\beta}}_{\text{OLS}})\boldsymbol{c}$。

## 五、应用与意义

Gauss-Markov 定理保证了最小二乘法在线性无偏估计类中的最优性，为经典回归推断提供了理论基础。当假设被违背（如异方差、自相关）时，它自然引出加权最小二乘（WLS）与广义最小二乘（GLS）的动机——通过对数据进行线性变换恢复"同方差"条件后再套用该定理，从而保持最优性。