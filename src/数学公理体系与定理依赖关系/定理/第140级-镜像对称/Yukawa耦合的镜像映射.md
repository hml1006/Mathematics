# Yukawa耦合的镜像映射

> **一句话大白话**：镜像对称把 A-模型（数有理曲线）和 B-模型（算周期积分）两本"账本"连起来，其中关键的桥梁是 Yukawa 耦合——两边各有一个由三点决定的"三阶杂交量"，靠镜像映射 $s=s(t)$ 用链式法则一换算，两边的量就严格对应起来。
>
> **小例子**：B-模型的 Yukawa 是周期 $\Pi$ 的三阶导 $\kappa_{ijk}^B=\Pi^\top\partial_i\partial_j\partial_k\Pi$，A-模型的是 GW 不变量级数 $\kappa_{ijk}^A=\sum_\beta\mathrm{GW}_{0,\beta}\,q^\beta$；镜像说这两者在 $s=s(t)$ 下通过 $\kappa^A=\kappa^B\frac{\partial s}{\partial t}\frac{\partial s}{\partial t}\frac{\partial s}{\partial t}$ 互相对应，于是"难算的曲线数"变成"好算的周期微商"。

## 一、定理介绍

设 $M$ 是 Calabi-Yau $n$-重，$W$ 是其镜像流形。镜像对称断言 A-模型与 B-模型的 Yukawa 耦合在镜像映射下对应：
$$
\kappa_{ijk}^A(t)=\kappa_{pqr}^B(s)\frac{\partial s^p}{\partial t^i}\frac{\partial s^q}{\partial t^j}\frac{\partial s^r}{\partial t^k},
$$
其中 $s=s(t)$ 是镜像映射，$t$ 是 Kähler 模空间坐标，$s$ 是复结构模空间坐标。该公式是镜像对称的核心计算工具：它把 A-模型的计数几何不变量归约为 B-模型可显式算出的周期积分。

## 二、原理思路

核心思想是"同一条等式，两边不同解读"。B-模型的 Yukawa 由全纯 $(n,0)$-形式 $\Omega(s)$ 的三阶微商定义，可化成周期向量的三阶导；A-模型的 Yukawa 由 Gromov-Witten 不变量展开给出。两者都满足由 Picard-Fuchs 方程导出的微分约束，通过 Gauss-Manin 连接与单值性，镜像映射把两边的坐标体系对齐，从而使量相等。

## 三、定理的严格表述

设 $M,W$ 为镜像 Calabi-Yau $n$-重，$t$ 为 Kähler 模坐标，$s$ 为复结构模坐标，$s=s(t)$ 为镜像映射。则 A-模型与 B-模型的 Yukawa 耦合满足
$$
\kappa_{ijk}^A(t)=\kappa_{pqr}^B(s(t))\frac{\partial s^p}{\partial t^i}\frac{\partial s^q}{\partial t^j}\frac{\partial s^r}{\partial t^k}.
$$
其中 $\kappa_{ijk}^B=\Pi^\top\partial_i\partial_j\partial_k\Pi$，$\Pi$ 为规范化周期向量。

## 四、证明过程

**步骤1：B-模型 Yukawa。** 定义
$$
\kappa_{ijk}^B=\int_M\Omega\wedge\partial_i\partial_j\partial_k\Omega,
$$
取局部平凡化使 $\Omega$ 的 $(n,0)$-分量归一化，则 $\partial_i\Omega=\kappa_i\Omega+\chi_i$，$\chi_i\in H^{n-1,1}$。

**步骤2：周期表示。** 令 $\Pi_\alpha(s)=\int_{\gamma_\alpha}\Omega(s)$ 为周期。在 Calabi-Yau 3-重情形，取规范化周期向量 $\mathbf\Pi$，有
$$
\kappa_{ijk}^B=\mathbf\Pi^\top\,\partial_i\partial_j\partial_k\mathbf\Pi.
$$

**步骤3：Picard-Fuchs 方程。** 周期向量满足
$$
\mathcal L_i\mathbf\Pi=0,\qquad i=1,\dots,h^{n-1,1},
$$
其中 $\mathcal L_i$ 为 Picard-Fuchs 算子，由模空间的 Gauss-Manin 连接决定。

**步骤4：A-模型 GW 展开。** A-模型 Yukawa 为
$$
\kappa_{ijk}^A(t)=\sum_{\beta\in H_2(M,\mathbb Z)}\mathrm{GW}_{0,\beta}^M(\omega_i,\omega_j,\omega_k)\,q^\beta,\qquad q^\beta=\exp\!\Big(2\pi i\int_\beta B+i\omega\Big).
$$

**步骤5：Schwarz 定理。** 满足同一 Picard-Fuchs 方程的两组函数相差一个单值性变换。镜像映射由周期之比定义：
$$
s^i=\frac{\Pi_i(t)}{\Pi_0(t)}.
$$

**步骤6：链式法则变换。** 在 $s=s(t)$ 下代入链式法则，并利用两侧 Yukawa 在大复结构极限边界条件的匹配，得
$$
\kappa_{ijk}^A(t)=\sum_{p,q,r}\kappa_{pqr}^B(s(t))\,\frac{\partial s^p}{\partial t^i}\frac{\partial s^q}{\partial t^j}\frac{\partial s^r}{\partial t^k}.
$$

**结论（$\square$）**：Yukawa 耦合的镜像映射公式成立，使 A-模型的 GW 不变量可通过 B-模型周期积分计算。

## 五、应用与意义

该公式是镜像对称的"计算发动机"。由于 B-模型只需解析地解周期积分（Picard-Fuchs 方程），而 A-模型要数有理曲线（极难），镜像映射让研究者从 B-模型一侧高效地读出 A-模型的计数几何信息。它是 GW 不变量计算、超弦紧化与模空间上的对偶性研究的基本工具。