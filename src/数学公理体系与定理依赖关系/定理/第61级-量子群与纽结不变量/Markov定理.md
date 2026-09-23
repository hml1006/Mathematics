# Markov 定理

> **一句话大白话**：链环用"闭辫"来表示时，"表示不同但其实是同一个链环"这件事被两类操作（共轭与稳定化）完全刻画；于是只要一个辫上的函数在这两类操作下不变，它就能定义出链环不变量。
>
> **小例子**：三叶结可写成 $B_2$ 中辫 $\sigma_1^{\,3}$ 的闭辫；把 $\sigma_1^{\,3}$ 换成共轭 $\gamma\sigma_1^{\,3}\gamma^{-1}$，或在末尾添一个 $\sigma_n^{\pm1}$，链环类型都不变，这正是 Markov 移动的两种情形。

## 一、定理介绍

> **前置依赖**：Jones多项式、Kauffman括号、Homfly多项式、Yang-Baxter方程、量子群定义与结构、辫群与闭辫概念。

Markov 定理（Markov's theorem on braids）由 A. A. Markov 于 1935 年证明，研究"闭辫"这一链环表示方式的冗余程度。给定 $n$ 股辫 $\alpha\in B_n$，把第 $i$ 股与第 $i+1$ 股按辫的规则相接，即得 $\mathbb R^3$ 中的链环 $\hat\alpha$，称为 $\alpha$ 的闭辫（closed braid）。Alexander 定理（1923）保证每个链环都同痕于某个闭辫，于是链环的分类问题可以搬到"所有辫的不交并 $\bigsqcup_n B_n$"上去，只需弄清哪些辫给出同一链环。

Markov 的答案极其简洁：这等价关系由两类移动生成。其一是共轭（conjugation）：$\alpha\rightsquigarrow\gamma\alpha\gamma^{-1}$，$\gamma\in B_n$；其二是稳定化（stabilization）：$\alpha\rightsquigarrow\alpha\sigma_n^{\pm1}$，其中把 $B_n$ 看作 $B_{n+1}$ 的子群。前者对应在闭辫上移动"切割点"，后者对应在闭辫上添加或去掉一个 Reidemeister I 型扭结。

该定理是纽结理论"代数化"的分水岭。V. F. R. Jones 在 1984 年发现：只要在辫群上构造一个满足这两条不变性的函数（Markov 迹），就自动得到链环不变量，于是他由 Temperley–Lieb 代数与 Hecke 代数的迹定义了 Jones 多项式，并进而发展出量子群与三维流形不变量的整套理论（Reshetikhin–Turaev、Ocneanu、Turaev–Wenzl）。

## 二、原理思路

1. **闭辫表示**：把 $\mathbb R^3$ 中的链环放入以固定轴为中心的圆环中、使其沿轴的辐角单调上升，便得到闭辫表示；这一几何构造即 Alexander 定理的内容。

2. **两类移动的几何含义**：M1 是沿闭辫改变参数的起点（切割圆盘沿环面滑动），几何上只是环面自同胚，与链环同痕相容；M2 是在闭辫的一股上加/减一个"小圈"（Reidemeister I 型扭结），显然不改变链环类型。

3. **完备性**：反之，两个闭辫表示之间的任意 ambient isotopy 可按时间分层，逐层只涉及有限个股的交叉改变；用共轭移动把涉及变化的股依次挪到末尾相邻位置，再把每个基本改变写成 $\sigma_n^{\pm1}$ 的插入或辫群内部的交叉重排，归纳即得有限次 M1、M2 的连接。

4. **商化为不变量**：Markov 移动生成的等价关系恰是链环同痕，于是任何在此等价关系下不变的函数都是链环不变量；Markov 迹正是这类函数。

## 三、定理的严格表述

**定理（Markov 1935）**：设 $\alpha\in B_n$、$\beta\in B_m$ 为辫，$\hat\alpha$、$\hat\beta$ 为对应闭辫。则 $\hat\alpha$ 与 $\hat\beta$ 在 $\mathbb R^3$ 中同痕当且仅当 $\alpha$ 与 $\beta$ 可由有限次以下两类 Markov 移动互相得到：
$$\text{(M1)}\quad \alpha\ \longleftrightarrow\ \gamma\alpha\gamma^{-1}\quad(\gamma\in B_n),$$
$$\text{(M2)}\quad \alpha\ \longleftrightarrow\ \alpha\sigma_n^{\pm1}\quad(\alpha\in B_n\subset B_{n+1}).$$

**配合 Alexander 定理的形式**：每个链环同痕于某闭辫，且若 $\hat\alpha$ 与 $\hat\beta$ 同痕则二者由 M1、M2 连接；故映射
$$\Big(\bigsqcup_{n\geq1}B_n\Big)\Big/\text{(M1, M2)}\ \longrightarrow\ \{\text{链环的同痕类}\},\qquad [\alpha]\mapsto[\hat\alpha]$$
是双射。

**推论（Markov 迹给出链环不变量）**：设函数族 $f_n:B_n\to R$（$n\geq1$，$R$ 为交换环，例如 $\mathbb Z[t^{\pm1/2}]$）满足
$$f_n(\gamma\alpha\gamma^{-1})=f_n(\alpha),\qquad f_{n+1}(\alpha\sigma_n^{\pm1})=f_n(\alpha),$$
则 $F(\hat\alpha):=f_n(\alpha)$ 良定义，且 $F$ 是链环不变量。用闭辫表示计算即可。

## 四、证明过程

**步骤 1（闭辫表示的存在性，Alexander 定理）。** 取 $S^3$ 的标准 Heegaard 分解 $S^3=V_1\cup V_2$（两个实心环），记 $A$ 为 $V_1$ 的核（轴）。给定链环 $L$，可通过同痕把它移入 $V_2$ 并使 $L$ 关于轴 $A$ 的辐角（角度参数）沿途单调递增：具体作法是先取一条经过 $A$ 的圆盘族 $D_\theta$（$\theta\in S^1$）扫过 $V_2$，把 $L$ 逐段推入这些圆盘，并用局部修改消去逆行的临界点。于是 $L=\hat\alpha$ 为某 $n$ 股辫的闭辫。这给出 Alexander 定理的几何内容，也说明闭辫表示总存在。

**步骤 2（M1 与链环同痕）。** 设 $\alpha\in B_n$，$\gamma\in B_n$。闭辫 $\hat\alpha$ 的构造依赖一个"切割圆盘" $D_\theta$，即在 $\theta=\theta_0$ 处切断闭辫并读出一段辫。改变 $\theta_0$ 至 $\theta_1$ 相当于把切割圆盘绕轴旋转，所读出的辫是把 $\alpha$ 的第 $n-k$ 至 $n$ 股"搬到前面"，其代数效果正是共轭 $\alpha\mapsto\gamma\alpha\gamma^{-1}$，其中 $\gamma$ 是这部分辫在 $B_n$ 中的元素。由于整个过程只是环面绕轴的整体旋转（保持链环与轴），$\hat\alpha$ 与 $\widehat{\gamma\alpha\gamma^{-1}}$ 同痕。故 M1 不改变链环类型。

**步骤 3（M2 与 Reidemeister I）。** 设 $\alpha\in B_n$，把它看作 $B_{n+1}$ 的元素（新增第 $n+1$ 股不动）。闭辫 $\widehat{\alpha\sigma_n}$ 与 $\hat\alpha$ 的差别集中在最后两股：$\sigma_n$ 使第 $n$、$n+1$ 股交换一次，闭辫后第 $n$ 股沿第 $n+1$ 股绕行半圈，在链环图上表现为一个只剩下自身的"小圈"（kink），即 Reidemeister I 型扭结。由 Reidemeister I 移动可把它去掉，故 $\widehat{\alpha\sigma_n}$ 与 $\hat\alpha$ 同痕；同理 $\widehat{\alpha\sigma_n^{-1}}$ 亦然。故 M2 不改变链环类型。

**步骤 4（完备性：M1、M2 生成全部等价关系）。** 设 $\hat\alpha$ 与 $\hat\beta$ 同痕，取二者共用的轴 $A$ 与圆盘族。把同痕 $H:S^1\times[0,1]\to S^3$（把闭辫 $\hat\alpha$ 变形为 $\hat\beta$，同时保持单调形式）按时间离散化，使每个小区间上只有有限个股发生交叉改变，并可设同痕在每一时刻都保持关于 $A$ 的单调性（这是 Alexander 定理证明中的"单调化"技巧，可逐段实现）。于是只需处理一次"基本改变"：

- 若基本改变发生在最后两股上，它可表示为在词中插入或删除 $\sigma_n^{\pm1}$，即 M2；
- 若发生在其他地方，先用 M1（共轭）把发生改变的位置挪到最后两股，再作 M2；把这一步骤整理回原词，相当于在辫群内用辫关系重排生成元，而这些重排正是 $\alpha\mapsto\gamma\alpha\gamma^{-1}$ 的形式。

对全部基本改变归纳，即得 $\alpha$ 与 $\beta$ 由有限次 M1、M2 连接。故 Markov 移动生成闭辫的整个同痕等价关系。此为 Markov 定理的核心，其严格化由 Birman（1974）用映射类群与辫群的短正合序列给出：闭辫同痕类与 $\bigsqcup B_n$ 在 M1、M2 下的商自然同构。

**步骤 5（Markov 迹是不变量）。** 设 $f_n$ 满足推论中的两条不变性，定义 $F(L):=f_n(\alpha)$，其中 $\hat\alpha$ 是 $L$ 的任一闭辫表示。良定义性：由步骤 1 表示存在；由步骤 2 至步骤 4，任意两个表示由有限次 M1、M2 连接，而 $f_n$ 在每次 M1、M2 下取值不变（注意 M2 改变股数时使用了 $f_{n+1}(\alpha\sigma_n^{\pm1})=f_n(\alpha)$），故 $f_n(\alpha)$ 不依赖表示选取。$F$ 显然是同痕不变量，推论得证。

**步骤 6（典型 Markov 迹：Jones 多项式）。** 取 Temperley–Lieb 代数 $TL_n$，其由 $1,e_1,\dots,e_{n-1}$ 生成，满足 $e_i^2=\delta e_i$（$\delta=-t^{1/2}-t^{-1/2}$）、辫关系与 Jones 关系。定义辫群表示 $\rho:B_n\to TL_n$，$\rho(\sigma_i)=t^{1/2}e_i+t^{-(1/2)}\cdot1$（这是 Kauffman 括号光滑化的代数化，满足 $\rho$ 的辫关系）。在 $TL_n$ 上取 Markov 迹 $\operatorname{tr}$（由"标架图上的圈计数"定义，满足 $\operatorname{tr}(1)=1$、$\operatorname{tr}(xe_n)=\delta\operatorname{tr}(x)$，其中 $x$ 由前 $n-1$ 个生成元生成）。于是 $f_n(\alpha):=\operatorname{tr}(\rho(\alpha))$ 是共轭不变且在稳定化下按 $\delta$ 变化：
$$f_{n+1}(\alpha\sigma_n^{\pm1})=\delta^{\pm1}\cdot f_n(\alpha).$$
用"框修正"因子 $\big(-\frac{1+t}{\sqrt t}\big)^{n-1}$ 与 $\big(\sqrt t\big)^{e(\alpha)}$（$e(\alpha)$ 为指数和）消去该 $\delta$ 与股数的依赖，即得 Kauffman 括号与 Jones 多项式。这就是 Jones（1985）用 Markov 迹构造 $V_L(t)$ 的完整思路。量子群情形同理：取 $U_q(\mathfrak{sl}_2)$ 的 $R$-矩阵表示 $\rho:B_n\to\operatorname{End}(V^{\otimes n})$，其上"量子迹"经规范化后给出 Homfly 多项式，构成 Reshetikhin–Turaev 不变量的代数框架。$\square$

## 五、应用与意义

- **Jones 与 Homfly 多项式的代数定义**：Markov 迹把"链环不变量"的构造化归为辫群上满足两条不变性的函数，是量子不变量的定义性入口。
- **量子群与 R-矩阵**：由量子群的表示与量子迹出发，Markov 定理保证所得到的量不依赖辫的选取，得 Reshetikhin–Turaev 型不变量。
- **辫群与 Hecke/Temperley–Lieb 代数**：把纽结理论、代数表示论与统计力学模型（六顶角模型、Potts 模型）联系起来。
- **辫群的词问题与算法**：由于 $B_n$ 有多种可判定的正规形（Garside 正规形等），Markov 移动为不变量的算法计算提供可操作路径。
- **映射类群与 Birman 正合序列**：闭辫与映射类群的关系把 Markov 定理嵌入低维拓扑与几何群论的结构之中。

## 相关条目

- [Jones多项式](./Jones多项式.md)：由 Temperley–Lieb 代数的 Markov 迹经规范化得到，是 Markov 定理最著名的应用。
- [Homfly多项式](./Homfly多项式.md)：由 Hecke 代数/量子群的量子迹给出，同属 Markov 迹框架。
- [Kauffman括号](./Kauffman括号.md)：光滑化规则给 $\rho(\sigma_i)=t^{1/2}e_i+t^{-1/2}$ 的 skein 解释。
- [Yang-Baxter方程](./Yang-Baxter方程.md)：$R$-矩阵满足的辫关系，是 $\rho:B_n\to\operatorname{End}(V^{\otimes n})$ 良定义的条件。
- [量子群定义与结构](./量子群定义与结构.md)：提供 $R$-矩阵与量子迹，构造 Homfly 等不变量。
- [Reshetikhin-Turaev不变量](./Reshetikhin-Turaev不变量.md)：把 Markov 迹框架系统化为三维流形不变量。
- [Lickorish–Wallace手术定理](./Lickorish–Wallace手术定理.md)：与 Markov 定理共同构成"纽结不变量到三维流形不变量"的两条代数化路径。
