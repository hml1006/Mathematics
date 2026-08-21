# Grothendieck 群 K0 的泛性质

> **一句话大白话**：$K_0(R)$ 是由所有有限生成射影 $R$-模的符号 $[P]$ 生成的阿贝尔群，满足 $[P]+[Q]=[P\oplus Q]$；它满足"最优映射"的泛性质——任何"加法型映射"都唯一地经过它分解。
>
> **小例子**：对域 $F$，射影模都是向量空间，$K_0(F)\cong\mathbb{Z}$（$[F^n]\mapsto n$）；对 PID（如 $\mathbb{Z}$），每个有限生成射影模都自由，同样有 $K_0(R)\cong\mathbb{Z}$。

## 一、定理介绍

> **前置依赖**：有限生成射影模、自由阿贝尔群与商群、群同态基本定理、泛性质。

Grothendieck 群 $K_0(R)$（Grothendieck 于 1950 年代研究 Riemann-Roch 时引入）是把环 $R$ 上的有限生成射影模（"几何对象"如向量丛）抽象为一个阿贝尔群不变量。泛性质定理断言 $K_0(R)$ 是"群完成"的典范对象，是代数 K 理论谱系（$K_0,K_1,K_2,\dots$）的出发点和最基本的结构性质。

## 二、原理思路

把射影模同构类生成的自由阿贝尔群模去关系 $[P\oplus Q]-[P]-[Q]$ 构成的子群得到 $K_0(R)=S/N$。泛性质的证明通过"从自由生成的 $S$ 上定义映射再穿过商群"的标准手法：定义 $\psi:S\to G$，验证 $N\subseteq\ker\psi$，由同态基本定理得到唯一诱导同态 $\tilde{\varphi}:K_0(R)\to G$。

## 三、定理的严格表述

设 $R$ 为含幺环，$K_0(R)$ 是由有限生成射影 $R$-模的符号 $[P]$ 生成的阿贝尔群，满足对任何正合列 $0\to P'\to P\to P''\to0$（$P',P,P''$ 有限生成射影）有 $[P]=[P']+[P'']$。则对任何阿贝尔群 $G$ 和任何映射 $\varphi:\{\text{有限生成射影 }R\text{-模}\}\to G$，满足：
- 若 $P\cong Q$ 则 $\varphi(P)=\varphi(Q)$；
- $\varphi(P\oplus Q)=\varphi(P)+\varphi(Q)$；
则存在唯一的群同态 $\tilde{\varphi}:K_0(R)\to G$ 使 $\tilde{\varphi}([P])=\varphi(P)$ 对所有 $P$ 成立。

## 四、证明过程

**证明：**

**步骤 1：建模。** 记 $S$ 为所有有限生成射影 $R$-模同构类的自由阿贝尔群，$N=\langle [P\oplus Q]-[P]-[Q]\rangle$，则 $K_0(R)=S/N$。

**步骤 2：定义 $\psi$。** 定义 $\psi(\sum n_i[P_i])=\sum n_i\varphi(P_i)$，因 $S$ 自由阿贝尔，此映射良定。

**步骤 3：验证 $N\subseteq\ker\psi$。** 对生成元 $[P\oplus Q]-[P]-[Q]$，由 $\varphi$ 的加法性：
$$
\psi([P\oplus Q]-[P]-[Q])=\varphi(P\oplus Q)-\varphi(P)-\varphi(Q)=0.
$$
故 $N\subseteq\ker\psi$。

**步骤 4：诱导同态。** 由同态基本定理，$\psi$ 诱导出唯一同态 $\tilde{\varphi}:S/N=K_0(R)\to G$，且 $\tilde{\varphi}([P])=\varphi(P)$。

**步骤 5：唯一性。** 若另一同态 $\tilde{\varphi}'$ 也满足同样条件，则对一切生成元 $[P]$ 有 $\tilde{\varphi}([P])=\tilde{\varphi}'([P])$，故相等。$\square$

## 五、应用与意义

$K_0$ 的泛性质是 K 理论一切结构结论的支点。它保证 $K_0$ 是"最经济的加法不变量"，从而可据以计算：$K_0(F)\cong\mathbb{Z}$、$K_0(R_1\times R_2)\cong K_0(R_1)\oplus K_0(R_2)$、Morita 等价下的不变性（$K_0(M_n(R))\cong K_0(R)$）等。在代数几何中 $K_0(X)$（向量丛的 K 群）与 Grothendieck-Riemann-Roch 定理紧密结合；在拓扑中 $K_0$ 与 Atiyah-Singer 指标理论相接。它亦为高次 K 群（$K_1,K_2$ 及 Quillen 的 $K_n$）的构建奠定概念基础。