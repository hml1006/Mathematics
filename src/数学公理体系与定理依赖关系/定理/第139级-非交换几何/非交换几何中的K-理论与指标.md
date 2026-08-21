# 非交换几何中的K-理论与指标

> **一句话大白话**：C*-代数上的 K-理论（$K_0,K_1$）给"代数几何不变量"当账本；一段短正合列会自动连成一个"六边形蛇形序列"，把指标与 Toeplitz 算子、Bott 周期性串起来算出指标——这是计算各种代数指标的标准装配线。
>
> **小例子**：$0\to J\to\mathcal A\xrightarrow\pi\mathcal B\to0$ 诱导六边形正合序列；连接映射 $\partial:K_1(\mathcal B)\to K_0(J)$ 由提升后的酉产生，经典 Toeplitz 情形 $\partial([f])=\mathrm{Index}(T_f)=-\mathrm{wind}(f)$。

## 一、定理介绍

> **前置依赖**：C*-代数K-理论（K0、K1）、短正合列诱导的长正合序列、Bott周期性、Toeplitz算子指标

K-理论与指标理论断言：C*-代数的短正合列诱导一个**六边形正合序列（Bott 周期序列）**，其连接映射 $\partial$ 由 Toeplitz 算子自然诱导，从而把指标定理（如 Toeplitz 指标）纳入 K-理论的代数框架，并展示 Bott 周期性 $K_i(\mathcal A)\cong K_{i+2}(\mathcal A)$。

## 二、原理思路

对 $\mathcal A$ 的短正合列 $0\to J\to\mathcal A\xrightarrow\pi\mathcal B\to0$，K-函子给出长正合列，因 Bott 周期为 2 呈现为六边形。连接映射 $\partial:K_1(\mathcal B)\to K_0(J)$：把 $\mathcal B$ 的酉 $u$ 提升为 $\mathcal A$ 中的 $v$（非酉），用 $v^*v,vv^*$ 构造投影 $e$，其与固定投影之差在 $J$ 中定义 $K_0$ 类；对偶地 $\partial:K_0(\mathcal B)\to K_1(J)$ 用 $2p-1$ 的可逆化构造酉类。证明分解为良定义性 + 六边形正合性 + Toeplitz 指标对应。

## 三、定理的严格表述

设 $0\to J\to\mathcal A\xrightarrow\pi\mathcal B\to0$ 为 C*-代数短正合列。则存在正合六边形
$$
\begin{array}{ccccccc}
K_0(J)&\to&K_0(\mathcal A)&\to&K_0(\mathcal B)\\
\uparrow&&&&\downarrow\\
K_1(\mathcal B)&\leftarrow&K_1(\mathcal A)&\leftarrow&K_1(J)
\end{array}
$$
连接映射 $\partial\in\{K_0(\mathcal B)\to K_1(J),\,K_1(\mathcal B)\to K_0(J)\}$ 如上。对 Toeplitz 代数序列 $0\to C_0(\mathbb R)\to T\to C(\mathbb T)\to0$，$\partial([f])=\mathrm{Index}(T_f)=-\mathrm{wind}(f)$。且 $K_i(\mathcal A)\cong K_{i+2}(\mathcal A)$（Bott 周期）。

## 四、证明过程

**步骤1：建立框架。** 设短正合列，$i$ 为含入、$\pi$ 为商映射。

**步骤2：构造 $\partial:K_1(\mathcal B)\to K_0(J)$。** 取 $[u]\in K_1(\mathcal B)$（$u\in M_n(\mathcal B)$ 酉），由 $\pi$ 满射取提升 $v\in M_n(\mathcal A)$，$\pi(v^*v)=\pi(vv^*)=I$。定义投影
$$
e=\begin{pmatrix}v^*v&v^*(1-vv^*)\\(1-v^*v)v&1-v^*v\end{pmatrix}\in M_{2n}(\tilde{\mathcal A}),
$$
且 $e-\begin{pmatrix}I&0\\0&0\end{pmatrix}\in M_{2n}(J)$，令 $\partial([u])=[e]-[\begin{pmatrix}I&0\\0&0\end{pmatrix}]\in K_0(J)$。

**步骤3：良定义性。** 若 $v_1,v_2$ 为 $u$ 的两个提升，则 $v_1-v_2\in M_n(J)$，其投影在 $K_0(J)$ 相等；若 $u_1\sim u_2$ 同伦，沿路径提升可证 $\partial([u_1])=\partial([u_2])$。

**步骤4：构造 $\partial:K_0(\mathcal B)\to K_1(J)$。** 取投影 $[p]\in K_0(\mathcal B)$，设 $\pi(q)=p$；修正出顶点 $y$ 使 $\pi(y)=2p-1$ 且 $y$ 可逆，定义 $\partial([p])=[y(y^*)^{-1/2}]\in K_1(J)$。

**步骤5：验证六边形正合性。** 在每点证 $\mathrm{im}=\ker$，如 $K_0(\mathcal A)\to K_0(\mathcal B)\to K_1(J)$：若 $[p]=\pi_*([e])$ 可提升，相关酉单位故 $\partial([p])=0$；反之 $\partial([p])=0$ 时可构造 $e\in\mathcal A$ 使 $\pi(e)=p$，故 $\ker\partial=\mathrm{im}\,\pi_*$。

**步骤6：Toeplitz 指标。** 对 $0\to C_0(\mathbb R)\to T\to C(\mathbb T)\to0$，连接映射给出 $\partial([f])=\mathrm{Index}(T_f)$，经典 Toeplitz 指标定理 $\mathrm{Index}(T_f)=-\mathrm{wind}(f)$。

**步骤7：Bott 周期性。** $K_0(\mathbb C)\cong\mathbb Z$，$K_1(\mathbb C)=0$，$K_0(C_0(\mathbb R^2))\cong\mathbb Z$，$K_1(C_0(\mathbb R^2))=0$ 推出 $K_i(\mathcal A)\cong K_{i+2}(\mathcal A)$。

**结论（$\square$）**：六边形正合序列是计算 K-理论并把指标与拓扑连接的基本工具。

## 五、应用与意义

该定理是 C*-代数 K-理论计算与指标理论的核心机制，用于非交换环面、叶状结构、交叉积的 K-群计算并支撑 Connes 指标定理。它把 Toeplitz、指数映射与 Bott 周期统一到代数正合序列语言中，是非交换几何的主要计算引擎之一。