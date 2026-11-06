# 第77级-算术几何

> 一句话级别概述：算术几何是现代数论与代数几何的交叉核心，用代数簇的几何结构来研究数域上有理点、有限域上点数的算术性质，并以 Faltings 定理、Mordell-Weil 定理与谷山-志村定理为三大支柱。

## 级别简介

本级别研究代数簇（尤其是椭圆曲线与亏格 $\ge2$ 的光滑曲线）在数域、有限域上的算术性质：有理点集的代数结构、有限域上点数的精确刻画，以及椭圆曲线与模形式之间的深层对应。核心内容包括 Mordell-Weil 定理（有限生成性）、椭圆曲线的 Weil 猜想（Hasse 界）、Faltings 定理（有理点有限性）以及谷山-志村定理。

## 本级别定理

- [Mordell-Weil定理](./Mordell-Weil定理.md)：椭圆曲线数域上的有理点构成有限生成阿贝尔群。
- [椭圆曲线的Weil猜想](./椭圆曲线的Weil猜想.md)：有限域上椭圆曲线点数满足准平方根级 Hasse 界。
- [谷山-志村定理](./谷山-志村定理.md)：$\mathbb{Q}$ 上每条椭圆曲线对应一个权 2 模形式。
- [Faltings定理](./Faltings定理.md)：亏格 $\ge2$ 的曲线在数域上有理点仅有有限多个。

- [弱 Mordell-Weil 定理](./弱Mordell-Weil定理.md)：若 $E(K)/mE(K)$ 对某 $m\ge2$ 有限，则 $E(K)$ 有限生成，故 Mordell-Weil 定理归结为有限性。
- [Néron-Tate 高度](./Néron-Tate高度.md)：典范高度 $\hat h$ 是 $E(K)$ 上的二次型，$\langle P,Q\rangle=\tfrac12(\hat h(P+Q)-\hat h(P)-\hat h(Q))$ 为非退化配对，其秩等于 $E(K)$ 的秩。
- [椭圆曲线的模曲线](./椭圆曲线的模曲线.md)：$Y_0(N)$ 的参数空间参数化带 $N$-同源的椭圆曲线对，模性定理即 $X_0(N)\to E$ 的存在性。
- [平展上同调](./平展上同调.md)：$\ell$-adic 平展上同调 $H^i_{\text{ét}}(X,\mathbb Q_\ell)$ 满足 Poincaré 对偶、Künneth 公式与基变换，是 Weil 猜想的载体。
- [Néron 模型](./Néron模型.md)：局部域上椭圆曲线存在极小正则整模型，其特殊纤维的约化类型（良好/乘性/加性）由 $j$ 不变量的赋值决定。
- [Tate-Shafarevich 群与 Selmer 群](./Tate-Shafarevich群与Selmer群.md)：$\mathrm{Sel}_m(E/K)\to E(K)/mE(K)\to Ш(E/K)[m]$ 正合，Selmer 群可计算而 $Ш$ 度量局部-整体障碍。
- [Schlessinger 形变理论](./Schlessinger形变理论.md)：形变函子可表（有形式 moduli）当且仅当满足 Schlessinger 条件 $H_0$–$H_2$。

## 前置知识

本级别依赖前序的代数几何基础（曲线的亏格、Jacobi 簇、光滑代数簇）、数域上的代数数论，以及模形式的基础知识。它通常建立在初等数论、椭圆曲线入门与有限域上的代数簇理论之上。

## 后继用途

本级别为朗兰兹纲领、椭圆曲线与模形式理论、丢番图方程的现代解法（如 Chabauty-Kim）以及算术代数几何的深化提供基础，也是证明 Fermat 大定理的关键环节。

## 关键定理速览

- Faltings 定理（Mordell 猜想）：亏格 $\ge2$ 曲线有理点有限。
- Mordell-Weil 定理：椭圆曲线有理点群有限生成。
- 谷山-志村定理：椭圆曲线与模形式的对应，通向模性提升与 Fermat 大定理。
- 椭圆曲线的 Weil 猜想（Hasse 界）：有限域点数的高精度估计。
