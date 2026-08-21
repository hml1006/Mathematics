# GMM估计量的渐近性质

> **一句话大白话**：当你想用一堆矩条件（"样本平均应为零"）来估计参数时，广义矩方法（GMM）会把所有条件揉成一个加权二次型最小化，它保持一致与渐近正态，而且选对权重矩阵还能让方差最小。
>
> **小例子**：矩条件 $\mathbb{E}[g(w_i,\theta_0)]=0$ 的样本平均 $\bar g(\theta)$ 在真值处应接近零。GMM 最小化 $\bar g(\theta)'W\bar g(\theta)$；当 $W$ 取最优权矩阵 $S^{-1}$（$S$ 为样本矩方差）时，估计量的渐近方差最小。

## 一、定理介绍

> **前置依赖**：大数定律、中心极限定理、Slutsky定理、泰勒展开、矩阵求逆与正定性

GMM（广义矩方法）估计的渐近性质是计量经济学推断的核心定理。对矩条件 $\mathbb{E}[g(w_i,\theta_0)]=0$，GMM 估计
$$
\hat\theta_{\text{GMM}}=\arg\min_\theta \bar g(\theta)'\hat W\bar g(\theta),\qquad \bar g(\theta)=\tfrac1n\sum_ig(w_i,\theta),
$$
在正则条件下保持一致、渐近正态；当 $\hat W$ 收敛于最优权矩阵 $W=S^{-1}$ 时达到最小渐近方差。

## 二、原理思路

一致性用"目标函数的一致收敛 + 极限目标在真值处唯一取最小"。因 $\bar g\xrightarrow{p}\mathbb{E}g$ 且 $\hat W\xrightarrow{p}W$，目标 $Q_n(\theta)\xrightarrow{p}Q_\infty(\theta)$；矩阵件使 $Q_\infty(\theta_0)=0$，识别条件使 $\theta\ne\theta_0$ 时 $Q_\infty(\theta)>0$，故最小点收敛到 $\theta_0$。渐近正态性对一阶条件做泰勒展开、用 CLT 与 Slutsky 得到正态分布，显式给出"三明治"渐近方差，并指出最优权重消去夹心项。

## 三、定理的严格表述

设 $\theta_0$ 满足矩条件，$G=\mathbb{E}[\partial g(w_i,\theta_0)/\partial\theta']$，$S=\lim_n\text{Var}(\sqrt n\,\bar g(\theta_0))$，$\hat W\xrightarrow{p}W>0$。则

1. $\hat\theta\xrightarrow{p}\theta_0$；
2. $\sqrt n(\hat\theta-\theta_0)\xrightarrow{d}N\!\big(0,\,(G'WG)^{-1}G'WSWG(G'WG)^{-1}\big)$；
3. 当 $W=S^{-1}$ 时渐近方差取最小 $ (G'S^{-1}G)^{-1}$。

## 四、证明过程

**步骤1：一致性。** $Q_n(\theta)=\bar g(\theta)'\hat W\bar g(\theta)\xrightarrow{p}Q_\infty(\theta)=\mathbb{E}g(\theta)'W\mathbb{E}g(\theta)$；$Q_\infty(\theta_0)=0$，识别使 $\theta\ne\theta_0$ 时 $Q_\infty>0$。由一致收敛（随机等度连续）与唯一最小性，$\hat\theta\xrightarrow{p}\theta_0$。

**步骤2：一阶条件。** $\frac{\partial Q_n}{\partial\theta}=2\hat G(\hat\theta)'\hat W\bar g(\hat\theta)=0$，其中 $\hat G(\theta)=\frac1n\sum_i\frac{\partial g(w_i,\theta)}{\partial\theta'}$。

**步骤3：均值展开。** 对 $\bar g(\hat\theta)$ 在 $\theta_0$ 处泰勒展开 $\bar g(\hat\theta)=\bar g(\theta_0)+\hat G(\bar\theta)(\hat\theta-\theta_0)$。

**步骤4：求解偏差。** 代入一阶条件得
$$
\sqrt n(\hat\theta-\theta_0)=-[\hat G(\hat\theta)'\hat W\hat G(\bar\theta)]^{-1}\hat G(\hat\theta)'\hat W\sqrt n\,\bar g(\theta_0).
$$

**步骤5：渐近正态性。** 由一致性 $\hat G\xrightarrow{p}G$，由 CLT $\sqrt n\,\bar g(\theta_0)\xrightarrow{d}N(0,S)$，Slutsky 给出三明治渐近方差。

**步骤6：最优权重。** 当 $W=S^{-1}$，渐近方差化为 $(G'S^{-1}G)^{-1}$，为所有 $W$ 中最小（正定序意义下）。

**结论（$\square$）**：GMM 一致、渐近正态，最优权重 $S^{-1}$ 达最小方差。

## 五、应用与意义

GMM 是极灵活的估计框架，把 IV、2SLS、随机效应等纳入统一理论，广泛应用于金融（资产定价矩条件）、劳动经济与实证宏观。其三明治方差直接催生了稳健标准误（HAC）实践，是计量推断工具箱的支柱方法之一。