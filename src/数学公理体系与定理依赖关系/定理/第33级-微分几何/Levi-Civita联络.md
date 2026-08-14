# Levi-Civita联络

## 介绍

Levi-Civita联络是 Riemann 几何中最重要的结构之一，由 Tullio Levi-Civita 在 1917 年引入。它是在 Riemann 流形上唯一确定的无挠度量相容联络，提供了向量沿曲线平行移动的规范方式。Levi-Civita 联络是 Riemann 几何中所有微分运算（协变导数、曲率、测地线）的基础，也是广义相对论中协变导数的数学框架。

## 分析

**定义**：设 $(M, g)$ 是 Riemann 流形。$M$ 上的 Levi-Civita 联络 $\nabla$ 是唯一的仿射联络，满足：

1. **度量相容性**（$\nabla g = 0$）：$X(g(Y, Z)) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$，对所有向量场 $X, Y, Z$ 成立；
2. **无挠性**（对称性）：$\nabla_X Y - \nabla_Y X = [X, Y]$，对所有向量场 $X, Y$ 成立。

**Koszul 公式**：Levi-Civita 联络由以下公式唯一确定：

$$
2g(\nabla_X Y, Z) = X(g(Y, Z)) + Y(g(Z, X)) - Z(g(X, Y)) - g(X, [Y, Z]) + g(Y, [Z, X]) + g(Z, [X, Y]).
$$

**Christoffel 符号**：在局部坐标 $(x^1, \ldots, x^n)$ 下，$\nabla_{\partial_i} \partial_j = \Gamma_{ij}^k \partial_k$，其中

$$
\Gamma_{ij}^k = \frac{1}{2} g^{kl} \left( \partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij} \right).
$$

**关键要点**：

- 度量相容性意味着平行移动保持向量的长度和角度。
- 无挠性保证了协变导数的对称性，与坐标系的选取无关。
- Levi-Civita 联络是 Riemann 流形上"自然"的联络，由 Riemann 度量唯一确定。
- 在 $\mathbb{R}^n$ 中，Levi-Civita 联络就是通常的方向导数（$\Gamma_{ij}^k = 0$）。

## 思考过程

Levi-Civita 联络的引入源于对曲面上协变导数的几何直观：

1. 在 $\mathbb{R}^3$ 中的曲面上，曲面的切向量沿曲面上的曲线的导数并不一定在切平面内——需要将其投影到切平面上，得到协变导数。

2. 这个投影操作定义了曲面上的联络，它满足度量相容性（因为 $\mathbb{R}^3$ 中的导数是度量相容的，投影不破坏这一性质）和无挠性。

3. 抽象到 Riemann 流形上，由 Riemann 度量通过 Koszul 公式唯一确定满足这两个条件的联络。

## 证明过程

**存在性和唯一性**：我们证明 Levi-Civita 联络的存在性和唯一性。

**证明**：设 $(M, g)$ 是 Riemann 流形。

**唯一性**：假设存在满足度量相容性和无挠性的联络 $\nabla$。由度量相容性，

$$
X(g(Y, Z)) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z).
$$

类似地，

$$
Y(g(Z, X)) = g(\nabla_Y Z, X) + g(Z, \nabla_Y X),
$$
$$
Z(g(X, Y)) = g(\nabla_Z X, Y) + g(X, \nabla_Z Y).
$$

将前两式相加减去第三式，利用无挠性 $\nabla_X Y - \nabla_Y X = [X, Y]$ 等，得

$$
2g(\nabla_X Y, Z) = X(g(Y, Z)) + Y(g(Z, X)) - Z(g(X, Y)) - g(X, [Y, Z]) + g(Y, [Z, X]) + g(Z, [X, Y]).
$$

由于 $g$ 非退化，$\nabla_X Y$ 由上式唯一确定。故 $\nabla$ 唯一。

**存在性**：用 Koszul 公式定义 $\nabla_X Y$。需要验证：
1. 右边对 $Z$ 是线性的，且由 $g$ 的非退化性，确定了一个向量场 $\nabla_X Y$；
2. $\nabla_X Y$ 对 $X$ 是 $C^\infty(M)$-线性的，对 $Y$ 是 $\mathbb{R}$-线性的，且满足 Leibniz 法则；
3. $\nabla$ 满足无挠性和度量相容性。

验证无挠性：由 Koszul 公式，计算 $g(\nabla_X Y - \nabla_Y X - [X, Y], Z)$，利用对称性可得结果为零。

验证度量相容性：直接计算 $X(g(Y, Z)) - g(\nabla_X Y, Z) - g(Y, \nabla_X Z)$，利用 Koszul 公式可得结果为零。$\square$

**Christoffel 符号的推导**：在局部坐标中，令 $X = \partial_i$，$Y = \partial_j$，$Z = \partial_k$，则 $[\partial_i, \partial_j] = 0$，代入 Koszul 公式得

$$
2g(\nabla_{\partial_i} \partial_j, \partial_k) = \partial_i g_{jk} + \partial_j g_{ik} - \partial_k g_{ij}.
$$

设 $\nabla_{\partial_i} \partial_j = \Gamma_{ij}^l \partial_l$，则 $g(\nabla_{\partial_i} \partial_j, \partial_k) = \Gamma_{ij}^l g_{lk} = \Gamma_{ij}^l g_{lk}$，故

$$
\Gamma_{ij}^l g_{lk} = \frac{1}{2} (\partial_i g_{jk} + \partial_j g_{ik} - \partial_k g_{ij}).
$$

乘以逆度量 $g^{km}$ 得 $\Gamma_{ij}^m = \frac{1}{2} g^{km} (\partial_i g_{jk} + \partial_j g_{ik} - \partial_k g_{ij})$。$\square$