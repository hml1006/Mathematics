# Rellich–Kondrachov 紧嵌入定理

> **一句话大白话**：在有界区域上，Sobolev 空间 $W^{k,p}$ 中的有界列不仅能在稍弱的 $L^q$ 空间里抽出收敛子列，而且收敛是强的——比连续嵌入"好一档"；代价是只能退化一点点指数（$q<p^*$）。
>
> **小例子**：$\Omega\subset\mathbb R^3$ 有界，$\|u_m\|_{H^1}\le1$，则 $H^1(\Omega)\hookrightarrow\hookrightarrow L^q(\Omega)$ 对一切 $q<6$ 成立，故可抽出在 $L^4(\Omega)$ 中强收敛的子列；但到临界指数 $q=6$ 时紧性失效（例如集中于一点的"气泡"序列）。

## 介绍

Sobolev 嵌入定理告诉我们 $W^{k,p}(\Omega)\hookrightarrow L^q(\Omega)$ 是**连续**嵌入，即 $\|u\|_q\le C\|u\|_{W^{k,p}}$。连续嵌入只把有界列变成有界列，不足以在非线性问题取极限时把乘积 $u_m v_m$ 的极限算出来。Rellich–Kondrachov 定理给出的是**紧**嵌入：把一个 Sobolev 有界列"升级"为一个在 $L^q$ 中**强收敛**的子列。

紧嵌入在 PDE 中无处不在：椭圆方程的能量泛函的弱下半连续性与极小元存在性（变分法直接方法）、Galerkin 方法取极限、特征值问题（$-\Delta$ 的紧预解式给出离散谱）、非线性项在弱收敛下的通过性，都依赖它。Rellich（1930）与 Kondrachov（1945）分别给出了 $p=2$ 与一般 $p$ 的情形。

定理的边界情形说明了"为什么只能 $q<p^*$"：临界指数 $p^*$ 处嵌入不紧，因为临界指数的尺度不变性允许测度集中。这一点与 Sobolev 不等式的最优常数、集中紧性原理（concentration compactness）直接相关。

## 分析

**前置依赖**：Sobolev 空间与弱导数、Sobolev 嵌入（Gagliardo–Nirenberg–Sobolev）不等式、Morrey 不等式、Fréchet–Kolmogorov 紧性准则、Minkowski不等式、Arzelà–Ascoli 定理、有界区域的延拓（反射）技巧。

**定理内容**：设 $\Omega\subset\mathbb R^n$ 是有界区域，边界 Lipschitz（例如 $C^1$ 或分段光滑），$1\le p<\infty$，$k\ge1$ 是整数，并记临界指数

$$p^*_k=\frac{np}{n-kp}\quad(kp<n).$$

则有紧嵌入：

**(1)** 若 $kp<n$：$\displaystyle W^{k,p}(\Omega)\hookrightarrow\hookrightarrow L^q(\Omega)$ 对一切 $1\le q<p^*_k$ 成立。

**(2)** 若 $kp=n$：$\displaystyle W^{k,p}(\Omega)\hookrightarrow\hookrightarrow L^q(\Omega)$ 对一切 $1\le q<\infty$ 成立。

**(3)** 若 $kp>n$：$\displaystyle W^{k,p}(\Omega)\hookrightarrow\hookrightarrow C^0(\overline{\Omega})$（关于上确界范数）成立。

**临界情形不紧**：当 $kp<n$ 时，连续嵌入 $W^{k,p}(\Omega)\hookrightarrow L^{p^*_k}(\Omega)$ **不是**紧的。

**证明策略**：核心是"Sobolev 嵌入给 $L^{p^*}$ 中的一致有界 + 平移估计给 $L^p$ 中的紧性 + 插值把两者拼成 $L^q$ 中的紧性"。

1. 对 $W^{1,p}$ 中的函数证明平移估计 $\|u(\cdot+h)-u\|_p\le|h|\|\nabla u\|_p$（沿直线的微积分基本定理 + Minkowski 不等式），从而对延拓后的族使用 Fréchet–Kolmogorov 得到 $L^p$ 中的相对紧性；
2. 由 Sobolev 嵌入得到 $L^{p^*}$ 中的一致有界；
3. 用 $L^p$ 范数的对数凸性（Riesz–Thorin 型插值）把"$L^p$ 中收敛 + $L^{p^*}$ 中有界"提升为"$L^q$ 中收敛"（$p\le q<p^*$）；$q<p$ 的情形由 $\Omega$ 有界直接得到。

## 思考过程

先想清楚**为什么有界区域上会有额外的紧性**。全空间上平移一个固定非零函数，$L^p$ 范数不变，显然不紧；有界区域"困住"了函数，不许它跑到无穷远，于是 (FK3) 自动满足，唯一需要验证的是 (FK2) 平移的等度连续性。而 Sobolev 范数恰好控制平移：$W^{1,p}$ 中的函数沿几乎每条直线都绝对连续（ACL 性质），于是

$$u(x+h)-u(x)=\int_0^1 h\cdot\nabla u(x+th)\,dt .$$

对两边取 $L^p$ 范数，把 $\nabla u(x+th)$ 的 $L^p$ 范数通过变量替换看出来等于 $\|\nabla u\|_p$，再用 Minkowski 积分不等式把积分搬到范数之外，得到 $\|u(\cdot+h)-u\|_p\le|h|\,\|\nabla u\|_p$，右端对全族一致地被 $|h|$ 控制——这正是 (FK2)。所以 $W^{1,p}$ 的有界族在 $L^p$ 中相对紧。

但我们需要的是 $L^q$（$q$ 可能大于 $p$）中的紧性。$L^p$ 里的强收敛本身不够，因为 $q>p$ 时 $\|\cdot\|_q$ 不被 $\|\cdot\|_p$ 控制（区域有界时只对 $q<p$ 方向有控制）。补救办法是**插值**：若一族在 $L^p$ 中"强收敛"而在 $L^{p^*}$ 中"一致有界"，则对任何介于两者之间的 $q$ 也是强收敛的。原因是 $L^q$ 范数是 $L^p$ 与 $L^{p^*}$ 范数的对数凸函数：

$$\|v\|_q\le\|v\|_p^{\theta}\|v\|_{p^*}^{1-\theta},\qquad \frac1q=\frac{\theta}{p}+\frac{1-\theta}{p^*}.$$

于是对 $u_j-u_k$：$L^p$ 范数趋于 $0$（Cauchy），$L^{p^*}$ 范数一致有界，故 $L^q$ 范数趋于 $0$：序列在 $L^q$ 中 Cauchy，$L^q$ 完备，收敛。

**临界指数为什么失效**？因为 $p^*$ 是尺度不变的指数，允许把质量"挤"到一个点上而不改变 $L^{p^*}$ 范数。

把 $q<p$ 的情形也补上：$\Omega$ 有界时 $\|v\|_{L^q(\Omega)}\le|\Omega|^{1/p-1/q}\|v\|_{L^p(\Omega)}$，故 $L^p$ 紧性自动给出 $L^q$ 紧性。

## 证明过程

为把技术细节降到最低，先对 $W_0^{1,p}(\Omega)$ 完整证明 $k=1$、$kp<n$ 的情形（零延拓使一切都在 $\mathbb R^n$ 上进行），再说明如何去掉"零边界"限制并推广到一般 $k$ 与临界/超临界情形。

**步骤 1：$W^{1,p}$ 函数的平移估计。**

设 $u\in W^{1,p}(\mathbb R^n)$ 紧支。由 Sobolev 空间的 ACL 性质，$u$ 沿几乎每条平行于坐标轴的直线绝对连续，且沿该直线的导数就是方向导数。故对几乎一切 $x$ 与每个 $h\in\mathbb R^n$，

$$u(x+h)-u(x)=\int_0^1 h\cdot\nabla u(x+th)\,dt .$$

取绝对值、用 Minkowski 积分不等式（把 $L^p$ 范数搬进积分号）：

$$\|u(\cdot+h)-u\|_p\le\int_0^1\big\|h\cdot\nabla u(\cdot+th)\big\|_p\,dt\le|h|\int_0^1\|\nabla u(\cdot+th)\|_p\,dt=|h|\,\|\nabla u\|_p ,$$

最后一步用了平移不改变 $L^p$ 范数。

**步骤 2：零延拓后使用 Fréchet–Kolmogorov。**

设 $(u_j)\subseteq W_0^{1,p}(\Omega)$ 满足 $\|u_j\|_{W^{1,p}(\Omega)}\le M$。把 $u_j$ 零延拓到 $\mathbb R^n$，记为 $\tilde u_j\in W^{1,p}(\mathbb R^n)$，则 $\tilde u_j$ 都支撑在同一个大球 $B(0,R)$ 内（$R$ 只依赖 $\Omega$），且 $\|\tilde u_j\|_{W^{1,p}(\mathbb R^n)}\le C M$。于是：

- $\|\tilde u_j\|_p\le CM$，一致有界；
- 由步骤 1，$\|\tilde u_j(\cdot+h)-\tilde u_j\|_p\le|h|\,\|\nabla\tilde u_j\|_p\le CM|h|$，右端与 $j$ 无关；
- 所有 $\tilde u_j$ 支撑在固定的 $B(0,R)$ 内，故 $\|\tilde u_j\|_{L^p(|x|>R')}=0$ 对 $R'>R$ 成立。

三条判据齐备，由 Fréchet–Kolmogorov 紧性准则，$(\tilde u_j)$ 在 $L^p(\mathbb R^n)$ 中相对紧。于是存在子列（仍记 $j$）与 $v\in L^p(\mathbb R^n)$ 使 $\tilde u_j\to v$ 于 $L^p(\mathbb R^n)$；由于 $v$ 必然也支撑在 $B(0,R)$ 内，把 $v$ 限制到 $\Omega$ 得 $u:=v|_\Omega\in L^p(\Omega)$，且

$$\|u_j-u\|_{L^p(\Omega)}=\|\tilde u_j-v\|_{L^p(\mathbb R^n)}\to0 .$$

**步骤 3：插值提升到 $L^q$（$p\le q<p^*$）。**

由 Sobolev 嵌入定理（Gagliardo–Nirenberg–Sobolev 不等式），存在 $C_S$ 使

$$\|w\|_{L^{p^*}(\Omega)}\le C_S\|w\|_{W^{1,p}_0(\Omega)}\qquad\Big(p^*=\frac{np}{n-p}\Big),$$

故对一切 $j$：$\|u_j\|_{L^{p^*}}\le C_S M$。设 $p\le q<p^*$，取 $\theta\in(0,1]$ 使

$$\frac1q=\frac{\theta}{p}+\frac{1-\theta}{p^*},$$

即 $\theta=\dfrac{1/p-1/q}{1/p-1/p^*}$。由 $L^p$ 范数的对数凸性（对 $|v|^\theta\cdot|v|^{1-\theta}$ 用 Hölder 不等式）得

$$\|w\|_{L^q}\le\|w\|_{L^p}^{\theta}\,\|w\|_{L^{p^*}}^{1-\theta}.$$

对上式取 $w=u_j-u_k$（它在 $W^{1,p}_0$ 中范数 $\le2M$，故 $L^{p^*}$ 范数 $\le2C_SM$），

$$\|u_j-u_k\|_{L^q}\le\|u_j-u_k\|_{L^p}^{\theta}\,(2C_SM)^{1-\theta}\xrightarrow[j,k\to\infty]{}0 ,$$

因为 $(u_j)$ 在 $L^p$ 中是 Cauchy 列。于是 $(u_j)$ 在 $L^q(\Omega)$ 中是 Cauchy 列；由 Riesz–Fischer 定理 $L^q$ 完备，故 $(u_j)$ 在 $L^q$ 中收敛。由于上面的推理对 $W^{1,p}_0$ 中**任意**有界序列都适用，得到 $W^{1,p}_0(\Omega)\hookrightarrow\hookrightarrow L^q(\Omega)$。

**步骤 4：$1\le q<p$ 的情形。**

因 $\Omega$ 有界，对 $w\in L^p(\Omega)$ 由 Hölder 不等式

$$\|w\|_{L^q(\Omega)}\le|\Omega|^{\frac1q-\frac1p}\|w\|_{L^p(\Omega)} ,$$

故步骤 2 得到的 $L^p$ 收敛直接蕴含 $L^q$ 收敛。结合步骤 3，对一切 $1\le q<p^*$ 都有紧嵌入，这就完成了 $k=1$ 情形 (1) 的证明。

**步骤 5：去掉零边界条件——延拓算子。**

设 $\Omega$ 有 Lipschitz 边界。存在有界线性**延拓算子** $E:W^{1,p}(\Omega)\to W^{1,p}(\mathbb R^n)$（由边界附近的局部反射与有限覆盖上的单位分解拼成），满足 $\|Eu\|_{W^{1,p}(\mathbb R^n)}\le C\|u\|_{W^{1,p}(\Omega)}$ 且 $Eu$ 支撑在一个固定的球内。对 $W^{1,p}(\Omega)$ 中的有界列作延拓，重复步骤 2 至步骤 4 即得 $W^{1,p}(\Omega)\hookrightarrow\hookrightarrow L^q(\Omega)$。这就证明了 $k=1$ 时 (1) 的一般形式。

**步骤 6：一般 $k$ 与临界、超临界情形。**

**(1) 的 $k\ge2$**：$W^{k,p}(\Omega)\subseteq W^{1,p}(\Omega)$ 连续（$k\ge1$；由弱导数的高阶到一阶的控制），故 $W^{k,p}$ 的有界列在 $W^{1,p}$ 中有界，由步骤 5 在 $L^p$ 中有收敛子列；另一方面 $W^{k,p}\hookrightarrow L^{p^*_k}$ 连续给出 $L^{p^*_k}$ 中的一致有界。用步骤 3 的插值（把 $p^*$ 换成 $p^*_k$）即得 $L^q$（$p\le q<p^*_k$）中的收敛；$q<p$ 仍由区域有界得到。

**(2) $kp=n$**：Sobolev 嵌入给出 $W^{k,p}(\Omega)\hookrightarrow L^r(\Omega)$ 对一切 $r<\infty$ 连续。取任意 $q\in[1,\infty)$，再取 $r>\max\{p,q\}$。$W^{k,p}$ 的有界列在 $W^{1,p}$ 中有界，故在 $L^p$ 中有收敛子列（步骤 5），同时在 $L^r$ 中一致有界；用插值（介于 $p$ 与 $r$）得 $L^q$ 中的收敛。故 (2) 成立。

**(3) $kp>n$**：由 Morrey 不等式，$W^{k,p}(\Omega)$ 连续嵌入 Hölder 空间 $C^{0,\alpha}(\overline\Omega)$（$\alpha=k-n/p$ 的小数部分，或临界情形下任意 $\alpha<1$）。延拓到 $\mathbb R^n$ 后，一个 $W^{k,p}$ 有界列在 $\overline\Omega$ 上一致有界且一致 Hölder 连续，因而等度连续。由 Arzelà–Ascoli 定理，存在子列在 $\overline\Omega$ 上一致收敛，即收敛于 $C^0(\overline\Omega)$（上确界范数）。这就给出 $W^{k,p}(\Omega)\hookrightarrow\hookrightarrow C^0(\overline\Omega)$，从而也紧嵌入到一切 $L^q(\Omega)$。

**步骤 7：临界指数不紧。**

设 $kp<n$。取非零的 $\phi\in C_c^\infty(\mathbb R^n)$，定义

$$u_j(x)=j^{\frac{n-p}{p}}\phi(jx)\qquad(j\to\infty).$$

直接计算（变量替换 $y=jx$）：$\|u_j\|_{L^p}=j^{-1}\|\phi\|_{L^p}\to0$，$\|\nabla u_j\|_{L^p}=\|\nabla\phi\|_{L^p}$，且临界缩放给出

$$\|u_j\|_{L^{p^*}}=\|\phi\|_{L^{p^*}}>0\qquad\text{对一切 }j .$$

故 $\|u_j\|_{W^{1,p}}\le\|\phi\|_{W^{1,p}}$ 一致有界，且因 $\|u_j\|_{L^p}\to0$ 而有 $u_j\rightharpoonup0$ 于 $L^p$（从而于 $W^{1,p}$：对每个 $\varphi\in C_c^\infty$，由弱导数的定义 $\int \partial_i u_j\,\varphi=-\int u_j\,\partial_i\varphi$，而 $\|u_j\|_p\to0$、$\partial_i\varphi$ 有界，故 $\int\partial_i u_j\,\varphi\to0$，即 $\partial_i u_j\rightharpoonup0$ 于 $L^p$）。若某子列在 $L^{p^*}$ 中强收敛，其极限必为弱极限 $0$，这将迫使 $\|u_j\|_{L^{p^*}}\to0$，与上式矛盾。故 $W^{1,p}(\Omega)\hookrightarrow L^{p^*}(\Omega)$ 不紧（把 $\phi$ 支撑在 $\Omega$ 内部的小球内即可在区域上实现该构造）。$\square$

**注**：定理中"$q<p^*_k$ 严格"是必需的；把 $q$ 取到 $p^*_k$ 时只能得到连续嵌入。而有界区域这一假设保证 (FK3)，无界区域上若不附加衰减条件，紧嵌入一般不成立。

## 相关条目

- [Sobolev嵌入定理](./Sobolev嵌入定理.md)：给出连续嵌入与临界指数 $p^*$，是本定理插值步骤的前提。
- [Sobolev空间定义](./Sobolev空间定义.md)：弱导数、$W^{k,p}$ 范数与 ACL 性质的来源。
- [Fréchet-Kolmogorov紧性准则](./Fréchet-Kolmogorov紧性准则.md)：本定理把紧性化归为该准则的三条判据。
