# Rademacher复杂度的泛化界

> **一句话大白话**：泛化误差的"额外成本"可以用假设空间拟合随机符号的能力（Rademacher 复杂度 $\mathfrak{R}_n$）来度量，数据越规整、族越简单，这个界越紧。
>
> **小例子**：对单位球 RKHS 一类函数，$\mathfrak{R}_n\le \Lambda/\sqrt{n}$，代入界式得到 $R(h)\le\hat{R}_n(h)+O(1/\sqrt{n})$，即样本量平方根级收敛。

## 一、定理介绍

> **前置依赖**：Rademacher 变量与对称化、McDiarmid 不等式、期望与概率界、损失函数有界性、Jensen 不等式

设 $\mathcal{H}$ 为假设空间，损失函数 $L$ 取值于 $[0,1]$。定理断言：对任意 $\delta>0$，以至少 $1-\delta$ 的概率，对所有 $h\in\mathcal{H}$ 一致成立
$$
R(h)\le \hat{R}_n(h)+2\mathfrak{R}_n(\mathcal{H})+\sqrt{\frac{\log\frac1\delta}{2n}},
$$
其中 $\mathfrak{R}_n(\mathcal{H})$ 为 $\mathcal{H}$ 的（总体）Rademacher 复杂度。它比 VC 维界更紧、且是"数据相关"的界。

## 二、原理思路

与 VC 维界一样利用对称化，但用 Rademacher 复杂度而非生长函数来量化 $\sup_{h\in\mathcal{H}}(R(h)-\hat{R}_n(h))$ 的集中性。证明分三步：先用 McDiarmid 不等式证明关键统计量围绕其期望集中；再用对称化把期望控制为 $2\mathfrak{R}_n(\mathcal{H})$；最后合成概率界。

## 三、定理的严格表述

经验 Rademacher 复杂度与总体 Rademacher 复杂度分别定义为
$$
\hat{\mathfrak{R}}_n(\mathcal{H})=\mathbb{E}_\varepsilon\left[\sup_{h\in\mathcal{H}}\frac1n\sum_{i=1}^n\varepsilon_i h(x_i)\right],\qquad
\mathfrak{R}_n(\mathcal{H})=\mathbb{E}_S[\hat{\mathfrak{R}}_n(\mathcal{H})],
$$
其中 $\varepsilon_i$ 为独立 Rademacher 变量。若损失 $L\in[0,1]$，则对任意 $\delta>0$，以至少 $1-\delta$ 的概率，对所有 $h\in\mathcal{H}$ 有
$$
R(h)\le \hat{R}_n(h)+2\mathfrak{R}_n(\mathcal{H})+\sqrt{\frac{\log\frac1\delta}{2n}}.
$$

## 四、证明过程

**步骤1：定义关键统计量。** 令 $\Phi(S)=\sup_{h\in\mathcal{H}}(R(h)-\hat{R}_n(h))$，目标是证明它集中在 $\mathbb{E}[\Phi(S)]$ 附近并估计该期望。

**步骤2：验证 McDiarmid 条件。** 替换第 $i$ 个样本 $(x_i,y_i)$ 为 $(x_i',y_i')$ 得 $S'$。因损失取值在 $[0,1]$，$\hat{R}_n(h)$ 的变化至多为 $1/n$，故
$$
|\Phi(S)-\Phi(S')|\le \frac1n,
$$
由 McDiarmid 不等式，$\mathbb{P}(\Phi(S)-\mathbb{E}[\Phi(S)]\ge t)\le e^{-2nt^2}$。

**步骤3：对称化。** 用 $R(h)=\mathbb{E}_{S'}[\hat{R}'_n(h)]$ 与 Jensen 不等式
$$
\mathbb{E}[\Phi(S)]=\mathbb{E}_S\left[\sup_{h\in\mathcal{H}}(R(h)-\hat{R}_n(h))\right]\le \mathbb{E}_{S,S'}\left[\sup_{h\in\mathcal{H}}(\hat{R}'_n(h)-\hat{R}_n(h))\right].
$$

**步骤4：引入 Rademacher 变量。** 加入 $\varepsilon_i$ 并利用 $\varepsilon_i$ 的分布对称性与上确界的次可加性，
$$
\mathbb{E}_{S,S'}\left[\sup_{h\in\mathcal{H}}\frac1n\sum_{i=1}^n\varepsilon_i\big(L(y_i',h(x_i'))-L(y_i,h(x_i))\big)\right]\le 2\mathfrak{R}_n(\mathcal{H}).
$$
故 $\mathbb{E}[\Phi(S)]\le2\mathfrak{R}_n(\mathcal{H})$。

**步骤5：综合。** 由 McDiarmid 不等式，以至少 $1-\delta$ 的概率
$$
\Phi(S)\le \mathbb{E}[\Phi(S)]+\sqrt{\frac{\log\frac1\delta}{2n}}\le 2\mathfrak{R}_n(\mathcal{H})+\sqrt{\frac{\log\frac1\delta}{2n}}.\qquad\square
$$

## 五、应用与意义

Rademacher 复杂度泛化界是 SRM、SVM 泛化分析、核方法与回归问题中通用的工具。由于它是数据相关、且对不同函数族（如 Lipschitz 收缩、RKHS 单位球）都能给出简洁界，通常比 VC 维界更紧、更普适，是当代统计学习理论的标准模块。