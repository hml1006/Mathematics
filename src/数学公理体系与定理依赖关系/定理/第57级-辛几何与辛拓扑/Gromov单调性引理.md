# Gromov 单调性引理

> **一句话大白话**：全纯曲线经过一点时，在围绕该点的球内"必须占用"至少与球面积成正比的一点能量；它没法把能量藏得无限稀疏——因此曲线不可能无限次地挤过同一点而不付出能量代价。
>
> **小例子**：$u:\mathbb C\to\mathbb C^{n}$ 全纯、$u(0)=0$，则 $\pi r^{2}m\le\text{Area}(u\cap B_r)$，其中 $m\ge1$ 是原点处的重数；$r\to0$ 时比值趋于 $\pi m$。

## 一、定理介绍

> **前置依赖**：伪全纯曲线与相容近复结构 $J$、辛形式 $\omega$ 与诱导度量、多重数（局部相交数）、辛形式与相容近复结构下的能量恒等式、$dd^{c}$ 与多次调和函数（plurisubharmonic）、坐标正规化（测地正规坐标 / Darboux 坐标）、比较定理

Gromov 单调性引理（monotonicity lemma，Gromov 1985）是伪全纯曲线局部理论的基本引理。它给出伪全纯曲线穿过一点时能量的**局部下界**：存在常数 $\hbar=\hbar(M,\omega,J,r)>0$，使任何非平凡的、经过 $p$ 且以多重数 $m$ 经过 $p$ 的 $J$-全纯曲线 $u$ 满足
$$\int_{u^{-1}(B_r(p))}u^{*}\omega\ \ge\ m\,\hbar.$$
在最简单的模型 $\mathbb C^{n}$（标准形式与标准复结构）中，这正是 Lelong 的经典结果
$$\text{Area}\bigl(u\cap B_r\bigr)\ \ge\ \pi r^{2}\,m,\qquad \lim_{r\to0}\frac{\text{Area}(u\cap B_r)}{\pi r^{2}}=m.$$
等价的"单调性"表述为：函数
$$a(r)=\frac{1}{r^{2}}\int_{u^{-1}(B_r(p))}u^{*}\omega$$
关于 $r$ 单调不减（在 $\mathbb C^n$ 中精确成立，在一般流形中对小的 $r$ 成立，或至多差一个由曲率控制的因子）。

这条引理是 Gromov 紧性定理的"能量量子化"步骤，也是"曲线不能在一点附近以任意小的能量发生拓扑变化"这一刚性现象的来源；它是 Gromov 非挤压定理、Floer 同调的能量估计、以及 SFT 中有界能量分析的关键。

## 二、原理思路

证明分"局部模型"与"流形化"两步。

1. **局部模型 $\mathbb C^{n}$（Lelong 论证）**：设 $u:\Sigma\to\mathbb C^{n}$ 全纯，$u(0)=0$。关键观察是 $dd^{c}|z|^{2}=2\sum dx_j\wedge dy_j$ 正是 Euclidean 面积形式（适当归一化），而 $dd^{c}\log|z|^{2}\ge0$（$\log|z|$ 是多次调和的，在 $\mathbb C^{n}\setminus\{0\}$ 上 $dd^{c}\log|z|^{2}$ 是原点处的正流），于是由 Stokes 定理，
$$a(r)=\frac{1}{r^{2}}\int_{u^{-1}(B_r)}u^{*}\bigl(dd^{c}|z|^{2}\bigr)=\int_{u^{-1}(\partial B_r)}u^{*}\bigl(d^{c}\log|z|^{2}\bigr),$$
且当 $r>s>0$ 时
$$a(r)-a(s)=\int_{u^{-1}(B_r\setminus B_s)}u^{*}\bigl(dd^{c}\log|z|^{2}\bigr)\ \ge\ 0.$$
故 $a$ 单调不减；又当 $r\to0$ 时 $a(r)\to\pi m$（$m$ 为原点处重数，由 Lelong–Poincaré 公式或局部展开得到），从而 $\text{Area}(u\cap B_r)=$（常数）$\cdot r^{2}a(r)\ge\pi r^{2}m$。

2. **流形化**：在一般 $(M,\omega,J,r)$ 中，在 $p$ 附近取 Darboux 坐标把 $\omega$ 化为标准形式（误差 $O(|z|)$），并把 $\omega$ 诱导的度量与平坦度量比较（在半径 $r<\text{inj}(p)$ 内二者可比较）；于是上述 Lelong 估计迁移到流形上，常数 $\hbar$ 吸收比较因子。$J$-相容性保证 $u$ 在局部坐标下是（近）全纯的，故 $dd^{c}$-正性论证仍适用。

## 三、定理的严格表述

**（Gromov 单调性引理）** 设 $(M,\omega)$ 是辛流形，$J$ 是与 $\omega$ 相容的近复结构，$g=\omega(\cdot,J\cdot)$ 为诱导 Riemann 度量，$p\in M$，取 $r<\text{inj}_{g}(p)$（单射半径）。则存在常数 $\hbar=\hbar(M,\omega,J,r)>0$，使对任何 $J$-全纯曲线
$$u:(\Sigma,j)\longrightarrow M,\qquad \bar\partial_{J}u=0,$$
若 $u$ 经过 $p$（即存在 $z_0\in\Sigma$ 使 $u(z_0)=p$）且在 $p$ 处的多重数为 $m\ge1$（即局部相交数 $m=\bigl(u\cdot[p]\bigr)_{z_0}$），则
$$\int_{u^{-1}(B_r(p))}u^{*}\omega\ \ge\ m\,\hbar.$$
特别地，任何非平凡经过 $p$ 的 $J$-全纯曲线满足 $\displaystyle\int_{u^{-1}(B_r(p))}u^{*}\omega\ge\hbar>0$。

**（单调性形式）** 对 $0<s<r$，
$$\frac{1}{r^{2}}\int_{u^{-1}(B_r(p))}u^{*}\omega\ \ge\ C^{-1}\,\frac{1}{s^{2}}\int_{u^{-1}(B_s(p))}u^{*}\omega,$$
其中 $C=C(M,\omega,J,r)\ge1$（在 $\mathbb C^{n}$ 的标准情形可取 $C=1$，即比值关于半径单调不减）。

**（长 Lelong 不等式 / 精确模型）** 在 $(\mathbb C^{n},\omega_{0},i)$ 中，对全纯 $u$ 有
$$\int_{u^{-1}(B_r)}u^{*}\omega_{0}\ \ge\ \pi r^{2}m,\qquad \lim_{r\to0}\frac{1}{\pi r^{2}}\int_{u^{-1}(B_r)}u^{*}\omega_{0}=m,$$
其中 $m$ 是 $u$ 在 $0\in\mathbb C^{n}$ 处的重数（$u(0)=0$）。

## 四、证明过程

**步骤 1：$\mathbb C^{n}$ 中的基本恒等式。**

在 $\mathbb C^{n}$ 上用坐标 $z=(z_1,\dots,z_n)$，$z_j=x_j+iy_j$，标准辛形式 $\omega_{0}=\sum_{j}dx_j\wedge dy_j=\frac{i}{2}\sum_j dz_j\wedge d\bar z_j$。定义
$$\rho(z)=|z|^{2}=\sum_j|z_j|^{2}.$$
直接计算
$$dd^{c}\rho=2\sum_{j}dx_j\wedge dy_j=2\omega_{0},\qquad d=\partial+\bar\partial,\quad d^{c}=i(\bar\partial-\partial).$$
又对 $\log\rho$：因 $\log|z|$ 在 $\mathbb C^{n}\setminus\{0\}$ 上调和，$\log\rho=2\log|z|$ 在 $\mathbb C^{n}\setminus\{0\}$ 上调和，故
$$dd^{c}\log\rho=0\quad(z\ne0),$$
且以原点为支撑（作为 $(1,1)$-流，$dd^{c}\log|z|^{2}=(2\pi)\cdot[\text{超平面}]\cdot$ 型；精确地 $dd^{c}\log\rho$ 的系数 $2\pi$ 使 Lelong–Poincaré 公式成立）。因此 $dd^{c}\log\rho\ \ge\ 0$ 作为流成立。$\square$

**步骤 2：$a(r)$ 的单调性。**

设 $u:\Sigma\to\mathbb C^{n}$ 全纯，$u(0)=0$。定义
$$a(r)=\frac{1}{r^{2}}\int_{u^{-1}(B_r)}u^{*}\bigl(dd^{c}\rho\bigr)\quad\text{（此处}\ dd^{c}\rho=2\omega_{0}\text{，故与面积成正比）}.$$
由 Stokes 定理（在 $u^{-1}(B_r\setminus B_s)$ 上，$u^{*}(dd^{c}f)=d(u^{*}d^{c}f)$）与 $d^{c}\rho=\rho\,d^{c}\log\rho$（因 $d^{c}\rho=\rho\,d^{c}\log\rho$）：
$$a(r)=\frac{1}{r^{2}}\int_{u^{-1}(\partial B_r)}u^{*}\bigl(d^{c}\rho\bigr)=\int_{u^{-1}(\partial B_r)}u^{*}\bigl(d^{c}\log\rho\bigr).$$
（用到 $u^{*}\rho=r^{2}$ 在 $\partial B_r$ 上。）于是对 $r>s>0$，
$$a(r)-a(s)=\int_{u^{-1}(B_r\setminus B_s)}u^{*}\bigl(dd^{c}\log\rho\bigr)\ \ge\ 0,$$
最后一步用到步骤 1 的 $dd^{c}\log\rho\ge0$ 与 $u$ 全纯（$u^{*}$ 保持 $(1,1)$-型的正性：全纯拉回保持正性）。故 $r\mapsto a(r)$ 单调不减。$\square$

**步骤 3：$r\to0$ 的极限与重数。**

由 Lelong–Poincaré 公式，$u_{*}[u^{-1}]$（以重数计的原像流）在 $0$ 处的 Lelong 数等于 $m$，即
$$\lim_{r\to0}\frac{1}{\pi r^{2}}\int_{u^{-1}(B_r)}u^{*}\omega_{0}=m.$$
（局部地写 $u(z)=u^{(m)}(z)+\text{高阶}$，$u^{(m)}$ 是第一个非零齐次分量，为 $m$ 次齐次多项式；$\displaystyle\lim_{r\to0}\frac{1}{\pi r^2}\int_{u^{-1}(B_r)}\omega_0$ 恰为该齐次映射的"次数"$m$，即重数。）由步骤 2 的单调性与步骤 3 的极限，对一切 $r>0$
$$\int_{u^{-1}(B_r)}u^{*}\omega_{0}=\frac{\pi r^{2}}{}\,a(r)\ \ge\ \pi r^{2}\,m. \square$$

**步骤 4：流形化（局部比较）。**

设 $p\in M$，取 $r<\text{inj}(p)$，令 $\exp_p:B_r(0)\subset T_pM\to B_r(p)$ 为测地指数映射。在 $T_pM$ 上选取使 $\omega_{p}=$ 标准形式的线性坐标（Darboux 线性化），并把 $\exp_p$ 拉回：在 $p$ 的局部坐标 $z$ 下，
$$\exp_p^{*}\omega=\omega_{0}+O(|z|),\qquad u^{*}\omega=u^{*}\omega_{0}+O(|z|)\,|du|^{2}\ \text{型}.$$
由 $J$-相容性，$\omega(\cdot,J\cdot)$ 是 Riemann 度量，与平坦度量在 $B_r$ 内可比较（比较常数 $C$）。把步骤 1–3 的论证用于 $\rho(z)=|z|^{2}\circ\exp_p^{-1}$（它是 $p$ 附近的"平方距离"函数，严格 $J$-多次调和且 $\sqrt{\rho}$ 亦 $J$-多次调和，可由步骤 1 的平坦情形 + $O(|z|)$ 扰动得到：$dd^{c}\rho$ 与 $\omega$ 可比较、$dd^{c}\sqrt{\rho}\ge0$ 在 $p$ 外成立），得
$$a(r)=\frac{1}{r^{2}}\int_{u^{-1}(B_r(p))}u^{*}\omega\ \text{单调（或差常数因子 }C^{-1}\text{）},$$
且 $\lim_{r\to0}a(r)\ge\pi m$ 型的下界，从而
$$\int_{u^{-1}(B_r(p))}u^{*}\omega\ \ge\ m\,\hbar,\qquad \hbar=\hbar(M,\omega,J,r)>0. \square$$

**步骤 5：常数 $\hbar$ 的存在性。**

由步骤 4，$\hbar$ 可以取为 $C^{-1}\pi$ 型常数（$C$ 来自度量比较与 $\omega$ 与 $dd^{c}\rho$ 的比较，仅依赖 $(M,\omega,J,r)$），故结论成立。$\square$

## 五、应用与意义

**理论意义**：
1. **能量量子化**：曲线经过一点必须付出一致正的能量，从而在能量有界时"经过某点的次数"一致有界，这是 Gromov 紧性定理中气泡数目有限的核心。
2. **刚性来源**：说明伪全纯曲线不能把能量"摊薄到无穷小"，是辛刚性（非挤压定理）的分析根基。
3. **正闭流与 Lelong 理论**：把多复变中的 Lelong–Poincaré 公式推广到近复（辛）情形，是非交换几何与正流理论的模型。

**应用领域**：
1. **Gromov–Witten 理论**：模空间紧化与虚拟基本类的能量估计。
2. **Floer 同调与 Arnold 猜测**：条带/圆柱的能量下界保证 $C^{0}$-界与紧性。
3. **辛拓扑与嵌入问题**：Gromov 非挤压定理、辛容量、Lagrangian 相交的刚性。
4. **SFT 与接触几何**：Hofer 能量的量子化与全纯建筑的收敛分析。

**推广**：
- **带边界的单调性**：对带 Lagrange 边界的曲线，在边界点附近用"平方距离到 Lagrange"作为多次调和函数，得到边界型单调性（Groman–Solomon 反向等周不等式、Duval 的证明）。
- **多重数与相交数**：带多重数 $m$ 的版本；以及曲线与除子/子流形相交的局部下界。
- **高余维与正流**：对正闭流（任意余维）的 Lelong 数与单调性，是正流极值理论的基础。

## 课堂问答

**老师**：Gromov 单调性引理给出什么定量下界？

**学生**：设 $J$ 与 $\omega$ 相容，$p\in M$，$r<\mathrm{inj}(p)$，则存在 $\hbar=\hbar(M,\omega,J,r)>0$，使任何经过 $p$、在 $p$ 处重数为 $m$ 的 $J$-全纯曲线满足
$$\int_{u^{-1}(B_r(p))}u^*\omega\ge m\,\hbar.$$
即在 $(\mathbb C^n,\omega_0,i)$ 中 $\mathrm{Area}(u\cap B_r)\ge\pi r^2m$，且 $r\to0$ 时比值 $\to m$。常见误区是把 $\hbar$ 理解为曲线整体能量——它只是小球内的局部能量下界。

**老师（追问）**：在 $\mathbb C^n$ 模型中，单调性是怎么来的？

**学生**：令 $a(r)=\frac1{r^2}\int_{u^{-1}(B_r)}u^*(dd^c\rho)$（$\rho=|z|^2$，$dd^c\rho=2\omega_0$）。由 $dd^c\rho=\rho\,dd^c\log\rho$ 与 Stokes 得 $a(r)=\int_{u^{-1}(\partial B_r)}u^*(d^c\log\rho)$，于是
$$a(r)-a(s)=\int_{u^{-1}(B_r\setminus B_s)}u^*(dd^c\log\rho)\ge0,$$
最后一步用 $dd^c\log\rho\ge0$（$\log|z|$ 调和）与全纯拉回保正性，故 $a$ 单调不减；再由 Lelong–Poincaré 公式 $a(r)\to\pi m$ 得下界。流形上取 Darboux 坐标把 $\omega$ 化为 $\omega_0+O(|z|)$、用度量比较吸收常数即得。

**老师（拓展）**：这条引理在辛拓扑中扮演什么角色？

**学生**：它是"能量量子化"的核心：曲线经过一点必付出统一正的能量，故能量有界时经过某点的次数一致有界，从而 Gromov 紧性中气泡数目有限；也是辛刚性（非挤压）与 Floer 能量估计的分析根基。带 Lagrange 边界的版本（对边界点用"到 $L$ 的平方距离"作为多次调和函数）给出边界型单调性。
