# Cox比例风险模型的部分似然估计

> **一句话大白话**：在生存分析里，不必精确估计"随时间变化的基线风险"，只用"比例风险"思想去掉基线项，靠比排序似然（部分似然）就能估计每种的协变量（药物、年龄）如何成倍改变风险，且估计一致、渐近正态。
>
> **小例子**：Cox 模型 $h(t|X)=h_0(t)e^{\beta'X}$ 的部分似然只依赖每个事件时刻"风险集内谁的风险更大"，基线 $h_0(t)$ 被分子分母抵消。系数 $\beta$ 的危险比 $e^\beta$ 表示协变量每加一单位风险倍数。

## 一、定理介绍

Cox 比例风险模型的部分似然估计算法是生存分析的核心方法。对风险函数
$$
h(t|X)=h_0(t)\exp(\beta'X),
$$
基于带删失的观测 $(T_i,\delta_i,X_i)$，部分似然
$$
L(\beta)=\prod_{i:\delta_i=1}\frac{e^{\beta'X_i}}{\sum_{j\in R(t_i)}e^{\beta'X_j}},\qquad R(t)=\{j:T_j\ge t\},
$$
其在正则条件下的最大化估计 $\hat\beta$ 是一致且渐近正态的。

## 二、原理思路

关键在于"去看每个事件时刻的条件概率"。给定风险集 $R(t_i)$，事件恰发生在个体 $i$ 上的条件概率为
$$
\frac{h(t_i|X_i)}{\sum_{j\in R(t_i)}h(t_i|X_j)}=\frac{h_0e^{\beta'X_i}}{\sum_j h_0e^{\beta'X_j}}=\frac{e^{\beta'X_i}}{\sum_j e^{\beta'X_j}},
$$
基线 $h_0$ 相消，得到不依赖基线的部分似然。估计量的渐近性质用**计数过程 + 鞅中心极限定理**建立：得分函数可写成鞅积分。

## 三、定理的严格表述

设观测 $(T_i,\delta_i,X_i)$ 独立同分布，部分似然 $L(\beta)$ 如上。定义对数部分似然 $\ell(\beta)$、得分 $U(\beta)=\partial\ell/\partial\beta$ 与观察信息 $I(\beta)=-\partial^2\ell/\partial\beta\partial\beta'$。正则条件下 $\hat\beta$ 满足 $U(\hat\beta)=0$，且
$$
\sqrt n(\hat\beta-\beta_0)\xrightarrow{d}N\!\big(0,\mathcal{I}(\beta_0)^{-1}\big),
$$
即 $\hat\beta\xrightarrow{p}\beta_0$ 且渐近正态。

## 四、证明过程

**步骤1：部分似然推导。** 条件概率式相消 $h_0$，非事件个体不贡献，连乘得 $L(\beta)$。

**步骤2：对数部分似然与得分。** 定义加权平均 $\bar X(\beta,t)=\frac{\sum_{j\in R(t)}X_je^{\beta'X_j}}{\sum_{j\in R(t)}e^{\beta'X_j}}$，得分
$$
U(\beta)=\sum_{i:\delta_i=1}\big[X_i-\bar X(\beta,t_i)\big].
$$

**步骤3：信息矩阵。** $I(\beta)=\sum_{i:\delta_i=1}\big[\frac{\sum_jX_jX_j'e^{\beta'X_j}}{\sum_j e^{\beta'X_j}}-\bar X\bar X'\big]=\sum_{i:\delta_i=1}\text{Var}_{R(t_i)}(X)$。

**步骤4：鞅框架。** 计数过程 $N_i(t)=\mathbf1_{\{T_i\le t,\delta_i=1\}}$、风险过程 $Y_i(t)=\mathbf1_{\{T_i\ge t\}}$，补偿子 $\Lambda_i(t)=\int_0^tY_i(s)h_0(s)e^{\beta'X_i}ds$，$M_i=N_i-\Lambda_i$ 为鞅。

**步骤5：得分函数的鞅表示。** $U(\beta)=\sum_i\int_0^\infty[X_i-\bar X(\beta,s)]\,dM_i(s)$；鞅积分的期望为零，鞅中心极限定理给出 $n^{-1/2}U(\beta_0)\xrightarrow{d}N(0,\mathcal I)$。

**步骤6：一致性。** $n^{-1}I(\beta)\xrightarrow{p}\mathcal I(\beta)$ 由大数定律与鞅收敛给出，M-估计理论给出 $\hat\beta\xrightarrow{p}\beta_0$。

**步骤7：渐近正态性。** 对得分泰勒展开 $0=U(\hat\beta)=U(\beta_0)+\frac{\partial U(\bar\beta)}{\partial\beta'}(\hat\beta-\beta_0)$，结合一致性、鞅 CLT 与 Slutsky：
$$
\sqrt n(\hat\beta-\beta_0)=(-n^{-1}U'(\bar\beta))^{-1}n^{-1/2}U(\beta_0)\xrightarrow{d}N(0,\mathcal I^{-1}).
$$

**结论（$\square$）**：部分似然估计一致且渐近正态。

## 五、应用与意义

Cox 模型是临床与流行病学生存分析的标准方法，广泛用于临床试验、药物疗效与预后因素分析。其"部分似然"思想无需估计基线风险，极大简化推断；结合鞅理论的稳健标准误与检验，已成生存分析最常用的回归工具。