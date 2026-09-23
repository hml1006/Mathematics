# Black-Scholes 型抛物方程

> **一句话大白话**：把期权价格看成"当前时刻 $t$ 与当前股价 $S$"的函数，它必须满足一条带终端条件的抛物型偏微分方程；解出这条方程，就给期权定了价。

> **小例子**：欧式看涨期权在到期日支付的金额是 $\Phi(S)=\max(S-K,0)$；把它当作终端条件代入本方程求解，得到的正是经典的 Black–Scholes 定价公式。

## 一、定理介绍

> **前置依赖**：Itô引理、Kolmogorov后向方程、条件期望的存在唯一性

Black–Scholes 型抛物方程是金融数学的奠基石：在不允许套利的市场中，任何可复制的衍生品价格 $V(t,S)$ 都必须满足

$$
\frac{\partial V}{\partial t}+\frac12\sigma^2S^2\frac{\partial^2 V}{\partial S^2}+rS\frac{\partial V}{\partial S}-rV=0,\qquad V(T,S)=\Phi(S),
$$

其中 $r$ 为无风险利率、$\sigma$ 为波动率、$\Phi$ 为到期支付函数。它本质上是一条**后向抛物型方程**：二阶项来自扩散（波动），一阶项与零阶项 $(-rV)$ 来自漂移与折现。Black 与 Scholes（1973）用"复制组合 + 无套利"导出它并给出闭式解，Merton 随后补上严格论证，这是随机分析在经济学中最著名的一次应用。

## 二、原理思路

1. **复制与对冲**：设价格函数 $V$ 足够光滑。持有 $1$ 份期权、卖空 $\Delta$ 份标的构成组合 $\Pi=V-\Delta S$。取 $\Delta=\partial_SV$，则 $\Pi$ 的瞬时随机项被完全对冲，$d\Pi$ 变成**无风险**增量。
2. **无套利定价**：无风险组合的收益率必须等于 $r$，即 $d\Pi=r\Pi\,dt$；比较 $dt$ 系数即得方程。
3. **后向方程视角**：风险中性测度下标的是几何布朗运动，生成元 $L=rS\partial_S+\frac12\sigma^2S^2\partial_S^2$；折现带来的 $(-rV)$ 使方程成为 $(\partial_t+L-r)V=0$，正是 Kolmogorov 后向方程的折现形式。
4. **求解**：由后向方程的鞅表示得 $V(t,S)=e^{-r(T-t)}\mathbb E[\Phi(S_T)\mid S_t=S]$，再作变量替换化为热方程算得闭式解。

## 三、定理的严格表述

设标的在风险中性测度下服从几何布朗运动 $dS_t=rS_t\,dt+\sigma S_t\,dW_t$，$S_t=S$，到期支付 $\Phi$ 满足适当增长条件。若 $V\in C^{1,2}([0,T]\times\mathbb R_+)$ 有界且满足

$$
\frac{\partial V}{\partial t}+\frac12\sigma^2S^2\frac{\partial^2 V}{\partial S^2}+rS\frac{\partial V}{\partial S}-rV=0,\qquad V(T,S)=\Phi(S),
$$

则对 $0\le t\le T$ 有

$$
V(t,S)=e^{-r(T-t)}\,\mathbb E\bigl[\Phi(S_T)\,\big|\,S_t=S\bigr].
$$

特别地取 $\Phi(S)=\max(S-K,0)$，经热方程求解得 Black–Scholes 公式

$$
V(t,S)=S\,\mathcal N(d_1)-Ke^{-r(T-t)}\,\mathcal N(d_2),\qquad
d_{1,2}=\frac{\ln(S/K)+(r\pm\frac12\sigma^2)(T-t)}{\sigma\sqrt{T-t}},
$$

其中 $\mathcal N$ 为标准正态分布函数。

## 四、证明过程

**证明。**

**步骤 1（组合与自融资）。** 设 $V(t,S)$ 为期权价格，组合 $\Pi=V-\Delta S$，则 $d\Pi=dV-\Delta\,dS$。对 $V$ 用 Itô 引理（$S$ 的二次变差 $(dS_t)^2=\sigma^2S_t^2dt$）：

$$
dV=\Bigl(\frac{\partial V}{\partial t}+\frac12\sigma^2S^2\frac{\partial^2 V}{\partial S^2}\Bigr)dt+\frac{\partial V}{\partial S}\,dS .
$$

**步骤 2（对冲随机项）。** 取 $\Delta=\partial_SV$，两项 $dS$ 相消：

$$
d\Pi=\Bigl(\frac{\partial V}{\partial t}+\frac12\sigma^2S^2\frac{\partial^2 V}{\partial S^2}\Bigr)dt ,
$$

右端不再含 $dW_t$，故 $\Pi$ 的瞬时增量是确定的。

**步骤 3（无套利方程）。** 无风险组合收益率必须为 $r$：$d\Pi=r\Pi\,dt=r(V-S\,\partial_SV)\,dt$。与步骤 2 比较 $dt$ 系数并整理：

$$
\frac{\partial V}{\partial t}+\frac12\sigma^2S^2\frac{\partial^2 V}{\partial S^2}+rS\frac{\partial V}{\partial S}-rV=0 .
$$

**步骤 4（与后向方程一致）。** 由 $L=rS\partial_S+\frac12\sigma^2S^2\partial_S^2$，上式等价于

$$
\Bigl(\frac{\partial}{\partial t}+L-r\Bigr)V=0,\qquad V(T,S)=\Phi(S),
$$

即在 Kolmogorov 后向方程中加入折现项 $-rV$。

**步骤 5（鞅表示）。** 令 $Y_s=e^{-r(s-t)}V(s,S_s)$，由 Itô 引理与步骤 4 的方程，

$$
dY_s=e^{-r(s-t)}\Bigl(\frac{\partial V}{\partial s}+LV-rV\Bigr)ds+e^{-r(s-t)}\sigma S_s\frac{\partial V}{\partial S}dW_s
=e^{-r(s-t)}\sigma S_s\frac{\partial V}{\partial S}dW_s ,
$$

为（局部）鞅，由 $V$ 有界它为真鞅。取条件期望（条件期望的存在唯一性）并用 $V(T,S_T)=\Phi(S_T)$，得

$$
V(t,S)=e^{-r(T-t)}\,\mathbb E\bigl[\Phi(S_T)\,\big|\,S_t=S\bigr].
$$

**步骤 6（化为热方程并解出闭式）。** 作替换 $x=\ln S$、$\tau=T-t$、$V=e^{-r\tau}u(\tau,x)$，并令 $y=x+(r-\frac12\sigma^2)\tau$ 消去漂移，方程化为标准热方程

$$
\frac{\partial u}{\partial \tau}=\frac12\sigma^2\frac{\partial^2 u}{\partial y^2},
$$

其解为高斯热核与初值 $u(0,y)=\Phi(e^{y})$ 的卷积。取 $\Phi(S)=\max(S-K,0)$，利用 $S_T=S\exp\bigl((r-\frac12\sigma^2)\tau+\sigma\sqrt\tau Z\bigr)$（$Z\sim\mathcal N(0,1)$）与正态分布的直接计算，即得步骤 3 后的 Black–Scholes 公式。$\square$

## 五、应用与意义

Black–Scholes 型抛物方程把"无套利"原理翻译成一条可解的偏微分方程，开创了衍生品定价的定量时代：它给出欧式期权的闭式价格与全套 Greeks（$\partial_SV$、$\partial_S^2V$、$\partial_tV$ 等风险敏感度），并支撑二叉树、有限差分、蒙特卡洛等数值方法。作为一条后向抛物方程，它也是 Feynman–Kac 公式与 HJB 方程的原型实例，在风险管理、实物期权与利率模型中被广泛推广（如局部波动率、随机波动率模型）。

## 相关条目

- [Feynman-Kac公式](./Feynman-Kac公式.md)：把本方程的解写成带折现的期望。
- [Kolmogorov后向方程](./Kolmogorov后向方程.md)：本方程是其加入折现项后的情形。
- [Itô引理](./Itô引理.md)：步骤 1、5 计算复合过程微分所用。
- [条件期望的存在唯一性](../第24级-概率论基础/条件期望的存在唯一性.md)：步骤 5 取条件期望的依据。
