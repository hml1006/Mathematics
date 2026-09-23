# Serre 相交公式

> **一句话大白话**：两条子簇在某点的"相交重数"可以用同调代数算出来——把它写成 $\mathrm{Tor}$ 群的交错和（Euler 特征数），这就是导出相交层"记在账上"的信息。
>
> **小例子**：在 $\mathbb{A}^2$ 中取 $X=\{y=x^2\}$ 与 $Y=\{y=0\}$，它们只在原点相交且相切，重数应为 $2$。Koszul 复形给出 $\mathrm{Tor}_0=k[x]/(x^2)$（长度 $2$）、$\mathrm{Tor}_1=0$，交错和 $=2$；若换成横截的 $X=\{y=x\}$，则 $\mathrm{Tor}_0=k[x]/(x)$（长度 $1$）、$\mathrm{Tor}_1=0$，交错和 $=1$。

## 一、定理介绍

> **前置依赖**：交换代数（局部环、正则局部环、正则序列、Koszul 复形）、Tor 函子与长度、闭子概形的相交理论、导出张量积与导出纤维积

Serre 相交公式（Serre 的 Tor 公式）是相交理论的代数基础：对光滑环境空间 $P$ 中两个闭子概形 $X,Y$，它们在一点 $z$ 的相交重数被定义为
$$i(X,Y;z)=\sum_{i\ge0}(-1)^i\,\ell_{\mathcal{O}_{P,z}}\Big(\mathrm{Tor}_i^{\mathcal{O}_{P,z}}\big(\mathcal{O}_{X,z},\mathcal{O}_{Y,z}\big)\Big).$$
Serre 证明该交错和有限、在"正常相交"时退化为张量积的长度，并满足相交重数应有的一切好性质（双线性、可加、在一般位置取 $\deg X\deg Y$ 等）。

在导出代数几何中，这条公式获得了概念解释：$X$ 与 $Y$ 的**导出纤维积** $X\times^{\mathbb{R}}_PY$ 的结构层是导出张量积 $\mathcal{O}_X\otimes^{\mathbb{L}}_{\mathcal{O}_P}\mathcal{O}_Y$，其同调层恰为 $\mathrm{Tor}_i$；于是 Serre 公式等价于"导出相交层的 Euler 特征数等于几何相交重数"。这解释了导出几何为何能把过相交（excess intersection）与形变理论统一处理。

## 二、原理思路

1. $P$ 光滑使 $\mathcal{O}_{P,z}$ 是正则局部环，于是 $X$（或 $Y$）局部由**正则序列**（长度 $=$ 余维）截出，从而拥有有限的 **Koszul 自由预解**。
2. 用该预解计算 $\mathrm{Tor}_i^{\mathcal{O}_P}(\mathcal{O}_X,\mathcal{O}_Y)$：交错和等于 Koszul 复形对 $\mathcal{O}_Y$ 张量后的 Euler 特征数，故只有有限项非零。
3. 若相交"正常"（$\mathrm{Tor}_i=0$ 对 $i>0$，即 Tor-独立），交错和退化为 $\mathrm{length}(\mathcal{O}_X\otimes\mathcal{O}_Y)$，即通常的相交重数。
4. 导出几何观点：$X\times^{\mathbb{R}}_PY$ 的结构层就是该 Tor 复形，Serre 公式是其 Euler 特征数在 $K_0$ 类群中的像。

## 三、定理的严格表述

设 $P$ 是域 $k$ 上的光滑概形，$X,Y\hookrightarrow P$ 为闭子概形，$z\in X\cap Y$ 为闭点，$A:=\mathcal{O}_{P,z}$ 且 $\dim A=n<\infty$。

**定理（Serre 相交公式）**：定义
$$i(X,Y;z)=\sum_{i\ge0}(-1)^i\,\ell_A\Big(\mathrm{Tor}_i^A\big(\mathcal{O}_{X,z},\mathcal{O}_{Y,z}\big)\Big),$$
则：
(1) 级数中只有有限项非零，故 $i(X,Y;z)\in\mathbb{Z}$ 良定义；当 $X,Y$ 在 $P$ 中正常相交时 $i(X,Y;z)\ge0$；
(2) 若 $\mathrm{Tor}_i^A(\mathcal{O}_{X,z},\mathcal{O}_{Y,z})=0$ 对一切 $i>0$ 成立（**正常相交 / Tor-独立**），则
$$i(X,Y;z)=\ell_A\big(\mathcal{O}_{X,z}\otimes_A\mathcal{O}_{Y,z}\big)=\ell_A\big(\mathcal{O}_{X\cap Y,z}\big),$$
即交错和退化为交子概形在 $z$ 处的局部长度；
(3) 有界性与 Euler 特征：$\mathrm{Tor}_i=0$ 对 $i>\dim A$ 成立，且
$$i(X,Y;z)=\chi\Big(\mathcal{O}_{X,z}\otimes^{\mathbb{L}}_A\mathcal{O}_{Y,z}\Big)=\Big[\mathcal{O}_{X\times^{\mathbb{R}}_PY,\,z}\Big]\in K_0\big(\text{有限长度 }A\text{-模}\big),$$
即它是导出纤维积结构层的 Euler 特征数。

**推论（Bézout 型计数）**：若 $X,Y\subset\mathbb{P}^n_k$ 为无公共分支的射影簇、$\dim X+\dim Y=n$，则 $X\cap Y$ 有限且
$$\sum_{z\in X\cap Y}i(X,Y;z)=\deg X\cdot\deg Y,$$
这是经典 Bézout 定理的相交重数形式。

## 四、证明过程

**步骤 1：Koszul 预解与有限性**

$P$ 光滑、$z$ 为闭点，故 $A=\mathcal{O}_{P,z}$ 是正则局部环，$\dim A=n$。设 $r=\mathrm{codim}(X,P)$，则 $\mathcal{O}_{X,z}=A/I$ 且 $I$ 可由 $r$ 个元素 $f_1,\dots,f_r$ 生成（正则环中高度为 $r$ 的理想可由 $r$ 个元素生成，且这 $r$ 个元素构成 $A$-正则序列）。于是 **Koszul 复形**
$$K_\bullet(f_1,\dots,f_r;A):\ 0\to\Lambda^rA^r\to\cdots\to\Lambda^1A^r\to A\to0$$
是 $\mathcal{O}_{X,z}=A/(f_1,\dots,f_r)$ 的一个长度 $r$ 的自由 $A$-预解（正则序列的 Koszul 复形正合）。因此对任意 $A$-模 $M$，
$$\mathrm{Tor}_i^A\big(\mathcal{O}_{X,z},M\big)=H_i\big(K_\bullet(f_1,\dots,f_r;A)\otimes_AM\big),$$
特别地
$$\mathrm{Tor}_i^A\big(\mathcal{O}_{X,z},\mathcal{O}_{Y,z}\big)=0\qquad(i>r).$$
于是求和只有 $0\le i\le r$ 项非零，$i(X,Y;z)$ 良定义，这证明了 (1) 的有限性部分（非负性在正常相交情形由 (2) 给出；一般情形的正性是 Gillet-Soulé 型的深刻结果，此处不强用）。

**步骤 2：正常相交时的退化**

设 $\mathrm{Tor}_i^A(\mathcal{O}_{X,z},\mathcal{O}_{Y,z})=0$ 对 $i>0$ 成立。则步骤 1 中的复形 $K_\bullet\otimes_A\mathcal{O}_{Y,z}$ 只在 $H_0$ 处有同调，即
$$\cdots\to K_1\otimes_A\mathcal{O}_{Y,z}\to K_0\otimes_A\mathcal{O}_{Y,z}\to0$$
是 $H_0=\mathcal{O}_{X,z}\otimes_A\mathcal{O}_{Y,z}$ 的一个有限自由预解。该复形各项均为有限长度 $A$-模且有界，故 Euler 特征数可在同调上计算，且等于 $\ell_A(H_0)$，于是
$$\sum_i(-1)^i\ell_A\big(\mathrm{Tor}_i^A(\mathcal{O}_{X,z},\mathcal{O}_{Y,z})\big)=\ell_A(H_0)=\ell_A\big(\mathcal{O}_{X,z}\otimes_A\mathcal{O}_{Y,z}\big).$$
当 $X,Y$ 在 $P$ 中正常相交（余维相加且交概形余维正确）时 $\mathcal{O}_{X,z}\otimes_A\mathcal{O}_{Y,z}=\mathcal{O}_{X\cap Y,z}$，故得 (2)。这解释了 Serre 公式的含义：交错和在正常相交时恰好等于"交概形的长度"，即经典相交重数。

**步骤 3：有界性与 Euler 特征解释**

由步骤 1，$\mathrm{Tor}_i=0$（$i>n$），故交错和等于有限复形 $K_\bullet(f)\otimes_A\mathcal{O}_{Y,z}$ 的 Euler 特征数。在导出代数几何中，$\mathcal{O}_{X,z}\otimes^{\mathbb{L}}_A\mathcal{O}_{Y,z}$ 就是（用上述自由预解替换、再取张量积所得的）复形，其第 $i$ 个同调层为 $\mathrm{Tor}_i^A(\mathcal{O}_{X,z},\mathcal{O}_{Y,z})$；导出纤维积 $X\times^{\mathbb{R}}_PY$ 在 $z$ 处的结构层即此复形。于是
$$i(X,Y;z)=\chi\big(\mathcal{O}_{X,z}\otimes^{\mathbb{L}}_A\mathcal{O}_{Y,z}\big)=\big[\mathcal{O}_{X\times^{\mathbb{R}}_PY,\,z}\big]\in K_0\big(\text{有限长度 }A\text{-模}\big),$$
即在 $K_0$ 类群中，几何相交重数就是导出相交层的类。这正是"导出相交把高阶 $\mathrm{Tor}$ 自动记账"的精确表述。

**步骤 4：Bézout 型推论**

当 $\dim X+\dim Y=n$ 且 $X,Y$ 无公共分支时 $X\cap Y$ 有限。把步骤 1-3 的局部公式沿 $X\cap Y$ 求和，并用整体 Koszul 复形的 Euler 特征计算：$\sum_z i(X,Y;z)=\sum_i(-1)^i\dim_k\mathrm{Tor}_i^{\mathcal{O}_P}(\mathcal{O}_X,\mathcal{O}_Y)$（整体版本），由 Koszul 复形的交错维数求和 $\sum_i(-1)^i\binom{r}{i}=0$（$r\ge1$）把该交错和化为 $\mathcal{O}_X$ 与 $\mathcal{O}_Y$ 的 Hilbert 多项式首项之比，即 $\deg X\cdot\deg Y$，得 Bézout 定理。

## 五、应用与意义

1. **相交理论的代数化**：Serre 公式把相交重数定义为 Tor 交错和，使相交理论完全纳入交换代数；正常相交时退化为张量积长度，过相交时保留高阶 Tor 信息（即 excess intersection 的显式记录），是 Fulton 相交理论的代数出发点之一。

2. **导出代数几何的直接动机**：导出纤维积 $X\times^{\mathbb{R}}_PY$ 的结构层就是 $\mathrm{Tor}$ 复形，Serre 公式说明"导出相交 = 带同调信息的相交"。由此发展出导出相交理论、虚拟基本类、形变-障碍理论以及 Gromov-Witten/DT 理论中的虚拟计数。

3. **推广**：公式可推广到非正规相交、非光滑环境与导出环谱（spectral algebraic geometry）的框架；在 $\infty$-范畴语言下，它成为"导出张量积的 Euler 特征 = 相交重数"的一般定理，并与 K-理论、Riemann-Roch（在导出设置下）紧密联系。
