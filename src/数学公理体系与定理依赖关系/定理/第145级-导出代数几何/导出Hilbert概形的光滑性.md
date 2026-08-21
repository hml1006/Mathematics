# 导出Hilbert概形的光滑性
>
> **一句话大白话**：参数化各种琐碎 moduli 的（导出）Hilbert 概形，往往带有多余的切复杂——但导出几何可以把它变成"每点都分离、光滑"的良构空间。
>
> **小例子**：对曲线上的 h-coh 有效链条参数化的导出 Hilbert 空间，其自同构带来的多余切空间被 $\pi_{<0}$ 收纳，成为形变理论中 smooth 的对象。

## 一、定理介绍

导出Hilbert概形的光滑性讨论了把经典 Hilbert 概形派生化之后所得的导出对象在合适意义下的 smoothness。经典 Hilbert 概形常有 nilpotent/多余切结构；其派生版本（以导出张积/导出 universal family 构造）在导形态射资格下（切锥、cotangent complex 零阶）呈现光滑性，即全部多余切即压制。

## 二、原理思路

用派生形变理论审视：$\mathrm{Hilb}^\mathrm{der}_X$ 的 cotangent complex 由 universal family 与 push-forward 组合而来；其"多余"部分源于分解族（作为 quotient）的 kernel。导出结构把这一切用 $\pi_{<0}\Omega$ 承载，而光滑性即意味着这些同伦群消失且基本无组合障碍——使 moduli "派生光滑"。

## 三、定理的严格表述

设 $X$ 为（导出）概形/stack，考虑其导出 Hilbert 模 $\mathrm{Hilb}^{\mathrm{der}}_X$（参数化带分解态的闭子概形，即 quotient $B\to\mathcal{O}$ 结构）。则存在一可通过派生几何构造的概形/stack 对象 $H$，使得对每个包含 proper 平展的谱族，其所需万有族的派生结构存在且唯一，且 $H$ 的代数 tangent complex $\mathbb{T}_H$ 廉正交并光滑（享受切精确、障碍收敛）。

## 四、证明过程

构造上把 Hilbert 概形的经典定义（对 per级数族取 Pushforward）引入派生态：定义带分解 quotient 族与万有族，用 cotangent complex 的 stretch 推导干净 clean 条件；验证由 $\mathrm{Hilb}=\operatorname{Map}(B,\mathsf{Q})-\mathrm{stack}$ 的派生光滑性（$T_H$ 有限度、限制）。最后用派生叠性质与多叶局部化证明 smoothness 与完整切结构。

## 五、应用与意义

导出 Hilbert/moduli 理论提供了在参数化问题中处理额外切与障碍的鲁棒框架，广泛应用于导出模空间、Donaldson–Thomas 不变量的定义与"派生碰撞"记数，是导出代数几何中"让 moduli 光滑化"的核心范例。