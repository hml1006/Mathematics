# Hopf-Rinow定理

> **一句话大白话**：黎曼流形的"完备"有好几种看似不同的说法——度量空间完备、测地线能无限延伸、有界闭集是紧的、指数映射定义在整个切空间上——它们其实说的是同一件事；而且只要完备，任意两点之间必有一条最短测地线。
>
> **小例子**：$\mathbb R^2$ 去掉原点就不完备：从某点出发的测地线可能"撞进"缺失的原点而无法延伸，两点间也未必有最短测地线。而球面 $S^2$ 与 $\mathbb R^n$ 都完备，任意两点都有极小测地线。

## 介绍

Hopf-Rinow 定理是黎曼几何的全局基本定理，由 Heinz Hopf 与 Willi Rinow 于 1931 年证明。它把四种完备性概念统一起来，并断言完备流形上任意两点可由极小测地线连接。

定理建立了"局部几何"（测地线方程是局部 ODE）与"全局度量"（距离、完备性、紧性）之间的桥梁：测地线完备是纯几何的、易检验的（解 ODE 能否延伸到全 $\mathbb R$），而度量完备是纯拓扑的。定理说两者等价，于是人们可以在二者间自由切换。它是 Bonnet–Myers 定理、Cartan–Hadamard 定理、Cheeger–Gromoll 分裂定理以及指数映射全局理论的前提。

## 分析

**前置依赖**：黎曼流形与度量、测地线与指数映射、测地线的极大延拓、Riemann 距离 $d(p,q)$、度量空间的完备性与紧性、逆映射定理、ODE 解对初值的连续依赖。

**定理内容**：设 $(M,g)$ 是连通黎曼流形。以下条件等价：

1. $(M,d)$ 是完备度量空间（度量完备）；
2. $(M,g)$ 是测地线完备的（每条测地线可延拓到 $t\in\mathbb R$）；
3. 存在 $p\in M$，使 $\exp_p$ 定义在整个 $T_pM$ 上；
4. 任一（等价地，存在一个）$p\in M$ 的闭有界子集都是紧的（Heine–Borel 性质）。

此外，若上述任一条成立，则对任意 $p,q\in M$ 存在连接它们的极小测地线 $\gamma$，即 $L(\gamma)=d(p,q)$。

**依赖的概念**：测地线完备、度量完备、指数映射、极小测地线、Heine–Borel 性质。

## 思考过程

四个条件的循环证明思路各有侧重。

"(1)$\Rightarrow$(2)"：若一条测地线只能延伸到有限时刻 $b$，那么当 $t\to b^-$ 时 $\gamma(t)$ 因速度恒长而是 Cauchy 列，度量完备保证它收敛到某点 $q$；于是用 $q$ 处的测地线方程可以再"接长"一段，与极大性矛盾。

"(2)$\Leftrightarrow$(3)"是定义层面的直接翻译：$\exp_p$ 定义在整个 $T_pM$ 上 $\iff$ 从 $p$ 出发的每条测地线可无限延伸。

"(3)$\Rightarrow$ 极小测地线存在"是核心：在切空间中取定半径 $\epsilon$ 的紧球面，用距离函数的连续性找到让剩余距离最小的方向 $v_0$，再证明沿 $v_0$ 的径向测地线一路都是最短的。

"(4)$\Rightarrow$(1)"：Cauchy 列必落在某个闭球中，Heine–Borel 使其紧，紧空间中 Cauchy 列收敛。"(3)$\Rightarrow$(4)"用 $\exp_p$ 的连续性与球面紧性把闭球拉回切空间的闭球，从而紧。

## 证明过程

**步骤 1：记号与基本事实。**

$M$ 连通使 $d$ 有限。测地线总可取单位速度参数化，$L(\gamma|_{[a,b]})=b-a$。对 $v\in T_pM$，记 $\gamma_v(t)=\exp_p(tv)$。

**步骤 2：$(2)\Rightarrow(3)$。**

取 $p$，对任意 $v\in T_pM$，测地线 $\gamma_v$ 在 $0$ 附近有定义；测地线完备意味着可延拓到全 $\mathbb R$，故 $\exp_p(v)=\gamma_v(1)$ 有定义。于是 $\exp_p$ 定义在整个 $T_pM$ 上。

**步骤 3：$(3)\Rightarrow(1)$之前的引理——极小测地线的存在。**

设 $\exp_p$ 定义于全 $T_pM$，$q\in M$，$r=d(p,q)>0$。取 $\epsilon<\min\{r,\ \text{normal radius at }p\}$，则曲面

$$
S_\epsilon=\exp_p\{v\in T_pM:|v|=\epsilon\}
$$

是紧集（球面 $\{|v|=\epsilon\}$ 紧，$\exp_p$ 连续）。函数 $x\mapsto d(x,q)$ 在 $S_\epsilon$ 上连续，故在 $y=\exp_p(v_0)$（$|v_0|=\epsilon$）处取得最小值。

证明 $d(y,q)=r-\epsilon$：任意连接 $p,q$ 的曲线必与 $S_\epsilon$ 相交于某点 $z$，其长度 $\ge \epsilon+d(z,q)\ge\epsilon+d(y,q)$，取下确界得 $r\ge\epsilon+d(y,q)$；又由三角不等式 $d(y,q)\ge r-d(p,y)\ge r-\epsilon$。故 $d(y,q)=r-\epsilon$。

**步骤 4：径向测地线是最短的。**

断言对 $0\le t\le\epsilon$，$d(p,\gamma_{v_0}(t))=t$。已知 $d(p,\gamma(t))\le t$；若对某 $t_1<\epsilon$ 有 $d(p,\gamma(t_1))<t_1$，则由 $\gamma(t_1)$ 到 $y$ 沿径向测地线的长度为 $\epsilon-t_1$（因 $\gamma$ 依弧长参数），于是存在长度 $<t_1+(\epsilon-t_1)=\epsilon$ 的曲线从 $p$ 到 $y$，与 $d(p,y)=\epsilon$ 矛盾。故在 $[0,\epsilon]$ 上 $\gamma_{v_0}$ 极小。

**步骤 5：迭代延伸到 $q$。**

把步骤 3–4 的论证应用于以 $y$ 为起点、终点 $q$、距离 $r-\epsilon$ 的情形（若 $r-\epsilon>0$），得到 $\gamma_{v_0}$ 的一段延长仍是极小。重复此过程（每步推进至少 $\epsilon$，总长有限 $r$，故至多 $\lceil r/\epsilon\rceil$ 步），把极小测地线段逐段拼接，最终得到连接 $p,q$ 的、长度为 $r$ 的测地线 $\gamma$。拼接处在两段都是测地线且切向一致，故整体为测地线，且 $L(\gamma)=r=d(p,q)$，即极小。

**步骤 6：$(3)\Rightarrow(4)$。**

由步骤 3–5，$\exp_p$ 是满射，且 $d(p,\exp_p v)\le|v|$。反之对任意 $x$，存在极小测地线给出 $v$ 使 $\exp_p v=x$ 且 $|v|=d(p,x)$。于是

$$
\exp_p\big(\overline{B(0,R)}\big)=\overline{B(p,R)}^{\,\text{（在 $M$ 中）}},
$$

且 $\overline{B(0,R)}$ 紧，$\exp_p$ 连续，故闭球 $\overline{B(p,R)}$ 紧。闭有界集含于某个 $\overline{B(p,R)}$ 中，是紧集的闭子集，从而紧。

**步骤 7：$(4)\Rightarrow(1)$。**

设 $(x_n)$ 是 Cauchy 列。则 $(x_n)$ 有界，即含于某闭球 $\overline{B(p,R)}$ 中；由 (4) 该球紧，紧度量空间中 Cauchy 列收敛，故 $(M,d)$ 完备。

**步骤 8：$(1)\Rightarrow(2)$。**

设 $\gamma:[0,b)\to M$ 是极大测地线，$|\dot\gamma|=1$，设 $b<\infty$。对 $t_n\nearrow b$，

$$
d(\gamma(t_n),\gamma(t_m))\le|t_n-t_m|\to0,
$$

故 $(\gamma(t_n))$ 是 Cauchy 列，由度量完备收敛到某 $q\in M$。取 $q$ 处的法坐标邻域 $U$ 并设 $\exp_q$ 在 $B(0,\delta)$ 上为微分同胚。当 $t_n$ 充分接近 $b$ 时 $\gamma(t_n)\in U$，写 $\gamma(t_n)=\exp_q(w_n)$，$|w_n|$ 有界；由 $\exp_q$ 局部可逆得 $w_n\to w$。定义 $\tilde\gamma(t)=\exp_q((t-b)w/|w|)$（$t>b$ 附近）并与 $\gamma$ 在 $t=b$ 处拼接。由于 $t=b$ 处 $\gamma(b)=q$ 且速度与拼接速度一致（由 $\gamma$ 的极限方向与 $w$ 一致），拼接后的曲线是 $[0,b+\delta')$ 上的测地线，与 $\gamma$ 极大矛盾。故 $b=\infty$；同理左端 $-\infty$。测地线完备成立。

由 2–8 的循环，四条件等价；极小测地线的存在性由步骤 3–5 在条件 (3)（即任一等价条件）下给出。$\square$

**推论**：完备黎曼流形上，任意两点的距离由连接它们的极小测地线实现；且 $d$ 与 $(M,g)$ 的拓扑相容。

## 相关条目

- [Bonnet-Myers定理](./Bonnet-Myers定理.md)：以 Hopf-Rinow 保证的极小测地线存在性为起点，用第二变分导出直径估计。
- [Cartan-Hadamard定理](./Cartan-Hadamard定理.md)：在非正曲率的完备单连通流形上，指数映射成为整体微分同胚，依赖 Hopf-Rinow。
- [测地线与Jacobi场](./测地线与Jacobi场.md)：测地线的极大延拓与 Jacobi 场刻画共轭点，是完备性讨论的基础语言。
