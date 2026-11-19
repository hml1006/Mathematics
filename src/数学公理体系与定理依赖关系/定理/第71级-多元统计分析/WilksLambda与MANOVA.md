# Wilks $\Lambda$ 与 MANOVA

> **一句话大白话**：多元方差分析要同时比较多个指标，Wilks $\Lambda$ 就看“假设解释的散布”加入后，总散布的行列式增加了多少；$\Lambda$ 越小，说明假设外的解释越显著。
>
> **小例子**：比较三种教学方法对数学、物理两项成绩的影响。把组内误差散布矩阵记为 $\boldsymbol E$，组间散布矩阵记为 $\boldsymbol H$，若 $\det\boldsymbol E/\det(\boldsymbol E+\boldsymbol H)$ 很小，就说明组别对这组二维成绩有不可忽略的解释力。

## 介绍

Wilks $\Lambda$ 是多元方差分析（MANOVA）和多元线性模型似然比检验的核心统计量。它把多个响应变量的假设平方和—叉积矩阵与误差矩阵压缩成一个行列式比值，并有精确的有限样本分布；大样本时还常用卡方近似。

## 分析

**前置依赖**：多元正态线性模型、Wishart 分布、矩阵行列式、广义特征值、独立 Beta 分布、似然比检验。

**定理内容**：设多元正态一般线性模型的各行观测独立、协方差矩阵相同。对某个含 $h$ 个自由度的线性假设，记假设散布矩阵为 $\boldsymbol H$、误差散布矩阵为 $\boldsymbol E$，误差自由度为 $e$，并设 $e\ge p$ 使 $\boldsymbol E$ 几乎必然 可逆。Wilks 统计量为

$$
\Lambda=\frac{\det\boldsymbol E}{\det(\boldsymbol E+\boldsymbol H)}
=\det(\boldsymbol I+\boldsymbol E^{-1}\boldsymbol H)^{-1}
=\prod_{j=1}^p\frac1{1+\lambda_j},
$$

其中 $\lambda_j$ 是 $\boldsymbol E^{-1}\boldsymbol H$ 的特征值。原假设下，其精确分布记作 $\Lambda(p,h,e)$。当 $h\ge p$ 时，它可表示为 $p$ 个独立 Beta 变量之积：

$$
\Lambda(p,h,e)\overset{d}=\prod_{i=1}^p B_i,
\qquad
B_i\sim\operatorname{Beta}\!\left(\frac{e-i+1}{2},\frac h2\right).
$$

当 $h<p$ 时，$\boldsymbol H$ 至多秩 $h$，上式不能仍写成 $p$ 个非退化 Beta 因子。此时利用参数对偶
$\Lambda(p,h,e)\overset{d}=\Lambda(h,p,e+h-p)$，得到 $h$ 个独立 Beta 变量之积：

$$
\Lambda(p,h,e)\overset{d}=\prod_{i=1}^h B_i,
\qquad
B_i\sim\operatorname{Beta}\!\left(\frac{e+h-p-i+1}{2},\frac p2\right).
$$

检验在 $\Lambda$ 足够小时拒绝原假设。若 $p,h$ 固定而 $e\to\infty$，常用的 Bartlett 渐近近似为

$$
-\left[e+h-\frac{p+h+1}{2}\right]\log\Lambda
\ \xrightarrow{d}\ \chi^2_{ph}.
$$

上述 Beta 乘积是**有限样本精确表示**，后一卡方公式是**渐近近似**，二者不能混称。

## 思考过程

若只有假设成立时的误差，散布由 $\boldsymbol E$ 描述；若假设不成立，未被模型解释的系统性差异会额外进入 $\boldsymbol H$。因此比较 $\det\boldsymbol E$ 与 $\det(\boldsymbol E+\boldsymbol H)$ 就是在比较两种模型所需的总体散布体积。

由于 $0\le\Lambda\le1$，拒绝方向是“小 $\Lambda$”。自由度为 $ph$ 来自原假设所含 $h$ 个约束与 $p$ 个响应维度的乘积；Bartlett 系数中的 $e+h$ 则对应完整模型下的总误差自由度校正。

## 证明过程

从正态似然出发，对受约束模型与完整模型分别最大化。最大化后的似然比只通过两个散布矩阵的行列式出现。若总样本数为 $N$，则似然比统计量满足

$$
LR=\left(\frac{\det\boldsymbol E}{\det(\boldsymbol E+\boldsymbol H)}\right)^{N/2}
=\Lambda^{N/2},
$$

所以按小 $\Lambda$ 拒绝与 Wilks 似然比检验等价。

在原假设下，$\boldsymbol E$ 与 $\boldsymbol H$ 独立，分别服从自由度为 $e$ 和 $h$ 的中心 Wishart 分布（$h<p$ 时 $\boldsymbol H$ 可以为奇异 Wishart）。当 $h\ge p$ 时，对 $\boldsymbol E^{-1/2}\boldsymbol H\boldsymbol E^{-1/2}$ 作逐步三角化，并利用 Wishart 矩阵的独立分块性质，可把广义 Beta 型行列式分解为 $p$ 个独立一维 Beta 变量，其参数依次为 $((e-i+1)/2,h/2)$。当 $h<p$ 时，广义特征值至多有 $h$ 个非零；交换假设与响应维度的角色给出 $\Lambda(p,h,e)\overset{d}=\Lambda(h,p,e+h-p)$，再应用前一乘积即得所列 $h$ 因子公式。特别地，$h=1$ 时退化为 $\Lambda\sim\operatorname{Beta}((e-p+1)/2,p/2)$，与 Hotelling 单假设自由度检验一致。

最后展开 $\log\Lambda$ 的矩生成函数。随着 $e\to\infty$，Beta 参数中的 $e$ 主导低阶累积量，归一化后的 $-\log\Lambda$ 收敛到自由度为 $ph$ 的卡方分布；保留下一阶自由度校正即得上述 Bartlett 系数。$\square$

## 课堂问答

**老师**：Wilks $\Lambda$ 是大好还是小好？它检验的究竟是什么？

**学生**：它不是越大越显著，而是越小越说明假设矩阵 $\boldsymbol H$ 带来的散布不可忽略。MANOVA 的原假设通常是若干组的均值向量相同，或某些均值回归系数全为零；它并不是在检验各组协方差矩阵相同。

**老师（追问）**：能否把 $-constant\log\Lambda$ 永远当成精确卡方？

**学生**：不能。精确有限样本分布是 $\Lambda(p,h,e)$，可写成独立 Beta 变量乘积：$h\ge p$ 时有 $p$ 个因子，$h<p$ 时须经参数对偶写成 $h$ 个因子；卡方形式则是在 $e\to\infty$ 时的渐近近似。某些低维特殊情形还能精确换算为 $F$，但不能把这条便利推广到所有 $p,h,e$。

**老师（拓展）**：为什么用行列式而不是直接把矩阵元素相加？

**学生**：行列式衡量整个散布椭球的广义体积，并且在线性坐标变换下按统一因子变化，所以比值 $\det\boldsymbol E/\det(\boldsymbol E+\boldsymbol H)$ 不受响应变量共同可逆线性变换的影响。

## 相关条目

- [Wishart 分布的密度函数与性质](./Wishart分布的密度函数与性质.md)：提供 $\boldsymbol E$ 与 $\boldsymbol H$ 的矩阵分布基础。
- [Hotelling $T^2$ 分布与检验](./HotellingT2分布与检验.md)：一个均值自由度的常见多元均值检验可与 Wilks $\Lambda$ 相互换算。
