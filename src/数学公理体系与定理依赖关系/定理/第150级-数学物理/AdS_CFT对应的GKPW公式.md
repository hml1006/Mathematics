# AdS_CFT对应的GKPW公式
>
> **一句话大白话**：AdS 引力配分函数与边界 CFT 生成泛函相等——AdS 里场的边界值看成 CFT 中算子的源。
>
> **小例子**：对标量场、边界条件下
$$
\Big\langle \exp\Big(\int_{\partial AdS}\phi_0\mathcal O\Big)\Big\rangle_{\mathrm{CFT}}=Z_{\mathrm{AdS}}[\phi_0]=\int_{\phi|_{\partial}=\phi_0}\mathcal D\phi\,e^{-S_{\mathrm{AdS}}[\phi]},
$$
即 GKPW 公式。

## 一、定理介绍

> **前置依赖**：AdS时空几何、共形场论(CFT)、全息原理与AdS/CFT对偶、路径积分配分函数、Witten图与生成泛函

AdS/CFT 对应的 GKPW 公式（Gubser–Klebanov–Polyakov 1998；Witten 1998）给出反de Sitter 空间中量子引力与边界共形场论对偶的精确数学表述：$d+1$ 维 AdS 中场的边界值 $\phi_0$ 作为 $d$ 维 CFT 算子 $\mathcal O$ 的源，且 CFT 生成泛函等于 AdS 配分函数。它是"全息原理"的算符形式。

## 二、原理思路

对偶链（Maldacena）提示 $\operatorname{String\,on\,AdS_{d+1}\times X}\Leftrightarrow \mathrm{CFT}_d$。把 CFT 生成泛函（对 braket 插 vbl）与 AdS 配分（有边界条件 $\phi_0$）等值：AdS 场 $\phi(z,x)\sim z^{d-\Delta}\phi_0(x)+z^\Delta\phi_1(x)$ 决定共形维数 $\Delta=\frac d2+\sqrt{\frac{d^2}{4}+m^2R^2}$；在半经典极限 $Z\simeq e^{-S_{\mathrm{on-shell}}}$ 给出 CFT 关联函数的 Witten 树计算。

## 三、定理的严格表述

设 $\operatorname{AdS}_{d+1}$ 具 Poincaré 坐标 $ds^2=\frac{R^2}{z^2}(dz^2+\eta_{\mu\nu}dx^\mu dx^\nu)$，边界 $\partial$（$z=0$）。对标量场 $\phi$（质量 $m$）与边界值 $\phi_0$：
$$
\Big\langle \exp\Big(\int\phi_0\,\mathcal O\Big)\Big\rangle_{\mathrm{CFT}}\;=\;Z_{\mathrm{AdS}}[\phi_0].
$$
$\mathcal O$ 共形维数 $\Delta=\frac d2+\sqrt{\frac{d^2}{4}+m^2R^2}$；半经典近似得 $\langle \mathcal O\mathcal O\rangle\simeq C_\Delta/|x-y|^{2\Delta}$。

## 四、证明过程

先求标量场在 AdS 的解与边界渐近（$z^{d-\Delta}\phi_0+z^\Delta\phi_1$）；把作用量化为边界态（on-shell）；援引弦-几何陈设的对偶（Maldacena 1997）获得等值；以鞍点近似 $Z_{\mathrm{AdS}}\approx e^{-S_{\mathrm{on-shell}}}$ 计算两点/多点关联函数（Witten 图）以验证 CFT 形式（幂律 + 谱匹配、等距群 $SO(d,2)$）。

## 五、应用与意义

GKPW 使 AdS/CFT 成为可计算全息框架：提供弦论态到 CFT 关联的显式对应，支撑热力学/黑洞、重态修正与纠缠熵研究，并用解析工具（Witten diagram）连同相变方程直达强耦合规范理论。它是现代全息/共形场论必遵的核心。