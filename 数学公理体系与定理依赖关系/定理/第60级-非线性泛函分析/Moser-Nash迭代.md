# Moser-Nash迭代

## 一、定理介绍

Moser-Nash 迭代（Moser-Nash Iteration）是由 Jürgen Moser（1960-61，用于证明 KAM 定理与紧 Riemann 流形上 Hörmander 的次椭圆估计）与 John Nash（1958，用于证明椭圆方程解的 $C^{1,\alpha}$ 正则性）独立发展的一种正则性提升方法。该方法通过交替使用 Sobolev 嵌入与能量估计，将解的"低阶可积性"逐次提升为"高阶可积性"或"逐点正则性"。

Moser 迭代成为现代偏微分方程理论中证明弱解有界性、Hölder 连续性、Harnack 不等式与正则性提升的核心技术，被 De Giorgi、Stampacchia 等进一步发展，构成所谓 De Giorgi-Nash-Moser 理论。其思想也深刻影响了几何分析、调和分析、随机分析等领域。

## 二、原理思路

Moser-Nash 迭代的核心思想可以概括为：

1. **能量估计**：将非线性或退化方程的解代入适当检验函数，得到关于 $L^p$ 范数的递推不等式：
$$\|u\|_{L^{p_{n+1}}} \leq C^{1/p_n} \cdot \left(\frac{p_n}{\delta}\right)^{\alpha/p_n} \cdot \|u\|_{L^{p_n}}.$$

2. **指标迭代**：取指标序列 $p_0 < p_1 < p_2 < \cdots \to \infty$（通常几何增长 $p_{n+1} = \kappa p_n$），反复应用能量估计。

3. **可和性**：通过乘积 $\prod_n C^{1/p_n}$ 与 $\prod_n (p_n)^{\alpha/p_n}$ 的收敛性（由 $\sum 1/p_n < \infty$ 与 $\sum \log p_n / p_n < \infty$ 保证），得到一致 $L^\infty$ 界。

4. **Hölder 正则性**：通过对振荡的迭代控制（而非仅范数），证明解的 Hölder 连续性。

5. **Nash 的思想**：通过"熵"与"能量"双指标的同时估计，证明解的 Hölder 正则性。Moser 则更直接地基于 Sobolev 嵌入迭代 $L^p$ 估计。

## 三、定理的严格表述

考虑散度型椭圆方程
$$-\operatorname{div}(A(x) \nabla u) = 0 \quad \text{in } \Omega \subset \mathbb{R}^n,$$
其中 $A(x)$ 是一致椭圆矩阵：存在 $\lambda, \Lambda > 0$ 使
$$\lambda |\xi|^2 \leq \xi^T A(x) \xi \leq \Lambda |\xi|^2, \quad \forall x \in \Omega, \xi \in \mathbb{R}^n.$$

**Moser 迭代定理（局部有界性）**：设 $u \in H^1_{\text{loc}}(\Omega)$ 是方程的弱解（或下解），则对任意紧子集 $K \Subset \Omega$，
$$\|u^+\|_{L^\infty(K)} \leq C(n, \lambda, \Lambda, K, \Omega) \|u^+\|_{L^2(\Omega)}.$$

**Moser 迭代定理（Harnack 不等式）**：设 $u \in H^1_{\text{loc}}(\Omega)$ 是方程的非负弱解，则存在 $C = C(n, \lambda/\Lambda)$ 使得对任意球 $B_{2R}(x_0) \subset \Omega$，
$$\sup_{B_R(x_0)} u \leq C \inf_{B_R(x_0)} u.$$

**De Giorgi-Nash-Moser 定理（Hölder 正则性）**：方程的弱解 $u$ 在 $\Omega$ 上局部 Hölder 连续，即对任意紧子集 $K \Subset \Omega$，存在 $\alpha = \alpha(n, \lambda/\Lambda) \in (0,1)$ 与 $C > 0$ 使
$$|u(x) - u(y)| \leq C |x - y|^\alpha, \quad \forall x, y \in K.$$

**Nash 的形式（更一般退化椭圆方程）**：考虑退化椭圆方程
$$\operatorname{div}(a^{ij}(x) \partial_j u) = 0,$$
其中系数 $a^{ij}$ 满足一致椭圆条件但不要求光滑。Nash 证明解是 Hölder 连续的，且获得了 Hölder 指数与系数的显式估计。

## 四、证明过程

下面给出 Moser 迭代证明局部有界性的核心步骤。

**步骤 1：$L^p$ 能量估计**

设 $u$ 是非负下解（即 $-\operatorname{div}(A\nabla u) \leq 0$）。取检验函数 $\varphi = u^{p-1} \eta^{2p}$（其中 $p \geq 1$，$\eta$ 是截断函数），代入弱形式：
$$\int_\Omega \nabla u^T A \nabla(u^{p-1}\eta^{2p})\, dx \leq 0.$$
计算：
$$\nabla(u^{p-1}\eta^{2p}) = (p-1) u^{p-2} \eta^{2p} \nabla u + 2p u^{p-1} \eta^{2p-1} \nabla \eta.$$

经整理与 Young 不等式，可得（令 $v = u^{p/2}$）：
$$\int_\Omega |\nabla v|^2 \eta^{2p}\, dx \leq C p^2 \int_\Omega v^2 |\nabla \eta|^{2p}\, dx.$$

即
$$\|v \eta^p\|_{H^1}^2 \leq C p^2 \int_\Omega v^2 |\nabla \eta|^{2p}\, dx.$$

**步骤 2：Sobolev 嵌入**

由 Sobolev 嵌入定理（$H^1 \hookrightarrow L^{2^*}$，$2^* = 2n/(n-2)$），
$$\|v \eta^p\|_{L^{2^*}}^2 \leq C \|v \eta^p\|_{H^1}^2 \leq C p^2 \int_\Omega v^2 |\nabla \eta|^{2p}\, dx.$$

即
$$\|u^{p/2} \eta^p\|_{L^{2^*}}^2 \leq C p^2 \|u^{p/2} \eta^p\|_{L^2}^2 \cdot \|\nabla \eta\|_{L^\infty}^{2p}.$$

等价地，令 $q = p \cdot \frac{n}{n-2} = p \kappa$（$\kappa = n/(n-2) > 1$）：
$$\|u\|_{L^q(\operatorname{supp}\,\eta)} \leq (C q)^{2/q} \|u\|_{L^p(\operatorname{supp}\,\eta + \text{邻域})}.$$

**步骤 3：迭代指标序列**

取 $p_0 = 2$，$p_{k+1} = \kappa p_k$，即 $p_k = 2 \kappa^k$。取截断函数 $\eta_k$ 支撑在半径 $r_k = r_0 (1 + \kappa^{-k}) / 2$ 的球中，使得 $\eta_k$ 在更小的球 $r_{k+1}$ 上为 $1$。

应用能量估计得
$$\|u\|_{L^{p_{k+1}}(B_{r_{k+1}})} \leq (C p_k)^{2/p_k} \cdot \left(\frac{1}{r_k - r_{k+1}}\right)^{2n/p_k} \cdot \|u\|_{L^{p_k}(B_{r_k})}.$$

记 $\phi_k = \|u\|_{L^{p_k}(B_{r_k})}$，得递推：
$$\phi_{k+1} \leq (C' \kappa^k)^{2/p_k} \phi_k.$$

**步骤 4：乘积收敛性**

迭代得
$$\phi_k \leq \phi_0 \prod_{j=0}^{k-1} (C' \kappa^j)^{2/p_j}.$$

取对数：
$$\log \prod_{j=0}^\infty (C' \kappa^j)^{2/p_j} = \sum_{j=0}^\infty \frac{2}{p_j} \log(C' \kappa^j) = \sum_{j=0}^\infty \frac{2}{2 \kappa^j} \log(C' \kappa^j).$$

由于 $\sum_j 1/\kappa^j < \infty$ 与 $\sum_j j/\kappa^j < \infty$（因 $\kappa > 1$），上述级数收敛。设极限为 $M$，则
$$\limsup_{k \to \infty} \phi_k \leq e^M \phi_0.$$

由于 $p_k \to \infty$，$\limsup_k \phi_k = \|u\|_{L^\infty(B_{r_\infty})}$（其中 $r_\infty = r_0/2$）。

故
$$\|u\|_{L^\infty(B_{r_0/2})} \leq C \|u\|_{L^2(B_{r_0})}.$$

这正是局部 $L^\infty$ 界。$\square$

**步骤 5：Hölder 正则性（简述）**

通过同时控制局部极大值 $M_k$ 与极小值 $m_k$ 的衰减，并应用振荡估计
$$\operatorname{osc}_{B_{r_{k+1}}} u \leq \theta \operatorname{osc}_{B_{r_k}} u, \quad \theta \in (0, 1),$$
可证 $u$ 在某点附近 Hölder 连续，指数 $\alpha = -\log \theta / \log \rho$（其中 $\rho$ 是半径比）。

## 五、应用与意义

**理论意义**：

1. **正则性理论的支柱**：Moser-Nash 迭代是证明椭圆方程弱解正则性（Hölder 连续性、Harnack 不等式）的核心方法，与 De Giorgi 方法并列为正则性理论的两大支柱。

2. **非线性分析的基础工具**：方法可推广到 $p$-Laplace 方程、平均曲率方程、各向异性方程等非线性与退化问题。

3. **不依赖光滑性的正则性**：仅依赖系数的一致椭圆性，不要求系数光滑，是非光滑系数问题正则性的关键。

**应用领域**：

1. **二阶椭圆方程**：证明散度型与非散度型椭圆方程弱解的 Hölder 正则性与 Harnack 不等式。

2. **抛物方程**：热方程、抛物型 $p$-Laplace 方程弱解的正则性，对应 Moser 的抛物 Harnack 不等式。

3. **$p$-Laplace 方程**：退化椭圆方程 $-\operatorname{div}(|\nabla u|^{p-2} \nabla u) = 0$ 的正则性。

4. **极小曲面与几何测度论**：极小曲面方程解的正则性，几乎极小曲面的正则性。

5. **KAM 定理**：Moser 在 KAM 定理的证明中使用类似迭代方法处理小除数问题，是 KAM 理论的关键工具。

6. **调和映射与几何流**：调和映射、Ricci 流等几何分析问题中的正则性。

7. **随机分析**：扩散过程转移密度的正则性，热核估计。

**推广与发展**：
- **De Giorgi 偏差方法**：另一种证明弱解 Hölder 正则性的方法，与 Moser 迭代等价但思路不同。
- **Stampacchia 插值方法**：通过插值不等式证明正则性。
- **Krylov-Safonov 理论**：非散度型椭圆方程的 Harnack 不等式（基于 Alexandrov-Bakelman-Pucci 极值原理）。
- **DiBenedetto 的 $p$-Laplace 正则性理论**：将 Moser 迭代推广到退化与奇异方程。
