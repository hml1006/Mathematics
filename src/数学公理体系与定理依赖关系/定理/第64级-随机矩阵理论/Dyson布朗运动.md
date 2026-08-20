# Dyson 布朗运动

> **一句话大白话**：把随机矩阵的特征值想象成一排互相"排斥"的小粒子，彼此推搡着又各自无规则乱走，它们随时间演化的集体运动就叫 Dyson 布朗运动——这是随机矩阵进入动力系统的入口。
>
> **小例子**：给 $N$ 个粒子同时加上"两两斥力"和随机布朗扰动，让 $t$ 从 $0$ 走到 $t$，粒子位置 $\lambda_1(t),\ldots,\lambda_N(t)$ 的联合演化正是 Hermite 系（高斯酉系）特征值随 $t$ 的漂移。

## 一、定理介绍

Dyson 布朗运动是随机矩阵理论中描述 Hermitian 随机矩阵特征值随时间演化的随机过程。Freeman Dyson 于 1962 年证明：若一个 Hermitian 矩阵的每个自由元素都按照独立的标准布朗运动演化，则其特征值满足一组相互耦合的随机微分方程，其中每个特征值受到来自其他所有特征值的排斥势作用。这一定理将随机矩阵的静态谱理论与随机过程的动态演化联系起来，深刻揭示了特征值之间的对数库仑相互作用。

## 二、原理思路

考虑一个 $N \times N$ 的 Hermitian 矩阵值过程 $H(t)$，其非对角元素为复布朗运动，对角元素为实布朗运动，且所有增量独立同分布。由于 $H(t)$ 是 Wigner 矩阵的连续类比，其特征值 $\lambda_1(t) \le \dots \le \lambda_N(t)$ 也随时间随机演化。关键在于：矩阵元素的独立布朗运动会诱导出特征值之间的强相关性。通过对矩阵特征值进行伊藤微分，可以发现非对角自由度被平均掉，只剩下特征值过程，并产生形如 $\sum_{j \neq i} 1/(\lambda_i - \lambda_j)$ 的漂移项。这正是带电粒子在二维空间中的一维约束所形成的对数排斥势的梯度。

## 三、定理的严格表述

设 $W(t)$ 为一个 $N \times N$ 的 Hermitian 布朗运动，定义为
$$
W(t) = \frac{1}{\sqrt{2N}} \left(B(t) + B(t)^*\right),
$$
其中 $B(t)$ 的实部与虚部均为独立的标准实矩阵值布朗运动。等价地，$W(t)$ 的对角元为方差 $1/N$ 的实布朗运动，非对角元为方差 $1/(2N)$ 的复布朗运动。

考虑 Ornstein-Uhlenbeck 型矩阵过程
$$
dH(t) = -\frac{1}{2} H(t) \, dt + dW(t),
$$
其中 $H(0)$ 为确定性的 Hermitian 矩阵（或服从某初始分布）。设 $\lambda_1(t) < \lambda_2(t) < \dots < \lambda_N(t)$ 为 $H(t)$ 的严格递增特征值。则存在同一概率空间上的布朗运动 $\{B_i(t)\}_{i=1}^N$，使得
$$
d\lambda_i(t) = -\frac{1}{2} \lambda_i(t) \, dt + \frac{1}{N} \sum_{j \neq i} \frac{1}{\lambda_i(t) - \lambda_j(t)} \, dt + \frac{1}{\sqrt{N}} \, dB_i(t),
$$
对 $i = 1, \dots, N$ 成立，直到首次碰撞时间
$$
\tau = \inf\{t > 0 : \lambda_i(t) = \lambda_j(t) \text{ 对某 } i \neq j\}.
$$
由于漂移项的强排斥性，实际上对任意有限时间 $T > 0$ 都有 $\mathbb{P}(\tau > T) = 1$，即特征值几乎必然不碰撞。

若考虑无 Ornstein-Uhlenbeck 漂移的纯 Dyson 布朗运动，方程为
$$
d\lambda_i(t) = \frac{1}{N} \sum_{j \neq i} \frac{1}{\lambda_i(t) - \lambda_j(t)} \, dt + \frac{1}{\sqrt{N}} \, dB_i(t).
$$

## 四、证明过程

Dyson 布朗运动的推导基于矩阵值伊藤公式和特征值扰动理论。

**步骤 1：矩阵元素的伊藤方程。** 设 $H(t)$ 为前述矩阵值过程，其元素满足
$$
dh_{ij}(t) = -\frac{1}{2} h_{ij}(t) \, dt + dw_{ij}(t),
$$
其中 $dw_{ij}$ 为独立（复）布朗运动增量，方差适当。

**步骤 2：特征值的一阶变分。** 设 $u_i(t)$ 为对应于 $\lambda_i(t)$ 的单位特征向量。由特征值一阶扰动公式，
$$
d\lambda_i(t) = u_i(t)^* \, dH(t) \, u_i(t) = -\frac{1}{2} \lambda_i(t) \, dt + u_i(t)^* \, dW(t) \, u_i(t).
$$
第一项为 $O(dt)$ 的 Ornstein-Uhlenbeck 漂移。第二项的二次变差给出 Brownian 噪声：
$$
\left\langle u_i^* dW u_i \right\rangle = \frac{1}{N} dt,
$$
因此可以写成 $\frac{1}{\sqrt{N}} dB_i(t)$。

**步骤 3：特征向量的二阶修正。** 利用非退化特征值的二阶微扰公式
$$
d\lambda_i = u_i^* dH u_i + \sum_{j \neq i} \frac{|u_j^* dH u_i|^2}{\lambda_i - \lambda_j} + o(dt),
$$
并计算交叉项的期望
$$
\mathbb{E}\left[|u_j^* dW u_i|^2 \, \big| \, \mathcal{F}_t\right] = \frac{1}{N} dt,
$$
得到漂移项
$$
\frac{1}{N} \sum_{j \neq i} \frac{1}{\lambda_i - \lambda_j} dt.
$$

**步骤 4：不碰撞性的证明。** 漂移项在 $\lambda_i \to \lambda_j$ 时发散，方向将两个特征值推开。构造 Lyapunov 函数
$$
L(t) = -\sum_{i<j} \log(\lambda_j(t) - \lambda_i(t)),
$$
可以证明其伊藤漂移有下界，从而排除有限时间碰撞。

**步骤 5：与静态系综的联系。** 当 $t \to \infty$ 时，$H(t)$ 的平稳分布为 GUE。此时特征值的静态联合密度
$$
\propto \prod_{i<j} (\lambda_i - \lambda_j)^2 \exp\left(-N \sum_i \lambda_i^2\right)
$$
正好是上述随机微分方程的不变测度，其对数梯度正是漂移项的来源。

## 五、应用与意义

Dyson 布朗运动为理解随机矩阵特征值的动态提供了自然框架。在量子混沌和核物理中，它模拟了复杂系统哈密顿量在外部微扰下的能级演化。在概率论中，它是研究随机矩阵局部统计普适性的关键工具：通过将一般 Wigner 矩阵与 GUE 用 Dyson 布朗运动连接起来，可以在适当时间尺度上证明两者特征值统计的耦合（如 Erdős-Schlein-Yau 的方法）。在金融数学中，相关矩阵特征值的随机演化也可用类似的特征值过程建模。此外，Dyson 布朗运动还与随机 Loewner 演化（SLE）、随机矩阵的 universality 证明以及最优输运中的梯度流解释有密切联系。
