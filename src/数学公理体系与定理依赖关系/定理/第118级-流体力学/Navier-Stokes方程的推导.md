# Navier-Stokes方程的推导

> **一句话大白话**：牛顿第二定律加上“流体不可压缩”与“粘性应力正比于变形率”两个假设，就推到出粘性流体的运动方程——Navier-Stokes 方程。
>
> **小例子**：一杯水里某小块的加速度等于压力差、粘性力和重力三者的和；这条“力平衡”用数学写出来就是 N-S 方程。

## 一、定理介绍

> **前置依赖**：牛顿第二定律（动量守恒）、质量守恒（连续性方程）、散度定理、应力张量与变形率张量、不可压缩性条件。

Navier-Stokes（N-S）方程描述粘性不可压缩流体的运动。它由质量守恒（连续性方程）与动量守恒（Cauchy 动量方程）配合牛顿流体本构关系推导而来，是现代流体力学与湍流研究的核心方程。

## 二、原理思路

从积分形式的守恒律出发，借助散度定理转化为微分形式，再把 Newton 流体的粘性应力 $\boldsymbol\tau=2\mu\boldsymbol D$ 代入动量方程，利用不可压缩性 $\nabla\cdot\boldsymbol u=0$ 化简即可。

## 三、定理的严格表述

粘性不可压缩流体的运动由下方程组描述
$$
\begin{cases}
\rho\left(\dfrac{\partial\boldsymbol u}{\partial t}+\boldsymbol u\cdot\nabla\boldsymbol u\right)=-\nabla p+\mu\nabla^2\boldsymbol u+\rho\boldsymbol f,\\[2mm]
\nabla\cdot\boldsymbol u=0.
\end{cases}
$$

## 四、证明过程

1. **连续性方程**。质量守恒得 $\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\boldsymbol u)=0$，不可压缩时 $\nabla\cdot\boldsymbol u=0$。
2. **动量方程**。由积分动量守恒与散度定理得
   $$
   \frac{\partial(\rho\boldsymbol u)}{\partial t}+\nabla\cdot(\rho\boldsymbol u\otimes\boldsymbol u)=\rho\boldsymbol f+\nabla\cdot\boldsymbol\sigma.
   $$
3. **本构关系**。Newton 流体 $\boldsymbol\sigma=-p\boldsymbol I+2\mu\boldsymbol D$，$\boldsymbol D=\frac12(\nabla\boldsymbol u+(\nabla\boldsymbol u)^\top)$。
4. **化简**。$\nabla\cdot\boldsymbol\tau=\mu\nabla^2\boldsymbol u$（因 $\nabla\cdot\boldsymbol u=0$），整理即得 N-S 方程。

## 五、应用与意义

N-S 方程在航空、海洋、气象与血流动力学中无处不在，其数学性质（光滑性与湍流唯一性）是千禧年问题之一。它是流体仿真与实验的理论基础，也是联系微观输运与宏观流动的桥梁。