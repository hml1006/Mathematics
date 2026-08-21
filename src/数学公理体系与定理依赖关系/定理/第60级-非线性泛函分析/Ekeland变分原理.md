# Ekeland变分原理

> **一句话大白话**：就算一个函数找不到真正的"谷底"，也总能在谷底附近不远处找到一个"几乎谷底"——取值够小、且再往任意方向移动都近乎不降的点（近似临界点）。
>
> **小例子**：对完备度量空间上一下方有界泛函 $f$，任给 $\varepsilon>0$ 都存在点 $x$ 使 $f(x)\leq \inf f+\varepsilon$，且对一切 $y\neq x$ 有 $f(y)>f(x)-\varepsilon d(x,y)$。

## 一、定理介绍

> **前置依赖**：完备度量空间与 Cauchy 列收敛性、下半连续泛函与闭水平集、偏序关系与 Zorn 型论证、Fréchet 导数与 Banach 空间对偶。

Ekeland 变分原理（Ekeland's Variational Principle）由 Ivar Ekeland 于 1974 年提出，是现代变分分析中最基本的变分原理之一。它断言：在完备度量空间上，任意下方有界的下半连续泛函都存在"近似临界点"——即在指定精度内取值接近下确界且梯度（在度量意义下）几乎为零的点。

Ekeland 变分原理的重要性在于它**不依赖任何线性结构或紧性假设**，仅需完备性与下半连续性，因此在不可微变分、非凸优化、临界点理论中具有基础性地位，并可作为 Caristi 不动点定理、Bishop-Phelps 定理、山路引理等多个重要定理的推导基础。

## 二、原理思路

Ekeland 变分原理的核心思想可概括为：

1. **近似极小点的精化**：给定一个近似极小点，可以找到一个"更好"的近似点 $x_\varepsilon$，使得在该点附近所有其他点的函数值严格大于 $f(x_\varepsilon)$（最多加上小的距离惩罚）。

2. **距离惩罚技巧**：将原泛函 $f$ 与距离函数的 $\lambda$ 倍相加构造"扰动泛函"，使新泛函的极小化列稳定收敛。

3. **完备性的利用**：通过构造下降序列并利用完备性获得极限点，是 Cantor 对角线法与闭区间套定理在一般度量空间的推广。

4. **$\varepsilon$-临界点**：在 Banach 空间中，若 $f$ 可微，则原理给出 $\|f'(x_\varepsilon)\| \leq \varepsilon / \lambda$，从而获得近似临界点。

## 三、定理的严格表述

设 $(X, d)$ 是完备度量空间，$f: X \to \mathbb{R} \cup \{+\infty\}$ 是下方有界的下半连续泛函（即 $\inf_X f > -\infty$，且对所有 $\alpha \in \mathbb{R}$，$\{x \mid f(x) \leq \alpha\}$ 是闭集）。

设 $\varepsilon > 0$，$x_0 \in X$ 满足
$$f(x_0) \leq \inf_X f + \varepsilon.$$

则对任意 $\lambda > 0$，存在 $x_\varepsilon \in X$ 满足：

(i) $f(x_\varepsilon) \leq f(x_0)$；

(ii) $d(x_\varepsilon, x_0) \leq \lambda$；

(iii) **变分不等式**：对所有 $x \neq x_\varepsilon$，
$$f(x) > f(x_\varepsilon) - \frac{\varepsilon}{\lambda}\, d(x, x_\varepsilon).$$

**Banach 空间的可微形式**：若 $X$ 是 Banach 空间，$f \in C^1(X, \mathbb{R})$ 下方有界，则对任意 $\varepsilon > 0$，存在 $x_\varepsilon \in X$ 满足
$$f(x_\varepsilon) \leq \inf_X f + \varepsilon, \quad \|f'(x_\varepsilon)\|_{X^*} \leq \sqrt{\varepsilon}$$
（取 $\lambda = \sqrt{\varepsilon}$ 即可），即 $f$ 存在近似临界点序列。

## 四、证明过程

不失一般性设 $\inf_X f = 0$（否则考虑 $f - \inf_X f$）。

**步骤 1：构造偏序关系**

定义 $X$ 上的偏序 $\preccurlyeq$：
$$y \preccurlyeq x \iff f(y) + \frac{\varepsilon}{\lambda} d(x, y) \leq f(x).$$

容易验证：
- 自反性：$x \preccurlyeq x$；
- 反对称性：若 $x \preccurlyeq y$ 且 $y \preccurlyeq x$，则 $x = y$；
- 传递性：若 $z \preccurlyeq y$ 且 $y \preccurlyeq x$，由三角不等式可得 $z \preccurlyeq x$。

**步骤 2：构造下降序列**

从 $x_1 = x_0$ 出发。设已构造 $x_n$。令
$$S_n = \{y \in X \mid y \preccurlyeq x_n\}.$$
由于 $x_n \in S_n$，$S_n \neq \emptyset$。设
$$c_n = \inf_{y \in S_n} f(y),$$
取 $x_{n+1} \in S_n$ 满足
$$f(x_{n+1}) \leq c_n + \frac{\varepsilon}{\lambda \cdot 2^n}.$$

**步骤 3：估计序列性质**

由 $x_{n+1} \preccurlyeq x_n$，
$$\frac{\varepsilon}{\lambda} d(x_n, x_{n+1}) \leq f(x_n) - f(x_{n+1}),$$
故 $f(x_n)$ 单调下降，且 $d(x_n, x_{n+1})$ 可被 $f(x_n) - f(x_{n+1})$ 控制。

将上式从 $n$ 到 $m-1$ 求和（$m > n$）：
$$\frac{\varepsilon}{\lambda} d(x_n, x_m) \leq \sum_{k=n}^{m-1} \frac{\varepsilon}{\lambda} d(x_k, x_{k+1}) \leq f(x_n) - f(x_m) \leq f(x_n).$$

由于 $f(x_n) \leq f(x_0) \leq \varepsilon$（注意 $\inf f = 0$），且对 $n \geq 1$，$f(x_n) \leq f(x_1) = f(x_0) \leq \varepsilon$，故
$$d(x_n, x_m) \leq \frac{\lambda}{\varepsilon} \cdot \frac{\varepsilon}{2^{n-1}} = \frac{\lambda}{2^{n-1}} \to 0.$$
（这里利用了 $c_n$ 的递归估计可得 $f(x_n) \to 0$，故 $d(x_n, x_m) \to 0$。）

更精确地，由 $x_{n+1} \in S_n$ 与 $c_n$ 的选取，
$$f(x_{n+1}) \leq c_n + \frac{\varepsilon}{\lambda 2^n} \leq f(x_{n+2}) + \frac{\varepsilon}{\lambda 2^n},$$
反复迭代可得 $f(x_n) \to 0$，进而 $\{x_n\}$ 是 Cauchy 列。

**步骤 4：取极限**

由 $(X, d)$ 完备，存在 $x_\varepsilon \in X$ 使 $x_n \to x_\varepsilon$。由 $f$ 下半连续，
$$f(x_\varepsilon) \leq \liminf_{n \to \infty} f(x_n) = 0 = \inf_X f \leq f(x_\varepsilon),$$
故 $f(x_\varepsilon) \leq f(x_0)$（因为 $f$ 单调下降且 $f(x_0) \geq f(x_\varepsilon)$）。

由 $d(x_0, x_\varepsilon) \leq \sum_n d(x_n, x_{n+1}) \leq \lambda$（求和），得 (ii)。

**步骤 5：变分不等式的证明**

设 $x \neq x_\varepsilon$，假设 $x \preccurlyeq x_\varepsilon$，即 $f(x) + \frac{\varepsilon}{\lambda} d(x_\varepsilon, x) \leq f(x_\varepsilon)$。由于 $d(x_\varepsilon, x) > 0$，故 $x \preccurlyeq x_n$ 对所有充分大的 $n$（由传递性与 $x \preccurlyeq x_\varepsilon \preccurlyeq x_n$），即 $x \in S_n$，故 $f(x) \geq c_n$，从而
$$f(x) + \frac{\varepsilon}{\lambda} d(x_\varepsilon, x) \leq f(x_\varepsilon) \leq c_n + \frac{\varepsilon}{\lambda 2^n},$$
取 $n \to \infty$，得 $f(x) + \frac{\varepsilon}{\lambda} d(x_\varepsilon, x) \leq f(x_\varepsilon) \leq f(x)$，与 $d(x_\varepsilon, x) > 0$ 矛盾。

故 $x \not\preccurlyeq x_\varepsilon$，即 $f(x) + \frac{\varepsilon}{\lambda} d(x, x_\varepsilon) > f(x_\varepsilon)$，这正是 (iii)。$\square$

**推论（近似临界点）**：若 $X$ 是 Banach 空间且 $f \in C^1$，对 $x \neq x_\varepsilon$ 令 $x = x_\varepsilon + t v$，$\|v\| = 1$，$t \to 0^+$，由变分不等式得
$$f'(x_\varepsilon)[v] \geq -\frac{\varepsilon}{\lambda}\|v\|,$$
对所有 $\|v\| = 1$ 成立，故 $\|f'(x_\varepsilon)\| \leq \varepsilon/\lambda$。

## 五、应用与意义

**理论意义**：

1. **无需紧性的变分原理**：Ekeland 原理仅依赖完备性与下半连续性，是替代紧致性条件的最基本工具。

2. **统一基础**：可推出 Caristi 不动点定理、Bishop-Phelps 定理、Banach 不动点定理等多个经典结果。

3. **近似临界点存在性**：在没有 (PS) 条件时，Ekeland 原理仍能保证近似临界点的存在，是临界点理论的"穷尽性"工具。

**应用领域**：

1. **山路引理的证明**：通过 Ekeland 原理在路径空间上构造近似临界点序列。

2. **Hamilton-Jacobi 方程**：用于证明粘性解的存在性与比较原理。

3. **最优控制**：在控制无紧性的最优控制问题中提供近似最优解的必要条件。

4. **非凸优化**：处理非凸、不可微优化问题的次梯度分析。

5. **非线性椭圆方程**：结合山路引理或直接应用，证明弱解的存在性。

**变体与推广**：
- **Caristi 不动点定理**：等价于 Ekeland 原理，给出完备度量空间上不动点的存在性。
- **Drop 定理**与 **Petal 定理**：几何形式的变分原理。
- **Deville-Godefroy-Zizler 变分原理**：在 Banach 空间中给出更精细的可微扰动形式。
- **Borwein-Preiss 变分原理**：使用光滑扰动函数的版本，便于在光滑空间中应用。
