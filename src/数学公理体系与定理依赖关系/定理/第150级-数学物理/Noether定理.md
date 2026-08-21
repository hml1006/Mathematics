# Noether定理

> **一句话大白话**：每个连续对称性都对应一条守恒律——作用量在连续变换下不变，就必然存在守恒流与守恒荷。
>
> **小例子**：时间平移对称 $\Rightarrow$ 能量守恒；空间平移对称 $\Rightarrow$ 动量守恒；旋转对称 $\Rightarrow$ 角动量守恒；$U(1)$ 对称 $\Rightarrow$ 电荷守恒。由 $j^\mu$ 满足 $\partial_\mu j^\mu=0$。

## 一、定理介绍

Noether 定理（E. Noether 1918）是理论物理与数学物理最基础的定理之一：若作用量 $S[\phi]$ 在单参数（连续）Lie 群变换下不变，则存在守恒流 $j^\mu$（$\partial_\mu j^\mu=0$），其荷 $Q=\int j^0\,d$ 在时间演化下守恒（$\dot Q=0$）。它把"对称性"与"守恒量"一一对应，是现代场论公理化的出发点。

## 二、原理思路

思路是变分法的直接应用：对满足运动方程（Euler–Lagrange）场，作用量对参数改变量 $\delta S=0$；把 $\delta S$ 展开成对 $j^\mu$ 的散度并利用运动方程消去体贡献，得到 $\partial_\mu j^\mu=0$。荷的守恒由 Gauss 定理（空间无穷远衰减）给出。关键是识别"Noether 流"的表达式。

## 三、定理的严格表述

设 $S[\phi]=\int L(\phi,\partial_\mu\phi)\,d^dx$ 在单参数变换 $x^\mu\to x^\mu+\epsilon X^\mu$、$\phi\to\phi+\epsilon\Psi$ 下不变。则对任意满足运动的 $\phi$ 存在守恒流
$$
j^\mu=\frac{\partial L}{\partial(\partial_\mu\phi)}(\Psi-X^\nu\partial_\nu\phi)+L X^\mu,
$$
满足 $\partial_\mu j^\mu=0$；且荷 $Q=\int j^0 d^{d-1}x$ 满足 $\frac{dQ}{dt}=0$（空间衰减足够快下）。

## 四、证明过程

写下 $\delta S$（分零部件与体积变化），用运动方程约化体项所得散度为零；构造 Noether 流 $j^\mu$；再由 $\partial_\mu j^\mu=0$ 与 Gauss 定理推 $\dot Q=\int\partial_i j^i=0$。特例：时空平移给出能量-动量张量 $T^{\mu\nu}$、旋转给出角动量、内对称给出荷。

## 五、应用与意义

Noether 定理确立了"对称性$\Rightarrow$守恒律"的普遍原理，是经典与量子场论、引力、规范理论的基础：它给出能量-动量张量、守恒荷与对称群表示的联系，也是量子化与重整化的粒度框架，贯穿现代物理的座标。