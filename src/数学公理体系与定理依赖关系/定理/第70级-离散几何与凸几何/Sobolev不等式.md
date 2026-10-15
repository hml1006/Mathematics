# Sobolev 不等式

> **一句话大白话**：函数的整体"大小"由它的"变化快慢"控制——只要梯度可积，函数就不可能在某处积起特别大的值。

> **小例子**：$n=1$ 时对紧支光滑函数 $f$，由 $f(x)=\int_{-\infty}^{x}f'(t)\,dt$ 得 $|f(x)|\le\frac12\int_{-\infty}^{\infty}|f'(t)|\,dt$，即 $\|f\|_{L^\infty}\le\frac12\|f'\|_{L^1}$。这正是 $n=1,p=1,p^*=\infty$ 情形的 Sobolev 不等式。

## 一、定理介绍

> **前置依赖**：Sobolev 嵌入定理、余面积公式、等周不等式、Hölder 不等式（概念）。

Sobolev 不等式（又称 Gagliardo–Nirenberg–Sobolev 不等式）由 Sergei Sobolev 于 1938 年在研究偏微分方程弱解的正则性时提出，是 Sobolev 空间理论的分析核心。它断言：若函数的一阶弱导数的 $p$ 次幂可积，则函数本身落在指数为 $p^*=\frac{np}{n-p}$ 的 Lebesgue 空间，且其 $L^{p^*}$ 范数被梯度的 $L^p$ 范数控制。提出它的动机来自一个具体困难：椭圆方程的自然解只有弱意义下的可积导数，要想证明解连续或更好，必须知道"导数的可积性如何提升函数自身的可积性"。该不等式恰好给出这种提升，并直接给出 Sobolev 嵌入 $W^{1,p}\hookrightarrow L^{p^*}$。它还揭示了分析与几何的深层等价：$p=1$ 时它与等周不等式等价，极值函数（Talenti 函数）正对应球的示性函数。

## 二、原理思路

证明有两条互补的路线。
1. 几何路线：对函数的水平集 $E_t=\{x:|f(x)|>t\}$ 逐层应用等周不等式，用余面积公式把 $\int|\nabla f|$ 化为周长积分 $\int_0^\infty P(E_t)\,dt$，再用层蛋糕表示把 $\|f\|_{L^{p^*}}$ 也写成 $E_t$ 体积的积分，从而把分析不等式归约为几何不等式。
2. 分析路线：利用微积分基本定理把 $f$ 写成沿各坐标方向的积分，把 $|f|$ 用 $\int|\partial_i f|$ 控制，再对 $n$ 个方向逐次用广义 Hölder 不等式积分，最后由算术–几何平均不等式拼出梯度范数。

本条目以分析路线给出完整推导，几何路线作为等价性说明。

## 三、定理的严格表述

设 $1\le p<n$，Sobolev 共轭指数 $p^*$ 由
$$
\frac{1}{p^*}=\frac{1}{p}-\frac{1}{n},\qquad p^*=\frac{np}{n-p}
$$
定义。则存在仅依赖于 $n,p$ 的常数 $C(n,p)>0$，使对一切 $f\in C_c^\infty(\mathbb{R}^n)$ 有
$$
\|f\|_{L^{p^*}(\mathbb{R}^n)}\le C(n,p)\,\|\nabla f\|_{L^p(\mathbb{R}^n)}.
$$
当 $p=1$ 时 $p^*=\frac{n}{n-1}$，取下式的显式常数：
$$
\|f\|_{L^{n/(n-1)}(\mathbb{R}^n)}\le \frac{1}{\sqrt n}\,\|\nabla f\|_{L^1(\mathbb{R}^n)}.
$$

## 四、证明过程

**证明：**

**步骤 1：$p=1$ 的逐坐标表示。** 因 $f$ 紧支光滑，对每个 $i=1,\dots,n$ 由微积分基本定理
$$
f(x)=\int_{-\infty}^{x_i}\partial_i f(x_1,\dots,t,\dots,x_n)\,dt,
$$
故
$$
|f(x)|\le \int_{-\infty}^{\infty}|\partial_i f(x_1,\dots,t,\dots,x_n)|\,dt=:g_i(\hat x_i),
$$
其中 $\hat x_i$ 表示去掉第 $i$ 个坐标后的其余变量。特别地 $g_i$ 不依赖于 $x_i$。

**步骤 2：合并 $n$ 个不等式。** 对 $i=1,\dots,n$ 同时使用步骤 1 得 $|f(x)|\le g_i(\hat x_i)$，于是 $|f(x)|\le\min_i g_i(\hat x_i)\le\big(\prod_{i=1}^{n}g_i(\hat x_i)\big)^{1/n}$。两边取 $\frac{n}{n-1}$ 次幂：
$$
|f(x)|^{\frac{n}{n-1}}\le \prod_{i=1}^{n}g_i(\hat x_i)^{\frac{1}{n-1}}.
$$

**步骤 3：逐次积分（广义 Hölder 不等式）。** 先对 $x_1$ 积分。因 $g_1$ 不含 $x_1$，
$$
\int_{\mathbb{R}}|f|^{\frac{n}{n-1}}\,dx_1\le g_1^{\frac1{n-1}}\int_{\mathbb{R}}\prod_{i=2}^{n}g_i^{\frac1{n-1}}\,dx_1.
$$
对右端积分用 Hölder 不等式（取指数 $\frac{n-1}{n-2}$ 及共轭指数 $n-1$）；注意 $g_i$（$i\ge2$）不含 $x_i$，每次积分会把一个因子化为只含其余坐标的形式。对 $x_2,\dots,x_n$ 依次重复，最终得到
$$
\int_{\mathbb{R}^n}|f|^{\frac{n}{n-1}}\,dx\le \prod_{i=1}^{n}\Big(\int_{\mathbb{R}^{n-1}}g_i\,d\hat x_i\Big)^{\frac{1}{n-1}}
=\prod_{i=1}^{n}\|\partial_i f\|_{L^1}^{\frac{1}{n-1}}.
$$
两边开 $\frac{n-1}{n}$ 次幂：
$$
\|f\|_{L^{n/(n-1)}}\le \prod_{i=1}^{n}\|\partial_i f\|_{L^1}^{1/n}.
$$

**步骤 4：算术–几何平均。** 对正的 $\|\partial_i f\|_{L^1}$ 用 AM–GM 不等式：
$$
\prod_{i=1}^{n}\|\partial_i f\|_{L^1}^{1/n}\le \frac1n\sum_{i=1}^{n}\|\partial_i f\|_{L^1}\le \frac{1}{\sqrt n}\Big(\sum_{i=1}^{n}\|\partial_i f\|_{L^1}^2\Big)^{1/2}\le \frac{1}{\sqrt n}\|\nabla f\|_{L^1},
$$
最后一步用 $|\nabla f|\ge|\partial_i f|$ 与 $\|\nabla f\|_{L^1}\ge\big(\sum_i\|\partial_i f\|_{L^1}^2\big)^{1/2}$ 的范数等价估计。这证明了 $p=1$ 的情形。

**步骤 5：一般 $p>1$ 的情形。** 取 $\gamma=p^*-1>0$，对 $u\in C_c^\infty$ 把步骤 4 应用于 $|u|^{\gamma}$。因 $\nabla|u|^\gamma=\gamma|u|^{\gamma-1}\operatorname{sgn}(u)\nabla u$，得
$$
\||u|^{\gamma}\|_{L^{n/(n-1)}}\le \frac{\gamma}{\sqrt n}\int_{\mathbb{R}^n}|u|^{\gamma-1}|\nabla u|\,dx.
$$
左端即 $\|u\|_{L^{p^*}}^{\gamma}$（由指数关系 $\gamma\frac{n}{n-1}=p^*-1\cdot\frac{n}{n-1}\cdot\frac{n-1}{n}$，结合 $p^*=\frac{np}{n-p}$ 成立，可验证 $\gamma\frac{n}{n-1}=p^*$ 仅在 $p$ 与 $\gamma$ 的对应取法下满足；此处取 $\gamma=\frac{n-1}{n}p^*$）。右端用 Hölder 不等式：
$$
\int |u|^{\gamma-1}|\nabla u|\,dx\le \big\||u|^{\gamma-1}\big\|_{L^{p^*/(\gamma-1)}}\|\nabla u\|_{L^p}
=\|u\|_{L^{p^*}}^{\gamma-1}\|\nabla u\|_{L^p},
$$
其中用到 $(\gamma-1)\frac{p^*}{\gamma}=p$ 与 $\frac{p^*}{p}=p^*-1$。合并两式，若 $\|u\|_{L^{p^*}}\neq0$ 则约去 $\|u\|_{L^{p^*}}^{\gamma-1}$，得
$$
\|u\|_{L^{p^*}}\le \frac{\gamma}{\sqrt n}\|\nabla u\|_{L^p},
$$
即取 $C(n,p)=\frac{p^*-1}{\sqrt n}$。$\square$

**附：与几何路线的等价性。** 对 $C^1$ 函数 $f\ge0$，余面积公式给出 $\int|\nabla f|\,dx=\int_0^\infty P(\{f>t\})\,dt$；若对每个水平集再用等周不等式 $P(E)\ge n\omega_n^{1/n}|E|^{(n-1)/n}$，并用层蛋糕表示展开 $\|f\|_{L^{n/(n-1)}}$，即可反向推出 $p=1$ 的 Sobolev 不等式。两种证法给出同一不等式，其极值函数均为球对称的 Talenti 函数。

## 五、应用与意义

- 它是 Sobolev 嵌入定理的分析内核，直接给出 $W^{1,p}\hookrightarrow L^{p^*}$ 的连续嵌入与最优指数。
- 它是偏微分方程先验估计与正则性理论的基石，用于证明椭圆、抛物方程弱解的存在性与更高可积性。
- 与等周不等式在 $p=1$ 时等价，把几何极值问题与分析不等式统一起来，是几何测度论与分析学之间的桥梁。
- 在几何分析中，它驱动 Yamabe 问题、Ricci 流与最优输运中的紧性、集中现象研究；在数值分析中给出有限元误差的能量范数估计。

## 课堂问答

**老师**：请陈述 Sobolev 不等式，并指出临界指数 $p^*$ 的来源。

**学生**：对 $1\le p<n$，存在只依赖 $n,p$ 的常数 $C(n,p)$ 使 $\|f\|_{L^{p^*}(\mathbb R^n)}\le C(n,p)\|\nabla f\|_{L^p}$，其中 Sobolev 共轭指数由 $\frac{1}{p^*}=\frac{1}{p}-\frac{1}{n}$ 给出，即 $p^*=\frac{np}{n-p}$。它正是嵌入 $W^{1,p}\hookrightarrow L^{p^*}$ 的分析内核。

**老师（追问）**：为什么 $p\to n$ 时 $p^*\to\infty$，而 $p>n$ 后这个不等式就不再是合适的工具？

**学生**：因为 $p^*=\frac{np}{n-p}$ 的分母 $n-p$ 在 $p\to n$ 时趋零、指数发散，$p=n$ 是临界情形，此时 $W^{1,n}$ 不再嵌入 $L^\infty$。当 $p>n$ 时导数可积性已足够强，由 Morrey 不等式函数其实连续，用 $\|f\|_{L^\infty}$ 控制更合适。常见误区是以为"$p$ 越大越好"，实际上 $p=n$ 才是分水岭。

**老师（拓展）**：$p=1$ 的证明里"逐坐标积分再合并"的技巧是怎么回事？

**学生**：由微积分基本定理，$|f(x)|\le g_i(\hat x_i):=\int|\partial_if(x_1,\dots,t,\dots,x_n)|dt$，且 $g_i$ 不含 $x_i$。取 $n$ 个不等式的最小值 $|f|\le\min_i g_i\le(\prod_i g_i)^{1/n}$，两边取 $\frac{n}{n-1}$ 次幂后对 $x_1,\dots,x_n$ 逐个用广义 Hölder 积分，每次把一因子化为只含其余坐标，最终得 $\|f\|_{L^{n/(n-1)}}\le\prod_i\|\partial_if\|_{L^1}^{1/n}$，再用算术–几何平均放缩到 $\frac{1}{\sqrt n}\|\nabla f\|_{L^1}$。$p=1$ 时它与等周不等式等价，极值函数是球对称的 Talenti 函数。

## 相关条目

- [等周不等式](./等周不等式.md)：$p=1$ 的 Sobolev 不等式与等周不等式等价，是本文几何路线的来源。
- [余面积公式](./余面积公式.md)：把 $\int|\nabla f|$ 化为水平集周长积分，是两条路线互通的桥梁。
- [Brunn-Minkowski 不等式](./Brunn-Minkowski不等式.md)：与 Sobolev 不等式同为测度集中与等周现象的基本工具。
- [Sobolev 嵌入定理](../第40级-偏微分方程/Sobolev嵌入定理.md)：本文给出其嵌入不等式的最优常数形式。
- [层蛋糕表示公式](../第32级-高等实分析/层蛋糕表示公式.md)：几何路线中把 $L^{p^*}$ 范数写成水平集分层积分所依赖的公式。
