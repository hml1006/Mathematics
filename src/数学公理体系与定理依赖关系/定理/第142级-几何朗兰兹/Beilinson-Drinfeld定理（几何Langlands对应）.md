# Beilinson-Drinfeld定理（几何Langlands对应）

> **一句话大白话**：曲线上某种"带Hecke本征性质"的D-模，和另一侧"局部系统的拟凝聚层"是一回事——这就是曲线上的全局几何Langlands对应。
>
> **小例子**：对 $\mathrm{Bun}_G$ 上具有Hecke本征性质的D-模 $\mathcal{F}$，直觉上它对应 $\mathrm{LocSys}_{{}^LG}$ 上的一个拟凝聚层，满足对每个 $x$ 的 Hecke 算子 $H_{x,V}(\mathcal{F})\cong\sigma_V(x)\boxtimes\mathcal{F}$。

## 一、定理介绍

> **前置依赖**：Hecke算子与Hecke对应、D-模理论、局部系统与模空间LocSys、Fourier-Mukai变换、Opers

Beilinson-Drinfeld定理是几何Langlands纲领的核心成果：设 $X$ 为亏格 $g>1$ 的光滑射影曲线，$G$ 为约化群，则 $\mathrm{Bun}_G$ 上（带Hecke本征性质）的D-模的范畴与 $L$-群 $^LG$ 的局部系统模空间 $\mathrm{LocSys}_{{}^LG}$ 上的拟凝聚层的范畴等价。它将算术的 Langlands 对应翻译成层论的范畴等价。

## 二、原理思路

其核心是构造两个互逆函子：正方向由"给定局部系统 $\sigma\mapsto$ Hecke本征D-模 $\mathcal{F}_\sigma$"给出（经 $D$-模理论中的消去/唯一性）；逆方向把 Hecke本征D-模 $\mathcal{F}$ 映射到 $\mathrm{LocSys}_{{}^LG}$ 上的"谱层"，常经 Fourier–Mukai 型变换实现。等价的关键在于 Hecke 算子的一致性。

## 三、定理的严格表述

设 $X$ 为亏格 $g>1$ 的光滑射影曲线 $/\mathbb{C}$，$G$ 约化群。存在范畴等价
$$
\mathrm{D\text{-}mod}(\mathrm{Bun}_G)_{\mathrm{Hecke}}\cong \mathrm{QCoh}(\mathrm{LocSys}_{{}^LG}),
$$
其中左端指 $\mathrm{Bun}_G$ 上满足对每个 $x\in X$ 与表示 $V$ 都有 $H_{x,V}(\mathcal{F})\cong\sigma_V(x)\boxtimes\mathcal{F}$ 的D-模的范畴（$\sigma$ 为 $^LG$ 局部系统），右端为 $\mathrm{LocSys}_{{}^LG}$ 上拟凝聚层的范畴。当局部系统带正则奇性时，该等价与 Opers 亦相容。

## 四、证明过程

先定义 Hecke 对应 $\mathrm{Hecke}\subset \mathrm{Bun}_G\times X\times\mathrm{Bun}_G$ 及 Hecke 算子 $H_x=(p_1)_*\circ(p_2)^!$。其次定义 Hecke 本征层并构造正方向 $\Psi:\mathrm{QCoh}(\mathrm{LocSys}_{{}^LG})\to\mathrm{D\text{-}mod}_{\mathrm{Hecke}}$。再利用 Fourier–Mukai 型变换构造逆方向 $\Phi$，并验证 $\Phi\Psi\simeq\mathrm{id},\;\Psi\Phi\simeq\mathrm{id}$（经基点化与退化论证）。正则奇性情形用 Opers 与 Beilinson–Drinfeld 的消去原理给出更明确的构造。

## 五、应用与意义

该定理是几何Langlands对应最基本的严格结果，确立了层论框架下"自守/Fourier 对偶"的成对原理。它为随后由 Kapustin–Witten 提出、经 ABZ 与 Gaitsgory 发展的复杂化/范畴化奠定基础，并推动了 $p$-adic 与派生几何中对弦论全息、代沟函子等方向的追踪。

## 课堂问答

**老师**：请陈述 Beilinson–Drinfeld 定理，并说明左端为什么必须限制在"具 Hecke 本征性"的 D-模上。

**学生**：先给结论：对亏格 $g>1$ 的光滑射影曲线 $X/\mathbb{C}$ 与约化群 $G$，存在范畴等价 $\mathrm{D\text{-}mod}(\mathrm{Bun}_G)_{\mathrm{Hecke}}\cong \mathrm{QCoh}(\mathrm{LocSys}_{{}^LG})$，左端是满足 $H_{x,V}(\mathcal{F})\cong\sigma_V(x)\boxtimes\mathcal{F}$ 的 D-模。限制的原因：一般的 $\mathrm{D\text{-}mod}(\mathrm{Bun}_G)$ 太大、太"分析"，只有 Hecke 本征的部分才带有足够刚性去对应某个整体局部系统 $\sigma$；这正是两个范畴能成对的关键一致性条件。

**老师（追问）**：两个互逆函子各是怎么构造的？为什么要有 $g>1$？

**学生**：正方向 $\Psi:\mathrm{QCoh}(\mathrm{LocSys}_{{}^LG})\to\mathrm{D\text{-}mod}_{\mathrm{Hecke}}$ 由"给定局部系统 $\sigma$ 造 Hecke 本征 D-模 $\mathcal{F}_\sigma$"给出（用 D-模的消去/唯一性）；逆方向 $\Phi$ 把 $\mathcal{F}$ 映到谱层，经 Hecke 特征值的几何构造与 Fourier–Mukai 型变换实现，再验证 $\Phi\Psi\simeq\mathrm{id}$、$\Psi\Phi\simeq\mathrm{id}$。$g>1$ 的技术作用在于让 $\mathrm{LocSys}_{{}^LG}$ 与 Hecke 本征层具备所需的有限性/刚性（$g=0,1$ 需另行处理）。常见误区：以为等价对任意 $\mathrm{Bun}_G$ 的 D-模成立——实际只在 Hecke 本征子范畴上成立。

**老师（拓展）**：当局部系统带正则奇性时会发生什么？这条定理的地位如何？

**学生**：带正则奇性时 Hecke 本征模与 Opers 相容，可由 Beilinson–Drinfeld 的消去原理给出更明确的构造。这条定理是几何 Langlands 最基本的严格结果，确立了层论框架下"自守/Fourier 对偶"的成对原理，为其范畴化与 Kapustin–Witten 的物理对应奠定基础。
