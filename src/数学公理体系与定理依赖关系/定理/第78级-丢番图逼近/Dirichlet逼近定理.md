# Dirichlet 逼近定理

> **一句话大白话**：无论多"难缠"的无理数，都能用分母不超过 $N$ 的分数 $\frac pq$ 逼近到误差小于 $\frac1N$，进而小于 $\frac1{q^2}$。好分数总是不缺。
>
> **小例子**：$\pi\approx\frac{22}{7}$，$|\pi-\frac{22}{7}|\approx0.00126<1/7^2\approx0.0204$；$|\pi-\frac{355}{113}|\approx2.7\times10^{-7}<1/113^2$。这些渐近分数正给出了平方级精度的逼近。

## 一、定理介绍

> **前置依赖**：鸽巢原理、实数的小数部分与取整函数、有理数逼近的基本概念。

Dirichlet 逼近定理是丢番图逼近的出发点。它断言对任意实数 $\alpha$ 和任意正整数 $N$，存在 $1\le q\le N$ 及 $p$，使 $|q\alpha-p|<\frac1N$。这是"有理数总能以平方级精度逼近实数"的普适保证，是连分数理论、无理性证明与丢番图方程的基础。

## 二、原理思路

证明只用鸽巢原理：考察 $N+1$ 个数 $0,\{\alpha\},\{2\alpha\},\dots,\{N\alpha\}$（$\{\cdot\}$ 为小数部分），全部落在 $[0,1)$；把 $[0,1)$ 分成 $N$ 个等长子区间，鸽巢原理保证有两个落在同一小区间，其差小于 $\frac1N$。这个差恰为 $|q\alpha-p|$，取 $q=j-i$、$p=\lfloor j\alpha\rfloor-\lfloor i\alpha\rfloor$ 即得。

## 三、定理的严格表述

设 $\alpha$ 是实数，$N$ 是正整数。则存在整数 $p,q$，满足 $1\le q\le N$，使
$$\left|q\alpha-p\right|<\frac1N,\qquad\text{即}\qquad\left|\alpha-\frac pq\right|<\frac1{qN}\le\frac1{q^2}.$$

**推论**：对任意无理数 $\alpha$，存在无穷多个有理数 $\frac pq$ 满足 $\left|\alpha-\frac pq\right|<\frac1{q^2}$。

## 四、证明过程

**证明（鸽巢原理）：**

**步骤 1：构造 $N+1$ 个数。** 考虑 $0,\{\alpha\},\{2\alpha\},\dots,\{N\alpha\}$，其中 $\{x\}=x-\lfloor x\rfloor\in[0,1)$。

**步骤 2：划分区间。** 把 $[0,1)$ 分成 $N$ 个等长子区间 $\left[\frac{i}{N},\frac{i+1}{N}\right)$（$i=0,\dots,N-1$）。

**步骤 3：鸽巢。** 由鸽巢原理，$N+1$ 个数中必有两个落在同一区间，设为 $\{i\alpha\},\{j\alpha\}$，$0\le i<j\le N$，则 $|\{j\alpha\}-\{i\alpha\}|<\frac1N$。

**步骤 4：取参数。** 令 $q=j-i$（$1\le q\le N$），$p=\lfloor j\alpha\rfloor-\lfloor i\alpha\rfloor$。则
$$\left|q\alpha-p\right|=\left|(j\alpha-\lfloor j\alpha\rfloor)-(i\alpha-\lfloor i\alpha\rfloor)\right|=|\{j\alpha\}-\{i\alpha\}|<\frac1N.$$
除以 $q$ 得 $\left|\alpha-\frac pq\right|<\frac1{qN}\le\frac1{q^2}$。$\square$

**推论证：** 对每个 $N$ 应用定理得 $\frac{p_N}{q_N}$；因 $\alpha$ 无理，这些分数互不相同（否则误差为零），故无穷多个。$\square$

## 五、应用与意义

Dirichlet 定理确立了丢番图逼近的"平方界" $1/q^2$，是所有无理性、Liouville 界、连分数理论的逻辑起点。它被推广为多维的 Minkowski 线性无形式、逼近共轭律 (Kronecker) 以及代数数的有效逼近理论。其鸽巢论证作为抽屉原理的经典应用，被誉为最优雅的初等数论证明之一。