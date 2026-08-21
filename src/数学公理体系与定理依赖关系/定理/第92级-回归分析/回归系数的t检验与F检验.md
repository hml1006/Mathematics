# 回归系数的 t 检验与 F 检验

> **一句话大白话**：做回归后要判断"某个变量到底有没有用"以及"整体模型到底行不行"，就分别用 t 检验和 F 检验，它们都基于正态假设下的精确分布。
>
> **小例子**：评估房价模型时，t 检验回答"面积这一项是否真的影响价格"，F 检验回答"面积、卧室数、房龄放在一起是否整体上解释了价格变化"。

## 一、定理介绍

> **前置依赖**：正态线性回归模型、估计量分布（正态性）、卡方分布、t 分布与 F 分布、帽子矩阵与幂等性、独立性

在正态线性回归模型 $\boldsymbol{Y} = \boldsymbol{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$（$\boldsymbol{\varepsilon} \sim N(\boldsymbol{0}, \sigma^2 \boldsymbol{I}_n)$）下，回归系数的估计量服从正态分布，其可导出用于单个系数检验的 $t$ 统计量与用于整体显著性检验的 $F$ 统计量，二者均可用精确分布做推断。

## 二、原理思路

核心在于残差平方和 $\text{SSE}$ 服从卡方分布且与回归系数估计独立。由 $\hat{\boldsymbol{\beta}} \sim N(\boldsymbol{\beta}, \sigma^2(\boldsymbol{X}^\top\boldsymbol{X})^{-1})$，标准化后的系数是标准正态量；而 $\text{SSE}/\sigma^2 \sim \chi^2_{n-p-1}$，二者相除即得 $t$ 分布。$F$ 统计量则是两个独立卡方量之比，服从 $F$ 分布。

## 三、定理的严格表述

### t 检验

对单个系数 $H_0: \beta_j = \beta_j^{(0)}$，用统计量

$$
t = \frac{\hat{\beta}_j - \beta_j^{(0)}}{\text{SE}(\hat{\beta}_j)} \sim t_{n-p-1},
$$

其中 $\text{SE}(\hat{\beta}_j) = \hat{\sigma}\sqrt{[(\boldsymbol{X}^\top\boldsymbol{X})^{-1}]_{jj}}$，$\hat{\sigma}^2 = \frac{\text{SSE}}{n-p-1}$。

### F 检验

对整体显著性 $H_0: \beta_1 = \cdots = \beta_p = 0$，用统计量

$$
F = \frac{\text{SSR}/p}{\text{SSE}/(n-p-1)} \sim F_{p, n-p-1}.
$$

## 四、证明过程

1. **系数的分布**：由 $\boldsymbol{Y} \sim N(\boldsymbol{X}\boldsymbol{\beta}, \sigma^2\boldsymbol{I})$ 与线性变换得 $\hat{\boldsymbol{\beta}} \sim N(\boldsymbol{\beta}, \sigma^2(\boldsymbol{X}^\top\boldsymbol{X})^{-1})$。
2. **卡方分布**：残差 $\hat{\boldsymbol{\varepsilon}} = (\boldsymbol{I} - \boldsymbol{H})\boldsymbol{Y}$，由帽子矩阵 $\boldsymbol{H}$ 的幂等性可证 $\text{SSE}/\sigma^2 \sim \chi^2_{n-p-1}$，且 $\hat{\boldsymbol{\beta}}$ 与 $\hat{\sigma}^2$ 独立。
3. **$t$ 统计量**：$\hat{\beta}_j$ 标准化后为正态量，除以独立卡方量的自由度根即得 $t$ 分布。
4. **$F$ 统计量**：$H_0$ 下 $\text{SSR}/\sigma^2 \sim \chi^2_p$ 且与 $\text{SSE}$ 独立，二者之比服从 $F_{p,n-p-1}$。

## 五、应用与意义

$t$ 检验用于判断单个解释变量是否显著，是变量筛选（逐步回归）的基础；$F$ 检验用于判断模型整体是否比仅含截距的零模型更有解释力，是方差分析（ANOVA）表的核心。二者共同构成经典回归规范推断的标准工具。