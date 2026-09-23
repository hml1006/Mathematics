# Blasius定理

> **一句话大白话**：二维不可压缩势流中，物体受到的合力与力矩不必逐点积分压力，只要把复速度的平方沿物体边界绕一圈做复围道积分就行了。

> **小例子**：绕半径为 $R$ 的圆柱、来流速度 $U$、环量 $\Gamma$ 的势流中，远场 $\left(\frac{dw}{dz}\right)^{2}=U^{2}-\frac{iU\Gamma}{\pi z}+\cdots$。由 Blasius 定理只需取 $1/z$ 项，得 $F_x-iF_y=\frac{i\rho}{2}\cdot 2U\Gamma=i\rho U\Gamma$，即阻力为零、升力 $F_y=\rho U\Gamma$，与 Kutta-Joukowski 定理一致。

## 一、定理介绍

> **前置依赖**：复势与复速度、Bernoulli方程、围道积分与Cauchy积分定理、留数定理、Laurent展开、不可压缩势流理论。

Blasius 定理由德国流体力学家 Paul Richard Heinrich Blasius（1883–1970）在 1910 年发表于《Zeitschrift für Mathematik und Physik》的论文《Funktionentheoretische Methoden in der Hydrodynamik》（流体力学中的函数论方法）中提出。Blasius 是 Prandtl 在哥廷根的学生，同一时期他还在 1908 年的学位论文中给出了平板边界层的相似解（即著名的 Blasius 方程），但这里所述的"Blasius 定理"指的是势流中计算合力与力矩的复变函数方法，二者是不同结果，常在文献中因同名而混淆。

该定理的提出动机十分具体：在理想流体（无粘、不可压、无旋）的二维势流模型中，物体表面的压力分布可由 Bernoulli 方程求出，但要把压力沿复杂翼型边界积分得到总力，计算极其繁琐。Blasius 发现，利用复势 $w(z)$ 与复速度 $\frac{dw}{dz}$ 的结构，可以把"沿边界的压力积分"整体改写为"复速度平方的围道积分"，从而借助 Cauchy 积分定理与留数定理，把注意力收缩到远场 Laurent 展开的少数几项上。这一变换不仅大幅简化计算，更揭示了一个深刻的物理事实：绕物体的合力只由环量决定，与翼型的具体形状无关。这正是 Kutta-Joukowski 升力定理的解析根源，也解释了 d'Alembert 伴谬（理想势流中阻力为零）的双重含义：形状的细节只在更高阶项中体现，而它们对围道积分没有贡献。

## 二、原理思路

1. 用 Bernoulli 方程把边界上的压力表示为 $p=C-\frac{\rho}{2}|q|^{2}$，其中 $q=\frac{dw}{dz}$ 为复速度，于是"压力积分"变成"复速度模长平方的积分"。

2. 把微元力写成复数形式：$dF=-p\,n\,ds$，其中 $n$ 为指向流体的外法向。对沿物体边界逆时针（物体位于左侧）的定向，法向与切向满足 $n\,ds=-i\,dz$，于是 $dF=i p\,dz$。

3. 关键一步是消去复共轭：物体边界是流线（$\psi$ 为常数），故 $q\,dz=dw=d\phi$ 为实数，从而 $q\,dz=\bar q\,d\bar z$，即 $d\bar z=\frac{q}{\bar q}dz$，这把力公式中的 $d\bar z$ 换成 $dz$；展开压力后常数项的积分为 $\oint d\bar z=0$，只剩 $\frac{i\rho}{2}\oint q^{2}dz$。最后用 Cauchy 定理把围道变形到远场大圆，用 Laurent 展开与留数定理计算。

## 三、定理的严格表述

设二维不可压缩势流，复势 $w(z)=\phi+i\psi$，复速度 $q(z)=\frac{dw}{dz}=u-iv$，流体密度为 $\rho$，$C$ 为物体边界并按逆时针方向（物体位于行进方向左侧）定向。则合力与关于原点的力矩（逆时针为正）分别为

$$
F_x-iF_y=\frac{i\rho}{2}\oint_{C}\left(\frac{dw}{dz}\right)^{2}dz ,
$$

$$
M=\mathrm{Re}\left[\frac{\rho}{2}\oint_{C}z\left(\frac{dw}{dz}\right)^{2}dz\right] .
$$

若 $q$ 在物体外全纯且单值，则可把 $C$ 变形为包围物体的任意闭曲线，特别是远处大圆 $C_R$：

$$
F_x-iF_y=\frac{i\rho}{2}\oint_{C_R}\left(\frac{dw}{dz}\right)^{2}dz .
$$

## 四、证明过程

**步骤 1（Bernoulli 化压力）。** 二维定常不可压无旋流动中 Bernoulli 方程给出 $p+\frac{\rho}{2}|q|^{2}=C$（常数），故边界上

$$
p=C-\frac{\rho}{2}|q|^{2}=C-\frac{\rho}{2}\left|\frac{dw}{dz}\right|^{2}.
$$

**步骤 2（微元力的复数表示）。** 设边界按逆时针定向，单位切向的复数表示为 $\frac{dz}{ds}$，指向流体的外法向为切向顺时针旋转 $90^\circ$，即 $n\,ds=-i\,dz$（可直接用圆周 $\theta\mapsto Re^{i\theta}$ 验证：$\theta=0$ 处切向为 $i$，外法向为 $1=-i\cdot i$）。作用在弧元上的力为

$$
dF=-p\,n\,ds=-p(-i\,dz)=i\,p\,dz\ \Longrightarrow\ F_x+iF_y=i\oint_{C}p\,dz .
$$

取共轭（$p$ 为实值）得

$$
F_x-iF_y=-i\oint_{C}p\,d\bar z .
$$

**步骤 3（边界是流线）。** 物体表面是流线，故沿 $C$ 有 $\psi=\text{const}$，于是 $dw=d\phi$ 为实的全微分。由 $dw=q\,dz$ 知 $q\,dz$ 是实数，取共轭得 $q\,dz=\bar q\,d\bar z$，因此

$$
d\bar z=\frac{q}{\bar q}\,dz=\frac{q^{2}}{|q|^{2}}\,dz .
$$

**步骤 4（代入压力）。** 把步骤 1、3 代入步骤 2：

$$
F_x-iF_y=-i\oint_{C}\left(C-\frac{\rho}{2}|q|^{2}\right)\frac{q^{2}}{|q|^{2}}dz=-iC\oint_{C}\frac{q^{2}}{|q|^{2}}dz+\frac{i\rho}{2}\oint_{C}q^{2}dz .
$$

**步骤 5（常数项消失）。** 由步骤 3，$\frac{q^{2}}{|q|^{2}}dz=d\bar z$，而 $\bar z$ 是单值函数的全微分，沿闭曲线积分 $\oint_{C}d\bar z=0$。故第一项为零，得

$$
F_x-iF_y=\frac{i\rho}{2}\oint_{C}\left(\frac{dw}{dz}\right)^{2}dz .
$$

**步骤 6（力矩公式）。** 关于原点定义力矩 $M=\oint_{C}\left(x\,dF_y-y\,dF_x\right)$，用复数写法即 $M=\oint_{C}\mathrm{Im}\left[\bar z\,dF\right]$。由步骤 2，$dF=i p\,dz$，于是 $M=\oint_{C}\mathrm{Im}\left[i\,p\,\bar z\,dz\right]$。用 $\bar z\,dz=d|z|^{2}-z\,d\bar z$ 且 $\oint_{C}d|z|^{2}=0$，得 $\oint_{C}\bar z\,dz=-\oint_{C}z\,d\bar z$；再由步骤 3 的 $d\bar z=\frac{q^{2}}{|q|^{2}}dz$，

$$
M=-\mathrm{Im}\left[i\oint_{C}p\,z\,\frac{q^{2}}{|q|^{2}}dz\right]=-\mathrm{Im}\left[iC\oint_{C}z\,d\bar z-\frac{i\rho}{2}\oint_{C}z\,q^{2}dz\right].
$$

对逆时针定向的闭曲线 $C$，由 Green 公式 $\oint_{C}z\,d\bar z=\oint_{C}(x\,dx+y\,dy)+i\oint_{C}(y\,dx-x\,dy)=-2iA$，其中 $A$ 为物体截面积，故 $iC\oint_{C}z\,d\bar z=2CA$ 为实数、其虚部为零。于是只剩第二项：

$$
M=\mathrm{Im}\left[\frac{i\rho}{2}\oint_{C}z\,q^{2}dz\right]=\frac{\rho}{2}\,\mathrm{Re}\left[\oint_{C}z\left(\frac{dw}{dz}\right)^{2}dz\right],
$$

其中用到对任意复数 $\zeta$ 有 $\mathrm{Im}[i\zeta]=\mathrm{Re}[\zeta]$。

**步骤 7（围道变形与留数计算）。** 因 $q=\frac{dw}{dz}$ 在物体外全纯，$q^{2}$ 亦然，由 Cauchy 积分定理可把 $C$ 变形为远处大圆 $C_R$，围道积分值不变。设远场 $\frac{dw}{dz}=U+\frac{i\Gamma}{2\pi z}+O\left(\frac{1}{z^{2}}\right)$，则

$$
\left(\frac{dw}{dz}\right)^{2}=U^{2}+\frac{iU\Gamma}{\pi z}+O\left(\frac{1}{z^{2}}\right),
$$

其中 $\frac{1}{z}$ 项系数为 $\frac{iU\Gamma}{\pi}$。由留数定理 $\oint_{C_R}\frac{dz}{z}=2\pi i$，且 $O(1/z^{2})$ 项在无穷远处积分为零，故

$$
\oint_{C_R}\left(\frac{dw}{dz}\right)^{2}dz=2\pi i\cdot\frac{iU\Gamma}{\pi}=-2U\Gamma
\ \Longrightarrow\ F_x-iF_y=\frac{i\rho}{2}\cdot(-2U\Gamma)=-i\rho U\Gamma ,
$$

即 $F_x=0$、$F_y=\rho U\Gamma$：阻力为零（d'Alembert 伴谬），升力等于 $\rho U\Gamma$，与 Kutta-Joukowski 定理一致；且可见合力只依赖 $1/z$ 项的系数（即环量），与形状对应的更高阶项无关。$\square$

## 五、应用与意义

- 空气动力学：把翼型升力、力矩的计算归结为远场 Laurent 系数，是薄翼理论与机翼设计解析方法的基石。
- Kutta-Joukowski 升力定理与 d'Alembert 伴谬：公式取远场大圆并只保留 $1/z$ 项即得 $L=\rho U\Gamma$，并说明理想势流中阻力恒为零。
- 复分析方法的应用范例：把物理量（力、力矩）化为全纯函数的围道积分与留数，是理论物理中"解析方法求全局量"的经典范式。

## 相关条目

- [Kutta-Joukowski定理](./Kutta-Joukowski定理.md)：本定理取远场留数后的直接推论，给出升力 $L=\rho U\Gamma$。
- [伯努利定理的严格证明](./伯努利定理的严格证明.md)：本证明步骤 1 中把表面压力化为复速度模长平方的依据。
- [Stokes定理](./Stokes定理.md)：同属流体力学经典积分定理，给出环量与涡量的关系。
- [Kelvin涡量定理](./Kelvin涡量定理.md)：说明环量在理想流体中的守恒性，为远场 $1/z$ 项稳定存在提供依据。
- [留数定理](../第18级-复分析/留数定理.md)：步骤 7 计算围道积分的核心工具。
- [洛朗级数展开定理](../第18级-复分析/洛朗级数展开定理.md)：远场复速度展开的理论依据。
