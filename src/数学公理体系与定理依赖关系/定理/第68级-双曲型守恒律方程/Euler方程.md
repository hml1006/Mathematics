# Euler方程

> **一句话大白话**：Euler方程把"质量不变、动量变化等于受力、能量守恒"这三大守恒律写成一组偏微分方程，用来描述无粘可压缩流体（比如空气）如何流动、何时会产生激波。
>
> **小例子**：在一根充满空气的管子里敲出扰动，管道中会生成激波；Euler方程描述的就是这股波传播时密度、速度、压力发生跳变的过程。

## 一、定理介绍

Euler 方程描述无黏性可压缩流体的运动，是双曲守恒律方程最重要的实例之一。一维可压缩 Euler 方程组可写为

$$
\begin{cases}
\rho_t + (\rho v)_x = 0,\\
(\rho v)_t + (\rho v^2 + p)_x = 0,\\
(\rho E)_t + \bigl((\rho E + p)v\bigr)_x = 0,
\end{cases}
$$

其中 $\rho$ 为密度，$v$ 为速度，$p$ 为压强，$E=e+\frac{v^2}{2}$ 为单位质量总能量，$e$ 为内能。Euler 方程的数学理论涵盖严格双曲性、Riemann 问题、激波与接触间断、熵条件以及弱解的存在性等，是连接偏微分方程与流体力学的核心课题。

## 二、原理思路

将 Euler 方程写成守恒律形式

$$
\nu_t + f(\nu)_x = 0,
\qquad \nu=(\rho,\rho v,\rho E)^\top,
$$

对状态方程 $p=p(\rho,e)$（满足热力学稳定性条件）进行线性化，可得其 Jacobi 矩阵 $Df(\nu)$ 的特征值为

$$
\lambda_1=v-c,\qquad \lambda_2=v,\qquad \lambda_3=v+c,
$$

其中 $c=\sqrt{\partial p/\partial\rho|_s}$ 为声速。因此系统在物理可容许状态区域内是严格双曲的。第一、第三特征场通常为真非线性，对应激波与稀疏波；第二特征场线性退化，对应接触间断。对严格凸的状态方程，可建立完整的 Riemann 解理论；对一般 Cauchy 问题，小初值下可通过 Glimm 格式或 front tracking 得到 BV 弱解。

## 三、定理的严格表述

### 3.1 一维 Euler 方程的严格双曲性

设状态方程 $p=p(\rho,e)$ 满足

$$
p>0,\qquad \frac{\partial p}{\partial e}>0,\qquad
\frac{\partial^2 p}{\partial \rho^2}\bigg|_s > 0
$$

对 $\rho>0$、$e>0$ 成立。则一维 Euler 方程在状态空间

$$
\Omega=\bigl\{(\rho,\rho v,\rho E):\ \rho>0,\ e>0\bigr\}
$$

内是严格双曲的，特征值为

$$
\lambda_1=v-c,\quad \lambda_2=v,\quad \lambda_3=v+c,
$$

其中

$$
c=\sqrt{\frac{\partial p(\rho,s)}{\partial \rho}}
$$

为局部声速。第二特征场线性退化，第一、第三特征场真非线性。

### 3.2 Riemann 解结构

给定左状态 $\nu_L=(\rho_L,v_L,p_L)$ 与右状态 $\nu_+=(\rho_+,v_+,p_+)$，且两者充分接近，则一维 Euler 方程的 Riemann 问题存在唯一 Lax 可容许的自相似解。该解由中间状态 $\nu_M^-,\nu_M^+$ 连接而成，结构为

$$
\nu_L\xrightarrow{1\text{-波}}\nu_M^-\xrightarrow{2\text{-接触间断}}\nu_M^+\xrightarrow{3\text{-波}}\nu_+,
$$

其中 1-波与 3-波各为激波或稀疏波，2-波为接触间断（速度与压强连续，密度可跳跃）。

### 3.3 局部适定性与奇性形成

对光滑初值 $(\rho_0,v_0,s_0)\in H^s(\mathbb{R})$，$s>3/2$，且 $\rho_0>0$，存在唯一局部光滑解。对一般非线性波，即使初值光滑，也会在有限时刻产生梯度爆破（激波形成），因此必须研究弱解理论。

## 四、证明过程

### 4.1 特征值的计算

将 Euler 方程写成拟线性形式。利用热力学关系 $de=T\,ds - p\,d(1/\rho)$，可选取变量 $(\rho,v,s)$。此时方程组为

$$
\begin{cases}
\rho_t + v\rho_x + \rho v_x = 0,\\
v_t + v v_x + \frac{1}{\rho}p_x = 0,\\
s_t + v s_x = 0.
\end{cases}
$$

其系数矩阵的特征方程为

$$
(v-\lambda)\bigl[(v-\lambda)^2 - c^2\bigr]=0,
$$

从而得到 $\lambda=v-c,v,v+c$。右特征向量分别为 $(-\rho/c,1,0)^\top$、$(p_s,0,-\rho)^\top$、$(\rho/c,1,0)^\top$，故三个特征值互异，系统严格双曲。

### 4.2 真非线性与线性退化

沿第一、第三特征场，有

$$
\nabla\lambda_1\cdot r_1 = -\frac{1}{2c}\frac{\partial(\rho c)}{\partial\rho}\bigg|_s \neq 0,
$$

同理 $\nabla\lambda_3\cdot r_3\neq 0$。沿第二特征场，$\lambda_2=v$，而 $r_2$ 的方向对应 $(\rho,v,s)$ 空间中 $v$ 不变、$s$ 变化的方向，因此

$$
\nabla\lambda_2\cdot r_2 = 0,
$$

即第二场线性退化，只产生接触间断。

### 4.3 Riemann 解的构造

对左右状态，分别画出通过左状态的第一族 Hugoniot/积分曲线与通过右状态的第三族 Hugoniot/积分曲线。中间状态由接触间断条件 $v_M^-=v_M^+$、$p_M^-=p_M^+$ 确定。由于系统在严格双曲且小扰动下满足隐函数定理条件，该交点唯一存在，从而 Riemann 解唯一。

### 4.4 弱解存在性

对总变差足够小的 BV 初值，可将 Glimm 格式或 front tracking 方法应用于 Euler 方程。由于每个特征场均满足真非线性或线性退化条件，Glimm 格式的波相互作用估计成立，得到一致 BV 界的近似解。取极限后得到满足 Rankine–Hugoniot 与 Lax 熵条件的弱解。

## 五、应用与意义

Euler 方程不仅是空气动力学、航空航天、内燃机燃烧等领域的核心模型，也是双曲守恒律数学理论的试金石。对 Euler 方程 Riemann 问题的完整理解直接催生了 Godunov 格式、Roe 格式、HLL 格式等现代计算流体力学方法。其数学理论中的严格双曲性、激波可容许性、熵解存在唯一性等成果，深刻影响了非线性偏微分方程、连续介质力学和数值分析的发展方向。研究 Euler 方程的弱解与奇性结构，至今仍是数学物理中的前沿课题。
