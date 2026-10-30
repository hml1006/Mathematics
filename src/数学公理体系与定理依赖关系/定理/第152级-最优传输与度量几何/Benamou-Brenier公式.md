# Benamou–Brenier 公式

> **一句话大白话**：两个分布之间的 $W_2$ 距离的平方，等于"让分布像流体一样变形、用最小动能从 $\mu_0$ 流到 $\mu_1$"所需的最小总动能；也就是说，最省运费的搬运方案等价于最省能量的流体演化。
>
> **小例子**：一维上 $\mu_0=\delta_0$、$\mu_1=\delta_1$，取匀速流 $\mu_t=\delta_t$、$v_t\equiv1$，动能积分为 $\int_0^1 1^2\,\mathrm dt=1$，恰等于 $W_2^2(\delta_0,\delta_1)=1$。

## 介绍

Benamou–Brenier 公式（2000）把最优传输问题改写成流体力学中的"动能最小化"问题：
$$
W_2^2(\mu_0,\mu_1)=\inf\left\{\int_0^1\!\!\int_{\mathbb R^d}|v_t(x)|^2\,\mathrm d\mu_t(x)\,\mathrm dt\right\},
$$
下确界取遍满足连续性方程 $\partial_t\mu_t+\nabla\cdot(v_t\mu_t)=0$ 且两端边际为 $\mu_0,\mu_1$ 的曲线与速度场。它第一次把 $W_2$ 写成"作用量泛函"的下确界，从而使最优传输可以套用变分法与最优控制的全部机器：$W_2$ 测地线成为"动能最小的流"，$W_2$ 空间获得形式黎曼结构，JKO 格式与 Otto 演算也由此展开。

## 几何直观

![左侧分布先被压缩变形，中部是时刻变化的速度箭头场，右侧展开为目标分布，下方标注动能积分](images/th-152-06-benamou-brenier.svg)

图意在说明：把源分布推成目标分布的所有"动画"中，每帧都配一个速度场 $v_t$，动能 $\int|v_t|^2\,\mathrm d\mu_t$ 衡量这一帧的"费力程度"；沿直线匀速平移的动画最省力，其总动能恰等于 $W_2^2$，而绕路的动画更费力。

## 分析

**前置依赖**：Wasserstein 距离、连续性方程与分布意义下的导数、Brenier 定理、Cauchy–Schwarz 不等式。

**数学内涵**：
- 单向不等式（$A\ge W_2^2$）只用连续性方程：若 $v_t$ 生成的流把 $\mu_s$ 送到 $\mu_t$，则 $W_2(\mu_s,\mu_t)\le\int_s^t\|v_r\|_{L^2(\mu_r)}\,\mathrm dr$，再分段求和用 Cauchy–Schwarz。
- 另一方向（$A\le W_2^2$）用 Brenier 映射构造"位移插值" $\mu_t=((1-t)\mathrm{id}+t\nabla\varphi)_\#\mu_0$，速度场取 $v_t=\nabla\varphi-\mathrm{id}$，其动能恰为 $W_2^2$。
- 常见误区：连续性方程是分布意义下的，$v_t$ 只需 $\mu_t$-几乎处处有定义；要求 $v_t$ 光滑或 $\mu_t$ 有密度都只是技术假设，与公式本身无关。

**结构**：
1. 对任给流，用流的映射估计相邻时刻的 $W_2$ 距离，分段求和得 $W_2^2\le A$。
2. 用 Brenier 最优映射构造位移插值与相应速度场，验证连续性方程。
3. 计算该流的动能，得 $A\le W_2^2$，于是等号成立且下确界可达。

## 思考过程

Brenier 定理给出"最优映射是凸函数梯度"，但它是一张静态的图；要把 $W_2$ 变成几何对象，就需要知道两点之间的"直线"是什么。Benamou 与 Brenier 的观察是：把映射 $T$ 拆成一条从 $\mathrm{id}$ 到 $T$ 的连续路径 $T_t=(1-t)\mathrm{id}+tT$，并记录每一点的速度 $T-\mathrm{id}$，那么这条路径的"长度平方"就是 $\int|T-\mathrm{id}|^2\,\mathrm d\mu_0=W_2^2$。反过来，任何满足连续性方程的流都给出这条长度的一个上界，故最省能的流就是最短路。这个"把静态最优传输动态化"的想法，使 Otto 得以在 2001 年把 $W_2$ 形式地当作黎曼流形，用流体力学语言重写 Fokker–Planck、多孔介质与聚集方程。

## 证明过程

**定理**：设 $\mu_0,\mu_1\in\mathcal P_2(\mathbb R^d)$ 且 $\mu_0\ll\mathcal L^d$。记 $\mathcal A$ 为所有满足下述条件的对 $((\mu_t)_{t\in[0,1]},(v_t))$ 的动能积分之集：$t\mapsto\mu_t$ 弱连续、$\mu|_{t=0}=\mu_0$、$\mu|_{t=1}=\mu_1$，$v_t$ 为 Borel 向量场且 $\int_0^1\|v_t\|^2_{L^2(\mu_t)}\,\mathrm dt<\infty$，并且
$$
\partial_t\mu_t+\nabla\cdot(v_t\mu_t)=0\quad\text{在}\ \mathcal D'((0,1)\times\mathbb R^d)\ \text{中成立}.
$$
则 $W_2^2(\mu_0,\mu_1)=\inf_{\mathcal A}\int_0^1\!\!\int|v_t|^2\,\mathrm d\mu_t\,\mathrm dt$，且下确界由位移插值达到。

**证明**：

### 1. 连续性方程给出流的估计

设 $((\mu_t),v_t)\in\mathcal A$，并设 $v_t$ 足够正则使流映射 $\Phi_{s,t}$ 存在，$\Phi_{s,s}=\mathrm{id}$ 且 $\frac{\mathrm d}{\mathrm dt}\Phi_{s,t}(x)=v_t(\Phi_{s,t}(x))$。由连续性方程，$(\Phi_{s,t})_\#\mu_s=\mu_t$，故 $(\mathrm{id},\Phi_{s,t})$ 是 $\mu_s$ 与 $\mu_t$ 的一个耦合，于是
$$
W_2^2(\mu_s,\mu_t)\le\int|\Phi_{s,t}(x)-x|^2\,\mathrm d\mu_s(x).
$$
而 $\Phi_{s,t}(x)-x=\int_s^t v_r(\Phi_{s,r}(x))\,\mathrm dr$，由 Cauchy–Schwarz
$$
|\Phi_{s,t}(x)-x|^2\le(t-s)\int_s^t|v_r(\Phi_{s,r}(x))|^2\,\mathrm dr .
$$
对 $\mu_s$ 积分并用 $(\Phi_{s,r})_\#\mu_s=\mu_r$，得 $W_2^2(\mu_s,\mu_t)\le(t-s)\int_s^t\|v_r\|^2_{L^2(\mu_r)}\,\mathrm dr$。

### 2. 分段求和得下界

把 $[0,1]$ 等分成 $n$ 段，记 $t_i=i/n$。由三角不等式与第 1 步，
$$
W_2(\mu_0,\mu_1)\le\sum_{i=0}^{n-1}W_2(\mu_{t_i},\mu_{t_{i+1}})\le\sum_{i=0}^{n-1}\left(\frac1n\int_{t_i}^{t_{i+1}}\|v_r\|^2\,\mathrm dr\right)^{1/2}.
$$
再用一次 Cauchy–Schwarz（对 $n$ 项求和），
$$
W_2^2(\mu_0,\mu_1)\le\left(\sum_{i=0}^{n-1}\frac1n\right)\left(\sum_{i=0}^{n-1}\int_{t_i}^{t_{i+1}}\|v_r\|_{L^2(\mu_r)}^2\,\mathrm dr\right)=\int_0^1\|v_t\|^2_{L^2(\mu_t)}\,\mathrm dt .
$$
故 $W_2^2\le\inf_{\mathcal A}A$。

### 3. 位移插值给出上界

由 Brenier 定理，存在凸函数 $\varphi$ 使 $T=\nabla\varphi$ 为最优映射，$\gamma=(\mathrm{id},T)_\#\mu_0$ 最优，且 $W_2^2(\mu_0,\mu_1)=\int|T(x)-x|^2\,\mathrm d\mu_0$。令
$$
e_t(x)=(1-t)x+tT(x),\qquad \mu_t=(e_t)_\#\mu_0,\qquad t\in[0,1],
$$
则 $\mu_0,\mu_1$ 为两端边际。取 $v_t$ 为满足 $v_t(e_t(x))=T(x)-x$ 的 Borel 场（在碰撞点上任取，见下），对 $\zeta\in C_c^\infty$ 计算
$$
\frac{\mathrm d}{\mathrm dt}\int\zeta\,\mathrm d\mu_t=\int\nabla\zeta(e_t(x))\cdot\big(T(x)-x\big)\,\mathrm d\mu_0=\int\nabla\zeta\cdot v_t\,\mathrm d\mu_t ,
$$
最后一步用 $\mu_t=(e_t)_\#\mu_0$。这正是 $\partial_t\mu_t+\nabla\cdot(v_t\mu_t)=0$ 的弱形式，故 $((\mu_t),v_t)\in\mathcal A$。

### 4. 计算动能

由 $\mu_t=(e_t)_\#\mu_0$ 与 $v_t(e_t(x))=T(x)-x$，
$$
\int_0^1\!\!\int|v_t|^2\,\mathrm d\mu_t\,\mathrm dt=\int_0^1\!\!\int|T(x)-x|^2\,\mathrm d\mu_0\,\mathrm dt=\int|T(x)-x|^2\,\mathrm d\mu_0=W_2^2(\mu_0,\mu_1).
$$

### 5. 结论

第 2 步给 $W_2^2\le\inf A$，第 3、4 步给 $\inf A\le W_2^2$，故等号成立，且位移插值达到下确界。碰撞点上 $v_t$ 的定义不影响 $\mu_t$-积分与弱形式，因为 $e_t$ 的像上的测度由 $(\mathrm{id},T)$ 的计划唯一决定。$\square$

## 课堂问答

**老师**：这个公式看起来只是把"搬运"换成"流动"，为什么算是重要进展？

**学生**：因为它把 $W_2$ 从"两个测度之间的数"变成"一条曲线上的作用量"。有了作用量就能谈变分、谈测地线、谈梯度流，$W_2$ 空间于是可以做微分几何；JKO 格式、Otto 演算、Wasserstein 空间上的 Ricci 曲率都是沿这条路走出来的。

**老师（追问）**：为什么必须要求两个方向分别证明，而不能只构造最优流？

**学生**：构造最优流只给出 $\inf A\le W_2^2$，即"存在一条这么省力的流"。要说明它是所有流里最省的，必须证明任给一条流其动能都不小于 $W_2^2$，这靠的是流的映射给出 $W_2$ 估计再分段求和，本质上是最短路的三角不等式。两个方向合起来才是等号。

**老师（拓展）**：如果换成 $p>1$ 的代价，这个公式怎么变？

**学生**：把 $|v_t|^2$ 换成 $|v_t|^p$、把连续性方程保留，就得到 $W_p^p(\mu_0,\mu_1)=\inf\int_0^1\!\!\int|v_t|^p\,\mathrm d\mu_t\,\mathrm dt$，最优流仍由位移插值给出。这条"作用量即距离"的思路还可推广到度量测度空间，成为定义 $W_p$ 测地线与研究 Euler 方程（Arnold 的无穷维几何观点）的出发点。
