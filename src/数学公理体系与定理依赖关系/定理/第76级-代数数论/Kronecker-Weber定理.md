# Kronecker-Weber 定理

> **一句话大白话**：$\mathbb{Q}$ 上的"阿贝尔扩张"（Galois 群可交换的扩张）看起来五花八门，其实全都"藏在"分圆域当中——任何这样的扩张都是某个 $\mathbb{Q}(\zeta_m)$ 的子域。
>
> **小例子**：$\mathbb{Q}(\sqrt2)$ 的 Galois 群是 $\mathbb{Z}/2\mathbb{Z}$（阿贝尔），可由分圆域说明：$\sqrt2\in\mathbb{Q}(\zeta_8)$，因为 $1+\zeta_8+\zeta_8^{-1}=\sqrt2$（$\zeta_8=e^{2\pi i/8}$）。更一般地，所有二次域都是某分圆域的子域。

## 一、定理介绍

Kronecker-Weber 定理论断：$\mathbb{Q}$ 的每个有限阿贝尔扩张都包含在某个分圆扩张 $\mathbb{Q}(\zeta_m)$ 中。换言之，所有阿贝尔扩张均由单位根生成。此定理是类域论在 $\mathbb{Q}$ 上的特例与优美封顶，也是 Hilbert 胆士"Kronecker 青春之梦"（论想要更多活动元构造更多扩张）的最简单情形。

## 二、原理思路

经典证明借助类域论：$\mathbb{Q}$ 的每个阿贝尔扩张 $K/\mathbb{Q}$ 对应一个"模 $m$ 的射线类群"（即 $\operatorname{Gal}(K/\mathbb{Q})\cong I_K^{\mathfrak m}/P_K^{\mathfrak m}$），而射线类群又可通过分圆域 $\mathbb{Q}(\zeta_m)$ 实现（因 $\operatorname{Gal}(\mathbb{Q}(\zeta_m)/\mathbb{Q})\cong(\mathbb{Z}/m\mathbb{Z})^\times$ 恰为模 $m$ 的互素类群）。由局部 Artin 映射与互反律锁定导子，可证明 $K\subseteq\mathbb{Q}(\zeta_m)$。

## 三、定理的严格表述

设 $K/\mathbb{Q}$ 是有限阿贝尔扩张（即 $K$ 是 $\mathbb{Q}$ 的有限 Galois 扩张且 $\operatorname{Gal}(K/\mathbb{Q})$ 是阿贝尔群）。则存在正整数 $m$，使
$$K\subseteq\mathbb{Q}(\zeta_m),$$
其中 $\zeta_m=e^{2\pi i/m}$ 是 $m$ 次本原单位根。事实上 $m$ 可取为 $K$ 的导子。

## 四、证明过程

**证明思路（类域论方法）：**

**步骤 1：局部情形。** 先证 $p$ 进版本：$\mathbb{Q}_p$ 的每个阿贝尔扩张是分圆扩张（或某些 $p$ 次根扩张）的子域。这由局部类域论（局部互反律，深入 Arjun 定理与局部 Kronecker-Weber）给出，为整体情形打基础。$\blacksquare$

**步骤 2：整体导子。** 对整体阿贝尔扩张 $K/\mathbb{Q}$，由类域论存在一个模（导子）$m$（不同的分歧处取局部导子的乘积），以及射线类群到 $\operatorname{Gal}(K/\mathbb{Q})$ 的 Artin 映射满同态，核为射线类群 $P_K^m$。$\blacksquare$

**步骤 3：用分圆域实现。** 考虑分圆域 $\mathbb{Q}(\zeta_m)$。其 Galois 群是 $(\mathbb{Z}/m\mathbb{Z})^\times$（阿贝尔），且 $\mathbb{Q}(\zeta_m)$ 的导子整除 $m$。由（整体）类域论，存在唯一子域 $K'\subseteq\mathbb{Q}(\zeta_m)$ 恰好"承载"模 $m$ 的 Artin 映射与 $K$ 相同（因 $K$ 对应的模整除 $m$，而 $\mathbb{Q}(\zeta_m)$ 覆盖所有"模 $m$ 的阿贝尔扩张"）。$\blacksquare$

**步骤 4：结论。** 由唯一性，$K=K'$，从而 $K\subseteq\mathbb{Q}(\zeta_m)$。$\square$

（注：亦存在不依赖完整类域论的初等证明，基于非分歧基底的 Chenevier 构型，但类域论是经典叙述。）$\square$

## 五、应用与意义

Kronecker-Weber 定理是"算术的阿贝尔类域"的漂亮封顶：它断言 $\mathbb{Q}$ 上所有阿贝尔扩张均可由单位根显式生成——即 $\operatorname{Gal}(\mathbb{Q}^{\mathrm{ab}}/\mathbb{Q})\cong\widehat{\mathbb{Z}}^\times$（整体类域论）。它是 Langlands 纲领与全局互反律的原始模型，也激发 Hilbert 第 12 问题（对一般域寻求类似"类域"的显式构造，虚二次域用椭圆函数复数乘）。在算法上配合分圆域提供了构造所有阿贝尔扩张的实用方法。