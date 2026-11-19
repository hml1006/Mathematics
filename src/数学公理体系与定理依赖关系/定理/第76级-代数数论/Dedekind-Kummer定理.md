# Dedekind–Kummer 定理

> **一句话大白话**：想知道素数 $p$ 在一个由 $\alpha$ 生成的数域里怎样分解，通常只需把 $\alpha$ 的极小多项式模 $p$ 分解；每个不可约因子就对应一个素理想，但前提是 $p$ 不整除指数 $[\mathcal O_K:\mathbb Z[\alpha]]$。
>
> **小例子**：对 $f(x)=x^3-2$ 与 $\alpha=\sqrt[3]{2}$，$f$ 在 $2$ 处 Eisenstein，因而 $2$ 不整除相应指数。模 $2$ 有 $f(x)\equiv x^3$，所以 $(2)=\mathfrak p^3$，其中 $\mathfrak p=(2,\alpha)$，剩余次数为 $1$，即 $2$ 完全分歧。

## 介绍

Dedekind–Kummer 定理把数域中素理想的分解转化为有限域上的多项式分解，是计算分歧指数和惯性次数的基本工具。定理的指数前提不可省略：当 $p$ 整除 $[\mathcal O_K:\mathbb Z[\alpha]]$ 时，直接把 $f\bmod p$ 的因子当作 $\mathcal O_K$ 的分解可能出错。

## 分析

**前置依赖**：代数整数与整基、数域整数环、素理想分解、有限域上的多项式唯一分解、中国剩余定理、理想指数。

**定理内容**：设 $K=\mathbb Q(\alpha)$，$\alpha$ 是代数整数，其首一极小多项式为 $f\in\mathbb Z[x]$，次数为 $n$。若有理素数满足

$$
p\nmid[\mathcal O_K:\mathbb Z[\alpha]],
$$

且在 $\mathbb F_p[x]$ 中

$$
\overline f(x)=\prod_{i=1}^g\overline g_i(x)^{e_i},
$$

其中 $\overline g_i$ 互不相同、首一且不可约，$g_i\in\mathbb Z[x]$ 是各自的首一提升，那么

$$
\mathfrak p_i=(p,g_i(\alpha))
$$

是互不相同的素理想，并且

$$
p\mathcal O_K=\prod_{i=1}^g\mathfrak p_i^{e_i},
\qquad e(\mathfrak p_i/p)=e_i,
\qquad f(\mathfrak p_i/p)=\deg g_i.
$$

两个常用的**不整除指数充分条件**是：若 $f$ 在 $p$ 处 Eisenstein，则 $p\nmid[\mathcal O_K:\mathbb Z[\alpha]]$；又因

$$
\operatorname{disc}(f)=[\mathcal O_K:\mathbb Z[\alpha]]^2\operatorname{disc}(K),
$$

若 $p^2\nmid\operatorname{disc}(f)$，也必有 $p\nmid[\mathcal O_K:\mathbb Z[\alpha]]$。这些条件都不能误写成“凡 $p\mid\operatorname{disc}(f)$ 就不能用定理”。

## 思考过程

环 $\mathbb Z[\alpha]/p\mathbb Z[\alpha]$ 同构于 $\mathbb F_p[x]/(\overline f)$，所以多项式模 $p$ 的分解自然产生商环的局部分解。要把这套分解提升到 $\mathcal O_K/p\mathcal O_K$，必须保证二者在 $p$ 处没有差别。

指数 $m=[\mathcal O_K:\mathbb Z[\alpha]]$ 正是这个差别的有限阶。若 $p\nmid m$，在 $p$-局部化后乘以 $m$ 可逆，自然映射成为同构；若 $p\mid m$，$\mathbb Z[\alpha]$ 在 $p$ 处可能不是极大序，朴素因子对应就可能遗漏或误认素理想。

## 证明过程

令 $m=[\mathcal O_K:\mathbb Z[\alpha]]$。当 $p\nmid m$ 时，对包含 $\mathbb Z[\alpha]$ 与 $\mathcal O_K$ 的有限商群在 $p$ 处局部化，$m$ 成为可逆因子，从而自然映射给出

$$
\mathcal O_K/p\mathcal O_K
\cong\mathbb Z[\alpha]/p\mathbb Z[\alpha]
\cong\mathbb F_p[x]/(\overline f).
$$

将 $\overline f=\prod_i\overline g_i^{e_i}$ 代入，并对中国剩余定理使用互素理想 $(\overline g_i^{e_i})$，得到

$$
\mathbb F_p[x]/(\overline f)
\cong\prod_{i=1}^g\mathbb F_p[x]/(\overline g_i^{e_i}).
$$

第 $i$ 个局部块对应的极大理想由 $(p,g_i(\alpha))$ 给出，其剩余域为 $\mathbb F_p[x]/(\overline g_i)$，故惯性次数为 $\deg g_i$；局部块中极大理想的幂零阶为 $e_i$，对应素理想分解中的指数 $e_i$。不同不可约因子给出不同极大理想，结论全部成立。$\square$

## 课堂问答

**老师**：Dedekind–Kummer 定理最关键的限制是什么？

**学生**：必须检查 $p\nmid[\mathcal O_K:\mathbb Z[\alpha]]$。满足时，若 $\overline f=\prod_i\overline g_i^{e_i}$，就有 $\mathfrak p_i=(p,g_i(\alpha))$、$p\mathcal O_K=\prod_i\mathfrak p_i^{e_i}$ 且 $f_i=\deg g_i$。指数条件不满足时不能机械套用。

**老师（追问）**：Eisenstein 条件在这里起什么作用？

**学生**：若极小多项式 $f$ 在 $p$ 处 Eisenstein，则 $p$ 不整除该指数，定理可用；此时模 $p$ 的分解是 $\overline f(x)=x^n$，故 $p$ 完全分歧，局部素理想可写为 $(p,\alpha)$，且 $e=n,f=1$。

**老师（拓展）**：判别式能给出一个更快的检查吗？

**学生**：可以。由 $\operatorname{disc}(f)=m^2\operatorname{disc}(K)$，若 $p^2\nmid\operatorname{disc}(f)$，则 $p\nmid m$。反过来不成立：$p^2$ 整除多项式判别式并不自动说明 $p$ 整除指数，更不自动说明定理失效。

## 相关条目

- [素理想分解与分歧惯性定理](./素理想分解与分歧惯性定理.md)：本定理计算出的 $e_i,\deg g_i$ 满足 $n=\sum_ie_if_i$。
- [数域整数环是 Dedekind 整环](./数域整数环是Dedekind整环.md)：提供素理想分解与局部理想理论所需的环结构。
