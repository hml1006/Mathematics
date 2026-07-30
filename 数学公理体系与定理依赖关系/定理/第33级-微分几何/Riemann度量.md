# Riemann度量

## 介绍

Riemann度量是 Riemann 几何的核心概念，由 Bernhard Riemann 在 1854 年的就职演讲《论几何学之基础假设》中引入。Riemann 度量是光滑流形上切空间内积的平滑选取，它使得流形上可以定义长度、角度、体积和曲率等几何概念。Riemann 度量的引入标志着从经典微分几何（研究 $\mathbb{R}^3$ 中的曲面）到现代 Riemann 几何（研究抽象流形）的根本性转变。

## 分析

**定义**：设 $M$ 是光滑流形。$M$ 上的 Riemann 度量 $g$ 是一个光滑的 $(0,2)$-型张量场，满足对每个 $p \in M$，$g_p: T_p M \times T_p M \to \mathbb{R}$ 是对称正定双线性形式。即：

1. **对称性**：$g_p(v, w) = g_p(w, v)$ 对所有 $v, w \in T_p M$ 成立；
2. **正定性**：$g_p(v, v) \ge 0$，且等号成立当且仅当 $v = 0$；
3. **光滑性**：对任意光滑向量场 $X, Y$，$g(X, Y)$ 是 $M$ 上的光滑函数。

**局部坐标表示**：在局部坐标 $(x^1, \ldots, x^n)$ 下，Riemann 度量可写为

$$
g = g_{ij}(x) \, dx^i \otimes dx^j,
$$

其中 $g_{ij}(x) = g(\partial_i, \partial_j)$ 是光滑函数，且矩阵 $(g_{ij})$ 对称正定。弧长微元为

$$
ds^2 = g_{ij} \, dx^i \, dx^j.
$$

**关键要点**：

- Riemann 度量使得流形成为度量空间——两点间的距离定义为连接它们的分段光滑曲线长度的下确界。
- 同一个流形上可以存在不同的 Riemann 度量（例如，球面上的标准度量与椭球面度量）。
- Riemann 度量诱导了 Levi-Civita 联络、Riemann 曲率张量等几何结构。
- 度量的概念可以推广到伪 Riemann 度量（如 Lorentz 度量），用于广义相对论。

## 思考过程

Riemann 度量的引入源于对抽象流形上几何测量的需求：

1. 在 $\mathbb{R}^3$ 中的曲面上，第一基本形式给出了切向量的内积，这是 Riemann 度量的原型。

2. Riemann 将这一概念推广到抽象流形上——在每个切空间上定义一个内积，且要求其光滑地依赖于基点。

3. 有了 Riemann 度量，就可以定义曲线的长度、切向量之间的夹角、区域的体积、测地线、曲率等几何概念。

4. 不同的度量选择会导致不同的几何——即使在同一个拓扑流形上。

## 证明过程

**基本性质**：

**1. 长度的定义**：设 $\gamma: [a, b] \to M$ 是分段光滑曲线，其长度为

$$
L(\gamma) = \int_a^b \sqrt{g_{\gamma(t)}(\gamma'(t), \gamma'(t))} \, dt = \int_a^b \sqrt{g_{ij}(\gamma(t)) \frac{d\gamma^i}{dt} \frac{d\gamma^j}{dt}} \, dt.
$$

**2. 距离函数**：定义 $d(p, q) = \inf\{L(\gamma) \mid \gamma \text{ 连接 } p \text{ 和 } q\}$。可以证明 $(M, d)$ 是度量空间，且拓扑与流形拓扑一致。

**3. 体积元**：Riemann 度量诱导了流形上的体积形式

$$
dV_g = \sqrt{\det(g_{ij})} \, dx^1 \wedge \cdots \wedge dx^n.
$$

**4. 等距变换**：两个 Riemann 流形 $(M, g)$ 和 $(N, h)$ 之间的微分同胚 $f: M \to N$ 称为等距，若 $f^* h = g$，即 $h_{f(p)}(df_p(v), df_p(w)) = g_p(v, w)$ 对所有 $p \in M$ 和 $v, w \in T_p M$ 成立。

**例子**：

- **Euclid 度量**：在 $\mathbb{R}^n$ 上，$g = \sum_{i=1}^n (dx^i)^2$，即 $g_{ij} = \delta_{ij}$。
- **球面度量**：在 $S^n$ 上，诱导度量来自 $\mathbb{R}^{n+1}$ 中的嵌入：$g = d\theta^2 + \sin^2\theta \, d\varphi^2$（对 $S^2$）。
- **双曲度量**：在 Poincaré 上半平面 $\mathbb{H}^2 = \{(x, y) \mid y > 0\}$ 上，$g = \frac{dx^2 + dy^2}{y^2}$。

**注**：Riemann 度量的存在性不是自动的——在紧致流形上，通过单位分解可以在任何光滑流形上构造 Riemann 度量。换言之，每个光滑流形都可以配备 Riemann 度量。