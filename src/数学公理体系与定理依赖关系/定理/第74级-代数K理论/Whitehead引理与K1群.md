# Whitehead 引理与 K1 群

> **一句话大白话**：$K_1(R)$ 测度了"一般线性群在交换子意义下"的不可分解部分：$K_1(R)=GL(R)/[GL(R),GL(R)]$；对域 $F$ 而言它恰好是乘法群 $F^\times$（由行列式实现）。
>
> **小例子**：对 $\mathbb{R}$ 有 $K_1(\mathbb{R})\cong\mathbb{R}^\times$，对 $\mathbb{Z}$ 有 $K_1(\mathbb{Z})\cong\mathbb{Z}^\times\cong\{\pm1\}$；而任何行列式为 $1$ 的整数矩阵都可经初等行变换化为单位矩阵，这正反映了 $K_1(\mathbb{Z})\cong\mathbb{Z}/2\mathbb{Z}$ 的"小"。

## 一、定理介绍

$K_1$ 群是一般线性群的稳定化、取交换子所得的核算对象。Whitehead 引理断言初等矩阵群 $E(R)$ 恰好等于换位子子群 $[GL(R),GL(R)]$，据此 $K_1(R)=GL(R)/E(R)$ 良定义。结合行列式映射，得到 $K_1(F)\cong F^\times$ 这一核心结果。这是 K 理论谱系中紧接 $K_0$ 的基本不变量。

## 二、原理思路

Whitehead 引理的证明分两侧：先验证每个初等矩阵 $e_{ij}(r)$ 是换位子（利用 $[e_{ik}(r),e_{kj}(1)]=e_{ij}(r)$），得 $E(R)\subseteq[GL,GL]$；再由对任意 $A$ 有 $Ae_{ij}(r)A^{-1}\in E(R)$，推出 $E(R)\trianglelefteq GL(R)$ 且商群交换，故 $[GL,GL]\subseteq E(R)$。对域加以提炼：$SL(F)=E(F)$，故 $\ker\det=[GL,GL]$，$K_1(F)\cong F^\times$。

## 三、定理的严格表述

设 $R$ 为含幺环，$GL(R)=\varinjlim_n GL_n(R)$，$E(R)$ 由初等矩阵生成。定义 $K_1(R)=GL(R)/[GL(R),GL(R)]$。

**Whitehead 引理：** $E(R)=[GL(R),GL(R)]$，即初等矩阵子群等于换位子子群，从而 $K_1(R)=GL(R)/E(R)$。

**定理：** 若 $R=F$ 为域，则 $K_1(F)\cong F^\times$；更一般地，对任意交换环 $R$ 有自然行列式映射 $\det:K_1(R)\to R^\times$。

## 四、证明过程

**证明：**

**步骤 1：$E(R)\subseteq[GL,GL]$。** 对互异的 $i,j,k$：
$$
[e_{ik}(r),e_{kj}(1)]=e_{ij}(r).
$$
故每个初等矩阵是换位子，$E(R)\subseteq[GL(R),GL(R)]$。

**步骤 2：$[GL,GL]\subseteq E(R)$。** 对 $A\in GL(R)$ 与 $e_{ij}(r)$：
$$
Ae_{ij}(r)A^{-1}=e_{ij}\Bigl(\sum_{k,l}A_{ik}r(A^{-1})_{lj}\Bigr)\in E(R).
$$
故 $E(R)\trianglelefteq GL(R)$ 且 $GL(R)/E(R)$ 交换，于是 $[GL(R),GL(R)]\subseteq E(R)$。两式合并即 $E(R)=[GL(R),GL(R)]$。$\square$

**推论（$K_1(F)\cong F^\times$）：** 行列式 $\det:GL(F)\to F^\times$ 是满群同态，$\ker\det=SL(F)$。由于域上任何行列式为 $1$ 的矩阵可由初等行变换化为单位矩阵，$SL(F)=E(F)$；再由 Whitehead 引理 $E(F)=[GL,GL]$，故 $\ker\det=[GL,GL]$，于是：
$$
K_1(F)=GL(F)/[GL(F),GL(F)]\cong F^\times.
$$
$\square$

## 五、应用与意义

$K_1$ 群把"可逆矩阵的稳定同伦"编码为代数不变量，在代数 K 理论、代数几何与同伦论中广泛应用。对环的同态 $R\to S$ 诱导 $K_1(R)\to K_1(S)$（同伦不变性），且 $K_1$ 满足矩阵不变性与 Morita 不变性（$K_1(M_n(R))\cong K_1(R)$）。$K_1(\mathbb{Z})\cong\mathbb{Z}/2\mathbb{Z}$ 等计算连接数论（单位群、类群）；高次 K 群（$K_2,K_3,\dots$）在 $K_1$ 基础上发展，Whitehead 引理是理解这些不变量的重要支点。它还与 Whitehead 扭、带符号的动力系统及 Milnor-Wood 型理论相通。