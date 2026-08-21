# ROC曲线下面积（AUC）的统计性质

> **一句话大白话**：把"诊断/分类器的好坏"凝练成一个介于 0.5 和 1 之间的数（AUC）：它等于随机取一个正例比随机取一个负例得分更高的概率。AUC=0.5 等于瞎猜，≈1 则几乎完美。
>
> **小例子**：一个预测"患病/健康"的评分器，AUC=0.9 表示随机挑一个病患者、一个健康者，有 90% 的概率患者的评分高于健康者。AUC 是 ROC 曲线下的面积，与样本量无关地刻画判别力。

## 一、定理介绍

AUC（Area Under the ROC Curve）是二分类判别力的核心指标。对连续评分 $S$ 与真实标签 $D\in\{0,1\}$，AUC 统计性质的基础是
$$
\text{AUC}=P(S_1>S_0),
$$
其中 $S_1,S_0$ 分别取自正例、负例的评分。由 Mann-Whitney U 统计量可直接估计，且渐近正态，可用其区间估计与假设检验衡量判别能力。

## 二、原理思路

关键是把 AUC 与秩统计量联结。配对 $(S_1,S_0)$ "正例高于负例"的事件概率就是 AUC；其经验估计恰为非参数 Mann-Whitney U 统计（与 Wilcoxon 秩和同族）。由此，AUC 的抽样分布能通过 U 统计的渐近理论处理：U 统计是"核 $\phi= \mathbf1\{s_1>s_0\}$"的可分解统计量，一致且渐近正态，方差可由核的结构写出，可在无分布假设下做置信区间与比较检验。

## 三、定理的严格表述

设正例评分 $S_1\sim F_1$、负例评分 $S_0\sim F_0$ 独立。AUC 定义为
$$
\text{AUC}=\int F_0(s)\,dF_1(s)=P(S_1>S_0)+\tfrac12P(S_1=S_0).
$$
经验估计（Mann-Whitney 型）
$$
\widehat{\text{AUC}}=\frac{1}{n_1n_0}\sum_{i=1}^{n_1}\sum_{j=1}^{n_0}\Big[\mathbf1\{S_{1i}>S_{0j}\}+\tfrac12\mathbf1\{S_{1i}=S_{0j}\}\Big]
$$
是 U 统计量，一致且渐近正态：$\widehat{\text{AUC}}\xrightarrow{a.s.}\text{AUC}$，$\sqrt n(\widehat{\text{AUC}}-\text{AUC})\xrightarrow{d}N(0,\sigma^2)$。

## 四、证明过程

**步骤1：AUC 的概率解释。** 由 ROC 曲线面积 $=\int F_0(s)dF_1(s)=P(S_1>S_0)$（含平局半计），将积分写为对照概率。

**步骤2：为 U 统计量。** 取核 $h(S_1,S_0)=\mathbf1\{S_1>S_0\}+\frac12\mathbf1\{S_1=S_0\}$，经验平均
$$
\widehat{\text{AUC}}=\frac{1}{\binom{n_1+n_0}{n_1}}\sum_{\text{配对所有}}(h),\quad\text{等}\ \frac{1}{n_1n_0}\sum_{i,j}h(S_{1i},S_{0j}),
$$
是两样本 U 统计量。

**步骤3：一致性（大数定律推广）。** U 统计量是一致（强一致）可分的核均值，由 Hoeffding 分解与大数定律，$\widehat{\text{AUC}}\xrightarrow{a.s.}\text{AUC}$。

**步骤4：渐近正态性（U 统计 CLT）。** 由 Hoeffding 渐近正态定理：$\sqrt n(\widehat{\text{AUC}}-\text{AUC})\xrightarrow{d}N(0,\sigma^2)$，其中渐近方差由核的投影（影响函数投影）确定，$\sigma^2=\lim_n\frac{n}{n_1}\zeta_1$ 等可显式计算。

**步骤5：推断应用。** 用渐近正态构造 AUC 的置信区间与两分类器 AUC 的差检验（配对时可用 Delong 法估计方差协方差）。

**结论（$\square$）**：AUC 既是概率又可作 U 统计，一致且渐近正态。

## 五、应用与意义

AUC 是医疗诊断测试、机器学习分类器评估最常用的指标，独立于阈值选取，广泛用于肿瘤标志物、影像辅助诊断、风险预测模型的效能评价。其 U 统计的严格性质支撑了置信区间、样本量计算与判别力比较检验，使"这个检测器到底多准"有了可靠的统计回答。