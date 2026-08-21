# Kelvin涡量定理

> **一句话大白话**：在无粘、正压、仅受保守力作用的流体里，任何一条随流体运动而移动的闭合环路上的环量，永远不随时间改变。
>
> **小例子**：一盆水被搅出旋涡后（无粘近似下），那个旋涡的整体“转动强度”会一直保持，就像角动量守恒一样牢固。

## 一、定理介绍

> **前置依赖**：欧拉方程、物质导数与对流通量、斯托克斯定理、正压性条件、保守力场（势函数）、向量微积分（环路积分）。

Kelvin 涡量定理（Kelvin's circulation theorem）断言：无粘、正压且体积力有势的流体中，沿封闭物质线的环量 $\Gamma=\oint_C\boldsymbol u\cdot d\boldsymbol l$ 满足 $D\Gamma/Dt=0$。它是涡管、涡线守恒性与许多涡动力学结论的出发点。

## 二、原理思路

交换环量物质导数中的微分与积分次序，把 $D\boldsymbol u/Dt$ 用 Euler 方程替换。第二项因 $\oint\boldsymbol u\cdot d\boldsymbol u=\oint d\big(\frac12|\boldsymbol u|^2\big)=0$ 而消失；正压性把 $\frac1\rho\nabla p$ 写成势函数梯度，闭合积分又为零。

## 三、定理的严格表述

对无粘、正压（$\rho=\rho(p)$）且体积力有势的流体，沿任一闭合物质线环量守恒
$$
\frac{D\Gamma}{Dt}=0,\qquad \Gamma=\oint_C\boldsymbol u\cdot d\boldsymbol l.
$$

## 四、证明过程

1. **交换次序**。
   $$
   \frac{D\Gamma}{Dt}=\oint_{C}\frac{D\boldsymbol u}{Dt}\cdot d\boldsymbol l+\oint_{C}\boldsymbol u\cdot\frac{D(d\boldsymbol l)}{Dt}.
   $$
2. **第二项为零**。因 $\frac{D(d\boldsymbol l)}{Dt}=d\boldsymbol u$，故
   $$
   \oint\boldsymbol u\cdot d\boldsymbol u=\oint d\Big(\frac12|\boldsymbol u|^2\Big)=0.
   $$
3. **Euler 方程**。$\frac{D\boldsymbol u}{Dt}=-\frac1\rho\nabla p+\boldsymbol g$。
4. **正压 + 有势**。$\frac1\rho\nabla p=\nabla P$，$\boldsymbol g=-\nabla G$，则 $\oint(-\nabla P-\nabla G)\cdot d\boldsymbol l=0$，故 $D\Gamma/Dt=0$。

## 五、应用与意义

Kelvin 定理是涡动力学的基础：它导出涡线守恒、Helmholtz 涡定理的推论（无粘流体“涡旋不会凭空产生”），并用于海气环流、台风与翼尖涡的理解。它为不可压缩理想流中的大尺度涡结构提供了守恒约束。