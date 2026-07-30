# Gauss-Bonnet定理（局部形式）

## 介绍

Gauss-Bonnet 定理是微分几何中最深刻的结果之一，它建立了曲面的局部几何量（Gauss 曲率）与全局拓扑量（Euler 示性数）之间的深刻联系。局部形式的 Gauss-Bonnet 定理将曲面上测地三角形的 Gauss 曲率积分与三角形内角和联系起来，是经典 Gauss-Bonnet 定理在曲面片上的推广。这个定理是微分几何和拓扑学交叉的典范，也是 Chern 示性类理论的前驱。

## 分析

**定理的精确表述**：设 $S$ 是 $\mathbb{R}^3$ 中的光滑曲面，$D \subset S$ 是由 $k$ 条光滑曲线（或分段光滑曲线）围成的单连通区域，边界 $\partial D$ 由 $k$ 条测地线段组成，各内角为 $\alpha_1, \alpha_2, \ldots, \alpha_k$。则

$$
\iint_D K \, dA + \sum_{i=1}^k \int_{\partial D_i} \kappa_g \, ds + \sum_{i=1}^k (\pi - \alpha_i) = 2\pi,
$$

其中 $K$ 是 Gauss 曲率，$\kappa_g$ 是边界曲线的测地曲率，$dA$ 是曲面的面积元，$ds$ 是弧长元。

**测地三角形特例**：若 $D$ 是测地三角形（三条边都是测地线，即 $\kappa_g = 0$），则

$$
\iint_D K \, dA + \sum_{i=1}^3 (\pi - \alpha_i) = 2\pi,
$$

即 $\iint_D K \, dA = (\alpha_1 + \alpha_2 + \alpha_3) - \pi$。

**关键要点**：

- 测地三角形内角和与 $\pi$ 的偏差恰好等于三角形内部 Gauss 曲率的总和。
- 在正曲率曲面（如球面）上，测地三角形内角和大于 $\pi$。
- 在负曲率曲面（如双曲曲面）上，测地三角形内角和小于 $\pi$。
- 在零曲率曲面（如平面）上，测地三角形内角和等于 $\pi$。

## 思考过程

局部 Gauss-Bonnet 定理的证明基于对曲面上的向量场沿边界曲线的旋转指数分析：

1. 在曲面区域 $D$ 上取一个光滑的单位向量场 $e$，考虑 $e$ 沿边界曲线 $\partial D$ 的旋转指数。

2. 利用 Levi-Civita 联络，将 $e$ 沿边界曲线的协变导数与测地曲率联系起来。

3. 由 Gauss 曲率与向量场旋转的关系（Poincaré-Hopf 定理在曲面上的应用），得到积分关系。

4. 对测地多边形，边界贡献由测地曲率的积分和角偏折（外角）组成。

## 证明过程

**证明**：我们给出测地三角形情形的证明概要。

**步骤 1**：切向量场的旋转指数。在 $D$ 上取一个光滑的单位切向量场 $V$（例如，从某点出发的径向向量场的投影）。令 $\theta$ 为 $V$ 与边界曲线切向量的夹角。沿边界 $\partial D$，$V$ 的旋转指数为

$$
\frac{1}{2\pi} \oint_{\partial D} \frac{d\theta}{ds} \, ds = 1.
$$

**步骤 2**：分解旋转。$\frac{d\theta}{ds}$ 可以分解为两部分：

$$
\frac{d\theta}{ds} = \kappa_g + \frac{d\varphi}{ds},
$$

其中 $\kappa_g$ 是边界曲线的测地曲率，$\varphi$ 是边界曲线本身的切向量相对于某个参考方向的角度。由切向量的旋转指数公式，

$$
\oint_{\partial D} \frac{d\varphi}{ds} \, ds = 2\pi - \sum_{i=1}^3 (\pi - \alpha_i) = \sum_{i=1}^3 \alpha_i - \pi.
$$

**步骤 3**：应用 Gauss-Bonnet 关系。利用协变导数和曲率的关系，向量场 $V$ 沿边界旋转的积分可以转化为 Gauss 曲率在 $D$ 上的积分：

$$
\oint_{\partial D} \frac{d\theta}{ds} \, ds = \iint_D K \, dA + \oint_{\partial D} \kappa_g \, ds.
$$

**步骤 4**：合并结果。由步骤 1-3，

$$
2\pi = \iint_D K \, dA + \oint_{\partial D} \kappa_g \, ds + \sum_{i=1}^3 (\pi - \alpha_i).
$$

对于测地三角形，$\kappa_g = 0$，故

$$
\iint_D K \, dA = (\alpha_1 + \alpha_2 + \alpha_3) - \pi.
$$

$\square$

**推论**：在常曲率曲面 $K \equiv \text{const}$ 上，测地三角形的面积 $A$ 满足：
- 若 $K > 0$（球面），$A = ((\alpha_1 + \alpha_2 + \alpha_3) - \pi)/K$；
- 若 $K = 0$（平面），$\alpha_1 + \alpha_2 + \alpha_3 = \pi$；
- 若 $K < 0$（双曲曲面），$A = (\pi - (\alpha_1 + \alpha_2 + \alpha_3))/|K|$。