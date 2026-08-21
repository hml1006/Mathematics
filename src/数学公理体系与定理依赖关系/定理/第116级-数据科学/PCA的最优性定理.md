# PCA的最优性定理

> **一句话大白话**：让数据投到某方向后“拉开得最开”（方差最大）的那个方向，正是协方差矩阵最大特征值对应的特征向量。
>
> **小例子**：一堆点在二维里斜着分布，PCA 找到的“第一主轴”就是协方差矩阵最大特征值对应的方向，投上去方差最大、信息保留最多。

## 一、定理介绍

主成分分析（PCA）寻找使投影后方差最大的正交方向。该定理用 Lagrange 乘子法证明：单位方向 $\boldsymbol w$ 上投影方差 $\boldsymbol w^\top\boldsymbol S\boldsymbol w$ 的最大值正是协方差矩阵 $\boldsymbol S$ 的最大特征值，极值方向即对应特征向量。

## 二、原理思路

把“方差最大”写成带约束的优化问题，用 Lagrange 乘子法求驻点，得到的驻点方程恰是特征值方程 $\boldsymbol S\boldsymbol w=\lambda\boldsymbol w$。最大特征值给出最大方差，其对应特征向量即第一主成分方向，后续方向据正交约束依次取最大特征值。

## 三、定理的严格表述

设 $\boldsymbol X\in\mathbb{R}^{n\times p}$ 为中心化数据矩阵，$\boldsymbol S=\frac1n\boldsymbol X^\top\boldsymbol X$ 为样本协方差矩阵，则第一主成分方向是如下问题的解
$$
\max_{\|\boldsymbol w\|=1}\boldsymbol w^\top\boldsymbol S\boldsymbol w,
$$
且 $\boldsymbol w_1$ 为 $\boldsymbol S$ 最大特征值对应的特征向量。

## 四、证明过程

1. **建模**。投影后方差为
   $$
   \mathrm{Var}(\boldsymbol X\boldsymbol w)=\frac1n\|\boldsymbol X\boldsymbol w\|^2=\boldsymbol w^\top\boldsymbol S\boldsymbol w.
   $$
2. **Lagrange 函数**。$\mathcal L(\boldsymbol w,\lambda)=\boldsymbol w^\top\boldsymbol S\boldsymbol w-\lambda(\boldsymbol w^\top\boldsymbol w-1)$。
3. **驻点方程**。对 $\boldsymbol w$ 求导并设零，
   $$
   \frac{\partial\mathcal L}{\partial\boldsymbol w}=2\boldsymbol S\boldsymbol w-2\lambda\boldsymbol w=\boldsymbol 0\;\Longrightarrow\;\boldsymbol S\boldsymbol w=\lambda\boldsymbol w.
   $$
4. **最优值**。代入目标函数得 $\boldsymbol w^\top\boldsymbol S\boldsymbol w=\lambda$，故最大特征值对应最大方差，特征向量即最优方向。

## 五、应用与意义

PCA 用于降维、特征提取与数据可视化，在图像处理、基因组学与金融中有广泛用途。该定理揭示“降维即谱分解”，并把最优性归约为对称矩阵的特征问题，是机器学习与统计学习的基本结果。