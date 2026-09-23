# Weierstrass 一致收敛定理

> **一句话大白话**：全纯函数列只要在紧集上一致收敛，极限仍是全纯函数，而且导数也自动跟着一致收敛到极限的导数。
>
> **小例子**：$\sum_{n\ge1}\frac{z^n}{n^2}$ 在 $\mathbb{D}$ 上内闭一致收敛，故其和函数全纯，且可以逐项求导得到 $\sum_{n\ge1}\frac{z^{n-1}}{n}$。

## 介绍

在实分析中，"一致收敛"只保证极限函数连续；可微性一般不能传递（例如 $|x|$ 可由光滑函数一致逼近）。复分析的情形则完全不同：全纯性在**内闭一致收敛**（即在每个紧子集上一致收敛）下是封闭的，而且这一封闭性是"到无穷阶"的——导数序列自动内闭一致收敛到极限的导数。

这条定理（常简称为 Weierstrass 定理，或 Weierstrass 收敛定理）使全纯函数空间在紧开拓扑下成为完备空间，是幂级数、Weierstrass 乘积、正规族理论（Montel 定理）、$\wp$ 函数与模形式等一切"无穷构造"的合法性根据。

## 分析

**前置依赖**：Cauchy 积分公式、Cauchy 估计、Morera 定理、一致收敛与积分/极限的交换、紧集上连续函数的一致收敛、区域的穷竭。

**定理内容**：设 $\Omega\subset\mathbb{C}$ 是区域，$f_n:\Omega\to\mathbb{C}$ 全纯，且 $f_n$ 在 $\Omega$ 的每个紧子集上一致收敛到 $f$（记作 $f_n\to f$ 内闭一致）。则

1. $f$ 在 $\Omega$ 上全纯；
2. 对每个 $k\ge1$，$f_n^{(k)}\to f^{(k)}$ 内闭一致；
3. （级数形式）若 $\sum_{n}f_n$ 内闭一致收敛，则其和函数全纯，且可逐项求导任意次。

**证明策略**：连续性由一致收敛保持；全纯性用 Morera 定理（沿三角形围道积分，一致收敛允许交换极限与积分）；导数的收敛用 Cauchy 积分公式把 $f_n'-f'$ 表示为 $f_n-f$ 沿圆周的积分，从而把导数差控制在函数差的一致范数之内。

## 思考过程

证 $f$ 全纯最方便的工具是 Morera 定理：它只需验证沿一切三角形围道的积分为零。每个 $f_n$ 全纯故 $\oint_{\partial T}f_n=0$，而一致收敛使得 $\oint_{\partial T}f_n\to\oint_{\partial T}f$（因为 $\left|\oint(f_n-f)\right|\le\|f_n-f\|_{\partial T}\cdot\text{周长}$），于是 $\oint_{\partial T}f=0$，由 Morera 得 $f$ 全纯。这条路线回避了"证明 $f$ 可导"这一较难的任务。

导数收敛的关键是"用积分表示导数"。取 $z$ 的一个小圆周，Cauchy 公式给出
$$f_n'(z)=\frac{1}{2\pi i}\oint_{|\zeta-z|=r}\frac{f_n(\zeta)}{(\zeta-z)^2}\,d\zeta,$$
于是
$$f_n'(z)-f'(z)=\frac{1}{2\pi i}\oint_{|\zeta-z|=r}\frac{f_n(\zeta)-f(\zeta)}{(\zeta-z)^2}\,d\zeta,$$
估值给出 $|f_n'(z)-f'(z)|\le\frac1r\sup_{|\zeta-z|=r}|f_n-f|$。若 $K$ 是紧集，取 $r>0$ 使 $K$ 的 $r$-邻域含于 $\Omega$，则上式对 $z\in K$ 一致成立，收敛性是内闭一致的。高阶导数同理，取 $k!$ 因子即可。

## 证明过程

**步骤 1：$f$ 连续。**

每个 $f_n$ 连续，且 $f_n\to f$ 内闭一致（特别地逐点收敛）。对 $z_0\in\Omega$ 与 $\epsilon>0$，取 $n$ 使 $\|f_n-f\|_{K}<\epsilon/3$（$K$ 是含 $z_0$ 的紧邻域），再由 $f_n$ 连续取 $\delta$ 使 $|z-z_0|<\delta\Rightarrow|f_n(z)-f_n(z_0)|<\epsilon/3$；于是
$$|f(z)-f(z_0)|\le|f-f_n|(z)+|f_n(z)-f_n(z_0)|+|f_n-f|(z_0)<\epsilon.$$
故 $f$ 连续。

**步骤 2：Morera 定理给出全纯性。**

设 $T\subset\Omega$ 是任一闭三角形（含其内部），$\partial T$ 为其边界。因 $\Omega$ 是区域，可先处理 $T\subset\Omega$（若 $T$ 的边界与 $\Omega$ 边界相交，则因 $T$ 紧，用穷竭或先取 $T$ 内的小三角形逼近，标准处理）。每个 $f_n$ 在 $\Omega$ 上全纯，由 Cauchy 定理
$$\oint_{\partial T}f_n(z)\,dz=0.$$
由 $f_n\to f$ 在紧集 $T$ 上一致收敛，
$$\Big|\oint_{\partial T}f\,dz-\oint_{\partial T}f_n\,dz\Big|\le\oint_{\partial T}|f-f_n|\,|dz|\le\|f-f_n\|_{T}\cdot L(\partial T)\xrightarrow{n\to\infty}0,$$
其中 $L(\partial T)$ 是周长。故 $\oint_{\partial T}f\,dz=0$。由于对一切三角形围道积分为零，且 $f$ 连续（步骤 1），Morera 定理给出 $f$ 在 $\Omega$ 上全纯。

**步骤 3：一阶导数内闭一致收敛。**

设 $K\subset\Omega$ 紧。因 $\Omega$ 开、$K$ 紧，$d(K,\mathbb{C}\setminus\Omega)=:\rho>0$。取 $r\in(0,\rho)$（例如 $r=\rho/2$），则对每个 $z\in K$，闭圆盘 $\overline{B(z,r)}\subset\Omega$，且
$$K_r:=\bigcup_{z\in K}\overline{B(z,r)}\subset\Omega\quad\text{是紧集。}$$

对 $z\in K$，由 Cauchy 积分公式应用于全纯函数 $f_n-f$（它在 $\Omega$ 上全纯）：
$$f_n'(z)-f'(z)=\frac{1}{2\pi i}\oint_{|\zeta-z|=r}\frac{f_n(\zeta)-f(\zeta)}{(\zeta-z)^2}\,d\zeta.$$
估值（$|\zeta-z|=r$，故 $|(\zeta-z)^2|=r^2$，周长 $2\pi r$）：
$$|f_n'(z)-f'(z)|\le\frac{1}{2\pi}\cdot\frac{\|f_n-f\|_{K_r}}{r^2}\cdot2\pi r=\frac{\|f_n-f\|_{K_r}}{r}.$$
右端与 $z\in K$ 无关，故
$$\|f_n'-f'\|_K\le\frac{\|f_n-f\|_{K_r}}{r}\xrightarrow{n\to\infty}0.$$
即 $f_n'\to f'$ 内闭一致。

**步骤 4：高阶导数内闭一致收敛。**

对 $k\ge1$，同样用 $f^{(k)}$ 的 Cauchy 积分公式：
$$f^{(k)}(z)=\frac{k!}{2\pi i}\oint_{|\zeta-z|=r}\frac{f(\zeta)}{(\zeta-z)^{k+1}}\,d\zeta,$$
故
$$|f_n^{(k)}(z)-f^{(k)}(z)|\le\frac{k!}{r^k}\|f_n-f\|_{K_r}\qquad(z\in K),$$
于是 $\|f_n^{(k)}-f^{(k)}\|_K\le\frac{k!}{r^k}\|f_n-f\|_{K_r}\to0$。对每个 $k$ 与每个紧集 $K$ 成立，即结论 2。

**步骤 5：级数形式（结论 3）。**

设 $\sum_{n}f_n$ 内闭一致收敛，记部分和 $S_N=\sum_{n\le N}f_n$，则 $S_N\to f:=\sum_nf_n$ 内闭一致，$S_N$ 全纯。由步骤 2、3，$f$ 全纯且 $S_N^{(k)}\to f^{(k)}$ 内闭一致，即
$$f^{(k)}=\sum_{n}f_n^{(k)}\qquad\text{（内闭一致收敛）}$$
对每个 $k\ge0$ 成立，这就是"逐项求导"的合法性。Weierstrass M-判别法是验证内闭一致收敛的常用手段。

**步骤 6：推论。**

（i）**空间的完备性**：以紧开拓扑（由半范数 $\|f\|_K$，$K$ 紧）看，全纯函数空间 $\mathcal{O}(\Omega)$ 是 $C(\Omega)$ 的闭子空间，故完备。这是 Montel 定理中"正规族的极限仍在族内"的依据。

（ii）**Hurwitz 定理**：若 $f_n$ 全纯且内闭一致收敛 $f_n\to f$，$f_n$ 在 $\Omega$ 上都没有零点，则或者 $f\equiv0$，或者 $f$ 在 $\Omega$ 上没有零点。证明用辐角原理：对不穿过零点的闭曲线 $\gamma$，$\oint_\gamma\frac{f_n'}{f_n}dz=0$（$f_n$ 无零点），由步骤 3 让 $n\to\infty$ 得 $\oint_\gamma\frac{f'}{f}dz=0$，从而 $f$ 在 $\gamma$ 内部的零点数与极点数为零。Hurwitz 定理是"单叶性的极限保持"（正规族中极值函数单射）的关键。

（iii）**唯一性定理的极限形式**：若 $f_n$ 全纯、内闭一致收敛到 $f$，且在含聚点的集合 $E\subset\Omega$ 上 $f_n=0$，则 $f\equiv0$。这说明全纯函数空间中的收敛比连续函数空间中的收敛"刚硬得多"。

## 相关条目

- [Montel定理](./Montel定理.md)：正规族的定义与定理的证明都依赖"内闭一致收敛极限仍全纯"。
- [Arzelà-Ascoli定理](./Arzelà-Ascoli定理.md)：提供收敛子列的存在性，与本定理的"极限保持全纯"互补。
- [Weierstrass因子分解定理](./Weierstrass因子分解定理.md)：无穷乘积的收敛性与可微性由本定理保证。
