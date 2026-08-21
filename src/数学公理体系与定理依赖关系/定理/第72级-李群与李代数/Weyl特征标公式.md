# Weyl 特征标公式

> **一句话大白话**：最高权为 $\lambda$ 的不可约表示的特征标，等于一个"交错和之比"：$\chi_{V(\lambda)}=\frac{\sum_{w\in W}\varepsilon(w)e^{w(\lambda+\rho)}}{\sum_{w\in W}\varepsilon(w)e^{w(\rho)}}$，其中 $\rho$ 是正根和的一半。
>
> **小例子**：对 $\mathfrak{sl}_2$，Weyl 公式给出权重 $k$ 的特征标 $\chi = \frac{e^{(k+1)\alpha/2}-e^{-(k+1)\alpha/2}}{e^{\alpha/2}-e^{-\alpha/2}}$，展成级数即得各权重的重数——一维不可约表示的权重谱被完整读出。

## 一、定理介绍

> **前置依赖**：半单李代数与最高权表示、根系与 Weyl 群、Weyl 分母公式、Weyl 积分公式、特征标正交性。

Weyl 特征标公式是一个闭式公式，给出复半单李代数的不可约表示（以最高权 $\lambda$ 标记）的特征标。作为 $W$-反变的交错和之比，它把表示权重的重数问题转化为组合代数运算，是表示论中最优美、最强有力的公式之一。它还蕴含 Weyl 维数公式与 Weyl 分母公式等推论。

## 二、原理思路

证明的主线是 Weyl 分母公式、Weyl 积分公式与特征标正交性事理的综合。先证明分母公式 $\sum_{w\in W}\varepsilon(w)e^{w(\rho)}=\prod_{\alpha\in\Phi^+}(e^{\alpha/2}-e^{-\alpha/2})$；再利用紧李群的 Weyl 积分公式把群上的积分化为极大环面上的积分，结合不可约特征标的正交基性质，验证交替和之比恰为最高权 $V(\lambda)$ 的特征标。

## 三、定理的严格表述

设 $\mathfrak{g}$ 是复半单李代数，$V(\lambda)$ 是以 $\lambda$ 为最高权的不可约表示，$\Phi^+$ 是正根系，$\rho=\frac{1}{2}\sum_{\alpha\in\Phi^+}\alpha$。则 $V(\lambda)$ 的特征标为：
$$
\chi_{V(\lambda)}=\frac{\sum_{w\in W}\varepsilon(w)e^{w(\lambda+\rho)}}{\sum_{w\in W}\varepsilon(w)e^{w(\rho)}},
$$
其中 $W$ 是 Weyl 群，$\varepsilon(w)$ 是 $w$ 的符号（行列式）。

## 四、证明过程

**证明：**

**步骤 1：特征标的性质。** 特征标 $\chi_V$ 是 $W$-不变的，并可由权展开 $\chi_V=\sum_\mu m_V(\mu)e^\mu$。

**步骤 2：Weyl 分母公式。** 记 $F=\sum_{w\in W}\varepsilon(w)e^{w(\rho)}$。对每个简单反射 $s_{\alpha_i}$，$s_{\alpha_i}(F)=-F$，故 $F$ 被 $(1-e^{-\alpha})$ 对每个 $\alpha\in\Phi^+$ 整除，比较次数得 $\sum_{w}\varepsilon(w)e^{w(\rho)}=\prod_{\alpha\in\Phi^+}(e^{\alpha/2}-e^{-\alpha/2})$。

**步骤 3：Weyl 积分公式。** 对 $G$ 上的类函数 $f$，$\int_G f\,dg=\frac{1}{|W|}\int_T f(t)\left|\sum_w\varepsilon(w)e^{w(\rho)}\right|^2dt$。

**步骤 4：特征标正交性。** 紧群不可约表示的特征标在 $L^2(G)$ 中构成标准正交基 $\langle\chi_V,\chi_W\rangle=\delta_{V,W}$。

**步骤 5：构造特征标。** 考察 $A_{\lambda+\rho}=\sum_w\varepsilon(w)e^{w(\lambda+\rho)}$，断言 $\frac{A_{\lambda+\rho}}{A_\rho}=\sum_\mu m_{V(\lambda)}(\mu)e^\mu$。左侧 $W$-不变故可按权展开；利用积分公式与正交性，可验证其系数恰为 $V(\lambda)$ 的权重数。

**步骤 6：验证。** 由分母公式，$\chi=\frac{A_{\lambda+\rho}}{A_\rho}$ 是 $e^\mu$ 的整系数组合，计算其与特征标的内积可证 $\chi$ 正是 $V(\lambda)$ 的特征标。$\square$

## 五、应用与意义

Weyl 特征标公式把表示论的重数问题代数化，直接导出 Weyl 维数公式与不可约表示的完整权重谱，是研究半单李代数表示、紧李群调和分析与量子群表示分类的基准工具。在数学物理中，它与 Peter-Weyl 定理共同支撑粒子物理中的量子数分类和对称性分析；在组合学中，特征标公式与 Schur 函数、幂和对称函数及其 Cauchy 恒等式密切相关，是表示论与对称函数之间的桥梁。
## 相关条目

- [Weyl 特征标公式（第38级-表示论）](../第38级-表示论/Weyl特征标公式.md)：与本条目为同一定理，另收录于第38级-表示论，可交叉参考。
