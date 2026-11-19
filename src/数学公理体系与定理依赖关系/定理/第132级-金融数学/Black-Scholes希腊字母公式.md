# Black-Scholes 希腊字母公式

> **一句话大白话**：Black-Scholes 公式不只给期权一个价格，还能直接回答价格对股价、股价曲率、波动率、时间和利率分别有多敏感；五个希腊字母就是把这些“价格旋钮”的一阶或二阶变化率算出来。
>
> **小例子**：若无分红股票与行权价相等且 $r=0$，则 $d_1=\sigma\sqrt\tau/2$。看涨 Delta 为 $\Phi(d_1)>1/2$，看跌 Delta 为 $\Phi(d_1)-1<0$；两者 Gamma、Vega 完全相同，而看涨 Rho 为正、看跌 Rho 为负。

## 介绍

希腊字母是 Black-Scholes 定价函数对模型参数的偏导数，用于对冲与风险归因。以下公式是无分红、常利率和常波动率模型内的**解析恒等式**，不是经验猜测，也不表示真实市场一定服从这些假设。特别地，Theta 的符号取决于对日历时间 $t$ 还是剩余期限 $\tau$ 求导，本文统一采用市场常见的“日历时间 Theta” $\Theta=\partial V/\partial t$。

## 分析

**前置依赖**：Black-Scholes 公式、Itô 引理与 Black-Scholes PDE、标准正态密度和分布函数、多元链式求导、看跌—看涨平价。

**定理内容**：设 $S>0$、$K>0$、$\tau=T-t>0$、$\sigma>0$，无风险利率 $r$ 为常数且标的不分红。记 $\Phi$ 为标准正态分布函数，$\varphi(x)=\Phi'(x)=(2\pi)^{-1/2}e^{-x^2/2}$，并令

$$
d_1=\frac{\ln(S/K)+(r+\sigma^2/2)\tau}{\sigma\sqrt\tau},
\qquad d_2=d_1-\sigma\sqrt\tau.
$$

欧式看涨、看跌价格分别为

$$
C=S\Phi(d_1)-Ke^{-r\tau}\Phi(d_2),
$$

$$
P=Ke^{-r\tau}\Phi(-d_2)-S\Phi(-d_1).
$$

### 1. Delta：股价一阶敏感度

$$
\boxed{\Delta_C=\frac{\partial C}{\partial S}=\Phi(d_1)}
$$

$$
\boxed{\Delta_P=\frac{\partial P}{\partial S}
=\Phi(d_1)-1=-\Phi(-d_1)}.
$$

### 2. Gamma：股价二阶敏感度

$$
\boxed{\Gamma_C=\Gamma_P
=\frac{\partial^2C}{\partial S^2}
=\frac{\varphi(d_1)}{S\sigma\sqrt\tau}}.
$$

### 3. Vega：波动率敏感度

这里 Vega 定义为对 $\sigma$ 本身求导，即 $\sigma$ 增加 $1.00$ 时的价格变化；若按“一个波动率点”即 $0.01$ 报价，数值需再除以 $100$。

$$
\boxed{\operatorname{Vega}_C=\operatorname{Vega}_P
=\frac{\partial C}{\partial\sigma}
=S\varphi(d_1)\sqrt\tau}.
$$

### 4. Theta：日历时间敏感度

以下 $\Theta=\partial V/\partial t$，而 $\partial\tau/\partial t=-1$：

$$
\boxed{\Theta_C
=-\frac{S\varphi(d_1)\sigma}{2\sqrt\tau}
-rKe^{-r\tau}\Phi(d_2)}
$$

$$
\boxed{\Theta_P
=-\frac{S\varphi(d_1)\sigma}{2\sqrt\tau}
+rKe^{-r\tau}\Phi(-d_2)}.
$$

若改用剩余期限偏导 $\partial V/\partial\tau$，则两式整体变号，即 $\partial V/\partial\tau=-\Theta$。

### 5. Rho：利率敏感度

$$
\boxed{\operatorname{Rho}_C=\frac{\partial C}{\partial r}
=K\tau e^{-r\tau}\Phi(d_2)}
$$

$$
\boxed{\operatorname{Rho}_P=\frac{\partial P}{\partial r}
=-K\tau e^{-r\tau}\Phi(-d_2)}.
$$

这些公式满足看跌—看涨平价 $C-P=S-Ke^{-r\tau}$ 所要求的全部导数关系，并且看涨、看跌各自满足

$$
\Theta+rS\Delta+\frac12\sigma^2S^2\Gamma-rV=0.
$$

## 思考过程

直接对 $S\Phi(d_1)$ 求导时，$d_1,d_2$ 本身也含 $S,\sigma,r,\tau$，看似会出现大量项。关键化简恒等式是

$$
Ke^{-r\tau}\varphi(d_2)=S\varphi(d_1),
$$

因为 $d_1^2-d_2^2=2\ln(S/K)+2r\tau$。它使 Delta 中两个含正态密度的项恰好抵消，也把 Vega 等公式压缩成简洁形式。

看跌公式无需重新逐项硬算：平价 $C-P=S-Ke^{-r\tau}$ 对 $S$ 的二阶导数为零、与 $\sigma$ 无关，所以两边 Gamma 和 Vega 相同；对 $S,t,r$ 求导则分别给出 Delta、Theta、Rho 的差额。最后用 Black-Scholes PDE 检验五个偏导是否相容，可避免 Theta 符号错误。

## 证明过程

### 1. 准备求导恒等式

由 $d_2=d_1-\sigma\sqrt\tau$ 得

$$
\frac{\partial d_1}{\partial S}
=\frac{\partial d_2}{\partial S}
=\frac1{S\sigma\sqrt\tau}.
$$

又由

$$
d_1^2-d_2^2=(d_1-d_2)(d_1+d_2)
=2\ln(S/K)+2r\tau
$$

得到 $\varphi(d_2)=\varphi(d_1)e^{\ln(S/K)+r\tau}$，即

$$
Ke^{-r\tau}\varphi(d_2)=S\varphi(d_1).
$$

### 2. Delta 与 Gamma

对看涨价格求 $S$ 的偏导：

$$
\begin{aligned}
\Delta_C
&=\Phi(d_1)+S\varphi(d_1)d_{1,S}
-Ke^{-r\tau}\varphi(d_2)d_{2,S}\\
&=\Phi(d_1)
+\frac{S\varphi(d_1)-Ke^{-r\tau}\varphi(d_2)}{S\sigma\sqrt\tau}
=\Phi(d_1).
\end{aligned}
$$

再求一次导数即得 $\Gamma_C=\varphi(d_1)/(S\sigma\sqrt\tau)$。平价给出 $\Delta_C-\Delta_P=1$ 与 $\Gamma_C=\Gamma_P$，从而得到看跌两式。

### 3. Vega

直接求导时有

$$
\frac{\partial d_1}{\partial\sigma}=-\frac{d_2}{\sigma},
\qquad
\frac{\partial d_2}{\partial\sigma}=-\frac{d_1}{\sigma}.
$$

因此

$$
\begin{aligned}
\frac{\partial C}{\partial\sigma}
&=S\varphi(d_1)\left(-\frac{d_2}{\sigma}\right)
-Ke^{-r\tau}\varphi(d_2)\left(-\frac{d_1}{\sigma}\right)\\
&=\frac{S\varphi(d_1)}{\sigma}(d_1-d_2)
=S\varphi(d_1)\sqrt\tau .
\end{aligned}
$$

平价右端不含 $\sigma$，故看跌 Vega 相同。

### 4. Theta

固定 $S,K,r,\sigma$，对 $\tau$ 求导。同样的正态密度化简给出

$$
\frac{\partial C}{\partial\tau}
=\frac{S\varphi(d_1)\sigma}{2\sqrt\tau}
+rKe^{-r\tau}\Phi(d_2).
$$

因 $\Theta_C=\partial C/\partial t=-\partial C/\partial\tau$，得到看涨 Theta。平价两边对 $t$ 求导给出

$$
\Theta_C-\Theta_P=-rKe^{-r\tau},
$$

所以 $\Theta_P=\Theta_C+rKe^{-r\tau}$，展开即看跌公式。

### 5. Rho 与 PDE 检验

对 $r$ 求导并再次使用 $Ke^{-r\tau}\varphi(d_2)=S\varphi(d_1)$，含密度的项抵消，留下

$$
\operatorname{Rho}_C=K\tau e^{-r\tau}\Phi(d_2).
$$

平价对 $r$ 求导给出 $\operatorname{Rho}_C-\operatorname{Rho}_P=K\tau e^{-r\tau}$，从而得到看跌 Rho。最后将五个公式代入 Black-Scholes PDE，可直接核对恒等式成立。$\square$

## 课堂问答

**老师**：五个希腊字母分别对什么变量求导，看涨期权的核心公式是什么？

**学生**：Delta、Gamma 分别是对 $S$ 的一阶、二阶导数，Vega 对 $\sigma$，Theta 对日历时间 $t$，Rho 对 $r$。看涨公式为 $\Delta_C=\Phi(d_1)$、$\Gamma_C=\varphi(d_1)/(S\sigma\sqrt\tau)$、$\operatorname{Vega}_C=S\varphi(d_1)\sqrt\tau$、$\Theta_C=-S\varphi(d_1)\sigma/(2\sqrt\tau)-rKe^{-r\tau}\Phi(d_2)$、$\operatorname{Rho}_C=K\tau e^{-r\tau}\Phi(d_2)$。

**老师（追问）**：为什么看跌与看涨的 Gamma、Vega 相同，而 Delta、Theta、Rho 不同？

**学生**：平价为 $C-P=S-Ke^{-r\tau}$。右端对 $S$ 的二阶导数为零且不含 $\sigma$，所以 $\Gamma_C=\Gamma_P$、$\operatorname{Vega}_C=\operatorname{Vega}_P$；右端对 $S,t,r$ 有非零导数，分别导致 $\Delta_C-\Delta_P=1$、$\Theta_C-\Theta_P=-rKe^{-r\tau}$、$\operatorname{Rho}_C-\operatorname{Rho}_P=K\tau e^{-r\tau}$。

**老师（拓展）**：Theta 为什么在不同资料里符号相反？这些公式能否直接当成真实市场的风险定律？

**学生**：本文 $\Theta=\partial V/\partial t$；若定义 $\partial V/\partial\tau$，由于 $\tau=T-t$，两者正好变号，必须先核对约定。公式在 Black-Scholes 模型内是严格恒等式，但现实中有分红、利率期限结构、随机波动率、跳跃、交易成本和流动性风险；实际对冲需调整模型并控制模型风险，不能把解析公式误当作无条件下成立的市场经验定律。

## 相关条目

- [Black-Scholes 公式](./Black-Scholes公式.md)
- [Itô 引理](../第96级-随机微分方程/Itô引理.md)
- [无套利原理](./无套利原理.md)
- [Feynman-Kac 公式在金融中的应用](./FeynmanKac公式在金融中的应用.md)
