# Gauss绝妙定理

> **一句话大白话**：曲面的"弯曲度"（高斯曲率）其实是它内部测量的固有性质，跟怎样放进空间、怎样形变（保方式地弯折）无关——面不改色地揉曲面，高斯曲率岿然不动。
>
> **小例子**：把一张纸卷成圆筒（等距变形），它的高斯曲率始终为 $0$；因为无论怎么弯折，曲率只依赖"贴在身上"的度量，而圆筒的内禀度量与原纸完全相同——这就是"绝妙"之处。

## 介绍

Gauss绝妙定理（Theorema Egregium）是微分几何史上最深刻的定理之一，由 Carl Friedrich Gauss 在 1827 年发表，他称之为"绝妙定理"。定理断言：曲面的 Gauss 曲率完全由第一基本形式（即度量）决定，而不依赖于曲面在 $\mathbb{R}^3$ 中的嵌入方式。换言之，Gauss 曲率是内蕴几何量——曲面上居住的二维生物可以不借助外部空间而测量出曲面的弯曲程度。这个定理是 Riemann 几何发展的先声，也是内蕴几何学的开端。

## 分析

**前置依赖**：第一基本形式、第二基本形式与 Weingarten 变换、Christoffel 符号、Gauss 公式与可积条件

**定理的精确表述**：设 $S \subset \mathbb{R}^3$ 是光滑曲面，其第一基本形式为 $I = E du^2 + 2F du dv + G dv^2$，第二基本形式为 $II = L du^2 + 2M du dv + N dv^2$。则 Gauss 曲率

$$
K = \frac{LN - M^2}{EG - F^2}
$$

可以仅用第一基本形式的系数 $E, F, G$ 及其一阶、二阶偏导数表示，即

$$
K = \frac{1}{(EG - F^2)^2} \left[ \begin{vmatrix} -\frac{1}{2}E_{vv} + F_{uv} - \frac{1}{2}G_{uu} & \frac{1}{2}E_u & F_u - \frac{1}{2}E_v \\ F_v - \frac{1}{2}G_u & E & F \\ \frac{1}{2}G_v & F & G \end{vmatrix} - \begin{vmatrix} 0 & \frac{1}{2}E_v & \frac{1}{2}G_u \\ \frac{1}{2}E_v & E & F \\ \frac{1}{2}G_u & F & G \end{vmatrix} \right].
$$

**更简洁的形式**：使用 Christoffel 符号，Gauss 曲率可表示为

$$
K = \frac{1}{EG - F^2} \left( (\Gamma_{22}^1)_u - (\Gamma_{12}^1)_v + \Gamma_{22}^2 \Gamma_{11}^1 + \Gamma_{22}^1 \Gamma_{12}^2 - \Gamma_{12}^2 \Gamma_{21}^1 - \Gamma_{12}^1 \Gamma_{22}^2 \right),
$$

其中 $\Gamma_{ij}^k$ 是第一基本形式确定的 Christoffel 符号。

**关键要点**：

- 定理的"绝妙"之处在于，Gauss 曲率 $K$ 虽然定义为 $K = \det(II)/\det(I)$，但它实际上只依赖于第一基本形式。
- 这意味着 Gauss 曲率是内蕴量——在曲面的等距变换下保持不变。
- 推论：无法在不改变 Gauss 曲率的情况下将球面映射到平面（即地图投影必然存在畸变）。
- 这个定理标志着内蕴几何的诞生，为 Riemann 几何奠定了基础。

## 思考过程

Gauss 绝妙定理的证明涉及对曲面的 Gauss 映射和 Weingarten 变换的深入分析：

1. Gauss 曲率定义为 $K = \det(W)$，其中 $W = I^{-1} II$ 是 Weingarten 变换。

2. 直接计算 $K = \frac{LN - M^2}{EG - F^2}$ 依赖于第二基本形式，但可以通过 Gauss 方程（Codazzi-Mainardi 方程的一部分）将 $LN - M^2$ 用第一基本形式表示。

3. Gauss 方程是曲面论的基本方程之一，它来源于 $\mathbf{r}_{uuv} = \mathbf{r}_{uvu}$ 和 $\mathbf{r}_{uvv} = \mathbf{r}_{vvu}$ 的可积条件。

4. 这个推导揭示了内蕴几何量与外在几何量的深刻联系。

## 证明过程

**证明**：我们对 Gauss 绝妙定理给出证明概要。

**步骤 1**：曲面基本方程。$\mathbf{r}_{uu}$、$\mathbf{r}_{uv}$、$\mathbf{r}_{vv}$ 可以表示为 $\mathbf{r}_u$、$\mathbf{r}_v$ 和 $\mathbf{n}$ 的线性组合（Gauss 公式）：

$$
\begin{aligned}
\mathbf{r}_{uu} &= \Gamma_{11}^1 \mathbf{r}_u + \Gamma_{11}^2 \mathbf{r}_v + L \mathbf{n}, \\
\mathbf{r}_{uv} &= \Gamma_{12}^1 \mathbf{r}_u + \Gamma_{12}^2 \mathbf{r}_v + M \mathbf{n}, \\
\mathbf{r}_{vv} &= \Gamma_{22}^1 \mathbf{r}_u + \Gamma_{22}^2 \mathbf{r}_v + N \mathbf{n},
\end{aligned}
$$

其中 $\Gamma_{ij}^k$ 是第一基本形式确定的 Christoffel 符号：

$$
\Gamma_{11}^1 = \frac{GE_u - 2FF_u + FE_v}{2(EG - F^2)}, \quad \Gamma_{11}^2 = \frac{2EF_u - EE_v + FE_u}{2(EG - F^2)}, \quad \text{等}.
$$

**步骤 2**：可积条件。由 $\frac{\partial}{\partial v}(\mathbf{r}_{uu}) = \frac{\partial}{\partial u}(\mathbf{r}_{uv})$，代入 Gauss 公式并比较 $\mathbf{n}$ 的分量，得到 Gauss 方程：

$$
(LN - M^2) = \frac{1}{2} \left[ (E_u \Gamma_{22}^2)_v - (E_v \Gamma_{12}^2)_u + \cdots \right] \cdot (EG - F^2).
$$

通过冗长的计算，右侧可以用 $E, F, G$ 及其导数表示。

**步骤 3**：Gauss 曲率的内蕴表达式。由 $K = \frac{LN - M^2}{EG - F^2}$，利用 Gauss 方程将 $LN - M^2$ 用第一基本形式表示，得到

$$
K = \frac{1}{(EG - F^2)^2} \left[ \begin{vmatrix} -\frac{1}{2}E_{vv} + F_{uv} - \frac{1}{2}G_{uu} & \frac{1}{2}E_u & F_u - \frac{1}{2}E_v \\ F_v - \frac{1}{2}G_u & E & F \\ \frac{1}{2}G_v & F & G \end{vmatrix} - \begin{vmatrix} 0 & \frac{1}{2}E_v & \frac{1}{2}G_u \\ \frac{1}{2}E_v & E & F \\ \frac{1}{2}G_u & F & G \end{vmatrix} \right].
$$

**步骤 4**：等距不变性。由于 $K$ 仅依赖于 $E, F, G$ 及其导数，而 $E, F, G$ 在等距变换下不变（等距保持第一基本形式），故 $K$ 在等距变换下不变。$\square$

**推论**：球面不能等距映射到平面（因为球面有正 Gauss 曲率，而平面的 Gauss 曲率为零）。这解释了为什么地图投影总是存在面积或角度畸变。

**应用**：Gauss 绝妙定理奠定了内蕴几何学的基础，是 Riemann 在 1854 年开创 Riemann 几何的直接先驱。在现代微分几何中，Gauss 曲率是 Ricci 曲率（广义相对论的核心概念）在二维情形的特例。