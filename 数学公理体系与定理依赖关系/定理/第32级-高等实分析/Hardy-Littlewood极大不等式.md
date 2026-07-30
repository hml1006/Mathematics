# Hardy-Littlewood极大不等式

## 介绍

Hardy-Littlewood极大不等式是调和分析和实分析中的基本不等式，由 G. H. Hardy 和 J. E. Littlewood 在 1930 年提出。它断言：函数 $f$ 的 Hardy-Littlewood 极大函数 $M f$ 的分布函数满足一个弱 $(1,1)$ 型不等式。这个不等式是 Lebesgue 微分定理证明的关键，也是奇异积分理论（如 Calderón-Zygmund 理论）的起点，在极大函数方法的发展中具有里程碑意义。

## 分析

**定义**：对局部可积函数 $f \in L^1_{\text{loc}}(\mathbb{R}^n)$，其 Hardy-Littlewood 极大函数定义为

$$
M f(x) = \sup_{r > 0} \frac{1}{|B(x, r)|} \int_{B(x, r)} |f(y)| \, dy,
$$

其中 $B(x, r)$ 是以 $x$ 为中心、半径为 $r$ 的球，$|B(x, r)|$ 是它的 Lebesgue 测度。

**定理的精确表述**：设 $f \in L^1(\mathbb{R}^n)$，则对任意 $\alpha > 0$，

$$
|\{x \in \mathbb{R}^n \mid M f(x) > \alpha\}| \le \frac{3^n}{\alpha} \|f\|_{L^1}.
$$

此外，对 $p > 1$，$M$ 是 $L^p$ 到 $L^p$ 的有界算子：

$$
\|M f\|_{L^p} \le C_p \|f\|_{L^p},
$$

其中 $C_p$ 是仅依赖于 $p$ 和维数 $n$ 的常数。

**关键要点**：

- 弱 $(1,1)$ 型不等式表明 $M f$ 几乎处处有限（对 $f \in L^1$ 而言）。
- $M f$ 一般不是 $L^1$ 可积的——弱 $(1,1)$ 型是 $L^1$ 情形下能得到的最佳结果。
- 对 $p > 1$，$M$ 在 $L^p$ 上有界，这通过 Marcinkiewicz 插值定理从弱 $(1,1)$ 型和 $L^\infty$ 有界性推出。
- 极大函数 $M f$ 是 Lebesgue 微分定理中"局部平均"的上确界，控制了函数的局部震荡。

## 思考过程

Hardy-Littlewood 极大不等式的证明利用 Vitali 覆盖引理：

1. **观察集合结构**：对 $\alpha > 0$，令 $E_\alpha = \{x \mid M f(x) > \alpha\}$。对每个 $x \in E_\alpha$，存在球 $B_x$ 包含 $x$ 使得 $\frac{1}{|B_x|} \int_{B_x} |f| > \alpha$。

2. **应用覆盖引理**：$\{B_x\}_{x \in E_\alpha}$ 是 $E_\alpha$ 的覆盖，由 Vitali 覆盖引理，存在不交子族 $\{B_j\}$ 使得 $E_\alpha \subset \bigcup_j 5B_j$（在零测集意义下）。

3. **测度估计**：$|E_\alpha| \le \sum_j |5B_j| = 5^n \sum_j |B_j| \le \frac{5^n}{\alpha} \sum_j \int_{B_j} |f| \le \frac{5^n}{\alpha} \|f\|_{L^1}$。

## 证明过程

**证明**：我们证明弱 $(1,1)$ 型不等式。设 $f \in L^1(\mathbb{R}^n)$，$\alpha > 0$，令 $E_\alpha = \{x \in \mathbb{R}^n \mid M f(x) > \alpha\}$。

**步骤 1**：对每个 $x \in E_\alpha$，由 $M f$ 的定义，存在 $r_x > 0$ 使得

$$
\frac{1}{|B(x, r_x)|} \int_{B(x, r_x)} |f(y)| \, dy > \alpha.
$$

令 $B_x = B(x, r_x)$，则 $\int_{B_x} |f| > \alpha |B_x|$。

**步骤 2**：$\{B_x\}_{x \in E_\alpha}$ 是 $E_\alpha$ 的覆盖。由 Vitali 覆盖引理（5 倍扩张版本），存在可数不交子族 $\{B_j\} \subset \{B_x\}$ 使得

$$
E_\alpha \subset \bigcup_{j=1}^\infty 5B_j \quad (\text{在零测集意义下}).
$$

**步骤 3**：测度估计。由 $\{B_j\}$ 的不交性，

$$
|E_\alpha| \le \sum_{j=1}^\infty |5B_j| = 5^n \sum_{j=1}^\infty |B_j|.
$$

由步骤 1 中的不等式，$|B_j| < \frac{1}{\alpha} \int_{B_j} |f|$，故

$$
|E_\alpha| \le \frac{5^n}{\alpha} \sum_{j=1}^\infty \int_{B_j} |f| \le \frac{5^n}{\alpha} \int_{\mathbb{R}^n} |f| = \frac{5^n}{\alpha} \|f\|_{L^1}.
$$

其中最后一个不等式利用了 $\{B_j\}$ 的不交性。$\square$

**$L^p$ 有界性**：对 $p > 1$，由 $M$ 的 $L^\infty$ 有界性（$\|M f\|_\infty \le \|f\|_\infty$）和弱 $(1,1)$ 型，通过 Marcinkiewicz 插值定理可得 $M$ 在 $L^p$ 上有界。

具体地，对任意 $f \in L^p$，令 $\lambda = \|f\|_p$，则

$$
\|M f\|_p^p = p \int_0^\infty \alpha^{p-1} |\{M f > \alpha\}| \, d\alpha \le p \int_0^\infty \alpha^{p-1} \min\left( \frac{C}{\alpha} \|f\|_1, \|f\|_\infty \right) d\alpha.
$$

通过适当的分解（将 $f$ 分解为 $|f| \le \alpha/2$ 和 $|f| > \alpha/2$ 两部分）可得 $\|M f\|_p \le C_p \|f\|_p$。$\square$

**应用**：Hardy-Littlewood 极大不等式是 Lebesgue 微分定理证明中的关键步骤——它给出了 $M f$ 的分布估计，从而可以证明 $f$ 的 Lebesgue 点几乎处处存在。此外，在奇异积分理论中，Calderón-Zygmund 分解和极大函数方法都依赖于这个不等式。