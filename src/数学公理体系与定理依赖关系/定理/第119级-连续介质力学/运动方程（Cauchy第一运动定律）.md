# 运动方程（Cauchy第一运动定律）

> **一句话大白话**：物体某个小块的“加速度×质量”等于它受到的“体积力 + 应力在表面上的合力”，写成微分形式就是动量守恒方程。
>
> **小例子**：地震波传过岩石时，每一点的振动由压力、剪切应力和重力的合力推动，其数学形式正是 Cauchy 第一运动定律。

## 一、定理介绍

Cauchy 第一运动定律把动量守恒化为局部微分方程
$$
\nabla\cdot\boldsymbol\sigma+\rho\boldsymbol b=\rho\dot{\boldsymbol v},
$$
其中 $\boldsymbol\sigma$ 为 Cauchy 应力张量，$\boldsymbol b$ 为体力密度，$\dot{\boldsymbol v}$ 为物质加速度。它是连续介质（固体与流体）运动方程的统一来源。

## 二、原理思路

从积分形式的动量守恒出发，用 Reynolds 输运定理处理物质导数的体积分，用散度定理把面力面积分（$\boldsymbol\sigma\cdot\boldsymbol n$）化为体积分，再利用“任意控制体上积分为零则被积函数为零”。

## 三、定理的严格表述

对连续介质体，动量守恒等价于
$$
\nabla\cdot\boldsymbol\sigma+\rho\boldsymbol b=\rho\dot{\boldsymbol v},
$$
其中 $\dot{\boldsymbol v}=\frac{D\boldsymbol v}{Dt}$ 为物质加速度。分量形式为
$$
\frac{\partial\sigma_{ij}}{\partial x_j}+\rho b_i=\rho\frac{Dv_i}{Dt}.
$$

## 四、证明过程

1. **积分动量守恒**。动量物质导数等于外力之和
   $$
   \frac{D}{Dt}\int_{\Omega}\rho\boldsymbol v\,dV=\int_{\Omega}\rho\boldsymbol b\,dV+\int_{\partial\Omega}\boldsymbol\sigma\cdot\boldsymbol n\,dS.
   $$
2. **Reynolds 输运**。$\frac{D}{Dt}\int\rho\boldsymbol\phi\,dV=\int\rho\frac{D\boldsymbol\phi}{Dt}\,dV$。
3. **面积分化体积分**。散度定理 $\int_{\partial\Omega}\boldsymbol\sigma\cdot\boldsymbol n\,dS=\int_\Omega\nabla\cdot\boldsymbol\sigma\,dV$。
4. **合并与局域化**。代入得 $\int_\Omega(\nabla\cdot\boldsymbol\sigma+\rho\boldsymbol b-\rho\dot{\boldsymbol v})dV=\boldsymbol 0$，由任意性得被积函数为零。

## 五、应用与意义

Cauchy 第一运动定律派生弹性波方程、Navier-Stokes 方程与结构动力学方程，是固体力学、流体力学与数值模拟的公共起点。它与 Cauchy 定理、Reynolds 定理共同构成连续介质运动学的守恒框架。