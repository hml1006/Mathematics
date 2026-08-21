# Riccati 方程与线性二次调节器（LQR）

> **一句话大白话**：LQR 在"省力"和"别偏离目标"之间取最佳平衡，关键落在一个Riccati方程上：解出 $P$ 后，最优反馈增益就是 $K=-R^{-1}B^TP$，系统既稳定又最优。
>
> **小例子**：对线性系统 $\dot x=Ax+Bu$ 最小化 $\int_0^\infty(x^TQx+u^TRu)\,dt$，令 $A^TP+PA-PBR^{-1}B^TP+Q=0$ 求正定解 $P$，即得稳定且最优的反馈 $u=Kx$。

## 一、定理介绍

> **前置依赖**：Hamilton–Jacobi–Bellman 方程、二次型值函数猜测、能控性与能观性（能镇定性/能检测性）、Lyapunov 稳定性方法与 LaSalle 不变集原理、矩阵方程正定解的存在唯一性。

线性二次调节器（Linear Quadratic Regulator, LQR）是最优控制中最经典、应用最广泛的问题之一。它研究如何为线性系统选择一个状态反馈控制律，使得一个关于状态与控制的二次性能指标达到最小。该问题的最优解可由代数 Riccati 方程（Algebraic Riccati Equation, ARE）或微分 Riccati 方程的解给出，形成线性状态反馈 $u^*=-Kx$。

## 二、原理思路

对线性系统 $\dot{x}=Ax+Bu$，考虑二次代价
$$
J=\int_0^{\infty}\bigl(x^{\mathsf{T}}Qx+u^{\mathsf{T}}Ru\bigr)\,dt.
$$
由于被积函数关于状态和控制均为二次型，且系统动态为线性，值函数可猜测为二次型 $V(x)=x^{\mathsf{T}}Px$。将其代入 HJB 方程，对 $u$ 求极小，可导出关于 $P$ 的 Riccati 方程。最优反馈增益为 $K=R^{-1}B^{\mathsf{T}}P$。

## 三、定理的严格表述

考虑线性时不变系统
$$
\dot{x}=Ax+Bu,
$$
其中 $x\in\mathbb{R}^n$，$u\in\mathbb{R}^m$。性能指标为
$$
J(x_0,u)=\int_0^{\infty}\bigl(x^{\mathsf{T}}Qx+u^{\mathsf{T}}Ru\bigr)\,dt,
$$
其中 $Q=Q^{\mathsf{T}}\succeq 0$，$R=R^{\mathsf{T}}\succ 0$。

**LQR 定理**：若 $(A,B)$ 能控（或能镇定）且 $(A,Q^{1/2})$ 能观（或能检测），则存在唯一的半正定解 $P=P^{\mathsf{T}}\succeq 0$ 满足代数 Riccati 方程
$$
A^{\mathsf{T}}P+PA-PBR^{-1}B^{\mathsf{T}}P+Q=0.
$$
最优控制为状态反馈
$$
u^*(t)=-Kx(t),\qquad K=R^{-1}B^{\mathsf{T}}P,
$$
闭环系统
$$
\dot{x}=(A-BK)x
$$
渐近稳定，且最优性能指标为
$$
J^*(x_0)=x_0^{\mathsf{T}}Px_0.
$$

### 有限时间 LQR

对有限时间 $[0,T]$，最优值函数为 $V(t,x)=x^{\mathsf{T}}P(t)x$，其中 $P(t)$ 满足微分 Riccati 方程
$$
-\dot{P}=A^{\mathsf{T}}P+PA-PBR^{-1}B^{\mathsf{T}}P+Q,\qquad P(T)=P_f.
$$

## 四、证明过程

**由 HJB 方程推导 ARE**：假设值函数 $V(x)=x^{\mathsf{T}}Px$。连续时间无折扣 HJB 方程为
$$
0=\inf_u\bigl\{x^{\mathsf{T}}Qx+u^{\mathsf{T}}Ru+\nabla V^{\mathsf{T}}(Ax+Bu)\bigr\}.
$$
由于 $\nabla V=2Px$，对 $u$ 求导并令其为零：
$$
2Ru+2B^{\mathsf{T}}Px=0\quad\Longrightarrow\quad u^*=-R^{-1}B^{\mathsf{T}}Px.
$$
代回 HJB 方程：
$$
0=x^{\mathsf{T}}Qx+x^{\mathsf{T}}PBR^{-1}B^{\mathsf{T}}Px+2x^{\mathsf{T}}P(A-BR^{-1}B^{\mathsf{T}}P)x.
$$
整理得
$$
0=x^{\mathsf{T}}\bigl(Q+A^{\mathsf{T}}P+PA-PBR^{-1}B^{\mathsf{T}}P\bigr)x,
$$
对所有 $x$ 成立，即得 ARE。

**稳定性证明**：取 $V(x)=x^{\mathsf{T}}Px$ 作为闭环系统
$$
\dot{x}=(A-BR^{-1}B^{\mathsf{T}}P)x
$$
的 Lyapunov 函数。沿轨迹求导：
$$
\dot{V}=x^{\mathsf{T}}\bigl[(A-BK)^{\mathsf{T}}P+P(A-BK)\bigr]x.
$$
由 ARE 可得
$$
(A-BK)^{\mathsf{T}}P+P(A-BK)=-Q-PBR^{-1}B^{\mathsf{T}}P.
$$
右端为负定（或半负定且由能观性保证不增于非零轨迹），结合 LaSalle 不变集原理，闭环系统渐近稳定。

## 五、应用与意义

- **经典控制**：LQR 提供了一种系统化的多变量控制器设计方法，兼顾响应性能与控制能量。
- **航空航天**：飞行器姿态控制、轨道保持与自动着陆中广泛使用 LQR/LQG（含 Kalman 滤波）框架。
- **机器人**：机械臂、倒立摆、无人车的平衡与轨迹跟踪常以 LQR 为基准控制器。
- **模型预测控制（MPC）**：LQR 的有限时域版本是线性 MPC 问题的核心子问题。
- **理论与计算**：Riccati 方程连接了最优控制、Hamilton 系统、谱分解与 $H_2$/$H_\infty$ 控制，是现代鲁棒控制理论的重要出发点。
