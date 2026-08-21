# Weierstrass逼近定理

> **一句话大白话**：任何连续函数都能被多项式"任意精确"地逼近——只要次数够高，多项式可以贴到跟连续函数一样近。
>
> **小例子**：$|\sin x|$ 在 $[0,\pi]$ 上连续，用高次多项式（如 Taylor 部分和配合平滑技巧）可把它在区间上一致逼近到任意误差 $\varepsilon>0$ 以内。

## 一、定理介绍

> **前置依赖**：二项式分布、大数定律、一致连续性、Chebyshev 不等式、一致收敛与稠密性。

Weierstrass 逼近定理是逼近论的开山定理：闭区间上的连续函数可以被多项式一致逼近。它断言多项式在 $C[a,b]$ 中是稠密的，从而把"对连续函数求和、积分、求根"等许多操作归结为对多项式的处理，也为后来的 Bernstein 多项式、Jackson 定理与构造性逼近奠定基础。

## 二、原理思路

核心是"利用光滑化与基函数"。Stone–Weierstrass 版本用"函数的代数/格结构"抽象推广；具体构造可用 Bernstein 多项式——把函数值与二项式分布（以 $t\in[0,1]$ 为成功概率、$n$ 次试验）的期望挂钩，由大数定律保证收敛。Bernstein 构造同时给出显式逼近多项式与逼近误差估计，是构造性证明的典范。

## 三、定理的严格表述

设 $f\in C[a,b]$，$\varepsilon>0$ 任意给定。则存在多项式 $P$，使得
$$
\|f-P\|_\infty=\max_{x\in[a,b]}|f(x)-P(x)|<\varepsilon.
$$
等价地，多项式集 $\mathbb{P}=\bigcup_n\mathbb{P}_n$ 在带一致范数的 $C[a,b]$ 中稠密。

**Bernstein 逼近（具体形式）**：对 $f\in C[0,1]$，其 $n$ 阶 Bernstein 多项式为
$$
B_n f(t)=\sum_{k=0}^{n}\binom{n}{k}f\left(\frac{k}{n}\right)t^{k}(1-t)^{n-k},
$$
则 $B_n f\rightrightarrows f$ 在 $[0,1]$ 上一致收敛。

## 四、证明过程（Bernstein 构造）

1. 不妨设 $f\in C[0,1]$（线性变换 $[a,b]\to[0,1]$）。引入独立的 Bernoulli 试验 $X_1,\dots,X_n$，$P(X_i=1)=t$。记 $S_n=X_1+\dots+X_n\sim\operatorname{Bin}(n,t)$。则
   $$
   B_n f(t)=\mathbb{E}\left[f\left(\frac{S_n}{n}\right)\right].
   $$

2. 由大数定律，$S_n/n\xrightarrow{P} t$。但函数值一致逼近还需借助一致连续性：设 $f$ 的一致连续模为
   $$
   \omega_f(\delta)=\sup_{|x-y|\le\delta}|f(x)-f(y)|\to0\quad(\delta\to0).
   $$

3. 对任意 $\eta>0$ 选 $\delta>0$ 使 $\omega_f(\delta)<\eta$。将期望按 $|S_n/n-t|$ 分界：
   $$
   |f(t)-B_n f(t)|\le\mathbb{E}\left[\left|f(t)-f\left(\frac{S_n}{n}\right)\right|\right]
   \le\eta+2\|f\|_\infty\,P\left(\left|\frac{S_n}{n}-t\right|\ge\delta\right).
   $$

4. 由 Chebyshev 不等式，$\operatorname{Var}(S_n)=nt(1-t)\le n/4$，
   $$
   P\left(\left|\frac{S_n}{n}-t\right|\ge\delta\right)\le\frac{t(1-t)}{n\delta^2}\le\frac{1}{4n\delta^2}.
   $$
   取 $n$ 足够大使上项 $<2\eta/(4\|f\|_\infty)$，则 $|f(t)-B_n f(t)|\le\eta+2\|f\|_\infty\cdot\frac{1}{4n\delta^2}<\eta+\eta=2\eta$（可通过调整常数使任意小）。故 $B_n f\rightrightarrows f$。$\blacksquare$

**注。** 更精细的估计给出 $|f(t)-B_n f(t)|\le C\,\omega_f(1/\sqrt{n})$，这正为 Jackson 定理的量化逼近提供直观基础；Banach 空间形式（Müntz 定理、Lusin），以及 Stone–Weierstrass 用"子代数生成元"抽象化，均有大量推广。

## 五、应用与意义

- **稠密性**：断言多项式是 $C[a,b]$ 的稠密线性子空间，使泛函分析与算子理论中对连续函数的研究可化归为多项式。
- **构造性逼近**：Bernstein 多项式给出显式逼近与误差界，是曲线曲面的 Bezier 表示的理论来源。
- **通往 Jackson 定理**：Bernstein 逼近的收敛速率分析直接启蒙了逼近速率（Jackson）与逆定理（Bernstein 型不等式）理论。
- **数值应用**：为插值、曲线设计、有限元形函数、以及机器学习中"神经/多项式网络"的普适逼近性质提供原型。
## 相关条目

- [Weierstrass 逼近定理（第67级-逼近论与样条理论）](../第67级-逼近论与样条理论/Weierstrass逼近定理.md)：与本条目为同一定理，另收录于第67级-逼近论与样条理论，可交叉参考。
