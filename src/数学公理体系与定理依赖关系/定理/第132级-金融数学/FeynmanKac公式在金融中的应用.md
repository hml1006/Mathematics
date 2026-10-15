# Feynman-Kac公式在金融中的应用

> **一句话大白话**：把"解偏微分方程算价格"和"求随机路径的平均值"这两件看起来毫不相干的事打通——某个期望值公式正好就是某个偏微分方程的解。
>
> **小例子**：期权的风险中性定价相当于"把未来收益 $f(X_T)$ 折现后的期望"，Feynman-Kac 保证这个期望等于一个抛物型 PDE 的解，于是既能用 PDE 方法算、也能用蒙特卡洛抽路径算，两条路结果一致。

## 一、定理介绍

> **前置依赖**：Ito引理、鞅论、风险中性测度、Black-Scholes型抛物方程、SDE解的存在唯一性定理

Feynman-Kac 公式建立了随机微分方程（SDE）与抛物型偏微分方程（PDE）之间的桥梁：形如
$$
V(x,t)=\mathbb{E}\!\left[e^{-\int_t^T r(X_s,s)\,ds}f(X_T,T)\;\Big|\;X_t=x\right]
$$
的函数正是下列 PDE 的解
$$
\frac{\partial V}{\partial t}+\mu\frac{\partial V}{\partial x}+\frac12\sigma^2\frac{\partial^2 V}{\partial x^2}-rV=0,\qquad V(x,T)=f(x,T),
$$
其中 $dX_t=\mu(X_t,t)dt+\sigma(X_t,t)dW_t$。它是风险中性定价的数学核心。

## 二、原理思路

思路绕"对数鞅"展开。定义贴现目标过程 $M_s=e^{-\int_t^s r\,du}V(X_s,s)$；对其应用 Ito 引理得到漂移项。在适当条件下 $M_s$ 是鞅，鞅要求漂移为零——这正是 PDE 中的被积项。由鞅性质 $V(X_t,t)=\mathbb{E}[M_T^{\text{(贴现)否}}]$ 同时给出期望表述与 PDE 表述，二者天然等价。

## 三、定理的严格表述

设 $X$ 满足 $dX_t=\mu(X_t,t)dt+\sigma(X_t,t)dW_t$，$r,f$ 满足多项式增长等正则条件。若 $V$ 由期望公式定义且足够光滑，则 $V$ 满足抛物型初值问题
$$
V_t+\mu V_x+\tfrac12\sigma^2V_{xx}-rV=0,\qquad V(x,T)=f(x,T).
$$
反之，该 PDE 的满足增长条件的温和解亦由期望公式给出。在 BS 模型（$\mu=rS$，$\sigma=\sigma S$）中化为
$$
V(S,t)=e^{-r(T-t)}\,\mathbb{E}^{\mathbb{Q}}[f(S_T)\mid S_t=S].
$$

## 四、证明过程

**步骤1：建立鞅过程。** 设 $M_s=e^{-\int_t^s r\,du}V(X_s,s)$，$t\le s\le T$，依据风险中性定价假设其为鞅。

**步骤2：应用 Ito 引理。** 计算 $dV=(V_s+\mu V_x+\tfrac12\sigma^2V_{xx})ds+\sigma V_x\,dW_s$，进而
$$
dM_s=e^{-\int_t^s r\,du}\Big[\big(V_s+\mu V_x+\tfrac12\sigma^2V_{xx}-rV\big)ds+\sigma V_x\,dW_s\Big].
$$

**步骤3：鞅条件导出 PDE。** 由鞅所需零漂移得
$$
V_s+\mu V_x+\tfrac12\sigma^2V_{xx}-rV=0,
$$
代入 $s=t$ 即得 Feynman-Kac 中的 PDE。

**步骤4：验证终端条件。** 当 $s=T$ 时 $V(X_T,T)=\mathbb{E}[e^0 f(X_T,T)\mid\mathcal{F}_T]=f(X_T,T)$，故 $V(x,T)=f(x,T)$。

**步骤5：金融应用。** 期权定价（BS 方程与风险中性期望）、信用风险（违约概率的 PDE/蒙特卡洛算法）、利率衍生品（债券价格的 PDE）皆落于此框架。

**结论（$\square$）**：期望公式与 PDE 等价，Ito 引理与鞅方法是桥接二者的引擎。

## 五、应用与意义

Feynman-Kac 公式是风险中性定价的理论支柱，使金融工程师可在"解析解 PDE"与"抽路径蒙特卡洛"间自由切换，并支撑信用违约、利率建模等广泛场景。它对偏微分方程终点算子兼顾"解析"与"数值"两大途径的统一，是金融数学中最常用的连接定理之一。

## 课堂问答

**老师**：期权定价既能解 PDE 又能做蒙特卡洛，二者凭什么等价？

**学生**：结论由 Feynman-Kac 公式保证：$V(x,t)=\mathbb E[e^{-\int_t^T r\,ds}f(X_T)\mid X_t=x]$ 恰是方程 $V_t+\mu V_x+\frac12\sigma^2V_{xx}-rV=0$ 满足 $V(x,T)=f(x,T)$ 的解；桥接引擎是对贴现过程 $M_s=e^{-\int_t^s r\,du}V(X_s,s)$ 用 Ito 引理并令漂移为零。

**老师（追问）**：为什么"令漂移为零"就等于那个 PDE？

**学生**：因为鞅的充要条件是无漂移，而 $dM_s=e^{-\int_t^s r\,du}[(V_s+\mu V_x+\frac12\sigma^2V_{xx}-rV)ds+\sigma V_x dW_s]$，去掉 $dW_s$ 项后令 $ds$ 系数为零，直接读出 Feynman-Kac 的 PDE——它与无套利定价是同一件事的两种写法。

**老师（拓展）**：这个期望表示在什么情况下会失效？

**学生**：当 $r,\mu,\sigma$ 依赖路径或存在跳跃时需推广为跳跃-扩散与更一般的生成元形式，并要求 $V$ 满足多项式增长以保证鞅条件与积分可交换；否则期望与解 PDE 可能不再吻合，需用粘性解或概率解严格化。
