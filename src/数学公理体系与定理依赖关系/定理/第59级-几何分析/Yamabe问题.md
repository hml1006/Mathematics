# Yamabe 问题

## 一、定理介绍

Yamabe 问题由日本数学家 Hidehiko Yamabe 于1960年提出，断言：在任意紧致 Riemann 流形上，存在与原度量共形且具有常标量曲率的度量。这一问题等价于在给定共形类中寻找使 Yamabe 泛函取最小值的度量，对应于一个半线性椭圆型偏微分方程的解。

Yamabe 本人在1960年给出了第一个证明尝试，但1968年 Trudinger 指出其证明中存在严重错误，并证明了在某些情形下 Yamabe 的结论成立。1976年 Aubin 证明：当流形不是局部共形平坦且维数 $n \geq 6$ 时，Yamabe 泛函的最小值严格小于 $\mathbb{S}^n$ 上对应的最小值，从而得到解的存在性。1984年 Schoen 完成了最后一步，他利用广义相对论中正质量定理（及其推广）处理了剩余情形（包括局部共形平坦流形和低维情形）。至此 Yamabe 问题圆满解决。

Yamabe 问题的解决是几何分析的标志性成果，深刻地联系了共形几何、变分法、临界 Sobolev 嵌入和正质量定理。它不仅给出了紧 Riemann 流形上的标准度量，还为后续的 Yamabe 流、Kazdan-Warner 恒等式、Nirenberg 问题等方向奠定了基础。

## 二、原理思路

**核心思想**：将共形类中度量的常标量曲率存在问题转化为 Yamabe 泛函极小化问题，通过变分法求解。

**关键要点**：

1. **共形变换下的标量曲率**：设 $\tilde{g} = u^{4/(n-2)} g$（$n \geq 3$），其中 $u > 0$ 是光滑函数。则 $\tilde{g}$ 的标量曲率 $\tilde{R}$ 为
$$\tilde{R} = u^{-\frac{n+2}{n-2}} \left(-\frac{4(n-1)}{n-2}\Delta_g u + R_g u\right).$$

2. **Yamabe 方程**：$\tilde{R} \equiv \lambda$（常数）等价于
$$-\frac{4(n-1)}{n-2}\Delta_g u + R_g u = \lambda u^{\frac{n+2}{n-2}}.$$
这是临界指数半线性椭圆方程。

3. **Yamabe 泛函**：定义
$$Q(M, g) = \frac{\int_M (a|\nabla u|^2 + R_g u^2) \, d\mathrm{vol}_g}{\left(\int_M u^{2n/(n-2)} \, d\mathrm{vol}_g\right)^{(n-2)/n}}, \quad a = \frac{4(n-1)}{n-2}.$$
Yamabe 常数 $Y(M, [g]) = \inf_u Q(M, g)$，下确界取遍所有 $u > 0$。

4. **Yamabe 不变量**：$\lambda(M) = \sup_{[g]} Y(M, [g])$ 是流形的微分不变量。

5. **变分策略**：
   - **Trudinger**：通过有界 $L^p$ 估计（$p < 2^* = 2n/(n-2)$）极小化 $Q$，取极限得到弱解；
   - **Aubin**：通过比较 $Y(M, [g])$ 与 $Y(\mathbb{S}^n, [g_0])$，证明当 $Y(M, [g]) < Y(\mathbb{S}^n, [g_0])$ 时极小化可达；
   - **Schoen**：在 $Y(M, [g]) = Y(\mathbb{S}^n, [g_0])$ 的临界情形下，利用正质量定理得到矛盾，从而 $Y(M, [g]) < Y(\mathbb{S}^n, [g_0])$ 总成立。

6. **Sobolev 嵌入的紧致性问题**：临界指数 $2^* = 2n/(n-2)$ 时 Sobolev 嵌入 $H^1 \hookrightarrow L^{2^*}$ 不紧，导致变分直接法失效。这是 Yamabe 问题难点的根源。

## 三、定理的严格表述

**定理（Yamabe 问题解决，Yamabe-Trudinger-Aubin-Schoen）**：设 $(M^n, g)$ 是紧致 Riemann 流形，$n \geq 3$。则在 $g$ 的共形类 $[g]$ 中存在度量 $\tilde{g}$，使 $\tilde{g}$ 的标量曲率 $\tilde{R}$ 为常数。

**定理（Yamabe 常数估计，Aubin 1976）**：
$$Y(M, [g]) \leq Y(\mathbb{S}^n, [g_{\mathrm{round}}]) = n(n-1)\omega_n^{2/n},$$
其中 $\omega_n = \mathrm{vol}(\mathbb{S}^n)$。若等号不成立，则 $Y(M, [g])$ 可被某光滑正函数 $u > 0$ 取到，$\tilde{g} = u^{4/(n-2)} g$ 即为 Yamabe 度量。

**定理（Schoen 1984）**：若 $(M, g)$ 不共形等价于标准球面 $(\mathbb{S}^n, g_{\mathrm{round}})$，则
$$Y(M, [g]) < Y(\mathbb{S}^n, [g_{\mathrm{round}}]).$$

**定理（局部共形平坦情形，Schoen）**：若 $(M, g)$ 是局部共形平坦且不共形等价于 $\mathbb{S}^n$，则 $Y(M, [g]) < Y(\mathbb{S}^n, [g_{\mathrm{round}}])$。证明利用到 $M$ 在 $\mathbb{S}^n$ 中的局部共形平坦嵌入及其在渐近平坦度量下的正质量定理。

**定理（Yamabe 流收敛，Brendle 2007）**：对任意紧 Riemann 流形上的初始度量，Yamabe 流（$\partial_t g = -R g$）当 $t \to \infty$ 时收敛到 Yamabe 度量，除非初始度量是局部共形平坦且具有正 Ricci 曲率（ Brendle 在2007年完成此例外情形的分析）。

## 四、证明过程

### 1. 共形变换公式推导

设 $\tilde{g} = u^{4/(n-2)} g$，$u > 0$ 光滑。直接计算 Christoffel 符号和曲率，得
$$\tilde{R} = u^{-\frac{n+2}{n-2}}\left(-\frac{4(n-1)}{n-2}\Delta_g u + R_g u\right).$$

$\tilde{R} \equiv \lambda$（常数）等价于
$$-\frac{4(n-1)}{n-2}\Delta_g u + R_g u = \lambda u^{\frac{n+2}{n-2}}. \quad (*)$$

### 2. Yamabe 泛函与变分

定义 Yamabe 商：
$$Q_g(u) = \frac{\int_M \left(\frac{4(n-1)}{n-2}|\nabla u|^2 + R_g u^2\right) d\mathrm{vol}_g}{\left(\int_M |u|^{2^*} d\mathrm{vol}_g\right)^{2/2^*}}, \quad 2^* = \frac{2n}{n-2}.$$

方程 $(*)$ 是 $Q_g$ 在 $L^{2^*}$ 约束下的 Euler-Lagrange 方程，$\lambda$ 是 Lagrange 乘子。Yamabe 常数
$$Y(M, [g]) = \inf_{u \neq 0} Q_g(u).$$

### 3. Trudinger 的有界性证明

**步骤 1**：用子临界泛函逼近。对 $p \in (2, 2^*)$，定义
$$Y_p(M, g) = \inf_{u \neq 0} \frac{\int_M \left(a|\nabla u|^2 + R_g u^2\right) d\mathrm{vol}_g}{\left(\int_M |u|^p d\mathrm{vol}_g\right)^{2/p}}.$$

**步骤 2**：子临界 Sobolev 嵌入 $H^1 \hookrightarrow L^p$ 紧（$p < 2^*$），由直接变分法 $Y_p$ 可被 $u_p > 0$ 取到。

**步骤 3**：取 $p \to 2^*$，得到 $u_p$ 的极限 $u$ 满足 $(*)$（弱解）。关键在于证明 $u \not\equiv 0$。

### 4. Aubin 的比较定理

Aubin 证明：通过选取局部爆破试验函数（test function）$u_\varepsilon$（集中在某点 $p$），可得
$$Y(M, [g]) \leq Y(\mathbb{S}^n, [g_{\mathrm{round}}]) + C\varepsilon^2(W_p(g)),$$
其中 $W_p(g)$ 是 $g$ 在 $p$ 处的 Weyl 张量（当 $n \geq 4$ 时）。

若 $g$ 不是局部共形平坦且 $n \geq 6$，则存在 $p$ 使 $W_p(g) \neq 0$ 且满足 Aubin 条件（梯度为零），从而 $Y(M, [g]) < Y(\mathbb{S}^n, [g_{\mathrm{round}}])$。

### 5. Schoen 的最后一步

**情形 1：$g$ 非局部共形平坦，$n \leq 5$**。Aubin 的 Weyl 张量方法失效。Schoen 构造更精细的试验函数，使其与 Green 函数的渐近展开匹配，得到
$$Y(M, [g]) < Y(\mathbb{S}^n, [g_{\mathrm{round}}]).$$

**情形 2：$g$ 局部共形平坦**。由 Schoen-Yau 的局部共形平坦嵌入定理，$(M, g)$ 可共形嵌入到 $\mathbb{S}^n$。在补集 $\mathbb{S}^n \setminus M$ 处的渐近平坦度量上应用正质量定理：
- 若 $Y(M, [g]) = Y(\mathbb{S}^n, [g_{\mathrm{round}}])$，则由试验函数极限得到的渐近平坦度量具有零 ADM 质量；
- 由正质量定理的刚性，该渐近平坦度量是 Euclid 度量；
- 这蕴含 $M = \mathbb{S}^n$ 的真开子集共形等价，矛盾。

因此 $Y(M, [g]) < Y(\mathbb{S}^n, [g_{\mathrm{round}}])$ 总成立。

### 6. 极小可达与正则性

由 $Y(M, [g]) < Y(\mathbb{S}^n, [g_{\mathrm{round}}])$，Trudinger 的子临界逼近的极限 $u$ 不恒为零。通过椭圆正则性理论，$u > 0$ 光滑，$\tilde{g} = u^{4/(n-2)} g$ 为 Yamabe 度量，$\tilde{R} \equiv \lambda$。$\square$

## 五、应用与意义

1. **共形几何**：Yamabe 问题给出了紧 Riemann 流形上共形类的标准代表，是共形微分几何的核心工具。

2. **Kazdan-Warner 恒等式**：与 Yamabe 问题密切相关，Kazdan-Warner 恒等式限制了哪些函数可作为 $\mathbb{S}^n$ 上 Riemann 度量的标量曲率。

3. **正质量定理的应用**：Schoen 的最后一步是正质量定理在共形几何中的首次重要应用，揭示了几何分析与广义相对论的深刻联系。

4. **Prescribed 标量曲率问题**：Yamabe 问题在 $\mathbb{S}^n$ 上的推广即 Nirenberg 问题：哪些函数可以是 $\mathbb{S}^n$ 上某共形度量的标量曲率。

5. **Yamabe 流与 Ricci 流**：Yamabe 流是 Ricci 流在共形类中的简化版本，其收敛性分析（Brendle, Schwetlick-Struwe）揭示了几何流的渐近行为。

6. **Kähler-Einstein 几何**：Yamabe 问题的复几何对应——Kähler-Einstein 度量存在性问题——是 Calabi 猜想与 Yau 定理的核心。

7. **共形不变量**：Yamabe 常数 $Y(M, [g])$ 是共形不变量，联系于共形 Laplacian 的第一特征值、热核渐近等。

8. **几何群论**：在无穷维共形群情形下，Yamabe 不变量用于分类紧流形的共形群。

Yamabe 问题以其简洁的陈述和深刻的解决过程，成为20世纪几何分析的标志性成就，展示了变分法、偏微分方程、共形几何和正质量定理等众多工具在几何研究中的精妙融合。
