# Pontryagin 极大值原理

## 一、定理介绍

Pontryagin 极大值原理（Pontryagin's Maximum Principle, PMP）给出了最优控制问题中极值轨迹必须满足的一组必要条件。它由 Lev Pontryagin 及其学派于 20 世纪 50 年代提出，是变分法在最优控制领域的推广，能够处理控制受约束、终端状态受约束等复杂情形。

## 二、原理思路

将控制 $u$ 视为待定函数，目标是使性能指标
$$
J=\int_{t_0}^{t_f}L(x,u,t)\,dt+\Phi(x(t_f))
$$
达到极小。引入协态（costate）变量 $\lambda(t)$，构造 Hamilton 函数
$$
H(x,u,\lambda,t)=L(x,u,t)+\lambda^{\mathsf{T}}f(x,u,t).
$$
PMP 指出：最优控制 $u^*(t)$ 必须在每一点使 $H$ 取最大值（对极小化问题），同时状态与协态满足 Hamilton 方程组，并满足相应的边界条件。

## 三、定理的严格表述

考虑受控系统
$$
\dot{x}=f(x,u,t),\qquad x(t_0)=x_0,
$$
其中 $x\in\mathbb{R}^n$，$u(t)\in U\subset\mathbb{R}^m$，$U$ 为容许控制集。性能指标为
$$
J(u)=\Phi(x(t_f))+\int_{t_0}^{t_f}L(x(t),u(t),t)\,dt.
$$
定义 Hamilton 函数
$$
H(x,u,\lambda,t)=L(x,u,t)+\lambda^{\mathsf{T}}f(x,u,t).
$$

**Pontryagin 极大值原理**：若 $u^*(t)$ 为最优控制，$x^*(t)$ 为对应最优状态轨迹，则存在非零的协态向量 $\lambda(t)$ 与常数 $\lambda_0\le 0$，使得

1. **状态方程**：
$$
\dot{x}^*(t)=\frac{\partial H}{\partial \lambda}(x^*,u^*,\lambda,t)=f(x^*,u^*,t).
$$

2. **协态方程**：
$$
\dot{\lambda}(t)=-\frac{\partial H}{\partial x}(x^*,u^*,\lambda,t).
$$

3. **极大值条件**：对几乎所有 $t\in[t_0,t_f]$，
$$
H(x^*(t),u^*(t),\lambda(t),t)=\max_{u\in U}H(x^*(t),u,\lambda(t),t).
$$

4. **横截条件**：若终端时间 $t_f$ 与终端状态 $x(t_f)$ 自由，则
$$
\lambda(t_f)=\lambda_0\frac{\partial \Phi}{\partial x}(x^*(t_f)),\qquad H(t_f)=0.
$$

通常取正规情形 $\lambda_0=-1$。

## 四、证明过程

PMP 的证明核心在于对控制变分引起的性能指标变化进行一阶分析。简述如下：

1. **针状变分（Needle Variation）**：在最优控制 $u^*$ 上施加一个小区间 $[\tau,\tau+\varepsilon]$ 内的扰动 $v\in U$，得到新控制 $u_\varepsilon$。

2. **状态扰动传播**：该扰动在 $t>\tau$ 处引起的状态偏差 $\delta x(t)$ 满足线性变分方程
$$
\delta\dot{x}=\frac{\partial f}{\partial x}(x^*,u^*,t)\delta x+\bigl[f(x^*,v,t)-f(x^*,u^*,t)\bigr]\mathbf{1}_{[\tau,\tau+\varepsilon]}(t).
$$

3. **引入协态消去状态变分**：取 $\lambda$ 满足协态方程，并令 $\lambda(t_f)=-\frac{\partial\Phi}{\partial x}(x^*(t_f))$（正规情形）。由分部积分可得性能指标一阶增量
$$
\delta J\approx \varepsilon\bigl[H(x^*(\tau),v,\lambda(\tau),\tau)-H(x^*(\tau),u^*(\tau),\lambda(\tau),\tau)\bigr].
$$

4. **最优性必要条件**：因 $u^*$ 最优，必须有 $\delta J\le 0$ 对所有 $v\in U$ 成立，于是得到极大值条件。横截条件与自由终端时间的条件由终端变分导出。

严格证明需要测度论、Brouwer 不动点定理或凸分析等工具，处理控制集非凸、状态约束等推广形式。

## 五、应用与意义

- **航天与轨迹优化**：最小时间、最小燃料的轨道转移问题常由 PMP 导出 Bang-Bang 或奇异控制结构。
- **经济学与管理科学**：最优消费、投资与库存问题可利用 PMP 获得刻画最优策略的微分方程组。
- **机器人与自动驾驶**：动态避障、能量最优路径规划中的必要条件常基于 PMP。
- **理论地位**：PMP 是最优控制理论的里程碑，将古典变分法推广到控制受闭集约束的情形，并为数值方法（如打靶法、同伦法）提供了一阶最优性系统。
