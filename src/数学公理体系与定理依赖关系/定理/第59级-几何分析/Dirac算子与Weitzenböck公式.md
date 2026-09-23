# Dirac 算子与 Weitzenböck 公式

> **一句话大白话**：旋量丛上的 Dirac 算子平方之后，除了"联络拉普拉斯"这一分析项，还会凭空多出标量曲率的四分之一——曲率直接从算子代数里"跳"出来。

> **小例子**：在单位球面 $S^n$（标量曲率 $S=n(n-1)>0$）上，Lichnerowicz 公式 $D^2=\nabla^*\nabla+\frac14S$ 给出 $D^2\ge\frac14S>0$，故 $S^n$ 上不存在非零调和旋量；这正是 Lichnerowicz 消失定理，也是"正标量曲率阻碍 Spin 流形的 $\hat A$-亏格"的根源。

## 一、定理介绍

> **前置依赖**：旋量丛与 Spin 结构、Clifford 代数与 Clifford 乘法、Levi-Civita 联络与协变导数、Riemann 曲率张量、Bochner 公式、Hodge 分解定理。

Dirac 算子由物理学家 Paul Dirac 于 1928 年为写出相对论性电子方程而引入，其核心是"把二阶的 Klein–Gordon 方程开平方"：在 Clifford 代数中取一组满足 $c_ic_j+c_jc_i=-2\delta_{ij}$ 的矩阵（Dirac 矩阵），令 $D=\sum_ic_i\partial_i$，则 $D^2=-\Delta$。Atiyah 与 Singer 在 1963 年建立的指标定理则把这类"椭圆微分算子"的解析指标与流形的拓扑不变量联系起来，而 Dirac 算子是其中最重要的一类。

Weitzenböck 公式则是把这类"一阶算子的平方"与"联络拉普拉斯（Bochner 拉普拉斯）"作比较的一族恒等式。1918 年 Weitzenböck 与 Bochner 对 $p$-形式、旋量等对象给出了统一的形式：一阶算子的平方 = 联络拉普拉斯 + 由曲率构成的零阶项。对 Dirac 算子，这个零阶项恰好是标量曲率的 $\frac14$，即 Lichnerowicz 1963 年得到的

$$D^2=\nabla^*\nabla+\frac14S.$$

这条公式的意义堪称"曲率输入分析"的典范。因为它，Bochner 技巧可以整体地用于旋量：若 $S>0$ 则 $D$ 无零模，进而由指标定理知 Spin 流形的 $\hat A$-亏格为零，给出正标量曲率的拓扑障碍（Lichnerowicz 消失定理）。Witten 用同一公式对 Dirac 算子作 Bochner 论证给出了正质量定理的著名证明；Hitchin 用它构造反例说明某些流形不容许正标量曲率度量；在 Seiberg–Witten 理论、指标定理的局部化证明与旋量几何中，Weitzenböck 公式都是基本工具。

## 二、原理思路

1. **把 $D$ 写成 Clifford 乘法与协变导数的组合**：取局部正交标架 $\{e_i\}$，令 $D=\sum_ic(e_i)\nabla_{e_i}$，其平方为 $D^2=\sum_{i,j}c_ic_j\nabla_i\nabla_j$。

2. **把 $\nabla_i\nabla_j$ 拆成对称与反对称两部分**：$\nabla_i\nabla_j=\frac12(\nabla_i\nabla_j+\nabla_j\nabla_i)+\frac12(\nabla_i\nabla_j-\nabla_j\nabla_i)$。因为 $c_ic_j$ 关于 $i,j$ 反对称、而对称部分关于 $i,j$ 对称，求和时只有对角项 $i=j$ 存活，这给出 $\sum_ic_i^2\nabla_i\nabla_i=-\sum_i\nabla_i\nabla_i=\nabla^*\nabla$。

3. **反对称部分即曲率，经 Clifford 收缩给出标量曲率**：反对称部分 $\frac12(\nabla_i\nabla_j-\nabla_j\nabla_i)$ 就是旋量联络的曲率 $R^{\mathbb S}_{ij}$；再把它与 $c_ic_j$ 收缩。展开 $c_ic_jc_kc_l$ 并利用 Riemann 张量的对称性与第一 Bianchi 恒等式，所有项合并为 $\frac14S$。于是 $D^2=\nabla^*\nabla+\frac14S$。

## 三、定理的严格表述

**约定**：设 $(M^n,g)$ 为闭的 Spin 流形，$\mathbb{S}\to M$ 为旋量丛，Clifford 乘法满足

$$c_ic_j+c_jc_i=-2\delta_{ij},\qquad c_i^2=-1,$$

其中 $c_i=c(e_i)$。Dirac 算子定义为

$$D=\sum_{i=1}^nc(e_i)\nabla_{e_i},$$

$\nabla$ 为 $\mathbb S$ 上的旋量联络（Levi-Civita 联络的旋量提升），$\nabla^*\nabla=-\sum_i\nabla_{e_i}\nabla_{e_i}$ 为联络拉普拉斯（在局部正交标架下）。

**定理（Lichnerowicz 公式, 1963）**：

$$D^2=\nabla^*\nabla+\frac14S\,\mathrm{Id},$$

其中 $S$ 是 $M$ 的标量曲率。

**定理（带扭曲的 Weitzenböck 公式）**：设 $E\to M$ 是带联络的 Hermite 向量丛，考虑 $\mathbb S\otimes E$ 上的扭曲 Dirac 算子 $D_E$。则

$$D_E^2=\nabla^*\nabla+\frac14S+\mathcal R^E,$$

其中 $\mathcal R^E$ 是由 $E$ 的曲率经 Clifford 收缩得到的零阶自伴算子。

**推论（Lichnerowicz 消失定理）**：若 $S>0$ 处处成立，则 $\ker D=\{0\}$；由 Atiyah–Singer 指标定理，Spin 流形的 $\hat A$-亏格 $\hat A(M)=0$。

**依赖的概念**：Clifford 代数、旋量联络、曲率算子、联络拉普拉斯、指标定理。

## 四、证明过程

**步骤 1（展开 $D^2$）。** 取 $p$ 的邻域内的局部正交标架 $\{e_1,\dots,e_n\}$，并设其在 $p$ 处满足 $\nabla_{e_i}e_j|_p=0$（测地标架），故在 $p$ 处 $\nabla_i\nabla_j$ 只由导数与联络算子交换子产生。直接展开：

$$D^2=\Bigl(\sum_ic_i\nabla_i\Bigr)\Bigl(\sum_jc_j\nabla_j\Bigr)=\sum_{i,j}c_ic_j\nabla_i\nabla_j.$$

**步骤 2（分离出联络拉普拉斯）。** 把二阶导数对半拆开：

$$\nabla_i\nabla_j=\frac12\bigl(\nabla_i\nabla_j+\nabla_j\nabla_i\bigr)+\frac12\bigl(\nabla_i\nabla_j-\nabla_j\nabla_i\bigr).$$

记对称部分 $S_{ij}=\frac12(\nabla_i\nabla_j+\nabla_j\nabla_i)$、曲率部分 $R^{\mathbb S}_{ij}=\nabla_i\nabla_j-\nabla_j\nabla_i$。由于 $c_ic_j=-c_jc_i$，有

$$\sum_{i,j}c_ic_jS_{ij}=\sum_ic_i^2\nabla_i\nabla_i=-\sum_i\nabla_i\nabla_i=\nabla^*\nabla,$$

（非对角项因 $c_ic_j$ 反对称而两两相消）。而

$$\sum_{i,j}c_ic_j\cdot\tfrac12R^{\mathbb S}_{ij}=\sum_{i<j}c_ic_jR^{\mathbb S}_{ij},$$

（同样因反对称性，只剩 $i<j$ 的对）。于是

$$D^2=\nabla^*\nabla+\sum_{i<j}c_ic_jR^{\mathbb S}_{ij}.$$

**步骤 3（曲率项的 Clifford 收缩）。** 旋量联络的曲率由黎曼曲率张量给出：

$$R^{\mathbb S}_{ij}=\frac14\sum_{k,l}R_{ijkl}\,c_kc_l.$$

代入曲率项并展开 $c_ic_jc_kc_l$：把乘积按 Clifford 关系重写为 $\delta$ 型项与全反对称的四指标项之和，再用 $R_{ijkl}$ 关于 $(i,j)$、$(k,l)$ 的反对称性，含 $\delta_{ij}$ 或 $\delta_{kl}$ 的项全部为零；余下的四指标项经第一 Bianchi 恒等式 $R_{ijkl}+R_{jkil}+R_{kijl}=0$ 化简。把指标逐对收缩，Ricci 张量与标量曲率依次出现，最终只留下标量曲率：

$$\sum_{i<j}c_ic_jR^{\mathbb S}_{ij}=\frac14S\,\mathrm{Id}.$$

（这是一个纯代数恒等式：把五组指标配对、逐个用对称性消去后，唯一存活的是 $S= \sum_{i,j}R_{ijij}$ 这一收缩。）代入步骤 2 即得

$$D^2=\nabla^*\nabla+\frac14S\,\mathrm{Id}.$$

**步骤 4（Lichnerowicz 消失定理）。** 设 $\psi\in\ker D$，即 $D\psi=0$。在闭流形 $M$ 上对 $0=\langle D^2\psi,\psi\rangle$ 积分，用 $\int_M\langle\nabla^*\nabla\psi,\psi\rangle d\mu=\int_M|\nabla\psi|^2d\mu\ge0$（分部积分，$\nabla^*$ 为 $\nabla$ 的形式伴随）得

$$0=\int_M|D\psi|^2d\mu=\int_M|\nabla\psi|^2d\mu+\frac14\int_MS\,|\psi|^2d\mu.$$

若 $S>0$ 而 $\psi\ne0$，右端两项中后一项严格为正、前一项非负，矛盾。故 $\ker D=\{0\}$，再由 Atiyah–Singer 指标定理得 $\hat A(M)=\mathrm{ind}\,D=0$。$\square$

## 五、应用与意义

- **正标量曲率的拓扑障碍**：$S>0$ 蕴含 $\hat A(M)=0$，Lichnerowicz 消失定理与 Hitchin 的反例共同刻画了 Spin 流形能否承载正标量曲率度量。
- **正质量定理（Witten 证明）**：对渐近平坦流形上的 Dirac 算子作 Weitzenböck 与 Bochner 论证，把 ADM 质量表示为边界旋量积分。
- **指标定理**：Dirac 算子的解析指标等于拓扑指标，是 Atiyah–Singer 指标定理最重要的特例。
- **Seiberg–Witten 理论与旋量几何**：扭曲 Weitzenböck 公式是估计与消失定理的基本工具。
- **Bochner 技巧的统一框架**：$p$-形式、旋量、$\mathrm{Spin}^c$ 结构上的 Weitzenböck 公式共享同一结构。

## 相关条目

- [Bochner公式](../第49级-黎曼几何/Bochner公式.md)：函数与 1-形式上的 Weitzenböck 公式，本条目是它在旋量丛上的推广。
- [正质量定理](./正质量定理.md)：Witten 的证明以 Dirac 算子的 Lichnerowicz 公式为核心。
- [标量曲率的共形变换公式](./标量曲率的共形变换公式.md)：正标量曲率问题与消失定理密切相关。
- [Hodge分解定理](../第49级-黎曼几何/Hodge分解定理.md)：$p$-形式的 Hodge 理论与 Weitzenböck 公式是同类"一阶算子平方"的比较。
- [Riemann曲率张量的对称性](../第49级-黎曼几何/Riemann曲率张量的对称性.md)：步骤 3 的 Clifford 收缩依赖曲率张量的对称性与第一 Bianchi 恒等式。
