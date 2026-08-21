# Kutta-Joukowski定理

> **一句话大白话**：机翼能获得升力，根源在于绕它有一圈“环量”；升力大小等于密度×来流速度×环量，且垂直于来流。
>
> **小例子**：调整机翼攻角带来适当环量 $\Gamma$，升力 $L=\rho U\Gamma$ 就足以托起飞机；若环量为零（对称无偏转）则升力也为零。

## 一、定理介绍

> **前置依赖**：复变函数全纯性与留数定理、Laurent展开、Bernoulli方程、Blasius定理、不可压缩势流理论。

Kutta-Joukowski 定理（升力定理）给出二维不可压缩势流中一个关键结论：单位展长升力 $L=\rho U\Gamma$，其中 $\Gamma$ 为绕物体的环量。它揭示了升力的本质机制，是空气动力学与机翼理论的基石。

## 二、原理思路

用复势 $w(z)$ 表示势流，远场 Laurent 展开中含环量项 $\frac{i\Gamma}{2\pi}\ln z$。由 Bernoulli 求压力、Blasius 定理把合力化为复速度平方的围道积分，用留数定理计算得到升力。

## 三、定理的严格表述

设二维不可压缩势流来流速度为 $U$，流体密度 $\rho$，绕任意形状物体环量为 $\Gamma$，则单位展长升力
$$
L=\rho U\Gamma,
$$
升力方向垂直于来流方向，且阻力为零（d'Alembert 伴谬）。

## 四、证明过程

1. **复势表示**。$w(z)=\phi+i\psi$，复速度 $\frac{dw}{dz}=u-iv$。
2. **远场展开**。$w(z)=Uz+\frac{i\Gamma}{2\pi}\ln z+\frac{a_1}{z}+\cdots$。
3. **Blasius 定理**。合力满足
   $$
   F_x-iF_y=\frac{i\rho}{2}\oint_C\Big(\frac{dw}{dz}\Big)^2dz.
   $$
4. **留数计算**。$\big(\frac{dw}{dz}\big)^2$ 中 $\frac1z$ 项系数为 $\frac{iU\Gamma}{\pi}$，围道积分为 $-2U\Gamma$，得
   $$
   F_x-iF_y=-i\rho U\Gamma\;\Longrightarrow\;F_x=0,\;F_y=\rho U\Gamma.
   $$

## 五、应用与意义

Kutta-Joukowski 定理解释了机翼升力的由来并量化其大小，是空气动力学设计与飞机性能分析的核心工具。它也澄清了理想势流中“环量即升力之源”这一重要物理思想，并引出 d'Alembert 伴谬等深层话题。