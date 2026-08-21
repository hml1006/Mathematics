# Tannaka-Krein 对偶定理

> **一句话大白话**：一个紧李群 $G$ 完全由其"行为卡片集"（$G$ 的表示范畴 $\operatorname{Rep}(G)$ 连同遗忘函子）决定——$G$ 恰好是同构于作为"保持张量积的自同构群" $\operatorname{Aut}^{\otimes}(F)$。
>
> **小例子**：$SO(3)$ 的不可约表示由自旋 $l=0,1,2,\dots$ 标记，张量积规则（$l_1\otimes l_2$ 的 Clebsch-Gordan 分解）完整记录了群的信息，以至从这些规则与遗忘函子就能重建 $SO(3)$。这个原理也是粒子物理中"量子数"猜想的基础。

## 一、定理介绍

Tannaka-Krein 对偶定理实现"对象由其对偶重建"：紧群的表示范畴（作为张量范畴，带遗忘函子）完全决定该群。它把表示论与范畴论连接起来，也是对"如何从对称性数据恢复原始结构"这一数学哲学问题的正回答。对 Hopf 代数更有一版本：$H\cong\operatorname{End}^{\otimes}(F)$。

## 二、原理思路

关键在于把恢复到"遗忘函子的张量自同构群"这一范畴论对象上。每个 $g\in G$ 定义自然变换 $\eta^{(g)}_V=\rho_V(g)$，与张量积相容，给出 $G\to\operatorname{Aut}^{\otimes}(F)$。单射性由 Peter-Weyl 定理（不可约表示分离 $G$ 的点）；满射性通过正则表示 $L^2(G)\cong\bigoplus_V V\otimes V^*$ 与 Schur 引理，把任意张量自同构化为某个 $g$ 的左乘。

## 三、定理的严格表述

设 $G$ 是紧李群，$\operatorname{Rep}(G)$ 是 $G$ 的有限维连续表示的张量范畴，配遗忘函子 $F:\operatorname{Rep}(G)\to\operatorname{Vect}_{\mathbb{C}}$。则：
$$
G\cong\operatorname{Aut}^{\otimes}(F),
$$
其中 $\operatorname{Aut}^{\otimes}(F)$ 是 $F$ 的张量自同构群（保持张量积与单位表示的自然变换构成的群）。更一般地，对任何 Hopf 代数 $H$，$H\cong\operatorname{End}^{\otimes}(F)$ 可从其表示范畴与遗忘函子恢复。

## 四、证明过程

**证明：**

**步骤 1：定义张量自同构群。** 遗忘函子 $F$ 把表示映到底向量空间。$F$ 的张量自同构是自然变换 $\eta:F\Rightarrow F$ 满足 $\eta_{V\otimes W}=\eta_V\otimes\eta_W$、$\eta_{\mathbf1}=\operatorname{id}_{\mathbb{C}}$；全体构成 $\operatorname{Aut}^{\otimes}(F)$。

**步骤 2：构造 $G\to\operatorname{Aut}^{\otimes}(F)$。** 对 $g\in G$ 定义 $\eta^{(g)}_V=\rho_V(g)$，因 $\rho_{V\otimes W}(g)=\rho_V(g)\otimes\rho_W(g)$，它是张量自同构，得群同态 $\phi:G\to\operatorname{Aut}^{\otimes}(F)$。

**步骤 3：单射性。** 若 $\phi(g)=\phi(h)$，则对一切 $V$ 有 $\rho_V(g)=\rho_V(h)$；由 Peter-Weyl 定理，不可约表示分离 $G$ 的点，故 $g=h$。

**步骤 4：满射性。** 任取 $\eta\in\operatorname{Aut}^{\otimes}(F)$。对正则表示 $L^2(G)\cong\bigoplus_V V\otimes V^*$，$\eta_{L^2(G)}$ 是 $G\times G$-等变的线性自同构。由 Schur 引理，它必是某个 $g\in G$ 的左乘，故 $\eta=\phi(g)$。

**步骤 5：Hopf 代数版本。** 对 Hopf 代数 $H$ 与遗忘函子 $F:\operatorname{Rep}(H)\to\operatorname{Vect}_k$，每个 $h\in H$ 定义 $\eta^{(h)}_V(v)=h\cdot v$，可证其给出 Hopf 代数同构 $H\cong\operatorname{End}^{\otimes}(F)$。$\square$

## 五、应用与意义

Tannaka-Krein 对偶是"对偶理论"的典范，它把紧群用其表示论刻画，是重建理论与量子对称（量子双、Drinfeld 对偶）、代数量子群与纤维函子理论的基础。在数学物理中，它为观测数据的对称性重建提供范式；在范畴论与代数几何（如 Tannakian 范畴）中，它奠定了"从纤维函子恢复代数群"的框架，是 Langlands 纲领与表示论统一视角的深层工具之一。