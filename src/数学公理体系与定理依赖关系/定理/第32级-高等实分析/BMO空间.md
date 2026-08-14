# BMO 空间

## 一、定理介绍

BMO（Bounded Mean Oscillation，有界平均振荡）空间由 John 和 Nirenberg 于 1961 年引入，是调和分析中的重要函数空间。BMO 空间包含 $L^\infty$，同时是许多奇异积分算子的自然目标空间。

BMO 空间在调和分析、偏微分方程和复分析中扮演核心角色。它是 Hardy 空间 $H^1$ 的对偶空间（Fefferman 定理），在 Calderón-Zygmund 算子理论、椭圆 PDE 正则性理论和几何测度论中有广泛应用。

## 二、原理思路

**核心思想**：BMO 函数不一定有界，但其局部振荡是有界的。函数在每个方体上的平均值与函数值的偏差被一致控制。

**关键观察**：
1. $L^\infty$ 函数显然是 BMO 函数，但 BMO 包含无界函数（如 $\log|x|$）
2. BMO 函数的指数可积性（John-Nirenberg 不等式）：局部呈指数衰减
3. BMO 是 $H^1$ 的对偶，这建立了 Hardy 空间与 BMO 之间的深刻联系
4. Calderón-Zygmund 算子将 $L^\infty$ 映射到 BMO

**证明策略**：
- 利用方体上的平均值定义 BMO 半范数
- 通过 John-Nirenberg 不等式建立指数可积性
- 使用 Calderón-Zygmund 分解证明 $H^1$-$BMO$ 对偶性

## 三、定理的严格表述

**定义（BMO 空间）**：设 $f \in L^1_{\text{loc}}(\mathbb{R}^n)$。定义 $f$ 的 **BMO 半范数**为
$$\|f\|_{\text{BMO}} = \sup_Q \frac{1}{|Q|}\int_Q |f(x) - f_Q| \, dx$$
其中上确界取遍所有方体 $Q \subset \mathbb{R}^n$（边平行于坐标轴），$f_Q = \frac{1}{|Q|}\int_Q f(y) \, dy$ 是 $f$ 在 $Q$ 上的平均值。

**BMO 空间**定义为
$$\text{BMO}(\mathbb{R}^n) = \{f \in L^1_{\text{loc}}(\mathbb{R}^n) : \|f\|_{\text{BMO}} < \infty\}$$
模去常数函数后，$\|\cdot\|_{\text{BMO}}$ 成为范数，BMO 成为 Banach 空间。

**等价刻画**：
$$\|f\|_{\text{BMO}} \sim \sup_Q \left(\frac{1}{|Q|}\int_Q |f - f_Q|^2\right)^{1/2} \sim \sup_Q \left(\frac{1}{|Q|}\int_Q |f - f_Q|^p\right)^{1/p}$$
对任意 $1 \leq p < \infty$，这些定义给出等价的半范数。

**基本定理**：

1. **John-Nirenberg 不等式**：存在常数 $c_1, c_2 > 0$（仅依赖维数 $n$），使得对任意 $f \in \text{BMO}$、任意方体 $Q$ 和任意 $\lambda > 0$，
$$|\{x \in Q : |f(x) - f_Q| > \lambda\}| \leq c_1 |Q| e^{-c_2 \lambda / \|f\|_{\text{BMO}}}$$

2. **指数可积性**：存在 $\varepsilon_0 > 0$，使得对任意 $f \in \text{BMO}$ 和方体 $Q$，
$$\frac{1}{|Q|}\int_Q e^{\varepsilon_0 |f - f_Q| / \|f\|_{\text{BMO}}} \, dx \leq C$$

3. **Fefferman 对偶定理**：$(H^1(\mathbb{R}^n))^* \cong \text{BMO}(\mathbb{R}^n)$，即 Hardy 空间 $H^1$ 的对偶是 BMO。

4. **嵌入关系**：$L^\infty \subset \text{BMO} \subset L^p_{\text{loc}}$（任意 $1 \leq p < \infty$），且 $\|f\|_{\text{BMO}} \leq 2\|f\|_\infty$。

5. **Calderón-Zygmund 算子**：若 $T$ 是 Calderón-Zygmund 奇异积分算子，则 $T: L^\infty \to \text{BMO}$ 有界。

## 四、证明过程

**定理（John-Nirenberg 不等式）**：

**证明**：设 $f \in \text{BMO}$，$Q$ 是方体，$\lambda > 0$。

**步骤 1**：Calderón-Zygmund 分解。对 $|f - f_Q|$ 在 $Q$ 上作 Calderón-Zygmund 分解，取高度 $\alpha = C\|f\|_{\text{BMO}}$（$C$ 待选）。得到 $|f - f_Q| = g + b$，其中 $\|g\|_\infty \leq 2^n \alpha$，$b = \sum b_j$，$\int b_j = 0$，$\sum |Q_j| \leq \frac{1}{\alpha}\int_Q |f - f_Q| \leq \frac{|Q|}{\alpha}\|f\|_{\text{BMO}}$。

选取 $C$ 使得 $\frac{|Q|}{\alpha}\|f\|_{\text{BMO}} \leq \frac{|Q|}{2}$，即 $\alpha \geq 2\|f\|_{\text{BMO}}$。

**步骤 2**：估计水平集。令 $E_\lambda = \{x \in Q : |f(x) - f_Q| > \lambda\}$。

$$E_\lambda \subset \{|g| > \lambda/2\} \cup \{|b| > \lambda/2\}$$

由于 $\|g\|_\infty \leq 2^n \alpha$，若 $\lambda > 2^{n+1}\alpha$，则 $|\{|g| > \lambda/2\}| = 0$。

**步骤 3**：迭代论证。对 $b$ 的支撑方体 $Q_j$，在每个 $Q_j$ 上重复上述分解。由于 $\int_{Q_j} b_j = 0$，
$$\frac{1}{|Q_j|}\int_{Q_j} |f - f_Q| \leq \frac{1}{|Q_j|}\int_{Q_j} |f - f_{Q_j}| + |f_{Q_j} - f_Q|$$

由 BMO 定义，第一项 $\leq \|f\|_{\text{BMO}}$。第二项通过嵌套方体的平均值差控制：
$$|f_{Q_j} - f_Q| \leq \sum_{k=0}^{N-1} |f_{Q_{j,k+1}} - f_{Q_{j,k}}| \leq C N \|f\|_{\text{BMO}}$$

经过仔细迭代，可以得到几何级数衰减：
$$|E_\lambda \cap Q| \leq C|Q| 2^{-\lambda / (c\|f\|_{\text{BMO}})}$$

转化为指数形式即得 John-Nirenberg 不等式。$\square$

**定理（Fefferman 对偶定理）**：$(H^1)^* \cong \text{BMO}$。

**证明思路**：

**步骤 1**：构造对偶配对。对 $f \in \text{BMO}$ 和 $g \in H^1$（原子分解 $g = \sum \lambda_j a_j$），定义
$$\langle f, g \rangle = \sum_j \lambda_j \int f(x) a_j(x) \, dx$$

由于原子 $a_j$ 满足 cancellation 条件 $\int a_j = 0$，
$$\int f a_j = \int_{Q_j} (f - f_{Q_j}) a_j$$
因此
$$|\langle f, g \rangle| \leq \sum |\lambda_j| \|f\|_{\text{BMO}} \|a_j\|_\infty |Q_j| \leq C\|f\|_{\text{BMO}} \|g\|_{H^1}$$

**步骤 2**：证明每个 $H^1$ 的连续线性泛函由 BMO 函数给出。利用 $H^1$ 原子的结构和 Riesz 表示定理的推广。

**步骤 3**：证明映射是满射。利用 Calderón-Zygmund 分解和 BMO 的指数可积性。$\square$

## 五、应用与意义

BMO 空间在现代分析中有广泛应用：

1. **调和分析**：BMO 是奇异积分算子的自然目标空间。Calderón-Zygmund 算子将 $L^\infty$ 映射到 BMO，将 $H^1$ 映射到 $L^1$。

2. **PDE 理论**：在椭圆型偏微分方程的正则性理论中，BMO 出现在 Schauder 估计和 $W^{2,p}$ 估计的端点情形。

3. **复分析**：在 $\mathbb{C}^n$ 中，BMOA 是解析 BMO 空间，与 Hardy 空间 $H^2$ 有密切联系。

4. **几何测度论**：BMO 函数与 quasiconformal 映射、Teichmüller 空间有深刻联系。

5. **概率论**：BMO 与鞅论中的 BMO 鞅相对应，在随机分析中有应用。

6. **插值理论**：BMO 是 $L^\infty$ 和某些函数空间之间的插值空间。

7. **数论**：BMO 在加性数论和解析数论的某些问题中出现。

BMO 空间的重要推广包括：vmo（vanishing mean oscillation）、CBMO（中心 BMO）、以及加权 BMO 空间。
