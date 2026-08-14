# Calderón-Zygmund 分解

## 一、定理介绍

Calderón-Zygmund 分解是调和分析中的基本工具，由 Alberto Calderón 和 Antoni Zygmund 于 1952 年引入。该分解将 $L^1$ 函数分解为"好部分"（$L^2$ 有界）和"坏部分"（具有 cancellation 性质），是研究奇异积分算子有界性的核心技术。

Calderón-Zygmund 分解在调和分析中的地位类似于实分析中的 Vitali 覆盖引理，它为弱型估计和插值定理提供了基础框架，是现代调和分析的基石之一。

## 二、原理思路

**核心思想**：对 $L^1$ 函数 $f$ 和给定高度 $\alpha > 0$，将 $f$ 分解为 $f = g + b$，其中：
- $g$（好函数）：$L^2$ 有界，$\|g\|_2^2 \leq C\alpha\|f\|_1$
- $b$（坏函数）：具有局部 cancellation 性质，支撑在测度小的集合上

**关键观察**：
1. 利用 Whitney 型覆盖引理，将 $\{|f| > \alpha\}$ 分解为不重叠的二进方体
2. 在每个方体上，$f$ 的平均值不超过 $C\alpha$
3. 好部分 $g$ 在每个方体上等于 $f$ 的平均值，因此 $L^\infty$ 有界
4. 坏部分 $b$ 在每个方体上积分为零，具有 cancellation 性质

**证明策略**：
- 使用二进方体的 Whitney 分解
- 利用方体上函数的平均值构造好部分和坏部分
- 通过 cancellation 性质控制坏部分的奇异积分

## 三、定理的严格表述

**定理（Calderón-Zygmund 分解）**：设 $f \in L^1(\mathbb{R}^n)$，$\alpha > 0$。则存在分解 $f = g + b$，满足：

1. **好部分**：$g \in L^2(\mathbb{R}^n)$，$\|g\|_\infty \leq 2^n \alpha$，且 $\|g\|_1 \leq \|f\|_1$

2. **坏部分**：$b = \sum_j b_j$，其中每个 $b_j$ 支撑在不重叠的二进方体 $Q_j$ 上，满足：
   - $\int_{Q_j} b_j(x) \, dx = 0$（cancellation 条件）
   - $\|b_j\|_1 \leq 2^{n+1} |Q_j| \alpha$
   - $\sum_j |Q_j| \leq \frac{\|f\|_1}{\alpha}$

3. **估计**：
   - $\|g\|_2^2 \leq 2^n \alpha \|f\|_1$
   - $\|b\|_1 \leq 2\|f\|_1$

**Whitney 分解引理**：设 $\Omega \subset \mathbb{R}^n$ 是开集。则存在可数个二进方体 $\{Q_j\}$ 使得：
1. $\Omega = \bigcup_j Q_j$（不重叠，至多边界相交）
2. $\text{diam}(Q_j) \leq d(Q_j, \Omega^c) \leq 4\text{diam}(Q_j)$

## 四、证明过程

**证明**：

**步骤 1**：定义水平集。令 $\Omega = \{x \in \mathbb{R}^n : Mf(x) > \alpha\}$，其中 $Mf$ 是 Hardy-Littlewood 极大函数。由弱型 $(1,1)$ 估计，$|\Omega| \leq \frac{C}{\alpha}\|f\|_1$。

实际上，更精确地，使用二进极大函数：令 $\Omega = \{x : M_d f(x) > \alpha\}$，其中 $M_d f(x) = \sup_{Q \ni x} \frac{1}{|Q|}\int_Q |f|$，$Q$ 取遍包含 $x$ 的二进方体。

**步骤 2**：Whitney 分解。对 $\Omega$ 应用二进 Whitney 分解：选取极大二进方体 $Q_j$ 使得 $\frac{1}{|Q_j|}\int_{Q_j} |f| > \alpha$。这些方体不重叠（若两个二进方体相交，则一个包含另一个，由极大性矛盾），且 $\Omega = \bigcup_j Q_j$。

由极大性，父方体 $\tilde{Q}_j$（边长是 $Q_j$ 的两倍）满足 $\frac{1}{|\tilde{Q}_j|}\int_{\tilde{Q}_j} |f| \leq \alpha$，因此
$$\frac{1}{|Q_j|}\int_{Q_j} |f| \leq \frac{2^n}{|\tilde{Q}_j|}\int_{\tilde{Q}_j} |f| \leq 2^n \alpha$$

**步骤 3**：构造分解。定义
$$g(x) = \begin{cases} f(x) & x \notin \Omega \\ \frac{1}{|Q_j|}\int_{Q_j} f(y) \, dy & x \in Q_j \end{cases}$$

$$b(x) = f(x) - g(x) = \sum_j b_j(x)$$
其中
$$b_j(x) = \left(f(x) - \frac{1}{|Q_j|}\int_{Q_j} f\right) \chi_{Q_j}(x)$$

**步骤 4**：验证好部分的性质。显然 $|g(x)| \leq |f(x)|$ 在 $\Omega^c$ 上，在 $Q_j$ 上 $|g(x)| \leq \frac{1}{|Q_j|}\int_{Q_j} |f| \leq 2^n \alpha$。因此 $\|g\|_\infty \leq 2^n \alpha$。

$$\|g\|_1 = \int_{\Omega^c} |f| + \sum_j \int_{Q_j} |g| \leq \int_{\Omega^c} |f| + \sum_j \int_{Q_j} |f| = \|f\|_1$$

$$\|g\|_2^2 \leq \|g\|_\infty \|g\|_1 \leq 2^n \alpha \|f\|_1$$

**步骤 5**：验证坏部分的性质。$\int b_j = \int_{Q_j} f - \int_{Q_j} f = 0$。

$$\|b_j\|_1 \leq \int_{Q_j} |f| + \int_{Q_j} |g| \leq 2\int_{Q_j} |f| \leq 2 \cdot 2^n \alpha |Q_j|$$

$$\sum_j |Q_j| = |\Omega| \leq \frac{\|f\|_1}{\alpha}$$

$$\|b\|_1 \leq \sum_j \|b_j\|_1 \leq 2\sum_j \int_{Q_j} |f| = 2\int_\Omega |f| \leq 2\|f\|_1$$

$\square$

**应用示例**：证明奇异积分算子 $T$ 的弱型 $(1,1)$ 估计。

设 $T$ 是 Calderón-Zygmund 奇异积分算子，核 $K$ 满足 $|K(x)| \leq C/|x|^n$ 和 Hölder 条件。对 $f \in L^1$，$\alpha > 0$，分解 $f = g + b$。

$$|\{x : |Tf(x)| > \alpha\}| \leq |\{x : |Tg(x)| > \alpha/2\}| + |\{x : |Tb(x)| > \alpha/2\}|$$

对好部分，由 Chebyshev 不等式和 $L^2$ 有界性：
$$|\{|Tg| > \alpha/2\}| \leq \frac{4}{\alpha^2}\|Tg\|_2^2 \leq \frac{4C}{\alpha^2}\|g\|_2^2 \leq \frac{C}{\alpha}\|f\|_1$$

对坏部分，利用 cancellation 和核的光滑性：
$$|\{|Tb| > \alpha/2\}| \leq \frac{2}{\alpha}\|Tb\|_{L^1(\Omega^*)} + |\Omega^*|$$
其中 $\Omega^* = \bigcup_j 3Q_j$。利用 cancellation 可以证明 $\|Tb\|_{L^1(\Omega^*)} \leq C\|f\|_1$。

## 五、应用与意义

Calderón-Zygmund 分解在现代分析中有广泛应用：

1. **奇异积分算子**：证明 Calderón-Zygmund 算子的弱型 $(1,1)$ 估计和 $L^p$ 有界性（$1 < p < \infty$）。

2. **极大算子**：建立 Hardy-Littlewood 极大算子的弱型估计。

3. **插值理论**：为 Marcinkiewicz 插值定理和 Riesz-Thorin 插值定理提供应用框架。

4. **PDE 正则性**：研究椭圆型和抛物型偏微分方程解的正则性。

5. **调和分析**：建立 Littlewood-Paley 理论、BMO 空间和 $H^1$ 空间的基本性质。

6. **加权估计**：推广到加权 $L^p$ 空间和 Muckenhoupt $A_p$ 权理论。

该分解的推广包括：连续 Calderón-Zygmund 分解、Cotlar-Stein 引理、以及 $T(1)$ 定理和 $T(b)$ 定理中的分解技术。
