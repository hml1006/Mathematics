# PAC学习的基本定理

> **一句话大白话**：一个假设空间能否被"概率意义上近似正确"地学好，与它本身有多复杂（VC 维）直接挂钩——VC 维有限就能学好，无穷大就学不会（无论给多少数据）。
>
> **小例子**：区间分类器（$d=2$）在足够样本下可用 ERM 学到近最优分类器；而"能实现任意标签分配"的函数类（$d=\infty$）无论样本多少都无法保证泛化。

## 一、定理介绍

设 $\mathcal{H}$ 为二分类假设空间。定理断言：$\mathcal{H}$ 是 PAC 可学习的当且仅当 $\text{VCdim}(\mathcal{H})<\infty$。若 $d=\text{VCdim}(\mathcal{H})<\infty$，则经验风险最小化（ERM）是 PAC 学习算法，样本复杂度满足
$$
m_\mathcal{H}(\varepsilon,\delta)=O\left(\frac{d}{\varepsilon}\log\frac1\varepsilon+\frac1\varepsilon\log\frac1\delta\right).
$$
它确立了"可学习性与假设空间储量"之间的等价关系。

## 二、原理思路

充分性方向：由 VC 维泛化界得到"对所有 $h$ 一致成立"的界，再取 $h=\hat h_n$（ERM 解）与最优假设 $h^\ast$ 比较，因 $\hat R_n(\hat h_n)\le\hat R_n(h^\ast)$，把 $R(\hat h_n)$ 控制为 $R(h^\ast)+2\varepsilon_{\text{comp}}(n)$，从而解得样本复杂度。必要性方向：若 $d=\infty$，构造被 $\mathcal{H}$ 打散的任意大点集与对抗分布，使任意算法对未观测点的误差至少 $1/2$，与 PAC 定义矛盾。

## 三、定理的严格表述

**PAC 可学习定义。** 存在算法 $\mathcal{A}$ 与函数 $m_\mathcal{H}(\varepsilon,\delta)$，使得对任意分布 $P$ 和任意 $\varepsilon,\delta>0$，当 $n\ge m_\mathcal{H}(\varepsilon,\delta)$ 时以至少 $1-\delta$ 的概率有
$$
R(\hat h_n)\le \inf_{h\in\mathcal{H}}R(h)+\varepsilon.
$$

**基本定理。** $\mathcal{H}$ 可 PAC 学习 $\iff$ $\text{VCdim}(\mathcal{H})<\infty$，且此时 ERM 实现学习、上界如上。

## 四、证明过程

**方向1（充分性）：** 对 $\hat h_n$ 应用 VC 泛化界，复杂度项记 $\varepsilon_{\text{comp}}(n)=\sqrt{\frac{8d\log(2en/d)}{n}}+\sqrt{\frac{8\log(2/\delta)}{n}}$。由 $\hat R_n(\hat h_n)\le\hat R_n(h^\ast)$，
$$
R(\hat h_n)\le \hat R_n(h^\ast)+\varepsilon_{\text{comp}}\le R(h^\ast)+2\varepsilon_{\text{comp}}.
$$
令 $n$ 足够大使 $2\varepsilon_{\text{comp}}\le\varepsilon$，即得
$$
n\ge \frac{Cd}{\varepsilon}\log\frac d\varepsilon+\frac{C}{\varepsilon}\log\frac1\delta,
$$
故 ERM 是 PAC 学习算法。

**方向2（必要性）：** 反设 $\text{VCdim}(\mathcal{H})=\infty$。对任意 $m$，存在 $m$ 个点被 $\mathcal{H}$ 打散。取 $P$ 均匀支撑其上、标签由某 $h^\ast$ 确定。因 $2^m$ 种标签全部可实现，任意算法至多观测 $m$ 个标签，对未观测点都存在某个 $h^\ast$ 使误差达至少 $1/2$，故泛化误差可做到 $\ge1/2>1/4$，与 PAC 定义矛盾。$\square$

## 五、应用与意义

PAC 基本定理是"何时学习在理论上可行"的判定标准，为假设空间设计、ERM 的合理性、以及学习算法的样本复杂度分析提供了统一框架。它是模型选择、VC 维计算与学习理论课程的核心结论，也为主动学习、不可知学习等扩展理论奠定基础。