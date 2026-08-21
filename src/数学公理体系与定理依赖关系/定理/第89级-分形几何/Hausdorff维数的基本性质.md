# Hausdorff维数的基本性质

> **一句话大白话**：Hausdorff 维数像一把"粗糙度尺子"：子集维数不超过母集（单调），可数并的维数等于各维数的上确界（可数稳定），拉伸不放大维数（Lipschitz 不变），开集维数正好等于空间维数。
>
> **小例子**：$[0,1]$ 的维数是 $1$，它的任意子集维数都不超过 $1$；有限个点的并维数为 $0$；平面里的开圆盘维数必为 $2$。

## 一、定理介绍

> **前置依赖**：Hausdorff 外测度的定义、测度的单调性、可数次可加性、Lipschitz 映射与等距映射、上确界与极限

Hausdorff 维数是刻画分形"填充空间程度"的核心不变量。本节给出它的一组基本性质，包括单调性、可数稳定性、Lipschitz 不变性、等距不变性与开集性，这些性质是后续计算所有经典分形维数的基石。

## 二、原理思路

Hausdorff 维数基于 $s$ 维 Hausdorff 外测度 $\mathcal{H}^s$：对 $s<\dim_H F$ 有 $\mathcal{H}^s(F)=\infty$，而 $s>\dim_H F$ 时有 $\mathcal{H}^s(F)=0$。各性质的证明都归约为：在临界指数处利用测度的单调性、可数次可加性与 Lipschitz 常数对直径的放大来控制 $\mathcal{H}^s$，从而比较维数。

## 三、定理的严格表述

设 $F\subset\mathbb{R}^n$，则 Hausdorff 维数 $\dim_H F$ 满足：

1. **单调性**：若 $E\subset F$，则 $\dim_H E\le\dim_H F$。
2. **可数稳定性**：$\displaystyle\dim_H\left(\bigcup_{i=1}^{\infty}F_i\right)=\sup_i\dim_H F_i$。
3. **Lipschitz 不变性**：若 $f:F\to\mathbb{R}^m$ 是 Lipschitz 映射，则 $\dim_H f(F)\le\dim_H F$。
4. **等距不变性**：若 $F$ 与 $G$ 等距，则 $\dim_H F=\dim_H G$。
5. **开集性**：若 $F\subset\mathbb{R}^n$ 是开集，则 $\dim_H F=n$。

## 四、证明过程

**证：**

**(1) 单调性**：$E\subset F$ 时，$F$ 的任何 $\delta$-覆盖也是 $E$ 的 $\delta$-覆盖，故 $\mathcal{H}^s_\delta(E)\le\mathcal{H}^s_\delta(F)$，取极限得 $\mathcal{H}^s(E)\le\mathcal{H}^s(F)$。若 $s>\dim_H F$，则 $\mathcal{H}^s(F)=0$，从而 $\mathcal{H}^s(E)=0$，故 $\dim_H E\le\dim_H F$。$\square$

**(2) 可数稳定性**：由单调性知 $\sup_i\dim_H F_i\le\dim_H(\bigcup_iF_i)$。反向：设 $s>\sup_i\dim_H F_i$，则每个 $\mathcal{H}^s(F_i)=0$，由可数次可加性
$$
\mathcal{H}^s\left(\bigcup_{i=1}^{\infty}F_i\right)\le\sum_{i=1}^{\infty}\mathcal{H}^s(F_i)=0
$$
故 $\dim_H(\bigcup_iF_i)\le s$，令 $s\to\sup_i\dim_H F_i^+$ 得反向不等式。$\square$

**(3) Lipschitz 不变性**：设 Lipschitz 常数为 $c$。若 $\{U_i\}$ 是 $F$ 的 $\delta$-覆盖，则 $\{f(F\cap U_i)\}$ 是 $f(F)$ 的 $c\delta$-覆盖，故
$$
\mathcal{H}^s_{c\delta}(f(F))\le\sum_i|f(F\cap U_i)|^s\le c^s\sum_i|U_i|^s
$$
令 $\delta\to0$ 得 $\mathcal{H}^s(f(F))\le c^s\mathcal{H}^s(F)$。若 $s>\dim_H F$，则 $\mathcal{H}^s(f(F))=0$，故 $\dim_H f(F)\le\dim_H F$。$\square$

**(4) 等距不变性**：等距是 Lipschitz 常数为 $1$ 的映射，由 (3) 即得。$\square$

**(5) 开集性**：非空开集 $F$ 含一个 $n$ 维球体，其 $n$ 维 Hausdorff 测度为正，故 $\dim_H F\ge n$；又 $F\subset\mathbb{R}^n$，由单调性 $\dim_H F\le n$。故 $\dim_H F=n$。$\square$

## 五、应用与意义

这组性质提供了计算维数的"工具箱"：可数稳定性和单调性常用来放缩构造上下界，Lipschitz 与等距不变性保证维数是几何内在量（可独立于坐标与嵌入计算）。它们与质量分布原理结合，是证明 Cantor 集、Sierpinski 三角形、Koch 曲线维数的统一方法。