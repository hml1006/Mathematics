# Laplace-Beltrami 算子与热方程

> **一句话大白话**：把"曲面上怎么求导、怎么扩散"统一成一个算子 $\Delta$，并证明"温度按 $\partial_t u=\Delta u$ 演化"的方程在紧流形上总有唯一解：能量单调减少，最大值不会凭空产生。

> **小例子**：在紧致无边的曲面 $M$ 上给定初始温度 $u_0$，解可写成特征函数展开 $u(x,t)=\sum_k e^{-\lambda_k t}\langle u_0,\varphi_k\rangle\varphi_k$；高频模式以 $e^{-\lambda_k t}$ 衰减，故 $u$ 最终趋于常数平均值。

## 一、定理介绍

> **前置依赖**：Riemann度量、测地线方程、Bochner公式、极大值原理、热方程的基本解。

Laplace–Beltrami 算子是 Laplace 算子 $\Delta=\sum_i\partial_i^2$ 在一般黎曼流形上的推广，由 Beltrami 于 1868 年研究曲面上的位势理论时以"散度形式"引入。它的定义要与度量相容：保持"二阶、无零阶项"的分析结构，同时在坐标变换下不变。

热方程

$$
\partial_t u=\Delta u
$$

是几何分析中最基本的发展方程。相比欧氏空间，流形上的热方程多出两层几何内容：其一，$\Delta$ 的系数由度量决定（局部坐标中体积元 $\sqrt{\lvert g\rvert}$ 进入系数）；其二，$\Delta$ 通过 Bochner 恒等式与 Ricci 曲率联系，使"曲率有下界"能转化为梯度估计。这正是 Hodge 理论、Ricci 流、平均曲率流、谱几何与热核方法的共同出发点。

本条目给出三件事：$\Delta$ 的散度形式与自伴性、热方程的存在唯一性、以及 Bochner 恒等式导出的梯度估计，它们是"热核与共轭热方程""热核与反向热方程"及各单调公式的技术前提。

## 二、原理思路

1. **几何不变的定义**：局部坐标中 $\Delta f=\mathrm{div}(\nabla f)=\frac{1}{\sqrt{\lvert g\rvert}}\partial_i\big(\sqrt{\lvert g\rvert}\,g^{ij}\partial_jf\big)$，散度定义含体积元 $\sqrt{\lvert g\rvert}$，故不依赖坐标系。
2. **自伴性来自散度定理**：取 $X=h\nabla f$ 并积分，立即得 $\int_Mh\Delta f\,d\mu=-\int_M\langle\nabla h,\nabla f\rangle\,d\mu$，于是 $\Delta$ 自伴且 $-\Delta\ge0$。
3. **谱分解给出解**：椭圆正则性保证 $-\Delta$ 预解紧，谱离散；把初值按特征函数展开即得 $e^{t\Delta}$，既给出存在性又给出 $t>0$ 的光滑化。
4. **能量与极值原理给出唯一性**：$\frac{d}{dt}\int_Mu^2=-2\int_M\lvert\nabla u\rvert^2\le0$，且 $\sup_Mu(\cdot,t)$ 不增，二者同时给出唯一性与稳定性。
5. **曲率进入估计**：Bochner 恒等式把 $\Delta\lvert\nabla u\rvert^2$ 拆成 Hessian 平方、$\langle\nabla u,\nabla\Delta u\rangle$ 与 Ricci 项，代入热方程后用极值原理即得梯度估计。

## 三、定理的严格表述

设 $(M^n,g)$ 紧致无边，$d\mu$ 为体积元，$\Delta=\mathrm{div}\circ\nabla$，约定 $\Delta=\sum_i\nabla_i\nabla_i$（符号使常数取零、$\Delta\le0$）。

**定理 1（散度形式与自伴性）.** 局部坐标中 $\Delta f=\frac{1}{\sqrt{\lvert g\rvert}}\partial_i\big(\sqrt{\lvert g\rvert}\,g^{ij}\partial_jf\big)$，且

$$
\int_Mh\,\Delta f\,d\mu=-\int_M\langle\nabla h,\nabla f\rangle\,d\mu=\int_Mf\,\Delta h\,d\mu .
$$

**定理 2（存在唯一性与单调性）.** 对任意 $u_0\in L^2(M,d\mu)$，$\partial_tu=\Delta u,\ u(\cdot,0)=u_0$ 有唯一解 $u\in C^\infty(M\times(0,\infty))$，且

$$
\frac{d}{dt}\int_Mu^2\,d\mu=-2\int_M\lvert\nabla u\rvert^2d\mu\le0 .
$$

当 $u_0\in C^\infty(M)$ 时解光滑到 $t=0$，并满足极值原理 $\sup_Mu(\cdot,t)\le\sup_Mu_0$、$\inf_Mu(\cdot,t)\ge\inf_Mu_0$。

**定理 3（Bochner 恒等式与梯度估计）.** 对 $u\in C^\infty(M)$，

$$
\frac12\Delta\lvert\nabla u\rvert^2=\lvert\mathrm{Hess}\,u\rvert^2+\langle\nabla u,\nabla\Delta u\rangle+\mathrm{Ric}(\nabla u,\nabla u).
$$

若 $\mathrm{Ric}\ge-(n-1)K$（$K\ge0$）且 $u$ 解热方程，则 $\lvert\nabla u\rvert^2(\cdot,t)\le e^{2(n-1)Kt}\sup_M\lvert\nabla u_0\rvert^2$。

## 四、证明过程

**步骤 1（散度形式与自伴性）。** 函数的梯度按度量逆给出 $(\nabla f)^i=g^{ij}\partial_jf$；向量场散度定义为 $\mathrm{div}X=\frac{1}{\sqrt{\lvert g\rvert}}\partial_i(\sqrt{\lvert g\rvert}X^i)$（保证 $\mathcal L_Xd\mu=(\mathrm{div}X)d\mu$）。代入 $X=\nabla f$ 得

$$
\Delta f=\mathrm{div}(\nabla f)=\frac{1}{\sqrt{\lvert g\rvert}}\partial_i\Big(\sqrt{\lvert g\rvert}\,g^{ij}\partial_jf\Big).
$$

取 $X=h\nabla f$，由散度定理 $\int_M\mathrm{div}X\,d\mu=0$，并用 $\mathrm{div}(h\nabla f)=h\Delta f+\langle\nabla h,\nabla f\rangle$，积分得定理 1 中的配对等式；右端关于 $f,h$ 对称，故 $\Delta$ 自伴。取 $h=f$ 得 $\int_Mf\Delta f\,d\mu=-\int_M\lvert\nabla f\rvert^2d\mu\le0$。

**步骤 2（谱分解给出存在性）。** $-\Delta$ 非负自伴且预解紧，故谱离散：$0=\lambda_0<\lambda_1\le\lambda_2\le\cdots\to\infty$（$\lambda_0=0$ 对应常函数，因 $\int\lvert\nabla f\rvert^2=0$ 推出 $\nabla f=0$）。取正交归一特征函数系 $\{\varphi_k\}$ 并令

$$
u(x,t)=\sum_{k\ge0}e^{-\lambda_kt}\langle u_0,\varphi_k\rangle_{L^2}\,\varphi_k(x).
$$

由 $e^{-\lambda_kt}\le e^{-\lambda_1t}$（$k\ge1$）与 Weyl 律 $\lambda_k\asymp k^{2/n}$，该级数在 $M\times[\delta,\infty)$（$\delta>0$）上连同各阶导数一致收敛；又 $\Delta\varphi_k=-\lambda_k\varphi_k$，逐项求导得 $\partial_tu=\Delta u$，故 $u$ 是光滑解。$t>0$ 时任意 $L^2$ 初值立即变光滑，这是热方程的正则化效应。

**步骤 3（能量与极值原理，唯一性）。** 设 $u$ 光滑解，由自伴性

$$
\frac{d}{dt}\int_Mu^2\,d\mu=2\int_Mu\,\partial_tu\,d\mu=2\int_Mu\Delta u\,d\mu=-2\int_M\lvert\nabla u\rvert^2d\mu\le0 .
$$

故 $\int_Mu^2$ 单调不增。若初值为 $0$，则 $\int_Mu^2\equiv0$，故 $u\equiv0$，结合步骤 2 得唯一性。极值原理：若 $u$ 在首次数值 $t_0$ 与内点 $p$ 处创新高，则该点 $\nabla u=0$、$\Delta u\le0$、$\partial_tu\ge0$，与 $\partial_tu=\Delta u$ 矛盾；故 $\sup_Mu(\cdot,t)$ 不增，同理 $\inf_Mu(\cdot,t)$ 不减，并得 $\lVert u(\cdot,t)\rVert_\infty\le\lVert u_0\rVert_\infty$。

**步骤 4（Bochner 恒等式与梯度估计）。** 取标准正交标架使 $\nabla_ie_j=0$，记 $\nabla_i=\nabla_{e_i}$，则

$$
\frac12\Delta\lvert\nabla u\rvert^2=\sum_{i,j}(\nabla_i\nabla_ju)^2+\sum_{i,j}\nabla_ju\,\nabla_i\nabla_i\nabla_ju ,
$$

第一项为 $\lvert\mathrm{Hess}\,u\rvert^2$；对第二项用 Ricci 恒等式调换 $i,j$ 次序，$\sum_i\nabla_i\nabla_i\nabla_ju=\nabla_j\Delta u-\mathrm{Ric}_j{}^l\nabla_lu$，对 $j$ 求和化成 $\langle\nabla u,\nabla\Delta u\rangle-\mathrm{Ric}(\nabla u,\nabla u)$，即得定理 3 的恒等式。若 $u$ 解热方程，则 $\nabla\Delta u=\partial_t\nabla u$，于是

$$
(\partial_t-\Delta)\lvert\nabla u\rvert^2=-2\lvert\mathrm{Hess}\,u\rvert^2-2\mathrm{Ric}(\nabla u,\nabla u)\le2(n-1)K\lvert\nabla u\rvert^2 .
$$

对 $v=e^{-2(n-1)Kt}\lvert\nabla u\rvert^2$ 用极值原理（$(\partial_t-\Delta)v\le0$）即得 $\lvert\nabla u\rvert^2(\cdot,t)\le e^{2(n-1)Kt}\sup_M\lvert\nabla u_0\rvert^2$。$\square$

## 五、应用与意义

- **Hodge 理论与消没定理**：自伴性与谱分解是 Hodge 分解定理的分析基础，配合 Bochner 恒等式得消没定理（$\mathrm{Ric}>0$ 时 $b_1=0$）。
- **谱几何**：特征值即几何量，Weyl 渐近律、Lichnerowicz 估计与热核迹的短时渐近（Minakshisundaram–Pleijel 展开）由此展开。
- **几何流**：Ricci 流与平均曲率流中的单调量（Huisken 单调公式、Perelman 熵）都建立在这一热算子框架与共轭热方程之上。
- **抛物极值原理**：$\sup u$ 不增是张量极值原理的标量原型，也是曲率估计中"由内点极值导出矛盾"的标准手段。

## 相关条目

- [coarea公式](./coarea公式.md)：与散度定理配合，把流形上的积分沿水平集分解。
- [第一变分公式](./第一变分公式.md)：面积元的一阶变分用到 $\mathrm{div}_M$，与本文散度计算同源。
- [Huisken单调公式](./Huisken单调公式.md)：以反向热核为权重，直接建立在本文的热方程框架上。
- [Hamilton张量极值原理](./Hamilton张量极值原理.md)：抛物极值原理在张量方程上的推广。
- [Bochner公式](../第49级-黎曼几何/Bochner公式.md)：定理 3 的详细推导与推广。
- [热方程的基本解](../第40级-偏微分方程/热方程的基本解.md)：欧氏热核的显式计算。
