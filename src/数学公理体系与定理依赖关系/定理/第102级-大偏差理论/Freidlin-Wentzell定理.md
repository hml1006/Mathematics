# Freidlin-Wentzell定理

> **一句话大白话**：带小噪声的随机微分方程，其样本路径偏离确定解的概率按"作用泛函" $I(\varphi)$ 的指数衰减，$I$ 越小越可能，最优路径由变分决定。
>
> **小例子**：Ornstein-Uhlenbeck 过程 $dX^\varepsilon=-X^\varepsilon dt+\varepsilon dW$ 在 $T$ 时刻超过 $a$ 的概率约 $e^{-a^2/(2(1-e^{-2T}))/ \varepsilon^2}$。

## 一、定理介绍

> **前置依赖**：Girsanov 变换、Schilder 定理、Itô 随机积分、标准 Brown 运动、Varadhan 引理。

考虑随机微分方程
$$
dX_t^\varepsilon=b(X_t^\varepsilon)\,dt+\varepsilon\,dW_t,\qquad X_0^\varepsilon=x_0,
$$
其中 $b:\mathbb R^d\to\mathbb R^d$ 为 Lipschitz 连续、$W_t$ 为 $d$ 维标准 Brown 运动。当 $\varepsilon\to0$ 时，$\{X_t^\varepsilon:t\in[0,T]\}$ 在 $C[0,T]$ 上满足速率为 $1/\varepsilon^2$ 的 LDP，速率函数为
$$
I(\varphi)=\begin{cases}\frac12\int_0^T|\dot\varphi(t)-b(\varphi(t))|^2\,dt, & \varphi\in H_0^1,\ \varphi(0)=x_0,\\ \infty, & \text{其他}.\end{cases}
$$

## 二、原理思路

通过 Girsanov 变换把小噪声 SDE 问题化归为 Schilder 情形：定义测度 $\mathbb Q_\varepsilon$ 使其下漂移项消失，$X^\varepsilon=x_0+\varepsilon\widetilde W$ 恰为 Schilder 缩放 Brown 运动；再用量度变换的指数权重（经 Varadhan 引理）在路径 $\varphi$ 处修正速率函数，合并后恰好得到 $\frac12\int|\dot\varphi-b(\varphi)|^2$。

## 三、定理的严格表述

设 $b$ 为 Lipschitz 连续，$\varepsilon>0$。则当 $\varepsilon\to0$ 时，$X^\varepsilon$ 满足速率 $1/\varepsilon^2$ 的 LDP，速率函数
$$
I(\varphi)=\frac12\int_0^T|\dot\varphi(t)-b(\varphi(t))|^2\,dt,\qquad \varphi\in H_0^1,\ \varphi(0)=x_0,
$$
否则 $I(\varphi)=\infty$。

## 四、证明过程

**步骤1：Girsanov 变换。** 定义
$$
\frac{d\mathbb Q_\varepsilon}{d\mathbb P}=\exp\left(-\frac1\varepsilon\int_0^T b(X^\varepsilon)\,dW-\frac1{2\varepsilon^2}\int_0^T|b(X^\varepsilon)|^2\,dt\right).
$$
在 $\mathbb Q_\varepsilon$ 下 $dX_t^\varepsilon=\varepsilon d\widetilde W_t$，即 $X^\varepsilon=x_0+\varepsilon\widetilde W$，回到 Schilder 情形。

**步骤2：Schilder 应用。** 在 $\mathbb Q_\varepsilon$ 下 $X^\varepsilon$ 满足速率 $1/\varepsilon^2$ 的 LDP，速率函数 $I_0(\varphi)=\frac12\int_0^T|\dot\varphi|^2dt$（$\varphi(0)=x_0$）。

**步骤3：测度变换修正。** 回到原测度 $\mathbb P$ 时，Girsanov 指数项在路径 $\varphi$ 上的极限贡献（经 Varadhan 引理）
$$
\Delta I(\varphi)=-\frac12\int_0^T|b(\varphi)|^2dt-\int_0^T b(\varphi)\cdot\dot\varphi\,dt.
$$

**步骤4：合并速率函数。**
$$
I(\varphi)=I_0(\varphi)+\Delta I(\varphi)=\frac12\int_0^T|\dot\varphi-b(\varphi)|^2dt.
$$

**步骤5：验证条件。** $I$ 下界半连续、水平集紧致（好速率函数），指数紧性与上下界估计由 Schilder 定理及 Girsanov 变换的有界性给出。$\square$

## 五、应用与意义

Freidlin-Wentzell 理论刻画了小噪声随机系统的稀有跃迁与远离确定轨道的概率，是研究随机微分方程、逃逸问题与 metastability 的核心工具。它支撑随机动力系统中的"最小作用路径"、速率函数的变分计算，以及统计物理、金融与生态模型中噪声诱发转变的定量分析。