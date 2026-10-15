# Pinelis极大不等式

> **一句话大白话**：对一列有界的鞅差，不只是最后一项的部分和，连整个部分和序列在任意时刻达到过的最大值，都以指数速度远离零，而且界的形式与 Hoeffding 不等式完全一致。

> **小例子**：设 $n=100$ 个独立的伯努利增量取 $\pm1$，即 $c_i=1$。则随机游走在任何时刻的最大值超过 $x=10$ 的概率不超过 $e^{-x^{2}/(2n)}=e^{-0.5}\approx0.61$；而"只是第 $n$ 步超过 $10$"的概率虽然更小，但极大不等式保证了整条路径都不会越界。

## 一、定理介绍

> **前置依赖**：鞅、鞅差序列、Hoeffding不等式、上穿不等式、条件期望的存在唯一性、指数矩方法。

Pinelis 极大不等式由 Iosif Pinelis 在 1994 年发表于《The Annals of Probability》的论文《Optimum bounds for the distributions of martingales in Banach spaces》中建立，是鞅集中不等式理论中的里程碑。在它之前，Hoeffding（1963）处理独立有界随机变量之和，Azuma（1967）把指数界推广到有界鞅差，但给出的都是**终点时刻** $S_n$ 的尾界。大偏差理论与序贯统计中真正需要的是**极大值** $\max_{k\le n}S_k$ 的界：序贯检验、置信序列（confidence sequence）、在线学习的后悔界、随机逼近的收敛分析都必须在任何时刻同时成立，而"对每个 $k$ 分别用终点界再做联合界"会损失一个 $\log n$ 因子，无法得到最优速率。

Pinelis 的贡献有两方面。其一，他证明了极大不等式可以与终点不等式共享同一指数常数，即 $\mathbb{P}(\max_{k\le n}S_k\ge x)\le\exp\left(-\frac{x^{2}}{2\sum_i c_i^{2}}\right)$，不需要额外的 $\log n$ 代价；其二，他把结果推广到 Banach 空间取值的鞅与自归一化（self-normalized）统计量，给出了常数意义下最优（optimal）的界。这一不等式因此成为时间一致（time-uniform）集中不等式的基准，也是 Hoeffding-Azuma 型结果的极大版本，在序贯分析、Bandit 算法与经验过程理论中被大量引用。

## 二、原理思路

1. 核心是把"终点尾概率"升级为"过程极大值的尾概率"。做法不是对每个时刻单独估计，而是构造一个**指数型非负上鞅**：把 Hoeffding 引理所给出的条件矩母函数界累乘，再用补偿项 $\frac{\lambda^{2}}{2}\sum_{i\le k}c_i^{2}$ 抵消累积涨落。

2. 对这一非负上鞅使用 Ville 极大不等式（离散型上鞅的极大不等式），得到"过程最大值超过阈值"的概率界。这一步使得界对全部时刻一致成立，而代价仅是把指数中的 $8$ 换成 $2$。

3. 最后对指数参数 $\lambda$ 求最优，得到 $-\frac{x^{2}}{2\sigma^{2}}$ 形式；对 $|S_k|$ 的两侧各用一次不等式并用联合界合并。

## 三、定理的严格表述

### 设定

设滤流 $\{\mathcal{F}_i\}_{i\ge0}$，$X_i$ 关于 $\mathcal{F}_i$ 可测且为鞅差，即 $\mathbb{E}[X_i\mid\mathcal{F}_{i-1}]=0$ 几乎必然；设存在常数 $c_i\ge0$ 使 $|X_i|\le c_i$ 几乎必然。记

$$
S_k=\sum_{i=1}^{k}X_i,\qquad \sigma^{2}=\sum_{i=1}^{n}c_i^{2},\qquad M_n^{*}=\max_{0\le k\le n}S_k .
$$

### 极大不等式（Hoeffding-Azuma-Pinelis 型）

对任意 $x\ge0$，

$$
\mathbb{P}\left(\max_{0\le k\le n}S_k\ge x\right)\le\exp\left(-\frac{x^{2}}{2\sigma^{2}}\right),
$$

$$
\mathbb{P}\left(\max_{0\le k\le n}\left|S_k\right|\ge x\right)\le2\exp\left(-\frac{x^{2}}{2\sigma^{2}}\right).
$$

### 条件矩母函数界

对任意 $\lambda\in\mathbb{R}$ 与每个 $i$，

$$
\mathbb{E}\left[e^{\lambda X_i}\mid\mathcal{F}_{i-1}\right]\le\exp\left(\frac{\lambda^{2}c_i^{2}}{2}\right).
$$

## 四、证明过程

**步骤 1（条件 Hoeffding 引理）。** 固定 $i$，在事件层面看，$X_i$ 在给定 $\mathcal{F}_{i-1}$ 下满足 $\mathbb{E}[X_i\mid\mathcal{F}_{i-1}]=0$ 且 $X_i\in[-c_i,c_i]$。Hoeffding 引理指出：若随机变量 $Y$ 满足 $\mathbb{E}Y=0$、$a\le Y\le b$，则 $\mathbb{E}[e^{\lambda Y}]\le e^{\lambda^{2}(b-a)^{2}/8}$。取 $a=-c_i$、$b=c_i$，区间长度为 $2c_i$，得

$$
\mathbb{E}\left[e^{\lambda X_i}\mid\mathcal{F}_{i-1}\right]\le\exp\left(\frac{\lambda^{2}(2c_i)^{2}}{8}\right)=\exp\left(\frac{\lambda^{2}c_i^{2}}{2}\right).
$$

**步骤 2（构造指数上鞅）。** 对固定的 $\lambda>0$ 定义

$$
M_k=\exp\left(\lambda S_k-\frac{\lambda^{2}}{2}\sum_{i=1}^{k}c_i^{2}\right),\qquad k=0,1,\dots,n .
$$

则 $M_k$ 关于 $\mathcal{F}_k$ 可测且 $M_k>0$。用步骤 1 与 $S_k=S_{k-1}+X_k$：

$$
\mathbb{E}\left[M_k\mid\mathcal{F}_{k-1}\right]=M_{k-1}\,e^{-\lambda^{2}c_k^{2}/2}\,\mathbb{E}\left[e^{\lambda X_k}\mid\mathcal{F}_{k-1}\right]\le M_{k-1}.
$$

故 $\{M_k\}$ 是非负上鞅，且 $\mathbb{E}M_n\le\mathbb{E}M_0=1$。

**步骤 3（Ville 极大不等式）。** 对非负上鞅 $\{M_k\}$ 与常数 $A>0$，由 Doob 极大不等式（或从首达时刻停机后用 $\mathbb{E}M_{\tau\wedge n}\le\mathbb{E}M_0$）得

$$
\mathbb{P}\left(\max_{0\le k\le n}M_k\ge A\right)\le\frac{\mathbb{E}M_n}{A}\le\frac{1}{A}.
$$

取 $A=e^{\lambda x}$ 即得 $\mathbb{P}\left(\max_{k}M_k\ge e^{\lambda x}\right)\le e^{-\lambda x}$。

**步骤 4（极大值事件的包含关系）。** 若 $\max_{0\le k\le n}S_k\ge x$，设 $k_0$ 为首次达到的时刻，则 $\lambda S_{k_0}\ge\lambda x$，故 $M_{k_0}\ge e^{\lambda x}$（补偿项非负）。因此

$$
\left\{\max_{0\le k\le n}S_k\ge x\right\}\subseteq\left\{\max_{0\le k\le n}M_k\ge e^{\lambda x}\right\}.
$$

**步骤 5（优化 $\lambda$）。** 由步骤 3、4，

$$
\mathbb{P}\left(\max_{0\le k\le n}S_k\ge x\right)\le\exp\left(-\lambda x+\frac{\lambda^{2}\sigma^{2}}{2}\right).
$$

右端指数为 $\lambda$ 的二次式，在 $\lambda=\dfrac{x}{\sigma^{2}}$ 处最小，代入得

$$
\mathbb{P}\left(\max_{0\le k\le n}S_k\ge x\right)\le\exp\left(-\frac{x^{2}}{2\sigma^{2}}\right).
$$

**步骤 6（双侧与常数优化）。** 把上述论证用于 $-X_i$（它仍是满足 $|-X_i|\le c_i$ 的鞅差），得到 $\mathbb{P}\left(\min_{k}S_k\le-x\right)\le e^{-x^{2}/(2\sigma^{2})}$，用联合界与左侧相加即得 $|S_k|$ 的极大不等式。将 Hoeffding 引理替换为 Pinelis 的最优引理（利用 $\mathbb{E}[X_i^{2}\mid\mathcal{F}_{i-1}]$ 的信息）可把指数常数进一步改进，即 Pinelis 所证明的常数最优性。$\square$

## 五、应用与意义

- 序贯分析：构造置信序列（confidence sequence）与序贯检验的临界值，保证在任意停时都有效的覆盖概率。
- 在线学习与 Bandit：遗憾界（regret bound）需要全时间一致的高概率界，极大不等式是标准工具。
- 大偏差与经验过程：给出经验过程 $\sup_{k\le n}$ 型统计量的指数界，是经典大偏差原理的离散、非渐近对应物。
- 自归一化统计：Pinelis 把不等式推广到以 $\sqrt{\sum_i X_i^{2}}$ 归一化的形式，适用于 t 统计量的非渐近分析。

## 课堂问答

**老师**：为什么"过程最大值$\max_{k\le n}S_k$"的尾界能不多付$\log n$？

**学生**：因为不必对每个时刻单独做联合界，而是构造指数上鞅$M_k=\exp(\lambda S_k-\frac{\lambda^2}{2}\sum_{i\le k}c_i^2)$，其中补偿项抵消累积涨落。对非负上鞅用 Ville 极大不等式直接得到全时刻一致的界
$$
\mathbb P\Big(\max_{0\le k\le n}S_k\ge x\Big)\le\exp\Big(-\frac{x^2}{2\sigma^2}\Big),\qquad\sigma^2=\sum_i c_i^2.
$$

**老师（追问）**：上鞅性质依据哪一步？$\lambda$怎么定？

**学生**：由条件 Hoeffding 引理，对鞅差$X_i\in[-c_i,c_i]$有$\mathbb E[e^{\lambda X_i}\mid\mathcal F_{i-1}]\le e^{\lambda^2c_i^2/2}$，逐项相乘并约掉补偿因子即得$\mathbb E[M_k\mid\mathcal F_{k-1}]\le M_{k-1}$。得到$\mathbb P(\max S_k\ge x)\le\exp(-\lambda x+\frac{\lambda^2\sigma^2}{2})$后对$\lambda$最优，取$\lambda=x/\sigma^2$即得指数$-\frac{x^2}{2\sigma^2}$。

**老师（拓展）**：它在哪些场景不可替代？

**学生**：序贯分析中构造置信序列、Bandit 的 regret 界、经验过程的$\sup_{k\le n}$型统计量都要求"对一切时刻同时成立"，终点界做不到。它与终点 Hoeffding–Azuma 界共享同一指数速率，不额外损失$\log n$因子，这正是 Pinelis 的关键贡献。

## 相关条目

- [切比雪夫型指数不等式](./切比雪夫型指数不等式.md)：同属该级别的指数型尾界，可比较终点界与极大界的差别。
- [Cramér定理](./Cramér定理.md)：和有界/轻尾增量的经典大偏差速率函数。
- [Gärtner-Ellis定理](./Gärtner-Ellis定理.md)：把大偏差从和推广到依赖结构的统计量。
- [Varadhan引理](./Varadhan引理.md)：大偏差原理的等价刻画与 Laplace 原理。
- [上穿不等式](../第41级-随机过程/上穿不等式.md)：上鞅极大不等式的经典形式，本证明步骤 3 的基础。
- [Hoeffding不等式](../第99级-统计学习理论/Hoeffding不等式.md)：步骤 1 依赖的引理来源，也是本不等式的非极大版本。
