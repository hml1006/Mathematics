# Hardy 空间 $H^p$ 理论

## 一、定理介绍

Hardy 空间 $H^p$ 是调和分析中一类重要的函数空间，最初由 G.H. Hardy 在 1915 年研究 Fourier 级数和解析函数时引入。在单位圆盘（或上半平面）上，$H^p$ 空间由满足一致有界条件的解析函数组成。在 $\mathbb{R}^n$ 上，Stein 和 Weiss 在 1960 年代将 Hardy 空间推广到高维实变量情形，建立了实变量 Hardy 空间理论。

Hardy 空间的核心意义在于：当 $p \le 1$ 时，$L^p$ 空间的许多分析工具失效（如 $L^p$ 的对偶空间不好描述，奇异积分算子在 $L^1$ 上无界），而 $H^p$ 空间提供了一个完美的替代框架。特别是 $H^1$ 是 $L^1$ 的适当替代——奇异积分算子在 $H^1$ 上有界，且 $H^1$ 的对偶空间是 BMO 空间。这一理论深刻联系了复分析、调和分析、偏微分方程和概率论。

## 二、原理思路

**经典 Hardy 空间（单位圆盘上）**：

在单位圆盘 $\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$ 上，$H^p(\mathbb{D})$ 由满足
$$\sup_{0 < r < 1} \left(\int_0^{2\pi} |F(re^{i\theta})|^p\, d\theta\right)^{1/p} < \infty$$
的解析函数 $F$ 组成。当 $p > 0$ 时，边界值 $F(e^{i\theta}) = \lim_{r \to 1} F(re^{i\theta})$ 几乎处处存在且属于 $L^p(\mathbb{T})$。

**实变量 Hardy 空间（$\mathbb{R}^n$ 上）**：

在 $\mathbb{R}^n$ 上，没有解析函数可用。Stein-Weiss 的定义利用调和函数：$f \in H^p(\mathbb{R}^n)$ 如果 $f$ 是某个调和函数向量 $(u_0, u_1, \ldots, u_N)$ 的第一个分量，其中 $u_0(x,t) = P_t * f(x)$（Poisson 积分），且
$$\sup_{t > 0} \left(\int_{\mathbb{R}^n} \left(\sum_{j=0}^N |u_j(x,t)|^2\right)^{p/2}\, dx\right)^{1/p} < \infty.$$

**Fefferman-Stein 的极大函数刻画**：

更实用的定义利用极大函数。定义非切向极大函数
$$\mathcal{N}f(x) = \sup_{|y-x|<t} |P_t * f(y)|,$$
则 $f \in H^p(\mathbb{R}^n)$ 当且仅当 $\mathcal{N}f \in L^p(\mathbb{R}^n)$。

**原子分解——核心工具**：

Hardy 空间理论最强大的工具是原子分解。$H^p$（$0 < p \le 1$）中的每个元素可以分解为 $p$-原子的级数：
$$f = \sum_j \lambda_j a_j,$$
其中每个 $a_j$ 是 $p$-原子（支在某方体 $Q_j$ 上，$L^\infty$ 有界，且满足消去条件 $\int x^\alpha a_j(x)\, dx = 0$ 对 $|\alpha| \le n(1/p - 1)$），$\sum |\lambda_j|^p < \infty$。

**关键洞察**：原子的消去条件补偿了 $L^p$（$p < 1$）中函数可能有的"振荡不足"，使得奇异积分算子可以作用在 $H^p$ 上。

## 三、定理的严格表述

**定义（实变量 Hardy 空间）**：设 $0 < p \le \infty$。$H^p(\mathbb{R}^n)$ 定义为所有 tempered distribution $f \in \mathcal{S}'(\mathbb{R}^n)$ 的集合，使得其非切向极大函数
$$\mathcal{N}f(x) = \sup_{|y-x|<t} |\Phi_t * f(y)| \in L^p(\mathbb{R}^n),$$
其中 $\Phi \in \mathcal{S}(\mathbb{R}^n)$ 满足 $\int \Phi \ne 0$，$\Phi_t(x) = t^{-n}\Phi(x/t)$。$H^p$ 的（拟）范数为 $\|f\|_{H^p} = \|\mathcal{N}f\|_{L^p}$。

**定理 1（原子分解定理）**：设 $0 < p \le 1$，$s \ge [n(1/p - 1)]$ 为整数。称可测函数 $a$ 是一个 $(p, \infty, s)$-原子，如果存在方体 $Q$ 使得：
- $\text{supp}(a) \subset Q$；
- $\|a\|_{L^\infty} \le |Q|^{-1/p}$；
- $\int_Q x^\alpha a(x)\, dx = 0$ 对所有 $|\alpha| \le s$。

则 $f \in H^p(\mathbb{R}^n)$ 当且仅当存在 $(p, \infty, s)$-原子 $\{a_j\}$ 和系数 $\{\lambda_j\}$ 使得
$$f = \sum_j \lambda_j a_j \quad (\text{在 } \mathcal{S}' \text{ 中收敛}),$$
且 $\sum_j |\lambda_j|^p < \infty$。此外，
$$\|f\|_{H^p} \sim \inf\left\{\left(\sum_j |\lambda_j|^p\right)^{1/p} : f = \sum_j \lambda_j a_j\right\}.$$

**定理 2（$H^1$-$BMO$ 对偶性，Fefferman 定理）**：
$$(H^1(\mathbb{R}^n))^* \cong BMO(\mathbb{R}^n).$$

更精确地，每个 $BMO$ 函数 $b$ 通过 $\ell(f) = \int_{\mathbb{R}^n} f(x)b(x)\,dx$ 定义 $H^1$ 上的连续线性泛函，且 $\|\ell\|_{(H^1)^*} \sim \|b\|_{BMO}$。

**定理 3（奇异积分算子在 $H^p$ 上的有界性）**：设 $T$ 是 Calderón-Zygmund 奇异积分算子，$0 < p \le 1$，$s \ge [n(1/p - 1)]$。若 $T$ 将每个 $(p, 2, s)$-原子映射到 $L^p$ 中（一致有界），则 $T$ 可以延拓为 $H^p \to L^p$ 的有界算子（当 $p < 1$）或 $H^1 \to L^1$ 的有界算子（当 $p = 1$）。

**定理 4（$H^p$ 与 $L^p$ 的关系）**：
- 当 $p > 1$ 时，$H^p(\mathbb{R}^n) = L^p(\mathbb{R}^n)$（等价范数）。
- 当 $p = 1$ 时，$H^1(\mathbb{R}^n) \subsetneq L^1(\mathbb{R}^n)$（真子空间）。
- 当 $p < 1$ 时，$H^p(\mathbb{R}^n) \subset L^p(\mathbb{R}^n)$ 不再成立，但 $H^p \subset \mathcal{S}'$。

## 四、证明过程

**原子分解定理的证明概要**：

**充分性**（原子级数属于 $H^p$）：设 $f = \sum \lambda_j a_j$。对每个原子 $a_j$，支在方体 $Q_j$ 上，利用消去条件和 Poisson 核的光滑性，可以证明
$$\|\mathcal{N}a_j\|_{L^p}^p \le C,$$
其中 $C$ 与原子无关。关键在于：对 $x$ 远离 $Q_j$ 时，消去条件使得 $P_t * a_j(x)$ 快速衰减；对 $x$ 靠近 $Q_j$ 时，利用 $L^\infty$ 界。

因此 $\|\mathcal{N}f\|_{L^p}^p \le C \sum |\lambda_j|^p$。

**必要性**（$H^p$ 函数可分解为原子）：这是较深的部分。核心思想是利用 Calderón-Zygmund 分解的变体。

给定 $f \in H^p$，考虑其极大函数 $\mathcal{N}f \in L^p$。对每个 $\lambda > 0$，令 $\Omega_\lambda = \{x : \mathcal{N}f(x) > \lambda\}$。在 $\Omega_\lambda$ 上作 Whitney 分解 $\{Q_j\}$，然后构造原子分解。

具体地，选取光滑函数 $\varphi$ 满足 $\int \varphi = 1$，令 $\varphi_t(x) = t^{-n}\varphi(x/t)$。定义
$$f(x) = \int_0^\infty \varphi_t * f(x) \frac{dt}{t} \quad (\text{在 } \mathcal{S}' \text{ 中}).$$

将积分区域按 $\mathcal{N}f$ 的大小分层，每层构造一个原子。详细过程涉及精细的 Calderón-Zygmund 型分解。$\square$

**$H^1$-$BMO$ 对偶性的证明概要**：

**$BMO \hookrightarrow (H^1)^*$**：设 $b \in BMO$，$f \in H^1$。将 $f$ 作原子分解 $f = \sum \lambda_j a_j$。对每个原子 $a$（支在 $Q$ 上，$\int a = 0$），
$$\left|\int a(x)b(x)\,dx\right| = \left|\int a(x)(b(x) - b_Q)\,dx\right| \le \|a\|_{L^\infty} \int_Q |b - b_Q| \le C\|b\|_{BMO}.$$

因此 $|\ell(f)| \le C\|b\|_{BMO} \sum |\lambda_j| \sim C\|b\|_{BMO}\|f\|_{H^1}$。

**$(H^1)^* \hookrightarrow BMO$**：反向证明利用 $H^1$ 中原子的特殊结构。对任意方体 $Q$ 和 $|g| \le 1$ 支在 $Q$ 上、$\int g = 0$ 的函数 $g$，$g$ 是 $H^1$ 原子（差常数）。由 $(H^1)^*$ 中的泛函 $\ell$，得 $|\ell(g)| \le C\|\ell\|$。取 $g$ 适当逼近 $\text{sgn}(b - b_Q)\chi_Q$，可推出 $\frac{1}{|Q|}\int_Q |b - b_Q| \le C\|\ell\|$。$\square$

## 五、应用与意义

1. **奇异积分算子的正确框架**：$H^1$ 是使得 Calderón-Zygmund 算子有界的 $L^1$ 的替代空间。Riesz 变换 $R_j: H^1 \to L^1$ 有界，而 $R_j: L^1 \to L^1$ 无界。

2. **偏微分方程**：在椭圆方程 $\Delta u = f$ 中，若 $f \in H^1$ 而非仅 $L^1$，则解的二阶导数属于 $L^1$（Stein 定理）。这在流体力学（Euler 方程的涡度方法）中有重要应用。

3. **复分析的联系**：在一维情形，$H^p(\mathbb{R})$ 可以刻画为边界值属于 $L^p$ 且 Fourier 变换支在 $[0,\infty)$ 上的函数，与上半平面的解析函数一一对应。

4. **多线性调和分析**：$H^p$ 理论的多线性推广在乘积估计和 PDE 中有重要应用。

5. **几何测度论**：Hardy 空间与补偿紧致性（compensated compactness）理论密切相关。Müller 和 Coifman 证明了某些非线性微分表达式（如 Jacobian）自动属于 $H^1$，这比 $L^1$ 估计更强。

6. **概率论**：通过鞅论方法，Hardy 空间可以与随机过程的极大函数联系起来，为概率论和分析学之间建立桥梁。
