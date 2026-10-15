# Navier-Stokes方程的推导

> **一句话大白话**：牛顿第二定律加上“流体不可压缩”与“粘性应力正比于变形率”两个假设，就推到出粘性流体的运动方程——Navier-Stokes 方程。
>
> **小例子**：一杯水里某小块的加速度等于压力差、粘性力和重力三者的和；这条“力平衡”用数学写出来就是 N-S 方程。

## 一、定理介绍

> **前置依赖**：牛顿第二定律（动量守恒）、质量守恒（连续性方程）、高斯散度定理、应力张量与变形率张量、不可压缩性条件。

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

## 课堂问答

**老师**：用一句话说，Navier-Stokes 方程是"什么守恒"在"什么假设"下的产物？

**学生**：结论先行：它是质量守恒与动量守恒，在"不可压缩 + 牛顿流体本构 $\boldsymbol\sigma=-p\boldsymbol I+2\mu\boldsymbol D$"两条假设下的产物。积分守恒律经散度定理化为微分形式，本构代入动量方程即得
$$
\rho\left(\frac{\partial\boldsymbol u}{\partial t}+\boldsymbol u\cdot\nabla\boldsymbol u\right)=-\nabla p+\mu\nabla^2\boldsymbol u+\rho\boldsymbol f,\qquad \nabla\cdot\boldsymbol u=0 .
$$
常见误区是把 N-S 当成凭空规定的方程，它其实只是 $\dot{\boldsymbol p}=\text{合力}$ 的连续版本。

**老师（追问）**：化简中 $\nabla\cdot(2\mu\boldsymbol D)=\mu\nabla^2\boldsymbol u$ 这一步，凭什么成立？

**学生**：因为不可压缩 $\nabla\cdot\boldsymbol u=0$。展开 $\nabla\cdot(\nabla\boldsymbol u+(\nabla\boldsymbol u)^\top)=\nabla(\nabla\cdot\boldsymbol u)+\nabla^2\boldsymbol u=\nabla^2\boldsymbol u$，含 $\nabla(\nabla\cdot\boldsymbol u)$ 的项正是被不可压缩条件消掉的。若可压缩，就要保留 $\mu\nabla(\nabla\cdot\boldsymbol u)$ 一类项，粘性系数还可能依赖散度。

**老师（拓展）**：那面力那一次变换里，散度定理做了什么？

**学生**：它把面力 $\oint_{\partial V}\boldsymbol\sigma\cdot\boldsymbol n\,dS$ 化为 $\int_V\nabla\cdot\boldsymbol\sigma\,dV$，于是积分守恒律各项都写成同一区域上的体积分，才能被局域化成逐点方程。这也解释了 N-S 两层结构：上层守恒律普适，下层本构依材料而变；缺了后续的光滑性，弱解唯一性正是千禧年问题。
