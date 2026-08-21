# Pontryagin极大值原理

> **一句话大白话**：找最优控制就像“在所有可行操控里选一个让哈密尔顿量最大”的：最优控制总能让 Hamiltonian 取到最大。
>
> **小例子**：开车想用最少油到达某点，Pontryagin 原理说在每一刻都选“使哈密尔顿函数最大”的油门与方向，整体就是最优路径。

## 一、定理介绍

Pontryagin 极大值原理给出最优控制的必要条件。它用 Hamiltonian
$$
\mathcal H(\boldsymbol x,\boldsymbol u,\boldsymbol\lambda,t)=L(\boldsymbol x,\boldsymbol u)+\boldsymbol\lambda^{\top}\boldsymbol f(\boldsymbol x,\boldsymbol u)
$$
描述，断言最优控制满足 $\mathcal H(\boldsymbol x^*,\boldsymbol u^*,\boldsymbol\lambda^*,t)=\max_{\boldsymbol u}\mathcal H(\boldsymbol x^*,\boldsymbol u,\boldsymbol\lambda^*,t)$，连同状态-协态方程构成两点边值问题。

## 二、原理思路

对控制器施加“变分”扰动，考察其对最优点的影响。由于极值点的一阶变分为零，沿可行扰动方向推出协态方程与顶点条件；再由控制可以自由扰动，得到 Hamiltonian 对控制的最大化条件。

## 三、定理的严格表述

设动态 $\dot{\boldsymbol x}=\boldsymbol f(\boldsymbol x,\boldsymbol u)$，性能指标 $J=\int_{t_0}^{t_f}L(\boldsymbol x,\boldsymbol u)\,dt$，定义协态 $\boldsymbol\lambda$ 满足
$$
\dot{\boldsymbol\lambda}=-\frac{\partial\mathcal H}{\partial\boldsymbol x}.
$$
则最优控制 $\boldsymbol u^*$ 满足极大值条件
$$
\mathcal H(\boldsymbol x^*,\boldsymbol u^*,\boldsymbol\lambda^*,t)=\max_{\boldsymbol u\in U}\mathcal H(\boldsymbol x^*,\boldsymbol u,\boldsymbol\lambda^*,t),
$$
且边界满足横截条件（自由端点时 $\boldsymbol\lambda(t_f)=0$ 等）。

## 四、证明过程

1. **构造 Hamiltonian**。$\mathcal H=L+\boldsymbol\lambda^{\top}\boldsymbol f$，把约束 $\dot{\boldsymbol x}=\boldsymbol f$ 引入指标。
2. **变分**。对控制摄动 $u^*+\varepsilon v$ 求指标一阶变化，极值点要求其一阶变分为零。
3. **协态方程**。由分部积分与任意性得到 $\dot{\boldsymbol\lambda}=-\partial\mathcal H/\partial\boldsymbol x$。
4. **极大值条件**。由控制可任意摄动且其系数为负，最优解要求 $\boldsymbol u^*$ 使 $\mathcal H$ 最大（对应“对每一个可行比较控制不比它差”）。
5. **横截条件**。由自由端点边界条件得出 $\boldsymbol\lambda$ 在端点处的取值条件。

## 五、应用与意义

Pontryagin 原理是火箭、导弹、自动驾驶与能源系统最优控制的基石，能处理 LQR 处理不了的一类带约束或奇异控制问题。它给出精确的必要条件，是 Bang-Bang 控制、奇异弧与最优轨迹分析的标准工具。