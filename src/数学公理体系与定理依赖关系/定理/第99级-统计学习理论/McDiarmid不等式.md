# McDiarmid不等式

> **一句话大白话**：不止是"和"，任何由一组相互独立随机变量决定的函数，只要单个变量改动对函数值的影响有限，那么函数值偏离期望的概率就指数式衰减。

> **小例子**：令 $X_1,\dots,X_n$ 为 $n$ 个独立均匀随机数，$f(X)=\max_i X_i$。改动任一 $X_i$ 对最大值的影响不超过 $1$，故 $c_i=1$；取 $n=100$、$\varepsilon=0.1$，得 $\mathbb{P}(|\max_i X_i-\mathbb{E}\max_i X_i|\ge0.1)\le 2e^{-2\cdot100\cdot0.01}=2e^{-2}\approx0.27$。

## 一、定理介绍

> **前置依赖**：Hoeffding不等式、条件期望的存在唯一性、鞅、鞅差序列、上穿不等式。

McDiarmid 不等式又称有界差分不等式（bounded differences inequality），由英国数学家 Colin McDiarmid 在 1989 年的综述《On the Method of Bounded Differences》中系统提出，是集中不等式理论的一次关键跃迁。Hoeffding 不等式只处理"独立随机变量之和"这一特殊结构，而现实中大量感兴趣的量并不是和，而是独立变量的更复杂函数：随机图的染色数、随机排列的最长递增子序列长度、随机算法的运行时间、网络中的最大负载、统计学习中的经验风险等。这些量之间不再具有可加性，独立性也无法直接传递到函数值上。

McDiarmid 的洞察是：**把"独立性"从目标量转移到自变量上，把"可加性"替换为"灵敏度"**。他引入有界差分条件：改动任意一个自变量（其余保持不变）导致函数值的变化不超过常数 $c_i$。在这条仅关于局部灵敏度的假设下，$f(X)$ 相对其期望的偏差仍然满足与 Hoeffding 完全同形的指数界。这一结果的技术核心是把 $f(X)$ 嵌入 Doob 鞅，用 Hoeffding 引理逐项控制鞅差，从而无需独立性假设于函数值本身。它由此成为组合学、随机图论、随机算法与统计学习理论中"用鞅证明集中"这一整套方法的原型，也是许多泛化界推导的最终落脚点。

## 二、原理思路

1. 把 $f(X)$ 关于自变量的逐个揭示过程写成 Doob 鞅：令 $Z_i=\mathbb{E}[f(X)\mid X_1,\dots,X_i]$，则 $Z_0=\mathbb{E}f(X)$、$Z_n=f(X)$，且 $Z_i$ 是一个鞅。

2. 关键引理：有界差分条件推出每个鞅差 $d_i=Z_i-Z_{i-1}$ 满足 $|d_i|\le c_i$ 几乎必然。做法是把条件期望写成对 $X_i$ 的两个条件值之差，而这两个条件值对应 $X_i$ 取不同值、其余变量完全相同，从而被 $c_i$ 控制。

3. 用 Hoeffding 引理的条件版本得到 $\mathbb{E}[e^{\lambda d_i}\mid X_1,\dots,X_{i-1}]\le e^{\lambda^{2}c_i^{2}/8}$，于是带补偿的指数过程是非负上鞅；再对 $t$ 优化，即得尾界。

## 三、定理的严格表述

### 有界差分条件

设 $X_1,\dots,X_n$ 相互独立，取值分别属于集合 $\mathcal{X}_i$。函数 $f\colon\prod_{i=1}^{n}\mathcal{X}_i\to\mathbb{R}$ 满足有界差分条件，若存在常数 $c_1,\dots,c_n\ge0$，使得对任意 $i$ 与任意仅在第 $i$ 个坐标上不同的两点 $x,x'\in\prod_i\mathcal{X}_i$，都有

$$
\left|f(x)-f(x')\right|\le c_i .
$$

### 有界差分不等式

在上述条件下，对任意 $\varepsilon>0$，

$$
\mathbb{P}\left(f(X)-\mathbb{E}f(X)\ge\varepsilon\right)\le \exp\left(-\frac{2\varepsilon^{2}}{\sum_{i=1}^{n}c_i^{2}}\right),
$$

$$
\mathbb{P}\left(\left|f(X)-\mathbb{E}f(X)\right|\ge\varepsilon\right)\le 2\exp\left(-\frac{2\varepsilon^{2}}{\sum_{i=1}^{n}c_i^{2}}\right).
$$

### 鞅差形式

记 $Z_i=\mathbb{E}[f(X)\mid X_1,\dots,X_i]$、$d_i=Z_i-Z_{i-1}$，则 $|d_i|\le c_i$ 几乎必然，且对任意 $\lambda\in\mathbb{R}$，

$$
\mathbb{E}\left[e^{\lambda d_i}\mid X_1,\dots,X_{i-1}\right]\le \exp\left(\frac{\lambda^{2}c_i^{2}}{8}\right).
$$

## 四、证明过程

**步骤 1（构造 Doob 鞅）。** 定义 $Z_i=\mathbb{E}\left[f(X)\mid X_1,\dots,X_i\right]$，$i=0,1,\dots,n$，其中 $Z_0=\mathbb{E}f(X)$、$Z_n=f(X)$。由条件期望的塔性质，对 $j\le i$ 有

$$
\mathbb{E}\left[Z_{i+1}\mid X_1,\dots,X_j\right]=Z_j,
$$

故 $\{Z_i\}$ 关于自然滤流是鞅，$d_i=Z_i-Z_{i-1}$ 是鞅差，$\mathbb{E}[d_i\mid X_1,\dots,X_{i-1}]=0$。

**步骤 2（鞅差的有界性）。** 记 $X_{1:i}=(X_1,\dots,X_i)$。把 $Z_i$ 写成对 $X_i$ 的条件期望，并把条件期望表示为积分平均：

$$
Z_i(X_{1:i})-Z_{i-1}(X_{1:i-1})=\int_{\mathcal{X}_i}\left[f(X_{1:i-1},t,X_{i+1:n})-Z_{i-1}(X_{1:i-1})\right]dP_i(t),
$$

其中 $X_{i+1:n}$ 在积分号下按条件分布取值。由定义 $Z_{i-1}=\int f(X_{1:i-1},t,X_{i+1:n})\,dP_i(t)\,dP_{i+1:n}$，把上式的被积函数对 $X_{i+1:n}$ 再取一次条件期望不改变积分值。于是被积函数形如 $\mathbb{E}\left[f(X_{1:i-1},t,X_{i+1:n})-f(X_{1:i-1},s,X_{i+1:n})\mid \cdot\right]$，其中 $s,t\in\mathcal{X}_i$ 是两个确定性取值。这两点仅在第 $i$ 个坐标上不同，由有界差分条件知其差的绝对值不超过 $c_i$，故积分绝对值不超过 $c_i$，即

$$
|d_i|\le c_i \quad\text{几乎必然}.
$$

**步骤 3（条件 Hoeffding 引理）。** 由步骤 1 知 $\mathbb{E}[d_i\mid X_1,\dots,X_{i-1}]=0$，由步骤 2 知 $d_i\in[-c_i,c_i]$。把 Hoeffding 引理逐点应用于条件分布（对给定 $X_1,\dots,X_{i-1}$ 的条件期望），得

$$
\mathbb{E}\left[e^{\lambda d_i}\mid X_1,\dots,X_{i-1}\right]\le \exp\left(\frac{\lambda^{2}c_i^{2}}{8}\right).
$$

**步骤 4（指数上鞅与极大不等式）。** 对 $\lambda>0$ 定义

$$
M_k=\exp\left(\lambda\sum_{i=1}^{k}d_i-\frac{\lambda^{2}}{8}\sum_{i=1}^{k}c_i^{2}\right),\qquad k=0,1,\dots,n .
$$

由步骤 3，$\mathbb{E}[M_k\mid X_1,\dots,X_{k-1}]\le M_{k-1}$，故 $\{M_k\}$ 是非负上鞅，且 $\mathbb{E}M_n\le M_0=1$。对非负上鞅使用极大不等式（Ville 不等式），得对任意 $x>0$

$$
\mathbb{P}\left(\max_{0\le k\le n}M_k\ge e^{\lambda x}\right)\le e^{-\lambda x}\,\mathbb{E}M_n\le e^{-\lambda x}.
$$

**步骤 5（取出尾概率并优化 $\lambda$）。** 事件 $\{f(X)-\mathbb{E}f(X)\ge x\}$ 即 $\{\sum_{i=1}^{n}d_i\ge x\}$，它蕴含 $\{M_n\ge e^{\lambda x}\}\subseteq\{\max_k M_k\ge e^{\lambda x}\}$，于是

$$
\mathbb{P}\left(f(X)-\mathbb{E}f(X)\ge x\right)\le \exp\left(-\lambda x+\frac{\lambda^{2}}{8}\sum_{i=1}^{n}c_i^{2}\right).
$$

右端是 $\lambda$ 的二次函数，在 $\lambda=\dfrac{4x}{\sum_i c_i^{2}}$ 处取最小值，代入得

$$
\mathbb{P}\left(f(X)-\mathbb{E}f(X)\ge x\right)\le \exp\left(-\frac{2x^{2}}{\sum_{i=1}^{n}c_i^{2}}\right).
$$

**步骤 6（双侧界）。** 对 $-f$（同样满足有界差分条件）重复上述论证得到相反方向的界，用联合界相加即得双侧不等式。$\square$

## 五、应用与意义

- 统计学习：经验风险作为样本的函数满足有界差分（损失有界时 $c_i=1/n$），由此得到与 Hoeffding 同形的泛化界，且可用于不独立于假设的复杂统计量。
- 随机图与组合学：染色数、独立集大小、最长路径长度等图参数的集中性都可由本不等式直接给出，只须验证单个顶点或边的改动影响有限。
- 随机算法：随机化贪心、随机舍入、负载均衡中最大负载的偏差控制。
- 方法论意义：它展示了"用鞅 + Hoeffding 引理"这一通用机器，后来被推广为自归一化集中不等式、有界差分鞅不等式等更强结果。

## 课堂问答

**老师**：McDiarmid 和 Hoeffding 是同一件事吗？

**学生**：不是，Hoeffding 是它的特例。结论：只要 $f$ 满足有界差分条件 $|f(x)-f(x')|\le c_i$（两点仅第 $i$ 个坐标不同），就有

$$
\mathbb{P}\big(|f(X)-\mathbb{E}f(X)|\ge t\big)\le2\exp\!\left(-\frac{2t^2}{\sum_{i=1}^n c_i^2}\right).
$$

Hoeffding 处理的是可加的 $f=\sum_iX_i$，此时 $c_i=b_i-a_i$，故退化回原式；McDiarmid 把独立性留在自变量上、只对函数提灵敏度要求。

**老师（追问）**：证明主线是什么？

**学生**：用鞅。令 $Z_i=\mathbb{E}[f(X)\mid X_1,\dots,X_i]$，则 $Z_0=\mathbb{E}f(X)$、$Z_n=f(X)$，是 Doob 鞅。有界差分条件推出鞅差 $|d_i|=|Z_i-Z_{i-1}|\le c_i$ 几乎必然；再由条件 Hoeffding 引理得 $\mathbb{E}[e^{\lambda d_i}\mid X_1,\dots,X_{i-1}]\le e^{\lambda^2c_i^2/8}$，于是指数过程 $M_k$ 是非负上鞅，用 Ville 极大不等式取出尾概率，最后对 $\lambda$ 求最小即得。

**老师（拓展）**：举一个"不是和"的例子，说明它为何必需？

**学生**：比如 $f(X)=\max_iX_i$，各 $X_i$ 独立均匀。改动任一 $X_i$ 对最大值的影响不超过 $1$，故 $c_i=1$，直接得 $\mathbb{P}(|\max_iX_i-\mathbb{E}\max_iX_i|\ge t)\le2e^{-2t^2/n}$。误区是以为只有"和"才能集中——像最长递增子序列、随机图染色数、经验风险这些非可加量，都靠有界差分框架处理。

## 相关条目

- [Hoeffding不等式](./Hoeffding不等式.md)：本定理的起点与特例，处理独立随机变量之和。
- [VC维的泛化界](./VC维的泛化界.md)：一致泛化界的经典推导，可与本定理给出的界比较。
- [稳定性与泛化](./稳定性与泛化.md)：用算法的稳定性刻画泛化误差，其证明依赖有界差分型论证。
- [Rademacher复杂度的泛化界](./Rademacher复杂度的泛化界.md)：另一类基于集中不等式的泛化界。
- [上穿不等式](../第41级-随机过程/上穿不等式.md)：非负上鞅极大不等式的离散版本。
- [鞅收敛定理](../第41级-随机过程/鞅收敛定理.md)：鞅论的基础结果，本定理的框架依赖鞅的定义与性质。
- [条件期望的存在唯一性](../第24级-概率论基础/条件期望的存在唯一性.md)：Doob 鞅构造的理论前提。
