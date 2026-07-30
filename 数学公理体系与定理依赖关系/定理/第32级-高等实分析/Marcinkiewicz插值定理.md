# Marcinkiewicz插值定理

## 介绍

Marcinkiewicz插值定理是调和分析和泛函分析中的基本工具，由 Józef Marcinkiewicz 在 1939 年提出。它断言：如果一个次线性算子同时满足弱 $(p_0, p_0)$ 型和弱 $(p_1, p_1)$ 型（$1 \le p_0 < p_1 \le \infty$），则它对所有 $p \in (p_0, p_1)$ 都是强 $(p, p)$ 型（即 $L^p$ 有界）。这个定理是从较弱的估计（分布函数估计）推导出较强的估计（范数估计）的有力工具，在奇异积分理论、Fourier 分析和偏微分方程中有广泛应用。

## 分析

**定理的精确表述**：设 $(X, \mu)$ 和 $(Y, \nu)$ 是测度空间，$T$ 是定义在 $L^{p_0}(X) + L^{p_1}(X)$ 上的次线性算子（即 $|T(f + g)| \le |T f| + |T g|$）。假设 $T$ 满足：

- **弱 $(p_0, p_0)$ 型**：存在 $A_0 > 0$ 使得 $\nu(\{y \mid |T f(y)| > \alpha\}) \le \left( \frac{A_0}{\alpha} \|f\|_{p_0} \right)^{p_0}$ 对所有 $\alpha > 0$ 和 $f \in L^{p_0}$ 成立；
- **弱 $(p_1, p_1)$ 型**：存在 $A_1 > 0$ 使得 $\nu(\{y \mid |T f(y)| > \alpha\}) \le \left( \frac{A_1}{\alpha} \|f\|_{p_1} \right)^{p_1}$ 对所有 $\alpha > 0$ 和 $f \in L^{p_1}$ 成立。

则对任意 $p \in (p_0, p_1)$，$T$ 是强 $(p, p)$ 型，即存在 $C_p > 0$ 使得

$$
\|T f\|_{L^p(Y)} \le C_p \|f\|_{L^p(X)}, \quad \forall f \in L^p(X).
$$

**关键要点**：

- 次线性条件（$|T(f+g)| \le |Tf| + |Tg|$）是必要的，它比线性条件弱。
- 弱 $(p, p)$ 型等价于 $T$ 从 $L^p$ 到 $L^{p,\infty}$（弱 $L^p$ 空间）的有界性。
- $p_0$ 和 $p_1$ 可以取 $1 \le p_0 < p_1 \le \infty$，但当 $p_1 = \infty$ 时，弱 $(\infty, \infty)$ 型就是强 $(\infty, \infty)$ 型（即 $L^\infty$ 有界）。
- $T$ 只需定义在 $L^{p_0} + L^{p_1}$ 上（即可以表示为 $L^{p_0}$ 和 $L^{p_1}$ 中函数的和）。

## 思考过程

Marcinkiewicz 插值定理的证明基于对函数 $f$ 的分解和分布函数的积分表示：

1. **分布函数积分公式**：$\|T f\|_p^p = p \int_0^\infty \alpha^{p-1} \nu(\{y \mid |T f(y)| > \alpha\}) \, d\alpha$。

2. **函数分解**：对每个 $\alpha > 0$，将 $f$ 分解为"大"部分 $f^\alpha = f \cdot \chi_{\{|f| > \delta \alpha\}}$ 和"小"部分 $f_\alpha = f - f^\alpha$，其中 $\delta$ 是待定参数。

3. **分别估计**：$T f$ 的分布函数由 $T f^\alpha$ 和 $T f_\alpha$ 的分布函数控制。对 $f^\alpha$ 使用弱 $(p_0, p_0)$ 型估计，对 $f_\alpha$ 使用弱 $(p_1, p_1)$ 型估计（或反过来，根据 $p$ 相对于 $p_0, p_1$ 的位置）。

4. **积分计算**：将分布函数估计代入积分公式，计算得到 $\|T f\|_p \le C_p \|f\|_p$。

## 证明过程

**证明**：设 $T$ 满足弱 $(p_0, p_0)$ 型和弱 $(p_1, p_1)$ 型条件，常数分别为 $A_0$ 和 $A_1$。取 $p \in (p_0, p_1)$。

**步骤 1**：分布函数表示。对任意 $f \in L^p$，

$$
\|T f\|_p^p = p \int_0^\infty \alpha^{p-1} \nu(\{y \mid |T f(y)| > \alpha\}) \, d\alpha.
$$

**步骤 2**：函数分解。对每个 $\alpha > 0$，取 $\delta > 0$（待定），定义

$$
f^\alpha(x) = f(x) \cdot \chi_{\{|f(x)| > \delta \alpha\}}(x), \quad f_\alpha(x) = f(x) \cdot \chi_{\{|f(x)| \le \delta \alpha\}}(x).
$$

则 $f = f^\alpha + f_\alpha$。由次线性性，$|T f| \le |T f^\alpha| + |T f_\alpha|$，故

$$
\{|T f| > \alpha\} \subset \{|T f^\alpha| > \alpha/2\} \cup \{|T f_\alpha| > \alpha/2\}.
$$

因此

$$
\nu(\{|T f| > \alpha\}) \le \nu(\{|T f^\alpha| > \alpha/2\}) + \nu(\{|T f_\alpha| > \alpha/2\}).
$$

**步骤 3**：应用弱型估计。假设 $p_1 < \infty$。对 $f^\alpha$ 使用弱 $(p_0, p_0)$ 型，对 $f_\alpha$ 使用弱 $(p_1, p_1)$ 型：

$$
\nu(\{|T f^\alpha| > \alpha/2\}) \le \left( \frac{2A_0}{\alpha} \|f^\alpha\|_{p_0} \right)^{p_0},
$$
$$
\nu(\{|T f_\alpha| > \alpha/2\}) \le \left( \frac{2A_1}{\alpha} \|f_\alpha\|_{p_1} \right)^{p_1}.
$$

**步骤 4**：范数计算。$\|f^\alpha\|_{p_0}^{p_0} = \int_{\{|f| > \delta \alpha\}} |f|^{p_0} \, d\mu$，$\|f_\alpha\|_{p_1}^{p_1} = \int_{\{|f| \le \delta \alpha\}} |f|^{p_1} \, d\mu$。

代入积分公式：

$$
\|T f\|_p^p \le p \int_0^\infty \alpha^{p-1} \left[ \left( \frac{2A_0}{\alpha} \right)^{p_0} \int_{\{|f| > \delta \alpha\}} |f|^{p_0} + \left( \frac{2A_1}{\alpha} \right)^{p_1} \int_{\{|f| \le \delta \alpha\}} |f|^{p_1} \right] d\alpha.
$$

**步骤 5**：交换积分次序。由 Fubini-Tonelli 定理，

$$
\int_0^\infty \alpha^{p-p_0-1} \int_{\{|f| > \delta \alpha\}} |f|^{p_0} \, d\mu \, d\alpha = \int_X |f|^{p_0} \int_0^{|f|/\delta} \alpha^{p-p_0-1} \, d\alpha \, d\mu = \frac{\delta^{-(p-p_0)}}{p-p_0} \|f\|_p^p.
$$

类似地，

$$
\int_0^\infty \alpha^{p-p_1-1} \int_{\{|f| \le \delta \alpha\}} |f|^{p_1} \, d\mu \, d\alpha = \int_X |f|^{p_1} \int_{|f|/\delta}^\infty \alpha^{p-p_1-1} \, d\alpha \, d\mu = \frac{\delta^{-(p-p_1)}}{p_1-p} \|f\|_p^p.
$$

**步骤 6**：合并估计。代入得

$$
\|T f\|_p^p \le p \left[ (2A_0)^{p_0} \frac{\delta^{-(p-p_0)}}{p-p_0} + (2A_1)^{p_1} \frac{\delta^{-(p-p_1)}}{p_1-p} \right] \|f\|_p^p.
$$

选择适当的 $\delta$（例如令两项相等）即可得到 $\|T f\|_p \le C_p \|f\|_p$。$\square$

**注**：当 $p_1 = \infty$ 时，弱 $(\infty, \infty)$ 型就是 $\|T f\|_\infty \le A_1 \|f\|_\infty$，证明中相应部分需做调整，结论同样成立。

**应用**：Hardy-Littlewood 极大算子的 $L^p$ 有界性（$p > 1$）可由其弱 $(1,1)$ 型和 $L^\infty$ 有界性通过 Marcinkiewicz 插值得到。