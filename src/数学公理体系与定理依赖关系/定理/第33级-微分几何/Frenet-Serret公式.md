# Frenet-Serret公式

> **一句话大白话**：描述一条空间曲线怎样用"切向、法向、次法向"三个贴身标架旋转前进——曲线的弯（曲率）和拧（挠率）就是这个标架随弧长转动的速度。
>
> **小例子**：对单位速度曲线 $\gamma(s)$，记 $T=\gamma'$、$N=T'/|T'|$、$B=T\times N$，则 Frenet-Serret给出 $\frac{d}{ds}\begin{bmatrix}T\\N\\B\end{bmatrix}=\begin{bmatrix}0&\kappa&0\\ -\kappa&0&\tau\\0&-\tau&0\end{bmatrix}\begin{bmatrix}T\\N\\B\end{bmatrix}$，平面曲线 $\tau=0$、螺旋线两者皆非零。

## 介绍

Frenet-Serret公式是微分几何中刻画空间曲线几何性质的基本公式，由法国数学家 Frenet 和 Serret 在 19 世纪中叶独立提出。它描述了空间曲线上切向量、主法向量和副法向量（合称为 Frenet 标架）沿弧长参数的变化率，通过曲率和挠率两个几何量完整地刻画了曲线的局部形状。这个公式是曲线理论的基石，也是理解曲线局部几何性质的核心工具。

## 分析

**定理的精确表述**：设 $\gamma(s)$ 是 $\mathbb{R}^3$ 中以弧长 $s$ 为参数的正则曲线（$\|\gamma'(s)\| = 1$），且曲率 $\kappa(s) \neq 0$。定义 Frenet 标架：

- 切向量：$T(s) = \gamma'(s)$
- 主法向量：$N(s) = T'(s) / \|T'(s)\|$
- 副法向量：$B(s) = T(s) \times N(s)$

则 Frenet-Serret 公式为：

$$
\begin{aligned}
\frac{dT}{ds} &= \kappa N, \\
\frac{dN}{ds} &= -\kappa T + \tau B, \\
\frac{dB}{ds} &= -\tau N,
\end{aligned}
$$

其中 $\kappa(s) = \|T'(s)\|$ 是曲线在点 $\gamma(s)$ 处的曲率，$\tau(s) = -\langle B'(s), N(s) \rangle$ 是挠率。

**矩阵形式**：

$$
\frac{d}{ds} \begin{pmatrix} T \\ N \\ B \end{pmatrix} = \begin{pmatrix} 0 & \kappa & 0 \\ -\kappa & 0 & \tau \\ 0 & -\tau & 0 \end{pmatrix} \begin{pmatrix} T \\ N \\ B \end{pmatrix}.
$$

**关键要点**：

- $\kappa(s)$ 度量曲线偏离直线的程度，即切向量方向的变化率。
- $\tau(s)$ 度量曲线偏离平面的程度，即副法向量方向的变化率。
- 曲率 $\kappa \equiv 0$ 当且仅当曲线是直线；挠率 $\tau \equiv 0$ 当且仅当曲线是平面曲线。
- 曲线由曲率和挠率唯一确定（曲线论基本定理）。

## 思考过程

Frenet-Serret 公式的推导基于对正交标架求导的反对称性：

1. 由 $T$ 的定义，$T'$ 垂直于 $T$（因为 $\|T\| = 1$），定义 $\kappa = \|T'\|$，$N = T'/\kappa$，得 $T' = \kappa N$。

2. 对 $N$ 求导，$N'$ 可分解为 $T$、$N$、$B$ 方向的分量。由 $N \perp T$，$\langle N', T \rangle = -\langle N, T' \rangle = -\kappa$。

3. $\langle N', N \rangle = 0$（因为 $\|N\| = 1$），定义 $\tau = \langle N', B \rangle$，得 $N' = -\kappa T + \tau B$。

4. 对 $B = T \times N$ 求导，利用向量微积分的性质，得到 $B' = -\tau N$。

## 证明过程

**证明**：设 $\gamma(s)$ 是弧长参数化的正则曲线，$\kappa(s) > 0$。

**步骤 1**：定义 Frenet 标架。$T(s) = \gamma'(s)$，由于 $\|T(s)\| = 1$，$T'(s) \perp T(s)$。定义 $\kappa(s) = \|T'(s)\|$，$N(s) = T'(s)/\kappa(s)$。则 $T' = \kappa N$。

**步骤 2**：定义副法向量。$B(s) = T(s) \times N(s)$，则 $\{T(s), N(s), B(s)\}$ 构成右手系正交规范基。

**步骤 3**：求导 $N$。将 $N'$ 在 Frenet 标架下展开：

$$
N' = \langle N', T \rangle T + \langle N', N \rangle N + \langle N', B \rangle B.
$$

由 $\langle N, T \rangle = 0$，两边求导得 $\langle N', T \rangle + \langle N, T' \rangle = 0$，故 $\langle N', T \rangle = -\langle N, T' \rangle = -\langle N, \kappa N \rangle = -\kappa$。

由 $\|N\| = 1$，$\langle N', N \rangle = 0$。

定义 $\tau(s) = \langle N'(s), B(s) \rangle$，称为挠率。因此

$$
N' = -\kappa T + \tau B.
$$

**步骤 4**：求导 $B$。$B = T \times N$，求导得

$$
B' = T' \times N + T \times N' = (\kappa N) \times N + T \times (-\kappa T + \tau B) = 0 + \kappa (T \times T) + \tau (T \times B).
$$

由于 $T \times T = 0$，$T \times B = T \times (T \times N) = -N$（向量三重积公式），故 $B' = -\tau N$。

**步骤 5**：写出 Frenet-Serret 公式。将上述结果合并即得

$$
\frac{d}{ds} \begin{pmatrix} T \\ N \\ B \end{pmatrix} = \begin{pmatrix} 0 & \kappa & 0 \\ -\kappa & 0 & \tau \\ 0 & -\tau & 0 \end{pmatrix} \begin{pmatrix} T \\ N \\ B \end{pmatrix}.
$$

**步骤 6**：挠率的表达式。由 $B' = -\tau N$，且 $B = T \times N$，可得 $\tau$ 用 $\gamma$ 及其导数表示的公式：

$$
\tau = \frac{(\gamma' \times \gamma'') \cdot \gamma'''}{\kappa^2} = \frac{\det(\gamma', \gamma'', \gamma''')}{\|\gamma' \times \gamma''\|^2}.
$$

$\square$

**推论（曲线论基本定理）**：给定 $\kappa(s) > 0$ 和 $\tau(s)$，存在唯一的曲线（在等距变换意义下）以 $\kappa$ 和 $\tau$ 为曲率和挠率。