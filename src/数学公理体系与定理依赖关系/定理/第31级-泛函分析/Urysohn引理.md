# Urysohn引理

> **一句话大白话**：在一个"足够好"的拓扑空间里，任意两个互不相交的闭集都能被一条连续函数彻底分开：一个上面恒为 $0$，另一个上面恒为 $1$，中间平滑过渡。

> **小例子**：取 $X=\mathbb{R}$，闭集 $A=\{0\}$、$B=\{2\}$，则 $f(x)=\max\{0,\min\{1,x/2\}\}$ 连续，且 $f(0)=0$、$f(2)=1$，就是一条现成的分离函数。

## 介绍

Urysohn 引理（Urysohn's Lemma）由苏联数学家乌雷松（P. S. Urysohn）于 1925 年提出，是点集拓扑中"正规性"这一分离公理最强大的推论。它要解决的问题是：一个只由开集语言定义的抽象拓扑空间，是否拥有足够多的连续实值函数，以致可以把不相交的闭集分离开？在此之前，函数与开集分属两个世界；Urysohn 引理第一次证明，只要空间是正规的（任意两个不相交闭集可被开集分离），就能造出一条具体的连续函数 $f:X\to[0,1]$。这条结论的意义在于"以函数刻画拓扑"：连续函数族不但足够丰富，还能再造出度量化、嵌入、延拓等一系列结果。它是 Tietze 延拓定理的直接前提，也是构造单位分解、证明 Urysohn 度量化定理以及现代分析中"用光滑函数逼近"套路的思想源头。

## 分析

**前置依赖**：拓扑空间与分离公理、正规空间、连续函数的定义、稠密子集、开集与闭包。

**定理内容**：设 $X$ 是正规拓扑空间，$A,B\subseteq X$ 是不相交的闭集。则存在连续函数 $f:X\to[0,1]$，使得

$$
f(x)=0\quad(\forall x\in A),\qquad f(x)=1\quad(\forall x\in B),
$$

且可要求 $0\le f\le1$ 处处成立。

**定理本质**：正规性恰好等价于"局部地插入中间开集"：若 $C\subseteq W$ 且 $C$ 闭、$W$ 开，则存在开集 $V$ 使 $C\subseteq V\subseteq\overline{V}\subseteq W$。Urysohn 的贡献是把这一"逐次插值"机制用到二进有理数上，造出一整族嵌套开集，再由这族开集读出函数值。

## 思考过程

难点在于"如何从开集造出函数"。关键想法是用二进有理数当刻度：先令 $U_1=X\setminus B$，再对每个二进有理数 $r\in(0,1)$ 造一个开集 $U_r$，使 $A\subseteq U_r$，且 $r<s$ 时 $\overline{U_r}\subseteq U_s$，形成一个随 $r$ 严格递增的嵌套开集塔。函数值就用"第一次进入"的刻度定义：$f(x)=\inf\{r:x\in U_r\}$。这样 $A$ 上的点因 $A\subseteq U_r$（所有 $r\in D$）而取 $0$，$B$ 上的点因落在 $U_1$ 之外而取 $1$。验证连续性时不去逐点估计，而是证明 $\{f<t\}=\bigcup_{r<t}U_r$ 与 $\{f>t\}=\bigcup_{s>t}(X\setminus\overline{U_s})$ 都是开集，二者构成 $[0,1]$ 的标准子基，从而 $f$ 连续。整体思路是"用开集结构承载函数的水平集"。

## 证明过程

**步骤 1：准备二进有理数与插值引理。** 记 $D=\{k2^{-n}:n\ge0,\ 1\le k\le2^{n}\}$ 为 $(0,1]$ 中的二进有理数集，它在 $(0,1]$ 中稠密。先证插值引理：若 $C$ 闭、$W$ 开且 $C\subseteq W$，则 $C$ 与 $X\setminus W$ 是不相交闭集，由 $X$ 正规存在开集 $V$ 使

$$
C\subseteq V\subseteq\overline{V}\subseteq W .
$$

**步骤 2：构造嵌套开集族 $\{U_r\}$。** 令 $U_1=X\setminus B$（开，且 $A\subseteq U_1$）。对 $n=1,2,\dots$ 逐层定义 $U_{k2^{-n}}$（$k$ 为奇数）：此时 $U_{(k-1)2^{-n}}$ 与 $U_{(k+1)2^{-n}}$ 已定义且满足闭包嵌套，由步骤 1 取 $U_{k2^{-n}}$ 使

$$
\overline{U_{(k-1)2^{-n}}}\subseteq U_{k2^{-n}}\subseteq\overline{U_{k2^{-n}}}\subseteq U_{(k+1)2^{-n}}.
$$

如此归纳地（利用二进有理数可数、逐层枚举）得到族 $\{U_r\}_{r\in D}$，满足对一切 $r<s$，

$$
A\subseteq U_r,\qquad \overline{U_r}\subseteq U_s .
$$

**步骤 3：定义分离函数。** 令

$$
f(x)=\begin{cases}\inf\{r\in D:x\in U_r\},&x\in U_1,\\ 1,&x\notin U_1.\end{cases}
$$

由于 $A\subseteq U_r$ 对每个 $r\in D$ 成立且 $A\subseteq U_1$，故 $x\in A$ 时 $f(x)=0$；又 $B\subseteq X\setminus U_1$，故 $x\in B$ 时 $f(x)=1$。显然 $0\le f\le1$。

**步骤 4：证明连续性。** 对任意实数 $t$，由嵌套性与二进有理数的稠密性可得两个水平集的精确表示

$$
\{f<t\}=\bigcup_{r\in D,\,r<t}U_r,\qquad \{f>t\}=\bigcup_{s\in D,\,s>t}\bigl(X\setminus\overline{U_s}\bigr).
$$

前者是开集之并，故开；后者是闭集之补的并，也开。验证第二个等式：若 $x\in X\setminus\overline{U_s}$（$s>t$），则 $x\notin U_r$ 对一切 $r<s$ 成立，故 $f(x)\ge s>t$；反之若 $f(x)>t$，取 $s$ 使 $t<s<f(x)$，则 $x\notin\overline{U_s}$。$[0,1]$ 的拓扑由形如 $[0,t)$ 与 $(t,1]$ 的集合生成，其原像都开，故 $f$ 连续。

**步骤 5：取值域调整。** 本构造已满足 $A$ 上为 $0$、$B$ 上为 $1$，且 $0\le f\le1$。若还需分离更一般的两组集合，可作平移伸缩 $g=\alpha f+\beta$ 把值域调到所需区间，连续性保持。

证毕。

## 相关条目

- [Tychonoff定理](./Tychonoff定理.md)：同为拓扑空间分离性的深入结果，与本引理同属"用开集刻画结构"的思路。
- [Tietze延拓定理](../第34级-代数拓扑/Tietze延拓定理.md)：以本引理为直接工具，把闭集上的连续函数延拓到全空间。
- [Riesz引理](./Riesz引理.md)：赋范空间中的几何分离思想，可与拓扑分离相互对照。
- [Stone-Weierstrass定理](./Stone-Weierstrass定理.md)：同样回答"连续函数族是否足够丰富"。
- [Baire纲定理](./Baire纲定理.md)：同属拓扑与分析交界处的基础工具。
