# GL(1)的几何Langlands对应

> **一句话大白话**：$\mathrm{Pic}(X)$ 上的 D-模和 $X$ 的所有一秩局部系统上的层可以用傅里叶变换相互转换。
>
> **小例子**：对曲线 $X$，$\mathrm{LocSys}_{\mathbb{C}^\times}\cong(\mathbb{C}^\times)^{2g}$，而它恰好是 $\mathrm{Pic}(X)$ 的对偶环面——这是 Fourier 对偶的几何版。

## 一、定理介绍

> **前置依赖**：Abel簇与其对偶、Picard簇、Poincaré线丛、Fourier-Mukai变换、D-模与拟凝聚层

$GL(1)$ 情形的几何Langlands对应是把经典傅里叶对偶（Abel簇与其对偶环面）翻译成"层与表示"的语句：$\mathrm{Pic}(X)$ 上的 D-模的派生范畴与秩一局部系统模空间 $\mathrm{LocSys}_{\mathbb{C}^\times}$ 上拟凝聚层的派生范畴等价。这一等价经 Poincaré 线丛的 Fourier–Mukai 变换实现。

## 二、原理思路

$\mathrm{Bun}_1=\mathrm{Pic}(X)$ 是 $X$ 的 Picard 簇（交换代数群），其对偶是 $\mathrm{Pic}^\vee(X)=\mathrm{Hom}(\pi_1(X),\mathbb{C}^\times)$，即秩一局部系统的模空间 $\mathrm{LocSys}_{\mathbb{C}^\times}$。在 Abel 簇上的 Fourier–Mukai 变换（以 Poincaré 线丛为核）给出对偶环面间派生范畴的等价，其限制到适当子范畴即得几何 Langlands 对应，且 Hecke 算子在该对应下映为"乘以特征"。

## 三、定理的严格表述

设 $X$ 为亏格 $g$ 的光滑射影曲线，$\mathrm{Bun}_1=\mathrm{Pic}(X)$，$\mathrm{LocSys}_{\mathbb{C}^\times}=\mathrm{Hom}(\pi_1(X),\mathbb{C}^\times)\cong(\mathbb{C}^\times)^{2g}$。则存在范畴等价
$$
\mathrm{D\text{-}mod}(\mathrm{Bun}_1)\cong \mathrm{QCoh}(\mathrm{LocSys}_{\mathbb{C}^\times}),
$$
该等价由以 Poincaré 线丛 $\mathcal{P}$ 为核的 Fourier–Mukai 变换 $\mathrm{FM}_{\mathcal{P}}$ 实现，并将 Hecke 算子 $H_x$ 映为乘以局部系统在 $x$ 处取值 $\alpha(x)$ 的算子。

## 四、证明过程

先分析 $\mathrm{Bun}_1=\bigsqcup_d\mathrm{Pic}^d(X)$ 的结构，并确认 $\mathrm{LocSys}_{\mathbb{C}^\times}=\mathrm{Hom}(\pi_1(X),\mathbb{C}^\times)$。其次写出 Hecke 算子作用 $H_x:\mathcal{F}(\mathcal{L})\mapsto\mathcal{F}(\mathcal{L}(x))$。然后以 Poincaré 线丛为核定义 $\mathrm{FM}_{\mathcal{P}}:\mathrm{D\text{-}mod}(\mathrm{Pic}(X))\to\mathrm{QCoh}(\mathrm{LocSys}_{\mathbb{C}^\times})$。最后验证该傅里叶变换在 Abel 簇上给出自对偶等价，并检验 Hecke 本征性 $H_x(\mathcal{F}_\alpha)\cong\alpha(x)\mathcal{F}_\alpha$。

## 五、应用与意义

$GL(1)$ 情形是几何 Langlands 的"零号特例"，虽简单却确立了全部结构（Picard 簇、局部系统、Fourier–Mukai）。它被用作一般群情形的校准基准，并在算术几何、Shimura 簇与 $p$-adic 几何中持续作为对偶环面/傅里叶理论的蓝本。