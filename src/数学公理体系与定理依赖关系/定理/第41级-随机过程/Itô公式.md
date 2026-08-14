# Itô 公式

## 介绍

Itô 公式（Itô's lemma）是随机分析中最核心的定理，由伊藤清在 1944 年提出。它是随机微积分中的链式法则，给出了具有 Brown 运动的随机过程的光滑函数展开式。与经典微积分不同，由于 Brown 运动的二次变差非零，Itô 公式包含一个额外的二阶修正项。Itô 公式是随机微分方程（SDE）理论、数理金融（如 Black–Scholes 公式）和随机控制理论的基石。

## 分析

**前置依赖**：Brown 运动、Itô 积分、二次变差、鞅、Taylor 展开。

**定理内容**：设 $f(t,x)$ 是 $C^{1,2}$ 函数（即 $f$ 对 $t$ 一阶连续可微，对 $x$ 二阶连续可微），$X_t$ 是 Itô 过程：
$$dX_t = \mu_t dt + \sigma_t dB_t$$
则 $Y_t = f(t, X_t)$ 也是 Itô 过程，且
$$dY_t = \left(\frac{\partial f}{\partial t} + \mu_t \frac{\partial f}{\partial x} + \frac{1}{2}\sigma_t^2 \frac{\partial^2 f}{\partial x^2}\right) dt + \sigma_t \frac{\partial f}{\partial x} dB_t$$

**多维形式**：设 $f(t, x_1, \dots, x_n)$ 是 $C^{1,2}$ 函数，$X_t^i$ 是 Itô 过程：
$$dX_t^i = \mu_t^i dt + \sum_{j=1}^m \sigma_t^{ij} dB_t^j$$
则
$$df(t, X_t) = \frac{\partial f}{\partial t} dt + \sum_{i=1}^n \frac{\partial f}{\partial x_i} dX_t^i + \frac{1}{2} \sum_{i,j=1}^n \frac{\partial^2 f}{\partial x_i \partial x_j} d[X^i, X^j]_t$$

**数学内涵**：Itô 公式中的额外项 $\frac{1}{2}\sigma_t^2 \frac{\partial^2 f}{\partial x^2} dt$ 来源于 Brown 运动的二次变差性质 $[B,B]_t = t$。在经典微积分中，$dB_t$ 是 $O(\sqrt{dt})$ 量级，而 $(dB_t)^2$ 是 $O(dt)$ 量级，不能忽略。

**证明策略**：对 $f(t,x)$ 进行 Taylor 展开到二阶，代入 $X_t$ 的增量，利用 Brown 运动的二次变差性质，取极限得到 Itô 公式。

## 思考过程

Itô 公式与经典链式法则的关键区别在于二阶项。回顾 Taylor 展开：
$$f(t+dt, x+dx) - f(t,x) = \frac{\partial f}{\partial t} dt + \frac{\partial f}{\partial x} dx + \frac{1}{2} \frac{\partial^2 f}{\partial x^2} (dx)^2 + \cdots$$

在经典微积分中，$(dx)^2$ 是 $O(dt^2)$ 量级，可忽略。但对于 Itô 过程 $dX_t = \mu dt + \sigma dB_t$，$(dX_t)^2 = \sigma^2 (dB_t)^2 + 2\mu\sigma dt dB_t + \mu^2 (dt)^2$。由于 $(dB_t)^2$ 的期望是 $dt$，且当 $dt \to 0$ 时 $(dB_t)^2 \to dt$（在 $L^2$ 意义下），故 $(dX_t)^2 = \sigma^2 dt + o(dt)$，不能忽略。

## 证明过程

**定理**（一维 Itô 公式）：设 $f \in C^{1,2}(\mathbb{R}_+ \times \mathbb{R})$，$X_t$ 满足 $dX_t = \mu_t dt + \sigma_t dB_t$，则
$$f(t, X_t) = f(0, X_0) + \int_0^t \left(\frac{\partial f}{\partial s} + \mu_s \frac{\partial f}{\partial x} + \frac{1}{2}\sigma_s^2 \frac{\partial^2 f}{\partial x^2}\right) ds + \int_0^t \sigma_s \frac{\partial f}{\partial x} dB_s$$

**证明**：

**步骤 1**：分划。取 $[0,t]$ 的分划 $0 = t_0 < t_1 < \cdots < t_n = t$，$\Delta t_i = t_{i+1} - t_i$，$\Delta X_i = X_{t_{i+1}} - X_{t_i}$。

**步骤 2**：Taylor 展开。
$$f(t, X_t) - f(0, X_0) = \sum_{i=0}^{n-1} [f(t_{i+1}, X_{t_{i+1}}) - f(t_i, X_{t_i})]$$
$$= \sum_i \left[\frac{\partial f}{\partial t} \Delta t_i + \frac{\partial f}{\partial x} \Delta X_i + \frac{1}{2} \frac{\partial^2 f}{\partial x^2} (\Delta X_i)^2 + R_i\right]$$
其中 $R_i$ 是高阶余项。

**步骤 3**：取极限 $n \to \infty$，$\max \Delta t_i \to 0$。
- $\sum \frac{\partial f}{\partial t} \Delta t_i \to \int_0^t \frac{\partial f}{\partial s} \, ds$。
- $\sum \frac{\partial f}{\partial x} \Delta X_i \to \int_0^t \frac{\partial f}{\partial x} dX_s = \int_0^t \frac{\partial f}{\partial x} \mu_s \, ds + \int_0^t \frac{\partial f}{\partial x} \sigma_s \, dB_s$。
- $\sum \frac{1}{2} \frac{\partial^2 f}{\partial x^2} (\Delta X_i)^2 \to \frac{1}{2} \int_0^t \frac{\partial^2 f}{\partial x^2} d[X,X]_s = \frac{1}{2} \int_0^t \frac{\partial^2 f}{\partial x^2} \sigma_s^2 \, ds$。
- 余项 $R_i$ 在极限中消失。

**步骤 4**：合并得 Itô 公式。$\square$

**例**（几何 Brown 运动）：设 $S_t = S_0 e^{(\mu - \sigma^2/2)t + \sigma B_t}$，则 $dS_t = \mu S_t dt + \sigma S_t dB_t$。反之，若 $dS_t = \mu S_t dt + \sigma S_t dB_t$，则 $S_t = S_0 e^{(\mu - \sigma^2/2)t + \sigma B_t}$。

**证明**：令 $f(t,x) = \ln x$，则 $\frac{\partial f}{\partial t} = 0$，$\frac{\partial f}{\partial x} = 1/x$，$\frac{\partial^2 f}{\partial x^2} = -1/x^2$。由 Itô 公式，
$$d(\ln S_t) = \left(0 + \mu S_t \cdot \frac{1}{S_t} + \frac{1}{2} \sigma^2 S_t^2 \cdot \left(-\frac{1}{S_t^2}\right)\right) dt + \sigma S_t \cdot \frac{1}{S_t} dB_t = \left(\mu - \frac{\sigma^2}{2}\right) dt + \sigma dB_t$$
积分即得。$\square$