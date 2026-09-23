# 欧氏空间中的紧性与 Heine-Borel 定理

> **一句话大白话**：在欧氏空间里，"紧"就是"有界且闭"——不会跑到无穷远，也不会漏掉自己的极限点，这两个条件合起来正好等价于紧致。
>
> **小例子**：闭区间 $[0,1]$、闭圆盘、球面都是紧集；开区间 $(0,1)$ 与整条直线 $\mathbb R$ 都不是紧的。

## 一、定理介绍

> **前置依赖**：Bolzano-Weierstrass定理、实数完备性定理的等价性、确界原理、紧致空间的连续像、极值定理

Heine–Borel 定理是欧氏空间（更一般地有限维赋范空间）中刻画紧性的基本定理：$K\subseteq\mathbb R^n$ 紧当且仅当 $K$ 有界且闭。它把"任意开覆盖有有限子覆盖"这一抽象的紧性条件，转化为两个极易检验的几何条件，因而成为分析、拓扑、优化与博弈论中最常用的判定工具。

在有限维之外定理一般失效：无限维赋范空间的闭单位球有界且闭但不紧。本条目给出 $\mathbb R^n$ 情形的完整证明，包括"序列紧与紧等价"这一度量空间事实，以及连续函数在紧集上取到最值的推论。

## 二、原理思路

1. **序列紧 $\Rightarrow$ 紧**：若开覆盖无有限子覆盖，从每个 $1/m$-球里挑出"不被任何单个 $U_\lambda$ 包含"的点，序列紧性给出收敛子列，落点所在的 $U_{\lambda_0}$ 最终会吞掉该小球，矛盾。
2. **区间紧**：由 Bolzano-Weierstrass 定理，$[a,b]$ 中任意序列有收敛子列且极限仍在 $[a,b]$，故 $[a,b]$ 序列紧，从而是紧的。
3. **有限乘积**：序列紧集之积仍序列紧（对两个坐标依次取子列）。
4. **有界闭 $\Rightarrow$ 紧**：$K$ 有界时 $K\subseteq[-M,M]^n$，而紧集的闭子集仍紧。
5. **紧 $\Rightarrow$ 有界、闭**：用球覆盖证有界，用 Hausdorff 分离（每点取半个距离的球）证闭。

## 三、定理的严格表述

**（Heine–Borel 定理）** 设 $K\subseteq\mathbb R^n$。以下三条等价：

(a) $K$ 是**紧**的：$K$ 的每个开覆盖都有有限子覆盖；

(b) $K$ 是**序列紧**的：$K$ 中每个序列都有收敛于 $K$ 中某点的子序列；

(c) $K$ **有界且闭**。

**（极值推论）** 设 $K\subseteq\mathbb R^n$ 非空紧，$f:K\to\mathbb R$ 连续。则 $f$ 在 $K$ 上取到最大值与最小值，即存在 $\boldsymbol a,\boldsymbol b\in K$ 使

$$
f(\boldsymbol a)=\min_{K}f,\qquad f(\boldsymbol b)=\max_{K}f .
$$

## 四、证明过程

**步骤 1：度量空间中序列紧 $\Rightarrow$ 紧**

设 $K$ 序列紧。先证 $K$ **完全有界**：否则存在 $\varepsilon>0$ 使 $K$ 不能被有限个半径 $\varepsilon$ 的球覆盖；递归选取 $\boldsymbol x_k\in K$ 使 $\boldsymbol x_k$ 与前面所有点的距离 $\ge\varepsilon$，则该序列任意两项距离 $\ge\varepsilon$，不存在收敛子列，矛盾。

再设 $\{U_\lambda\}$ 是 $K$ 的开覆盖且无有限子覆盖。对每个 $m$，用有限个半径 $1/m$ 的球覆盖 $K$（完全有界）；由无有限子覆盖，存在 $\boldsymbol x_m\in K$ 使 $B(\boldsymbol x_m,1/m)$ 不包含于任何 $U_\lambda$。由序列紧性取子列 $\boldsymbol x_{m_j}\to\boldsymbol x\in K$。因 $\boldsymbol x\in U_{\lambda_0}$（$\lambda_0$ 为某指标）且 $U_{\lambda_0}$ 开，存在 $\rho>0$ 使 $B(\boldsymbol x,\rho)\subseteq U_{\lambda_0}$。取 $j$ 充分大使 $1/m_j<\rho/2$ 且 $\|\boldsymbol x_{m_j}-\boldsymbol x\|<\rho/2$，则 $B(\boldsymbol x_{m_j},1/m_j)\subseteq B(\boldsymbol x,\rho)\subseteq U_{\lambda_0}$，与取法矛盾。故 $K$ 有有限子覆盖，即 $K$ 紧。$\square$

**步骤 2：闭区间 $[a,b]$ 紧**

设 $(\boldsymbol y_k)$ 是 $[a,b]$ 中的序列。由 Bolzano-Weierstrass 定理（有界实数列有收敛子列），它与实数完备性定理的等价性保证该列存在收敛子列；其极限属于闭区间 $[a,b]$。故 $[a,b]$ 序列紧，由步骤 1 得 $[a,b]$ 紧。$\square$

**步骤 3：有限乘积与方体 $[-M,M]^n$ 紧**

设 $X,Y$ 序列紧。对 $X\times Y$ 中序列 $(\boldsymbol x_k,\boldsymbol y_k)$，先取子列使 $\boldsymbol x_{k_j}$ 收敛于 $X$ 中某点，再取该子列的子列使 $\boldsymbol y$ 坐标收敛于 $Y$ 中某点，于是 $(\boldsymbol x_{k_j},\boldsymbol y_{k_j})$ 收敛于 $X\times Y$ 中某点。故 $X\times Y$ 序列紧，由步骤 1 紧。

对 $n$ 作归纳：$n=1$ 由步骤 2，$[-M,M]^n=[-M,M]^{n-1}\times[-M,M]$ 紧。$\square$

**步骤 4：有界闭 $\Rightarrow$ 紧**

设 $K$ 有界且闭。取 $M>0$ 使 $K\subseteq[-M,M]^n$。设 $\{U_\lambda\}$ 为 $K$ 的开覆盖，则 $\{U_\lambda\}\cup\{\mathbb R^n\setminus K\}$ 是紧集 $[-M,M]^n$ 的开覆盖，故有有限子覆盖；去掉其中可能出现的 $\mathbb R^n\setminus K$，剩下的 $U_\lambda$ 有限个已覆盖 $K$。故 $K$ 紧。$\square$

**步骤 5：紧 $\Rightarrow$ 有界**

取一点 $\boldsymbol x_0$，则 $\{B(\boldsymbol x_0,m)\}_{m\in\mathbb N}$ 是 $K$ 的开覆盖，有有限子覆盖，故 $K\subseteq B(\boldsymbol x_0,m_0)$ 对某个 $m_0$ 成立，即 $K$ 有界。$\square$

**步骤 6：紧 $\Rightarrow$ 闭**

设 $K$ 紧，$\boldsymbol x\notin K$。对每个 $\boldsymbol y\in K$，令 $r_{\boldsymbol y}=d(\boldsymbol x,\boldsymbol y)/2>0$，则 $\{B(\boldsymbol y,r_{\boldsymbol y})\}_{\boldsymbol y\in K}$ 是 $K$ 的开覆盖，有有限子覆盖 $B(\boldsymbol y_1,r_1),\dots,B(\boldsymbol y_m,r_m)$。令 $r=\min_i r_i>0$。若存在 $\boldsymbol z\in B(\boldsymbol x,r)\cap K$，则某 $i$ 使 $\boldsymbol z\in B(\boldsymbol y_i,r_i)$，于是

$$
d(\boldsymbol x,\boldsymbol y_i)\le d(\boldsymbol x,\boldsymbol z)+d(\boldsymbol z,\boldsymbol y_i)<r+r_i\le 2r_i=d(\boldsymbol x,\boldsymbol y_i),
$$

矛盾。故 $B(\boldsymbol x,r)\cap K=\varnothing$，即 $\boldsymbol x$ 是 $K$ 的补集的内点，$K$ 闭。$\square$

**步骤 7：极值推论**

$f$ 连续，由紧致空间的连续像知 $f(K)\subseteq\mathbb R$ 是紧集，从而有界且闭。由确界原理 $f(K)$ 有上确界 $\sup f(K)\in\mathbb R$；因 $f(K)$ 闭，其上确界属于 $f(K)$，即存在 $\boldsymbol b\in K$ 使 $f(\boldsymbol b)=\sup f(K)=\max_K f$。对下确界同理得最小值。$\blacksquare$

## 五、应用与意义

**在分析与博弈论中的作用**：

1. **极值的存在性**：连续函数在紧集上取到最值，是优化与博弈论中"最优反应存在""Nash 均衡存在"的第一步；角谷不动点定理中的凸紧定义域正依赖本定理把"闭有界"识别为"紧"。
2. **最值与最佳逼近**：凸集投影、距离函数的可达性、Weierstrass 逼近等都以紧性或"下水平集紧"为存在性依据。
3. **一致连续与有限覆盖**：紧性给出"连续 $\Rightarrow$ 一致连续"以及积分理论中分割的存在性，是实分析与拓扑的标准工具。

**理论意义**：Heine–Borel 定理把抽象的紧性具体化为"有界 $+$ 闭"，是有限维欧氏空间特有的性质，其本质在于 $\mathbb R^n$ 的完备性与局部紧性。在一般度量空间中只保留"紧 $\Rightarrow$ 有界闭"单向结论（且"闭有界"一般推不出紧）；在无限维赋范空间中该定理整体失效，这正是泛函分析需要弱拓扑与 Banach–Alaoglu 定理的原因。
