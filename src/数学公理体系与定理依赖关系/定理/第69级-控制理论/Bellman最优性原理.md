# Bellman 最优性原理

> **一句话大白话**：Bellman最优性原理说：一个最优决策不论进行到哪一步，从该步往后的剩余决策也必须是"从这一状态出发的最优解"——最优路径的每一段都不能拖后腿。
>
> **小例子**：求走迷宫的最短路径，若整条路径最优，那么从途中某格到终点的后半段，也必然是那格到终点的最短路。

## 一、定理介绍

Bellman 最优性原理（Bellman's Principle of Optimality）是动态规划（Dynamic Programming, DP）的理论基石，由 Richard Bellman 于 20 世纪 50 年代提出。它指出：一个最优策略的任意剩余部分，在给定当前状态下，仍然是相应子问题的最优策略。该原理将多阶段决策问题分解为一系列单阶段优化问题，从而导出最优值函数所满足的递推关系或偏微分方程。

## 二、原理思路

考虑从初始状态 $x_0$ 出发，通过选择控制序列 $u_0,u_1,\dots$ 使累计代价最小。若已知从任意状态 $x$ 出发的“最优未来代价”$V(x)$，则在当前状态应选择使“即时代价 + 未来最优代价”最小的控制。这种“未来代价折现”的思想将全局优化问题局部化，形成了 Bellman 方程。

对连续时间系统，当值函数足够光滑时，Bellman 方程退化为 Hamilton–Jacobi–Bellman（HJB）偏微分方程；对离散时间系统，则得到递推形式的动态规划方程。

## 三、定理的严格表述

### 离散时间情形

考虑离散时间受控系统
$$
x_{k+1}=f(x_k,u_k),\qquad u_k\in U,
$$
性能指标
$$
J(x_0,\{u_k\})=\sum_{k=0}^{\infty}\gamma^k r(x_k,u_k),
$$
其中 $\gamma\in(0,1]$ 为折扣因子，$r$ 为单步代价。定义最优值函数
$$
V(x)=\inf_{\{u_k\}}J(x,\{u_k\}).
$$

**Bellman 最优性原理**：若最优值函数 $V$ 存在，则它满足 Bellman 方程
$$
V(x)=\inf_{u\in U}\bigl\{r(x,u)+\gamma V(f(x,u))\bigr\}.
$$
并且，若 $u^*(x)$ 达到上式右端下确界，则 $u^*$ 为最优反馈策略。

### 连续时间情形

考虑连续时间系统
$$
\dot{x}=f(x,u),\qquad u\in U,
$$
性能指标
$$
J(x,u)=\int_0^{\infty}e^{-\rho t}L(x(t),u(t))\,dt,
$$
其中 $\rho\ge 0$。定义值函数
$$
V(x)=\inf_{u(\cdot)}J(x,u).
$$

**Hamilton–Jacobi–Bellman 方程**：若 $V$ 连续可微，则
$$
\rho V(x)=\inf_{u\in U}\bigl\{L(x,u)+\nabla V(x)^{\mathsf{T}}f(x,u)\bigr\}.
$$
定义 Hamilton 函数
$$
H(x,\nabla V)=\inf_{u\in U}\bigl\{L(x,u)+\nabla V^{\mathsf{T}}f(x,u)\bigr\},
$$
则 HJB 方程可写为
$$
\rho V(x)=H(x,\nabla V(x)).
$$

## 四、证明过程

**离散时间情形的证明**：设 $V$ 为最优值函数。对任意初始状态 $x$ 和任意容许控制 $u_0$ 于第一步，剩余子问题从 $x_1=f(x,u_0)$ 开始，其最优代价为 $V(x_1)$。因此总代价满足
$$
J(x,u_0,u_1,\dots)=r(x,u_0)+\gamma J(x_1,u_1,\dots)\ge r(x,u_0)+\gamma V(x_1).
$$
对所有 $u_0$ 取下确界得
$$
V(x)\ge \inf_{u_0\in U}\bigl\{r(x,u_0)+\gamma V(f(x,u_0))\bigr\}.
$$
反之，对任意 $\varepsilon>0$，存在策略使 $J(x_1,\cdot)\le V(x_1)+\varepsilon$，于是
$$
V(x)\le r(x,u_0)+\gamma V(x_1)+\gamma\varepsilon.
$$
令 $\varepsilon\to 0$ 并取下确界，得到反向不等式。故 Bellman 方程成立。

**连续时间情形的证明**：对固定 $x$，考虑在无穷小区间 $[0,\Delta t]$ 内采用常数控制 $u$，之后采用最优策略。则
$$
V(x)\le \int_0^{\Delta t}e^{-\rho s}L(x(s),u)\,ds+e^{-\rho\Delta t}V(x(\Delta t)).
$$
对 $\Delta t$ 作一阶展开并除以 $\Delta t$，令 $\Delta t\to 0^+$，得
$$
0\le L(x,u)-\rho V(x)+\nabla V(x)^{\mathsf{T}}f(x,u).
$$
对 $u$ 取下确界得到 HJB 方程。最优策略达到该下确界。

## 五、应用与意义

- **动态规划算法**：离散 HJB 方程是值迭代、策略迭代与 Q-learning 的理论基础。
- **最优控制**：HJB 方程提供了连续时间最优控制的充分条件，与 Pontryagin 极大值原理互为补充。
- **强化学习**：Bellman 方程是 MDP（马尔可夫决策过程）与强化学习中值函数近似的核心等式。
- **经济学与运筹学**：多期投资、库存、资源分配等问题均可通过 Bellman 原理获得结构化的最优策略。
- **计算复杂性**：虽然原理在理论上优雅，但“维度灾难”使其在状态维数高时难以直接求解，因此催生了各种近似动态规划与神经网络方法。
