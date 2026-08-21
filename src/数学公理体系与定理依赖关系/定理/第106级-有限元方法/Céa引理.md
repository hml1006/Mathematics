# Céa引理

> **一句话大白话**：有限元解与真解的误差（在能量范数下）不超过"取全体试探函数做最佳逼近"的误差 —— 网格细化多少，逼近就被"压制"多少，逼近与离散误差一体两翼。
>
> **小例子**：$-\Delta u=f$ 的线性有限元解 $u_h$ 满足 $\|u-u_h\|_{H^1}\le C\,\inf_{v_h\in V_h}\|u-v_h\|_{H^1}$，故只要 $V_h$ 能很好逼近 $u$，误差就小——误差界归结为插值/逼近界。

## 一、定理介绍

Céa 引理是有限元误差分析的核心引理：它把"离散解的误差"转化为"离散空间对真解的最佳逼近误差"，这一转换使得误差分析可以从"构造 $V_h$"（网格与多项式阶）出发去衡量逼近质量。它适用于任何满足 Lax–Milgram 条件的椭圆问题，是"逼近 + 离散稳定性"分开处理的枢纽。

## 二、原理思路

利用 Galerkin 正交性：离散解 $u_h$ 满足 $a(u-u_h,v_h)=0$ 对一切 $v_h\in V_h$。由强制性、连续性与正交性对能量范数 $\|\cdot\|_A$ 的作用，得到"近似误差 $\le C\times$ 逼近误差"的关键不等式：取任意 $v_h\in V_h$（其整体偏差可借由 $a$ 的三角不等式与正交性），正交性让 $\|u-u_h\|_A\le\|u-v_h\|_A$（对能量范数）恰成立。

## 三、定理的严格表述

设 $V$ 是 Hilbert 空间，$a(\cdot,\cdot)$ 满足 Lax–Milgram 条件（连续常数 $M$、强制常数 $\alpha$），$f\in V'$。设 $u\in V$ 为连续问题的解（$a(u,v)=\ell(v),\,\forall v$），$V_h\subset V$ 为有限维有限元空间，$u_h\in V_h$ 为离散解（$a(u_h,v_h)=\ell(v_h),\,\forall v_h\in V_h$）。则
$$
\|u-u_h\|_A\le\inf_{v_h\in V_h}\|u-v_h\|_A,
$$
其中 $\|w\|_A=\sqrt{a(w,w)}$ 为能量范数。用 $V$ 范数表示为
$$
\|u-u_h\|_V\le\frac{M}{\alpha}\inf_{v_h\in V_h}\|u-v_h\|_V.
$$

## 四、证明过程

1. **Galerkin 正交性**。由定义 $a(u,v_h)=\ell(v_h)=a(u_h,v_h)$ 对一切 $v_h\in V_h$，故
   $$
   a(u-u_h,v_h)=0,\quad\forall v_h\in V_h.
   $$

2. **取任意 $v_h$**。对任意 $w_h\in V_h$，令 $w_h-u_h\in V_h$，由正交性 $a(u-u_h,w_h-u_h)=0$。于是
   $$
   \|u-u_h\|_A^2=a(u-u_h,u-u_h)=a(u-u_h,u-w_h)+a(u-u_h,w_h-u_h)=a(u-u_h,u-w_h).
   $$

3. **Cauchy–Schwarz 与能量最简形式**。能量范数下 $a$ 满足 $|a(x,y)|\le\|x\|_A\|y\|_A$，故
   $$
   \|u-u_h\|_A^2\le\|u-u_h\|_A\,\|u-w_h\|_A\quad\Rightarrow\quad\|u-u_h\|_A\le\|u-w_h\|_A.
   $$
   对 $w_h$ 取下确界即得 $\|u-u_h\|_A\le\inf_{v_h}\|u-v_h\|_A$。

4. **$V$ 范数估计**。由强制性 $\alpha\|u-u_h\|^2\le a(u-u_h,u-u_h)\le M\|u-u_h\|\,\|u-u_h\|_A$ 与第 3 步能量界联合得到
   $$
   \|u-u_h\|_V\le\frac{M}{\alpha}\inf_{v_h}\|u-v_h\|_V.
   $$
   $\blacksquare$

## 五、应用与意义

- **误差可减**：把"有限元收敛"转化为"空间逼近能力"（Chebyshev/Weierstrass 型逼近），配合插值误差定理导出 有限元逼近的误差估计。
- **定性论断**：只要 $V_h\to V$ 稠密逼近，则 $u_h\to u$（如网格加细 $h\to0$ 时 $V_h\rightrightarrows$）。
- **稳定性的代价**：常数 $M/\alpha$ 说明条件数/病态控制（预条件）会影响误差质量。
- **耦合后验**：Céa 引理与后验误差估计配合时，用"离散残差"去估计 $\inf_{v_h}\|u-v_h\|$，连接局部误差分析。