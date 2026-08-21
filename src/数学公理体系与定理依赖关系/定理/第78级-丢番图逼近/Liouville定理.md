# Liouville 定理

> **一句话大白话**：$d$ 次代数无理数很难被有理数逼近——误差至少是某个常数除以 $q^d$。这给出了所有代数数的"逼近硬度下限"。太容易逼近的数（违反这条下限）必是超越数。
>
> **小例子**：Liouville 数 $\sum_{n\ge1}10^{-n!}$ 能被 $10^{-(d+1)!}$ 级误差逼近（比任何 $d$ 次代数数的下界 $c/q^d$ 都小），故它不可能是代数数，只能是超越数。这是超越数存在的第一个构造性证明。

## 一、定理介绍

> **前置依赖**：代数数与最小多项式、中值定理、整系数多项式取值的整数下界。

Liouville 定理（1844）给出代数无理数的通用逼近下界 $|\alpha-\frac pq|\ge\frac{c(\alpha)}{q^d}$（$d$ 为次数）。它是"高次代数数不好逼近"的精确刻画，并由此构造出一大类超越数（Liouville 数），开创超越数理论。

## 二、原理思路

设 $\alpha$ 的最小多项式 $f\in\mathbb{Z}[x]$，$f(p/q)\neq0$。一方面 $|f(p/q)|=\frac{|a_dp^d+\cdots+a_0q^d|}{q^d}\ge\frac1{q^d}$（分子为非零整数），得不小于分母倒数的下界；另一方面由中值定理 $|f(p/q)|=|f'(\xi)||\alpha-\frac pq|\le M|\alpha-\frac pq|$（在 $\alpha$ 邻域内 $|f'|\le M$）。两结合即得 $\left|\alpha-\frac pq\right|\ge\frac{1}{Mq^d}$。

## 三、定理的严格表述

设 $\alpha$ 是 $d$ 次代数无理数（$d\ge2$）。则存在常数 $c(\alpha)>0$，使对所有有理数 $\frac pq$（$q>0$）有
$$\left|\alpha-\frac pq\right|\ge\frac{c(\alpha)}{q^d}.$$

**推论（Liouville 数）** $\alpha=\sum_{n=1}^{\infty}10^{-n!}$ 是超越数。

## 四、证明过程

**证明：**

**步骤 1：最小多项式。** 设 $f(x)=a_dx^d+\cdots+a_0\in\mathbb{Z}[x]$（$a_d>0$）为 $\alpha$ 的不可约最小多项式，$\deg f=d\ge2$。因 $f$ 不可约且 $\alpha$ 无理，$f(\frac pq)\neq0$。

**步骤 2：下界。**
$$\left|f\Big(\frac pq\Big)\right|=\frac{|a_dp^d+a_{d-1}p^{d-1}q+\cdots+a_0q^d|}{q^d}\ge\frac1{q^d},$$
因为分子是非零整数，绝对值至少为 $1$。$\blacksquare$

**步骤 3：中值定理上界。** 存在 $\xi$ 介于 $\alpha$ 与 $\frac pq$ 之间使 $f(\frac pq)=f'(\xi)(\frac pq-\alpha)$。令 $M=\max_{|x-\alpha|\le1}|f'(x)|$。若 $|\alpha-\frac pq|<1$ 则 $\xi\in[\alpha-1,\alpha+1]$，$|\frac pq-\alpha|=\frac{|f(p/q)|}{|f'(\xi)|}\ge\frac1{Mq^d}$。$\blacksquare$

**步骤 4：平凡情形。** 若 $|\alpha-\frac pq|\ge1$，不等式显然。取 $c(\alpha)=\min\{1,\frac1M\}$ 即对所有 $\frac pq$ 成立。$\square$

**推论证明：** 对任意 $d$，取 $q=10^{d!}$、$p=10^{d!}\sum_{n=1}^d10^{-n!}$，则
$$\Big|\alpha-\frac pq\Big|=\sum_{n=d+1}^{\infty}10^{-n!}<2\cdot10^{-(d+1)!}=\frac{2}{q^{d+1}}.$$
若 $\alpha$ 是 $d$ 次代数数，Liouville 定理要求误差 $\ge\frac{c}{q^d}$，而这里对充分大 $q$ 有 $\frac2{q^{d+1}}<\frac c{q^d}$，矛盾。故 $\alpha$ 超越。$\square$

## 五、应用与意义

Liouville 定理是超越数论的奠基：它提供首批超越数（Liouville 数）并确立"代数数的逼近指数 $\le d$"的下界基准，直接催生 Thue-Siegel-Roth 序列（最终把指数降到 2）。它也是丢番图逼近中"下界"技巧（最小多项式 + 中值定理 + 范数取整）的原型，其思想推广到线性形式、$p$-adic 逼近和量子定理，并用于 Diophantine 方程（如 Thue 方程）的有限性判定。