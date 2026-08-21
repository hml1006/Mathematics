# Black-Scholes公式

> **一句话大白话**：给欧式期权算"公平保费"的解析公式——保费由股价、波动率、到期时间、行权价和无风险利率决定，公式把它们一锅端出明码标价的价格。
>
> **小例子**：看涨期权价格 $C=S_t\Phi(d_1)-Ke^{-r(T-t)}\Phi(d_2)$：波动率越小、离到期越近、行权价越"虚"，$C$ 越小；公式把看似复杂的期权定价变成套标准正态分布函数就能算的封闭式。

## 一、定理介绍

> **前置依赖**：Ito引理、几何布朗运动（对数正态过程）、热传导方程与Green函数、无套利原理、看跌-看涨平价关系

Black-Scholes 公式给出欧式期权在连续时间 Black-Scholes 模型下的解析定价解。对标的 $S_t$、行权价 $K$、到期 $T$、无风险利率 $r$、波动率 $\sigma$，欧式看涨期权价格为

$$
C(S_t,t)=S_t\Phi(d_1)-K e^{-r(T-t)}\Phi(d_2),
$$
$$
d_1=\frac{\ln(S_t/K)+(r+\sigma^2/2)(T-t)}{\sigma\sqrt{T-t}},\qquad d_2=d_1-\sigma\sqrt{T-t},
$$

其中 $\Phi$ 为标准正态 CDF。它是金融数学最具影响力的成果之一。

## 二、原理思路

核心是"对冲掉风险、按无风险收益计价"。股价满足 $dS=\mu S\,dt+\sigma S\,dW$，依据 Ito 引理跟踪期权价格 $V(S,t)$ 的变化；构造对冲组合 $\Pi=V-\Delta S$，选择 $\Delta=\partial V/\partial S$ 消除随机项，由无套利要求组合收益等于无风险利率，从而导出 Black-Scholes PDE；再经变量代换化为热传导方程并用 Green 函数求解即得封闭公式。

## 三、定理的严格表述

在 Black-Scholes 模型假设（股价对数正态、无摩擦、常数 $r,\sigma$）下，欧式看涨期权价格 $C$ 满足

$$
\frac{\partial V}{\partial t}+rS\frac{\partial V}{\partial S}+\frac12\sigma^2S^2\frac{\partial^2 V}{\partial S^2}-rV=0,\qquad V(S,T)=\max(S-K,0),
$$

其解为如上封闭公式；欧式看跌期权由看跌-看涨平价 $C-P=S-Ke^{-r(T-t)}$ 给出
$$
P(S,t)=Ke^{-r(T-t)}\Phi(-d_2)-S\Phi(-d_1).
$$

## 四、证明过程

**步骤1：建立偏微分方程。** 由 Ito 引理得 $dV=(V_t+\mu S V_S+\tfrac12\sigma^2S^2V_{SS})dt+\sigma S V_S\,dW$。构造 $\Pi=V-\Delta S$ 并取 $\Delta=V_S$，则 $d\Pi=(V_t+\tfrac12\sigma^2S^2V_{SS})dt$。由无套利得 $d\Pi=r\Pi dt$，解得 Black-Scholes PDE。

**步骤2：边界条件。** 终端条件 $V(S,T)=\max(S-K,0)$；$S=0$ 时 $V=0$；$S\to\infty$ 时 $V\sim S$。

**步骤3：化为热传导方程。** 令 $\tau=T-t$、$x=\ln S$、$V=e^{-r\tau}u$，化简得 $
u_\tau=\tfrac12\sigma^2u_{xx}+(r-\tfrac12\sigma^2)u_x$；再令 $y=x+(r-\tfrac12\sigma^2)\tau$，得标准热方程 $w_\tau=\tfrac12\sigma^2w_{yy}$，初值 $w(y,0)=\max(e^y-K,0)$。

**步骤4：求解热方程。** 基本解 $G(y,\tau)=(2\pi\sigma^2\tau)^{-1/2}\exp(-y^2/(2\sigma^2\tau))$，解为
$$
w(y,\tau)=\int_{\ln K}^{\infty}G(y-\xi,\tau)(e^\xi-K)\,d\xi=I_1-I_2.
$$

**步骤5：计算积分。** 配平方得 $I_1=e^{y+\frac12\sigma^2\tau}\Phi\bigl(\frac{y+\sigma^2\tau-\ln K}{\sigma\sqrt\tau}\bigr)$，$I_2=K\Phi\bigl(\frac{y-\ln K}{\sigma\sqrt\tau}\bigr)$。

**步骤6：代回原变量。** 回代 $e^{y+\frac12\sigma^2\tau}=Se^{r(T-t)}$ 并识别 $d_1,d_2$，即得 $C=S\Phi(d_1)-Ke^{-r(T-t)}\Phi(d_2)$。

**步骤7：看跌期权定价。** 由看跌-看涨平价直接给出 $P$。

**结论（$\square$）**：BS 公式给出欧式期权的封闭解析定价。

## 五、应用与意义

Black-Scholes 公式是衍生品定价的里程碑，为期权交易、风险管理与波动率（隐含波动率）推断提供了标准工具，并直接推动了 1973 年以来的期权市场繁荣。其"动态复制 + 无套利定价"框架更成为整个现代金融工程的方法论基石。