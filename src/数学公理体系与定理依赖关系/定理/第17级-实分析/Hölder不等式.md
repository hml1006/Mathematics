# Hölder 不等式

> **一句话大白话**：函数乘积的积分，被"一个函数的 $p$ 次方积分"和"另一个函数的 $q$ 次方积分"以 $\frac1p+\frac1q=1$ 的方式共同控制住。
>
> **小例子**：取 $p=q=2$，即得 $\left|\int fg\right|\le\left(\int f^2\right)^{1/2}\left(\int g^2\right)^{1/2}$，正是 Cauchy–Schwarz 不等式的积分形式。

## 介绍

Hölder 不等式（赫尔德不等式）是 $L^p$ 空间理论的核心不等式。设共轭指数 $p,q>1$ 满足 $\frac1p+\frac1q=1$，则对任意 $f\in L^p$、$g\in L^q$ 有 $fg\in L^1$ 且

$$
\int |fg|\,d\mu\le\|f\|_p\|g\|_q
$$

它由德国数学家奥托·赫尔德（Otto Hölder）于 1889 年给出，是 Cauchy–Schwarz 不等式（$p=q=2$ 情形）向一般指数的推广。

Hölder 不等式与 Minkowski 不等式一起，构成 $L^p$ 成为赋范空间的基石：前者用于控制乘积与证明对偶性（$(L^p)^*\cong L^q$），后者用于证明三角不等式。它也是内插不等式、Young 不等式、多项分布估计等结果的出发点。

## 分析

Young卷积不等式、测度与 Lebesgue 积分、$L^p$ 空间与范数 $\|f\|_p=\left(\int|f|^p\right)^{1/p}$、单调收敛定理

**定理内容**：设 $(X,\Sigma,\mu)$ 为测度空间，$1<p,q<\infty$ 且 $\frac1p+\frac1q=1$。若 $f\in L^p(\mu)$、$g\in L^q(\mu)$，则 $fg\in L^1(\mu)$ 且

$$
\int_X |f g|\,d\mu\le\left(\int_X |f|^p\,d\mu\right)^{1/p}\left(\int_X |g|^q\,d\mu\right)^{1/q}
$$

等号成立当且仅当存在不全为零的常数 $\alpha,\beta\ge0$ 使 $\alpha|f|^p=\beta|g|^q$ 几乎处处成立。对 $p=1,q=\infty$，不等式为 $\int|fg|\le\|g\|_\infty\int|f|$。

**数学内涵**：
- 它把"乘积的积分"分解为两个"各自范数"之积，是 $L^p$ 空间有良好结构的关键。
- 取 $p=q=2$ 得 Cauchy–Schwarz；取 $g\equiv1$ 得 $\|f\|_1\le\mu(X)^{1/q}\|f\|_p$。

## 思考过程

证明分两步。第一步是逐点的 Young 不等式：对 $a,b\ge0$，

$$
ab\le\frac{a^p}{p}+\frac{b^q}{q}
$$

它来自指数函数 $t\mapsto e^t$ 的凸性（等价于对数的凹性），把"乘积"拆成"两个幂次的加权和"。第二步是整体化：先归一化使 $\|f\|_p=\|g\|_q=1$，把 Young 不等式逐点用于 $|f(x)|,|g(x)|$ 再积分，右端恰为 $\frac1p+\frac1q=1$，即得结论。一般的 $f,g$ 通过缩放回到归一化情形。

## 证明过程

**步骤 1：Young 不等式。** 设 $a,b\ge0$，$1<p,q<\infty$，$\frac1p+\frac1q=1$。若 $a=0$ 或 $b=0$，结论显然。否则令 $A=a^p$，$B=b^q$。由 $t\mapsto e^t$ 的凸性与权重 $\frac1p,\frac1q$，

$$
ab=\exp\!\left(\frac1p\ln A+\frac1q\ln B\right)\le\frac1p e^{\ln A}+\frac1q e^{\ln B}=\frac{a^p}{p}+\frac{b^q}{q}
$$

**步骤 2：归一化。** 设 $\|f\|_p>0$ 且 $\|g\|_q>0$（否则 $f=0$ a.e. 或 $g=0$ a.e.，结论显然）。令

$$
F=\frac{f}{\|f\|_p},\qquad G=\frac{g}{\|g\|_q}
$$

则 $\|F\|_p=\|G\|_q=1$，且 $\int|fg|=\|f\|_p\|g\|_q\int|FG|$。故只需证 $\int|FG|\le1$。

**步骤 3：逐点应用并积分。** 对每个 $x$，把步骤 1 用于 $a=|F(x)|$、$b=|G(x)|$：

$$
|F(x)G(x)|\le\frac{|F(x)|^p}{p}+\frac{|G(x)|^q}{q}
$$

两边关于 $\mu$ 积分（各项非负，积分可与和交换）：

$$
\int|FG|\,d\mu\le\frac1p\int|F|^p\,d\mu+\frac1q\int|G|^q\,d\mu=\frac{\|F\|_p^p}{p}+\frac{\|G\|_q^q}{q}=\frac1p+\frac1q=1
$$

**步骤 4：还原并处理 $p=1$。** 由步骤 2、3，$\int|fg|\le\|f\|_p\|g\|_q$。当 $p=1$ 时 $q=\infty$，由 $|g|\le\|g\|_\infty$ a.e. 得 $\int|fg|\le\|g\|_\infty\int|f|$。

**步骤 5：等号条件。** 等号要求步骤 1 的 Young 不等式逐点取等。$t\mapsto e^t$ 严格凸，$ab=\frac{a^p}p+\frac{b^q}q$ 取等当且仅当 $a^p=b^q$（即 $\ln A=\ln B$）。故等号成立当且仅当 $|F|^p=|G|^q$ a.e.，还原后即存在 $\alpha,\beta\ge0$ 不全为零使 $\alpha|f|^p=\beta|g|^q$ a.e.。$\square$

**推论（$L^p$ 包含关系）**：若 $\mu(X)<\infty$ 且 $1\le p<q\le\infty$，则 $L^q\subset L^p$，且

$$
\|f\|_p\le\mu(X)^{\frac1p-\frac1q}\|f\|_q
$$

## 课堂问答

**老师**：乘积的积分 $\int|fg|$ 凭什么被两个 $L^p,L^q$ 范数之积控制？

**学生**：结论：当 $\frac1p+\frac1q=1$ 时 $\int|fg|\le\|f\|_p\|g\|_q$。核心是逐点 Young 不等式 $ab\le\frac{a^p}{p}+\frac{b^q}{q}$，它来自 $t\mapsto e^t$ 的凸性。先归一化 $\|F\|_p=\|G\|_q=1$，再逐点应用并积分，右端恰为 $\frac1p+\frac1q=1$。

**老师（追问）**：等号什么时候成立？$p=q=2$ 时它变成什么？

**学生**：等号当且仅当存在不全为零的 $\alpha,\beta\ge0$ 使 $\alpha|f|^p=\beta|g|^q$ 几乎处处成立。$p=q=2$ 时得 Cauchy–Schwarz 的积分形式 $\left|\int fg\right|\le\|f\|_2\|g\|_2$。另外取 $g\equiv1$ 得 $\|f\|_1\le\mu(X)^{1/q}\|f\|_p$。

**老师（拓展）**：它在哪些地方是关键工具？$\|f\|_p=0$ 怎么办？

**学生**：它是证明 $L^p$ 对偶 $(L^p)^*\cong L^q$、内插不等式、Riesz 表示定理的基础。若 $\|f\|_p=0$ 则 $f=0$ 几乎处处，结论平凡，证明中须单独排除这种退化情形。

## 相关条目

- [里斯-费舍尔定理](./里斯-费舍尔定理.md)：$L^p$ 空间完备性，Hölder 不等式是其中许多估计的基础。
- [单调收敛定理](./单调收敛定理.md)：积分与逐点不等式取极限的理论依据。
