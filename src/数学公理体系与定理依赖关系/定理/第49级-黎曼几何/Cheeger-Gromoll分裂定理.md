# Cheeger-Gromoll 分裂定理

> **一句话大白话**：一个"处处不往内弯"（Ricci ≥ 0）且包含一条能无限延长的测地线（直线）的完整流形，可以被"拆成"欧氏直线股 $\mathbb{R}\times$（更低维的另一块）——一条拉直的正曲率流形，"直接从直线处裂开"成乘积。
>
> **小例子**：圆柱 $\mathbb{R}\times S^1$ 的曲率为0（Ricci非负）且有一条沿轴向无限延伸的直线，Cheeger-Gromoll 正是把整体$M$写成分裂积 $\mathbb{R}\times M'$；有理据有直线就能"切一刀"成乘积结构。

## 一、定理介绍

Cheeger-Gromoll 分裂定理是 Riemann 几何中的基本定理，由 Jeff Cheeger 和 Detlef Gromoll 于 1971 年证明。该定理断言：若完备 Riemann 流形具有非负 Ricci 曲率且包含一条直线（即测地线在两个方向上都是最短的），则该流形等距同构于 Riemann 积 $\mathbb{R} \times N$。

分裂定理是比较几何的核心结果，与 Bonnet-Myers 定理、Cartan-Hadamard 定理一起构成了曲率与拓扑关系的完整图景。它在几何分析、广义相对论和群论中有重要应用。

## 二、原理思路

**核心思想**：非负 Ricci 曲率下，直线（totally geodesic line）的存在迫使流形分裂为积结构。

**关键观察**：
1. Busemann 函数：直线 $\gamma$ 定义两个 Busemann 函数 $b^+$ 和 $b^-$，它们的和 $b^+ + b^-$ 满足 $\Delta(b^+ + b^-) \leq 0$（由 Laplacian 比较定理）
2. 同时 $b^+ + b^- \geq 0$（由三角不等式），且在 $\gamma$ 上为零
3. 由强极大值原理，$b^+ + b^- \equiv 0$
4. 因此 $b^+$ 和 $b^-$ 是调和函数，且梯度为 1，水平集给出积分解

**证明策略**：
- 构造 Busemann 函数并建立 Laplacian 估计
- 应用 Laplacian 比较定理和强极大值原理
- 证明 Busemann 函数的水平集是全测地超曲面
- 通过梯度流构造等距同构

## 三、定理的严格表述

**定义（直线）**：Riemann 流形 $M$ 中的**直线**（line）是一条测地线 $\gamma: \mathbb{R} \to M$，使得对任意 $s, t \in \mathbb{R}$，$d(\gamma(s), \gamma(t)) = |s - t|$。即 $\gamma$ 在任意两点间都是最短路径。

**定义（Busemann 函数）**：设 $\gamma: [0, \infty) \to M$ 是射线（ray，即对任意 $t \geq 0$，$d(\gamma(0), \gamma(t)) = t$）。$\gamma$ 的 **Busemann 函数**定义为
$$b(x) = \lim_{t \to \infty} (d(x, \gamma(t)) - t)$$

**定理（Cheeger-Gromoll 分裂定理）**：设 $(M^n, g)$ 是完备 Riemann 流形，$\text{Ric} \geq 0$。若 $M$ 包含一条直线 $\gamma: \mathbb{R} \to M$，则 $M$ 等距同构于 Riemann 积 $\mathbb{R} \times N$，其中 $N$ 是 $(n-1)$ 维完备 Riemann 流形，$\text{Ric}_N \geq 0$。直线 $\gamma$ 对应于 $\mathbb{R} \times \{p\}$。

**推论**：

1. **紧致流形**：若 $M$ 紧致，$\text{Ric} \geq 0$，且 $\pi_1(M)$ 包含一条直线（在万有覆盖中），则万有覆盖 $\tilde{M} \cong \mathbb{R}^k \times N'$，其中 $N'$ 紧致。

2. **非负截面曲率**：若 $M$ 完备，截面曲率 $K \geq 0$，且 $M$ 包含直线，则 $M \cong \mathbb{R} \times N$。

3. **总曲率定理**：若 $M$ 完备，$\text{Ric} \geq 0$，则 $M$ 的端（end）数有限，且每个端是柱状的。

## 四、证明过程

**证明**：

**步骤 1**：Busemann 函数的定义。设 $\gamma: \mathbb{R} \to M$ 是直线。定义两条射线 $\gamma^+(t) = \gamma(t)$（$t \geq 0$）和 $\gamma^-(t) = \gamma(-t)$（$t \geq 0$）。对应的 Busemann 函数为
$$b^+(x) = \lim_{t \to \infty} (d(x, \gamma(t)) - t)$$
$$b^-(x) = \lim_{t \to \infty} (d(x, \gamma(-t)) - t)$$

**步骤 2**：基本性质。由三角不等式，
$$b^+(x) + b^-(x) \geq -d(\gamma(t), \gamma(-t)) + 2t = -2t + 2t = 0$$
（这里用了 $d(x, \gamma(t)) + d(x, \gamma(-t)) \geq d(\gamma(t), \gamma(-t)) = 2t$）

在 $\gamma(0)$ 处，$b^+(\gamma(0)) = 0$，$b^-(\gamma(0)) = 0$，因此 $(b^+ + b^-)(\gamma(0)) = 0$。

**步骤 3**：Laplacian 比较。在分布意义下，由 Laplacian 比较定理（$\text{Ric} \geq 0$），
$$\Delta b^+ \leq 0, \quad \Delta b^- \leq 0$$
（Busemann 函数是半凹的，其 Laplacian 在支撑函数意义下有上界）

因此 $\Delta(b^+ + b^-) \leq 0$，即 $b^+ + b^-$ 是上调和函数（superharmonic）。

**步骤 4**：强极大值原理。$b^+ + b^-$ 是上调和函数，在 $\gamma(0)$ 处达到最小值 0。由强极大值原理，$b^+ + b^- \equiv 0$。

**步骤 5**：调和性。由于 $b^+ + b^- = 0$，$b^+ = -b^-$。又 $\Delta b^+ \leq 0$ 且 $\Delta b^- \leq 0$，因此 $\Delta b^+ = 0$，$b^+$ 是调和函数。

**步骤 6**：梯度为 1。Busemann 函数是 1-Lipschitz 的：$|\nabla b^+| \leq 1$。由于 $b^+$ 调和且非常数，由 Hopf 引理，$|\nabla b^+| > 0$。

更精细的论证：在 $\gamma$ 上，$b^+(\gamma(t)) = -t$，因此 $|\nabla b^+| = 1$。由 Bochner 公式和 $\text{Ric} \geq 0$，
$$\frac{1}{2}\Delta |\nabla b^+|^2 = |\text{Hess}(b^+)|^2 + \langle \nabla b^+, \nabla \Delta b^+ \rangle + \text{Ric}(\nabla b^+, \nabla b^+)$$
由于 $\Delta b^+ = 0$ 和 $\text{Ric} \geq 0$，
$$\frac{1}{2}\Delta |\nabla b^+|^2 \geq |\text{Hess}(b^+)|^2 \geq 0$$
因此 $|\nabla b^+|^2$ 是次调和函数。由于 $|\nabla b^+| \leq 1$ 且在 $\gamma$ 上等于 1，由强极大值原理，$|\nabla b^+| \equiv 1$。

**步骤 7**：Hessian 为零。由上述 Bochner 公式和 $|\nabla b^+| = 1$（常数），
$$0 = \frac{1}{2}\Delta |\nabla b^+|^2 \geq |\text{Hess}(b^+)|^2$$
因此 $\text{Hess}(b^+) = 0$，即 $b^+$ 的梯度场 $\nabla b^+$ 是平行的（parallel vector field）。

**步骤 8**：积分解。设 $V = \nabla b^+$。$V$ 是单位平行向量场，因此其积分曲线是测地线。水平集 $N = b^{-1}(0)$ 是全测地超曲面（因为 $\text{Hess}(b^+) = 0$）。

定义映射 $\Phi: \mathbb{R} \times N \to M$ 为 $\Phi(t, p) = \phi_t(p)$，其中 $\phi_t$ 是 $V$ 的流。由于 $V$ 是平行的，$\Phi$ 是等距同构。$\square$

## 五、应用与意义

Cheeger-Gromoll 分裂定理在多个领域有重要应用：

1. **比较几何**：与 Bonnet-Myers 定理（正 Ricci 曲率蕴含紧致）和 Cartan-Hadamard 定理（非正截面曲率蕴含万有覆盖可缩）一起，构成曲率-拓扑关系的完整图景。

2. **流形分类**：用于研究非负曲率流形的结构，如 Soul 定理（非负曲率非紧流形收缩到 Soul）。

3. **广义相对论**：在时空的奇点定理和正质量定理中有应用。

4. **群论**：用于研究具有非负曲率的完备流形的基本群的结构。

5. **几何流**：Ricci 流中的分裂定理类似结果用于研究流形的分解。

6. **刚性定理**：分裂定理的加强形式（如几乎分裂定理）研究曲率接近非负时流形的结构。

分裂定理的推广包括：Lorentz 分裂定理（广义相对论中的时空分裂）、几乎分裂定理（Gromov-Hausdorff 收敛意义下）、以及 orbifold 和度量空间上的分裂定理。
