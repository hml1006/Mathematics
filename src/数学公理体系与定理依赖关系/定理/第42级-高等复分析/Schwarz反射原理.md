# Schwarz 反射原理

## 介绍

Schwarz 反射原理（Schwarz reflection principle）是复分析中的基本定理，由 Hermann Schwarz 建立。该原理断言，一个在实轴上半平面解析且取实值的函数可以解析延拓到下半平面，延拓方式为 $f(\bar{z}) = \overline{f(z)}$。该原理是解析延拓理论中的经典工具，广泛应用于共形映射、边界值问题和特殊函数理论中。

## 分析

**前置依赖**：全纯函数、解析延拓、Cauchy 积分公式、唯一性定理。

**定理内容**：设 $\Omega^+ \subset \mathbb{C}^+$ 是上半平面中的开集，且 $\Omega^+$ 的边界包含实轴上的一个开区间 $I$。若 $f$ 在 $\Omega^+$ 上全纯，且对每个 $x \in I$，$\lim_{z \to x, \operatorname{Im}z > 0} f(z)$ 存在且为实数，则 $f$ 可解析延拓到 $\Omega = \Omega^+ \cup I \cup \overline{\Omega^+}$，延拓后的函数定义为
$$F(z) = \begin{cases}
f(z), & z \in \Omega^+ \\
\overline{f(\bar{z})}, & z \in \overline{\Omega^+}
\end{cases}$$
其中 $\overline{\Omega^+} = \{\bar{z} \mid z \in \Omega^+\}$。

**一般形式**：若 $\gamma$ 是解析弧，$f$ 在 $\gamma$ 的一侧解析且将 $\gamma$ 映射到另一条解析弧，则 $f$ 可穿越 $\gamma$ 延拓。

**数学内涵**：Schwarz 反射原理体现了复分析中"对称性"的深刻内涵——函数在边界上的实值性导致其关于实轴共轭对称。这种对称性可以推广到更一般的解析弧和共形映射。

**证明策略**：定义 $F$ 如上述，然后验证 $F$ 在 $\Omega$ 上全纯。在 $\Omega^+$ 和 $\overline{\Omega^+}$ 上全纯是显然的，在实轴上的点通过 Morera 定理或 Cauchy 积分公式验证全纯性。

## 思考过程

Schwarz 反射原理的证明思路很直接：先定义延拓后的函数 $F$，然后证明 $F$ 在实轴上的点处全纯。关键在于，对实轴上的点 $x_0$，考虑一个包含 $x_0$ 的小圆盘，将圆盘分为上下两部分，在上下两部分分别用 $f$ 和 $\overline{f(\bar{z})}$ 定义，然后证明 $F$ 在 $x_0$ 处解析。

这可以通过 Cauchy 积分公式或 Morera 定理来证明。利用 $f$ 在实轴上取实值的条件，可以证明 $F$ 在实轴上的积分沿着小三角形的路径为零，从而由 Morera 定理得 $F$ 全纯。

## 证明过程

**定理**（Schwarz 反射原理）：设 $\Omega^+ \subset \mathbb{C}^+$ 是区域，$I \subset \partial\Omega^+ \cap \mathbb{R}$ 是开区间。若 $f: \Omega^+ \cup I \to \mathbb{C}$ 满足：
1. $f$ 在 $\Omega^+$ 上全纯。
2. 对每个 $x \in I$，$f(x) = \lim_{z \to x, \operatorname{Im}z>0} f(z) \in \mathbb{R}$。
则 $f$ 可解析延拓到 $\Omega = \Omega^+ \cup I \cup \overline{\Omega^+}$。

**证明**：

**步骤 1**：定义延拓。设 $\Omega^- = \{\bar{z} \mid z \in \Omega^+\}$，定义
$$F(z) = \begin{cases}
f(z), & z \in \Omega^+ \cup I \\
\overline{f(\bar{z})}, & z \in \Omega^-
\end{cases}$$

**步骤 2**：$F$ 在 $\Omega^+$ 上全纯是已知的。在 $\Omega^-$ 上，令 $g(z) = \overline{f(\bar{z})}$。由于 $z \mapsto \bar{z}$ 是反全纯映射，且 $f$ 全纯，$g$ 是 $\Omega^-$ 上的全纯函数。

**步骤 3**：在 $I$ 上全纯。取 $x_0 \in I$，存在 $\varepsilon > 0$ 使得 $D(x_0, \varepsilon) \subset \Omega$。对 $D(x_0, \varepsilon)$ 中的任意三角形 $\Delta$，若 $\Delta$ 完全在 $\Omega^+ \cup I$ 或 $\Omega^- \cup I$ 中，则 $\int_\Delta F = 0$ 由 Cauchy 定理保证。

**步骤 4**：若 $\Delta$ 跨越实轴，将 $\Delta$ 分为上下两部分 $\Delta^+$ 和 $\Delta^-$。由 $F$ 在 $I$ 上的连续性，积分沿实轴部分的贡献相互抵消，故
$$\int_\Delta F = \int_{\Delta^+} f + \int_{\Delta^-} \overline{f(\bar{z})} = 0$$
由 Morera 定理，$F$ 在 $x_0$ 处全纯。

**步骤 5**：由唯一性定理，$F$ 是 $f$ 在 $\Omega$ 上的解析延拓。$\square$

**推论**（共形映射的边界延拓）：若 $f$ 将上半平面共形映射到某区域，且将实轴映射到实轴，则 $f$ 可延拓为整个复平面上的亚纯函数。