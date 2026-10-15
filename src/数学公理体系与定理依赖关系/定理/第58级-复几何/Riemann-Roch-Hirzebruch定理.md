# Riemann-Roch-Hirzebruch 定理

> **一句话大白话**：紧复流形上，一个全纯向量丛的各阶上同调维数的交错和（解析指标）等于一个纯拓扑量——把该丛的 Chern 特征标与流形的 Todd 类相乘再积分。
>
> **小例子**：取 $E=\mathcal O$、$X$ 为紧 Riemann 面，则 $\chi(X,\mathcal O)=1-g=\int_X\operatorname{td}(X)=\int_X(1+\tfrac{1}{2}c_1(X))$，即经典 Riemann–Roch：$h^0-h^1=1-g$。

## 一、定理介绍

> **前置依赖**：紧复流形与全纯向量丛、Dolbeault 定理 $H^{q}(X,E)\cong H^{0,q}_{\bar\partial}(X,E)$、$\bar\partial_E$ 与 Dolbeault 复形、椭圆算子与指标（解析指标）、Chern 类与 Chern 特征标 $\operatorname{ch}$、Todd 类 $\operatorname{td}(X)$、分裂原理（Chern 根）、Atiyah–Singer 指标定理

Riemann–Roch–Hirzebruch 定理（HRR，Hirzebruch 1954 年证明，推广了 Riemann 与 Roch 对曲线的经典结果、以及 Riemann–Roch–Hirzebruch 对代数曲面的结果）断言：对紧复流形 $X$ 上的全纯向量丛 $E$，
$$\chi(X,E):=\sum_{q=0}^{n}(-1)^{q}\dim_{\mathbb C}H^{q}(X,E)=\int_{X}\operatorname{ch}(E)\wedge\operatorname{td}(X),$$
其中
$$\operatorname{ch}(E)=\operatorname{rank}E+\sum_{i\ge1}\frac{1}{i!}\text{（Chern 类的多项式）},\qquad \operatorname{td}(X)=\prod_{j}\frac{x_j}{1-e^{-x_j}},$$
$x_j$ 是 $T^{1,0}X$ 的 Chern 根。

这一定理是复几何与代数几何中最重要的计算工具：它给出上同调维数的交错和（一个解析/代数量）等于拓扑量（Chern 数与 Todd 数）。它是 Atiyah–Singer 指标定理在 $\bar\partial$ 算子情形下的特例与先导；在代数几何中，它与 Serre 对偶、Grothendieck 对偶（Grothendieck–Riemann–Roch）一起构成相交理论与枚举几何的基础。

## 二、原理思路

证明（现代方式）借助 Atiyah–Singer 指标定理，分三步：

1. **解析指标 = 椭圆算子的指标**：由 Dolbeault 定理，$\bigoplus_q H^{q}(X,E)$ 是椭圆算子
$$\bar\partial_E:\mathcal A^{0,\text{even}}(X,E)\longrightarrow\mathcal A^{0,\text{odd}}(X,E)$$
（更精确地 $D=\bar\partial_E+\bar\partial_E^{*}$）的核与余核，故
$$\chi(X,E)=\operatorname{ind}(\bar\partial_E):=\dim\ker\bar\partial_E-\dim\operatorname{coker}\bar\partial_E.$$

2. **拓扑指标（Atiyah–Singer）**：对紧流形上的椭圆算子，分析指标等于拓扑指标，后者由算子符号的 K 理论类与流形的 Todd 类通过 $\operatorname{ch}\cdot\operatorname{td}$ 计算。对 $\bar\partial_E$，其符号类给出 $\operatorname{ch}(E)$，流形贡献 $\operatorname{td}(X)$。

3. **显式计算（分裂原理）**：用分裂原理把 $T^{1,0}X$ 与 $E$ 分别拆成线丛之和，则
$$\operatorname{td}(X)=\prod_j\frac{x_j}{1-e^{-x_j}},\qquad \operatorname{ch}(E)=\sum_i e^{y_i},$$
（$x_j$ 为切丛 Chern 根，$y_i$ 为 $E$ 的 Chern 根），积分即得具体的 Chern 数表达式。

对低维情形可给出初等验证：曲线 $n=1$、曲面 $n=2$ 的 HRR 可分别由 Serre 对偶 + Chern 类计算与 Noether 公式直接证明，无需指标定理。

## 三、定理的严格表述

**（Riemann–Roch–Hirzebruch 定理）** 设 $X$ 是 $n$ 维紧复流形，$E\to X$ 是全纯向量丛。则
$$\chi(X,E)=\sum_{q=0}^{n}(-1)^{q}\dim_{\mathbb C}H^{q}(X,E)=\int_{X}\operatorname{ch}(E)\operatorname{td}(X),$$
其中积分指取 $H^{2n}(X;\mathbb Q)$ 的基本类方向的分量。

**（特征类的显式形式）** 由分裂原理，形式上引入切丛的 Chern 根 $x_1,\dots,x_n$（$c(T^{1,0}X)=\prod_j(1+x_j)$）与 $E$ 的 Chern 根 $y_1,\dots,y_r$（$c(E)=\prod_i(1+y_i)$），则
$$\operatorname{td}(X)=\prod_{j=1}^{n}\frac{x_j}{1-e^{-x_j}},\qquad \operatorname{ch}(E)=\sum_{i=1}^{r}e^{y_i}.$$
于是
$$\chi(X,E)=\int_{X}\left(\sum_{i=1}^{r}e^{y_i}\right)\prod_{j=1}^{n}\frac{x_j}{1-e^{-x_j}}.$$

**（低维特例）**
- **曲线（$n=1$）**：$\chi(X,E)=\deg E+\operatorname{rank}E\,(1-g)$；取 $E=\mathcal O_D$（除子 $D$）即经典 Riemann–Roch $\chi(\mathcal O_D)=\deg D+1-g$。
- **曲面（$n=2$）**：$\chi(X,E)=\operatorname{rank}E\,\chi(\mathcal O_X)+\deg(\ldots)$，即 Noether 公式
$$\chi(X,E)=\operatorname{rank}E\cdot\frac{c_1^{2}+c_2}{12}+\frac{1}{2}\bigl(c_1(E)^2-c_1(E)c_1(X)\bigr)-\frac{1}{2}\bigl(c_1(E)\,c_1(X)\bigr)+\cdots$$
（写成标准形式：$\chi(E)=\operatorname{rank}E\cdot\chi(\mathcal O_X)+\frac12(c_1(E)^2-c_1(E)c_1(X))+\frac12 c_1(E)\,c_1(X)$ 型的组合，其中 $\chi(\mathcal O_X)=\frac{c_1^2+c_2}{12}$）。
- **射影空间（$X=\mathbb{CP}^{n}$）**：$T^{1,0}\mathbb{CP}^{n}$ 的 Chern 根为 $n$ 个 $h$ 与 $-h$ 的配列组合，给出 $\operatorname{td}(\mathbb{CP}^{n})=(1+h)^{n+1}/h$ 的截断。

**（Atiyah–Singer 形式）** $\chi(X,E)=\operatorname{ind}(\bar\partial_E)=\operatorname{ind}_{\text{top}}(\bar\partial_E)$，其中 $\operatorname{ind}_{\text{top}}$ 由符号 $\sigma(\bar\partial_E)=$ 的 K 理论类与 $\operatorname{td}(X)$ 给出。

## 四、证明过程

**步骤 1：把交错和化为椭圆算子指标。**

由 Dolbeault 定理，$H^{q}(X,E)\cong H^{0,q}_{\bar\partial}(X,E)$（取值于 $E$ 的 $\bar\partial$-上同调）。考虑 Dolbeault 复形
$$0\to\mathcal A^{0,0}(X,E)\xrightarrow{\bar\partial_E}\mathcal A^{0,1}(X,E)\xrightarrow{\bar\partial_E}\cdots\xrightarrow{\bar\partial_E}\mathcal A^{0,n}(X,E)\to0.$$
它在每一处是椭圆复形（$\bar\partial_E$ 的符号在 $(0,q)$-形式上由 $\xi^{0,1}$-外乘给出，恰为椭圆）。于是
$$\chi(X,E)=\sum_q(-1)^q\dim H^{q}=\operatorname{ind}(\bar\partial_E:\mathcal A^{0,\text{even}}\to\mathcal A^{0,\text{odd}}). \square$$

**步骤 2：应用 Atiyah–Singer 指标定理。**

**Atiyah–Singer 指标定理**：紧流形上任意椭圆算子 $D$ 满足
$$\operatorname{ind}(D)=\operatorname{ind}_{\text{top}}(D):=\int_{T^{*}X}\operatorname{ch}(\sigma(D))\operatorname{td}(T^{*}X\otimes\mathbb C)\Big|_{\text{基本类}}.$$
对 $D=\bar\partial_E$（作用在偶/奇 $(0,\bullet)$ 形式），其符号在 $(x,\xi)\in T^{*}X$ 处为 Clifton–外乘算子 $\xi^{0,1}\wedge-\xi^{0,1}\text{-收缩}$，其 K 理论类恰为 $\pi^{*}E$（$\pi:T^{*}X\to X$），而 $T^{*}X$ 的 Todd 类在 $\pi^{*}$ 下的贡献给出 $X$ 的 ${td}(X)$。代入即得
$$\operatorname{ind}(\bar\partial_E)=\int_{X}\operatorname{ch}(E)\operatorname{td}(X). \square$$

**步骤 3：用分裂原理计算 Todd 类与 Chern 特征标。**

由分裂原理（见「Chern 类与分裂原理」），存在 $\pi:Fl(T^{1,0}X)\to X$（必要时与 $E$ 的旗丛取纤维积）使 $\pi^{*}(T^{1,0}X)=\bigoplus_j L_j$、$\pi^{*}E=\bigoplus_i M_i$ 且 $\pi^{*}$ 在上同调上单射。记 $x_j=c_1(L_j)$、$y_i=c_1(M_i)$。则
$$c(T^{1,0}X)=\prod_j(1+x_j),\qquad c(E)=\prod_i(1+y_i),$$
由分裂原理的 $\pi^*$-单射性，关于特征类（对称多项式）的恒等式可在分裂情形验证，故
$$\operatorname{td}(X)=\pi^{*}\text{-拉回意义下}\prod_j\frac{x_j}{1-e^{-x_j}},\qquad \operatorname{ch}(E)=\sum_i e^{y_i}.$$
在分裂情形，$e^{y_i}$ 与 $\frac{x_j}{1-e^{-x_j}}$ 展开为
$$e^{y_i}=1+y_i+\frac{y_i^{2}}{2!}+\cdots,\qquad \frac{x}{1-e^{-x}}=1+\frac{x}{2}+\frac{x^{2}}{12}-\frac{x^{4}}{720}+\cdots,$$
乘积的 $2n$ 次分量给出由 Chern 数与 Chern 特征标组成的拓扑不变量。$\square$

**步骤 4：曲线情形的初等验证。**

设 $\dim X=1$、$E$ 为秩 $r$ 的全纯向量丛。由 Serre 对偶 $H^{1}(X,E)\cong H^{0}(X,\omega_X\otimes E^{*})^{*}$，并利用 $\deg$ 与 $\operatorname{rank}$ 的可加性，得
$$\chi(X,E)=\deg E+r(1-g).$$
另一方面，$\operatorname{ch}(E)=r+c_1(E)$，$\operatorname{td}(X)=1+\frac{1}{2}c_1(X)$，$c_1(X)$ 的次数为 $2-2g$，故
$$\int_X\operatorname{ch}(E)\operatorname{td}(X)=\int_X\left(r+c_1(E)\right)\left(1+\frac{1}{2}c_1(X)\right)=\frac{r}{2}\cdot 2(1-g)+\deg E=r(1-g)+\deg E.$$
两边一致，定理在 $n=1$ 成立。$\square$

**步骤 5：一般情形的逻辑链条。**

一般 $n$ 由步骤 1–3 完成：指标定理给 $\operatorname{ind}(\bar\partial_E)=\int\operatorname{ch}(E)\operatorname{td}(X)$，而步骤 1 给 $\operatorname{ind}(\bar\partial_E)=\chi(X,E)$，两者合并即定理。需要强调指标的"拓扑不变性"：$\operatorname{ind}(\bar\partial_E)$ 只依赖 $E$ 的拓扑类与 $X$ 的拓扑，故可用分裂原理在形式上化简。$\square$

## 五、应用与意义

**理论意义**：
1. **分析—拓扑的等价**：把复几何中的上同调维数（解析量）完全化为 Chern 数与 Todd 数（拓扑量），是"指标定理"思想的最初范例。
2. **K 理论与上同调**：Chern 特征标 $\operatorname{ch}:K^0(X)\to H^{\text{even}}(X;\mathbb Q)$ 是环同构（模挠），HRR 是其在整体几何上的表现。
3. **Grothendieck 推广**：相对版本 Grothendieck–Riemann–Roch 把 HRR 推广到映射 $f:X\to Y$ 的（上）同调推进，是代数几何相交理论的核心。

**应用领域**：
1. **代数几何**：曲线/曲面的 Riemann–Roch、Noether 公式、Hirzebruch–Riemann–Roch 用于计算层上同调、几何亏格与不变量。
2. **模空间与计数几何**：Gromov–Witten 不变量、Donaldson–Thomas 不变量、Hilbert 概型的交点计算。
3. **Kodaira 嵌入与消没**：奇点消解、曲面分类（Enriques–Kodaira 分类）中的关键计算。
4. **数学物理**：弦论中反常消除、椭圆亏格与配分函数中的指标计算。

**推广**：
- **Atiyah–Singer 指标定理**：把 HRR 推广到任意椭圆算子与 Dirac 型算子（$\hat A$-亏格、Signature 定理）。
- **等变 HRR**：Atiyah–Segal–Singer 的等变指标定理（Lefschetz 不动点公式的推广）。
- **特征 $p$ 与晶体情形**：Grothendieck–Riemann–Roch 在代数 $K$ 理论、晶体上同调、以及 Riemann–Roch 对奇异簇的推广（Verdier 的 RR）。

## 课堂问答

**老师**：Riemann-Roch-Hirzebruch 把"上同调维数的交错和"变成纯拓扑积分。它本质上是哪个定理的特例？

**学生**：是指标定理的特例。由 Dolbeault 定理，$\sum_q(-1)^q\dim H^q(X,E)=\mathrm{ind}(\bar\partial_E)$，即 Dolbeault 复形（偶次到奇次）的解析指标。Atiyah-Singer 指标定理说解析指标等于拓扑指标 $\int_X\mathrm{ch}(E)\mathrm{td}(X)$，其中 $\bar\partial_E$ 的符号类给出 $\mathrm{ch}(E)$，流形贡献 $\mathrm{td}(X)=\prod_j\frac{x_j}{1-e^{-x_j}}$，$x_j$ 是 $T^{1,0}X$ 的 Chern 根。

**老师（追问）**：不用指标定理，曲线情形能直接验证吗？

**学生**：能。曲线 $X$ 上 $\mathrm{ch}(E)=r+c_1(E)$、$\mathrm{td}(X)=1+\frac12c_1(X)$，积分得 $\int_X(r+c_1(E))(1+\frac12c_1(X))=r(1-g)+\deg E$，而 Serre 对偶给 $\chi(X,E)=\deg E+r(1-g)$，两边一致。曲面情形则由 Noether 公式 $\chi(\mathcal O_X)=\frac{c_1^2+c_2}{12}$ 实现。

**老师（拓展）**：分裂原理在定理证明中扮演什么角色？

**学生**：它把计算从一般丛约化到线丛之和。取旗丛 $Fl(T^{1,0}X)$ 使 $\pi^*(T^{1,0}X)=\bigoplus_jL_j$、$\pi^*(E)=\bigoplus_iM_i$，$c_1(L_j)=x_j$、$c_1(M_i)=y_i$，于是 $\mathrm{ch}(E)=\sum_ie^{y_i}$、$\mathrm{td}(X)=\prod_j\frac{x_j}{1-e^{-x_j}}$，展开取 $2n$ 次分量即得由 Chern 数组成的拓扑不变量。其相对形式 Grothendieck-Riemann-Roch 进一步推广到态射 $f:X\to Y$，成为相交理论的核心。
