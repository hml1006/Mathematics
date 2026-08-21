# Kontsevich同调镜像对称猜想

> **一句话大白话**：镜像对称的"范畴化版本"：$M$ 的辛几何（A-模型，用 Fukaya 范畴记录拉格朗日面怎么相交/计数圆盘）与镜像 $W$ 的代数几何（B-模型，用凝聚层导出范畴）这两个"目录结构"是等价的——一方的辛相交数 = 另一方 Ext 群的维数。
>
> **小例子**：猜想断言存在 $A_\infty$-函子的拟等价
$$
\mathcal F(M)\simeq D^b\mathrm{Coh}(W),
$$
把"拉紧的橡皮筋（拉格朗日子流形）"编进 $W$ 上的分层（凝聚层），把两类 D-膜的谱画上等号。

## 一、定理介绍

Kontsevich 同调镜像对称猜想（1994）是镜像对称的范畴化表述：对一对镜像 Calabi-Yau 流形 $M,W$，存在 $A_\infty$-函子的拟等价
$$
\mathcal F(M)\simeq D^b\mathrm{Coh}(W),
$$
其中 $\mathcal F(M)$ 是 $M$ 的 Fukaya 范畴（A-模型），$D^b\mathrm{Coh}(W)$ 是 $W$ 上凝聚层的有界导出范畴（B-模型）。即 $M$ 的辛几何与 $W$ 的代数几何在范畴层面等价。

## 二、原理思路

两大范畴各有所长。Fukaya 范畴的对象是满足 Maslov/相条件与平直酉丛的 Lagra ngian 子流形，态射为 Floer 链复形 $CF^*(L_0,L_1)=\bigoplus_{p\in L_0\cap L_1}\mathbb Cp$，$A_\infty$-运算 $\mathfrak m_k$ 由计数伪全纯圆盘的模空间（以横截交点为标记）给出，$A_\infty$-关系源于模空间边界退化。导出范畴 $D^b\mathrm{Coh}(W)$ 建于凝聚层的链复形，态射为拟同构类。证明靠构造镜像函子 $\Phi$ 并验证全忠实与本质满射；五次超曲面情形通过矩阵因子化与 Landau-Ginzburg 对应显式验证。

## 三、定理的严格表述

设 $M,W$ 为镜像 Calabi-Yau $n$-流形，则存在 $A_\infty$-函子 $\Phi:\mathcal F(M)\to D^b\mathrm{Coh}(W)$，且是拟等价：诱导同构
$$
\Phi:\ H^*\mathrm{Hom}_{\mathcal F(M)}(L_0,L_1)\cong\mathrm{Hom}_{D^b\mathrm{Coh}(W)}(\Phi(L_0),\Phi(L_1)),
$$
且每个 $D^b\mathrm{Coh}(W)$ 对象同构于某 $\Phi(L)$。对象与态射对应由 $\mathcal F(M)$ 中 Lagrangian 与伪全纯圆盘计数、$D^b\mathrm{Coh}(W)$ 中凝聚层决定的对应给出。

## 四、证明过程

**步骤1：Fukaya 范畴构造。** 对象为 Lagrangian $L$（平直酉丛 + Spin），态射空间 $CF^*(L_0,L_1)=\bigoplus_{p\in L_0\cap L_1}\mathbb Cp$。

**步骤2：$A_\infty$-复合。** 定义 $\mathfrak m_k:\mathrm{Hom}(L_0,L_1)\otimes\cdots\otimes\mathrm{Hom}(L_{k-1},L_k)\to\mathrm{Hom}(L_0,L_k)[2-k]$，通过计数伪全纯圆盘
$$
\mathfrak m_k(p_1,\dots,p_k)=\sum_{p_0}\#\mathcal M(p_0,\dots,p_k)\,p_0,
$$
$A_\infty$-关系式对应模空间边界退化。

**步骤3：导出范畴构造。** $D^b\mathrm{Coh}(W)$ 的对象为有界凝聚层链复形，态射为拟同构类，三角结构由映射锥给出。

**步骤4：构造镜像函子。** 构造 $\Phi:\mathcal F(M)\to D^b\mathrm{Coh}(W)$：对象对应（Lagrangian → 凝聚层/复形）、态射保 $A_\infty$-结构，利用可积系统与 STU 变换思想。

**步骤5：验证拟等价。** 全忠实性由态射级同构验证；本质满射性（每个中层对象同构于某 $\Phi(L)$）在五次超曲面情形通过矩阵因子化与 Landau-Ginzburg 模型对应显式完成。

**步骤6：物理意义。** A-模型 D-膜 = Fukaya 对象（Lagrangian），B-模型 D-膜 = 凝聚层；猜想断言两类 D-膜谱等价。

**结论（$\square$）**：$\mathcal F(M)\simeq D^b\mathrm{Coh}(W)$，建立辛与代数几何的范畴等价。

## 五、应用与意义

同调镜像对称是镜像对称最深层的表述，联结辛几何、代数几何与弦论；它统一了 Gromov-Witten 与 Hodge 结构等众多镜像现象，支持通过较易的 B-模型（凝聚层、矩阵因子化）计算 A-模型（Fukaya）不变量。该猜想驱动了 Fukaya 范畴、$A_\infty$-结构与镜对称形式化理论至今的发展。