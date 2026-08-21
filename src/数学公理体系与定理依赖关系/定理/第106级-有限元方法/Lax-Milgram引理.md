# Lax-Milgram引理

> **一句话大白话**：只要一个"泛函表示的椭圆算子"满足"不太小（强制）、不太疯（有界）"两个条件，对应的变分问题就一定有且只有一个解——且解连续依赖右端。
>
> **小例子**：$-\Delta u=f$（带齐次 Dirichlet 边值）的变分形式 $a(u,v)=\int\nabla u\cdot\nabla v$ 满足强制性与有界性，Lax–Milgram 直接给出 $H^1_0$ 中解的存在唯一。

## 一、定理介绍

> **前置依赖**：Hilbert 空间与对偶空间、Riesz 表示定理、双线性形的连续性与强制性、封闭算子（闭图）与不动点论证、连续线性泛函。

Lax–Milgram 引理是椭圆型偏微分方程弱解理论的中枢：对 Hilbert 空间 $V$ 上的双线性形 $a(\cdot,\cdot)$，当它满足强制（coercive）与连续有界两条件时，抽象变分问题 $a(u,v)=\ell(v)\ (\forall v\in V)$ 对每个连续线性泛函 $\ell$ 有唯一解，且映射 $\ell\mapsto u$ 连续。它统一处理了 Poisson、Helmholtz、二阶椭圆算子的弱解存在性，也是有限元离散稳定性与 Céa 引理的理论基础。

## 二、原理思路

核心是 Riesz 表示定理与闭图/不动点论证。把 $a$ 的作用转化为算子 $A:V\to V$（由 $a(u,v)=\langle Au,v\rangle$ 定义），强制使 $A$ 在 $V$ 上可逆，从而 $u=A^{-1}\ell$。存在性既可通过由 Riesz 与 Brouwer 不动点，也可通过正交补刻画：证明 $A(V)=V$ 且 $A$ 单射闭，从而满射。关键验证依赖强制性给出的"下界"与连续性给出的"上界"。

## 三、定理的严格表述

设 $V$ 为实 Hilbert 空间，商（对偶）$V'$。设 $a:V\times V\to\mathbb{R}$ 满足：

1. **连续性**（有界性）：存在 $M\ge0$ 使 $|a(u,v)|\le M\|u\|\,\|v\|$，$\forall u,v\in V$；
2. **强制性**（$V$-椭圆性）：存在 $\alpha>0$ 使 $a(u,u)\ge\alpha\|u\|^2$，$\forall u\in V$。

则对任意 $\ell\in V'$，变分问题：求 $u\in V$ 使
$$
a(u,v)=\ell(v),\quad \forall v\in V,
$$
存在唯一解 $u\in V$，且满足稳定性估计
$$
\alpha\,\|u\|\le\|\ell\|_{V'}.
$$

## 四、证明过程（Riesz + 不动点/闭算子）

1. **定义算子**。由 Riesz 表示定理，存在有界线性算子 $A:V\to V$ 与向量 $\lambda\in V$ 满足 ${a(u,v)=\langle Au,v\rangle}$、$\ell(v)=\langle \lambda,v\rangle$。则原问题化为 $Au=\lambda$。

2. **强制蕴含有界性与单射**。由强制性，$a(u,u)\ge\alpha\|u\|^2$；结合连续性 $a(u,u)\le M\|u\|^2$。又 $a(u,u)=\langle Au,u\rangle$，故
   $$
   \alpha\|u\|^2\le\langle Au,u\rangle\le\|Au\|\,\|u\|\quad\Rightarrow\quad\|Au\|\ge\alpha\|u\|.
   $$
   于是 $A$ 有正下界、单射。

3. **证明 $A(V)=V$（满的/闭范围）**. 若 $A(V)\subsetneq V$，取 $V$ 中非零元 $w\perp A(V)$，即 $\langle Au,w\rangle=0\ (\forall u)$。特别取 $u=w$：$\langle Aw,w\rangle=a(w,w)\ge\alpha\|w\|^2>0$ 与正交性矛盾。故 $A(V)=V$。

4. **存在唯一与连续依赖**。$A$ 双射，$u=A^{-1}\lambda$ 唯一；且 $\alpha\|u\|\le\|Au\|=\|\lambda\|=\|\ell\|_{V'}$，给出稳定性估计。$\blacksquare$

**注.** 对非对称（非自共轭）但有强制性的 $a$，仍需成立（不动点耦合法）；对不定问题需改用更多前提（Gårding 不等式 + 正则性等）。

## 五、应用与意义

- **弱解存在性**：统一给出椭圆边值问题（Poisson、Neumann、Robin、多物理耦合线性问题）在 $H^1_0$ 等空间中的解存在唯一。
- **有限元地基**：Lax–Milgram 保证离散与连续变分问题的良定性，并为 Céa 引理（离散解的能量误差控制）提供前提。
- **稳定估计**：$u$ 对 $\ell$ 的连续依赖 $\alpha\|u\|\le\|\ell\|$ 是 a priori 界与稳定性的基础。
- **数值分析**：强制性常数 $\alpha$、连续性常数 $M$ 直接进入 Céa 引理与误差常数 $M/\alpha$，是网格收敛阶分析的起点。