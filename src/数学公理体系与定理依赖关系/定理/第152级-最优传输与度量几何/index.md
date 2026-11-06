# 第152级-最优传输与度量几何

> 一句话级别概述：最优传输把「搬土」变成几何：用把一堆质量搬到另一堆的最小代价来定义距离、比较分布，并由此给度量空间装上黎曼式的微积分。

## 级别简介

本级别以 Monge-Kantorovich 问题为主线：先建立最优耦合与对偶，再在二次成本下得到 Brenier 的梯度映射；随后用 Wasserstein 距离把概率测度空间变成度量空间，得到 Kantorovich-Rubinstein 与 Benamou-Brenier 两种等价刻画；最后以 JKO 格式把梯度流写成极小化序列，并用 RCD 条件把黎曼几何的极限纳入度量测度空间。

## 本级别定理

- [Monge 问题与 Kantorovich 松弛](./Monge问题与Kantorovich松弛.md)：Monge 问题求映射 $T$ 使 $\int c(x,T(x))\,\mathrm d\mu$ 最小；Kantorovich 把它松弛为耦合 $\pi\in\Pi(\mu,\nu)$ 上的线性规划，最优值相同。
- [Kantorovich 对偶定理](./Kantorovich对偶定理.md)：$\min_{\pi}\int c\,\mathrm d\pi=\sup_{\varphi\oplus\psi\le c}\left(\int\varphi\,\mathrm d\mu+\int\psi\,\mathrm d\nu\right)$。
- [Brenier 定理](./Brenier定理.md)：二次成本 $c=|x-y|^2$ 下最优耦合唯一且由凸函数梯度给出：$T=\nabla\varphi$，$\nabla\varphi_\#\mu=\nu$。
- [Wasserstein 距离的度量性质](./Wasserstein距离的度量性质.md)：$W_p(\mu,\nu)=\left(\inf_{\pi\in\Pi(\mu,\nu)}\int|x-y|^p\,\mathrm d\pi\right)^{1/p}$ 是度量，且 $W_p(\mu_n,\mu)\to0$ 当且仅当弱收敛且 $p$ 阶矩收敛。
- [Kantorovich-Rubinstein 对偶](./Kantorovich-Rubinstein对偶.md)：$W_1(\mu,\nu)=\sup_{\mathrm{Lip}(f)\le1}\int f\,\mathrm d(\mu-\nu)$。
- [Benamou-Brenier 公式](./Benamou-Brenier公式.md)：$W_2^2(\mu_0,\mu_1)=\inf\left\{\int_0^1\!\!\int|v_t|^2\,\mathrm d\mu_t\,\mathrm dt:\ \partial_t\mu_t+\nabla\!\cdot(v_t\mu_t)=0\right\}$。
- [JKO 格式（Wasserstein 梯度流）](./JKO格式.md)：隐式欧拉 $\mu_{k+1}=\arg\min_\mu\frac{1}{2\tau}W_2^2(\mu,\mu_k)+\mathcal F(\mu)$ 在 $\tau\to0$ 时收敛到 $\mathcal F$ 的 $W_2$ 梯度流，取 $\mathcal F$ 为相对熵即得 Fokker-Planck 方程。
- [RCD 空间与 Gromov-Hausdorff 稳定性](./RCD空间与Gromov-Hausdorff稳定性.md)：曲率维数条件 $\mathrm{RCD}(K,N)$ 在测度 Gromov-Hausdorff 极限下封闭，因而给出"黎曼流形的极限"这一度量测度空间类。

## 前置知识

测度论与弱收敛、凸分析与 Fenchel 对偶、Lipschitz 函数与 Rademacher 定理、Riemann 几何的基本概念。

## 后继用途

为度量测度几何、最优传输驱动的 PDE（Fokker-Planck、聚集-扩散方程）、Wasserstein 统计与生成模型提供统一语言。

## 关键定理速览

- Kantorovich 对偶：最优耦合问题等于一对函数的极大化。
- Brenier 定理：二次成本下最优映射必是凸函数的梯度。
- Wasserstein 距离既度量分布又刻画弱收敛。
- JKO 格式：梯度流 = Wasserstein 空间上的隐式欧拉。
- RCD(K,N) 在 Gromov-Hausdorff 极限下封闭。
