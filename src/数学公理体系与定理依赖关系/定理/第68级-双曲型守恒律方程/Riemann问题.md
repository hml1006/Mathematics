# Riemann问题

## 一、定理介绍

Riemann 问题是守恒律方程的一类特殊初值问题：初值由两个常数状态在 $x=0$ 处跳跃组成，即

$$
\nu(x,0)=\begin{cases}
\nu_L, & x<0,\\
\nu_+, & x>0.
\end{cases}
$$

由于方程的尺度不变性，其解通常具有自相似形式 $\nu(x,t)=\nu(x/t)$。Riemann 解由若干基本波组合而成：激波（shock）、稀疏波（rarefaction wave）和接触间断（contact discontinuity）。研究 Riemann 问题不仅有助于理解守恒律方程的局部结构，也是构造数值格式（如 Godunov 格式、Glimm 格式）的核心工具。

## 二、原理思路

双曲守恒律系统

$$
\nu_t + f(\nu)_x = 0
$$

在严格双曲假设下，矩阵 $A(\nu)=Df(\nu)$ 有 $n$ 个互异实特征值

$$
\lambda_1(\nu)<\lambda_2(\nu)<\cdots<\lambda_n(\nu)
$$

及对应右特征向量 $r_k(\nu)$。每个特征场要么是真非线性的（genuinely nonlinear），要么是线性退化的（linearly degenerate）。

- 对**真非线性场**，可产生激波或稀疏波；
- 对**线性退化场**，只产生接触间断。

Riemann 问题的解可视为从 $\nu_L$ 出发，沿各特征场的 Hugoniot 曲线或积分曲线到达 $\nu_+$ 的分段路径。

## 三、定理的严格表述

### 3.1 基本假设

设 $f\in C^2(\mathbb{R}^n;\mathbb{R}^n)$，且对所有考虑的 $\nu$，矩阵 $Df(\nu)$ 有 $n$ 个互异实特征值，即系统是**严格双曲**的。第 $k$ 特征场满足下列条件之一：

- 真非线性：$\nabla\lambda_k(\nu)\cdot r_k(\nu)\neq 0$；
- 线性退化：$\nabla\lambda_k(\nu)\cdot r_k(\nu)\equiv 0$。

### 3.2 Riemann 解的结构定理

设 $|\nu_+-\nu_L|$ 充分小，则上述 Riemann 问题存在唯一的自相似弱解（在 Lax 熵条件下），该解由至多 $n$ 个基本波组成，每个波对应一个特征场，依次为

$$
\nu_L=\nu_0\xrightarrow{1}\nu_1\xrightarrow{2}\cdots\xrightarrow{n}\nu_n=\nu_+,
$$

其中第 $k$ 个波为以下三种之一：

1. **激波**：速度 $s_k$ 满足 Rankine–Hugoniot 条件

$$
s_k(\nu_k-\nu_{k-1}) = f(\nu_k)-f(\nu_{k-1}),
$$

并满足 Lax 熵条件

$$
\lambda_k(\nu_{k-1}) > s_k > \lambda_k(\nu_k).
$$

2. **稀疏波**：在区域 $\lambda_k(\nu_{k-1}) < x/t < \lambda_k(\nu_k)$ 内，解沿第 $k$ 特征场的积分曲线变化，满足

$$
\frac{d\nu}{d\xi}=r_k(\nu),\qquad \nu\bigl(\lambda_k(\nu_{k-1})\bigr)=\nu_{k-1},
\quad \nu\bigl(\lambda_k(\nu_k)\bigr)=\nu_k.
$$

3. **接触间断**：当第 $k$ 场线性退化时，间断速度等于两侧特征值：

$$
s_k=\lambda_k(\nu_{k-1})=\lambda_k(\nu_k),
$$

且仍满足 Rankine–Hugoniot 条件。

## 四、证明过程

### 4.1 自相似形式的必然性

方程与初值在变换 $(x,t)\mapsto (\alpha x,\alpha t)$ 下不变，因此若解唯一，则必满足 $\nu(x,t)=\nu(x/t)$。令 $\xi=x/t$，方程化为

$$
-\xi \nu'(\xi) + f\bigl(\nu(\xi)\bigr)' = 0,
$$

即

$$
\bigl(Df(\nu)-\xi I\bigr)\nu'(\xi)=0.
$$

若 $\nu'(\xi)\neq 0$，则 $\xi$ 必为某特征值 $\lambda_k(\nu)$，且 $\nu'(\xi)$ 平行于 $r_k(\nu)$，这正是稀疏波的微分方程。

### 4.2 局部波曲线的存在性

对每个 $k$，定义 Hugoniot 曲线

$$
H_k(\varepsilon;\nu_-)=\bigl\{\nu_+:\,s(\nu_+ - \nu_-) = f(\nu_+)-f(\nu_-)\bigr\}
$$

与积分曲线

$$
R_k(\varepsilon;\nu_-)=\bigl\{\nu_+:\,\nu_+=\nu_- + \varepsilon r_k(\nu_-) + O(\varepsilon^2)\bigr\}.
$$

由隐函数定理，当 $\varepsilon$ 充分小时这两条曲线存在且彼此在 $O(\varepsilon^2)$ 意义下相切。将 $\nu_L$ 到 $\nu_+$ 的状态分解为

$$
\nu_+ - \nu_L = \sum_{k=1}^n \varepsilon_k r_k(\nu_L) + O(|\varepsilon|^2),
$$

可依次选取每个波的强度 $\varepsilon_k$，使中间状态 $\nu_1,\dots,\nu_{n-1}$ 唯一确定。对真非线性场，根据 $\varepsilon_k$ 的符号选择激波或稀疏波。

### 4.3 Lax 熵条件保证唯一性

在每一场中附加 Lax 熵条件可排除非物理的膨胀激波，确保每个波的选取唯一，从而整个 Riemann 解唯一。

## 五、应用与意义

Riemann 问题的精确解是构造高分辨率守恒律数值方法（如 Godunov 格式、近似 Riemann 解法器）的基石。它将复杂的非线性波相互作用分解为局部可解析的激波、稀疏波和接触间断，极大地推动了可压缩流体力学和交通流模型的数值模拟。对 Riemann 解结构的深入理解也为研究一般 Cauchy 问题的 BV 解、激波稳定性等提供了范式。
