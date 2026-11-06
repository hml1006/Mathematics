# 第156级-微局部分析与半经典分析

> 一句话级别概述：微局部分析把奇性拆成位置与方向两半：波前集告诉你奇性在哪里、朝哪个方向传播；半经典分析则把量子谱与经典轨道对接。

## 级别简介

本级别先建立拟微分算子的象征演算与波前集，给出奇性传播与 Hörmander 亚椭圆性；随后转入半经典侧：Weyl 定律、Egorov 定理、Gutzwiller 迹公式、半经典测度与量子极限，最后以复 WKB 与 Stokes 现象收尾。

## 本级别定理

- [拟微分算子的象征演算](./拟微分算子的象征演算.md)：拟微分算子复合的象征满足 $p\#q\sim\sum_{\alpha}\frac{(-i)^{|\alpha|}}{\alpha!}\partial_\xi^\alpha p\,\partial_x^\alpha q$。
- [波前集与奇性传播定理](./波前集与奇性传播定理.md)：$\mathrm{WF}(u)\subset T^*X\setminus0$ 刻画奇性的位置与方向；椭圆算子不改变 $\mathrm{WF}$，双曲算子沿 Hamilton 流传播奇性。
- [Hörmander 亚椭圆性定理](./Hörmander亚椭圆性定理.md)：若主象征 $p_m$ 满足亚椭圆条件（$p_m=0\Rightarrow \mathrm d p_m\ne0$ 且 $\mathrm{Im}p_m$ 的符号条件），则 $Pu\in C^\infty\Rightarrow u\in C^\infty$。
- [半经典 Weyl 定律](./半经典Weyl定律.md)：计数函数满足 $N(\lambda)\sim(2\pi)^{-n}\mathrm{vol}(\Omega)\lambda^{n/2}$，即特征值"均匀铺满"相空间。
- [Egorov 定理](./Egorov定理.md)：量子演化与经典流共轭：$\mathrm{Op}(a)\circ U(t)\approx U(t)\circ\mathrm{Op}(a\circ\phi_t)$，是量子遍历性的出发点。
- [Gutzwiller 迹公式](./Gutzwiller迹公式.md)：$\mathrm{tr}\,e^{-itH/\hbar}\sim\sum_{\gamma}\frac{T_\gamma}{i\hbar^{1/2}|\det(I-P_\gamma)|^{1/2}}e^{iS_\gamma/\hbar}$，谱由周期轨道求和给出。
- [半经典测度与量子极限](./半经典测度与量子极限.md)：半经典测度的聚点必为 Laplacian 不变的经典概率测度，量子极限与经典不变测度由此对应。
- [复 WKB 与 Stokes 现象](./复WKB与Stokes现象.md)：复相位下的渐近解在 Stokes 线两侧取不同线性组合，指数小的项在穿越时"突然出现"。

## 前置知识

Fourier 分析与分布理论、Sobolev 空间、Hamilton 力学与辛几何、谱理论。

## 后继用途

为偏微分方程的奇性分析、量子混沌、谱几何与散射理论提供核心工具。

## 关键定理速览

- 拟微分算子的复合按象征渐近展开。
- 波前集刻画奇性的位置与方向，椭圆算子不改变它。
- Egorov 定理：量子演化与经典流共轭。
- Gutzwiller 迹公式把谱写成周期轨道求和。
- 半经典测度的聚点是经典不变测度。
