# VC维的泛化界

> **一句话大白话**：假设空间越复杂（VC维 $d$ 越大），训练误差与真实误差的差距越大；但只要样本够多，真实误差就以高概率被"训练误差加一个复杂度项"控制住。
>
> **小例子**：用阈值分类器（$d=1$）和所有线性分类器对比，在同样样本下复杂度项 $\sqrt{\frac{2d\log(en/d)}{n}}$ 中 $d$ 越大界越松，这正是过拟合风险随复杂度上升的定量体现。

## 一、定理介绍

设 $\mathcal{H}$ 为二分类假设空间，VC 维为 $d=\text{VCdim}(\mathcal{H})$，$R(h)$ 为期望风险，$\hat{R}_n(h)$ 为经验风险。定理断言：以至少 $1-\delta$ 的概率，对所有 $h\in\mathcal{H}$ 一致成立
$$
R(h)\le \hat{R}_n(h)+\sqrt{\frac{2d\log\frac{en}{d}}{n}}+\sqrt{\frac{\log\frac1\delta}{2n}}.
$$
它把"样本外泛化"与"假设空间复杂度"用 VC 维定量联系起来，是监督学习理论中最重要的泛化界之一。

## 二、原理思路

核心思想是用"对称化 + 生长函数 + Hoeffding 型联合界"把 $\sup_{h\in\mathcal{H}}|\hat{R}_n(h)-R(h)|$ 的偏差控制住。关键步骤是引入 Ghost（影子）样本 $S'$ 与原样本 $S$ 的对称化技巧，再用 Rademacher 随机变量交换 $S$ 与 $S'$ 的标签，最终把最坏偏差的出现概率归结为生长函数 $\Pi_\mathcal{H}(2n)$ 与独立指数项的联合界，最后由 Sauer-Shelah 引理用 VC 维 $d$ 上界生长函数。

## 三、定理的严格表述

### 泛化不等式

设 $\mathcal{H}$ 为二分类假设空间，$\text{VCdim}(\mathcal{H})=d<\infty$，损失 $L$ 取 0-1 损失。则对任意 $\delta>0$，以至少 $1-\delta$ 的概率，对所有 $h\in\mathcal{H}$ 有
$$
R(h)\le \hat{R}_n(h)+\sqrt{\frac{2d\log\frac{en}{d}}{n}}+\sqrt{\frac{\log\frac1\delta}{2n}}.
$$

### 生长函数与 Sauer-Shelah 引理

$\mathcal{H}$ 在 $n$ 个点上的生长函数为
$$
\Pi_\mathcal{H}(n)=\max_{x_1,\dots,x_n}\left|\{(h(x_1),\dots,h(x_n)):h\in\mathcal{H}\}\right|.
$$
若 $\text{VCdim}(\mathcal{H})=d$，则对 $n\ge d$，
$$
\Pi_\mathcal{H}(n)\le \sum_{i=0}^{d}\binom{n}{i}\le \left(\frac{en}{d}\right)^d.
$$

## 四、证明过程

**步骤1：生长函数与 VC 维。** 定义算上述生长函数，并由 Sauer-Shelah 引理知 $\Pi_\mathcal{H}(n)\le(en/d)^d$。

**步骤2：对称化引理。** 令 $Z_i=\mathbf1_{\{h(x_i)\ne y_i\}}$，引入与 $S$ 同分布且独立的 Ghost 样本 $S'$，其经验风险为 $\hat{R}'_n(h)$。由对称化技巧
$$
\mathbb{P}\left(\sup_{h\in\mathcal{H}}(R(h)-\hat{R}_n(h))>\varepsilon\right)\le \mathbb{P}\left(\sup_{h\in\mathcal{H}}(\hat{R}'_n(h)-\hat{R}_n(h))>\frac{\varepsilon}{2}\right).
$$

**步骤3：引入 Rademacher 变量。** 联合样本 $S\cup S'$ 共 $2n$ 个点，引入独立 Rademacher 变量 $\varepsilon_i$ 交换 $S$ 与 $S'$ 的标签，使上述概率被
$$
\mathbb{P}\left(\sup_{h\in\mathcal{H}}\frac1n\sum_{i=1}^n\varepsilon_i\big(\mathbf1_{\{h(x_i')\ne y_i'\}}-\mathbf1_{\{h(x_i)\ne y_i\}}\big)>\frac{\varepsilon}{2}\right)
$$
控制。

**步骤4：利用生长函数。** 给定 $S\cup S'$，$\sup_h\frac1n\sum_i\varepsilon_i(\cdot)$ 最多取 $\Pi_\mathcal{H}(2n)$ 个不同的值。由 Hoeffding 不等式和联合界
$$
\mathbb{P}\left(\sup_{h\in\mathcal{H}}(\hat{R}'_n(h)-\hat{R}_n(h))>\frac{\varepsilon}{2}\mid S,S'\right)\le \Pi_\mathcal{H}(2n)e^{-n\varepsilon^2/8}.
$$

**步骤5：取期望并反解。** 对 $S,S'$ 取期望，并利用 $\Pi_\mathcal{H}(2n)\le(2en/d)^d$，令右端等于 $\delta$，解出
$$
\varepsilon=\sqrt{\frac{8}{n}\left(d\log\frac{2en}{d}+\log\frac{1}{\delta}\right)}.
$$

**步骤6：简化。** 由 $\sqrt{a+b}\le\sqrt a+\sqrt b$ 调整常数，即得定理形式。$\square$

## 五、应用与意义

VC 维泛化界解释了为什么"假设空间复杂度必须受控"才能保证泛化：过大的 $d$ 使界变松，对应过拟合。它是 PAC 学习基本定理、以及结构风险最小化（SRM）理论的核心依据，并指导实践中通过正则化、模型选择与交叉验证在偏差与方差之间取得平衡。