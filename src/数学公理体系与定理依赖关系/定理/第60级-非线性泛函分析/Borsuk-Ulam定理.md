# Borsuk–Ulam 定理

> **一句话大白话**：球面上无论怎样连续地测量不超过球面维数的几个数值，总存在一对正对面的点，测出来的结果完全一样——这种"巧合"是拓扑强制的，躲不掉。
>
> **小例子**：$n=2$ 时，地球表面任意时刻总有一对对径点温度与气压都相同；$n=1$ 时，赤道上任意连续函数必有一对对径点取相同值。

## 一、定理介绍

> **前置依赖**：度理论、Leray-Schauder度理论、射影空间的 $\mathbb Z/2$ 上同调与杯积结构、覆盖空间提升定理、对径映射与商空间构造。

Borsuk–Ulam 定理（Borsuk–Ulam theorem）由 Karol Borsuk 于 1933 年证明，是代数拓扑中最经典的"不存在性"定理之一。它断言：$n$ 维球面上任何到 $n$ 维欧氏空间的连续映射必有一对对径点取同值；等价的说法是：不存在从 $S^n$ 到 $S^{n-1}$ 的连续奇映射（odd map，满足 $f(-x)=-f(x)$）。

Borsuk 的原始动机来自对紧致度量空间对称性的研究：他希望把"球面不能被连续地展开到更低维球面"这一几何直觉化为可严格验证的命题。1930 年代 Ulam 在苏格兰咖啡馆（Scottish Café）问题集中提出的"地球对径点问题"（任意时刻存在温度与气压都相同的对径点）使该定理广为人知。

定理的意义有三个层面。其一，它与 Brouwer 不动点定理、Lusternik–Schnirelmann 定理互相等价，共同刻画 $\mathbb R^n$ 与 $S^n$ 的固有维数。其二，它给出火腿三明治定理等组合几何结果。其三，它的标准证明示范了 $\mathbb Z/2$ 等变上同调与射影空间上同调环的威力，是"用代数不变量判定映射不存在"的范式。

## 二、原理思路

证明的基本策略是把连续映射的存在性化归为代数不变量的不可能性：

1. **化归为奇映射**：若连续 $f:S^n\to\mathbb R^n$ 处处 $f(x)\neq f(-x)$，则把 $f(x)-f(-x)$ 单位化即得 $S^n\to S^{n-1}$ 的连续奇映射。于是定理等价于：不存在连续奇映射 $S^n\to S^{n-1}$。

2. **对径商化**：奇映射与对径作用 $x\mapsto-x$ 相容，因而下降为射影空间之间的连续映射 $\bar g:\mathbb{RP}^n\to\mathbb{RP}^{n-1}$。

3. **上同调环的阶数矛盾**：$\mathbb Z/2$ 系数下 $H^*(\mathbb{RP}^m;\mathbb Z/2)=\mathbb Z/2[\beta]/(\beta^{m+1})$。只需说明 $\bar g$ 在 $H^1$ 上不为零，那么 $\bar g^*(\beta^n)=(\bar g^*\beta)^n$ 落在 $H^n(\mathbb{RP}^n)$ 中非零，而 $\beta^n\in H^n(\mathbb{RP}^{n-1})=0$，维数越界给出矛盾。

## 三、定理的严格表述

**定理（Borsuk–Ulam）**：设 $n\geq1$ 为整数，$f:S^n\to\mathbb R^n$ 连续，则存在 $x\in S^n$ 使得
$$f(x)=f(-x).$$

**等价形式一（奇映射形式）**：不存在连续映射 $g:S^n\to S^{n-1}$ 满足
$$g(-x)=-g(x),\qquad \forall\, x\in S^n.$$

**等价形式二（低维目标）**：若连续 $f:S^n\to\mathbb R^m$ 且 $m\leq n$，则存在 $x\in S^n$ 使 $f(x)=f(-x)$。$m<n$ 时把它与坐标投影 $\mathbb R^n\to\mathbb R^m$ 复合，即可由定理直接得到。

**等价形式三（Lusternik–Schnirelmann）**：若 $S^n$ 被 $n+1$ 个闭集 $F_1,\dots,F_{n+1}$ 覆盖，则其中某个 $F_i$ 含有互相对径的点对。

## 四、证明过程

**步骤 1（化归为奇映射的不存在性）。** 反设 $f:S^n\to\mathbb R^n$ 满足 $f(x)\neq f(-x)$ 对一切 $x$。则 $x\mapsto f(x)-f(-x)$ 连续且处处非零，其模长连续且恒正，故
$$g(x)=\frac{f(x)-f(-x)}{\lvert f(x)-f(-x)\rvert}$$
连续且取值于单位球面 $S^{n-1}\subset\mathbb R^n$，并满足 $g(-x)=-g(x)$。反之，若这样的连续奇映射 $g$ 存在，把它视为 $\mathbb R^n$ 值函数即得处处 $f(x)\neq f(-x)$ 的映射（因为 $g(x)=-g(-x)\neq g(-x)$）。故原定理与"不存在连续奇映射 $S^n\to S^{n-1}$"等价。

**步骤 2（$n=1$ 的情形）。** 此时 $S^0=\{\pm1\}$。若 $g:S^1\to S^0$ 连续，因 $S^1$ 连通而 $S^0$ 不连通，故 $g$ 为常值映射。但奇性要求 $g(x)=-g(-x)$，非零映射不可能取常值，矛盾。故 $n=1$ 时不存在这样的奇映射。

**步骤 3（对径作用与射影空间）。** 设 $n\geq2$。在 $S^n$ 上考虑对径作用 $\mathbb Z/2$，商空间为 $\mathbb{RP}^n=S^n/\{\pm1\}$。由 $g(-x)=-g(x)$ 知 $g$ 与该作用可交换，故由商映射的泛性质，$g$ 诱导唯一的连续映射
$$\bar g:\mathbb{RP}^n\longrightarrow\mathbb{RP}^{n-1},\qquad \bar g\circ q_n=q_{n-1}\circ g,$$
其中 $q_m:S^m\to\mathbb{RP}^m$ 为商映射。

**步骤 4（射影空间的 $\mathbb Z/2$ 上同调环）。** $\mathbb{RP}^m$ 有每个维度恰一个胞腔的胞腔分解 $e^0\cup e^1\cup\cdots\cup e^m$。其胞腔上链复形在 $\mathbb Z$ 系数下微分为交替的 $0$ 与乘以 $2$，模 $2$ 后全部消失，故
$$H^k(\mathbb{RP}^m;\mathbb Z/2)\cong\begin{cases}\mathbb Z/2,&0\leq k\leq m,\\ 0,&k>m.\end{cases}$$
设 $\beta\in H^1(\mathbb{RP}^m;\mathbb Z/2)$ 为生成元，则 $\beta^k$ 生成 $H^k$，且
$$H^*(\mathbb{RP}^m;\mathbb Z/2)\cong\mathbb Z/2[\beta]/(\beta^{m+1}).$$
特别地 $\beta^{m}\neq0$ 而 $\beta^{m+1}=0$。

**步骤 5（$\bar g$ 在 $H^1$ 上是同构）。** 由 Hurewicz 定理与万有系数定理，$H^1(\mathbb{RP}^k;\mathbb Z/2)\cong\operatorname{Hom}(\pi_1(\mathbb{RP}^k),\mathbb Z/2)\cong\mathbb Z/2$。先证 $\bar g$ 诱导的 $\pi_1$ 同态 $\bar g_*:\pi_1(\mathbb{RP}^n)\to\pi_1(\mathbb{RP}^{n-1})$ 非零。否则 $\bar g$ 可提升（覆盖空间提升定理）到万有覆叠 $S^{n-1}$，得到 $\tilde g:\mathbb{RP}^n\to S^{n-1}$；于是 $h:=\tilde g\circ q_n:S^n\to S^{n-1}$ 满足 $h(-x)=h(x)$，因为 $q_n(-x)=q_n(x)$。另一方面 $q_{n-1}\circ h=q_{n-1}\circ g$ 说明 $h(x)=\pm g(x)$ 对一切 $x$；由 $S^n$（$n\geq1$）连通，符号必为常数，于是 $g$ 与偶映射 $h$ 相差整体符号，本身也是偶映射，这与 $g$ 是非常值奇映射矛盾。故 $\bar g_*$ 非零；由于 $H^1\cong\operatorname{Hom}(\pi_1,\mathbb Z/2)$，得
$$\bar g^*:H^1(\mathbb{RP}^{n-1};\mathbb Z/2)\longrightarrow H^1(\mathbb{RP}^n;\mathbb Z/2)$$
是同构，即 $\alpha:=\bar g^*(\beta)$ 是 $H^1(\mathbb{RP}^n;\mathbb Z/2)$ 的非零元。

**步骤 6（环同态导出矛盾）。** $\bar g^*$ 是分次环同态，故
$$\bar g^*(\beta^{\,n})=\alpha^{\,n}.$$
右端：$\alpha\neq0$ 生成 $H^1(\mathbb{RP}^n;\mathbb Z/2)$，故 $\alpha^{\,n}$ 生成 $H^n(\mathbb{RP}^n;\mathbb Z/2)\cong\mathbb Z/2$，从而 $\alpha^{\,n}\neq0$。左端：$\beta^{\,n}\in H^n(\mathbb{RP}^{n-1};\mathbb Z/2)=0$，故 $\bar g^*(\beta^{\,n})=0$。两端矛盾。因此不存在连续奇映射 $S^n\to S^{n-1}$，由步骤 1 定理得证。$\square$

## 五、应用与意义

- **对径点问题**：地球上任意时刻存在一对对径点，其温度与气压（或任意 $2$ 个连续测量量）完全一致。
- **火腿三明治定理**：任意 $n$ 块可测的"火腿"可被一张超平面同时平分，其证明把 Borsuk–Ulam 应用于"平分超平面"的连续参数化。
- **Brouwer 不动点定理与 Lusternik–Schnirelmann 定理**：与 Borsuk–Ulam 互相等价，共同刻画 $\mathbb R^n$ 与 $S^n$ 的固有维数。
- **拓扑组合学**：Kneser 猜想的 Lovász 证明、Tucker 引理及多种离散不动点定理均以 Borsuk–Ulam 为原型。
- **非线性分析**：与 Leray–Schauder 度、Schauder 不动点定理配合，用于证明对称非线性方程的非零解与对称破缺，是临界点理论（山路引理、喷泉定理）的拓扑基础之一。

## 课堂问答

**老师**：Borsuk-Ulam 定理"必有一对对径点取同值"，它的代数证明靠什么不变量？

**学生**：靠射影空间的 $\mathbb Z/2$ 上同调环。先把问题化为"不存在连续奇映射 $S^n\to S^{n-1}$"：若 $f(x)\neq f(-x)$，则 $g(x)=\frac{f(x)-f(-x)}{|f(x)-f(-x)|}$ 就是连续奇映射。奇映射与对径作用交换，下降为 $\bar g:\mathbb{RP}^n\to\mathbb{RP}^{n-1}$。由 $H^*(\mathbb{RP}^m;\mathbb Z/2)=\mathbb Z/2[\beta]/(\beta^{m+1})$，若 $\bar g^*$ 在 $H^1$ 上非零则 $\bar g^*(\beta^n)=(\bar g^*\beta)^n\neq0$，但 $\beta^n\in H^n(\mathbb{RP}^{n-1})=0$，矛盾；而 $\bar g^*$ 在 $H^1$ 上必非零，否则 $\bar g$ 可提升到 $S^{n-1}$，迫使 $g$ 为偶映射，与奇性矛盾。

**老师（追问）**：$n=1$ 的低维情形还需要上同调吗？

**学生**：不需要，用连通性即可。$S^0=\{\pm1\}$ 不连通而 $S^1$ 连通，故连续 $g:S^1\to S^0$ 必为常值，但奇性 $g(x)=-g(-x)$ 不允许非零常值映射，矛盾。这也说明定理的困难恰在 $n\ge2$ 时"对径商化加上同调环"所提供的额外信息量。

**老师（拓展）**：Borsuk-Ulam 与 Brouwer 不动点、Lusternik-Schnirelmann 是什么关系？

**学生**：三者在紧凸/球面情形互相等价，共同刻画 $\mathbb R^n$ 与 $S^n$ 的固有维数。Borsuk-Ulam 的覆盖形式即 LS 定理：若 $S^n$ 被 $n+1$ 个闭集覆盖，则其中某个含对径点对。应用上它给出火腿三明治定理（$n$ 块火腿可被一张超平面同时平分）、Kneser 猜想的 Lovász 证明，以及奇非线性方程对称解的存在性（配合 Leray-Schauder 度中奇映射的度为奇数）。

## 相关条目

- [Leray-Schauder度理论](./Leray-Schauder度理论.md)：用映射度给出"奇映射不存在"的另一条证明路线，并把结论推广到非线性算子的对称解。
- [Schauder不动点定理](./Schauder不动点定理.md)：同属拓扑不动点方法，用于非线性方程解的存在性。
- [山路引理](./山路引理.md)：对称变分问题中借助拓扑不变量获得临界点的典型方法。
- [度理论](../第34级-代数拓扑/度理论.md)：奇映射的映射度必为奇数，是 Borsuk–Ulam 的等价刻画之一。
- [上同调与杯积结构](../第34级-代数拓扑/上同调与杯积结构.md)：射影空间上同调环与杯积计算是本证明的代数核心。
- [覆盖空间提升定理](../第34级-代数拓扑/覆盖空间提升定理.md)：步骤 5 中把 $\pi_1$ 上的零同态提升为到覆叠空间的映射。
