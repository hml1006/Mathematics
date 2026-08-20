# Wigner 半圆律

> **一句话大白话**：很大很大的对称随机矩阵，把特征值摊开来看会"挤"成半圆形状——随机波动的细节被抹平，只留下一个固定的半圆轮廓。
>
> **小例子**：对 $n\times n$ 对称随机矩阵（顶点 i.i.d.、零均值、方差有限），把特征值除以 $\sqrt n$，当 $n\to\infty$ 时其经验谱分布收敛到 $[-2,2]$ 上的半圆密度 $p(x)=\frac1{2\pi}\sqrt{4-x^2}$。

## 一、定理介绍

Wigner 半圆律是随机矩阵理论中最基本、最重要的结果之一，它描述了一大类 Hermitian（或实对称）随机矩阵在维数趋于无穷时，其特征值经验分布的极限形状。Eugene Wigner 于 1955 年在研究原子核能级时首次观察到这一现象：复杂量子系统的哈密顿量所对应的随机矩阵，其本征值的宏观分布并非杂乱无章，而是呈现出优美的半圆形密度。该定律揭示了高维随机矩阵深层的一致性与普适性，奠定了随机矩阵理论的基石。

## 二、原理思路

考虑一个 $N \times N$ 的 Hermitian 随机矩阵 $H_N$，其非对角元素为独立同分布的随机变量，均值为 $0$，方差为 $1/N$（因此总方差规模可控）。由于矩阵是 Hermitian 的，其特征值 $\lambda_1, \dots, \lambda_N$ 都是实数。定义经验谱分布（empirical spectral distribution, ESD）为
$$
\mu_N = \frac{1}{N} \sum_{i=1}^N \delta_{\lambda_i}.
$$
当 $N \to \infty$ 时，若适当地将特征值缩放，则 $\mu_N$ 会弱收敛到一个确定的概率分布，其密度函数恰好是一个以原点为中心、半径为 $2$ 的半圆。直观上，这相当于大量独立随机涨落经过 Hermitian 结构的耦合后，在宏观尺度上产生了确定性的平衡形态。

## 三、定理的严格表述

设 $(X_{ij})_{1 \le i \le j < \infty}$ 为一族独立同分布的实值随机变量，满足
$$
\mathbb{E}[X_{ij}] = 0, \quad \mathbb{E}[X_{ij}^2] = 1.
$$
对每个 $N \ge 1$，构造 $N \times N$ 的 Wigner 矩阵 $W_N = (w_{ij})$，其中
$$
w_{ij} = \frac{1}{\sqrt{N}} X_{ij}, \quad w_{ji} = w_{ij} \quad (i < j), \quad w_{ii} = \frac{1}{\sqrt{N}} X_{ii}.
$$
记 $W_N$ 的特征值为 $\lambda_1 \le \lambda_2 \le \dots \le \lambda_N$，并定义经验谱分布
$$
\mu_{W_N} = \frac{1}{N} \sum_{i=1}^N \delta_{\lambda_i}.
$$
则当 $N \to \infty$ 时，$\mu_{W_N}$ 几乎必然弱收敛到 Wigner 半圆分布 $\mu_{\mathrm{sc}}$，其密度函数为
$$
\rho_{\mathrm{sc}}(x) = \frac{1}{2\pi} \sqrt{4 - x^2} \, \mathbf{1}_{[-2,2]}(x).
$$
等价地，对任意有界连续函数 $f: \mathbb{R} \to \mathbb{R}$，有
$$
\frac{1}{N} \sum_{i=1}^N f(\lambda_i) \xrightarrow{\text{a.s.}} \int_{-2}^{2} f(x) \, \rho_{\mathrm{sc}}(x) \, dx.
$$

## 四、证明过程

Wigner 半圆律的证明有多种途径，其中最经典的是矩方法和 Stieltjes 变换方法。下面概述矩方法的核心步骤。

**步骤 1：矩方法的归约。** 由于半圆分布由各阶矩唯一确定，只需证明对任意正整数 $k$，
$$
\frac{1}{N} \sum_{i=1}^N \lambda_i^k = \frac{1}{N} \operatorname{Tr}(W_N^k) \xrightarrow{\text{a.s.}} m_k,
$$
其中 $m_k$ 是半圆分布的 $k$ 阶矩。奇数阶矩 $m_{2k+1} = 0$，偶数阶矩为 Catalan 数
$$
m_{2k} = C_k = \frac{1}{k+1} \binom{2k}{k}.
$$

**步骤 2：展开矩阵幂的迹。** 利用迹的循环性，
$$
\frac{1}{N} \operatorname{Tr}(W_N^k) = \frac{1}{N^{1+k/2}} \sum_{i_1,\dots,i_k} X_{i_1 i_2} X_{i_2 i_3} \cdots X_{i_k i_1}.
$$
由于 $X_{ij}$ 均值为零，要使期望不为零，乘积中的每个随机变量必须至少出现两次。

**步骤 3：图论计数。** 将指标序列 $(i_1, i_2, \dots, i_k, i_1)$ 视为一个闭合路径。非零贡献主要来自那些在路径中每条边至少经过两次的图。当 $k$ 为奇数时，不存在这样的路径，极限为 $0$。当 $k = 2\ell$ 为偶数时，主导贡献对应于每条边恰好经过两次的非交叉配对（non-crossing pairings），其数目正是 Catalan 数 $C_\ell$。

**步骤 4：方差控制与大数定律。** 通过计算展开式中各项的方差，并利用独立性以及 $X_{ij}$ 的有限矩条件，可以证明当 $N \to \infty$ 时方差趋于零，从而得到几乎必然的收敛。

**步骤 5：Stieltjes 变换方法（补充）。** 记 $m_N(z) = \frac{1}{N} \operatorname{Tr}((W_N - zI)^{-1})$ 为经验谱分布的 Stieltjes 变换。利用 Schur 补公式或留数恒等式，可得自洽方程
$$
m(z) = -\frac{1}{z + m(z)},
$$
其解给出 Stieltjes 变换
$$
m(z) = \frac{-z + \sqrt{z^2 - 4}}{2},
$$
反演即得半圆密度 $\rho_{\mathrm{sc}}$。

## 五、应用与意义

Wigner 半圆律的重要性远超随机矩阵理论本身。在量子物理中，它解释了复杂原子核、无序固体和量子混沌系统中能级宏观分布的普适性。在无线通信中，大规模 MIMO 系统的信道矩阵特征值分布服从半圆律，指导了频谱效率与功率分配的优化。在统计学中，高维协方差矩阵的谱分析依赖于半圆律作为基准。此外，半圆律还与自由概率论中的自由中心极限定理深刻联系：独立 Hermitian 随机矩阵之和的谱分布收敛到半圆，这可以视为经典中心极限定理的非交换推广。
