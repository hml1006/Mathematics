# Feynman-Kac 公式

> **一句话大白话**：有一类偏微分方程的解，可以通过"沿着随机路径取期望"算出来——把确定性分析与随机游走挂上钩，两条路会给出同一个答案。
>
> **小例子**：期权价格满足的偏微分方程，它的解就是"在随机股票价格未来轨迹上打折求和"的数学期望，这正是 Feynman-Kac 公式。

## 一、定理介绍

Feynman-Kac 公式建立了二阶抛物型偏微分方程与布朗型随机过程的概率表示之间的联系。设 $X_t$ 满足 $dX_t=\mu(t,X_t)dt+\sigma(t,X_t)dW_t$，且 $f$ 满足 Kolmogorov 后向方程及终端条件 $f(T,x)=\Phi(x)$，则

$$
f(t,x) = \mathbb{E}\Big[\int_t^T g(s,X_s)e^{-\int_t^s r(u,X_u)du}ds + \Phi(X_T)e^{-\int_t^T r(u,X_u)du}\;\Big|\;X_t=x\Big].
$$

## 二、原理思路

对折现过程 $Y_t = f(t,X_t)e^{-R_t}$（$R_t=\int_0^t r(s,X_s)ds$）应用 Itô 引理。利用后向方程把 $t$ 相关的漂移项消成 $-g$，于是 $Y$ 的随机微分中随机积分部分是鞅。对 $Y$ 从 $t$ 到 $T$ 积分并取条件期望，随机积分项期望为零，剩下的期望表达式即给解一个概率形式。

## 三、定理的严格表述

设 $f$ 满足后向方程

$$
\frac{\partial f}{\partial t} + \mu\frac{\partial f}{\partial x} + \frac12\sigma^2\frac{\partial^2 f}{\partial x^2} - rf + g = 0,\qquad f(T,x)=\Phi(x),
$$

则概率表示

$$
f(t,x) = \mathbb{E}\Big[\int_t^T g(s,X_s)e^{-\int_t^s r(u,X_u)du}ds + \Phi(X_T)e^{-\int_t^T r(u,X_u)du}\;\Big|\;X_t=x\Big].
$$

## 四、证明过程

1. **定义折现过程**：$Y_t=f(t,X_t)e^{-R_t}$，$Z_t=\int_0^t g e^{-R_s}ds$。
2. **Itô 引理**：$d(Y_t) = e^{-R_t}\big(\partial_t f+\mu\partial_x f+\frac12\sigma^2\partial_{xx}f-rf\big)dt + e^{-R_t}\sigma\partial_x f\,dW_t$。
3. **代入后向方程**：漂移项变为 $-g e^{-R_t}dt$，故 $dY_t=-g e^{-R_t}dt+\text{鞅项}$。
4. **积分取期望**：$f(T,X_T)e^{-R_T}-f(t,x)e^{-R_t}=-\int_t^T ge^{-R_s}ds+\text{鞅}$，取条件期望消去鞅。
5. **整理**：结合终端条件 $\Phi(X_T)$ 即得概率表示。

## 五、应用与意义

Feynman-Kac 公式是金融工程的理论支柱：它把 Black-Scholes 方程的解写成期望，是实现蒙特卡洛定价（对高维欧式期权）的基本工具。它也是随机偏微分方程与调和分析、薛定谔方程的路径积分表述之间的联系，广泛用于定价、状态转换信号、随机最优化与遍历理论。