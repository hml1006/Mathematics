# Hodge 指数定理

> **一句话大白话**：光滑射影曲面上的相交形式只有"一个正方向，其余全是负方向"：与一个丰沛（正）类垂直的类，自交数必为负；自交数为零当且仅当这个类本身为零。
>
> **小例子**：在 $\mathbb{P}^1\times\mathbb{P}^1$ 上取 $H=a+b$（丰沛类，$a\cdot b=1$、$a^2=b^2=0$），令 $D=a-b$，则 $D\cdot H=0$ 而 $D^2=-2<0$；同时 $H^2=2>0$，正方向确实只有一个。

## 一、定理介绍

> **前置依赖**：光滑射影曲面与相交理论、Néron-Severi 群与数值等价、丰沛除子与 Nakai-Moishezon 判据、Riemann-Roch 与 Serre 对偶、Hodge 理论（调和代表、Lefschetz 分解、Hodge-Riemann 双线性关系）

Hodge 指数定理是代数曲面理论的基本定理，由 W. Hodge 提出并证明：在光滑射影曲面 $X$ 上，相交形式对 $H^{1,1}(X,\mathbb{R})$ 的符号差为 $(1,h^{1,1}-1)$，即恰有一个正特征值、其余全为负特征值。

等价的说法更常用于代数几何：设 $H$ 为丰沛除子，则 $H^2>0$；而对任何满足 $D\cdot H=0$ 的除子类 $D$，有 $D^2\le0$，且 $D^2=0\iff D\equiv0$（数值等价于零）。这一定理确立了曲面上"正锥"的几何形状（正锥是开的且只含一个"方向"的意义下的强凸性），是曲面分类、一般型曲面（$K^2>0$ 与 $K\cdot D>0$ 的论证）、Riemann-Roch 的应用以及 Néron-Severi 结构理论的关键，也在算术几何中与 Hasse 原理合成为 Hasse-Hodge 定理。

## 二、原理思路

最干净的证明走 Kähler 几何路线（Howard-Chern、Hodge-Riemann）：

1. 丰沛除子 $H$ 对应 $X$ 上的 Kähler 类 $\omega$；相交形式与 $\int_X\alpha\wedge\beta$ 一致（Poincaré 对偶）。
2. $H^\perp$ 恰是"原始（primitive）类"构成的空间，即与 $\omega$ 缩并为零的实 $(1,1)$-类。
3. **局部（逐点）恒等式**：在 Kähler 正规坐标下，原始实 $(1,1)$-形式 $\alpha$ 满足
$$\alpha\wedge\alpha=-\frac12|\alpha|^2_\omega\ \omega\wedge\omega\le0,$$
等号当且仅当 $\alpha$ 在各点为零。积分即得 $\alpha^2\le0$，等号当且仅当 $\alpha$ 的上同调类为零。
4. 于是 $\omega^\perp$ 上相交形式负定，加上 $\omega^2>0$，得符号差 $(1,h^{1,1}-1)$。

另一条纯代数路线（Hodge 引理）用 Riemann-Roch：若 $D^2>0$ 则某个倍数 $\pm mD$ 与一个有效除子线性等价，从而对丰沛 $H$ 有 $D\cdot H\ne0$；它处理 $D^2>0$ 的情形，而 $D^2=0$ 的情形仍需第 3 步的逐点论证（或相当的逼近论证）。

## 三、定理的严格表述

设 $X$ 是代数闭域 $k$ 上的光滑射影曲面，$(\ ,\ )$ 为除子（或 $H^{1,1}$ 类）的相交形式，$\rho=\mathrm{rank}\,\mathrm{NS}(X)\le h^{1,1}(X)$ 为 Néron-Severi 群的秩。

**定理（Hodge 指数定理）**：
(1) 对每个丰沛除子 $H$ 有 $H^2>0$；
(2) 若 $D$ 是除子、$D\cdot H=0$，则 $D^2\le0$；进一步
$$D^2=0\iff D\equiv0\ (\text{数值等价于 }0);$$
(3) 相交形式在 $\mathrm{NS}(X)\otimes\mathbb{R}$（等价地，在 $H^{1,1}(X,\mathbb{R})$）上的符号差为 $(1,\rho-1)$；对固定的丰沛类 $H$，形式在超平面 $H^\perp=\{D:D\cdot H=0\}$ 上负定。

**推论（正锥的强凸性）**：每个数值非零的类 $D$，若 $D^2>0$ 则 $D\cdot H\ne0$ 对一切丰沛 $H$ 成立；因此 $\{D:D^2>0\}$ 分成两支，其中恰有一支与丰沛类正向相交（"正锥"），是开的凸锥。

## 四、证明过程

**步骤 1：几何设定与 $H^2>0$**

取丰沛除子 $H$（可为充分大的倍数，使 $H$ 非常丰沛），其对应的 Kähler 类记作 $\omega$，则 $X$ 是紧 Kähler 曲面，且对实 $(1,1)$-类 $\alpha,\beta$ 有
$$(\alpha,\beta)=\int_X\alpha\wedge\beta$$
（Poincaré 对偶）。特别地 $H^2=\int_X\omega\wedge\omega>0$：$\omega$ 是 Kähler 形式时 $\omega^2/2$ 是与定向相容的正体积形式，故 $\int_X\omega^2>0$。这给出 (1)。

**步骤 2：$H^\perp$ 即原始类空间**

由 Poincaré 对偶，$D\cdot H=0$ 等价于 $\alpha\cdot\omega=0$，即 $\int_X\alpha\wedge\omega=0$。而在曲面（复维数 $2$）上的 Lefschetz 分解为 $H^2=H^2_{\mathrm{prim}}\oplus\mathbb{R}\omega$，其中 $H^2_{\mathrm{prim}}=\ker(L)$（$L=\omega\wedge\cdot$，$H^{1,1}_{\mathrm{prim}}=\{\alpha\in H^{1,1}_{\mathbb{R}}:\alpha\wedge\omega=0\}$，此处用到硬 Lefschetz 与 $\omega\wedge\cdot$ 在 $H^{1,1}$ 上的对偶描述）。故 $H^\perp\cap H^{1,1}=H^{1,1}_{\mathrm{prim}}$。

**步骤 3：原始 $(1,1)$-类的逐点计算（核心）**

取 $\alpha$ 为闭的原始实 $(1,1)$-形式（在它的上同调类中取调和代表，则 $\alpha$ 是 $C^\infty$ 的闭形式）。在任一点 $p$ 取该点处的 Kähler 正规坐标，使
$$\omega=i\big(dz^1\wedge d\bar z^1+dz^2\wedge d\bar z^2\big),$$
并写 $\alpha=i\sum_{j,k}a_{j\bar k}\,dz^j\wedge d\bar z^k$。$\alpha$ 为实形式给出 $\overline{a_{j\bar k}}=a_{k\bar j}$；$\alpha$ 原始给出 $\alpha\wedge\omega=0$，即 $a_{1\bar1}+a_{2\bar2}=0$（无迹条件）。

设 $\Omega=dz^1\wedge d\bar z^1\wedge dz^2\wedge d\bar z^2$ 为局部体积元，直接做外积（重排因子并注意 $\omega\wedge\omega=-2\Omega$）得
$$\alpha\wedge\alpha=-2\Big(|a_{1\bar1}|^2+|a_{1\bar2}|^2+|a_{2\bar1}|^2+|a_{2\bar2}|^2\Big)\Omega=-\frac12\Big(\sum_{j,k}|a_{j\bar k}|^2\Big)\,\omega\wedge\omega.$$
记 $|\alpha|^2_\omega=\sum_{j,k}|a_{j\bar k}|^2\ge0$（Kähler 度量下的逐点范数平方），则
$$\alpha\wedge\alpha=-\frac12|\alpha|^2_\omega\ \omega\wedge\omega,$$
这是一条在各点成立的代数恒等式。由于 $\omega^2/2$ 是正体积形式，两边积分得
$$\alpha^2=\int_X\alpha\wedge\alpha=-\frac12\int_X|\alpha|^2_\omega\ \frac{\omega^2}{2}\cdot2\le0,$$
即 $\alpha^2=-\frac14\int_X|\alpha|^2_\omega\,\omega^2\le0$。

**步骤 4：等号情形与负定性**

若 $\alpha^2=0$，则步骤 3 中 $\int_X|\alpha|^2_\omega\omega^2=0$，被积函数非负，故 $\alpha$ 在 $X$ 上逐点为零，即 $\alpha=0$ 是零形式，其调和代表为零，故 $\alpha$ 的上同调类为 $0$。因此相交形式在 $H^{1,1}_{\mathrm{prim}}=H^\perp\cap H^{1,1}$ 上**负定**：
$$\alpha\in H^\perp\ \Longrightarrow\ \alpha^2\le0,\quad\text{等号仅当 }\alpha=0.$$
对除子类（$\mathrm{NS}(X)\otimes\mathbb{R}\subseteq H^{1,1}_{\mathbb{R}}$）限制仍有此性质：$D\cdot H=0\Rightarrow D^2\le0$，且 $D^2=0\Rightarrow D\equiv0$，这正是 (2)。

**步骤 5：符号差**

$H^{1,1}_{\mathbb{R}}=\mathbb{R}\omega\oplus H^{1,1}_{\mathrm{prim}}$ 是正交直和：$\omega$ 与 $H^{1,1}_{\mathrm{prim}}$ 相交为零，而 $\omega^2>0$、形式在 $H^{1,1}_{\mathrm{prim}}$ 上负定（步骤 4，维数 $h^{1,1}-1$）。故符号差为 $(1,h^{1,1}-1)$，限制到 $\mathrm{NS}(X)\otimes\mathbb{R}$ 得 $(1,\rho-1)$，这就是 (3)。推论由 (2) 直接得到：若 $D^2>0$ 且 $D\cdot H=0$，则与 (2) 矛盾，故 $D^2>0$ 的类必与每个丰沛类正向或负向相交，且该符号在丰沛锥上局部常值（丰沛锥连通），故只有一支为"正"。

## 五、应用与意义

1. **曲面理论的基础工具**：Hodge 指数定理给出 $K^2>0$、$K\cdot H>0$（$K$ 为典范类）在各种分类论证中的强约束；它是 Riemann-Roch 定理在曲面上得以"符号化"应用（如 Noether 不等式、Bogomolov-Miyaoka-Yau 不等式）的必要输入。

2. **Néron-Severi 与正锥**：定理刻画了正锥的强凸性与超平面负定性，是 Néron-Severi 群算术结构（Hasse-Hodge 定理、Hodge 猜想的曲面情形）、以及$\mathbb{Q}$-除子正性（nef、big、伪有效）理论的起点，并在 Mori 纲领（锥定理）中经由"负定性 ⇒ 极小模型"的论证发挥作用。

3. **推广**：高维情形的对应物是 Hodge-Riemann 双线性关系与"指数定理"（在 $H^{p,p}$ 的原始部分上符号为 $(-1)^p$），它构成 Hodge 理论、Lefschetz 分解与 Gromov 的 Kähler 锥几何的基础；在算术几何中，Hodge 指数定理与 Hasse 原理、Tate 猜想（曲面情形）以及相交形式的算术解释密切相关。

## 课堂问答

**老师**：用一句话说清 Hodge 指数定理在光滑射影曲面上断言了什么？

**学生**：结论：相交形式的符号差为 $(1,h^{1,1}-1)$——只有一个正方向。等价地：$H^2>0$；对任意 $D$ 有 $D\cdot H=0\Rightarrow D^2\le0$，且 $D^2=0\iff D\equiv0$（数值等价于零）。

**老师（追问）**：证明里那个"逐点恒等式"为什么能给出全局负定？

**学生**：取 Kähler 类 $\omega$，$H^\perp\cap H^{1,1}=H^{1,1}_{\mathrm{prim}}$。在 Kähler 正规坐标下，原始实 $(1,1)$-形式满足 $\alpha\wedge\alpha=-\frac12|\alpha|^2_\omega\,\omega\wedge\omega\le0$。因 $\omega^2/2$ 是正体积形式，积分得 $\alpha^2\le0$；而 $\alpha^2=0$ 迫使 $|\alpha|^2_\omega\equiv0$，即 $\alpha=0$，故在 $H^\perp$ 上负定且等号只在零类。加上 $\omega^2>0$ 即得符号差。

**老师（拓展）**：高维有对应吗？它和算术几何什么关系？

**学生**：高维对应是 Hodge–Riemann 双线性关系：在原始部分 $H^{p,p}_{\mathrm{prim}}$ 上符号为 $(-1)^p$。它是 Lefschetz 分解与 Kähler 锥/Mori 纲领（锥定理）的基础；算术上，曲面情形与 Hasse 原理合成为 Hasse–Hodge 定理，并与 Tate 猜想的曲面情形密切相关。 常见误区是以为"负定"对所有同调类成立——其实负定只在与丰沛类垂直的超平面 $H^\perp$ 上，正方向恰由 $H$ 本身贡献。
