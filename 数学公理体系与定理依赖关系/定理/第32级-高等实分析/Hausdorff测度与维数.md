# Hausdorff 测度与维数

## 一、定理介绍

Hausdorff 测度和 Hausdorff 维数是几何测度论中的基本概念，由 Felix Hausdorff 于 1919 年引入。它们为任意度量空间中的集合提供了精细的"大小"度量，能够区分传统 Lebesgue 测度无法区分的集合（如 Cantor 集、分形等）。

Hausdorff 维数是分形几何的核心概念，能够刻画自相似集合、随机分形和动力系统的不变集的复杂程度。与拓扑维数不同，Hausdorff 维数可以是分数，反映了集合的"粗糙度"和"不规则性"。

## 二、原理思路

**核心思想**：用直径小的集合覆盖目标集合，通过调整覆盖集合的直径的幂次来定义不同"维度"的测度。

**关键观察**：
1. 在 $\mathbb{R}^n$ 中，$k$ 维子集的 $k$ 维"体积"可以通过直径为 $\delta$ 的小球覆盖来近似
2. 当 $\delta \to 0$ 时，如果集合的"真实维数"小于 $s$，则 $s$ 维 Hausdorff 测度为 0
3. 如果集合的"真实维数"大于 $s$，则 $s$ 维 Hausdorff 测度为 $\infty$
4. Hausdorff 维数是使测度从 $\infty$ 跳到 0 的临界值

**证明策略**：
- 构造外测度并验证其 Carathéodory 条件
- 利用覆盖引理（如 Vitali 覆盖引理）建立测度的几何性质
- 通过质量分布原理（mass distribution principle）计算具体集合的维数

## 三、定理的严格表述

**定义（Hausdorff 测度）**：设 $(X, d)$ 是度量空间，$s \geq 0$。对 $\delta > 0$ 和 $E \subset X$，定义
$$\mathcal{H}_\delta^s(E) = \inf\left\{\sum_{i=1}^\infty (\text{diam}(U_i))^s : E \subset \bigcup_{i=1}^\infty U_i, \text{diam}(U_i) \leq \delta\right\}$$
其中 $\text{diam}(U) = \sup\{d(x, y) : x, y \in U\}$。

定义 $s$ 维 **Hausdorff 测度**为
$$\mathcal{H}^s(E) = \lim_{\delta \to 0} \mathcal{H}_\delta^s(E) = \sup_{\delta > 0} \mathcal{H}_\delta^s(E)$$

**定义（Hausdorff 维数）**：集合 $E$ 的 **Hausdorff 维数**定义为
$$\dim_H(E) = \inf\{s \geq 0 : \mathcal{H}^s(E) = 0\} = \sup\{s \geq 0 : \mathcal{H}^s(E) = \infty\}$$

**基本性质**：

1. **测度性质**：$\mathcal{H}^s$ 是 Borel 正则外测度，所有 Borel 集都是 $\mathcal{H}^s$ 可测的。

2. **与 Lebesgue 测度的关系**：在 $\mathbb{R}^n$ 中，$\mathcal{H}^n = c_n \mathcal{L}^n$，其中 $c_n = \frac{\pi^{n/2}}{2^n \Gamma(n/2 + 1)}$ 是单位球的体积，$\mathcal{L}^n$ 是 Lebesgue 测度。

3. **单调性**：若 $E \subset F$，则 $\mathcal{H}^s(E) \leq \mathcal{H}^s(F)$，$\dim_H(E) \leq \dim_H(F)$。

4. **可数稳定性**：$\dim_H\left(\bigcup_{i=1}^\infty E_i\right) = \sup_i \dim_H(E_i)$。

5. **Lipschitz 不变性**：若 $f: X \to Y$ 是 Lipschitz 映射，则 $\dim_H(f(E)) \leq \dim_H(E)$。

**重要定理**：

- **质量分布原理**：若 $\mu$ 是 $E$ 上的概率测度，且存在 $C > 0$ 使得 $\mu(B(x, r)) \leq C r^s$ 对所有 $x \in E$ 和小 $r$ 成立，则 $\mathcal{H}^s(E) \geq 1/C > 0$，从而 $\dim_H(E) \geq s$。

- **Frostman 引理**：$\dim_H(E) \geq s$ 当且仅当存在 $E$ 上的非零 Borel 测度 $\mu$ 使得 $\mu(B(x, r)) \leq r^s$ 对所有 $x$ 和小 $r$ 成立。

## 四、证明过程

**定理**：$\mathcal{H}^s$ 是外测度。

**证明**：

**步骤 1**：非负性和空集。显然 $\mathcal{H}^s(\emptyset) = 0$，$\mathcal{H}^s(E) \geq 0$。

**步骤 2**：单调性。若 $E \subset F$，则 $F$ 的任意 $\delta$-覆盖也是 $E$ 的 $\delta$-覆盖，因此 $\mathcal{H}_\delta^s(E) \leq \mathcal{H}_\delta^s(F)$，取极限得 $\mathcal{H}^s(E) \leq \mathcal{H}^s(F)$。

**步骤 3**：次可数可加性。设 $E \subset \bigcup_{j=1}^\infty E_j$。需要证明 $\mathcal{H}^s(E) \leq \sum_{j=1}^\infty \mathcal{H}^s(E_j)$。

若 $\sum \mathcal{H}^s(E_j) = \infty$，结论显然成立。假设 $\sum \mathcal{H}^s(E_j) < \infty$。

对任意 $\varepsilon > 0$ 和每个 $j$，存在 $\delta$-覆盖 $\{U_{j,i}\}_{i=1}^\infty$ 使得 $E_j \subset \bigcup_i U_{j,i}$，$\text{diam}(U_{j,i}) \leq \delta$，且
$$\sum_{i=1}^\infty (\text{diam}(U_{j,i}))^s \leq \mathcal{H}_\delta^s(E_j) + \frac{\varepsilon}{2^j}$$

则 $\{U_{j,i}\}_{j,i}$ 是 $E$ 的 $\delta$-覆盖，因此
$$\mathcal{H}_\delta^s(E) \leq \sum_{j=1}^\infty \sum_{i=1}^\infty (\text{diam}(U_{j,i}))^s \leq \sum_{j=1}^\infty \left(\mathcal{H}_\delta^s(E_j) + \frac{\varepsilon}{2^j}\right) \leq \sum_{j=1}^\infty \mathcal{H}^s(E_j) + \varepsilon$$

令 $\varepsilon \to 0$，得 $\mathcal{H}_\delta^s(E) \leq \sum \mathcal{H}^s(E_j)$。再令 $\delta \to 0$，得 $\mathcal{H}^s(E) \leq \sum \mathcal{H}^s(E_j)$。$\square$

**定理**：所有 Borel 集是 $\mathcal{H}^s$ 可测的（Carathéodory 条件）。

**证明思路**：需要证明对任意 $A \subset X$ 和 Borel 集 $B$，
$$\mathcal{H}^s(A) \geq \mathcal{H}^s(A \cap B) + \mathcal{H}^s(A \setminus B)$$

由于 Borel $\sigma$-代数由闭集生成，只需对闭集 $B$ 验证。设 $d(A \cap B, A \setminus B) = d > 0$（因为 $B$ 闭）。

对 $\delta < d/2$，$A$ 的任意 $\delta$-覆盖 $\{U_i\}$ 中，每个 $U_i$ 至多与 $A \cap B$ 和 $A \setminus B$ 之一相交。因此可以将覆盖分为两部分：$\{U_i\}$ 中与 $A \cap B$ 相交的覆盖 $A \cap B$，其余的覆盖 $A \setminus B$。

因此 $\mathcal{H}_\delta^s(A) \geq \mathcal{H}_\delta^s(A \cap B) + \mathcal{H}_\delta^s(A \setminus B)$。令 $\delta \to 0$ 即得结论。$\square$

**定理**：在 $\mathbb{R}^n$ 中，$\mathcal{H}^n = c_n \mathcal{L}^n$。

**证明思路**：

1. 首先证明对立方体 $Q = [0, a]^n$，$\mathcal{H}^n(Q) = a^n$。
2. 利用覆盖引理：任意开集可以用几乎不重叠的立方体覆盖。
3. 通过平移和放缩不变性，证明 $\mathcal{H}^n$ 与 $\mathcal{L}^n$ 成比例。
4. 计算单位球的 Hausdorff 测度，确定比例常数 $c_n$。

具体细节涉及 Vitali 覆盖引理和等直径集的最大体积问题（等周不等式）。$\square$

**质量分布原理的证明**：

设 $\mu$ 是 $E$ 上的概率测度，$\mu(B(x, r)) \leq C r^s$。

对任意 $\delta$-覆盖 $\{U_i\}$，对每个 $U_i$，取 $x_i \in U_i \cap E$，则 $U_i \subset B(x_i, \text{diam}(U_i))$。

因此 $1 = \mu(E) \leq \sum \mu(U_i) \leq \sum \mu(B(x_i, \text{diam}(U_i))) \leq C \sum (\text{diam}(U_i))^s$。

取下确界，$\mathcal{H}_\delta^s(E) \geq 1/C$。令 $\delta \to 0$，$\mathcal{H}^s(E) \geq 1/C > 0$。$\square$

## 五、应用与意义

Hausdorff 测度和维数在多个数学分支中有重要应用：

1. **分形几何**：刻画 Cantor 集、Koch 曲线、Sierpinski 地毯等分形的维数。例如，三分 Cantor 集的 Hausdorff 维数是 $\ln 2 / \ln 3$。

2. **几何测度论**：研究极小曲面、Plateau 问题和rectifiable 集合的基础工具。

3. **动力系统**：刻画混沌吸引子、Julia 集和 Mandelbrot 集的维数。

4. **调和分析**：研究奇异测度、Riesz 位势和容量理论。

5. **数论**：研究 Diophantine 逼近中例外集的维数（如 Jarník-Besicovitch 定理）。

6. **概率论**：Brown 运动轨迹的 Hausdorff 维数几乎必然为 2。

7. **偏微分方程**：研究奇点集的维数和正则性。

Hausdorff 维数与 Box 维数、填充维数等其他分形维数有密切联系，但具有更好的测度论性质（如可数稳定性）。
