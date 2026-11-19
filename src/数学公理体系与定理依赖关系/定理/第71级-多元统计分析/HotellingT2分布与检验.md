# Hotelling $T^2$ 分布与检验

> **一句话大白话**：一元正态总体用 $t$ 统计量检验一个均值，多元正态总体就把多个方向的距离合成一个 $T^2$；在正态假设下，它的分布可以精确换算成 $F$ 分布。
>
> **小例子**：同时测量一批产品的长度和重量，要检验总体均值是否为 $(\mu_{10},\mu_{20})$。计算样本均值与目标均值之间、按样本协方差校正后的距离，若 $T^2$ 超过 $F$ 分布给出的临界值，就拒绝原假设。

## 介绍

Hotelling $T^2$ 是 Student $t^2$ 的多元推广，用于检验多元正态总体的均值向量，也可构造均值的置信椭球。以下结论是**有限样本精确分布结论**，不是依靠大样本得到的卡方近似。

## 分析

**前置依赖**：多元正态分布、样本均值与样本协方差的独立性、Wishart 分布、卡方分布与 $F$ 分布、正定矩阵。

**定理内容**：设 $\boldsymbol X_1,\ldots,\boldsymbol X_n$ 独立同分布于 $N_p(\boldsymbol\mu,\boldsymbol\Sigma)$，其中 $\boldsymbol\Sigma\succ0$ 且 $n>p$。记

$$
\overline{\boldsymbol X}=\frac1n\sum_{i=1}^n\boldsymbol X_i,\qquad
\boldsymbol S=\frac1{n-1}\sum_{i=1}^n(\boldsymbol X_i-\overline{\boldsymbol X})(\boldsymbol X_i-\overline{\boldsymbol X})^\top .
$$

在原假设 $H_0:\boldsymbol\mu=\boldsymbol\mu_0$ 下，定义

$$
T^2=n(\overline{\boldsymbol X}-\boldsymbol\mu_0)^\top
\boldsymbol S^{-1}(\overline{\boldsymbol X}-\boldsymbol\mu_0),
$$

则有精确分布

$$
\frac{n-p}{p(n-1)}T^2\sim F_{p,n-p},
\qquad\text{等价地}\qquad
T^2\sim\frac{p(n-1)}{n-p}F_{p,n-p}.
$$

因此显著性水平为 $\alpha$ 的检验在

$$
T^2>\frac{p(n-1)}{n-p}F_{p,n-p}(1-\alpha)
$$

时拒绝 $H_0$；相应的 $1-\alpha$ 置信椭球由把上述不等式反向、并把 $\boldsymbol\mu_0$ 换成待定的 $\boldsymbol\mu$ 得到。

## 思考过程

一元情形中，样本均值的标准化误差提供分子卡方，独立样本方差提供分母卡方。多元情形只是把标量方差换成 Wishart 矩阵，并用 $\boldsymbol S^{-1}$ 同时校正各方向的尺度和相关性。

条件 $n>p$ 保证 $n-1\ge p$，样本协方差矩阵几乎必然 可逆。若忽略有限自由度，直接把 $T^2$ 当作 $\chi_p^2$，那通常只是 $n\to\infty$ 时的渐近近似，而不是这里所说的精确检验。

## 证明过程

令 $\boldsymbol z=\sqrt n\,\boldsymbol\Sigma^{-1/2}(\overline{\boldsymbol X}-\boldsymbol\mu_0)$，并令 $\boldsymbol W=\boldsymbol\Sigma^{-1/2}((n-1)\boldsymbol S)\boldsymbol\Sigma^{-1/2}$。正态样本理论给出

$$
\boldsymbol z\sim N_p(\boldsymbol0,\boldsymbol I_p),\qquad
\boldsymbol W\sim W_p(\boldsymbol I_p,n-1),
$$

且二者独立，同时 $T^2=(n-1)\boldsymbol z^\top\boldsymbol W^{-1}\boldsymbol z$。

对 $\boldsymbol z$ 作旋转可把该二次型化为独立卡方变量的比，得到标准正态—Wishart 恒等式

$$
T^2\overset{d}= (n-1)\frac{\chi_p^2}{\chi_{n-p}^2},
$$

其中分子与分母独立。再利用

$$
F_{p,n-p}\overset{d}=\frac{\chi_p^2/p}{\chi_{n-p}^2/(n-p)},
$$

便得到 $\frac{n-p}{p(n-1)}T^2\sim F_{p,n-p}$。当 $p=1$ 时，此式退化为通常的 $t_{n-1}^2=F_{1,n-1}$。$\square$

## 课堂问答

**老师**：Hotelling $T^2$ 检验为什么要用 $F$ 分布，而不直接用卡方分布？

**学生**：因为协方差矩阵也由同一份样本估计，估计它带来了额外的不确定性。在 $n>p$ 的正态模型中，精确关系是 $\frac{n-p}{p(n-1)}T^2\sim F_{p,n-p}$；只有样本量增大、估计协方差的不确定性相对减小时，才常用 $T^2$ 的渐近卡方近似。

**老师（追问）**：为什么要求 $n>p$？

**学生**：散布矩阵的自由度是 $n-1$，要使它几乎必然 满秩，需要 $n-1\ge p$。否则 $\boldsymbol S$ 奇异，通常形式的 $\boldsymbol S^{-1}$ 和相应的 $F$ 校准都不能直接使用。

**老师（拓展）**：这个精确公式是否也适用于任意非正态样本？

**学生**：不能原样套用。$F$ 分布结论依赖正态性带来的样本均值与样本协方差独立、以及 Wishart 分布。非正态大样本可以另用中心极限定理建立渐近检验，但那是另一类命题。

## 相关条目

- [Wishart 分布的密度函数与性质](./Wishart分布的密度函数与性质.md)：给出推导 $T^2$ 精确分布所需的样本散布矩阵分布。
- [多元正态分布的最大似然估计](./多元正态分布的最大似然估计.md)：说明样本均值与样本散布矩阵如何由正态似然得到。
