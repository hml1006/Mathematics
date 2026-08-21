# 极值指数与MDA的刻画（von Mises条件）

> **一句话大白话**：通过观察"尾商函数" $r(x)$ 在右端点附近的增长率，就能判断一个具体分布的最大值落在三大吸引域中的哪一个。
>
> **小例子**：指数分布 $r(x)=1$、$r'(x)=0$，故属于 Gumbel 吸引域；与 Fisher-Tippett-Gnedenko 给出的标准极限吻合。

## 一、定理介绍

设 $F$ 为绝对连续分布，密度 $f$，右端点 $\omega(F)=\sup\{x:F(x)<1\}\le\infty$，定义尾商函数
$$
r(x)=\frac{1-F(x)}{f(x)},\qquad x<\omega(F).
$$
von Mises 条件用 $\lim r'(x)$ 或 $\lim\frac{xr'(x)}{r(x)}$ 判别 $F$ 落入哪个最大吸引域（MDA），为判断"属于何种极值分布"提供了可操作的准则。

## 二、原理思路

通过尾商函数把分布尾部的"相对剩余量"线性化，并由 $U(t)=F^{-1}(1-1/t)$ 到 $U'(t)=r(U(t))/t$ 建立与归一化常数的联系。不同情形下 $r$ 呈现不同增长（缓变、幂律、幂律之有界端点），据此选取 $a_n,b_n$ 使 $F^n(a_nx+b_n)$ 收敛到对应的标准极值分布。

## 三、定理的严格表述

设 $F$ 绝对连续、密度 $f$、右端点 $\omega(F)$，$r(x)=(1-F(x))/f(x)$。则

1. 若 $\lim_{x\to\omega(F)}r'(x)=0$，则 $F\in\text{MDA}(G_0)$（Gumbel）。
2. 若存在 $\alpha>0$ 使 $\lim_{x\to\infty}\frac{xr'(x)}{r(x)}=\alpha$ 且 $\omega(F)=\infty$，则 $F\in\text{MDA}(G_{1,1/\alpha})$（Fréchet）。
3. 若存在 $\alpha>0$ 使 $\lim_{x\to\omega(F)}\frac{xr'(x)}{r(x)}=-\alpha$ 且 $\omega(F)<\infty$，则 $F\in\text{MDA}(G_{2,1/\alpha})$（Weibull）。

这里 $F\in\text{MDA}(G)$ 指存在 $a_n>0,b_n$ 使 $\frac{M_n-b_n}{a_n}\xrightarrow{d}G$。

## 四、证明过程

**步骤1：Gumbel 情形。** 记 $U(t)=F^{-1}(1-1/t)$，由 $F(U(t))=1-1/t$ 求导得 $U'(t)=r(U(t))/t$。von Mises 条件 $r'\to0$ 使 $r$ 为缓变函数，存在 $a(t)=r(U(t))$ 使
$$
\lim_{t\to\infty}\frac{U(tx)-U(t)}{a(t)}=\log x.
$$
取 $a_n=r(U(n))$、$b_n=U(n)$，得 $F^n(a_nx+b_n)\to e^{-e^{-x}}$。

**步骤2：Fréchet 情形。** $\frac{r'}{r}\sim\frac{\alpha}{x}$ 积分得 $r(x)\sim Cx^\alpha$，再由 $U'(t)\sim CU(t)^\alpha/t$ 得 $U(t)$ 幂律增长。取 $a_n=U(n)$、$b_n=0$，得 $F^n(a_nx)\to e^{-x^{-\alpha}}$。

**步骤3：Weibull 情形。** 由 $\frac{xr'}{r}\to-\alpha$ 及 $\omega(F)<\infty$，$r(x)\sim C(\omega(F)-x)^\alpha$，解得 $\omega(F)-U(t)\sim C't^{-1/(\alpha-1)}$。取 $a_n=\omega(F)-U(n)$、$b_n=\omega(F)$，得 $F^n(a_nx+b_n)\to e^{-(-x)^\alpha}$。$\square$

## 五、应用与意义

von Mises 条件把三大吸引域的理论区分转化为对尾商函数可检验的极限条件，是极值建模中选择 GEV/GPD 参数族与实际分布类型的桥梁。它指导数据诊断（判断是否重尾、有无上界），并从理论上刻画了哪些分布属于尾部规则变化的吸引域。