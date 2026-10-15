# 代数Riccati方程

> **一句话大白话**：给一个线性系统和一个"偏离代价 + 能量代价"的二次指标，最优反馈增益是由一个二次矩阵方程解出来的：这个方程就叫代数 Riccati 方程，它有唯一的半正定解，且使闭环稳定。
>
> **小例子**：倒立摆的 LQR 控制器中，期望状态代价 $\boldsymbol Q$ 与输入代价 $\boldsymbol R$ 一旦给定，控制器参数就由 $\boldsymbol A^{\top}\boldsymbol P+\boldsymbol P\boldsymbol A-\boldsymbol P\boldsymbol B\boldsymbol R^{-1}\boldsymbol B^{\top}\boldsymbol P+\boldsymbol Q=\boldsymbol 0$ 唯一确定。

## 一、定理介绍

> **前置依赖**：LQR的最优反馈、Lyapunov稳定性定理、可控性的Kalman秩条件、线性时不变系统的状态响应公式

对线性时不变系统 $\dot{\boldsymbol x}=\boldsymbol A\boldsymbol x+\boldsymbol B\boldsymbol u$ 与无限时域二次指标，**代数 Riccati 方程**（ARE）为

$$
\boldsymbol A^{\top}\boldsymbol P+\boldsymbol P\boldsymbol A-\boldsymbol P\boldsymbol B\boldsymbol R^{-1}\boldsymbol B^{\top}\boldsymbol P+\boldsymbol Q=\boldsymbol 0 ,
$$

其中 $\boldsymbol Q=\boldsymbol Q^{\top}\ge\boldsymbol 0$、$\boldsymbol R=\boldsymbol R^{\top}>\boldsymbol 0$。满足该方程且使闭环矩阵 $\boldsymbol A-\boldsymbol B\boldsymbol R^{-1}\boldsymbol B^{\top}\boldsymbol P$ 为 Hurwitz（特征值实部全负）的解称为**稳定化解**，它正是 LQR 最优反馈增益 $\boldsymbol K=\boldsymbol R^{-1}\boldsymbol B^{\top}\boldsymbol P$ 的来源。

本条目补足 LQR 定理中"存在唯一稳定化解"这一关键前提：给出解的 Lyapunov 积分表示、稳定性验证与**唯一性**的严格证明。唯一性依赖一个代数事实——两个 Hurwitz 矩阵的 Sylvester 方程只有零解。

## 二、原理思路

1. **稳定化解满足 Lyapunov 方程**：设 $\boldsymbol P$ 满足 ARE 且 $\boldsymbol A_{\boldsymbol K}=\boldsymbol A-\boldsymbol B\boldsymbol K$ 稳定（$\boldsymbol K=\boldsymbol R^{-1}\boldsymbol B^{\top}\boldsymbol P$），把 ARE 改写成 $\boldsymbol A_{\boldsymbol K}^{\top}\boldsymbol P+\boldsymbol P\boldsymbol A_{\boldsymbol K}=-(\boldsymbol Q+\boldsymbol K^{\top}\boldsymbol R\boldsymbol K)$。
2. **积分表示**：$\boldsymbol A_{\boldsymbol K}$ 稳定使下式收敛，给出解的显式表达，从而 $\boldsymbol P\ge\boldsymbol 0$。
3. **唯一性**：两个解之差满足一个齐次 Sylvester 方程；由两个矩阵都稳定，该方程只有零解。

## 三、定理的严格表述

**（代数 Riccati 方程）** 设 $\boldsymbol A\in\mathbb R^{n\times n}$、$\boldsymbol B\in\mathbb R^{n\times m}$、$\boldsymbol Q=\boldsymbol Q^{\top}\in\mathbb R^{n\times n}$（$\boldsymbol Q\ge\boldsymbol 0$）、$\boldsymbol R=\boldsymbol R^{\top}\in\mathbb R^{m\times m}$（$\boldsymbol R>\boldsymbol 0$），记 $\boldsymbol S=\boldsymbol B\boldsymbol R^{-1}\boldsymbol B^{\top}$。假设 $(\boldsymbol A,\boldsymbol B)$ 可稳定且 $(\boldsymbol A,\boldsymbol Q^{1/2})$ 可检测。则 ARE 存在**唯一**的对称半正定解 $\boldsymbol P$，且

$$
\boldsymbol A_{\boldsymbol K}:=\boldsymbol A-\boldsymbol B\boldsymbol R^{-1}\boldsymbol B^{\top}\boldsymbol P=\boldsymbol A-\boldsymbol S\boldsymbol P
$$

为 Hurwitz 矩阵。

**（唯一性命题）** 若 $\boldsymbol P_1,\boldsymbol P_2$ 都是 ARE 的对称解，且 $\boldsymbol A-\boldsymbol S\boldsymbol P_1$、$\boldsymbol A-\boldsymbol S\boldsymbol P_2$ 均为 Hurwitz，则 $\boldsymbol P_1=\boldsymbol P_2$。

## 四、证明过程

**步骤 1：稳定化解满足 Lyapunov 方程**

设 $\boldsymbol P=\boldsymbol P^{\top}$ 满足 ARE，$\boldsymbol K=\boldsymbol R^{-1}\boldsymbol B^{\top}\boldsymbol P$，则 $\boldsymbol B^{\top}\boldsymbol P=\boldsymbol R\boldsymbol K$、$\boldsymbol P\boldsymbol B=\boldsymbol K^{\top}\boldsymbol R$、$\boldsymbol B\boldsymbol R^{-1}\boldsymbol B^{\top}\boldsymbol P=\boldsymbol B\boldsymbol K$。计算

$$
\boldsymbol A_{\boldsymbol K}^{\top}\boldsymbol P+\boldsymbol P\boldsymbol A_{\boldsymbol K}
=(\boldsymbol A-\boldsymbol B\boldsymbol K)^{\top}\boldsymbol P+\boldsymbol P(\boldsymbol A-\boldsymbol B\boldsymbol K)
=\boldsymbol A^{\top}\boldsymbol P+\boldsymbol P\boldsymbol A-2\boldsymbol K^{\top}\boldsymbol R\boldsymbol K .
$$

由 ARE，$\boldsymbol A^{\top}\boldsymbol P+\boldsymbol P\boldsymbol A=-\boldsymbol Q+\boldsymbol P\boldsymbol B\boldsymbol R^{-1}\boldsymbol B^{\top}\boldsymbol P=-\boldsymbol Q+\boldsymbol K^{\top}\boldsymbol R\boldsymbol K$。故

$$
\boldsymbol A_{\boldsymbol K}^{\top}\boldsymbol P+\boldsymbol P\boldsymbol A_{\boldsymbol K}
=-\big(\boldsymbol Q+\boldsymbol K^{\top}\boldsymbol R\boldsymbol K\big)\le\boldsymbol 0 . \tag{1}
$$

（1）正是以 $\boldsymbol Q+\boldsymbol K^{\top}\boldsymbol R\boldsymbol K\ge\boldsymbol 0$ 为"耗散项"的 Lyapunov 方程；由 Lyapunov稳定性定理，$\boldsymbol A_{\boldsymbol K}$ 稳定与（1）相容。$\square$

**步骤 2：解的积分表示与半正定性**

设 $\boldsymbol A_{\boldsymbol K}$ 为 Hurwitz，则由（1）得近似解为 Lyapunov 积分

$$
\boldsymbol P=\int_0^{\infty}e^{\boldsymbol A_{\boldsymbol K}^{\top}t}\big(\boldsymbol Q+\boldsymbol K^{\top}\boldsymbol R\boldsymbol K\big)e^{\boldsymbol A_{\boldsymbol K}t}\,dt . \tag{2}
$$

因 $\boldsymbol A_{\boldsymbol K}$ 的特征值实部全负，$e^{\boldsymbol A_{\boldsymbol K}t}$ 指数衰减，积分绝对收敛。$(\boldsymbol Q+\boldsymbol K^{\top}\boldsymbol R\boldsymbol K)$ 对称半正定，故被积函数对称半正定，$\boldsymbol P=\boldsymbol P^{\top}\ge\boldsymbol 0$。直接求导可验证（2）满足（1）：对 $t\mapsto e^{\boldsymbol A_{\boldsymbol K}^{\top}t}\boldsymbol M e^{\boldsymbol A_{\boldsymbol K}t}$（$\boldsymbol M=\boldsymbol Q+\boldsymbol K^{\top}\boldsymbol R\boldsymbol K$）求导并积分 $\int_0^\infty\frac{d}{dt}(\cdot)dt=-\boldsymbol M$，即得（1）。$\square$

**步骤 3：正定性**

若 $\boldsymbol Q>\boldsymbol 0$，则在（2）中被积函数非负且 $t=0$ 时为 $\boldsymbol M\ge\boldsymbol Q>\boldsymbol 0$，由连续性存在 $\delta>0$ 使对 $t\in[0,\delta]$ 有 $\boldsymbol M(t):=e^{\boldsymbol A_{\boldsymbol K}^{\top}t}\boldsymbol M e^{\boldsymbol A_{\boldsymbol K}t}\ge\frac12\boldsymbol Q>\boldsymbol 0$。于是对任意 $\boldsymbol x\ne\boldsymbol 0$，

$$
\boldsymbol x^{\top}\boldsymbol P\boldsymbol x=\int_0^{\delta}\boldsymbol x^{\top}\boldsymbol M(t)\boldsymbol x\,dt+\int_\delta^\infty\boldsymbol x^{\top}\boldsymbol M(t)\boldsymbol x\,dt
\ge\frac{\delta}{2}\boldsymbol x^{\top}\boldsymbol Q\boldsymbol x>0 ,
$$

故 $\boldsymbol P>\boldsymbol 0$。更一般地，若 $(\boldsymbol A,\boldsymbol Q^{1/2})$ 可检测，则（2）的核为零，同样得 $\boldsymbol P>\boldsymbol 0$。$\square$

**步骤 4：唯一性（Sylvester 论证）**

设 $\boldsymbol P_1,\boldsymbol P_2$ 为 ARE 的两个对称解，且 $\boldsymbol A_i:=\boldsymbol A-\boldsymbol S\boldsymbol P_i$（$i=1,2$）均 Hurwitz。记 $\boldsymbol W=\boldsymbol P_1-\boldsymbol P_2$。两式相减：

$$
\boldsymbol A^{\top}\boldsymbol W+\boldsymbol W\boldsymbol A-\big(\boldsymbol P_1\boldsymbol S\boldsymbol P_1-\boldsymbol P_2\boldsymbol S\boldsymbol P_2\big)=\boldsymbol 0 .
$$

注意 $\boldsymbol P_1\boldsymbol S\boldsymbol P_1-\boldsymbol P_2\boldsymbol S\boldsymbol P_2=\boldsymbol P_1\boldsymbol S(\boldsymbol P_1-\boldsymbol P_2)+(\boldsymbol P_1-\boldsymbol P_2)\boldsymbol S\boldsymbol P_2=\boldsymbol P_1\boldsymbol S\boldsymbol W+\boldsymbol W\boldsymbol S\boldsymbol P_2$。代入并用 $\boldsymbol A_i=\boldsymbol A-\boldsymbol S\boldsymbol P_i$：

$$
(\boldsymbol A-\boldsymbol S\boldsymbol P_1)^{\top}\boldsymbol W+\boldsymbol W(\boldsymbol A-\boldsymbol S\boldsymbol P_2)=\boldsymbol 0,
\qquad\text{即}\qquad
\boldsymbol A_1^{\top}\boldsymbol W+\boldsymbol W\boldsymbol A_2=\boldsymbol 0 . \tag{3}
$$

这是关于 $\boldsymbol W$ 的齐次 Sylvester 方程。定义线性算子 $\mathcal T(\boldsymbol X)=\boldsymbol A_1^{\top}\boldsymbol X+\boldsymbol X\boldsymbol A_2$。若 $\boldsymbol A_1^{\top}$ 的特征值为 $\lambda_1,\dots,\lambda_n$、$\boldsymbol A_2$ 的特征值为 $\mu_1,\dots,\mu_n$，则 $\mathcal T$ 的特征值为全体 $\lambda_i+\mu_j$。因 $\boldsymbol A_1,\boldsymbol A_2$ 均 Hurwitz，有 $\mathrm{Re}\,\lambda_i<0$ 且 $\mathrm{Re}\,\mu_j<0$，故 $\mathrm{Re}(\lambda_i+\mu_j)<0$，特别地 $\lambda_i+\mu_j\ne0$。因此 $\mathcal T$ 可逆，（3）只给出 $\boldsymbol W=\boldsymbol 0$，即 $\boldsymbol P_1=\boldsymbol P_2$。$\blacksquare$

**步骤 5：与最优控制的一致性**

由 LQR的最优反馈，值函数 $V(\boldsymbol x)=\boldsymbol x^{\top}\boldsymbol P\boldsymbol x$ 中的 $\boldsymbol P$ 满足 ARE 且闭环稳定；由可控性的Kalman秩条件与状态响应公式，闭环轨迹 $\boldsymbol x(t)=e^{\boldsymbol A_{\boldsymbol K}t}\boldsymbol x_0$ 指数衰减，指标值恰为（2）式给出的二次型。因此（2）是有限最优代价，而步骤 4 说明它不依赖构造方式，是 $\boldsymbol P$ 的**唯一**刻画。$\blacksquare$

## 五、应用与意义

**在控制论中的作用**：

1. **LQR 的构造核心**：代数 Riccati 方程给出最优状态反馈增益 $\boldsymbol K=\boldsymbol R^{-1}\boldsymbol B^{\top}\boldsymbol P$，是 LQR 控制器设计的唯一计算步骤，可通过 Schur 方法或迭代法数值求解。
2. **H∞ 控制与 Kalman 滤波**：H∞ 次优控制归结为一个带不定项的 Riccati 方程；Kalman–Bucy 滤波的对偶形式是滤波 Riccati 方程，与 ARE 同型（把 $\boldsymbol A$ 换成 $\boldsymbol A^{\top}$、$\boldsymbol B$ 换成 $\boldsymbol C^{\top}$）。
3. **稳定性与鲁棒性**：稳定化解给出闭环的 Lyapunov 函数 $\boldsymbol x^{\top}\boldsymbol P\boldsymbol x$，并给出增益裕度等鲁棒性指标。

**理论意义**：本条目把"最优控制"问题化为一个代数方程的可解性问题。解的存在性来自 LQR 最优值函数，解的唯一性来自 Hurwitz 矩阵的 Sylvester 方程性质，解的稳定性来自 Lyapunov 理论——三者合起来说明二次最优控制框架是良定的。（2）式还表明稳定化解可写成闭环轨迹上的二次型积分，这是 Riccati 方程"动态规划 $+$ Lyapunov"双重身份的体现。

## 课堂问答

**老师**：ARE 一般是非线性矩阵方程，解可能不唯一，凭什么说 LQR 用的那个解存在且唯一？

**学生**：结论：在 $(\boldsymbol A,\boldsymbol B)$ 可稳定、$(\boldsymbol A,\boldsymbol Q^{1/2})$ 可检测时，ARE 存在唯一对称半正定解，且对应的 $\boldsymbol A_{\boldsymbol K}=\boldsymbol A-\boldsymbol B\boldsymbol R^{-1}\boldsymbol B^{\top}\boldsymbol P$ 是 Hurwitz。存在性由 LQR 最优值函数给出积分表示
$$
\boldsymbol P=\int_0^\infty e^{\boldsymbol A_{\boldsymbol K}^{\top}t}(\boldsymbol Q+\boldsymbol K^{\top}\boldsymbol R\boldsymbol K)e^{\boldsymbol A_{\boldsymbol K}t}\,dt ,
$$
因 $\boldsymbol A_{\boldsymbol K}$ 稳定而绝对收敛，被积函数对称半正定，故 $\boldsymbol P=\boldsymbol P^{\top}\ge\boldsymbol 0$。

**老师（追问）**：唯一性那一步，你究竟用了什么代数事实？

**学生**：两个稳定化解之差 $\boldsymbol W=\boldsymbol P_1-\boldsymbol P_2$ 满足齐次 Sylvester 方程
$$
(\boldsymbol A-\boldsymbol S\boldsymbol P_1)^{\top}\boldsymbol W+\boldsymbol W(\boldsymbol A-\boldsymbol S\boldsymbol P_2)=\boldsymbol 0,\qquad \boldsymbol S=\boldsymbol B\boldsymbol R^{-1}\boldsymbol B^{\top} .
$$
算子 $\mathcal T(\boldsymbol X)=\boldsymbol A_1^{\top}\boldsymbol X+\boldsymbol X\boldsymbol A_2$ 的特征值是 $\lambda_i+\mu_j$；因 $\boldsymbol A_1,\boldsymbol A_2$ 都 Hurwitz，$\mathrm{Re}(\lambda_i+\mu_j)<0$，特别地不为零，故 $\mathcal T$ 可逆，只能 $\boldsymbol W=\boldsymbol 0$。常见误区是以为"半正定解唯一"不靠稳定性——离开两个闭环都稳定这一前提，非稳定化解可以有很多。

**老师（拓展）**：积分表示除了证存在性，还告诉我们在什么意义上 $\boldsymbol P$ 是"最优"的？

**学生**：它表明 $\boldsymbol P$ 恰是把闭环轨迹代入二次指标后的值函数系数，即最小代价为 $\boldsymbol x_0^{\top}\boldsymbol P\boldsymbol x_0$；只要 $\boldsymbol Q>\boldsymbol 0$ 或 $(\boldsymbol A,\boldsymbol Q^{1/2})$ 可检测，该积分核非奇异，$\boldsymbol P>\boldsymbol 0$，它同时充当闭环的 Lyapunov 函数，把"最优"与"稳定"绑在同一个 $\boldsymbol P$ 上。
