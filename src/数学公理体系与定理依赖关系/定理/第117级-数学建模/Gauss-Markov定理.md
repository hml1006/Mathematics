# Gauss-Markov定理

> **一句话大白话**：在经典的线性回归假设下，最小二乘估计是所有“线性且无偏”的估计里方差最小的——俗话说是同类里的“最优”。
>
> **小例子**：用身高预测体重，OLS 估计的斜率虽然没有哪个线性无偏箭头方差更小，有偏方法（如岭回归）虽有偏但常以更大偏差换更小方差。

## 一、定理介绍

Gauss-Markov 定理是线性模型估计理论的基石。它断言：在线性模型 $\boldsymbol Y=\boldsymbol X\boldsymbol\beta+\boldsymbol\varepsilon$ 满足零均值、同方差、无自相关且 $\boldsymbol X$ 满秩时，最小二乘估计量 $\hat{\boldsymbol\beta}_{\mathrm{OLS}}$ 为 BLUE，即在所有线性无偏估计中方差最小（矩阵意义下）。

## 二、原理思路

先证 $\hat{\boldsymbol\beta}$ 线性且无偏、协方差 $\sigma^2(\boldsymbol X^\top\boldsymbol X)^{-1}$；再取任意线性无偏估计 $\boldsymbol C\boldsymbol Y$，无偏性给出 $\boldsymbol C\boldsymbol X=\boldsymbol I_p$，最后用半正定矩阵方法证明其协方差与 OLS 之差半正定。

## 三、定理的严格表述

在线性模型 $\boldsymbol Y=\boldsymbol X\boldsymbol\beta+\boldsymbol\varepsilon$ 中，设
1. $\mathbb{E}[\boldsymbol\varepsilon]=\boldsymbol 0$；
2. $\mathrm{Var}(\boldsymbol\varepsilon)=\sigma^2\boldsymbol I_n$；
3. $\boldsymbol X$ 非随机且满列秩 $r=\mathrm{rank}(\boldsymbol X)=p<n$。

则最小二乘估计量 $\hat{\boldsymbol\beta}=(\boldsymbol X^\top\boldsymbol X)^{-1}\boldsymbol X^\top\boldsymbol Y$ 是 BLUE。

## 四、证明过程

1. **线性无偏**。设 $\boldsymbol A=(\boldsymbol X^\top\boldsymbol X)^{-1}\boldsymbol X^\top$，
   $$
   \mathbb{E}[\hat{\boldsymbol\beta}]=\boldsymbol\beta+\boldsymbol A\,\mathbb{E}[\boldsymbol\varepsilon]=\boldsymbol\beta.
   $$
2. **协方差**。$\mathrm{Var}(\hat{\boldsymbol\beta})=\boldsymbol A\,\mathrm{Var}(\boldsymbol Y)\boldsymbol A^\top=\sigma^2(\boldsymbol X^\top\boldsymbol X)^{-1}$。
3. **任意线性无偏估计**。设 $\tilde{\boldsymbol\beta}=\boldsymbol C\boldsymbol Y$，无偏性给出 $\boldsymbol C\boldsymbol X=\boldsymbol I_p$。
4. **比较方差**。记 $\boldsymbol D=\boldsymbol C-\boldsymbol A$，由 $\boldsymbol D\boldsymbol X=(\boldsymbol C-\boldsymbol A)\boldsymbol X=\boldsymbol I-\boldsymbol I=\boldsymbol 0$，
   $$
   \mathrm{Var}(\tilde{\boldsymbol\beta})-\mathrm{Var}(\hat{\boldsymbol\beta})
   =\sigma^2\boldsymbol D\boldsymbol D^\top\succeq\boldsymbol 0.
   $$
   故 OLS 方差最小，为 BLUE。

## 五、应用与意义

Gauss-Markov 定理为回归分析的效率理论提供了基准，是计量经济、统计学与机器学习线性模型的地基。它也明确界定了“OLS 为何难以被线性无偏替代”，并引出岭回归、LASSO 等有偏但更稳健的方法。