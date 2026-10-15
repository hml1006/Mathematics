# Lefschetz 迹公式

> **一句话大白话**：一个映射"有多少个不动点"这种几何信息，可以完全由它在同调群上诱导的线性映射的迹算出来——迹不为零，就一定有不动点。
>
> **小例子**：$S^1$ 上的旋转 $\theta\mapsto\theta+\alpha$，在 $H_0,H_1$ 上的诱导都为恒等，故 $L(f)=1-1=0$；当 $\alpha\not\equiv0$ 时确实没有不动点。而恒等映射的 $L=1-1+1=2$，此时整个 $S^1$ 都是不动点。

## 一、定理介绍

> **前置依赖**：奇异同调群、有限单纯复形与 CW 复形、映射度与局部度、单纯逼近定理、链复形的迹与 Euler 特征

Lefschetz 迹公式由 S. Lefschetz 于 1926 年提出，是代数拓扑中最常用的计算工具之一：它把一个自映射的不动点计数（带符号的局部贡献）与其在同调上的线性代数量——Lefschetz 数 $L(f)$——等同起来。

它是 Atiyah-Bott 不动点定理、Lefschetz 不动点定理以及（作为其代数几何与算术推广的）Grothendieck-Lefschetz 迹公式的原型。在模形式理论中，把公式用于模曲线 $X_0(N)$ 上的 Hecke 对应 $T_m$，即得经典的 **Eichler-Selberg 迹公式**，从而可用类数、除子和等初等数据计算 Hecke 算子在尖点形式空间 $S_k(\Gamma_0(N))$ 上的迹。这正是本条目出现在"椭圆曲线与模形式"层级中的原因。

## 二、原理思路

关键想法是：**不动点只能出现在被映射"固定"的单纯形上，而链群层面的迹自动记录了这些贡献。**

1. 先用单纯逼近把 $f$ 换成有限单纯复形上的单纯映射，并用 Hopf 迹公式把"同调上的交错迹"换成"链群上的交错迹"。
2. 单纯映射在链群上的矩阵很稀疏：对角元非零当且仅当该单纯形被映射到自身（保持或反转定向）。
3. 若 $f$ 无不动点，细分后可使每个单纯形与自己的像不相交，于是所有对角元为 $0$，$L(f)=0$。
4. 一般情形下把每个非退化不动点用互不相交的小邻域隔离，逐点计算局部贡献（局部度），求和即得结论。

## 三、定理的严格表述

设 $X$ 为有限 CW 复形（或紧可三角化空间），$f:X\to X$ 连续。定义 **Lefschetz 数**
$$L(f)=\sum_{i\ge0}(-1)^i\,\mathrm{tr}\Big(f_*:H_i(X;\mathbb{Q})\to H_i(X;\mathbb{Q})\Big),$$
其中只有有限多个 $H_i$ 非零，故为有限和。

**定理（Lefschetz 迹公式）**：设不动点集 $\mathrm{Fix}(f)=\{x\in X:f(x)=x\}$ 有限，且每个不动点 $p$ 非退化（即 $1-f$ 在 $p$ 的某邻域内为局部同胚，$\deg\big((1-f)|_{\partial U_p}\big)\ne0$）。则
$$L(f)=\sum_{p\in\mathrm{Fix}(f)}\mathrm{ind}_p(f),\qquad \mathrm{ind}_p(f)=\deg\big((1-f)\big|_{\partial U_p}\big)\in\mathbb{Z},$$
其中 $U_p$ 是只含唯一不动点 $p$ 的小球邻域，$\mathrm{ind}_p(f)$ 称为 $f$ 在 $p$ 的局部指标；当 $f$ 在 $p$ 附近为（定向）局部同胚时 $\mathrm{ind}_p(f)=\pm1$。

**推论（Lefschetz 不动点定理）**：若 $L(f)\ne0$，则 $f$ 必有不动点。特别地，若 $X$ 是可缩紧空间（如 $D^n$）则 $L(f)=1$，得到 Brouwer 不动点定理。

**对应用例（Eichler-Selberg 迹公式的来源）**：取 $X=X_0(N)$ 为模曲线、$f=T_m$ 为第 $m$ 个 Hecke 对应（一个"多值映射"，即 $X_0(N)$ 上的对应）。在 $H^0,H^1,H^2$ 上计算迹（对应 Eisenstein 部分与尖点部分），不动点由椭圆点、CM 点与尖点给出，即得到 $\mathrm{tr}\big(T_m\mid S_k(\Gamma_0(N))\big)$ 的显式公式。

## 四、证明过程

**步骤 1：Hopf 迹公式（链上迹 = 同调上迹）**

设 $K$ 为有限单纯复形，$f:K\to K$ 为单纯映射。则 $f$ 诱导链映射 $f_\#:C_i(K;\mathbb{Q})\to C_i(K;\mathbb{Q})$，并且
$$\sum_i(-1)^i\mathrm{tr}\big(f_\#\mid C_i\big)=\sum_i(-1)^i\mathrm{tr}\big(f_*\mid H_i\big)=L(f).$$
证明：$C_i(K;\mathbb{Q})$ 有限维。对有限维链复形的自同态 $\phi$ 有恒等式 $\sum_i(-1)^i\mathrm{tr}(\phi\mid C_i)=\sum_i(-1)^i\mathrm{tr}(\phi\mid H_i)$——把 $C_i$ 分解为 $\mathrm{im}\,\partial_{i+1}$、$\ker\partial_i\cap(\mathrm{im}\partial_{i+1})^{\perp}$ 与 $H_i$ 的代表的直和（或对复形长度作归纳，利用 $\phi\partial=\partial\phi$），每层的迹在同调层与边界层间相消，即得。

**步骤 2：无不动点的情形**

设 $\mathrm{Fix}(f)=\varnothing$。由单纯逼近定理（必要时细分），可设 $f$ 为单纯映射且对每个单纯形 $\sigma$ 有 $f(\sigma)\cap\sigma=\varnothing$：否则 $|f(\sigma)\cap\sigma|$ 上的某个点近似给出不动点，而由 $X$ 紧与 $f$ 连续可排除这一可能（取有限次细分即可）。此时对每个 $i$-单纯形 $\sigma$，$f_\#(\sigma)$ 是若干 $i$-单纯形的整线性组合，而组合中不可能出现 $\sigma$ 本身（因 $f(\sigma)\cap\sigma=\varnothing$），故 $\mathrm{tr}(f_\#\mid C_i)=0$。由步骤 1，$L(f)=0$。这证明了"$L(f)\ne0\Rightarrow$ 存在不动点"。

**步骤 3：隔离不动点（Lefschetz 数的加性）**

设不动点有限且非退化。取互不相交的小闭球邻域 $U_p$（每个 $U_p$ 只含不动点 $p$），令 $U=\bigcup_pU_p$、$A=K\setminus U^\circ$。对 $(K,A)$ 与其子复形用相对同调的长正合序列（Mayer-Vietoris 型分解），并注意 $A$ 上 $f$ 无不动点（由步骤 2 的论证 $L(f|_A)=0$），可得
$$L(f)=L\big(f\mid_A\big)+L\big(f\mid_U\ \mathrm{rel}\ \partial U\big)=\sum_p L\big(f\mid_{U_p}\ \mathrm{rel}\ \partial U_p\big).$$
（逐次对每个 $U_p$ 重复同一分解，即得最后的求和形式；相对 Lefschetz 数用相对同调 $H_i(U_p,\partial U_p;\mathbb{Q})$ 的诱导迹定义。）

**步骤 4：计算单个非退化不动点的局部贡献**

把 $U_p$ 取成 $n$ 维球（在充分细的三角剖分下为其子复形），球内 $f$ 只有一个不动点 $p$。设 $n=\dim X$（其它维数的情形同理，此时 $U_p$ 用 $n$ 维球并对低维同调取 $0$）。由于 $p$ 非退化，$1-f$ 在 $\partial U_p\cong S^{n-1}$ 上处处不为零，于是
$$g:=1-f:\partial U_p\to\mathbb{R}^n\setminus\{0\}$$
有良定义的度 $\deg(g)$（局部度）。球对球面的相对同调只有一处非零：$H_n(U_p,\partial U_p;\mathbb{Q})\cong\mathbb{Q}$，生成元为基本类 $[U_p,\partial U_p]$。链层面的计算（把 $f$ 与 $\mathrm{id}$ 的链映射之差在上述生成元上取值，并用 $g$ 在边界球面上的度表示边界映射的对应系数）给出
$$L\big(f\mid_{U_p}\ \mathrm{rel}\ \partial U_p\big)=\deg(g)=\deg\big((1-f)\big|_{\partial U_p}\big)=:\mathrm{ind}_p(f).$$
（符号约定由基本类的定向与 $n$ 的奇偶决定；若采用与 $L(f)$ 中基本类一致的不定向约定，则上式直接成立。）

**步骤 5：求和**

由步骤 3、4 得
$$L(f)=\sum_{p\in\mathrm{Fix}(f)}L\big(f\mid_{U_p}\ \mathrm{rel}\ \partial U_p\big)=\sum_{p\in\mathrm{Fix}(f)}\mathrm{ind}_p(f),$$
证毕。

## 五、应用与意义

1. **Lefschetz 不动点定理**：$L(f)\ne0$ 保证不动点存在。$D^n$ 上 $L(f)=1$，立即得到 Brouwer 不动点定理；对紧 Lie 群作用、球面自映射等均有直接推论。

2. **Atiyah-Bott 推广**：把孤立不动点推广到不动点子流形，得到
$$L(f)=\sum_{F\subseteq X^f}\int_F\frac{\mathrm{ch}_f(\nu_F)}{\mathrm{euler}(\nu_F)}$$
型的局部化公式，成为等变指标理论、Duistermaat-Heckman 局部化与 Bott 留数的基石。

3. **模形式中的应用（Eichler-Selberg）**：对模曲线 $X_0(N)$ 上的 Hecke 对应 $T_m$ 应用迹公式，$H^1$ 部分的迹即 $\mathrm{tr}(T_m\mid S_k(\Gamma_0(N)))$，而不动点（椭圆点、CM 点、尖点）与 Eisenstein 部分给出显式的数论修正项。这使 Hecke 算子的迹可用 Hurwitz 类数、除子和等纯粹数论数据计算，是模形式理论的基本工具，也是本层级（椭圆曲线与模形式）中该定理的核心用途。

4. **算术推广**：把同调换成 étale 上同调、把 $f$ 换成 Frobenius 对应，即得 Grothendieck-Lefschetz 迹公式 $\#X(\mathbb{F}_q)=\sum(-1)^i\mathrm{tr}(\mathrm{Frob}\mid H^i_c)$，是 Weil 猜想的证明框架（见 Lefschetz-Grothendieck 迹公式）。

## 课堂问答

**老师**：请写出 Lefschetz 数 $L(f)$ 的定义，并说明为什么它能数不动点。

**学生**：先给结论：$L(f)=\sum_{i\ge0}(-1)^i\,\mathrm{tr}\big(f_*:H_i(X;\mathbb{Q})\to H_i(X;\mathbb{Q})\big)$，当不动点有限且非退化时 $L(f)=\sum_{p\in\mathrm{Fix}(f)}\mathrm{ind}_p(f)$，其中 $\mathrm{ind}_p(f)=\deg\big((1-f)|_{\partial U_p}\big)$ 是局部指标（在局部同胚处为 $\pm1$）。它能数不动点，是因为 Hopf 迹公式把同调上的交错迹换成链群上的交错迹，而单纯映射在链群上的对角元非零当且仅当该单纯形被映到自身——即贡献一个不动点。

**老师（追问）**：证明里"无不动点则 $L(f)=0$"是怎么做到的？非退化假设又用在哪？

**学生**：若无不动点，由单纯逼近（必要时细分）可让每个单纯形与自身像不相交，于是所有链层对角元为 $0$，$L(f)=0$；反过来 $L(f)\ne0$ 就保证存在不动点（Lefschetz 不动点定理）。非退化假设用在隔离不动点那步：把每个不动点用互不相交的小球邻域 $U_p$ 包住，$A=X\setminus U^\circ$ 上 $f$ 无不动点使 $L(f|_A)=0$，再用相对同调的长正合序列分解得 $L(f)=\sum_p L(f|_{U_p}\ \mathrm{rel}\ \partial U_p)$，而单个贡献等于 $\deg((1-f)|_{\partial U_p})$。常见误区：以为公式只在有限复形上成立——其实 CW 复形、紧可三角化空间均可。

**老师（拓展）**：它在模形式与算术几何里有什么推广？

**学生**：把公式用于模曲线 $X_0(N)$ 上的 Hecke 对应 $T_m$，$H^1$ 部分的迹即为 $\mathrm{tr}(T_m\mid S_k(\Gamma_0(N)))$，不动点（椭圆点、CM 点、尖点）与 Eisenstein 部分给出显式修正项，这就是 Eichler–Selberg 迹公式；再把它换成 étale 上同调、$f$ 换成 Frobenius，即得 Grothendieck–Lefschetz 迹公式 $\#X(\mathbb{F}_q)=\sum_i(-1)^i\mathrm{tr}(\mathrm{Frob}\mid H^i_c)$，是 Weil 猜想的证明框架。
