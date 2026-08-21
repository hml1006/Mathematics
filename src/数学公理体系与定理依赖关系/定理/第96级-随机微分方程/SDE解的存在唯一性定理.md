# SDE 解的存在唯一性定理

> **一句话大白话**：只要随机微分方程的漂移和扩散项"够温和"（不剧烈变化、不会猛增），并且从有界的起点出发，那么它的强解就一定存在且唯一。
>
> **小例子**：描述股票价格的 SDE，只要漂移与波动率函数连续有界，市场模型就有且只有一条轨道描述价格演化。

## 一、定理介绍

> **前置依赖**：随机微分方程与 Itô 积分、Lipschitz 与线性增长条件、Picard 迭代、Itô 等距、Gronwall 引理、Chebyshev 不等式与 Borel-Cantelli 引理

考虑 SDE $dX_t = \mu(t,X_t)dt + \sigma(t,X_t)dW_t$，$X_0=\xi$。在 Lipschitz 条件、线性增长条件与 $\mathbb{E}\|\xi\|^2<\infty$ 下，存在唯一的强解 $X_t$，且 $\mathbb{E}[\sup_{0\le t\le T}\|X_t\|^2]<\infty$。

## 二、原理思路

采用 Picard 迭代（同常微分方程）并利用 Itô 等距与 Gronwall 引理。先证迭代序列的 $L^2$ 范数一致有界（线性增长条件），再证其差分方差被控制（Lipschitz 条件），进而得到平方收敛与几乎必然一致收敛，极限即为解；唯一性由两条解的差满足的 Gronwall 不等式推出。

## 三、定理的严格表述

设存在常数 $K>0$ 使对所有 $t\in[0,T]$、$x,y$ 有

$$
\|\mu(t,x)-\mu(t,y)\| + \|\sigma(t,x)-\sigma(t,y)\| \le K\|x-y\|,
$$

$$
\|\mu(t,x)\| + \|\sigma(t,x)\| \le K(1+\|x\|),
$$

且 $\xi$ 与 $W$ 独立、$\mathbb{E}\|\xi\|^2<\infty$。则存在唯一强解 $X_t$ 满足 $\mathbb{E}\big[\sup_{0\le t\le T}\|X_t\|^2\big]<\infty$。

## 四、证明过程

1. **Picard 迭代**：$X_t^{(0)}=\xi$，$X_t^{(n+1)}=\xi+\int_0^t\mu(s,X_s^{(n)})ds+\int_0^t\sigma(s,X_s^{(n)})dW_s$。
2. **Itô 等距**：$\mathbb{E}\big[\big(\int_0^t f_sdW_s\big)^2\big]=\mathbb{E}\int_0^t f_s^2ds$。
3. **一致有界**：由线性增长条件与 Gronwall 引理，$\sup_t\mathbb{E}\|X_t^{(n)}\|^2\le C$。
4. **收敛性**：$\mathbb{E}\|X_{t}^{(n+1)}-X_t^{(n)}\|^2\le\frac{(2K^2(T+1)t)^n}{n!}D_0$，由 Chebyshev-Borel-Cantelli 得一致收敛。
5. **极限与唯一**：取极限为解；两解的差由 Gronwall 得 $\mathbb{E}\|\Delta_t\|^2=0$。

## 五、应用与意义

该定理为随机微分方程理论奠定了基础，保证在较温和条件下 SDE 有定义良好的强解，使资产定价、物理系统、扩散模型、随机滤波等应用中的 SDE 建模具有数学严谨性。Lipschitz 与线性增长条件也揭示了当扩散系数"病态"（如平方根、不光滑）时需引入弱解、存在性门槛更精细的议题。