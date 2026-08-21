# 投资组合的Markowitz有效前沿

> **一句话大白话**：光看"平均收益"选股不够，还要看"波动/风险"；在所有给定风险下收益最高的组合们，连成一条"风险-收益"曲线就是有效前沿，理性的投资者只在这条曲线上挑。
>
> **小例子**：两只股票一个高收益高风险、一个低收益低风险，混合搭配后能在同样风险下拿到更高收益。Markowitz 有效前沿就是这条"在风险风险下收益最大"的帕累托最优集合。

## 一、定理介绍

Markowitz 有效前沿（Efficient Frontier）是均值-方差框架（MPT）的核心成果。对 $n$ 种风险资产，有效前沿由所有"给定风险（方差）下收益最大，或给定收益下风险最小"的最优组合构成。其参数形式为
$$
\sigma_p=\sqrt{\frac{(E[R_p]-r_f)^2}{a}},\qquad a=\boldsymbol\mu'\,\Sigma^{-1}\boldsymbol\mu,
$$
其中 $\boldsymbol\mu$ 为超额收益向量，$\Sigma$ 为协方差矩阵。有效前沿在 $(\sigma_p,E[R_p])$ 平面是一条双曲线的上支。

## 二、原理思路

思路是"分散化降风险 + 二次规划选最优"。组合方差 $\sigma_p^2=\mathbf w'\Sigma\mathbf w$ 因协方差带交叉项而通常小于各资产方差的加权平均，因此分散化降低非系统性风险；在"目标收益、权重和为 1"两约束下最小化方差构造成一个凸二次规划，其 Lagrange 解给出唯一最优权重，随目标收益变动扫出整条有效前沿。

## 三、定理的严格表述

设 $n$ 种资产收益向量 $\mathbf R$、均值 $\mathbf R$、正定协方差 $\Sigma$，权重 $\mathbf w$ 满足 $\mathbf w'\mathbf 1=1$。有效前沿上任意组合是下式之解，其中 $\mu_0$ 遍历可行收益范围：

$$
\min_{\mathbf w}\ \tfrac12\mathbf w'\Sigma\mathbf w\quad\text{s.t.}\ \mathbf w'\mathbf R=\mu_0,\ \mathbf w'\mathbf 1=1.
$$

其解为 $\mathbf w=\lambda_1\Sigma^{-1}\mathbf R+\lambda_2\Sigma^{-1}\mathbf 1$，$(E[R_p],\sigma_p)$ 落在由 $\sigma_p^2=\frac{(E[R_p]-r_f)^2}{a}$（存在无风险资产时）刻画的有效前沿上。

## 四、证明过程

**步骤1：建立优化问题。** 在"目标收益 $\mu_0$、权重和 $1$"约束下最小化方差 $\tfrac12\mathbf w'\Sigma\mathbf w$。

**步骤2：Lagrange 乘子法。** 构造
$$
\mathcal{L}=\tfrac12\mathbf w'\Sigma\mathbf w-\lambda_1(\mathbf w'\mathbf R-\mu_0)-\lambda_2(\mathbf w'\mathbf 1-1),
$$
一阶条件 $\Sigma\mathbf w-\lambda_1\mathbf R-\lambda_2\mathbf 1=0$，解得 $\mathbf w=\lambda_1\Sigma^{-1}\mathbf R+\lambda_2\Sigma^{-1}\mathbf 1$。

**步骤3：求解乘子。** 设 $A=\mathbf R'\Sigma^{-1}\mathbf R$，$B=\mathbf R'\Sigma^{-1}\mathbf 1$，$C=\mathbf 1'\Sigma^{-1}\mathbf 1$，代入约束得线性方程组
$$
\begin{cases}
A\lambda_1+B\lambda_2=\mu_0,\\
B\lambda_1+C\lambda_2=1,
\end{cases}
$$
解出 $\lambda_1,\lambda_2$，得到闭式最优权重。

**步骤4：端点组合与两基金分离。** 有效前沿组合都是两个"端点组合"（最小方差点与切点组合）的凸组合，从而组合配置可被"两基金定理"概括。

**步骤5：导出前沿方程。** 代入 $\sigma_p^2=\mathbf w'\Sigma\mathbf w$，经线性代数整理得到方差-收益二次关系，配合无风险资产时得到 $\sigma_p=\sqrt{(E[R_p]-r_f)^2/a}$，即双曲线（抛物面投影）有效前沿。

**结论（$\square$）**：最优组合构成凸问题的解，随目标收益扫出有效前沿。

## 五、应用与意义

Markowitz 有效前沿是现代资产配置理论的出发点，催生了两基金分离、资本资产定价模型（CAPM）、夏普比率与指数基金等实务体系。它揭示了"分散化为何重要"以及"风险与收益的权衡"，是每一位资产配置者计算最优仓位的起点。