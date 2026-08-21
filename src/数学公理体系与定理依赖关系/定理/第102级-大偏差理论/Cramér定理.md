# Cramér定理

> **一句话大白话**：独立同分布样本的均值偏离真实均值时，偏离概率以 $\exp(-nI(x))$ 的指数速率衰减，其中 $I$ 是矩生成函数的 Legendre 变换。
>
> **小例子**：公平硬币抛 $n$ 次，正面率 $\ge3/4$ 的概率约 $e^{-n(3/4\log3-\log2)}$，每多抛一次概率就乘上一个约 $0.877$ 的衰减因子。

## 一、定理介绍

设 $X_1,\dots,X_n$ 为 i.i.d. 随机变量，其矩生成函数 $M(\theta)=\mathbb E[e^{\theta X_1}]$ 在 $\theta=0$ 的某邻域内有限，记对数矩生成函数 $\Lambda(\theta)=\log M(\theta)$。令 $S_n=\sum_iX_i$，$\overline X_n=S_n/n$。则 $\{\overline X_n\}$ 满足速率为 $n$ 的大偏差原理，速率函数为
$$
I(x)=\sup_{\theta\in\mathbb R}\{\theta x-\Lambda(\theta)\},
$$
即 $\Lambda$ 的 Legendre 变换。它给出
$$
\mathbb P(\overline X_n\in B)\approx\exp\big(-n\inf_{x\in B}I(x)\big).
$$

## 二、原理思路

上界用 Chebyshev 型指数（切尔诺夫）不等式：$\mathbb P(S_n\ge na)\le e^{-\theta na}\mathbb E[e^{\theta S_n}]=e^{-n(\theta a-\Lambda(\theta))}$，对 $\theta>0$ 取下确界。下界用指数鞅与 Esscher 测度 $\frac{d\mathbb Q_\theta}{d\mathbb P}=e^{\theta S_n-n\Lambda(\theta)}$ 倾斜，使新测度下均值 $\Lambda'(\theta_a)=a$，配合中心极限定理得到精确的指数下界。

## 三、定理的严格表述

设 $\Lambda(\theta)=\log\mathbb E[e^{\theta X_1}]$ 在 $\theta=0$ 邻域内有限，$I(x)=\sup_\theta\{\theta x-\Lambda(\theta)\}$。则对任意闭集 $C$ 与开集 $U\subset\mathbb R$，
$$
\limsup_{n\to\infty}\frac1n\log\mathbb P(\overline X_n\in C)\le-\inf_{x\in C}I(x),
$$
$$
\liminf_{n\to\infty}\frac1n\log\mathbb P(\overline X_n\in U)\ge-\inf_{x\in U}I(x).
$$
即 $\{\overline X_n\}$ 满足速率 $n$ 的 LDP。

## 四、证明过程

**步骤1：上界。** 对 $\theta>0$，$\mathbb P(\overline X_n\ge a)\le e^{-n(\theta a-\Lambda(\theta))}$，得 $\limsup\frac1n\log\mathbb P(\overline X_n\ge a)\le-\sup_{\theta>0}\{\theta a-\Lambda(\theta)\}$；$\theta<0$ 一侧同理。

**步骤2：下界（指数鞅）。** 设 $\Lambda'(\theta_a)=a$，定义 Esscher 测度 $\frac{d\mathbb Q_{\theta_a}}{d\mathbb P}=e^{\theta_aS_n-n\Lambda(\theta_a)}$。则
$$
\mathbb P(\overline X_n\in(a,a+\delta))=\mathbb E_{\mathbb Q_{\theta_a}}\left[e^{-n(\theta_a\overline X_n-\Lambda(\theta_a))}\mathbf1_{\{\overline X_n\in(a,a+\delta)\}}\right]\gtrsim e^{-n(\theta_aa-\Lambda(\theta_a))}\,\mathbb Q_{\theta_a}(\overline X_n\in(a,a+\delta)).
$$
在 $\mathbb Q_{\theta_a}$ 下 $\overline X_n$ 方差 $\approx\Lambda''(\theta_a)/n$，由中心极限定理 $\mathbb Q_{\theta_a}(\overline X_n\in(a,a+\delta))\approx\delta\sqrt{n}/\sqrt{2\pi\Lambda''(\theta_a)}$，故
$$
\liminf_n\frac1n\log\mathbb P(\overline X_n\in(a,a+\delta))\ge-\theta_aa+\Lambda(\theta_a)=-I(a).
$$

**步骤3：Legendre 变换性质。** $I$ 是凸函数、下界半连续，$\inf I=0$ 且 $I(\mathbb E[X_1])=0$。

**步骤4：合成。** 对闭集用紧集逼近与有限覆盖，对开集用小区间覆盖与下界，得到 LDP 上下界。$\square$

## 五、应用与意义

Cramér 定理是大偏差理论的基石，给出了稀有事件概率（如误差超大概率、极端失败概率）的指数精确刻画。它支撑 Chernoff 界、Sanov 定理、假设检验的错误指数分析与金融极端损失估计，并作为 Gärtner-Ellis、近似计算等推广的起点。