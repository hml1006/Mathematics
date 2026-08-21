# Tracy-Widom 分布

> **一句话大白话**：巨型随机矩阵"最大的那个特征值"波动到哪儿是有规律的——经过恰当缩放后，它服从一个固定不变的 Tracy-Widom 分布，而不受具体排列方式扰乱。
>
> **小例子**：对 $n\times n$ 高斯酉系（GUE），令 $\lambda_{\max}$ 为最大特征值，则 $n^{1/6}(\lambda_{\max}-2\sqrt n)$ 随 $n\to\infty$ 依分布收敛到 Tracy-Widom 分布 $F_2$。

## 一、定理介绍

> **前置依赖**：GUE 特征值联合密度与 Hermite 多项式、行列式点过程与 Fredholm 行列式、Hermite 函数的 Plancherel-Rotach 渐近、Airy 函数与 Airy 核、Painlevé II 方程。

Tracy-Widom 分布是随机矩阵理论中描述最大特征值在适当中心化与缩放后极限分布的一类重要概率分布。与 Wigner 半圆律和 Marchenko-Pastur 定律刻画特征值的宏观 bulk 分布不同，Tracy-Widom 定律关注的是谱边缘的微观涨落。Tracy 与 Widom 在 1990 年代证明了 GUE（Gaussian Unitary Ensemble）的最大特征值在 $N^{-2/3}$ 尺度下收敛到一个由 Painlevé II 方程显式刻画的分布。这一定律后来在大量随机矩阵模型和组合问题中被发现具有惊人的普适性。

## 二、原理思路

考虑一个 $N \times N$ 的 GUE 矩阵 $M_N$，其密度正比于 $\exp(-N \operatorname{Tr}(M_N^2))$。其特征值的联合密度为
$$
P(\lambda_1, \dots, \lambda_N) \propto \prod_{i<j} (\lambda_i - \lambda_j)^2 \exp\left(-N \sum_{i=1}^N \lambda_i^2\right).
$$
最大特征值 $\lambda_{\max}^{(N)}$ 依概率收敛到 Wigner 半圆分布的右端点 $2$。为了观察其涨落，需要减去 $2$ 并乘以放大因子 $N^{2/3}$。直观上，$N^{-2/3}$ 是半圆密度在边缘 $x=2$ 附近消失速率 $\sqrt{2-x}$ 所决定的特征尺度。Tracy-Widom 分布 $F_2$ 正是这一定标后极限的累积分布函数。

## 三、定理的严格表述

设 $M_N$ 为 $N \times N$ 的 GUE 随机矩阵，其联合特征值密度如上。记
$$
\lambda_{\max}^{(N)} = \max_{1 \le i \le N} \lambda_i.
$$
则当 $N \to \infty$ 时，
$$
N^{2/3} \left(\lambda_{\max}^{(N)} - 2\right) \xrightarrow{d} \mathrm{TW}_2,
$$
其中 $\mathrm{TW}_2$ 为 Tracy-Widom 分布（指标 $\beta=2$），其累积分布函数 $F_2(s)$ 可表示为
$$
F_2(s) = \exp\left(-\int_s^\infty (x-s) q(x)^2 \, dx\right).
$$
这里 $q(s)$ 是 Hastings-McLeod 解，即 Painlevé II 方程
$$
q''(s) = s q(s) + 2 q(s)^3
$$
满足边界条件
$$
q(s) \sim \mathrm{Ai}(s), \quad s \to +\infty,
$$
的唯一解，其中 $\mathrm{Ai}(s)$ 为 Airy 函数。

对于实对称的 GOE（Gaussian Orthogonal Ensemble），相应的极限分布为 $F_1$，表达式为
$$
F_1(s)^2 = F_2(s) \exp\left(-\int_s^\infty q(x) \, dx\right).
$$
对于四元数自对偶的 GSE（Gaussian Symplectic Ensemble），极限分布为 $F_4$。这三个分布分别对应 Dyson 指标 $\beta = 1, 2, 4$。

## 四、证明过程

Tracy-Widom 定律的证明高度依赖于可积概率与正交多项式技巧。以下是 GUE 情形的证明概要。

**步骤 1：行列式点过程表示。** GUE 特征值构成一个行列式点过程，其核函数可用 Hermite 多项式显式写出：
$$
K_N(x,y) = \sum_{k=0}^{N-1} \psi_k(x) \psi_k(y),
$$
其中 $\psi_k$ 是 Hermite 函数。最大特征值不超过 $t$ 的概率可写成 Fredholm 行列式
$$
\mathbb{P}\left(\lambda_{\max}^{(N)} \le t\right) = \det(I - K_N)_{L^2(t,\infty)}.
$$

**步骤 2：Plancherel-Rotach 渐近与 Airy 核。** 在边缘 $x=2$ 附近作变量替换
$$
x = 2 + \frac{\xi}{N^{2/3}}, \quad y = 2 + \frac{\eta}{N^{2/3}},
$$
利用 Hermite 函数的 Plancherel-Rotach 渐近公式，可得
$$
\frac{1}{N^{2/3}} K_N\left(2 + \frac{\xi}{N^{2/3}}, 2 + \frac{\eta}{N^{2/3}}\right) \to K_{\mathrm{Ai}}(\xi,\eta),
$$
其中 Airy 核
$$
K_{\mathrm{Ai}}(\xi,\eta) = \frac{\mathrm{Ai}(\xi) \mathrm{Ai}'(\eta) - \mathrm{Ai}'(\xi) \mathrm{Ai}(\eta)}{\xi - \eta}.
$$

**步骤 3：Fredholm 行列式收敛。** 由核的一致收敛性和迹类算子的连续性，
$$
\mathbb{P}\left(N^{2/3}(\lambda_{\max}^{(N)} - 2) \le s\right) \to \det(I - K_{\mathrm{Ai}})_{L^2(s,\infty)}.
$$

**步骤 4：Painlevé II 表示。** Tracy 与 Widom 进一步证明上述 Fredholm 行列式可表示为
$$
\det(I - K_{\mathrm{Ai}})_{L^2(s,\infty)} = \exp\left(-\int_s^\infty (x-s) q(x)^2 \, dx\right),
$$
其中 $q$ 满足 Painlevé II 方程。这通过将行列式的对数导数与 Hamiltonian 系统联系得到。

## 五、应用与意义

Tracy-Widom 分布的普适性远超随机矩阵领域。在组合数学中，随机排列最长递增子序列的长度在正确缩放后收敛到 $F_2$（Baik-Deift-Johansson 定理）。在统计物理中，它描述了一类随机生长模型（如 KPZ 方程与 TASEP）在长时间下的涨落分布。在高维统计中，Tracy-Widom 分布给出了主成分分析、协方差矩阵检验和稀疏检测中最大特征值显著性的精确临界分布。近年来，它还在机器学习的优化景观、随机图论以及排队论中被发现扮演重要角色，成为连接随机矩阵、可积系统与非线性波动方程的普适性标志。

## 相关条目

- [Tracy-Widom 分布（第146级-随机矩阵理论）](../第146级-随机矩阵理论/Tracy-Widom分布.md)：与本条目为同一定理，另收录于第146级-随机矩阵理论，可交叉参考。
