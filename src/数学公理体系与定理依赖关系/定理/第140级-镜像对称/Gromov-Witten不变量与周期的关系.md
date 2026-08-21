# Gromov-Witten不变量与周期的关系

> **一句话大白话**：数清"$M$ 上有多少条指定次数的有理曲线"极难，但镜像对称给了条捷径——把这些数藏进镜像 $W$ 上的周期积分（满足 Picard-Fuchs 方程），对镜子那边求三次导就能把曲线数"称"出来。
>
> **小例子**：五次流形 $M=\{X_0^5+\cdots+X_4^5-5\psi X_0\cdots X_4=0\}$ 上 $d$ 次曲线数记 $N_d$；镜像公式 $\sum_\beta\mathrm{GW}_{0,\beta}\,q^\beta=\frac{d^3}{dt^3}\Pi(t)$ 给出 $N_1=2875$、$N_2=609250$、$N_3=317206375$…——都是真实的那几次著名曲线数。

## 一、定理介绍

> **前置依赖**：Gromov-Witten理论、Picard-Fuchs方程、周期积分、Yukawa耦合、Calabi-Yau流形上的模空间

Gromov-Witten 不变量与周期的关系是镜像对称的可计算核心：$M$ 的（A-模型）Gromov-Witten 不变量可从镜像 $W$ 的（B-模型）周期积分中读出。令 $\Pi(t)$ 为周期、$q=e^{2\pi i t}$，则构造性公式
$$
\sum_{\beta\in H_2(M)}\mathrm{GW}_{0,\beta}^M\,q^\beta=\frac{d^3}{dt^3}\Pi(t)
$$
连接了闭形式乘法与周期微商，常被用来计算超曲面上有理曲线计数。

## 二、原理思路

以五次超曲面为例。五次 $M\subset\mathbb P^4$ 是 Calabi-Yau 3-重（$h^{1,1}=1$，$h^{2,1}=101$），其镜像 $W$ 由轨道折叠（orbifolding）$W=M/(\mathbb Z_5)^3$ 得（$h^{1,1}=101$，$h^{2,1}=1$）。周期 $\Pi(\psi)=\int_\gamma\Omega(\psi)$ 满足 Picard-Fuchs 方程，其幂级数保证供镜像映射 $t=\Pi_1/\Pi_0$；B-模型 Yukawa $\kappa_{ttt}=\frac{d^3}{dt^3}\Pi$，A-模型 Yukawa $\kappa_{ttt}^A=\sum_dN_d\frac{d^3q^d}{1-q^d}$，镜像令相等解出 $N_d$。

## 三、定理的严格表述

设 $M,W$ 为镜像 Calabi-Yau 3-重，$\Pi$ 为 W 上周期（含镜像映射 $t=\frac1{2\pi i}\log\psi^5+\text{正则}$，$q=e^{2\pi it}$）。则
$$
\kappa_{ttt}^A=\sum_{\beta}\mathrm{GW}_{0,\beta}^M q^\beta=\frac{d^3}{\,dt^3}\Pi(t)=\kappa_{ttt}^B,
$$
由该等式可逐一解出有理 GW 不变量 $N_d$（如 $N_1=2875$，$N_2=609250$）。

## 四、证明过程

**步骤1：五次超曲面。** 设 $M=\{X_0^5+\cdots+X_4^5-5\psi X_0X_1X_2X_3X_4=0\}\subset\mathbb P^4$，为 3-Calabi-Yau，$h^{1,1}=1$、$h^{2,1}=101$。

**步骤2：构造镜像。** $W=M/(\mathbb Z_5)^3$ 轨道折叠，满足 $h^{1,1}=101$、$h^{2,1}=1$，与翻转公式一致。

**步骤3：周期与 Picard-Fuchs。** $\Pi(\psi)=\int_\gamma\Omega(\psi)$，$\gamma\in H_3(M,\mathbb Z)$，满足
$$
\Big[\theta^4-5\psi\prod_{i=1}^4(5\theta+i)\Big]\Pi=0,\qquad \theta=\psi\frac d{d\psi}.
$$

**步骤4：求解周期。** $\psi=0$ 附近幂级数解 $\Pi_0(\psi)=\sum_n\frac{(5n)!}{(n!)^5}\psi^{5n}$，$\Pi_1(\psi)=\frac1{2\pi i}\Pi_0\log\psi^5+\text{正则}$。

**步骤5：构造镜像映射。** $t=\Pi_1(\psi)/\Pi_0(\psi)=\frac1{2\pi i}\log\psi^5+\text{幂级数修正}$。

**步骤6：计算 Yukawa 与 GW。** B-模型 $\kappa_{ttt}=\frac{d^3}{dt^3}\Pi$；A-模型 $\kappa_{ttt}^A=\sum_{d\ge1}N_d\frac{d^3q^d}{1-q^d}$。镜像相等，比较系数解出
$$
N_1=2875,\quad N_2=609250,\quad N_3=317206375,\ \dots
$$
恰为五次超曲面 $d$ 次有理曲线的真实数目。

**结论（$\square$）**：GW 不变量可由周期积分（镜像侧）计算。

## 五、应用与意义

该关系是镜像对称最成功的应用之一：通过 B-模型的解析（Picard-Fuchs）计算 A-模型的计数几何不变量，直接解决了五次超曲面有理曲线的经典计数难题（2875 等惊人整数）。它确立了"周期-曲线数"对偶，是除价几何（enumeration）与镜像计算的范式工具。