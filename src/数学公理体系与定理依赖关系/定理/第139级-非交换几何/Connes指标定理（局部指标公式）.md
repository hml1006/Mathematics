# Connes指标定理（局部指标公式）

> **一句话大白话**：非交换版的 Atiyah-Singer 指标定理：一个椭圆形算子的"解析指标"（核减余核的维数差）能用"两极账本"——解析的账（散一段）与拓扑/循环上同调的账（特征数）——精确算出来，哪怕空间根本没有"点"的概念。
>
> **小例子**：经典情形 $\mathrm{Index}(D_+)=\int_X\hat A(R)\wedge\mathrm{ch}(a)$；Connes 把它推广到谱三元组 $(\mathcal A,\mathcal H,D)$，用热核或 JLO 循环余链把指标写成"超迹 + 非交换留数"的局部公式。

## 一、定理介绍

Connes 指标定理（局部指标公式）把 Atiyah-Singer 指标定理推广到非交换几何。对 $d$ 维偶数分次谱三元组 $(\mathcal A,\mathcal H,D)$ 与分次 $\gamma$，对任意 $a\in\mathcal A$ 有
$$
\mathrm{Index}(D_a^+)=\mathrm{Tr}_s(\gamma\,ae^{-tD^2})=\int\hat A(\nabla)\wedge\mathrm{ch}(a),
$$
其中 $D_a$ 为 $D$ 与 $a$ 的耦合，$\mathrm{Tr}_s$ 为超迹，$\hat A$ 为的符号，$\mathrm{ch}$ 为陈特征。它统一并推广了经典指标定理到非交换几何。

## 二、原理思路

证明沿"麦克斯金-辛格恒等式 + 热核展开 + 循环上同调"推进。McKean-Singer 指出指标与 $t$ 无关：$\mathrm{Index}(D_+)=\mathrm{Tr}_s(\gamma e^{-tD^2})$。当 $t\to0^+$，热核 $e^{-tD^2}$ 有渐近展开 $a_k(a,D^2)$，限定即 $\hat A$-类与陈特征；Connes 洞察到该局部指标可写成**循环上同调**语言（JLO 余链），用非交换留数表达，回代几何情形恢复 Atiyah-Singer。

## 三、定理的严格表述

设 $(\mathcal A,\mathcal H,D)$ 为 $d$ 维偶数度谱三元组，$\gamma^2=1$，$\gamma D=-D\gamma$，$[D,\pi(a)]$ 有界，$(D^2+1)^{-1/2}$ 紧。则对任意 $a\in\mathcal A$
$$
\mathrm{Index}(D_a^+)=\int\hat A(\nabla)\wedge\mathrm{ch}(a)
=\langle[\phi_D],\,[a]\rangle,
$$
其中 $\phi_D(a_0,\dots,a_n)=\mathrm{Tr}_s(\gamma a_0[D,a_1]\cdots[D,a_n]e^{-tD^2})$ 的极限定义循环上同调类 $[\phi_D]\in HC^*(\mathcal A)$。

## 四、证明过程

**步骤1：McKean-Singer 公式。** 对任意 $t>0$，
$$
\mathrm{Index}(D_+)=\mathrm{Tr}_s(\gamma e^{-tD^2})=\mathrm{Tr}(\gamma e^{-tD^2}|_{\mathcal H_+})-\mathrm{Tr}(\gamma e^{-tD^2}|_{\mathcal H_-}),
$$
指标与 $t$ 无关。

**步骤2：热核渐近展开。** $t\to0^+$ 时热核有系数 $a_k(a,D^2)$ 的局部几何展开，
$$
\mathrm{Tr}(ae^{-tD^2})\sim\sum_{k=0}^{\infty}t^{(k-d)/2}a_k(a,D^2).
$$

**步骤3：局部指标公式。** 偶数维下 $t\to0^+$ 时
$$
\mathrm{Tr}_s(\gamma ae^{-tD^2})\to\int_X\hat A(R)\wedge\mathrm{ch}(a),
$$
$\hat A(R)$ 由曲率 $R$ 决定、$\mathrm{ch}(a)$ 为陈特征形式。

**步骤4：循环余链表示。** 定义循环余链 $\phi_D(a_0,\dots,a_n)=\mathrm{Tr}_s(\gamma a_0[D,a_1]\cdots[D,a_n]e^{-tD^2})$，其极限定义循环上同调类 $[\phi_D]$。

**步骤5：JLO 余链。** Jaffe-Lesniewski-Osterwalder 构造
$$
\mathrm{Ch}_t(D)(a_0,\dots,a_n)=\int_{\Delta_n}\mathrm{Tr}_s\!\big(\gamma a_0e^{-s_0tD^2}[D,a_1]e^{-s_1tD^2}\cdots[D,a_n]e^{-s_ntD^2}\big)ds,
$$
为循环余链且上同调类与 $t$ 无关。

**步骤6：非交换留数。** 定义 $\int a=\mathrm{Res}_{s=0}\mathrm{Tr}(a|D|^{-s})$，Wodzicki 留数与 Dixmier 迹的关系给出循环上同调类。

**步骤7：指标定理的循环版本。** $\langle[\phi_D],[a]\rangle=\mathrm{Index}(D_a^+)$，其中左为循环上同调与 K-理论类的配对。

**步骤8：回到几何。** $\mathcal A=C^\infty(M)$、$D$ 为 Dirac 算子时，$\phi_D$ 对应 $\hat A$-类，恢复经典 Atiyah-Singer 指标定理。

**结论（$\square$）**：Connes 局部指标公式统一并推广指标定理到非交换几何。

## 五、应用与意义

Connes 指标定理是非交换几何核心成果，为"无点空间上的指标理论"提供严格框架，联系热核、循环上同调与拓扑。它在叶状结构指标、非交换环面指标、以及标准模型几何化中都发挥关键作用，是非交换流形的拓扑-解析桥接基石。