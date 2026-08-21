# Pickands-Balkema-de Haan定理

> **一句话大白话**：对一个足够大的阈值，超过该阈值的"超额量"的条件分布会越来越像一个广义帕累托分布（GPD），这让"只看尾部数据"成为可能。
>
> **小例子**：对日损失序列取 95% 分位作阈值，超过部分的分布可用 GPD 拟合，据此估计 VaR 与极端损失概率。

## 一、定理介绍

> **前置依赖**：条件分布（条件概率）、分布函数与尾部分布、最大吸引域（MDA）、一致收敛、极限的比值运算。

设 $X_1,\dots,X_n$ i.i.d.，分布 $F$，且 $F$ 属于极值分布 $G_\xi$ 的最大吸引域（$\frac{M_n-b_n}{a_n}\xrightarrow{d}G_\xi$）。则对充分大的阈值 $u$，超过量 $Y=X-u$ 的条件分布满足
$$
\lim_{u\to\omega(F)}\;\sup_{0\le y\le\omega(F)-u}\left|F_u(y)-G_{\xi,\sigma(u)}(y)\right|=0,
$$
其中 $G_{\xi,\sigma}$ 为广义帕累托分布（GPD）
$$
G_{\xi,\sigma}(y)=1-\left(1+\xi\frac{y}{\sigma}\right)^{-1/\xi}\quad(\xi\ne0),\qquad
G_{0,\sigma}(y)=1-e^{-y/\sigma}.
$$
它使 POT（峰值超过阈值）方法有了理论根基。

## 二、原理思路

由 $F\in\text{MDA}(G_\xi)$ 得到尾部的指数展开 $t[1-F(a(t)x+b(t))]\to(1+\xi x)^{-1/\xi}$。取 $t=1/(1-F(u))$，把 $F_u(y)=1-(1-F(u+y))/(1-F(u))$ 中分子分母各自的尾部近似代入，比值便约化为 GPD 的形式，其尺度参数随 $u$ 平移 $\sigma(u)=a(t)+\xi(u-b(t))$。

## 三、定理的严格表述

设 $F\in\text{MDA}(G_\xi)$，$F_u(y)=\mathbb P(X-u\le y\mid X>u)$ 为超过量条件分布。则存在 $\sigma(u)>0$ 使
$$
\lim_{u\to\omega(F)}\;\sup_{0\le y\le\omega(F)-u}\left|F_u(y)-G_{\xi,\sigma(u)}(y)\right|=0,
$$
其中 $\sigma(u)=a\left(\frac1{1-F(u)}\right)+\xi\left(u-b\left(\frac1{1-F(u)}\right)\right)$，$G_{\xi,\sigma}$ 为 GPD；$\xi=0$ 时取极限得指数形式 $G_{0,\sigma}(y)=1-e^{-y/\sigma}$。

## 四、证明过程

**步骤1：条件分布。** $F_u(y)=\mathbb P(X-u\le y\mid X>u)=\frac{F(u+y)-F(u)}{1-F(u)}=1-\frac{1-F(u+y)}{1-F(u)}$，$0\le y<\omega(F)-u$。

**步骤2：用吸引域条件。** 由 $F\in\text{MDA}(G_\xi)$，$1-F(x)\sim t^{-1}(1+\xi x_t)^{-1/\xi}$（取 $t=1/(1-F(u))$、$x_t=(u-b(t))/a(t)$）。

**步骤3：比值约化。** 对 $x_t(y)=(u+y-b(t))/a(t)=x_t+y/a(t)$，
$$
1-\frac{1-F(u+y)}{1-F(u)}\to 1-\frac{(1+\xi x_t(y))^{-1/\xi}}{(1+\xi x_t)^{-1/\xi}}=1-\left(1+\frac{\xi y}{\sigma(u)}\right)^{-1/\xi}.
$$

**步骤4：一致收敛。** 由极值理论的一致收敛结果，上述收敛在 $y\in[0,\omega(F)-u)$ 上一致。取 $\xi\to0$ 得 $F_u(y)\to1-e^{-y/\sigma(u)}$。$\square$

## 五、应用与意义

Pickands-Balkema-de Haan 定理是 POT 方法（超过阈值建模）的基石，使只需对少量"超额量"用 GPD 拟合即可刻画整条尾部，数据利用效率高于块极大值法。它在金融风险（VaR/ES）、水文、气象与精算等领域广泛用于极端事件的统计建模。