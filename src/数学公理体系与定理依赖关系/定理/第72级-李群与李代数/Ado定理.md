# Ado 定理

> **一句话大白话**：任何一个有限维李代数，不管它多抽象，都能被"具体化"成某个矩阵李代数的子代数——李括号就是矩阵换位子，抽象的括号运算总有具体的矩阵模型。

> **小例子**：$\mathfrak{sl}_2(\mathbb{R})$ 是迹为零的 $2\times2$ 实矩阵全体，本身就是矩阵李代数；而幂零海森堡代数 $\mathfrak{h}$（由 $X,Y,Z$ 生成，$[X,Y]=Z$ 为中心）也能嵌入 $\mathfrak{gl}_3$：取 $X\mapsto E_{12}$、$Y\mapsto E_{23}$、$Z\mapsto E_{13}$ 即验证 $[E_{12},E_{23}]=E_{13}$。

## 一、定理介绍

> **前置依赖**：李代数与理想、可解与幂零李代数、Levi 分解（概念）、半单李代数与 Cartan 判别法、Lie 定理、泛包络代数（概念）。

Ado 定理由 Igor Ado 于 1935 年证明（后经 Iwasawa、Jacobson、Harish-Chandra 等人推广与简化），断言特征零域上任意有限维李代数都有忠实有限维表示，即同构于某个 $\mathfrak{gl}(n,k)$ 的子代数。它回答了李理论中最基本的存在性问题：抽象定义的李代数是否总能"坐实"为矩阵代数？因为没有这一步，就无法把李代数与李群的对应（李第三定理）落地——李群需要具体的矩阵实现才能构造。Ado 定理与 Levi 分解、Engel 定理、Lie 定理配合，构成有限维李代数结构理论的最后一环：可解部分提供表示、半单部分由伴随表示提供忠实性，两者榫接得到整体的忠实表示。

## 二、原理思路

1. 用 Levi 分解把问题拆为"可解核 + 半单部分"：$\mathfrak{g}=\mathfrak{r}\rtimes\mathfrak{s}$，其中 $\mathfrak{r}=\operatorname{rad}\mathfrak{g}$ 可解、$\mathfrak{s}$ 半单。
2. 半单部分不难：$\mathfrak{s}$ 的伴随表示忠实（半单李代数的中心为零，由 Cartan 判别法），故 $\mathfrak{s}\hookrightarrow\mathfrak{gl}(\mathfrak{s})$。
3. 关键归约：只需找到 $\mathfrak{r}$ 的忠实有限维表示，并把它"提升"为 $\mathfrak{g}$-模；随后对可解李代数用维数归纳法（取余维 $1$ 理想）与 Zassenhaus 的提升技巧证明其忠实表示存在；两者用直和/张量并置整合，得到 $\mathfrak{g}$ 的忠实表示。

## 三、定理的严格表述

设 $k$ 是特征 $0$ 的域，$\mathfrak{g}$ 是 $k$ 上的有限维李代数。则存在正整数 $n$ 与单同态
$$
\rho:\mathfrak{g}\hookrightarrow\mathfrak{gl}(n,k),\qquad \rho([X,Y])=[\rho(X),\rho(Y)].
$$
即 $\mathfrak{g}$ 同构于 $\mathfrak{gl}(n,k)$ 的某个子代数，$n$ 可取不超过 $\dim\mathfrak{g}$ 的某个界。特别地，每个有限维李代数都是线性的（linear）。

## 四、证明过程

**证明（归约 + 可解情形）：**

**步骤 1：Levi 分解。** 每个有限维李代数有分解 $\mathfrak{g}=\mathfrak{r}\rtimes\mathfrak{s}$，其中 $\mathfrak{r}=\operatorname{rad}\mathfrak{g}$ 是极大可解理想（Levi 因子），$\mathfrak{s}$ 半单。记 $\dim\mathfrak{s}=m$。

**步骤 2：半单部分的忠实性。** 由 Cartan 判别法，$\mathfrak{s}$ 半单当且仅当其 Killing 型非退化；半单李代数的中心为零。于是伴随表示 $\operatorname{ad}:\mathfrak{s}\to\mathfrak{gl}(\mathfrak{s})$ 的核为中心 $=0$，故 $\mathfrak{s}\to\mathfrak{gl}(\mathfrak{s})$ 是单同态。

**步骤 3：归约为可解核的忠实性。** 设 $(\sigma,V)$ 是 $\mathfrak{r}$ 的忠实有限维表示。构造 $\mathfrak{g}$-模 $M=V^{\oplus (m+1)}$：$\mathfrak{r}$ 按 $\sigma$ 分别作用在每个直和项上；对 $X\in\mathfrak{s}$，利用 $\mathfrak{s}$ 通过 $\operatorname{ad}$ 作用在 $\mathfrak{r}$ 上，令 $X$ 把第 $i$ 项映到第 $i+1$ 项并与 $\sigma(\operatorname{ad}X)$ 复合：
$$
X\cdot(v_0,\dots,v_m)=\big(0,\ \sigma(\operatorname{ad}X)v_0,\ \sigma(\operatorname{ad}X)v_1,\dots,\sigma(\operatorname{ad}X)v_{m-1}\big).
$$
直接验证 $\mathfrak{g}$ 的括号关系成立（$\mathfrak{r}$-作用是模作用、$\mathfrak{s}$-作用按 Levi 分解的相容性），故 $M$ 是 $\mathfrak{g}$-模。若某 $Y=H+X\in\mathfrak{g}$（$H\in\mathfrak{r},X\in\mathfrak{s}$）在 $M$ 上作用为零，则其在第 $0$ 项上的作用给出 $\sigma(H)=0$，故 $H=0$；再看它在各次幂上的迭代，由 $\sigma$ 忠实与 $\operatorname{ad}X$ 在半单代数上的性质推出 $X=0$。因此 $\mathfrak{r}$ 在 $M$ 上作用忠实，$\mathfrak{g}$ 亦然（此处作用在 $M$ 上的表示忠实需要 $\mathfrak{r}$ 忠实且 $X\neq0$ 时在足够多直和项上出现，具体用 $\operatorname{ad}X\neq0$ 与 $\sigma$ 忠实逐项检验）。

**步骤 4：可解李代数有忠实有限维表示。** 对 $\dim\mathfrak{g}$ 归纳。因 $\mathfrak{g}$ 可解，$\mathfrak{g}\neq[\mathfrak{g},\mathfrak{g}]$，故存在余维 $1$ 理想 $\mathfrak{h}\triangleleft\mathfrak{g}$。由归纳假设取 $\mathfrak{h}$ 的忠实有限维表示 $(\rho_0,V)$。写 $\mathfrak{g}=\mathfrak{h}\oplus kx$（$x\notin\mathfrak{h}$）。

**步骤 5：Zassenhaus 提升。** 在 $W=\bigoplus_{i=0}^{N}V_i$（$V_i\cong V$）上定义 $\mathfrak{g}$ 的作用：对 $h\in\mathfrak{h}$，$h\cdot v_i=\rho_0(h)v_i$；对 $x$，
$$
x\cdot v_i=\rho_0(\operatorname{ad}x)\,v_i+v_{i+1}\quad(0\le i<N),\qquad x\cdot v_N=\rho_0(\operatorname{ad}x)\,v_N.
$$
（$\operatorname{ad}x$ 保 $\mathfrak{h}$，故 $\rho_0(\operatorname{ad}x)$ 有意义。）由 $\rho_0$ 是表示且 $\operatorname{ad}x$ 是 $\mathfrak{h}$ 的导子，可验证这定义出 $\mathfrak{g}$-模结构：关键是 $[h,x]=\operatorname{ad}x(h)$ 使 $h\cdot(x\cdot v_i)-x\cdot(h\cdot v_i)=\rho_0([h,\operatorname{ad}x])(v_i)+\dots$ 与 $\rho_0(\operatorname{ad}[h,x])$ 匹配，逐项检查即得。

**步骤 6：选 $N$ 够大使忠实。** 设 $H+\lambda x$ 在 $W$ 上作用为零。看第 $0$ 项的像：$\rho_0(H)v_0+\lambda v_1=0$，故 $v_1$ 分量给出 $\lambda$ 与 $\rho_0(H)$ 的关系。取 $N>\dim V$（例如 $N=\dim\mathfrak{h}+1$），反复迭代 $x\cdot$ 有
$$
x^k\cdot v_0=\sum_{j=0}^{k}\binom{k}{j}\rho_0(\operatorname{ad}x)^{k-j}v_j ,
$$
即可由作用为零推出 $\rho_0(H)=0$ 且 $\lambda\rho_0$ 的各级 $\rho_0(\operatorname{ad}x)^i=0$；由 $\rho_0$ 忠实与 $\operatorname{ad}x$ 的性质得 $H=0,\lambda=0$。故表示忠实，归纳完成。

**步骤 7：合并。** 由步骤 3 与 4，$\mathfrak{r}$ 有忠实表示，从而 $\mathfrak{g}$ 有忠实表示；再与步骤 2 的半单情形统一，即得 Ado 定理。$\square$

## 五、应用与意义

- 它是李群–李代数对应（李第三定理）的存在性前提：任意有限维实李代数都能"矩阵化"，才有对应的单连通李群。
- 它把抽象李代数的表示论归约为矩阵问题，使迹、行列式、特征多项式等线性代数工具可用于李代数。
- 在量子力学与数学物理中，物理的对称代数是抽象给出的，Ado 定理保证它们总有矩阵实现，从而可写成算符代数。
- 与 Levi 分解、Engel 定理、Lie 定理组合，构成有限维李代数结构理论的完整链条。
- 在代数群与特征 $p$ 情形有相应推广（Iwasawa、Jacobson），是线性李代数理论的基础。

## 相关条目

- [李群与李代数的对应定理](./李群与李代数的对应定理.md)：Ado 定理是其存在性证明的第一步归约。
- [Engel 定理与 Lie 定理](./Engel定理与Lie定理.md)：可解与幂零情形的结构定理，与本文的可解归纳配合。
- [半单李代数的分类定理](./半单李代数的分类定理.md)：半单部分由伴随表示提供忠实性所依赖的理论。
- [李群与李代数的对应](../第39级-李群与李代数/李群与李代数的对应.md)：Ado 定理在该条目的存在性证明中被引用。
- [Cartan 判别法](../第39级-李群与李代数/Cartan判别法.md)：判定半单性、进而保证伴随表示忠实。
- [Lie 定理](../第39级-李群与李代数/Lie定理.md)：可解李代数表示的上三角化结构定理。
