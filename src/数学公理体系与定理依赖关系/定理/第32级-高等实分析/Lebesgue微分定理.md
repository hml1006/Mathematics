# Lebesgue微分定理

> **一句话大白话**：几乎处处地，函数在一点的值就等于"越缩越小的球里函数平均值"的极限——微分与积分的"互逆"在小球不断坍缩的意义上处处几乎都成立。
>
> **小例子**：对 $f\in L^1_{\mathrm{loc}}$，几乎对每个点 $x$ 有 $\lim_{r\to0}\frac{1}{|B_r(x)|}\int_{B_r(x)}f\,dy=f(x)$；例如常值 $f$ 显然成立，跳跃函数在可数零点外也都满足。

## 介绍

Lebesgue微分定理是实分析中最基本的定理之一，它断言：局部可积函数 $f$ 在几乎每点处的球平均收敛到该点的函数值。换言之，对于 $f \in L^1_{\text{loc}}(\mathbb{R}^n)$，几乎每个 $x \in \mathbb{R}^n$ 都是 $f$ 的 Lebesgue 点，满足

$$
\lim_{r \to 0} \frac{1}{|B(x, r)|} \int_{B(x, r)} f(y) \, dy = f(x).
$$

这个定理统一了微积分中"平均值趋于函数值"的直观，是 Lebesgue 积分理论相对于 Riemann 积分的重大优势之一，也是调和分析、偏微分方程和概率论中许多基本结果的基础。

## 分析

**前置依赖**：Hardy-Littlewood 极大不等式、$C_c(\mathbb{R}^n)$ 在 $L^1$ 中的稠密性、局部可积函数、几乎处处收敛

**定理的精确表述**：设 $f \in L^1_{\text{loc}}(\mathbb{R}^n)$。则对 Lebesgue 几乎所有的 $x \in \mathbb{R}^n$，

$$
\lim_{r \to 0} \frac{1}{|B(x, r)|} \int_{B(x, r)} f(y) \, dy = f(x).
$$

更一般地，若 $f \in L^1_{\text{loc}}(\mathbb{R}^n)$，则几乎每个 $x$ 都是 $f$ 的 Lebesgue 点，即

$$
\lim_{r \to 0} \frac{1}{|B(x, r)|} \int_{B(x, r)} |f(y) - f(x)| \, dy = 0.
$$

**关键要点**：

- 极限是逐点几乎处处收敛，不是一致收敛。
- 对 $f \in L^p$（$1 \le p \le \infty$）也有同样的结论（因为 $L^p \subset L^1_{\text{loc}}$）。
- 定理表明，在几乎每个点处，$f$ 的局部平均可以任意接近 $f$ 在该点的值。
- 这个定理不适用于 Riemann 积分——Riemann 可积函数可以在一个正测度集上不连续，此时微分定理不成立。

## 思考过程

Lebesgue 微分定理的证明基于 Hardy-Littlewood 极大不等式和密度论证：

1. **定义极大函数**：$M f(x) = \sup_{r>0} \frac{1}{|B(x,r)|} \int_{B(x,r)} |f(y)| dy$。

2. **考虑上极限**：定义 $\Omega f(x) = \limsup_{r \to 0} \frac{1}{|B(x,r)|} \int_{B(x,r)} f(y) dy - \liminf_{r \to 0} \frac{1}{|B(x,r)|} \int_{B(x,r)} f(y) dy$。

3. **证明 $\Omega f = 0$ 几乎处处**：对任意 $\varepsilon > 0$，考虑集合 $\{x \mid \Omega f(x) > \varepsilon\}$，利用 $C_c(\mathbb{R}^n)$ 在 $L^1$ 中的稠密性和 Hardy-Littlewood 极大不等式证明其测度为零。

4. **Lebesgue 点**：进一步证明 $\lim_{r \to 0} \frac{1}{|B(x,r)|} \int_{B(x,r)} |f(y) - f(x)| dy = 0$ 几乎处处成立。

## 证明过程

**证明**：我们分几步证明 Lebesgue 微分定理。

**步骤 1**：对连续函数 $g \in C_c(\mathbb{R}^n)$，定理显然成立——对任意 $x$，

$$
\lim_{r \to 0} \frac{1}{|B(x, r)|} \int_{B(x, r)} g(y) \, dy = g(x).
$$

这是连续函数的平均值的标准性质。

**步骤 2**：定义上极限算子。对任意局部可积函数 $f$，定义

$$
T_r f(x) = \frac{1}{|B(x, r)|} \int_{B(x, r)} f(y) \, dy,
$$
$$
T^* f(x) = \limsup_{r \to 0} T_r f(x), \quad T_* f(x) = \liminf_{r \to 0} T_r f(x).
$$

需要证明 $T^* f = T_* f = f$ 几乎处处成立。

**步骤 3**：对任意 $\varepsilon, \delta > 0$，令 $E_{\varepsilon, \delta} = \{x \mid T^* f(x) - T_* f(x) > \varepsilon, \text{且 } |f(x)| \le 1/\delta\}$。我们证明 $|E_{\varepsilon, \delta}| = 0$。

取 $g \in C_c(\mathbb{R}^n)$ 使得 $\|f - g\|_{L^1} < \varepsilon \delta / 5^n$。则 $f = g + (f - g)$。由于 $T^* g = T_* g = g$（连续函数情形），

$$
T^* f - T_* f \le T^*(f - g) - T_*(f - g) \le 2 M(f - g)(x),
$$

其中 $M$ 是 Hardy-Littlewood 极大函数。

若 $x \in E_{\varepsilon, \delta}$，则 $M(f - g)(x) > \varepsilon/2$。由 Hardy-Littlewood 极大不等式，

$$
|E_{\varepsilon, \delta}| \le |\{M(f - g) > \varepsilon/2\}| \le \frac{2 \cdot 5^n}{\varepsilon} \|f - g\|_{L^1} < 2\delta.
$$

由于 $\delta$ 任意小，$|E_{\varepsilon, \delta}| = 0$。令 $\varepsilon \to 0$ 得 $T^* f = T_* f$ 几乎处处成立。

**步骤 4**：证明极限等于 $f$。考虑 $F = \{x \mid \lim_{r \to 0} T_r f(x) \neq f(x)\}$。对任意 $k \in \mathbb{N}$，令 $f_k(x) = \max(-k, \min(k, f(x)))$，则 $f_k$ 有界。由步骤 3，$\lim_{r \to 0} T_r f_k(x)$ 几乎处处存在，记为 $L_k(x)$。由 $L^1$ 收敛，可证 $L_k = f_k$ 几乎处处。再由 $k \to \infty$ 得到 $\lim_{r \to 0} T_r f = f$ 几乎处处。

**步骤 5**：Lebesgue 点。对 $f \in L^1_{\text{loc}}$，考虑函数 $h(y) = |f(y) - f(x)|$，对固定的 $x$ 应用微分定理得

$$
\lim_{r \to 0} \frac{1}{|B(x, r)|} \int_{B(x, r)} |f(y) - f(x)| \, dy = 0
$$

对几乎所有的 $x$ 成立。$\square$

**推论**：若 $f \in L^1_{\text{loc}}(\mathbb{R}^n)$ 且对几乎每个 $x$，$\int_{B(x,r)} f = 0$ 对所有 $r > 0$ 成立，则 $f = 0$ 几乎处处成立。

**应用**：Lebesgue 微分定理是测度论中"密度"概念的基础，在分形几何中用于定义点态维数，在偏微分方程中用于建立弱解的正则性。