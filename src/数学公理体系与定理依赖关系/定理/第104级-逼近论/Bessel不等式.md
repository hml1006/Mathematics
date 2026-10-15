# Bessel不等式

> **一句话大白话**：把向量在一组标准正交方向上做投影，所有投影长度的平方加起来，永远不超过原来向量长度的平方，多出来的长度就是还没被这些方向覆盖的部分。

> **小例子**：在 $\mathbb{R}^{3}$ 中取标准正交基 $e_1,e_2$ 与向量 $x=(3,4,12)$。则 $\langle x,e_1\rangle^{2}+\langle x,e_2\rangle^{2}=9+16=25\le\sqrt{9+16+144}^{2}=169$，差额 $144$ 正是第三个方向上的分量平方。

## 一、定理介绍

> **前置依赖**：内积空间、标准正交系、勾股定理、Cauchy-Schwarz不等式、正交投影定理。

Bessel 不等式得名于德国天文学家兼数学家 Friedrich Wilhelm Bessel（1784–1846）。1828 年前后，Bessel 在研究行星轨道摄动与三角级数时发现：对周期函数 $f$ 的 Fourier 系数，其平方和总是不超过函数本身平方的积分均值，即 $\frac{a_0^{2}}{2}+\sum_{n\ge1}(a_n^{2}+b_n^{2})\le\frac{1}{\pi}\int_{-\pi}^{\pi}f^{2}$。这个观察原本是 Fourier 级数收敛性讨论中的技术性工具（它保证了系数趋于零，因而是 Riemann-Lebesgue 引理的前身），后来被推广到一般内积空间中的标准正交系，成为正交展开理论的第一块基石。

它的意义在于给出了正交展开的"能量守恒不等式"：若正交系不完整（不是基），则向量长度平方严格大于投影系数平方之和，差额由正交补中的分量贡献；若正交系是完备的，则不等式取等号，这就是 Parseval 恒等式。因此 Bessel 不等式刻画了"用有限或可数多个正交方向去逼近一个向量"时究竟丢失了多少信息，是逼近论中判定最佳逼近误差、讨论正交多项式展开收敛性的出发点。在傅里叶分析与小波分析中，它也是框架（frame）理论与采样定理的基本构件。

## 二、原理思路

1. 取标准正交系 $\{e_1,e_2,\dots\}$ 与向量 $x$，构造第 $N$ 个正交投影（部分和）$S_N=\sum_{n=1}^{N}\langle x,e_n\rangle e_n$，它落在这些方向张成的子空间中。

2. 利用正交性验证 $x-S_N$ 与每个 $e_m$（$m\le N$）正交，从而 $x$ 被分解为两个正交分量 $S_N$ 与 $x-S_N$。由勾股定理，$\|x\|^{2}=\|S_N\|^{2}+\|x-S_N\|^{2}$。

3. 由 $\|S_N\|^{2}=\sum_{n=1}^{N}|\langle x,e_n\rangle|^{2}$ 及 $\|x-S_N\|^{2}\ge0$ 得到部分和不等式；再令 $N\to\infty$ 用单调收敛得到完整级数的 Bessel 不等式。同时，$\|x-S_N\|$ 的最小性说明 $S_N$ 是子空间中的最佳逼近。

## 三、定理的严格表述

设 $\mathcal{H}$ 为内积空间，$\{e_n\}_{n\ge1}\subseteq\mathcal{H}$ 为标准正交系，即

$$
\langle e_m,e_n\rangle=\delta_{mn}=\begin{cases}1,&m=n,\\0,&m\ne n.\end{cases}
$$

则对任意 $x\in\mathcal{H}$，级数 $\sum_{n\ge1}\left|\langle x,e_n\rangle\right|^{2}$ 收敛，且

$$
\sum_{n=1}^{\infty}\left|\langle x,e_n\rangle\right|^{2}\le\|x\|^{2}.
$$

进一步，若 $\mathcal{H}$ 完备（Hilbert 空间）且 $\{e_n\}$ 为完备正交系，则等号成立，即 Parseval 恒等式

$$
\sum_{n=1}^{\infty}\left|\langle x,e_n\rangle\right|^{2}=\|x\|^{2}.
$$

此外，对每个 $N$，部分和 $S_N=\sum_{n=1}^{N}\langle x,e_n\rangle e_n$ 在 $\mathrm{span}\{e_1,\dots,e_N\}$ 中实现最佳逼近，且逼近误差满足

$$
\left\|x-S_N\right\|^{2}=\|x\|^{2}-\sum_{n=1}^{N}\left|\langle x,e_n\rangle\right|^{2}.
$$

## 四、证明过程

**步骤 1（部分和的范数）。** 固定 $N$，令 $S_N=\sum_{n=1}^{N}c_n e_n$，其中 $c_n=\langle x,e_n\rangle$。由标准正交性，

$$
\|S_N\|^{2}=\left\langle\sum_{m=1}^{N}c_m e_m,\sum_{n=1}^{N}c_n e_n\right\rangle=\sum_{m,n=1}^{N}c_m\overline{c_n}\,\delta_{mn}=\sum_{n=1}^{N}|c_n|^{2}=\sum_{n=1}^{N}\left|\langle x,e_n\rangle\right|^{2}.
$$

**步骤 2（余项与子空间正交）。** 对任意 $1\le m\le N$，

$$
\left\langle x-S_N,\,e_m\right\rangle=\langle x,e_m\rangle-\sum_{n=1}^{N}c_n\langle e_n,e_m\rangle=c_m-c_m=0 .
$$

故 $x-S_N$ 与 $e_1,\dots,e_N$ 张成的子空间正交。

**步骤 3（勾股分解）。** 因 $S_N$ 是 $e_1,\dots,e_N$ 的线性组合，$\langle S_N,\,x-S_N\rangle=0$，于是

$$
\|x\|^{2}=\|S_N+(x-S_N)\|^{2}=\|S_N\|^{2}+\|x-S_N\|^{2}.
$$

结合步骤 1 得

$$
\|x-S_N\|^{2}=\|x\|^{2}-\sum_{n=1}^{N}\left|\langle x,e_n\rangle\right|^{2}.
$$

**步骤 4（获得部分和不等式）。** 由 $\|x-S_N\|^{2}\ge0$ 立即得到

$$
\sum_{n=1}^{N}\left|\langle x,e_n\rangle\right|^{2}\le\|x\|^{2}\qquad\text{对一切 }N .
$$

**步骤 5（令 $N\to\infty$）。** 上式右端与 $N$ 无关，故非负项级数的部分和有上界 $\|x\|^{2}$，从而收敛，令 $N\to\infty$ 即得

$$
\sum_{n=1}^{\infty}\left|\langle x,e_n\rangle\right|^{2}\le\|x\|^{2}.
$$

**步骤 6（最佳逼近性与等号条件）。** 设 $y=\sum_{n=1}^{N}d_n e_n$ 为子空间中任一元素，则 $\langle x-y,e_m\rangle=\langle x,e_m\rangle-d_m$，故

$$
\|x-y\|^{2}=\|x\|^{2}-\sum_{n=1}^{N}\left(2\,\mathrm{Re}\,\overline{d_n}c_n-|d_n|^{2}\right)=\|x-S_N\|^{2}+\sum_{n=1}^{N}|c_n-d_n|^{2},
$$

右端在 $d_n=c_n$ 时最小，故 $S_N$ 为最佳逼近。当 $\{e_n\}$ 完备时 $\|x-S_N\|\to0$，于是步骤 3 给出等号，即 Parseval 恒等式。$\square$

## 五、应用与意义

- 正交展开：给出 Fourier 级数、Legendre/Chebyshev 展开、小波展开中系数平方和的收敛性与上界，是 Parseval 恒等式与 Plancherel 定理的前身。
- 最佳逼近：把最小二乘逼近的误差表示为"总能量减已解释能量"，是投影法与正规方程的理论依据。
- 数值分析：在有限元、谱方法中用于估计截断误差，指导基函数选取与阶数控制。
- 框架与小波：在具有冗余性的框架中，Bessel 不等式恰是"上框架界"的定义条件，保证重构算子的有界性。

## 课堂问答

**老师**：内积空间里，向量在一组标准正交系上的投影系数平方和，为什么不超过向量本身的范数平方？

**学生**：因为投影只提取了"部分信息"。取 $S_N=\sum_{n=1}^N\langle x,e_n\rangle e_n$，由正交性可验证 $\langle x-S_N,e_m\rangle=0$（$m\le N$），故 $S_N\perp(x-S_N)$。由勾股定理 $\|x\|^2=\|S_N\|^2+\|x-S_N\|^2=\sum_{n=1}^N|\langle x,e_n\rangle|^2+\|x-S_N\|^2\ge\sum_{n=1}^N|\langle x,e_n\rangle|^2$。对一切 $N$ 成立，令 $N\to\infty$ 即得 $\sum_{n=1}^\infty|\langle x,e_n\rangle|^2\le\|x\|^2$。

**老师（追问）**：等号什么时候成立？差额代表什么？

**学生**：当 $\{e_n\}$ 完备（是 Hilbert 空间的规范正交基）时 $\|x-S_N\|\to0$，不等式升级为 Parseval 恒等式 $\sum_n|\langle x,e_n\rangle|^2=\|x\|^2$。差额 $\|x-S_N\|^2=\|x\|^2-\sum_{n=1}^N|\langle x,e_n\rangle|^2$ 正是落在正交补里、这些方向尚未覆盖的能量。

**老师（拓展）**：它与最佳逼近、框架理论有什么关系？

**学生**：证明中已顺带说明 $S_N$ 是 $\operatorname{span}\{e_1,\dots,e_N\}$ 中的最佳逼近，误差恰为上述差额，这是最小二乘与投影法的能量解释。常见误区是把它与 Parseval 混用——Bessel 是单向不等式，只有完备时才取等号。在冗余的框架中，它正是"上框架界"的定义条件，也是采样定理与重构算子有界性的基础；其 Fourier 系数版本 $\frac{a_0^2}{2}+\sum_{n\ge1}(a_n^2+b_n^2)\le\frac{1}{\pi}\int_{-\pi}^{\pi}f^2$ 是 Riemann–Lebesgue 引理的前身。

## 相关条目

- [正交多项式的最佳逼近性质](./正交多项式的最佳逼近性质.md)：把本不等式用于正交多项式展开的误差分析。
- [最佳逼近的存在唯一性](./最佳逼近的存在唯一性.md)：本定理步骤 6 所讨论的最佳逼近问题的系统理论。
- [Weierstrass逼近定理](./Weierstrass逼近定理.md)：保证逼近误差可任意小的存在性结果。
- [Chebyshev逼近理论](../第67级-逼近论与样条理论/Chebyshev逼近理论.md)：一致范数下的最佳逼近，与内积范数形成对照。
- [正交多项式理论](../第67级-逼近论与样条理论/正交多项式理论.md)：标准正交系的构造与性质。
- [正交投影定理](../第31级-泛函分析/正交投影定理.md)：本证明所依赖的投影几何。
- [Plancherel定理](../第51级-调和分析/Plancherel定理.md)：正交展开等号成立的傅里叶分析版本。
