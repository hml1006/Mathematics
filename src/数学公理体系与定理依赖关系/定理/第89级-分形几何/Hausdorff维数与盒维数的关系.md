# Hausdorff维数与盒维数的关系

> **一句话大白话**：盒维数用"覆盖所需的盒子个数"估维数，Hausdorff 维数总是不超过盒维数——即 $\dim_H F\le\underline{\dim}_B F\le\overline{\dim}_B F$，但它通常比盒维数更精细。
>
> **小例子**：可数稠密集（如 $\mathbb{Q}$）的 Hausdorff 维数为 $0$，但盒维数可能接近 $n$——说明盒维数对"空隙大但分布密"的集合偏保守。

## 一、定理介绍

> **前置依赖**：Hausdorff 测度与 Hausdorff 维数的定义、盒维数（上/下）的定义、对数比较与极限、集合覆盖的计数

Hausdorff 维数（精确但难算）与盒维数（直观但粗略）是两种最重要的分形维数定义。本定理建立了它们之间的基本不等式，给出了两种维数的相对位置，并指出反向不等式的失效原因。

## 二、原理思路

核心思想是用盒覆盖给出的粗估计去控制 $s$ 维 Hausdorff 测度：若用 $N_\delta(F)$ 个直径为 $\delta$ 的集合覆盖 $F$，则该覆盖对 $\mathcal{H}^s_\delta(F)$ 的贡献不超过 $N_\delta(F)\cdot\delta^s$。当 $s<\dim_H F$ 时 $\mathcal{H}^s(F)=\infty$，迫使 $N_\delta(F)\delta^s>1$，从而把 $\log N_\delta/-\log\delta$ 压低在 $s$ 之上。

## 三、定理的严格表述

（Hausdorff 维数与盒维数的关系）设有界集 $F\subset\mathbb{R}^n$，则
$$
\dim_H F\le\underline{\dim}_B F\le\overline{\dim}_B F
$$

## 四、证明过程

**证：** 设 $s>0$，$\delta>0$，$N_\delta(F)$ 是覆盖 $F$ 所需直径为 $\delta$ 的集合的最小个数，则存在 $N_\delta(F)$ 个直径为 $\delta$ 的集合覆盖 $F$，从而
$$
\mathcal{H}^s_\delta(F)\le N_\delta(F)\cdot\delta^s
$$
若 $s<\dim_H F$，则 $\mathcal{H}^s(F)=\infty$，对充分小的 $\delta$ 有 $\mathcal{H}^s_\delta(F)>1$，故 $N_\delta(F)\delta^s>1$，即
$$
\log N_\delta(F)+s\log\delta>0\Rightarrow\frac{\log N_\delta(F)}{-\log\delta}>s
$$
取 $\delta\to0$ 的下极限，得 $\underline{\dim}_B F\ge s$。令 $s\to\dim_H F^-$ 得 $\underline{\dim}_B F\ge\dim_H F$。上盒维数总不小于下盒维数，故 $\dim_H F\le\underline{\dim}_B F\le\overline{\dim}_B F$。$\square$

**注**：反向不等式一般成立不了。例如可数稠密集的 Hausdorff 维数为 $0$，但其盒维数可取到 $n$，因为粗盒子永远避不开稠密点。

## 五、应用与意义

这条不等式解释了为何盒维数常作为 Hausdorff 维数的"上界近似"，也警示要用更精细的测度手段才能区分一些退化集合。在实际计算中，当区间长度 $|U_i|^s$ 的求和能被盒子数目有效控制时，两者相等，这为数值维数估计提供了理论边界。