# Riemann曲率张量

> **一句话大白话**：用"先沿 $X$ 再沿 $Y$ 平行搬运，和逆着顺序搬，到底差出多少"来度量空间的弯曲——两个方向顺序一换就走样，这个走样量就是曲率。
>
> **小例子**：平面上沿任意方向先 $X$ 后 $Y$ 与先 $Y$ 后 $X$ 平移结果相同，曲率张量 $R=0$；在球面上则出现非零差，$R(X,Y)Z=\nabla_X\nabla_Y Z-\nabla_Y\nabla_X Z-\nabla_{[X,Y]}Z$ 精确量化"搬一圈方向转了多少角"。

## 介绍

Riemann曲率张量是 Riemann 几何中最重要的局部不变量，由 Bernhard Riemann 在 1854 年引入。它定量描述了 Riemann 流形在每一点处的弯曲程度，反映了 Levi-Civita 联络的非交换性。Riemann 曲率张量是截面曲率、Ricci 曲率和标量曲率的基础，在广义相对论中通过 Einstein 场方程与物质分布相联系。它是流形局部几何性质的完整刻画——曲率张量处处为零当且仅当流形局部等距于欧氏空间。

## 分析

**定义**：设 $(M, g)$ 是 Riemann 流形，$\nabla$ 是 Levi-Civita 联络。Riemann 曲率张量 $R$ 是 $(1,3)$-型张量场，定义为

$$
R(X, Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X, Y]} Z,
$$

其中 $X, Y, Z$ 是光滑向量场。

**坐标分量**：在局部坐标 $(x^1, \ldots, x^n)$ 下，$R(\partial_i, \partial_j)\partial_k = R_{ijk}^l \partial_l$，其中

$$
R_{ijk}^l = \partial_i \Gamma_{jk}^l - \partial_j \Gamma_{ik}^l + \Gamma_{jp}^l \Gamma_{ik}^p - \Gamma_{ip}^l \Gamma_{jk}^p.
$$

**全协变形式**：$R_{ijkl} = g_{lp} R_{ijk}^p$，满足对称性：

- $R_{ijkl} = -R_{jikl} = -R_{ijlk}$
- $R_{ijkl} = R_{klij}$
- $R_{ijkl} + R_{iklj} + R_{iljk} = 0$（第一 Bianchi 恒等式）

**关键要点**：

- $R(X, Y)Z$ 度量了沿 $X$ 和 $Y$ 方向平行移动一周后 $Z$ 的变化。
- 截面曲率 $K(\Pi) = \frac{g(R(X, Y)Y, X)}{g(X, X)g(Y, Y) - g(X, Y)^2}$ 是曲率张量的几何解释。
- 曲率张量满足 Bianchi 恒等式，这些恒等式在广义相对论中对应于能量-动量守恒。
- $\mathbb{R}^n$ 的曲率张量为零（因为 $\Gamma_{ij}^k = 0$）。

## 思考过程

Riemann 曲率张量的引入源于对平行移动非交换性的观察：

1. 在欧氏空间中，沿不同路径平行移动同一向量，结果相同——平行移动与路径无关。

2. 在弯曲空间中，沿一个小环路平行移动向量，返回后向量方向会发生变化。这个变化正比于环路所围区域的曲率。

3. 通过计算沿坐标方向平行移动的交换子，即 $[\nabla_X, \nabla_Y]Z - \nabla_{[X,Y]}Z$，得到曲率张量。

4. 曲率张量完全刻画了流形的局部弯曲性质，是截面曲率、Ricci 曲率等导出量的基础。

## 证明过程

**基本性质**：

**1. 对称性**：Riemann 曲率张量满足以下对称性：

$$
R(X, Y)Z = -R(Y, X)Z,
$$
$$
g(R(X, Y)Z, W) = -g(R(X, Y)W, Z),
$$
$$
g(R(X, Y)Z, W) = g(R(Z, W)X, Y),
$$
$$
R(X, Y)Z + R(Y, Z)X + R(Z, X)Y = 0.
$$

**证明**：前两个对称性从定义直接可得。第三个对称性（交换对称性）需要利用度量相容性和无挠性。第四个是第一 Bianchi 恒等式，证明如下：

由无挠性，$[X, Y] = \nabla_X Y - \nabla_Y X$，代入曲率定义：

$$
R(X, Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{\nabla_X Y} Z + \nabla_{\nabla_Y X} Z.
$$

轮换 $(X, Y, Z)$ 并相加，利用 $\nabla$ 的对称性和 Jacobi 恒等式，可得结果为零。$\square$

**2. 第一 Bianchi 恒等式**：

$$
R(X, Y)Z + R(Y, Z)X + R(Z, X)Y = 0.
$$

**3. 第二 Bianchi 恒等式**：

$$
(\nabla_W R)(X, Y)Z + (\nabla_X R)(Y, W)Z + (\nabla_Y R)(W, X)Z = 0.
$$

**截面曲率**：对 $p \in M$ 和二维子空间 $\Pi \subset T_p M$，截面曲率定义为

$$
K(\Pi) = \frac{g(R(v, w)w, v)}{g(v, v)g(w, w) - g(v, w)^2},
$$

其中 $\{v, w\}$ 是 $\Pi$ 的任意基。$K(\Pi)$ 与基的选取无关，且完全确定了 Riemann 曲率张量。

**Ricci 曲率**：Ricci 曲率张量是 Riemann 曲率张量的迹：

$$
\operatorname{Ric}(X, Y) = \operatorname{tr}(Z \mapsto R(Z, X)Y) = \sum_{i=1}^n g(R(e_i, X)Y, e_i),
$$

其中 $\{e_i\}$ 是正交规范基。在坐标下，$R_{ij} = R_{ikj}^k = g^{kl} R_{kijl}$。

**标量曲率**：$R = g^{ij} R_{ij} = \operatorname{tr}_g(\operatorname{Ric})$。

**应用**：在广义相对论中，Einstein 场方程为 $\operatorname{Ric} - \frac{1}{2} R g = 8\pi T$，其中 $T$ 是能量-动量张量，将时空曲率与物质分布联系起来。