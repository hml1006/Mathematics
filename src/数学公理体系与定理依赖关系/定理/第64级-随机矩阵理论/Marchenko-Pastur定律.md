# Marchenko-Pastur 定律

> **一句话大白话**：当样本量与维度同时变大（且比例固定）时，样本协方差矩阵特征值的整体分布会稳定收敛到一个确定形状——Marchenko-Pastur 分布，告诉你随机数据的"方差谱"长什么样。
>
> **小例子**：对 $m\times n$ 的 i.i.d. 高斯数据矩阵（样本 $n$、维数 $m$），令 $n,m\to\infty$ 使 $m/n\to c$，其特征值落在区间 $[(1-\sqrt c)^2,\;(1+\sqrt c)^2]$ 上，按 MP 密度 $p(x)\propto \frac{\sqrt{(b-x)(x-a)}}{x}$ 分布。

## 一、定理介绍

Marchenko-Pastur 定律是随机矩阵理论中描述样本协方差矩阵特征值极限分布的基本结果。与 Wigner 半圆律不同，它关注的是形如 $S_N = \frac{1}{n} X X^*$ 的样本协方差矩阵，其中 $X$ 是一个具有独立同分布元素的 $N \times n$ 数据矩阵。当维数 $N$ 与样本量 $n$ 同时趋于无穷且保持比例 $N/n \to c \in (0,\infty)$ 时，$S_N$ 的经验特征值分布收敛到一个确定性的概率分布，其支撑区间和密度由参数 $c$ 决定。这一定律由高维统计中的样本协方差分析问题驱动，在统计学、信号处理和机器学习中有广泛应用。

## 二、原理思路

设数据矩阵 $X_N$ 为 $N \times n$ 矩阵，元素为均值为 $0$、方差为 $1$ 的独立同分布随机变量。样本协方差矩阵定义为
$$
S_N = \frac{1}{n} X_N X_N^*.
$$
当 $N$ 固定而 $n \to \infty$ 时，经典统计告诉我们 $S_N$ 依概率收敛到单位矩阵 $I_N$。然而当 $N$ 与 $n$ 同阶增长时，特征值的样本波动不会消失，而是凝聚成一条连续曲线。Marchenko-Pastur 定律刻画了这一高维极限：特征值集中在区间 $[(1-\sqrt{c})^2, (1+\sqrt{c})^2]$ 上，密度呈反平方根奇异形态，并在 $c < 1$ 时于 $0$ 处可能有一个质量点。

## 三、定理的严格表述

设 $(X_{ij})_{i,j \ge 1}$ 为独立同分布的复值随机变量，满足
$$
\mathbb{E}[X_{ij}] = 0, \quad \mathbb{E}[|X_{ij}|^2] = 1.
$$
令 $X_N$ 为 $N \times n$ 矩阵，元素为 $X_{ij}/\sqrt{n}$。定义样本协方差矩阵
$$
S_N = X_N X_N^*.
$$
假设当 $N, n \to \infty$ 时，维数比收敛到
$$
\frac{N}{n} \to c \in (0, \infty).
$$
记 $S_N$ 的经验特征值分布为
$$
\mu_{S_N} = \frac{1}{N} \sum_{i=1}^N \delta_{\lambda_i(S_N)}.
$$
则 $\mu_{S_N}$ 几乎必然弱收敛到 Marchenko-Pastur 分布 $\mu_{\mathrm{MP}}^{(c)}$，其 Stieltjes 变换 $m(z)$ 满足二次方程
$$
z c m(z)^2 + (z + c - 1) m(z) + 1 = 0.
$$
具体密度函数如下：

- 当 $0 < c \le 1$ 时，$\mu_{\mathrm{MP}}^{(c)}$ 在 $[a,b]$ 上绝对连续，其中 $a = (1-\sqrt{c})^2$，$b = (1+\sqrt{c})^2$，密度为
$$
\rho_{\mathrm{MP}}^{(c)}(x) = \frac{1}{2\pi c x} \sqrt{(b-x)(x-a)} \, \mathbf{1}_{[a,b]}(x).
$$

- 当 $c > 1$ 时，除上述连续部分外，在 $0$ 处还有一个大小为 $1 - 1/c$ 的原子质量，即
$$
\mu_{\mathrm{MP}}^{(c)} = \left(1 - \frac{1}{c}\right) \delta_0 + \rho_{\mathrm{MP}}^{(c)}(x) \, dx.
$$

- 当 $c = 1$ 时，$a = 0$，$b = 4$，密度在 $0$ 处呈 $1/\sqrt{x}$ 型奇异性。

## 四、证明过程

Marchenko-Pastur 定律的证明同样可以通过矩方法或 Stieltjes 变换完成，现代最常用的方法是 Stieltjes 变换结合确定性等价技巧。

**步骤 1：Stieltjes 变换的定义。** 记
$$
m_N(z) = \frac{1}{N} \operatorname{Tr}((S_N - zI)^{-1}), \quad z \in \mathbb{C}^+.
$$
目标证明 $m_N(z)$ 几乎必然收敛到一个确定性函数 $m(z)$。

**步骤 2：Sherman-Morrison 展开与自洽方程。** 对 $S_N = \frac{1}{n} X_N X_N^*$，利用矩阵逆引理（matrix inversion lemma）以及列向量的独立性，可推导
$$
m_N(z) \approx -\frac{1}{z \left(1 - \frac{1}{n} \operatorname{Tr}((S_N - zI)^{-1})\right)}.
$$
当 $N/n \to c$ 时，上式形式化为
$$
m(z) = -\frac{1}{z \left(1 - c \, m(z)\right) - c \, m(z)}.
$$
整理后得到
$$
z c m(z)^2 + (z + c - 1) m(z) + 1 = 0.
$$

**步骤 3：解二次方程。** 取上半平面中虚部为正的解，有
$$
m(z) = \frac{-(z + c - 1) + \sqrt{(z + c - 1)^2 - 4 z c}}{2 z c}.
$$
通过 Stieltjes 反演公式
$$
\rho(x) = \frac{1}{\pi} \lim_{\varepsilon \downarrow 0} \operatorname{Im}\, m(x + i\varepsilon),
$$
即可得到 Marchenko-Pastur 密度。

**步骤 4：矩方法验证（概要）。** 计算半矩可得
$$
\int x^k \, d\mu_{\mathrm{MP}}^{(c)}(x) = \sum_{\pi \in \mathrm{NC}(k)} c^{\#(\pi)},
$$
其中求和遍历所有非交叉划分，与 Catalan 数的推广相对应。这进一步印证了高维极限下随机矩阵谱矩的组合结构。

## 五、应用与意义

Marchenko-Pastur 定律在高维统计推断中具有核心地位。主成分分析（PCA）中，样本协方差矩阵的大特征值反映了真实的低维信号结构，而小特征值则 Marchenko-Pastur 分布描述的噪声 bulk 中。该定律为判断主成分是否显著提供了理论阈值 $(1+\sqrt{c})^2$。在信号处理中，它用于阵列处理、MUSIC 算法以及协方差矩阵估计的收缩方法。在金融领域，高维资产收益率样本相关矩阵的特征值分布常用 Marchenko-Pastur 律来区分系统风险因子与随机噪声。机器学习中的核矩阵、样本协方差矩阵以及随机特征模型也广泛受益于这一普适性结果。
