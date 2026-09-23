# Lefschetz-Verdier 不动点公式

> **一句话大白话**：经典的"不动点个数 = 上同调迹"在代数几何里要靠相交理论来兑现：把映射画成 $X\times X$ 里的"图"，不动点就是这张图与对角线的交点；Lefschetz 数等于这两个闭子概形（带系数层）的相交数，而相交数只在固定点集上非零——这就是 Lefschetz-Verdier 公式。
>
> **小例子**：$\mathbb{F}_q$ 上的 Frobenius 图 $\Gamma_\phi$ 与对角线 $\Delta$ 的交点恰是 $\mathbb{F}_q$-有理点，且 Frobenius 在切空间上微分为零，故局部相交重数退化为茎 $\mathcal{F}_x$ 上的迹，于是 $\#X(\mathbb{F}_q)=\sum_i(-1)^i\mathrm{tr}(\phi^*\mid H^i_c(\bar X,\mathcal{F}))$——这正是 Grothendieck-Lefschetz 迹公式。

## 一、定理介绍

> **前置依赖**：层与层上同调、Poincare对偶定理、Künneth公式、Serre相交公式

Lefschetz-Verdier 不动点公式（SGA 5, Exposé III，Verdier）是 Grothendieck-Lefschetz 迹公式的"母版"。核心想法是把一个**对应**（correspondence）
$$
X\xleftarrow{\ c_1\ }Z\xrightarrow{\ c_2\ }X
$$
（$\dim Z=\dim X$，$c_1,c_2$ 固有）画成乘积 $X\times_kX$ 中的闭子概形 $\Gamma_c=(c_1,c_2)(Z)$，则对应的 Lefschetz 数
$$
L(c,\mathcal{F})=\sum_i(-1)^i\,\mathrm{tr}\big(c^*\mid H^i_c(X,\mathcal{F})\big)
$$
等于 $\Gamma_c$ 与对角线 $\Delta$ 带系数 $\mathcal{F}\boxtimes\mathcal{F}^\vee$ 的**相交数**：
$$
L(c,\mathcal{F})=\big\langle\Gamma_c,\ \Delta\big\rangle_{\mathcal{F}} .
$$
由于 $\Gamma_c\cap\Delta$ 的支撑就是固定点集 $\mathrm{Fix}(c)$，该相交数可沿着 $\mathrm{Fix}(c)$ 局部化，得到"局部 Lefschetz 数"的求和；特别地**无不动点则 Lefschetz 数必为零**。

与"椭圆曲线与模形式"层级的 Lefschetz 迹公式对照：那里是拓扑/同调版本（相交数 = 迹），此处把同调换成构造性层系数的紧支 étale 上同调，并给出**局部因子**这一额外信息，因而更强、更适用于算术。

## 二、原理思路

三步走。

第一，**把映射变成类**。上同调是反变函子，映射 $f$ 不对 $H^*_c$ 直接作用；但若给层 $\mathcal{F}$ 配一个"传输"$\alpha:f^*\mathcal{F}\to\mathcal{F}$（算术情形取 Frobenius 相容作用），就得到自同态 $H^*_c(\alpha)\circ f^*$，其交错迹即 Lefschetz 数。对应 $c$ 同理，用 $c^*=c_{2*}\circ\alpha\circ c_1^*$ 定义。

第二，**把迹变成相交数**。Künneth 公式把 $H^*_c(X\times X,\mathcal{F}\boxtimes\mathcal{F}^\vee)$ 分解为 $H^*_c(X,\mathcal{F})\otimes H^*_c(X,\mathcal{F}^\vee)$；Poincaré 对偶给出的求值配对非退化，使每一对上同调类对应一个自同态（endomorphism）的迹。对角类 $\Delta$ 在该配对下正是"迹/求值"类，$c^*$ 的转置正是 $\Gamma_c$ 的类，于是两者相交数就是 $\mathrm{tr}(c^*)$。

第三，**把相交数局部化**。相交只在 $\mathrm{Fix}(c)$ 上有支撑，用闭浸入的局部化三角可把整体相交数拆成逐点局部项之和。正特征、非横截的交点有重数，而局部项正是 Verdier 用"迹映射"（trace map）与对偶 formalism 严格定义的，从而不必假设横截。

## 三、定理的严格表述

设 $k$ 为域，$X$ 为 $k$ 上分离有限型概形，$X$ 固有（proper）以保证 $H^i_c=H^i$ 且 $c_1,c_2$ 固有；$\mathcal{F}$ 为 $X$ 上构造性 $\bar{\mathbb{Q}}_\ell$-层，$\alpha:c_2^*\mathcal{F}\to c_1^{!}\mathcal{F}$ 为传输．记 $\Gamma_c\subset X\times_kX$ 为对应图。

**定理（Lefschetz-Verdier 不动点公式）**：
$$
L(c,\mathcal{F}):=\sum_i(-1)^i\mathrm{tr}\big(c^*\mid H^i_c(X,\mathcal{F})\big)=\big\langle\Gamma_c,\Delta\big\rangle_{\mathcal{F}},
$$
其中右端为以 $\mathcal{F}\boxtimes\mathcal{F}^\vee$ 为系数的相交数，且只依赖 $\mathrm{Fix}(c):=c_1\big(c_2^{-1}(\Delta)\big)$。

**局部形式**：存在支撑在 $\mathrm{Fix}(c)$ 上的"固定点类" $\eta_c$ 使
$$
L(c,\mathcal{F})=\int_{\mathrm{Fix}(c)}\mathrm{Tr}(\eta_c);
$$
当 $\mathrm{Fix}(c)$ 有限且各点为孤立固定点时，
$$
L(c,\mathcal{F})=\sum_{x\in\mathrm{Fix}(c)}L_x(c,\mathcal{F}),
$$
$L_x$ 称局部 Lefschetz 数。于是 $\mathrm{Fix}(c)=\emptyset\Rightarrow L(c,\mathcal{F})=0$。

**推论（Grothendieck-Lefschetz 迹公式）**：取 $k=\mathbb{F}_q$、$c=\Gamma_{\phi^n}$（绝对 Frobenius $\phi$ 的 $n$ 次幂图），则 $\mathrm{Fix}(c)=X(\mathbb{F}_{q^n})$，且因 $d\phi^n=0$ 局部因子退化为茎上的迹：
$$
\#X(\mathbb{F}_{q^n})\ \text{（带系数计数）}=\sum_{x\in X(\mathbb{F}_{q^n})}\mathrm{tr}\big(\mathrm{Frob}_x^n\mid\mathcal{F}_x\big)=\sum_i(-1)^i\mathrm{tr}\big(\phi^{n*}\mid H^i_c(\bar X,\mathcal{F})\big).
$$

## 四、证明过程

**步骤1：定义对应诱导的上同调自同态。** 因 $c_1$ 固有，存在拉回 $c_1^*:H^i_c(X,\mathcal{F})\to H^i_c(Z,c_1^*\mathcal{F})$；因 $c_2$ 固有，存在 $c_{2*}:H^i_c(Z,c_2^{!}\mathcal{F})\to H^i_c(X,\mathcal{F})$。令
$$
c^*=c_{2*}\circ H^i_c(\alpha)\circ c_1^*\ :\ H^i_c(X,\mathcal{F})\longrightarrow H^i_c(X,\mathcal{F}),
$$
这是有限维向量空间的自同态，故交错迹 $L(c,\mathcal{F})$ 良定义。

**步骤2：Künneth 分解。** 由 Künneth 公式
$$
H^n_c(X\times_kX,\ \mathcal{F}\boxtimes\mathcal{F}^\vee)\ \cong\bigoplus_{i+j=n}H^i_c(X,\mathcal{F})\otimes H^j_c(X,\mathcal{F}^\vee),
$$
右侧为有限维，且对乘积投影分别为 $c_1,c_2$ 的对应有交换性（投影公式），故 $\Gamma_c$ 的类可写成 $\sum_\nu u_\nu\otimes v_\nu$ 的像。

**步骤3：Poincaré 对偶下的迹 = 相交数。** 设 $n=\dim X$。Poincaré 对偶给出非退化配对
$$
\langle\ ,\ \rangle:H^i_c(X,\mathcal{F})\times H^{2n-i}_c(X,\mathcal{F}^\vee)\longrightarrow \bar{\mathbb{Q}}_\ell(-n),
$$
并给出"求值类" $\Delta$ 的类在 $H^{2n}_c(X\times X,\cdot)$ 中对应于该配对的迹形式 $\sum_i(-1)^i\mathrm{id}$。于是把 $\Gamma_c$ 与 $\Delta$ 都用步骤2的分解表示后相乘，逐项配对得
$$
\big\langle\Gamma_c,\Delta\big\rangle_{\mathcal{F}}=\sum_i(-1)^i\mathrm{tr}\Big(\big(\text{$\Gamma_c$ 在 $H^i_c\otimes H^{2n-i}_c$ 上的对应算子}\big)\Big)=\sum_i(-1)^i\mathrm{tr}\big(c^*\mid H^i_c(X,\mathcal{F})\big),
$$
因为 $c^*$ 与 $\Gamma_c$ 定义的算子在非退化配对下互为转置、彼此有相同的迹。

**步骤4：支撑落在固定点集上。** 设 $\mathrm{Fix}(c)=\emptyset$。则在 $Z$ 上 $c_2$ 的像与 $\Delta$ 的原像在 $X$ 中无交，即存在分解使 $c_2^{-1}(\Delta)=\emptyset$；沿闭浸入 $j:(X\times X)\setminus\Delta\hookrightarrow X\times X$ 的局部化三角 $j_!j^{!}\to\mathrm{id}\to\Delta_*\Delta^{*}\to$，与 $X\times X\setminus\Gamma_c$ 的对应三角比较，$\Gamma_c$ 的类在 $H^{2n}$ 中为零，故 $\langle\Gamma_c,\Delta\rangle=0$，即 $L(c,\mathcal{F})=0$。同理若 $\mathrm{Fix}(c)$ 有限，把 $X\times X$ 沿 $\mathrm{Fix}$ 逐点裁剪，相交类被压到 $\mathrm{Fix}$ 上，得 $L(c,\mathcal{F})=\sum_xL_x$。

**步骤5：局部 Lefschetz 数。** 固定孤立点 $x\in\mathrm{Fix}(c)$。取仅含该不动点的小开邻域 $U$（在假定各固定点孤立时），对 $U$ 重复步骤1–4 得局部项
$$
L_x(c,\mathcal{F})=\mathrm{tr}\big(\text{$\eta_c$ 在 }x\text{ 的茎上的作用}\big),
$$
其显式由 $x$ 处切空间上的"Lefschetz 局部因子"（$1-dc$ 的行列式与 $\mathcal{F}_x$ 上传输的迹）给出；当 $dc=0$（如 Frobenius 在 $\mathbb{F}_{q^n}$ 上）时切空间因子为 $1$，$L_x=\mathrm{tr}(\mathrm{Frob}_x\mid\mathcal{F}_x)$。

**步骤6：得到 Grothendieck-Lefschetz。** 取 $c=\Gamma_{\phi^n}$。此时 $c_1,c_2$ 皆为同构，$c^*=\phi^{n*}$，且 $\mathrm{Fix}(c)$ 恰为有理点集，每点孤立（$\mathrm{Spec}\,\mathbb{F}_{q^n}$-点）。由步骤3–5，
$$
\sum_i(-1)^i\mathrm{tr}\big(\phi^{n*}\mid H^i_c(\bar X,\mathcal{F})\big)=\sum_{x\in X(\mathbb{F}_{q^n})}\mathrm{tr}\big(\mathrm{Frob}_x^n\mid\mathcal{F}_x\big),
$$
对 $\mathcal{F}=\bar{\mathbb{Q}}_\ell$ 右端即 $\#X(\mathbb{F}_{q^n})$。

**结论（$\square$）**：Lefschetz 数 = 对应图与对角线的（层系数）相交数 = 固定点集上的局部 Lefschetz 数之和，Grothendieck-Lefschetz 迹公式为其 Frobenius 特例。

## 五、应用与意义

该公式是算术代数几何的"计数引擎"：它把有理点计数、Hecke 对应与 Frobenius 的作用统一为相交数与局部因子问题，是 Weil 猜想（有理性、函数方程、Riemann 假设）证明框架中"迹 = 相交"这一环的关键；其带系数的局部因子形式支撑了 Deligne-Lusztig 对有限群表示的构造、Lefschetz 铅笔与单值性论证，以及现代迹公式（导出几何、形变理论、Weil II）中"计数即上同调"的范式。
