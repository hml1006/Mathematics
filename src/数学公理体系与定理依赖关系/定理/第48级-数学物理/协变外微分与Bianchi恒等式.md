# 协变外微分与Bianchi恒等式

> **一句话大白话**：协变外微分是把普通外微分"搬"到带联络的向量丛上；对它连做两次就得到曲率。而 Bianchi 恒等式说的是一句极其省事的自洽性——"曲率本身是闭的"，两次作用得到的曲率满足必然的相容条件，绝不是巧合。
>
> **小例子**：对 Levi-Civita 联络，协变外微分 $d^\nabla$ 两次作用在张量场上给出 Riemann 曲率；$d^\nabla\Omega=0$ 就对应第二 Bianchi 恒等式 $\nabla_a R_{bcde}+\nabla_b R_{cade}+\nabla_c R_{abde}=0$，而挠率为零给出第一（代数）Bianchi 恒等式。

## 介绍

协变外微分（covariant exterior derivative）是把外微分算子从平凡丛推广到一般带联络向量丛的工具：设 $\pi:E\to M$ 是光滑向量丛，$\nabla$ 是其上联络，则对 $E$-值微分形式 $\xi\in\Omega^p(M;E)$ 定义 $d^\nabla\xi\in\Omega^{p+1}(M;E)$。它的核心性质是"两次作用不再为零，而是产生曲率"：

$$
d^\nabla d^\nabla=\Omega\wedge\cdot,
$$

其中 $\Omega\in\Omega^2(M;\mathrm{End}\,E)$ 是 $\nabla$ 的曲率形式。由此立得**Bianchi 恒等式**（又称第二 Bianchi 恒等式）

$$
d^\nabla\Omega=0.
$$

在 Levi-Civita 联络（无挠）的情形下，还有**第一 Bianchi 恒等式**这一纯代数关系

$$
R(X,Y)Z+R(Y,Z)X+R(Z,X)Y=0.
$$

这些恒等式在微分几何与数学物理中无处不在：它们是 Gauss–Codazzi–Mainardi 方程、Einstein 张量守恒（$\nabla^a G_{ab}=0$）、Yang–Mills 方程的相容性、Chern–Weil 特征类理论的共同代数基础。可以说"曲率不是随便一个 2-形式，它必须满足 Bianchi 恒等式"。

## 分析

**前置依赖**：向量丛与联络、协变导数、向量值微分形式与外微分、分次（graded）Leibniz 法则、曲率形式、Levi-Civita 联络与挠率张量、Riemann 曲率张量。

**定理内容**：（1）（曲率表述）设 $\Omega=d^\nabla d^\nabla$，则 $\Omega$ 是 $\mathcal A^0(M)$-线性的，即 $\Omega\wedge\cdot\in\Omega^2(M;\mathrm{End}\,E)$，且

$$
d^\nabla\Omega=0.
$$

（2）（Riemann 表述）对 Levi-Civita 联络，
$$
\nabla_X R(Y,Z)W+\nabla_Y R(Z,X)W+\nabla_Z R(X,Y)W=0\quad(\text{第二 Bianchi}),
$$
$$
R(X,Y)Z+R(Y,Z)X+R(Z,X)Y=0\quad(\text{第一 Bianchi}).
$$

**依赖的概念**：联络的曲率、协变外微分、分次 Leibniz 法则、挠率。

## 思考过程

Bianchi 恒等式的证明几乎是"形式化的必然"。协变外微分像普通外微分一样满足分次 Leibniz 法则：

$$
d^\nabla(\alpha\wedge\xi)=d\alpha\wedge\xi+(-1)^{p}\alpha\wedge d^\nabla\xi,\qquad \alpha\in\Omega^p(M),\ \xi\in\Omega^\bullet(M;E).
$$

关键观察是：$\Omega\wedge\cdot=d^\nabla d^\nabla$ 是 $d^\nabla$ 的"平方"，因此 $d^\nabla(\Omega\wedge\xi)=d^\nabla d^\nabla d^\nabla\xi$。把左边用分次 Leibniz 展开，立即得到 $(d^\nabla\Omega)\wedge\xi$ 加上 $\Omega\wedge d^\nabla\xi$；而右边"三次作用"直接等于 $\Omega\wedge d^\nabla\xi$。两边相减，$(d^\nabla\Omega)\wedge\xi=0$，由 $\xi$ 任意得 $d^\nabla\Omega=0$。整个证明只用了一个交换律式的技巧，没有真正的计算。

第一 Bianchi 恒等式则来自挠率取零：把 Riemann 曲率代入并利用 $\nabla_X Y-\nabla_Y X=[X,Y]$，三个协变导数项与李括号项恰好两两抵消。

## 证明过程

**步骤 1：协变外微分的定义与分次 Leibniz 法则。**

在局部平凡化 $E|_U\cong U\times\mathbb R^r$ 上，$\nabla$ 的表出为 $\nabla\xi=d\xi+A\wedge\xi$，其中 $A$ 是联络 1-形式（$\mathfrak{gl}(r)$-值）。对 $\xi\in\Omega^p(M;E)$ 定义 $d^\nabla\xi=d\xi+A\wedge\xi$。可直接验证

$$
d^\nabla(\alpha\wedge\xi)=d\alpha\wedge\xi+(-1)^p\alpha\wedge d^\nabla\xi.
$$

（局部化后是 $\mathbb R^r$-值形式的普通外微分与矩阵乘法的分次 Leibniz 法则。）

**步骤 2：$\Omega=d^\nabla d^\nabla$ 是张量性的。**

对 $\xi\in\Omega^0(M;E)$ 计算
$$
d^\nabla d^\nabla\xi=d(d\xi+A\xi)+A\wedge(d\xi+A\xi)=dA\wedge\xi-A\wedge d\xi+A\wedge d\xi+A\wedge A\wedge\xi=(dA+A\wedge A)\wedge\xi.
$$
记 $\Omega=dA+A\wedge A$（曲率 2-形式）。等式右端作为 $\xi$ 的 $\mathcal A^0$-线性映射，说明 $\Omega\wedge\cdot=d^\nabla d^\nabla$ 是张量性的，即 $d^\nabla d^\nabla$ 对函数是 $C^\infty$-线性的。

**步骤 3：处理 $\Omega\wedge\cdot$ 的分次 Leibniz 法则。**

因 $\Omega$ 是 2-形式（偶次），乘法算子 $\xi\mapsto\Omega\wedge\xi$ 是偶次算子，故它与 $d^\nabla$ 满足"无符号"的分次 Leibniz 法则：

$$
d^\nabla(\Omega\wedge\xi)=(d^\nabla\Omega)\wedge\xi+\Omega\wedge d^\nabla\xi. \tag{$\ast$}
$$

**步骤 4：由 $d^\nabla\Omega\wedge\xi=d^\nabla d^\nabla d^\nabla\xi-d^\nabla d^\nabla d^\nabla\xi=0$ 完成证明。**

由步骤 2，$\Omega\wedge\xi=d^\nabla d^\nabla\xi$，故左端 $d^\nabla(\Omega\wedge\xi)=d^\nabla d^\nabla d^\nabla\xi$。又由 $d^\nabla d^\nabla=\Omega\wedge\cdot$ 直接应用于 $d^\nabla\xi$，有

$$
d^\nabla d^\nabla(d^\nabla\xi)=\Omega\wedge d^\nabla\xi.
$$

比较 $(\ast)$ 两端：

$$
(d^\nabla\Omega)\wedge\xi+\Omega\wedge d^\nabla\xi=d^\nabla d^\nabla d^\nabla\xi=\Omega\wedge d^\nabla\xi,
$$

故 $(d^\nabla\Omega)\wedge\xi=0$ 对一切 $\xi\in\Omega^\bullet(M;E)$ 成立。取 $\xi$ 为 $E$ 的局部截面（$p=0$）即得 $d^\nabla\Omega=0$。这正是第二 Bianchi 恒等式。

**步骤 5：换算到 Riemann 曲率。**

把 $E=TM$、$\nabla$ 取 Levi-Civita 联络，则 $\Omega$ 与 Riemann 曲率张量 $R$ 的关系为 $R(X,Y)Z=\Omega(X,Y)Z$。$d^\nabla\Omega=0$ 且 $\Omega$ 取值于 $\mathrm{End}(TM)$，展开即

$$
(\nabla_X R)(Y,Z)W+(\nabla_Y R)(Z,X)W+(\nabla_Z R)(X,Y)W=0,
$$

即第二 Bianchi 恒等式。（在无挠且 $M$ 的切丛上，$\nabla$ 诱导于 $TM$ 的联络让 $d^\nabla$ 对 $\Omega$ 的一次作用正是三个循环协变导数之和。）

**步骤 6：第一 Bianchi 恒等式（代数）。**

对 Levi-Civita 联络，挠率 $T(X,Y)=\nabla_XY-\nabla_YX-[X,Y]=0$。由 $R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z$，对 $R(X,Y)Z+R(Y,Z)X+R(Z,X)Y$ 直接展开，三个 $\nabla_X\nabla_YZ$ 型项、三个 $\nabla_{[X,Y]}Z$ 型项与六个一阶项按 $X,Y,Z$ 的循环对称两两配对；利用 $\nabla$ 的无挠性把 $\nabla_XY-\nabla_YX$ 换成 $[X,Y]$，再把 $\nabla_X\nabla_YZ-\nabla_{\nabla_XY}Z=\nabla^2_{X,Y}Z$ 的形式代入循环求和，得

$$
R(X,Y)Z+R(Y,Z)X+R(Z,X)Y=\nabla_X\big(T(Y,Z)\big)+\nabla_Y\big(T(Z,X)\big)+\nabla_Z\big(T(X,Y)\big)-T(T(X,Y),Z)-\cdots=0.
$$

右端每一项都含挠率因子，故由 $T=0$ 得零，第一 Bianchi 恒等式成立。$\square$

**推论**：曲率形式满足 $d^\nabla\Omega=0$，从而 Chern–Weil 构造（取不变多项式 $P$ 后 $d\,P(\Omega)=P'(d^\nabla\Omega)=0$）给出良定义的上同调类——特征类。

## 相关条目

- [Yang-Mills方程](./Yang-Mills方程.md)：以 $d^\nabla F=0$（Bianchi）与 $d^\nabla\ast F=0$（场方程）为基本方程组的规范场理论。
- [Atiyah-Singer指标定理](./Atiyah-Singer指标定理.md)：特征类理论建立在曲率的 Bianchi 恒等式与 Chern–Weil 同态之上。
