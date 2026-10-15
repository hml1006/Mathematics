# Hurwitz 定理

> **一句话大白话**：一族都不取零值的全纯函数，若内闭一致收敛，则极限函数或者恒等于零，或者也不取零值——"没有零点"这条性质在一致极限下不会凭空生出零点。
>
> **小例子**：$f_n(z)=e^{z/n}$ 在 $\mathbb C$ 上处处非零，内闭一致收敛到 $f\equiv1$，也处处非零；而 $f_n(z)=z+\frac1n$ 的极限是 $f(z)=z$，在 $0$ 处出现零点——此时 $f_n$ 在 $\Omega=\mathbb C$ 上并非"处处非零"（它们在 $-1/n$ 处为零），所以并不违反定理。

## 介绍

辐角原理告诉我们：全纯函数的零点个数可以由积分 $\frac{1}{2\pi i}\oint_\gamma\frac{f'}{f}dz$ 算出。Hurwitz 定理正是把它与"内闭一致收敛"结合起来：既然 $f_n\to f$ 时 $f_n'\to f'$（Weierstrass 一致收敛定理）且 $\frac{f_n'}{f_n}\to\frac{f'}{f}$（在 $f\ne0$ 的圆周上一致），那么零点个数的积分表达式也就收敛，于是 $f$ 的零点个数是 $f_n$ 零点个数的极限。

由此立刻得到：若每个 $f_n$ 都无零点，则极限函数在每个小圆盘内的零点个数为 $0$，即 $f$ 在 $\Omega$ 上无零点——除非 $f$ 恒等于零（这时"零点计数"失效，因为 $f'/f$ 无意义）。这条看似简单的结论是正规族理论中"单叶性在极限下保持"的关键，也是 Picard 定理与单值化理论中的标准工具。

它的另一常用形式是**零点计数形式**：若 $f$ 在某点有 $m$ 阶零点，则对充分大的 $n$，$f_n$ 在该点的小邻域内恰有 $m$ 个零点（计重数）。这是"零点是局部稳定的"这一直觉的严格化。

## 分析

**前置依赖**：全纯函数与 Cauchy 积分公式、辐角原理（$\frac{1}{2\pi i}\oint_\gamma\frac{f'}{f}dz$ 等于 $\gamma$ 内部零点个数）、Weierstrass 一致收敛定理（内闭一致收敛极限全纯、导数内闭一致收敛）、全纯函数零点的孤立性与恒等定理、一致收敛下积分与极限的交换。

**定理内容（Hurwitz）**：设 $\Omega\subseteq\mathbb C$ 是区域，$f_n:\Omega\to\mathbb C$ 全纯，且 $f_n\to f$ 在 $\Omega$ 的每个紧子集上一致（内闭一致收敛）。若每个 $f_n$ 在 $\Omega$ 上都没有零点，则

$$\text{或者}\ f\equiv0\ \text{于}\ \Omega,\qquad\text{或者}\ f\ \text{在}\ \Omega\ \text{上没有零点}.$$

**定理内容（零点计数形式）**：设 $f_n\to f$ 内闭一致，$f\not\equiv0$。设 $z_0\in\Omega$ 是 $f$ 的 $m\ge0$ 阶零点。则存在 $r>0$ 使得对充分大的 $n$，$f_n$ 在 $B(z_0,r)$ 内恰有 $m$ 个零点（计重数），且这些零点随 $n\to\infty$ 趋于 $z_0$。

**定理内容（单叶性极限）**：设 $\Omega$ 是区域，$f_n$ 在 $\Omega$ 上单叶（injective）且全纯，$f_n\to f$ 内闭一致。则 $f$ 或者是常数，或者也是单叶的。

**证明策略**：设 $f\not\equiv0$ 且在某点 $z_0$ 为零。取 $z_0$ 的小圆周 $\gamma$，使 $f$ 在 $\gamma$ 上不为零（零点孤立）。在 $\gamma$ 上，$f_n\to f$ 一致且 $f_n'\to f'$ 一致，且 $|f_n|$ 一致地离开 $0$，故 $\frac{f_n'}{f_n}\to\frac{f'}{f}$ 一致。对辐角原理取极限：$f_n$ 在 $\gamma$ 内的零点数为 $0$，故 $f$ 在 $\gamma$ 内的零点数也为 $0$，与 $f(z_0)=0$ 矛盾。单叶性用"两点的差函数"化归到零点的情形。

## 思考过程

**为什么需要"在圆周上一致地离开零"？** 因为要交换极限与积分的是 $\frac{f_n'}{f_n}$，它含有除法。仅知 $f_n\to f$ 一致还不够，必须知道 $f$ 在圆周上有正的下界 $m>0$，这样当 $n$ 大时 $|f_n|\ge m/2>0$，比值才有意义且一致收敛。而"$f$ 在圆周上不为零"是可以保证的：若 $f\not\equiv0$，其零点集在 $\Omega$ 内没有聚点，故以 $z_0$ 为心取足够小的圆周可以避开全部零点。

**为什么"或者 $f\equiv0$"这一分支不可去掉？** 因为示性函数式的性质"无零点"不能通过 $f\equiv0$ 检验（$0$ 处处为零）。例子：$f_n(z)=z/n$ 在每个紧集上一致趋于 $0$，但每个 $f_n$ 都有零点（在 $0$ 处）；$f\equiv0$ 确实取零值。至于 $f_n$ 在 $\Omega$ 上无零点却极限恒为 $0$ 的例子，如 $f_n(z)=e^{-nz}$ 在右半平面（收敛到 $0$ 但不内闭一致……）；更标准的例子是在单个点附近：$f_n(z)=e^{-n}$ 是常数，收敛到 $0$，处处非零——这说明 $f\equiv0$ 分支确实可能发生。所以定理的表述必须是"二择一"。

**单叶性怎么化归？** 单叶意味着"若 $a\ne b$ 则 $f(a)\ne f(b)$"。固定 $a\ne b$，令 $g_n(z)=f_n(z)-f_n(a)$：$g_n$ 在 $b$ 附近（取一个不含 $a$ 的小圆盘 $D$）没有零点，因为 $f_n$ 单叶且 $b\ne a$。于是可以对该圆盘用 Hurwitz，得到 $g(z)=f(z)-f(a)$ 在 $D$ 上恒为零或恒不为零。若 $f(b)=f(a)$，则 $g(b)=0$，故必然 $g\equiv0$ 于 $D$，再由恒等定理（$\Omega$ 连通）$g\equiv0$ 于 $\Omega$，即 $f\equiv f(a)$ 是常数。反之若 $f$ 不是常数，则对一切 $a\ne b$ 都有 $f(a)\ne f(b)$：$f$ 单叶。

## 证明过程

**步骤 1：圆周上的准备。**

设 $f\not\equiv0$，反设存在 $z_0\in\Omega$ 使 $f(z_0)=0$。因 $\Omega$ 开，取 $r_0>0$ 使 $\overline{B(z_0,r_0)}\subseteq\Omega$。因 $f\not\equiv0$ 且全纯，其零点集在 $\Omega$ 内无聚点，故存在 $0<r<r_0$ 使 $f$ 在圆周

$$\gamma=\{z:|z-z_0|=r\}$$

上处处非零。又 $\gamma$ 紧、$|f|$ 连续，故

$$m:=\min_{z\in\gamma}|f(z)|>0 .$$

**步骤 2：$\frac{f_n'}{f_n}$ 在圆周上一致收敛到 $\frac{f'}{f}$。**

由假设 $f_n\to f$ 在紧集 $\overline{B(z_0,r)}$ 上一致，故存在 $N$ 使 $n\ge N$ 时 $\|f_n-f\|_\gamma<m/2$。于是对 $z\in\gamma$，

$$|f_n(z)|\ge|f(z)|-|f_n(z)-f(z)|\ge m-\frac m2=\frac m2>0 ,$$

即 $f_n$ 在 $\gamma$ 上也没有零点，比值 $\frac{f_n'}{f_n}$ 在 $\gamma$ 上有定义。

另一方面，由 Weierstrass 一致收敛定理，$f_n'\to f'$ 在紧集 $\overline{B(z_0,r)}$ 上一致。于是

$$\left|\frac{f_n'}{f_n}-\frac{f'}{f}\right|=\frac{|f_n'f-f'f_n|}{|f_n|\,|f|}\le\frac{|f_n'-f'|\,|f|+|f'|\,|f_n-f|}{(m/2)m}\le\frac{2}{m^2}\Big(\|f_n'-f'\|_\gamma\,\|f\|_\gamma+\|f'\|_\gamma\|f_n-f\|_\gamma\Big),$$

右端与 $z\in\gamma$ 无关且趋于 $0$。故 $\frac{f_n'}{f_n}\to\frac{f'}{f}$ 在 $\gamma$ 上一致。

**步骤 3：对辐角原理取极限。**

$f_n$ 在 $\overline{B(z_0,r)}$ 上全纯且在 $\gamma$ 上非零，故由辐角原理，$f_n$ 在 $B(z_0,r)$ 内的零点个数（计重数）为

$$N_n=\frac{1}{2\pi i}\oint_\gamma\frac{f_n'(\zeta)}{f_n(\zeta)}\,d\zeta .$$

由假设每个 $f_n$ 在 $\Omega$ 上没有零点，故 $N_n=0$。由步骤 2，被积函数在 $\gamma$（长度 $2\pi r$）上一致收敛，故可在积分号下取极限：

$$\frac{1}{2\pi i}\oint_\gamma\frac{f'(\zeta)}{f(\zeta)}\,d\zeta=\lim_{n\to\infty}N_n=0 .$$

再由辐角原理（$f$ 在 $\gamma$ 上非零），左端恰为 $f$ 在 $B(z_0,r)$ 内的零点个数。故 $f$ 在 $B(z_0,r)$ 内无零点。

**步骤 4：导出矛盾。**

但 $z_0\in B(z_0,r)$ 且 $f(z_0)=0$，矛盾。因此当 $f\not\equiv0$ 时 $f$ 在 $\Omega$ 上处处非零，Hurwitz 定理得证。$\square$

**步骤 5：零点计数形式。**

设 $f\not\equiv0$，$z_0$ 是 $f$ 的 $m$ 阶零点。由零点的孤立性，可取 $r>0$ 使 $\overline{B(z_0,r)}\subseteq\Omega$ 且 $f$ 在 $\overline{B(z_0,r)}\setminus\{z_0\}$ 上非零。由步骤 2 的同一论证，$\frac{f_n'}{f_n}\to\frac{f'}{f}$ 在圆周 $\gamma=\{|z-z_0|=r\}$ 上一致（只要 $|f|$ 在 $\gamma$ 上有正的下界），故

$$N_n=\frac{1}{2\pi i}\oint_\gamma\frac{f_n'}{f_n}\,d\zeta\xrightarrow[n\to\infty]{}\frac{1}{2\pi i}\oint_\gamma\frac{f'}{f}\,d\zeta=m .$$

因 $N_n$ 是整数序列且收敛到整数 $m$，故存在 $N$ 使 $n\ge N$ 时 $N_n=m$：$f_n$ 在 $B(z_0,r)$ 内恰有 $m$ 个零点（计重数）。又若某个子列的零点 $w_n$ 不趋于 $z_0$，则存在子列 $w_{n_k}\to w\ne z_0$，由 $f_{n_k}(w_{n_k})=0$ 与一致收敛得 $f(w)=0$，与 $f$ 在 $\overline{B(z_0,r)}\setminus\{z_0\}$ 上非零矛盾。故这些零点随 $n\to\infty$ 趋于 $z_0$。$\square$

**步骤 6：单叶性的极限保持。**

设 $\Omega$ 是区域，$f_n:\Omega\to\mathbb C$ 单叶且内闭一致收敛到 $f$。反设 $f$ 不是常数但存在 $a\ne b$ 使 $f(a)=f(b)$。

因 $a\ne b$，取 $r>0$ 使

$$D:=B(b,r)\subseteq\Omega,\qquad a\notin\overline D .$$

对每个 $n$ 定义 $g_n(z):=f_n(z)-f_n(a)$（$z\in\Omega$）。因 $f_n$ 单叶且 $a\notin D$，对一切 $z\in D$ 有 $z\ne a$，故 $f_n(z)\ne f_n(a)$，即

$$g_n\ \text{在}\ D\ \text{内没有零点}.$$

又 $g_n\to g$ 内闭一致，其中 $g(z)=f(z)-f(a)$。由 Hurwitz 定理（应用于区域 $D$）：或者 $g\equiv0$ 于 $D$，或者 $g$ 在 $D$ 上无零点。

但 $g(b)=f(b)-f(a)=0$，故必 $g\equiv0$ 于 $D$，即 $f\equiv f(a)$ 于 $D$。由恒等定理（$f-f(a)$ 全纯、$\Omega$ 连通、零集 $D$ 有聚点），$f\equiv f(a)$ 于 $\Omega$，即 $f$ 是常数，与反设矛盾。

因此若 $f$ 不是常数，则对一切 $a\ne b$ 有 $f(a)\ne f(b)$，即 $f$ 单叶。$\square$

**推论（单叶族的紧性应用）**：设 $\mathcal{F}$ 是单位圆盘上的一族单叶函数，若局部一致有界，则它在紧开拓扑下的极限函数或者为常数、或者单叶（用 Montel 定理先抽收敛子列，再用步骤 6）。这正是 Koebe 型极值问题与单值化定理中所需要的"极限不失去单叶性"的保证。

## 课堂问答

**老师**：一族"处处无零点"的全纯函数，一致极限为什么不会凭空生出零点？

**学生**：结论：设 $f_n\to f$ 内闭一致且每个 $f_n$ 在 $\Omega$ 上无零点，则或者 $f\equiv0$，或者 $f$ 在 $\Omega$ 上无零点。用辐角原理：$f_n$ 在圆周 $\gamma$ 内的零点数 $N_n=\frac{1}{2\pi i}\oint_\gamma\frac{f_n'}{f_n}dz=0$，而 $\frac{f_n'}{f_n}\to\frac{f'}{f}$ 在 $\gamma$ 上一致，取极限得 $\oint_\gamma\frac{f'}{f}dz=0$，即 $f$ 在 $\gamma$ 内无零点。

**老师（追问）**：为什么必须知道 $f$ 在圆周上"一致地离开零"？

**学生**：因为被积函数 $\frac{f_n'}{f_n}$ 含除法，只有一致收敛还不够。由 $f\not\equiv0$ 时零点的孤立性，可取圆周 $\gamma$ 使 $f\ne0$ 在其上，令 $m=\min_\gamma|f|>0$，则 $n$ 大时 $|f_n|\ge m/2>0$，比值才有意义并且一致收敛。

**老师（拓展）**：单叶性怎么化归到零点情形？

**学生**：固定 $a\ne b$，取不含 $a$ 的小圆盘 $D\ni b$，令 $g_n=f_n-f_n(a)$，则 $g_n$ 在 $D$ 上无零点。Hurwitz 给出 $g=f-f(a)$ 在 $D$ 上恒零或恒非零；若 $f(b)=f(a)$ 则 $g\equiv0$，由恒等定理 $f$ 为常数。故非常数极限仍单叶，这正是"单叶性在极限下保持"。

## 相关条目

- [Weierstrass一致收敛定理](./Weierstrass一致收敛定理.md)：提供 $f_n'\to f'$ 的内闭一致收敛，是步骤 2 的前提。
- [Montel定理](./Montel定理.md)：与 Hurwitz 定理配合，从单叶族中抽出极限并保持单叶性。
- [单值化定理](./单值化定理.md)：其证明中"极限映射的单叶性/常数性"论证正是 Hurwitz 定理的应用。
