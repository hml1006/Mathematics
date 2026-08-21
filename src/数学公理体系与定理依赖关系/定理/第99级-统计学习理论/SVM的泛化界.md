# SVM的泛化界

> **一句话大白话**：用核函数把数据映射到再生核希尔伯特空间后，SVM 的泛化误差被"核范数 $\Lambda$ 除以 $\sqrt n$"这一复杂度项限制，与输入空间维度无关。
>
> **小例子**：径向基核下把数据升到高维甚至无穷维，只要 $\|f\|_\mathcal{H}\le\Lambda$，SVM 泛化误差仍以 $O(1/\sqrt{n})$ 收敛，这正是"高维不惧过拟合"的理论支撑。

## 一、定理介绍

设 $\mathcal{H}$ 为再生核希尔伯特空间（RKHS）中的单位球 $\{f:\|f\|_\mathcal{H}\le\Lambda\}$，核函数满足 $K(x,x)\le1$，损失取铰链损失 $L(y,f(x))=\max(0,1-yf(x))$。则对任意 $\delta>0$，以至少 $1-\delta$ 的概率，对所有 $f\in\mathcal{H}$ 有
$$
R(f)\le \hat R_n(f)+\frac{2\Lambda}{\sqrt n}+\sqrt{\frac{\log\frac1\delta}{2n}}.
$$

## 二、原理思路

先计算 RKHS 单位球的 Rademacher 复杂度：利用再生性质把 $\frac1n\sum_i\varepsilon_if(x_i)$ 写成范数内积 $\langle f,\frac1n\sum_i\varepsilon_iK(x_i,\cdot)\rangle_\mathcal{H}$，再由 Cauchy-Schwarz 与核条件 $K(x,x)\le1$ 给出 $\mathfrak{R}_n\le\Lambda/\sqrt n$；最后代入 Rademacher 复杂度的泛化界。

## 三、定理的严格表述

对 $\mathcal{H}=\{f:\|f\|_\mathcal{H}\le\Lambda\}$，$K(x,x)\le1$，铰链损失 $L(y,f)=\max(0,1-yf)$。若偏差 $R(f)=\mathbb{E}[L(y,f(x))]$、经验偏差 $\hat R_n(f)=\frac1n\sum_iL(y_i,f(x_i))$，则对任意 $\delta>0$，以至少 $1-\delta$ 的概率对所有 $f\in\mathcal{H}$
$$
R(f)\le \hat R_n(f)+\frac{2\Lambda}{\sqrt n}+\sqrt{\frac{\log\frac1\delta}{2n}}.
$$

## 四、证明过程

**步骤1：Rademacher 复杂度。** 由定义
$$
\hat{\mathfrak{R}}_n(\mathcal{H})=\mathbb{E}_\varepsilon\left[\sup_{\|f\|_\mathcal{H}\le\Lambda}\frac1n\sum_{i=1}^n\varepsilon_if(x_i)\right].
$$
由 Riesz 表示 $f(x_i)=\langle f,K(x_i,\cdot)\rangle_\mathcal{H}$，得 $\frac1n\sum_i\varepsilon_if(x_i)=\langle f,\frac1n\sum_i\varepsilon_iK(x_i,\cdot)\rangle_\mathcal{H}$。

**步骤2：Cauchy-Schwarz。** 于是
$$
\sup_{\|f\|_\mathcal{H}\le\Lambda}\left\langle f,\frac1n\sum_{i=1}^n\varepsilon_iK(x_i,\cdot)\right\rangle_\mathcal{H}\le \Lambda\left\|\frac1n\sum_{i=1}^n\varepsilon_iK(x_i,\cdot)\right\|_\mathcal{H}.
$$

**步骤3：计算范数。** 由再生性质
$$
\left\|\frac1n\sum_{i=1}^n\varepsilon_iK(x_i,\cdot)\right\|_\mathcal{H}^2=\frac1{n^2}\sum_{i,j}\varepsilon_i\varepsilon_jK(x_i,x_j).
$$
对 $\varepsilon$ 取期望，交叉项 $\mathbb{E}[\varepsilon_i\varepsilon_j]=0$ 消失，余 $\frac1{n^2}\sum_iK(x_i,x_i)\le\frac1n$。

**步骤4：期望复杂度。** 因此 $\mathfrak{R}_n(\mathcal{H})\le\mathbb{E}_S[\Lambda/\sqrt n]=\Lambda/\sqrt n$。

**步骤5：Rademacher 泛化界。** 由 Rademacher 复杂度的泛化界，
$$
R(f)\le \hat R_n(f)+2\mathfrak{R}_n(\mathcal{H})+\sqrt{\frac{\log\frac1\delta}{2n}}\le \hat R_n(f)+\frac{2\Lambda}{\sqrt n}+\sqrt{\frac{\log\frac1\delta}{2n}}.\qquad\square
$$

## 五、应用与意义

该界解释了核方法（尤其是 SVM）在高维/无穷维特征空间仍能泛化的原因：复杂度由 RKHS 范数而非输入维度衡量。它支撑铰链损失的松弛处理、核函数的选择标准（$K(x,x)\le1$）以及正则化参数 $\Lambda$ 的调节，是统计学习理论与实践连接的重要桥梁。