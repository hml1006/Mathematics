# Lasso 的变量选择一致性

> **一句话大白话**：Lasso 用带尖角的 $L_1$ 惩罚，能把不重要的系数直接压成 0，实现"自动选变量"；在样本足够多、条件合适时，它选出的变量组合会收敛到真实的重要变量集合。
>
> **小例子**：一堆可能影响房价的变量中许多是无关的，Lasso 会把它们的系数变成 0，只留下真正有关的少数几个，并且样本够大时几乎总能选对。

## 一、定理介绍

> **前置依赖**：线性回归模型、$L_1$ 范数与凸优化、K.K.T. 条件、大数定律与概率收敛、不可表示条件、相合性

Lasso 用 $L_1$ 惩罚进行收缩与变量选择，其估计为 $\hat{\boldsymbol{\beta}}_{\text{Lasso}} = \arg\min_{\boldsymbol{\beta}}\frac{1}{2n}\|\boldsymbol{Y}-\boldsymbol{X}\boldsymbol{\beta}\|^2 + \lambda_n\|\boldsymbol{\beta}\|_1$。在一定条件下，Lasso 具有**变量选择一致性**：以趋于 1 的概率正确识别重要变量的集合。

## 二、原理思路

Lasso 解的 K.K.T. 条件刻画出"非重要变量的内积被约束在 $\lambda_n$ 以内"的机制。关键的**不可表示条件**（Irrepresentable Condition）保证非重要变量对重要变量的"相关性投影"足够小，使得 oracle 估计（已知真实变量）能满足 K.K.T.，从而与 Lasso 解重合，进而实现精确变量选择。

## 三、定理的严格表述

设真实参数 $\boldsymbol{\beta}^* = (\boldsymbol{\beta}_1^{*\top}, \boldsymbol{\beta}_2^{*\top})^\top$，$\boldsymbol{\beta}_1^*\neq\boldsymbol{0}$，$\boldsymbol{\beta}_2^*=\boldsymbol{0}$。若满足：

1. 不可表示条件：$\big|\boldsymbol{X}_2^\top\boldsymbol{X}_1(\boldsymbol{X}_1^\top\boldsymbol{X}_1)^{-1}\operatorname{sign}(\boldsymbol{\beta}_1^*)\big| < \boldsymbol{1}-\eta$（逐元素）；
2. $\lambda_n\to0$ 且 $\sqrt{n}\lambda_n\to\infty$；
3. $\boldsymbol{X}_1^\top\boldsymbol{X}_1/n \to \boldsymbol{C}$（正定）；

则 Lasso 具有变量选择一致性：

$$
\mathbb{P}\big(\{j:\hat{\beta}_j\neq0\} = \{j:\beta_j^*\neq0\}\big) \to 1,\quad n\to\infty.
$$

## 四、证明过程

1. **K.K.T. 条件**：对 $\hat\beta_j\neq0$ 有 $\frac{1}{n}\boldsymbol{X}_j^\top(\boldsymbol{Y}-\boldsymbol{X}\hat{\boldsymbol{\beta}}) = \lambda_n\operatorname{sign}(\hat\beta_j)$；对 $\hat\beta_j=0$ 有 $|\frac{1}{n}\boldsymbol{X}_j^\top(\boldsymbol{Y}-\boldsymbol{X}\hat{\boldsymbol{\beta}})| \le \lambda_n$。
2. **Oracle 估计**：$\hat{\boldsymbol{\beta}}_1^{\text{oracle}} = (\boldsymbol{X}_1^\top\boldsymbol{X}_1)^{-1}\boldsymbol{X}_1^\top\boldsymbol{Y}$，$\hat{\boldsymbol{\beta}}_2^{\text{oracle}} = \boldsymbol{0}$。
3. **重合性**：在不可表示条件下存在 $\lambda_n$ 使 oracle 解满足 K.K.T.，故与 Lasso 解重合。
4. **概率收敛**：由 $\sqrt{n}\lambda_n\to\infty$ 得 oracle 估计相合，结合不可表示条件，非重要变量系数被精确压零，最终收敛到真实变量集合概率趋于 1。

## 五、应用与意义

Lasso 是稀疏高维回归与变量选择的核心工具，广泛应用于基因组、信号处理与机器学习稀疏建模。其变量选择一致性揭示了"何时能真正选对变量"的充分条件，也说明当不可表示条件被违反时 Lasso 可能失效，从而启发弹性网（Elastic Net）、自适应 Lasso 等改进。