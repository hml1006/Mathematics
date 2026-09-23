# Baker-Campbell-Hausdorff 公式

> **一句话大白话**：两个矩阵的指数相乘 $\exp X\exp Y$，一般不等于 $\exp(X+Y)$；Baker-Campbell-Hausdorff 公式把差距精确补上——补出来的 $Z$ 完全由 $X,Y$ 的多重李括号写成，说明群乘法的"扭曲"全部编码在李括号里。

> **小例子**：取 $X=\begin{pmatrix}0&a\\0&0\end{pmatrix}$、$Y=\begin{pmatrix}0&0\\b&0\end{pmatrix}$，则 $[X,Y]=\begin{pmatrix}ab&0\\0&-ab\end{pmatrix}$ 与 $X,Y$ 都对易，此时 $\exp X\exp Y=\exp(X+Y+\frac12[X,Y])$，公式只需到一阶括号项即精确。

## 一、定理介绍

> **前置依赖**：李代数与李括号、指数映射、伴随表示、形式幂级数与 Bernoulli 数（概念）、Lie 群与李代数的对应（概念）。

Baker-Campbell-Hausdorff（BCH）公式由 Henry Frederick Baker（1905）、John Edward Campbell（1897–1903）与 Felix Hausdorff（1906）先后研究，后由 Dynkin（1947）给出显式通项。它给出：当 $X,Y$ 充分接近 $0$ 时，存在 $Z$（由 $X,Y$ 的迭代李括号组成的收敛级数）使 $\exp X\exp Y=\exp Z$。它解决的问题是把局部李群的乘法用李代数运算显式表示，其深刻含义是：李群的局部结构完全由李括号决定，这正是李群–李代数对应成立的根本原因。它也是量子力学（算符对易子展开）、算子分裂数值方法与控制论中 Lie 级数展开的基础工具。

## 二、原理思路

1. 记 $Z(t)=\log(\exp(tX)\exp(tY))$，由指数映射在 $0$ 附近的局部逆，$Z(t)$ 对小的 $t$ 解析，且 $Z(0)=0$。
2. 对 $t$ 求导，利用"指数导数的伴随公式" $\frac{d}{dt}e^{Z}=e^{Z}\frac{1-e^{-\operatorname{ad}Z}}{\operatorname{ad}Z}\dot Z$，把 $Z$ 的微分方程写成关于 $\operatorname{ad}Z$ 的形式幂级数方程。
3. 把该方程按 $t$ 的幂次展开，逐阶递推解出系数（$Z_1=X+Y$、$Z_2=\frac12[X,Y]$ 等），即得 Dynkin 通项公式。

## 三、定理的严格表述

设 $\mathfrak{g}$ 是有限维实或复李代数（或含单位元的结合代数视作李代数）。则存在 $0$ 的邻域 $U\subseteq\mathfrak{g}$，使对一切 $X,Y\in U$，$\exp X\exp Y$ 落在指数映射的像中，且存在唯一 $Z\in\mathfrak{g}$ 使得
$$
\exp X\exp Y=\exp Z,\qquad Z=\log(\exp X\exp Y).
$$
$Z$ 可写成收敛的多重李括号级数（Dynkin 公式）：
$$
Z=\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}\sum_{\substack{r_i+s_i>0\\1\le i\le n}}\frac{[X^{r_1}Y^{s_1}\cdots X^{r_n}Y^{s_n}]}{r_1!s_1!\cdots r_n!s_n!\,\big(\sum_{i=1}^{n}(r_i+s_i)\big)}.
$$
低阶展开为
$$
Z=X+Y+\frac12[X,Y]+\frac1{12}\big[X,[X,Y]\big]+\frac1{12}\big[Y,[Y,X]\big]-\frac1{24}\big[Y,[X,[X,Y]]\big]+\cdots
$$

## 四、证明过程

**证明：**

**步骤 1：$Z(t)$ 的存在与解析性。** 定义 $\gamma(t)=\exp(tX)\exp(tY)$。由于 $\exp$ 在 $0$ 处是局部微分同胚，对小的 $t$，$\gamma(t)$ 落在 $\exp$ 的像内且可唯一写成 $\gamma(t)=\exp Z(t)$，$Z(0)=0$。$\gamma$ 解析，$\log$ 在恒等元附近解析，故 $t\mapsto Z(t)$ 在 $0$ 附近解析，可写 $Z(t)=\sum_{k\ge1}Z_k t^k$。

**步骤 2：指数导数的伴随公式。** 对算子 $Z$，有恒等式
$$
\frac{d}{dt}e^{Z(t)}=e^{Z(t)}\cdot\frac{1-e^{-\operatorname{ad}Z(t)}}{\operatorname{ad}Z(t)}\,\dot Z(t),
$$
其中 $\frac{1-e^{-u}}{u}=1-\frac u2+\frac{u^2}{6}-\cdots$ 是整函数，$\operatorname{ad}Z$ 按幂级数代入。该式由 $\frac{d}{dt}e^{Z}=\int_0^1e^{sZ}\dot Z e^{(1-s)Z}ds$ 与 $\operatorname{ad}$ 的展开推出。

**步骤 3：导出 $Z$ 的微分方程。** 另一方面
$$
\frac{d}{dt}\gamma(t)=X\exp(tX)\exp(tY)+\exp(tX)Y\exp(tY)=X\,e^{Z}+e^{t\operatorname{ad}X}Y\,e^{Z}.
$$
利用 $e^{-Z}Ye^{Z}=e^{\operatorname{ad}Z}Y$ 把第二项左提出 $e^Z$：
$$
X\,e^{Z}+e^{t\operatorname{ad}X}Y\,e^{Z}=\big(X+e^{t\operatorname{ad}X}Y\big)e^{Z}=e^{Z}\Big(e^{-\operatorname{ad}Z}\big(X+e^{t\operatorname{ad}X}Y\big)\Big).
$$
与步骤 2 的 $e^{Z}\frac{1-e^{-\operatorname{ad}Z}}{\operatorname{ad}Z}\dot Z$ 比较（$e^Z$ 可逆），得
$$
\frac{1-e^{-\operatorname{ad}Z}}{\operatorname{ad}Z}\dot Z=e^{-\operatorname{ad}Z}\big(X+e^{t\operatorname{ad}X}Y\big),
$$
故
$$
\dot Z(t)=f(\operatorname{ad}Z)\big(X+e^{t\operatorname{ad}X}Y\big),\qquad f(u)=\frac{u}{e^{u}-1}=1-\frac u2+\frac{u^2}{12}-\cdots
$$
（用了 $\frac{u}{1-e^{-u}}e^{-u}=\frac{u}{e^{u}-1}$）。

**步骤 4：解出一阶项。** 令 $t=0$：$Z(0)=0$，$f(0)=1$，$e^{0}=\mathrm{id}$，故 $\dot Z(0)=X+Y$，即 $Z_1=X+Y$。

**步骤 5：解出二阶项。** 对步骤 3 的方程再求导并在 $t=0$ 取值。记 $A=\operatorname{ad}Z$，则
$$
\ddot Z=f'(A)(\operatorname{ad}\dot Z)\big(X+e^{t\operatorname{ad}X}Y\big)+f(A)\,\operatorname{ad}X\,e^{t\operatorname{ad}X}Y.
$$
在 $t=0$：$A=0$，$f(0)=1$，$f'(0)=-\frac12$，$\dot Z(0)=X+Y$，
$$
\ddot Z(0)=-\frac12\operatorname{ad}(X+Y)(X+Y)+[X,Y]=-\frac12\big([X,Y]+[Y,X]\big)+[X,Y]=[X,Y].
$$
于是 $Z_2=\frac12\ddot Z(0)=\frac12[X,Y]$。

**步骤 6：递推与通项。** 一般地，把 $f(\operatorname{ad}Z)$ 与 $e^{t\operatorname{ad}X}$ 都按 $t$ 展开，代入步骤 3 的方程，比较 $t^{k-1}$ 的系数即得 $Z_k$ 的递推式：右端只含 $Z_1,\dots,Z_{k-1}$ 与 $X,Y$ 的括号，故可逐阶唯一解出。这一递推的显式解即为步骤 3 所述 Dynkin 公式（系数由 Bernoulli 数 $B_n$ 与括号的多项式给出，$\frac{u}{e^u-1}$ 的展开系数正是 Bernoulli 数）。前三阶给出
$$
Z=X+Y+\frac12[X,Y]+\frac1{12}\big[X,[X,Y]\big]+\frac1{12}\big[Y,[Y,X]\big]+\cdots
$$
级数在 $X,Y$ 充分小时收敛（应用 Cauchy 估计控制 $Z_k$）。$\square$

## 五、应用与意义

- 它是李群–李代数对应的核心：群乘法在单位元附近完全由李括号决定，从而同构的李代数给出局部同构的李群。
- 在量子力学中，算符的 BCH 展开给出对易子修正，是 Weyl 量子化、路径积分与对称性分析的标准工具。
- 在数值分析中，它解释算子分裂（如 Strang 分裂）与 Lie 群积分器的精度阶，是几何数值积分的设计依据。
- 在控制论中，Lie 级数展开用于非线性系统的能达性分析与 Chow–Rashevskii 定理。
- BCH 的无穷级数与 Magnus 展开是常微分方程指数积分与自由李代数研究的出发点。

## 相关条目

- [李群与李代数的对应定理](./李群与李代数的对应定理.md)：BCH 公式是该对应定理的关键技术步骤。
- [Ado 定理](./Ado定理.md)：先把李代数嵌入矩阵代数，BCH 的收敛性论证便归结为矩阵情形。
- [Weyl 特征标公式](./Weyl特征标公式.md)：同为李理论中把群层信息转化为代数层计算的典范公式。
- [BCH 公式](../第39级-李群与李代数/BCH公式.md)：与本条目为同一定理，另收录于第39级-李群与李代数，可交叉参考。
- [指数映射](../第39级-李群与李代数/指数映射.md)：本公式的描述对象，其局部可逆性是 $Z(t)$ 存在的前提。
- [李群与李代数的对应](../第39级-李群与李代数/李群与李代数的对应.md)：BCH 公式在该条目的证明中被引用。
