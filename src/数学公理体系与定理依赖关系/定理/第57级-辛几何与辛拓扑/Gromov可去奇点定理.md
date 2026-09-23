# Gromov可去奇点定理

> **一句话大白话**：一条"能量有限"的伪全纯曲线，如果只在一点上没有定义，那么这一点其实不是真奇点——把它补上之后曲线依然光滑，并未被"撕开"。
>
> **小例子**：在去心圆盘上全纯且满足 $\int_{D\setminus\{0\}}|f'(z)|^2\,dA<\infty$ 的函数必可解析延拓到 $0$（Laurent 展开中的负次幂项全部消失）。Gromov 可去奇点定理就是这一经典事实在伪全纯曲线上的推广，它是 Gromov 紧性定理与 Floer 同调"气泡分析"的分析基础。

## 一、定理介绍

> **前置依赖**：伪全纯曲线与 Cauchy–Riemann 方程 $\bar\partial_Ju=0$、辛形式与相容近复结构下的能量恒等式 $E(u)=\int u^*\omega=\frac12\int|du|^2$、$J$-全纯曲线的均值不等式（Gromov 单调性引理的局部形式）、全纯函数的 Laurent 展开与经典可去奇点定理、一致椭圆系统的 Weyl 引理（或 Calderón–Zygmund 估计）。

Gromov 可去奇点定理（Gromov Removable Singularity Theorem）是 Mikhail Gromov 在 1985 年关于伪全纯曲线的奠基性工作中证明的基本分析定理。它断言：$J$-全纯曲线 $u:D\setminus\{0\}\to M$ 只要能量有限，就不存在"真正的"奇点；$u$ 总可以光滑地延拓为整条圆盘 $D$ 上的 $J$-全纯曲线。

这一定理的意义在于它把"奇点"与"能量集中"精确地联系起来：曲线之所以可能在某点失去光滑性，唯一的原因是能量在该点附近不收敛（例如 $z\mapsto 1/z$ 型的行为使 $\int|du|^2=\infty$）。因此只要能量有限，模空间中的曲线就不会在定义域内部"炸开"；而 Gromov 紧性定理中出现的"气泡"（bubble）恰恰是能量无限或定义域被去掉一点时才会发生的现象。这个定理是 Floer 同调、Gromov–Witten 不变量与伪全纯曲线模空间理论的基石之一，也是调和映射中 Sacks–Uhlenbeck 可去奇点定理的伪全纯版本。

## 二、原理思路

定理的整个证明由三个互相配合的分析事实构成。

1. **能量的局部衰减**：有限能量 $E(u)<\infty$ 意味着能量在每个二进环域上的贡献构成一个可和的数列，故在半径趋于零的圆盘上能量必然趋于零：$E(u|_{D_r})\to0$（$r\downarrow0$）。

2. **均值不等式控制振荡**：$J$-全纯曲线的均值不等式给出 $\sup_{D_{r/2}}|du|^2\le C r^{-2}E(u|_{D_r})$。对它作重标定（把半径为 $r$ 的圆盘放大成单位圆盘）后可见：半径 $r$ 的圆盘上 $|du|\cdot r\le C\,E(u|_{D_r})^{1/2}\to0$，即曲线在小圆盘上的像的直径趋于零。于是小圆盘的像收缩到唯一一点，极限 $\lim_{z\to0}u(z)$ 存在。

3. **坐标化后用椭圆正则性去奇点**：在极限点附近取坐标卡，把 $J$ 拉直成标准复结构，方程化为一个带有连续系数的椭圆系统 $\partial_{\bar z}f+q(f)\partial_z f=0$；由于 $f$ 连续且属于 $W^{1,2}$，Weyl 引理与自举（bootstrapping）给出 $f$ 光滑。

第 1、2 步负责"拓扑上的可去"，第 3 步负责"光滑性的可去"，二者合起来即得结论。

## 三、定理的严格表述

设 $(M,J)$ 是近复流形（典型情形为辛流形 $(M,\omega)$ 配以与 $\omega$ 相容的近复结构 $J$），并固定 $M$ 上一个与 $J$ 相容的 Riemann 度量。记 $D=\{z\in\mathbb C:|z|<1\}$ 为单位圆盘。

**定义（有限能量）**：称 $J$-全纯曲线 $u:D\setminus\{0\}\to M$ 具有有限能量，是指
$$E(u)=\int_{D\setminus\{0\}}u^*\omega=\frac12\int_{D\setminus\{0\}}|du|^2\,dA<\infty,$$
其中 $dA$ 为 Euclid 面积元。（对相容的 $J$，两个积分恒相等。）

**定理（Gromov 可去奇点定理）**：设 $u:D\setminus\{0\}\to M$ 是 $J$-全纯曲线且 $E(u)<\infty$。则：

1. 极限 $p=\lim_{z\to0}u(z)$ 存在，从而 $u$ 唯一地连续延拓为 $\bar u:D\to M$，$\bar u(0)=p$；
2. 延拓后的 $\bar u$ 是 $J$-全纯的；特别地，若 $J$ 光滑，则 $\bar u$ 光滑（$C^\infty$）。

**推论（能量集中即奇点）**：若 $u:D\setminus\{0\}\to M$ 是 $J$-全纯曲线且极限 $\lim_{z\to0}u(z)$ 不存在，则 $E(u)=\infty$。

**注**：定理对定义域被去掉任何有限个内点的情形逐点施用即可；对穿孔 Riemann 曲面（柱端）的相应陈述是 Floer 同调中有界能量曲线的"端部收敛"性质。

## 四、证明过程

**步骤 1：全纯情形的模型证明（经典可去奇点定理）。**

先处理 $M=\mathbb C$、$J=J_0$（标准复结构）的情形。设 $f$ 在 $D\setminus\{0\}$ 上全纯，有 Laurent 展开
$$f(z)=\sum_{k\in\mathbb Z}a_kz^k,\qquad 0<|z|<1.$$
其导数 $f'(z)=\sum_{k\ne0}k\,a_kz^{k-1}$。对 $0<r<1$ 计算 Dirichlet 能量：
$$\int_{r<|z|<1}|f'(z)|^2\,dA=\sum_{k\ne0}|k|^2|a_k|^2\int_r^1\!\!\int_0^{2\pi}s^{2k-1}\,d\theta\,ds=\sum_{k\ne0}2\pi|k|^2|a_k|^2\int_r^1 s^{2k-1}\,ds.$$
对 $k\le-1$，记 $n=-k\ge1$，则 $2k-1=-2n-1$，从而
$$\int_r^1 s^{-2n-1}\,ds=\frac{1}{2n}\left(r^{-2n}-1\right)\xrightarrow[r\downarrow0]{}\infty.$$
因此若某个 $k<0$ 有 $a_k\ne0$，则当 $r\downarrow0$ 时 $\int_{r<|z|<1}|f'|^2\,dA$ 将趋于 $+\infty$，与能量有限矛盾。故 $a_k=0$ 对一切 $k<0$ 成立，$f(z)=\sum_{k\ge0}a_kz^k$ 在 $z=0$ 处解析，可去奇点得证。$\square$（模型情形）

**步骤 2：能量在收缩圆盘上趋于零。**

对 $k\ge0$ 记二进环域能量
$$e_k=\int_{2^{-k-1}<|z|<2^{-k}}|du|^2\,dA\ \ge0.$$
这些环域互不相交且并集为 $D\setminus\{0\}$，故 $\sum_{k\ge0}e_k=2E(u)<\infty$。可和的正项级数通项趋于零，因此
$$e_k\longrightarrow0,\qquad\text{且}\qquad E\!\left(u|_{D_{2r_k}}\right)=\frac12\sum_{j\ge k}e_j\longrightarrow0\quad(r_k=2^{-k}).$$

**步骤 3：均值不等式与像的直径估计。**

引用 $J$-全纯曲线的均值不等式：存在常数 $\hbar>0$ 与 $C$（只依赖 $(M,J)$ 与所取相容度量），使得对任意 $J$-全纯的 $v:D_\rho\to M$，只要 $E(v)\le\hbar$，就有
$$\sup_{z\in D_{\rho/2}}|dv(z)|^2\le \frac{C}{\rho^2}\,E(v).$$
（这是 Gromov 单调性引理在同调平凡圆盘上的局部形式。）

取 $r_k=2^{-k}$，定义重标定曲线
$$v_k(z)=u(2r_kz),\qquad z\in D_1 .$$
则 $E(v_k)=E\!\left(u|_{D_{2r_k}}\right)\to0$，故当 $k$ 充分大时 $E(v_k)\le\hbar$。对 $v_k$ 施用均值不等式（取 $\rho=1$），得
$$\sup_{z\in D_{1/2}}|dv_k(z)|^2\le C\,E(v_k).$$
由 $dv_k(z)=2r_k\,du(2r_kz)$，上式等价于
$$(2r_k)^2\sup_{w\in D_{r_k}}|du(w)|^2\le C\,E(v_k),\qquad\text{即}\qquad \sup_{w\in D_{r_k}}|du(w)|\le\frac{C^{1/2}E(v_k)^{1/2}}{2r_k}.$$
于是像 $u(D_{r_k/2})$ 的直径满足
$$\mathrm{diam}\,u\!\left(D_{r_k/2}\right)\le \sup_{w\in D_{r_k/2}}|du(w)|\cdot\frac{r_k}{2}\le \frac{C^{1/2}}{4}\,E(v_k)^{1/2}\longrightarrow0 .$$

**步骤 4：极限存在，得到连续延拓。**

集合 $\overline{u(D_{r_k/2})}$ 是 $M$ 中紧集，且随 $k$ 增大而递降（因 $r_k$ 递减），其直径由步骤 3 趋于零，故交集恰为单点：
$$\bigcap_{k\ge0}\overline{u\!\left(D_{r_k/2}\right)}=\{p\}.$$
对任意 $z\pm0$ 取 $k$ 使 $|z|<r_k/2$，则 $u(z)\in u(D_{r_k/2})$，于是
$$d\bigl(u(z),p\bigr)\le \mathrm{diam}\,u\!\left(D_{r_k/2}\right)\longrightarrow0\qquad(z\to0).$$
故 $\lim_{z\to0}u(z)=p$ 存在，令 $\bar u(0)=p$ 便把 $u$ 连续延拓到整个 $D$。

**步骤 5：坐标化与椭圆正则性，得到光滑延拓。**

取 $p$ 附近的坐标卡 $\varphi:U\to\mathbb C^n$，$\varphi(p)=0$，并取 $\varphi$ 使 $J$ 在 $p$ 处化为标准复结构。由步骤 4，存在 $\rho>0$ 使 $u(D_\rho\setminus\{0\})\subset U$。令
$$f=\varphi\circ u:D_\rho\setminus\{0\}\to\mathbb C^n .$$
则 $f$ 连续（在 $0$ 处取值为 $0$），$f\in W^{1,2}(D_\rho;\mathbb C^n)$（能量有限），且 $f$ 满足局部坐标下的伪全纯方程
$$\partial_{\bar z}f+q(f)\,\partial_z f=0,$$
其中 $q$ 是光滑的 $\mathbb C^{n\times n}$-值函数，且 $q(0)=0$（因 $J$ 在 $p$ 处标准）。

由于 $f$ 连续、$q$ 光滑，复合 $q\circ f$ 有界且连续，上述方程是以 $f$ 为未知量的**一致椭圆**一阶系统，系数属于 $L^\infty$。由椭圆系统的 Weyl 引理（弱解若属于 $L^2$ 且系数有界，则属于 $W^{2,2}_{loc}$），得 $f\in W^{2,2}_{loc}(D_\rho)$。

再者，$f\in W^{2,2}_{loc}\subset C^{0,\alpha}_{loc}$（Sobolev 嵌入），故 $q\circ f\in C^{0,\alpha}$；对方程用 Schauder 估计得 $f\in C^{1,\alpha}$；再迭代（$f\in C^{k,\alpha}\Rightarrow q\circ f\in C^{k,\alpha}\Rightarrow f\in C^{k+1,\alpha}$）即得 $f\in C^\infty(D_\rho)$。特别地 $f$ 在 $0$ 处光滑，故 $\bar u=\varphi^{-1}\circ f$ 在 $0$ 处光滑，从而在整个 $D$ 上光滑且 $J$-全纯。$\square$

**步骤 6：推论与"能量集中"的解释。**

若 $\lim_{z\to0}u(z)$ 不存在，则由步骤 3–4 的推导（其唯一用到的假设是 $E(u)<\infty$）可见必有 $E(u)=\infty$：因为若 $E(u)<\infty$，步骤 2–4 便保证极限存在。这正是 Gromov 紧性定理中"气泡"的来源——气泡是能量在一点集中的极限，其定义域正是被挖去该点的（或极限中多出来的）$S^2$。$\square$

## 五、应用与意义

**理论意义**：

1. **伪全纯曲线模空间的正则性基础**：可去奇点定理保证了在定义域内部曲线的光滑性只取决于能量是否有限，从而模空间中的曲线是光滑的、其奇性只能出现在"能量爆破"处。

2. **Gromov 紧性定理的关键一步**：在证明紧性定理时，需要把收敛只在有限个点（能量集中点）失败的极限曲线补成光滑曲线并对这些点插值气泡；可去奇点定理正是"补点"的合法性来源。

3. **与调和映射理论的平行**：它是 Sacks–Uhlenbeck 关于有限能量调和映射 $S^2\to M$ 可去奇点定理的伪全纯对应物，二者共同构成模空间紧性分析的标准工具。

**应用领域**：

1. **Floer 同调**：Floer 方程的解在柱端具有有限能量，可去奇点定理（及其柱端版本）保证解在端部有极限、可用落点（asymptotics）分类，从而使模空间的紧致化与链复形的定义成立。

2. **Gromov–Witten 不变量与量子辛几何**：Gromov–Witten 不变量通过伪全纯曲线的模空间定义，其模空间紧性（含气泡）与不变量与 $J$ 的无关性都依赖本定理。

3. **Yamabe 型与调和映射问题**：有限能量解在奇点处的可去性，是研究缩并、爆破与亚稳定性时反复使用的引理。

4. **低维拓扑与辛拓扑**：Gromov 用伪全纯曲线证明辛嵌入的非挤压定理，其中曲线的奇点控制正是由可去奇点定理保证的。

**推广**：对权为 $2$ 的调和 $2$-形式、对具有有限能量的全纯曲线进入 Kähler 流形的情形，均有相应的可去奇点定理；经典全纯函数的可去奇点定理则是本定理在 $M=\mathbb C$ 时的特例。

## 相关条目

- [Gromov单调性引理](./Gromov单调性引理.md)：其局部形式给出的均值不等式是证明中控制曲线振荡的关键工具。
- [Gromov紧性定理](./Gromov紧性定理.md)：可去奇点定理是该定理中"补点插气泡"步骤的分析基础。
- [Floer同调](./Floer同调.md)：Floer 解的端部渐近与模空间紧化直接依赖本定理。
